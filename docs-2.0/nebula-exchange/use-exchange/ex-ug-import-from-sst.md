# 导入SST文件数据

本文以一个示例说明如何将数据源的数据生成SST（Sorted String Table）文件并保存在HDFS上，然后导入Nebula Graph，示例数据源是CSV文件。

> **说明**：仅Linux系统支持导入SST文件。

## 背景信息

Exchange支持两种数据导入模式：

- 直接将数据源的数据通过**nGQL**语句的形式导入Nebula Graph。

- 将数据源的数据生成SST文件，然后借助Console将SST文件导入Nebula Graph。

下文将介绍生成SST文件并用其导入数据的适用场景、实现方法、前提条件、操作步骤等内容。

## 适用场景

- 适合在线业务，因为生成时几乎不会影响业务（只是读取Schema），导入速度快。

  !!! caution
  
        虽然导入速度快，但是导入期间（大约10秒）会阻塞对应空间的写操作，建议在业务低峰期进行导入。

- 适合数据源数据量较大的场景，导入速度快。

## 实现方法

Nebula Graph底层使用RocksDB作为键值型存储引擎。RocksDB是基于硬盘的存储引擎，提供了一系列API用于创建及导入SST格式的文件，有助于快速导入海量数据。

SST文件是一个内部包含了任意长度的有序键值对集合的文件，用于高效地存储大量键值型数据。生成SST文件的整个过程主要由Exchange的Reader、sstProcessor和sstWriter完成。整个数据处理过程如下：

1. Reader从数据源中读取数据。

2. sstProcessor根据Nebula Graph的Schema信息生成SST文件，然后上传至HDFS。SST文件的格式请参见[数据存储格式](../../1.introduction/3.nebula-graph-architecture/4.storage-service.md)。

3. sstWriter打开一个文件并插入数据。生成SST文件时，Key必须按照顺序写入。

4. 生成SST文件之后，RocksDB通过`IngestExternalFile()`方法将SST文件导入到Nebula Graph中。例如：

  ```
  IngestExternalFileOptions ifo;
  # 导入两个SST文件
  Status s = db_->IngestExternalFile({"/home/usr/file1.sst", "/home/usr/file2.sst"}, ifo);
  if (!s.ok()) {
    printf("Error while adding file %s and %s, Error %s\n",
           file_path1.c_str(), file_path2.c_str(), s.ToString().c_str());
    return 1;
  }
  ```

  调用`IngestExternalFile()`方法时，RocksDB默认会将文件拷贝到数据目录，并且阻塞RocksDB写入操作。如果SST文件中的键范围覆盖了Memtable键的范围，则将Memtable落盘（flush）到硬盘。将SST文件放置在LSM树最优位置后，为文件分配一个全局序列号，并打开写操作。

## 数据集

