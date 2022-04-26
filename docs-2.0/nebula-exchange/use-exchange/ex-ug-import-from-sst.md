# 导入 SST 文件数据

本文以一个示例说明如何将数据源的数据生成 SST（Sorted String Table）文件并保存在 HDFS 上，然后导入 Nebula Graph，示例数据源是 CSV 文件。

## 注意事项

- 仅 Linux 系统支持导入 SST 文件。

- 不支持属性的 Default 值。

- 企业版 Exchange {{exchange.release}}不支持基于 [GEOGRAPHY](../../3.ngql-guide/3.data-types/10.geography.md) 类型的数据生成 SST 文件。

## 背景信息

Exchange 支持两种数据导入模式：

- 直接将数据源的数据通过** nGQL **语句的形式导入 Nebula Graph。

- 将数据源的数据生成 SST 文件，然后借助 Console 将 SST 文件导入 Nebula Graph。

下文将介绍生成 SST 文件并用其导入数据的适用场景、实现方法、前提条件、操作步骤等内容。

## 适用场景

- 适合在线业务，因为生成时几乎不会影响业务（只是读取 Schema），导入速度快。

  !!! caution
  
        导入期间（大约 10 秒）会阻塞对应空间的写操作，并且之后数小时内可能有历史数据整理，建议在业务低峰期进行导入。

- 适合数据源数据量较大的场景，导入速度快。

## 实现方法

Nebula Graph 底层使用 RocksDB 作为键值型存储引擎。RocksDB 是基于硬盘的存储引擎，提供了一系列 API 用于创建及导入 SST 格式的文件，有助于快速导入海量数据。

SST 文件是一个内部包含了任意长度的有序键值对集合的文件，用于高效地存储大量键值型数据。生成 SST 文件的整个过程主要由 Exchange 的 Reader、sstProcessor 和 sstWriter 完成。整个数据处理过程如下：

1. Reader 从数据源中读取数据。

2. sstProcessor 根据 Nebula Graph 的 Schema 信息生成 SST 文件，然后上传至 HDFS。SST 文件的格式请参见[数据存储格式](../../1.introduction/3.nebula-graph-architecture/4.storage-service.md)。

3. sstWriter 打开一个文件并插入数据。生成 SST 文件时，Key 必须按照顺序写入。

4. 生成 SST 文件之后，RocksDB 通过`IngestExternalFile()`方法将 SST 文件导入到 Nebula Graph 中。例如：

  ```
  IngestExternalFileOptions ifo;
  # 导入两个 SST 文件
  Status s = db_->IngestExternalFile({"/home/usr/file1.sst", "/home/usr/file2.sst"}, ifo);
  if (!s.ok()) {
    printf("Error while adding file %s and %s, Error %s\n",
           file_path1.c_str(), file_path2.c_str(), s.ToString().c_str());
    return 1;
  }
  ```

  调用`IngestExternalFile()`方法时，RocksDB 默认会将文件拷贝到数据目录，并且阻塞 RocksDB 写入操作。如果 SST 文件中的键范围覆盖了 Memtable 键的范围，则将 Memtable 落盘（flush）到硬盘。将 SST 文件放置在 LSM 树最优位置后，为文件分配一个全局序列号，并打开写操作。

## 数据集

