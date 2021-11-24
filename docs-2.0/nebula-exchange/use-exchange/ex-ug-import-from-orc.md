# 导入 ORC 文件数据

本文以一个示例说明如何使用 Exchange 将存储在 HDFS 或本地的 ORC 文件数据导入 Nebula Graph。

如果要向 Nebula Graph 导入本地 ORC 文件，请参见 [Nebula Importer](https://github.com/vesoft-inc/nebula-importer "Click to go to GitHub")。

## 数据集

本文以 [basketballplayer 数据集](https://docs-cdn.nebula-graph.com.cn/dataset/dataset.zip) 为例。

## 环境配置

本文示例在 MacOS 下完成，以下是相关的环境配置信息：

- 硬件规格：
  - CPU：1.7 GHz Quad-Core Intel Core i7
  - 内存：16 GB

- Spark：2.4.7 单机版

- Hadoop：2.9.2 伪分布式部署

- Nebula Graph：{{nebula.release}}。使用 [Docker Compose 部署](../../4.deployment-and-installation/2.compile-and-install-nebula-graph/3.deploy-nebula-graph-with-docker-compose.md)。

## 前提条件

开始导入数据之前，用户需要确认以下信息：

- 已经[安装部署 Nebula Graph](../../4.deployment-and-installation/2.compile-and-install-nebula-graph/2.install-nebula-graph-by-rpm-or-deb.md) 并获取如下信息：

  - Graph 服务和 Meta 服务的的 IP 地址和端口。

  - 拥有 Nebula Graph 写权限的用户名和密码。

- 已经编译 Exchange。详情请参见[编译 Exchange](../ex-ug-compile.md)。本示例中使用 Exchange {{exchange.release}}。

- 已经安装 Spark。

- 了解 Nebula Graph 中创建 Schema 的信息，包括 Tag 和 Edge type 的名称、属性等。

- 如果文件存储在 HDFS 上，需要确认 Hadoop 服务运行正常。

- 如果文件存储在本地且 Nebula Graph 是集群架构，需要在集群每台机器本地相同目录下放置文件。

## 操作步骤

### 步骤 1：在 Nebula Graph 中创建 Schema

分析 ORC 文件中的数据，按以下步骤在 Nebula Graph 中创建 Schema：

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

### 步骤 2：处理 ORC 文件

确认以下信息：

1. 处理 ORC 文件以满足 Schema 的要求。

2. 获取 ORC 文件存储路径。

### 步骤 3：修改配置文件

编译 Exchange 后，复制`target/classes/application.conf`文件设置 ORC 数据源相关的配置。在本示例中，复制的文件名为`orc_application.conf`。各个配置项的详细说明请参见[配置说明](../parameter-reference/ex-ug-parameter.md)。

```conf
{
  # Spark 相关配置
  spark: {
    app: {
      name: Nebula Exchange {{exchange.release}}
    }
    driver: {
      cores: 1
      maxResultSize: 1G
    }
    executor: {
        memory:1G
    }

    cores {
      max: 16
    }
  }

  # Nebula Graph 相关配置
  nebula: {
    address:{
      # 指定 Graph 服务和所有 Meta 服务的 IP 地址和端口。
      # 如果有多台服务器，地址之间用英文逗号（,）分隔。
      # 格式："ip1:port","ip2:port","ip3:port"
      graph:["127.0.0.1:9669"]
      meta:["127.0.0.1:9559"]
    }

    # 指定拥有 Nebula Graph 写权限的用户名和密码。
    user: root
    pswd: nebula

    # 指定图空间名称。
    space: basketballplayer
    connection {
      timeout: 3000
      retry: 3
    }
    execution {
      retry: 3
    }
    error: {
      max: 32
      output: /tmp/errors
    }
    rate: {
      limit: 1024
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
        # 指定数据源，使用 ORC。
        source: orc

        # 指定如何将点数据导入 Nebula Graph：Client 或 SST。
        sink: client
      }

      # 指定 ORC 文件的路径。
      # 如果文件存储在 HDFS 上，用双引号括起路径，以 hdfs://开头，例如"hdfs://ip:port/xx/xx"。
      # 如果文件存储在本地，用双引号括起路径，以 file://开头，例如"file:///tmp/xx.orc"。
      path: "hdfs://192.168.*.*:9000/data/vertex_player.orc"

      # 在 fields 里指定 ORC 文件中 key 名称，其对应的 value 会作为 Nebula Graph 中指定属性的数据源。
      # 如果需要指定多个值，用英文逗号（,）隔开。
      fields: [age,name]

      # 指定 Nebula Graph 中定义的属性名称。
      # fields 与 nebula.fields 的顺序必须一一对应。
      nebula.fields: [age, name]

      # 指定一个列作为 VID 的源。
      # vertex 的值必须与 ORC 文件中的字段保持一致。
      # 目前，Nebula Graph {{nebula.release}}仅支持字符串或整数类型的 VID。
      vertex: {
        field:id
      }

      # 指定单批次写入 Nebula Graph 的最大点数量。
      batch: 256

      # 指定 Spark 分片数量。
      partition: 32
    }

    # 设置 Tag team 相关信息。
    {
      # 指定 Nebula Graph 中定义的 Tag 名称。
      name: team
      type: {
        # 指定数据源，使用 ORC。
        source: orc

        # 指定如何将点数据导入 Nebula Graph：Client 或 SST。
        sink: client
      }

      # 指定 ORC 文件的路径。
      # 如果文件存储在 HDFS 上，用双引号括起路径，以 hdfs://开头，例如"hdfs://ip:port/xx/xx"。
      # 如果文件存储在本地，用双引号括起路径，以 file://开头，例如"file:///tmp/xx.orc"。
      path: "hdfs://192.168.*.*:9000/data/vertex_team.orc"

      # 在 fields 里指定 ORC 文件中 key 名称，其对应的 value 会作为 Nebula Graph 中指定属性的数据源。
      # 如果需要指定多个值，用英文逗号（,）隔开。
      fields: [name]

      # 指定 Nebula Graph 中定义的属性名称。
      # fields 与 nebula.fields 的顺序必须一一对应。
      nebula.fields: [name]

      # 指定一个列作为 VID 的源。
      # vertex 的值必须与 ORC 文件中的字段保持一致。
      # 目前，Nebula Graph {{nebula.release}}仅支持字符串或整数类型的 VID。
      vertex: {
        field:id
      }

      # 指定单批次写入 Nebula Graph 的最大点数量。
      batch: 256

      # 指定 Spark 分片数量。
      partition: 32
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
        # 指定数据源，使用 ORC。
        source: orc

        # 指定如何将点数据导入 Nebula Graph：Client 或 SST。
        sink: client
      }

      # 指定 ORC 文件的路径。
      # 如果文件存储在 HDFS 上，用双引号括起路径，以 hdfs://开头，例如"hdfs://ip:port/xx/xx"。
      # 如果文件存储在本地，用双引号括起路径，以 file://开头，例如"file:///tmp/xx.orc"。
      path: "hdfs://192.168.*.*:9000/data/edge_follow.orc"

      # 在 fields 里指定 ORC 文件中 key 名称，其对应的 value 会作为 Nebula Graph 中指定属性的数据源。
      # 如果需要指定多个值，用英文逗号（,）隔开。
      fields: [degree]

      # 指定 Nebula Graph 中定义的属性名称。
      # fields 与 nebula.fields 的顺序必须一一对应。
      nebula.fields: [degree]

      # 指定一个列作为起始点和目的点的源。
      # vertex 的值必须与 ORC 文件中的字段保持一致。
      # 目前，Nebula Graph {{nebula.release}}仅支持字符串或整数类型的 VID。
      source: {
        field: src
      }
      target: {
        field: dst
      }

      # 指定一个列作为 rank 的源（可选）。
      #ranking: rank

      # 指定单批次写入 Nebula Graph 的最大边数量。
      batch: 256

      # 指定 Spark 分片数量。
      partition: 32
    }

    # 设置 Edge type serve 相关信息。
    {
      # 指定 Nebula Graph 中定义的 Edge type 名称。
      name: serve
      type: {
        # 指定数据源，使用 ORC。
        source: orc

        # 指定如何将点数据导入 Nebula Graph：Client 或 SST。
        sink: client
      }

      # 指定 ORC 文件的路径。
      # 如果文件存储在 HDFS 上，用双引号括起路径，以 hdfs://开头，例如"hdfs://ip:port/xx/xx"。
      # 如果文件存储在本地，用双引号括起路径，以 file://开头，例如"file:///tmp/xx.orc"。
      path: "hdfs://192.168.*.*:9000/data/edge_serve.orc"

      # 在 fields 里指定 ORC 文件中 key 名称，其对应的 value 会作为 Nebula Graph 中指定属性的数据源。
      # 如果需要指定多个值，用英文逗号（,）隔开。
      fields: [start_year,end_year]

      # 指定 Nebula Graph 中定义的属性名称。
      # fields 与 nebula.fields 的顺序必须一一对应。
      nebula.fields: [start_year, end_year]

      # 指定一个列作为起始点和目的点的源。
      # vertex 的值必须与 ORC 文件中的字段保持一致。
      # 目前，Nebula Graph {{nebula.release}}仅支持字符串或整数类型的 VID。
      source: {
        field: src
      }
      target: {
        field: dst
      }

      # 指定一个列作为 rank 的源（可选）。
      #ranking: _c5

      # 指定单批次写入 Nebula Graph 的最大边数量。
      batch: 256

      # 指定 Spark 分片数量。
      partition: 32
    }

  ]
  # 如果需要添加更多边，请参考前面的配置进行添加。
}
```

### 步骤 4：向 Nebula Graph 导入数据

运行如下命令将 ORC 文件数据导入到 Nebula Graph 中。关于参数的说明，请参见[导入命令参数](../parameter-reference/ex-ug-para-import-command.md)。

```bash
${SPARK_HOME}/bin/spark-submit --master "local" --class com.vesoft.nebula.exchange.Exchange <nebula-exchange-{{exchange.release}}.jar_path> -c <orc_application.conf_path> 
```

!!! note

    JAR 包有两种获取方式：[自行编译](../ex-ug-compile.md) 或者从 maven 仓库下载。

示例：

```bash
${SPARK_HOME}/bin/spark-submit  --master "local" --class com.vesoft.nebula.exchange.Exchange  /root/nebula-exchange/nebula-exchange/target/nebula-exchange-{{exchange.release}}.jar  -c /root/nebula-exchange/nebula-exchange/target/classes/orc_application.conf
```

用户可以在返回信息中搜索`batchSuccess.<tag_name/edge_name>`，确认成功的数量。例如`batchSuccess.follow: 300`。

### 步骤 5：（可选）验证数据

用户可以在 Nebula Graph 客户端（例如 Nebula Graph Studio）中执行查询语句，确认数据是否已导入。例如：

```ngql
GO FROM "player100" OVER follow;
```

用户也可以使用命令 [`SHOW STATS`](../../3.ngql-guide/7.general-query-statements/6.show/14.show-stats.md) 查看统计数据。

### 步骤 6：（如有）在 Nebula Graph 中重建索引

导入数据后，用户可以在 Nebula Graph 中重新创建并重建索引。详情请参见[索引介绍](../../3.ngql-guide/14.native-index-statements/README.md)。