本文以[basketballplayer数据集](https://docs-cdn.nebula-graph.com.cn/dataset/dataset.zip)为例。

## 环境配置

本文示例在MacOS下完成，以下是相关的环境配置信息：

- 硬件规格：
  - CPU：1.7 GHz Quad-Core Intel Core i7
  - 内存：16 GB

- Spark：2.4.7 单机版

- Hadoop：2.9.2 伪分布式部署

- Nebula Graph：{{nebula.release}}。

## 前提条件

开始导入数据之前，用户需要确认以下信息：

- 已经[安装部署Nebula Graph {{nebula.release}}](../../4.deployment-and-installation/2.compile-and-install-nebula-graph/2.install-nebula-graph-by-rpm-or-deb.md)并获取如下信息：

  - Graph服务和Meta服务的的IP地址和端口。

  - 拥有Nebula Graph写权限的用户名和密码。

  - Meta服务配置文件中的`--ws_storage_http_port`和Storage服务配置文件中的`--ws_http_port`一致。例如都为`19779`。

  - Graph服务配置文件中的`--ws_meta_http_port`和Meta服务配置文件中的`--ws_http_port`一致。例如都为`19559`。

  - Schema的信息，包括Tag和Edge type的名称、属性等。

- 已经[编译Exchange](../ex-ug-compile.md)，或者直接[下载](https://repo1.maven.org/maven2/com/vesoft/nebula-exchange/)编译完成的.jar文件。本示例中使用Exchange {{exchange.release}}。

- 已经安装Spark。

- 已经安装JDK 1.8或以上版本，并配置环境变量JAVA_HOME。

- 确认Hadoop服务在所有部署Storage服务的机器上运行正常。

  !!! note
  
      - 如果需要生成其他数据源的SST文件，请参见相应数据源的文档，查看前提条件部分。

      - 如果只需要生成SST文件，不需要在部署Storage服务的机器上安装Hadoop服务。

## 操作步骤

### 步骤 1：在Nebula Graph中创建Schema

分析CSV文件中的数据，按以下步骤在Nebula Graph中创建Schema：

1. 确认Schema要素。Nebula Graph中的Schema要素如下表所示。

    | 要素  | 名称 | 属性 |
    | :--- | :--- | :--- |
    | Tag | `player` | `name string, age int` |
    | Tag | `team` | `name string` |
    | Edge Type | `follow` | `degree int` |
    | Edge Type | `serve` | `start_year int, end_year int` |

2. 使用Nebula Console创建一个图空间**basketballplayer**，并创建一个Schema，如下所示。

    ```ngql
    ## 创建图空间
    nebula> CREATE SPACE basketballplayer \
            (partition_num = 10, \
            replica_factor = 1, \
            vid_type = FIXED_STRING(30));
    
    ## 选择图空间basketballplayer
    nebula> USE basketballplayer;
    
    ## 创建Tag player
    nebula> CREATE TAG player(name string, age int);
    
    ## 创建Tag team
    nebula> CREATE TAG team(name string);
    
    ## 创建Edge type follow
    nebula> CREATE EDGE follow(degree int);

    ## 创建Edge type serve
    nebula> CREATE EDGE serve(start_year int, end_year int);
    ```

更多信息，请参见[快速开始](../../2.quick-start/1.quick-start-workflow.md)。

### 步骤 2：处理CSV文件

确认以下信息：

1. 处理CSV文件以满足Schema的要求。

  !!! note

        可以使用有表头或者无表头的CSV文件。

2. 获取CSV文件存储路径。

### 步骤 3：修改配置文件

编译Exchange后，复制`target/classes/application.conf`文件设置相关配置。在本示例中，复制的文件名为`sst_application.conf`。各个配置项的详细说明请参见[配置说明](../parameter-reference/ex-ug-parameter.md)。

```conf
{
  # Spark相关配置
  spark: {
    app: {
      name: Nebula Exchange 2.0
    }

    master:local

    driver: {
      cores: 1
      maxResultSize: 1G
    }

    executor: {
        memory:1G
    }

    cores:{
      max: 16
    }
  }

  # Nebula Graph相关配置
  nebula: {
    address:{
      graph:["127.0.0.1:9669"]
      meta:["127.0.0.1:9559"]
    }
    user: root
    pswd: nebula
    space: basketballplayer

    # SST文件相关配置
    path:{
        # 本地临时存放生成的SST文件的目录
        local:"/tmp"

        # SST文件在HDFS的存储路径
        remote:"/sst"
        
        # HDFS的NameNode地址
        hdfs.namenode: "hdfs://*.*.*.*:9000"
    }

    # 客户端连接参数
    connection {
      # socket连接、执行的超时时间，单位：毫秒。
      timeout: 30000
    }

    error: {
      # 最大失败数，超过后会退出应用程序。
      max: 32
      # 失败的导入作业将记录在输出路径中。
      output: /tmp/errors
    }

    # 使用谷歌的RateLimiter来限制发送到NebulaGraph的请求。
    rate: {
      # RateLimiter的稳定吞吐量。
      limit: 1024

      # 从RateLimiter获取允许的超时时间，单位：毫秒
      timeout: 1000
    }
  }


  # 处理点
  tags: [
    # 设置Tag player相关信息。
    {
      # 指定Nebula Graph中定义的Tag名称。
      name: player
      type: {
        # 指定数据源，使用CSV。
        source: csv

        # 指定如何将点数据导入Nebula Graph：Client或SST。
        sink: sst
      }

      # 指定CSV文件的路径。
      # 文件存储在HDFS上，用双引号括起路径，以hdfs://开头，例如"hdfs://ip:port/xx/xx"。
      path: "hdfs://*.*.*.*:9000/dataset/vertex_player.csv"

      # 如果CSV文件没有表头，使用[_c0, _c1, _c2, ..., _cn]表示其表头，并将列指示为属性值的源。
      # 如果CSV文件有表头，则使用实际的列名。
      fields: [_c1, _c2]

      # 指定Nebula Graph中定义的属性名称。
      # fields与nebula.fields的顺序必须一一对应。
      nebula.fields: [age, name]

      # 指定一个列作为VID的源。
      # vertex的值必须与上述fields或者csv.fields中的列名保持一致。
      # 目前，Nebula Graph {{nebula.release}}仅支持字符串或整数类型的VID。
      vertex: {
        field:_c0
      }

      # 指定的分隔符。默认值为英文逗号（,）。
      separator: ","

      # 如果CSV文件有表头，请将header设置为true。
      # 如果CSV文件没有表头，请将header设置为false。默认值为false。
      header: false

      # 指定单批次写入Nebula Graph的最大点数量。
      batch: 256

      # 指定Spark分片数量。
      partition: 32
    }

    # 设置Tag team相关信息。
    {
      # 指定Nebula Graph中定义的Tag名称。
      name: team
      type: {
        # 指定数据源，使用CSV。
        source: csv

        # 指定如何将点数据导入Nebula Graph：Client或SST。
        sink: sst
      }

      # 指定CSV文件的路径。
      # 文件存储在HDFS上，用双引号括起路径，以hdfs://开头，例如"hdfs://ip:port/xx/xx"。
      path: "hdfs://*.*.*.*:9000/dataset/vertex_team.csv"

      # 如果CSV文件没有表头，使用[_c0, _c1, _c2, ..., _cn]表示其表头，并将列指示为属性值的源。
      # 如果CSV文件有表头，则使用实际的列名。
      fields: [_c1]

      # 指定Nebula Graph中定义的属性名称。
      # fields与nebula.fields的顺序必须一一对应。
      nebula.fields: [name]

      # 指定一个列作为VID的源。
      # vertex的值必须与上述fields或者csv.fields中的列名保持一致。
      # 目前，Nebula Graph {{nebula.release}}仅支持字符串或整数类型的VID。
      vertex: {
        field:_c0
      }

      # 指定的分隔符。默认值为英文逗号（,）。
      separator: ","

      # 如果CSV文件有表头，请将header设置为true。
      # 如果CSV文件没有表头，请将header设置为false。默认值为false。
      header: false

      # 指定单批次写入Nebula Graph的最大点数量。
      batch: 256

      # 指定Spark分片数量。
      partition: 32
    }


    # 如果需要添加更多点，请参考前面的配置进行添加。
  ]
  # 处理边
  edges: [
    # 设置Edge type follow相关信息。
    {
      # 指定Nebula Graph中定义的Edge type名称。
      name: follow
      type: {
        # 指定数据源，使用CSV。
        source: csv

        # 指定如何将点数据导入Nebula Graph：Client或SST。
        sink: sst
      }

      # 指定CSV文件的路径。
      # 文件存储在HDFS上，用双引号括起路径，以hdfs://开头，例如"hdfs://ip:port/xx/xx"。
      path: "hdfs://*.*.*.*:9000/dataset/edge_follow.csv"

      # 如果CSV文件没有表头，使用[_c0, _c1, _c2, ..., _cn]表示其表头，并将列指示为属性值的源。
      # 如果CSV文件有表头，则使用实际的列名。
      fields: [_c2]

      # 指定Nebula Graph中定义的属性名称。
      # fields与nebula.fields的顺序必须一一对应。
      nebula.fields: [degree]

      # 指定一个列作为起始点和目的点的源。
      # vertex的值必须与上述fields或者csv.fields中的列名保持一致。
      # 目前，Nebula Graph {{nebula.release}}仅支持字符串或整数类型的VID。
      source: {
        field: _c0
      }
      target: {
        field: _c1
      }

      # 指定的分隔符。默认值为英文逗号（,）。
      separator: ","

      # 指定一个列作为rank的源(可选)。

      #ranking: rank

      # 如果CSV文件有表头，请将header设置为true。
      # 如果CSV文件没有表头，请将header设置为false。默认值为false。
      header: false

      # 指定单批次写入Nebula Graph的最大边数量。
      batch: 256

      # 指定Spark分片数量。
      partition: 32
    }

    # 设置Edge type serve相关信息。
    {
      # 指定Nebula Graph中定义的Edge type名称。
      name: serve
      type: {
        # 指定数据源，使用CSV。
        source: csv

        # 指定如何将点数据导入Nebula Graph：Client或SST。
        sink: sst
      }

      # 指定CSV文件的路径。
      # 文件存储在HDFS上，用双引号括起路径，以hdfs://开头，例如"hdfs://ip:port/xx/xx"。
      path: "hdfs://*.*.*.*:9000/dataset/edge_serve.csv"

      # 如果CSV文件没有表头，使用[_c0, _c1, _c2, ..., _cn]表示其表头，并将列指示为属性值的源。
      # 如果CSV文件有表头，则使用实际的列名。
      fields: [_c2,_c3]

      # 指定Nebula Graph中定义的属性名称。
      # fields与nebula.fields的顺序必须一一对应。
      nebula.fields: [start_year, end_year]

      # 指定一个列作为起始点和目的点的源。
      # vertex的值必须与上述fields或者csv.fields中的列名保持一致。
      # 目前，Nebula Graph {{nebula.release}}仅支持字符串或整数类型的VID。
      source: {
        field: _c0
      }
      target: {
        field: _c1
      }

      # 指定的分隔符。默认值为英文逗号（,）。
      separator: ","

      # 指定一个列作为rank的源(可选)。
      #ranking: _c5

      # 如果CSV文件有表头，请将header设置为true。
      # 如果CSV文件没有表头，请将header设置为false。默认值为false。
      header: false

      # 指定单批次写入Nebula Graph的最大边数量。
      batch: 256

      # 指定Spark分片数量。
      partition: 32
    }

  ]
  # 如果需要添加更多边，请参考前面的配置进行添加。
}
```

### 步骤 4：生成SST文件

运行如下命令将CSV源文件生成为SST文件。关于参数的说明，请参见[命令参数](../parameter-reference/ex-ug-para-import-command.md)。

```bash
${SPARK_HOME}/bin/spark-submit --master "local" --class com.vesoft.nebula.exchange.Exchange <nebula-exchange-{{exchange.release}}.jar_path> -c <sst_application.conf_path> 
```

!!! note

    JAR包有两种获取方式：[自行编译](../ex-ug-compile.md)或者从maven仓库下载。

示例：

```bash
${SPARK_HOME}/bin/spark-submit  --master "local" --class com.vesoft.nebula.exchange.Exchange  /root/nebula-spark-utils/nebula-exchange/target/nebula-exchange-{{exchange.release}}.jar  -c /root/nebula-spark-utils/nebula-exchange/target/classes/sst_application.conf
```

任务执行完成后，可以在HDFS上的`/sst`目录（`nebula.path.remote`参数指定）内查看到生成的SST文件。

!!! note

    如果对Schema有修改操作，例如重建图空间、修改Tag、修改Edge type等，需要重新生成SST文件，因为SST文件会验证Space ID、Tag ID、Edge ID等信息。

### 步骤 5：导入SST文件

!!! note

    导入前请确认以下信息：

    - 确认所有部署Storage服务的机器上都已部署Hadoop服务，并配置HADOOP_HOME和JAVA_HOME。
    
    - Meta服务配置文件中的`--ws_storage_http_port`（如果没有，请手动添加）和Storage服务配置文件中的`--ws_http_port`一致。例如都为`19779`。

    - Graph服务配置文件中的`--ws_meta_http_port`（如果没有，请手动添加）和Meta服务配置文件中的`--ws_http_port`一致。例如都为`19559`。

!!! caution
  
    如果需要导入SST文件至Nebula Graph 2.5.x中，请在[Storage配置文件](../../5.configurations-and-logs/1.configurations/4.storage-config.md)中添加`--enable_vertex_cache =false`，并重启Storage服务，才能正常导入SST文件，否则可能会出现没有覆盖旧数据的问题。

使用客户端工具连接Nebula Graph数据库，按如下操作导入SST文件：

1. 执行命令选择之前创建的图空间。

  ```ngql
  nebula> USE basketballplayer;
  ```

2. 执行命令下载SST文件：

  ```ngql
  nebula> DOWNLOAD HDFS "hdfs://<hadoop_address>:<hadoop_port>/<sst_file_path>";
  ```

  示例：

  ```ngql
  nebula> DOWNLOAD HDFS "hdfs://*.*.*.*:9000/sst";
  ```

2. 执行命令导入SST文件：

  ```ngql
  nebula> INGEST;
  ```

!!! note

    - 如果需要重新下载，请在Nebula Graph安装路径内的`data/storage/nebula`目录内，将对应Space ID目录内的`download`文件夹删除，然后重新下载SST文件。如果是图空间是多副本，保存副本的所有机器都需要删除`download`文件夹。

    - 如果导入时出现问题需要重新导入，重新执行`INGEST;`即可。

### 步骤 6：（可选）验证数据

用户可以在Nebula Graph客户端（例如Nebula Graph Studio）中执行查询语句，确认数据是否已导入。例如：

```ngql
GO FROM "player100" OVER follow;
```

用户也可以使用命令[`SHOW STATS`](../../3.ngql-guide/7.general-query-statements/6.show/14.show-stats.md)查看统计数据。

### 步骤 7：（如有）在Nebula Graph中重建索引

导入数据后，用户可以在Nebula Graph中重新创建并重建索引。详情请参见[索引介绍](../../3.ngql-guide/14.native-index-statements/README.md)。