本文以 [basketballplayer 数据集](https://docs-cdn.nebula-graph.com.cn/dataset/dataset.zip)为例。

## 环境配置

本文示例在 MacOS 下完成，以下是相关的环境配置信息：

- 硬件规格：
  - CPU：1.7 GHz Quad-Core Intel Core i7
  - 内存：16 GB

- Spark：2.4.7 单机版

- Hadoop：2.9.2 伪分布式部署

- Nebula Graph：{{nebula.release}}。

## 前提条件

开始导入数据之前，用户需要确认以下信息：

- 已经[安装部署 Nebula Graph {{nebula.release}}](../../4.deployment-and-installation/2.compile-and-install-nebula-graph/2.install-nebula-graph-by-rpm-or-deb.md) 并获取如下信息：

  - Graph 服务和 Meta 服务的的 IP 地址和端口。

  - 拥有 Nebula Graph 写权限的用户名和密码。

  - Meta 服务配置文件中的`--ws_storage_http_port`和 Storage 服务配置文件中的`--ws_http_port`一致。例如都为`19779`。

  - Graph 服务配置文件中的`--ws_meta_http_port`和 Meta 服务配置文件中的`--ws_http_port`一致。例如都为`19559`。

  - Schema 的信息，包括 Tag 和 Edge type 的名称、属性等。

- 已经[编译 Exchange](../ex-ug-compile.md)，或者直接[下载](https://repo1.maven.org/maven2/com/vesoft/nebula-exchange/)编译完成的。jar 文件。本示例中使用 Exchange {{exchange.release}}。

- 已经安装 Spark。

- 已经安装 JDK 1.8 或以上版本，并配置环境变量 JAVA_HOME。

- 确认 Hadoop 服务在所有部署 Storage 服务的机器上运行正常。

  !!! note
  
      - 如果需要生成其他数据源的 SST 文件，请参见相应数据源的文档，查看前提条件部分。

      - 如果只需要生成 SST 文件，不需要在部署 Storage 服务的机器上安装 Hadoop 服务。
      
      - 如需在 INGEST（数据导入）结束后自动移除 SST 文件，在 Storage 服务配置文件中增加`--move_files=true`，该配置会让 Nebula Graph 在 INGEST 后将 SST 文件移动（`mv`）到`data`目录下。`--move_files`的默认值为`false`，此时 Nebula Graph 会复制（`cp`）SST 文件而不是移动。

## 操作步骤

### 步骤 1：在 Nebula Graph 中创建 Schema

分析 CSV 文件中的数据，按以下步骤在 Nebula Graph 中创建 Schema：

1. 确认 Schema 要素。Nebula Graph 中的 Schema 要素如下表所示。

    | 要素  | 名称 | 属性 |
    | :--- | :--- | :--- |
    | Tag | `player` | `name string, age int` |
    | Tag | `team` | `name string` |
    | Edge Type | `follow` | `degree int` |
    | Edge Type | `serve` | `start_year int, end_year int` |

2. 使用 Nebula Console 创建一个图空间** basketballplayer**，并创建一个 Schema，如下所示。

    ```ngql
    ## 创建图空间
    nebula> CREATE SPACE basketballplayer \
            (partition_num = 10, \
            replica_factor = 1, \
            vid_type = FIXED_STRING(30));
    
    ## 选择图空间 basketballplayer
    nebula> USE basketballplayer;
    
    ## 创建 Tag player
    nebula> CREATE TAG player(name string, age int);
    
    ## 创建 Tag team
    nebula> CREATE TAG team(name string);
    
    ## 创建 Edge type follow
    nebula> CREATE EDGE follow(degree int);

    ## 创建 Edge type serve
    nebula> CREATE EDGE serve(start_year int, end_year int);
    ```

更多信息，请参见[快速开始](../../2.quick-start/1.quick-start-workflow.md)。

### 步骤 2：处理 CSV 文件

确认以下信息：

1. 处理 CSV 文件以满足 Schema 的要求。

  !!! note

        可以使用有表头或者无表头的 CSV 文件。

2. 获取 CSV 文件存储路径。

### 步骤 3：修改配置文件

编译 Exchange 后，复制`target/classes/application.conf`文件设置相关配置。在本示例中，复制的文件名为`sst_application.conf`。各个配置项的详细说明请参见[配置说明](../parameter-reference/ex-ug-parameter.md)。

```conf
{
  # Spark 相关配置
  spark: {
    app: {
      name: Nebula Exchange {{exchange.release}}
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

  # Nebula Graph 相关配置
  nebula: {
    address:{
      graph:["127.0.0.1:9669"]
      meta:["127.0.0.1:9559"]
    }
    user: root
    pswd: nebula
    space: basketballplayer

    # SST 文件相关配置
    path:{
        # 本地临时存放生成的 SST 文件的目录
        local:"/tmp"

        # SST 文件在 HDFS 的存储路径
        remote:"/sst"
        
        # HDFS 的 NameNode 地址
        hdfs.namenode: "hdfs://*.*.*.*:9000"
    }

    # 客户端连接参数
    connection: {
      # socket 连接、执行的超时时间，单位：毫秒。
      timeout: 30000
    }

    error: {
      # 最大失败数，超过后会退出应用程序。
      max: 32
      # 失败的导入作业将记录在输出路径中。
      output: /tmp/errors
    }

    # 使用Google Guava RateLimiter 来限制发送到 Nebula Graph 的请求。
    rate: {
      # RateLimiter 的稳定吞吐量。
      limit: 1024

      # 从 RateLimiter 获取允许的超时时间，单位：毫秒
      timeout: 1000
    }
  }

  # 处理点
  tags: [
    # 设置 Tag player 相关信息。
    {
      # 指定 Nebula Graph 中定义的 Tag 名称。
      name: player
      type: {
        # 指定数据源，使用 CSV。
        source: csv

        # 指定如何将点数据导入 Nebula Graph：Client 或 SST。
        sink: sst
      }

      # 指定 CSV 文件的路径。
      # 文件存储在 HDFS 上，用双引号括起路径，以 hdfs://开头，例如"hdfs://ip:port/xx/xx.csv"。
      path: "hdfs://*.*.*.*:9000/dataset/vertex_player.csv"

      # 如果 CSV 文件没有表头，使用 [_c0, _c1, _c2, ..., _cn] 表示其表头，并将列指示为属性值的源。
      # 如果 CSV 文件有表头，则使用实际的列名。
      fields: [_c1, _c2]

      # 指定 Nebula Graph 中定义的属性名称。
      # fields 与 nebula.fields 的顺序必须一一对应。
      nebula.fields: [age, name]

      # 指定一个列作为 VID 的源。
      # vertex 的值必须与上述 fields 或者 csv.fields 中的列名保持一致。
      # 目前，Nebula Graph {{nebula.release}}仅支持字符串或整数类型的 VID。
      vertex: {
        field:_c0
      }

      # 指定的分隔符。默认值为英文逗号（,）。
      separator: ","

      # 如果 CSV 文件有表头，请将 header 设置为 true。
      # 如果 CSV 文件没有表头，请将 header 设置为 false。默认值为 false。
      header: false

      # 指定单批次写入 Nebula Graph 的最大点数量。
      batch: 256

      # 指定 Spark 分片数量。
      partition: 32

      # 生成 SST 文件时是否要基于 Nebula Graph 中图空间的 partition 进行数据重分区。
      repartitionWithNebula: false
    }

    # 设置 Tag team 相关信息。
    {
      # 指定 Nebula Graph 中定义的 Tag 名称。
      name: team
      type: {
        # 指定数据源，使用 CSV。
        source: csv

        # 指定如何将点数据导入 Nebula Graph：Client 或 SST。
        sink: sst
      }

      # 指定 CSV 文件的路径。
      # 文件存储在 HDFS 上，用双引号括起路径，以 hdfs://开头，例如"hdfs://ip:port/xx/xx.csv"。
      path: "hdfs://*.*.*.*:9000/dataset/vertex_team.csv"

      # 如果 CSV 文件没有表头，使用 [_c0, _c1, _c2, ..., _cn] 表示其表头，并将列指示为属性值的源。
      # 如果 CSV 文件有表头，则使用实际的列名。
      fields: [_c1]

      # 指定 Nebula Graph 中定义的属性名称。
      # fields 与 nebula.fields 的顺序必须一一对应。
      nebula.fields: [name]

      # 指定一个列作为 VID 的源。
      # vertex 的值必须与上述 fields 或者 csv.fields 中的列名保持一致。
      # 目前，Nebula Graph {{nebula.release}}仅支持字符串或整数类型的 VID。
      vertex: {
        field:_c0
      }

      # 指定的分隔符。默认值为英文逗号（,）。
      separator: ","

      # 如果 CSV 文件有表头，请将 header 设置为 true。
      # 如果 CSV 文件没有表头，请将 header 设置为 false。默认值为 false。
      header: false

      # 指定单批次写入 Nebula Graph 的最大点数量。
      batch: 256

      # 指定 Spark 分片数量。
      partition: 32

      # 生成 SST 文件时是否要基于 Nebula Graph 中图空间的 partition 进行数据重分区。
      repartitionWithNebula: false
    }

    # 如果需要添加更多点，请参考前面的配置进行添加。
  ]
  # 处理边
  edges: [
    # 设置 Edge type follow 相关信息。
    {
      # 指定 Nebula Graph 中定义的 Edge type 名称。
      name: follow
      type: {
        # 指定数据源，使用 CSV。
        source: csv

        # 指定如何将点数据导入 Nebula Graph：Client 或 SST。
        sink: sst
      }

      # 指定 CSV 文件的路径。
      # 文件存储在 HDFS 上，用双引号括起路径，以 hdfs://开头，例如"hdfs://ip:port/xx/xx.csv"。
      path: "hdfs://*.*.*.*:9000/dataset/edge_follow.csv"

      # 如果 CSV 文件没有表头，使用 [_c0, _c1, _c2, ..., _cn] 表示其表头，并将列指示为属性值的源。
      # 如果 CSV 文件有表头，则使用实际的列名。
      fields: [_c2]

      # 指定 Nebula Graph 中定义的属性名称。
      # fields 与 nebula.fields 的顺序必须一一对应。
      nebula.fields: [degree]

      # 指定一个列作为起始点和目的点的源。
      # vertex 的值必须与上述 fields 或者 csv.fields 中的列名保持一致。
      # 目前，Nebula Graph {{nebula.release}}仅支持字符串或整数类型的 VID。
      source: {
        field: _c0
      }
      target: {
        field: _c1
      }

      # 指定的分隔符。默认值为英文逗号（,）。
      separator: ","

      # 指定一个列作为 rank 的源（可选）。

      #ranking: rank

      # 如果 CSV 文件有表头，请将 header 设置为 true。
      # 如果 CSV 文件没有表头，请将 header 设置为 false。默认值为 false。
      header: false

      # 指定单批次写入 Nebula Graph 的最大边数量。
      batch: 256

      # 指定 Spark 分片数量。
      partition: 32

      # 生成 SST 文件时是否要基于 Nebula Graph 中图空间的 partition 进行数据重分区。
      repartitionWithNebula: false
    }

    # 设置 Edge type serve 相关信息。
    {
      # 指定 Nebula Graph 中定义的 Edge type 名称。
      name: serve
      type: {
        # 指定数据源，使用 CSV。
        source: csv

        # 指定如何将点数据导入 Nebula Graph：Client 或 SST。
        sink: sst
      }

      # 指定 CSV 文件的路径。
      # 文件存储在 HDFS 上，用双引号括起路径，以 hdfs://开头，例如"hdfs://ip:port/xx/xx.csv"。
      path: "hdfs://*.*.*.*:9000/dataset/edge_serve.csv"

      # 如果 CSV 文件没有表头，使用 [_c0, _c1, _c2, ..., _cn] 表示其表头，并将列指示为属性值的源。
      # 如果 CSV 文件有表头，则使用实际的列名。
      fields: [_c2,_c3]

      # 指定 Nebula Graph 中定义的属性名称。
      # fields 与 nebula.fields 的顺序必须一一对应。
      nebula.fields: [start_year, end_year]

      # 指定一个列作为起始点和目的点的源。
      # vertex 的值必须与上述 fields 或者 csv.fields 中的列名保持一致。
      # 目前，Nebula Graph {{nebula.release}}仅支持字符串或整数类型的 VID。
      source: {
        field: _c0
      }
      target: {
        field: _c1
      }

      # 指定的分隔符。默认值为英文逗号（,）。
      separator: ","

      # 指定一个列作为 rank 的源（可选）。
      #ranking: _c5

      # 如果 CSV 文件有表头，请将 header 设置为 true。
      # 如果 CSV 文件没有表头，请将 header 设置为 false。默认值为 false。
      header: false

      # 指定单批次写入 Nebula Graph 的最大边数量。
      batch: 256

      # 指定 Spark 分片数量。
      partition: 32

      # 生成 SST 文件时是否要基于 Nebula Graph 中图空间的 partition 进行数据重分区。
      repartitionWithNebula: false
    }

  ]
  # 如果需要添加更多边，请参考前面的配置进行添加。
}
```

### 步骤 4：生成 SST 文件

运行如下命令将 CSV 源文件生成为 SST 文件。关于参数的说明，请参见[命令参数](../parameter-reference/ex-ug-para-import-command.md)。

```bash
${SPARK_HOME}/bin/spark-submit --master "local" --conf spark.sql.shuffle.partitions=<shuffle_concurrency> --class com.vesoft.nebula.exchange.Exchange <nebula-exchange-{{exchange.release}}.jar_path> -c <sst_application.conf_path> 
```

!!! note

    生成 SST 文件时，会涉及到 Spark 的 shuffle 操作，请注意在提交命令中增加`spark.sql.shuffle.partitions`的配置。

!!! note

    JAR 包有两种获取方式：[自行编译](../ex-ug-compile.md)或者从 maven 仓库下载。

示例：

```bash
${SPARK_HOME}/bin/spark-submit  --master "local" --conf spark.sql.shuffle.partitions=200 --class com.vesoft.nebula.exchange.Exchange  /root/nebula-exchange/nebula-exchange/target/nebula-exchange-{{exchange.release}}.jar  -c /root/nebula-exchange/nebula-exchange/target/classes/sst_application.conf
```

任务执行完成后，可以在 HDFS 上的`/sst`目录（`nebula.path.remote`参数指定）内查看到生成的 SST 文件。

!!! note

    如果对 Schema 有修改操作，例如重建图空间、修改 Tag、修改 Edge type 等，需要重新生成 SST 文件，因为 SST 文件会验证 Space ID、Tag ID、Edge ID 等信息。

### 步骤 5：导入 SST 文件

!!! note

    导入前请确认以下信息：

    - 确认所有部署 Storage 服务的机器上都已部署 Hadoop 服务，并配置 HADOOP_HOME 和 JAVA_HOME。
    
    - Meta 服务配置文件中的`--ws_storage_http_port`（如果没有，请手动添加）和 Storage 服务配置文件中的`--ws_http_port`一致。例如都为`19779`。

    - Graph 服务配置文件中的`--ws_meta_http_port`（如果没有，请手动添加）和 Meta 服务配置文件中的`--ws_http_port`一致。例如都为`19559`。

使用客户端工具连接 Nebula Graph 数据库，按如下操作导入 SST 文件：

1. 执行命令选择之前创建的图空间。

  ```ngql
  nebula> USE basketballplayer;
  ```

2. 执行命令下载 SST 文件：

  ```ngql
  nebula> SUBMIT JOB DOWNLOAD HDFS "hdfs://<hadoop_address>:<hadoop_port>/<sst_file_path>";
  ```

  示例：

  ```ngql
  nebula> SUBMIT JOB DOWNLOAD HDFS "hdfs://*.*.*.*:9000/sst";
  ```

2. 执行命令导入 SST 文件：

  ```ngql
  nebula> SUBMIT JOB INGEST;
  ```

!!! note

    - 如果需要重新下载，请在 Nebula Graph 安装路径内的`data/storage/nebula`目录内，将对应 Space ID 目录内的`download`文件夹删除，然后重新下载 SST 文件。如果图空间是多副本，保存副本的所有机器都需要删除`download`文件夹。

    - 如果导入时出现问题需要重新导入，重新执行`SUBMIT JOB INGEST;`即可。

### 步骤 6：（可选）验证数据

用户可以在 Nebula Graph 客户端（例如 Nebula Graph Studio）中执行查询语句，确认数据是否已导入。例如：

```ngql
GO FROM "player100" OVER follow;
```

用户也可以使用命令 [`SHOW STATS`](../../3.ngql-guide/7.general-query-statements/6.show/14.show-stats.md) 查看统计数据。

### 步骤 7：（如有）在 Nebula Graph 中重建索引

导入数据后，用户可以在 Nebula Graph 中重新创建并重建索引。详情请参见[索引介绍](../../3.ngql-guide/14.native-index-statements/README.md)。
