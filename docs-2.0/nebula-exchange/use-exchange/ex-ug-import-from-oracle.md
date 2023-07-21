# 导入 Oracle 数据

本文以一个示例说明如何使用 Exchange 将存储在 Oracle 上的数据导入{{nebula.name}}。

## 数据集

本文以 [basketballplayer 数据集](https://docs-cdn.nebula-graph.com.cn/dataset/dataset.zip)为例。

在本示例中，该数据集已经存入 Oracle 中名为`basketball`的数据库中，以`player`、`team`、`follow`和`serve`四个表存储了所有点和边的信息。以下为各个表的结构。

```sql
oracle> desc player;
+-----------+-------+---------------+ 
| Column    | Null  | Type          |
+-----------+-------+---------------+ 
| PLAYERID  |  -    | VARCHAR2(30)  |
| NAME      |  -    | VARCHAR2(30)  |
| AGE       |  -    | NUMBER        |
+-----------+-------+---------------+ 

oracle> desc team;
+-----------+-------+---------------+ 
| Column    | Null  | Type          |
+-----------+-------+---------------+ 
| TEAMID    |  -    | VARCHAR2(30)  |
| NAME      |  -    | VARCHAR2(30)  |
+-----------+-------+---------------+ 

oracle> desc follow;
+-------------+-------+---------------+ 
| Column      | Null  | Type          |
+-------------+-------+---------------+ 
| SRC_PLAYER  |  -    | VARCHAR2(30)  |
| DST_PLAYER  |  -    | VARCHAR2(30)  |
| DEGREE      |  -    | NUMBER        |
+-------------+-------+---------------+ 

oracle> desc serve;
+------------+-------+---------------+ 
| Column     | Null  | Type          |
+------------+-------+---------------+ 
| PLAYERID   |  -    | VARCHAR2(30)  |
| TEAMID     |  -    | VARCHAR2(30)  |
| START_YEAR |  -    | NUMBER        |
| END_YEAR   |  -    | NUMBER        |
+------------+-------+---------------+ 
```

## 环境配置

本文示例在 MacOS 下完成，以下是相关的环境配置信息：

- 硬件规格：
  - CPU：1.7 GHz Quad-Core Intel Core i7
  - 内存：16 GB

- Spark：2.4.7，单机版

- {{nebula.name}}：{{nebula.release}}。
  
## 前提条件

开始导入数据之前，用户需要确认以下信息：

- 已经[安装部署{{nebula.name}}](../../4.deployment-and-installation/2.compile-and-install-nebula-graph/2.install-nebula-graph-by-rpm-or-deb.md) 并获取如下信息：

  - Graph 服务和 Meta 服务的的 IP 地址和端口。

  - 拥有{{nebula.name}}写权限的用户名和密码。

- 已经编译 Exchange。详情请参见[编译 Exchange](../ex-ug-compile.md)。本示例中使用 Exchange {{exchange.release}}。

- 已经安装 Spark。

- 了解{{nebula.name}}中创建的 Schema 信息，包括 Tag 和 Edge type 的名称、属性等。

## 操作步骤

### 步骤 1：在{{nebula.name}}中创建 Schema

分析数据，按以下步骤在{{nebula.name}}中创建 Schema：

1. 确认 Schema 要素。{{nebula.name}}中的 Schema 要素如下表所示。

    | 要素  | 名称 | 属性 |
    | :--- | :--- | :--- |
    | Tag | `player` | `name string, age int` |
    | Tag | `team` | `name string` |
    | Edge Type | `follow` | `degree int` |
    | Edge Type | `serve` | `start_year int, end_year int` |

2. 在{{nebula.name}}中创建一个图空间 **basketballplayer**，并创建一个 Schema，如下所示。

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

更多信息，请参见[快速开始](../../2.quick-start/1.quick-start-overview.md)。

### 步骤 2：修改配置文件

编译 Exchange 后，复制`target/classes/application.conf`文件设置 Oracle 数据源相关的配置。在本示例中，复制的文件名为`oracle_application.conf`。各个配置项的详细说明请参见[配置说明](../parameter-reference/ex-ug-parameter.md)。

```conf
{
  # Spark 相关配置
  spark: {
    app: {
      name: NebulaGraph Exchange {{exchange.release}}
    }
    driver: {
      cores: 1
      maxResultSize: 1G
    }
    cores: {
      max: 16
    }
  }

# {{nebula.name}} 相关配置
  nebula: {
    address:{
      # 以下为 {{nebula.name}} 的 Graph 服务和 Meta 服务所在机器的 IP 地址及端口。
      # 如果有多个地址，格式为 "ip1:port","ip2:port","ip3:port"。
      # 不同地址之间以英文逗号 (,) 隔开。
      graph:["127.0.0.1:9669"]
      #任意一个 Meta 服务的地址。
      #如果您的 {{nebula.name}} 在虚拟网络中，如k8s，请配置 Leader Meta的地址。
      meta:["127.0.0.1:9559"]
    }
    # 填写的账号必须拥有 {{nebula.name}} 相应图空间的写数据权限。
    user: root
    pswd: nebula
    # 填写 {{nebula.name}} 中需要写入数据的图空间名称。
    space: basketballplayer
    connection: {
      timeout: 3000
      retry: 3
    }
    execution: {
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
    {
      # {{nebula.name}} 中对应的 Tag 名称。
      name: player
      type: {
        # 指定数据源文件格式，设置为 Oracle。
        source: oracle
        # 指定如何将点数据导入{{nebula.name}}：Client 或 SST。
        sink: client
      }


      url:"jdbc:oracle:thin:@host:1521:db"
      driver: "oracle.jdbc.driver.OracleDriver"
      user: "root"
      password: "123456"
      table: "basketball.player"
      sentence: "select playerid, name, age from player"

      # 在 fields 里指定 player 表中的列名称，其对应的 value 会作为{{nebula.name}}中指定属性。
      # fields 和 nebula.fields 里的配置必须一一对应。
      # 如果需要指定多个列名称，用英文逗号（,）隔开。
      fields: [age,name]
      nebula.fields: [age,name]

      # 指定表中某一列数据为{{nebula.name}}中点 VID 的来源。
      vertex: {
        field:playerid
      # udf:{
      #            separator:"_"
      #            oldColNames:[field-0,field-1,field-2]
      #            newColName:new-field
      #        }
      }

      # 单批次写入{{nebula.name}}的数据条数。
      batch: 256

      # Spark 分区数量
      partition: 32
    }
    # 设置 Tag team 相关信息。
    {
      name: team
      type: {
        source: oracle
        sink: client
      }

      url:"jdbc:oracle:thin:@host:1521:db"
      driver: "oracle.jdbc.driver.OracleDriver"
      user: "root"
      password: "123456"
      table: "basketball.team"
      sentence: "select teamid, name from team"

      fields: [name]
      nebula.fields: [name]
      vertex: {
        field: teamid
      }
      batch: 256
      partition: 32
    }

  ]

  # 处理边数据
  edges: [
    # 设置 Edge type follow 相关信息
    {
      # {{nebula.name}}中对应的 Edge type 名称。
      name: follow

      type: {
        # 指定数据源文件格式，设置为 Oracle。
        source: oracle

        # 指定边数据导入 {{nebula.name}} 的方式，
        # 指定如何将点数据导入{{nebula.name}}：Client 或 SST。
        sink: client
      }

      url:"jdbc:oracle:thin:@host:1521:db"
      driver: "oracle.jdbc.driver.OracleDriver"
      user: "root"
      password: "123456"
      table: "basketball.follow"
      sentence: "select src_player, dst_player, degree from follow"

      # 在 fields 里指定 follow 表中的列名称，其对应的 value 会作为{{nebula.name}}中指定属性。
      # fields 和 nebula.fields 里的配置必须一一对应。
      # 如果需要指定多个列名称，用英文逗号（,）隔开。
      fields: [degree]
      nebula.fields: [degree]

      # 在 source 里，将 follow 表中某一列作为边的起始点数据源。
      # 在 target 里，将 follow 表中某一列作为边的目的点数据源。
      source: {
        field: src_player
      # udf:{
      #            separator:"_"
      #            oldColNames:[field-0,field-1,field-2]
      #            newColName:new-field
      #        }
      }

      target: {
        field: dst_player
      # udf:{
      #            separator:"_"
      #            oldColNames:[field-0,field-1,field-2]
      #            newColName:new-field
      #        }
      }

      # 指定一个列作为 rank 的源（可选）。
      #ranking: rank

      # 单批次写入{{nebula.name}}的数据条数。
      batch: 256

      # Spark 分区数量
      partition: 32
    }

    # 设置 Edge type serve 相关信息
    {
      name: serve
      type: {
        source: oracle
        sink: client
      }

      url:"jdbc:oracle:thin:@host:1521:db"
      driver: "oracle.jdbc.driver.OracleDriver"
      user: "root"
      password: "123456"
      table: "basketball.serve"
      sentence: "select playerid, teamid, start_year, end_year from serve"

      fields: [start_year,end_year]
      nebula.fields: [start_year,end_year]
      source: {
        field: playerid
      }
      target: {
        field: teamid
      }

      # 指定一个列作为 rank 的源（可选）。
      #ranking: rank

      batch: 256
      partition: 32
    }
  ]
}
```

### 步骤 3：向{{nebula.name}}导入数据

运行如下命令将 Oracle 数据导入到{{nebula.name}}中。关于参数的说明，请参见[导入命令参数](../parameter-reference/ex-ug-para-import-command.md)。

```bash
${SPARK_HOME}/bin/spark-submit --master "local" --class com.vesoft.nebula.exchange.Exchange <nebula-exchange-{{exchange.release}}.jar_path> -c <oracle_application.conf_path>
```

!!! note

    JAR 包有两种获取方式：[自行编译](../ex-ug-compile.md)或者从 maven 仓库下载。

示例：

```bash
${SPARK_HOME}/bin/spark-submit  --master "local" --class com.vesoft.nebula.exchange.Exchange  /root/nebula-exchange/nebula-exchange/target/nebula-exchange-{{exchange.release}}.jar  -c /root/nebula-exchange/nebula-exchange/target/classes/oracle_application.conf
```

用户可以在返回信息中搜索`batchSuccess.<tag_name/edge_name>`，确认成功的数量。例如`batchSuccess.follow: 300`。

### 步骤 4：（可选）验证数据

用户可以在{{nebula.name}}客户端（例如 NebulaGraph Studio）中执行查询语句，确认数据是否已导入。例如：

```ngql
LOOKUP ON player YIELD id(vertex);
```

用户也可以使用命令 [`SHOW STATS`](../../3.ngql-guide/7.general-query-statements/6.show/14.show-stats.md) 查看统计数据。

### 步骤 5：（如有）在{{nebula.name}}中重建索引

导入数据后，用户可以在{{nebula.name}}中重新创建并重建索引。详情请参见[索引介绍](../../3.ngql-guide/14.native-index-statements/README.md)。
