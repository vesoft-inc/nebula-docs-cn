# 导出{{nebula.name}}数据

Exchange 支持将{{nebula.name}}中的数据导出到 CSV 文件或另一个图空间（不同{{nebula.name}}集群也支持）中。本文介绍具体的操作步骤。

!!! enterpriseonly

    仅企业版 Exchange 支持导出{{nebula.name}}数据。

## 环境准备

本示例在 Linux 系统的虚拟机环境下完成，导出数据前准备的软硬件信息如下。

### 硬件

| 类型 | 信息 |
| - | - |
| CPU | 4 Intel(R) Xeon(R) Platinum 8260 CPU @ 2.30GHz |
| 内存 | 16G |
| 硬盘 | 50G |

### 系统

CentOS 7.9.2009

### 软件

| 名称 | 版本 |
| - | - |
| JDK | 1.8.0 |
| Scala | 2.12.11 |
| Spark | 2.4.7 |
| {{nebula.name}} | {{nebula.release}} |

### 数据集

在本示例中，作为数据源的{{nebula.name}}存储着 [basketballplayer 数据集](https://docs.nebula-graph.io/2.0/basketballplayer-2.X.ngql)，其中的 Schema 要素如下表所示。

| 要素  | 名称 | 属性 |
| :--- | :--- | :--- |
| Tag | `player` | `name string, age int` |
| Tag | `team` | `name string` |
| Edge type | `follow` | `degree int` |
| Edge type | `serve` | `start_year int, end_year int` |

## 操作步骤

1. 从 [{{nebula.name}}企业版套餐](https://nebula-graph.com.cn/pricing/) 中获取企业版 Exchange 的 JAR 文件。

2. 修改配置文件。
  
  企业版 Exchange 提供了导出{{nebula.name}}数据专用的配置文件模板`export_to_csv.conf`和`export_to_nebula.conf`，其中各配置项的说明参见 [Exchange 配置](../parameter-reference/ex-ug-parameter.md)。本示例使用的配置文件核心内容如下：
  
  - 导出到 CSV 文件：

  ```conf
  # Use the command to submit the exchange job:
  
  # spark-submit \
  # --master "spark://master_ip:7077" \
  # --driver-memory=2G --executor-memory=30G  \
  # --total-executor-cores=60 --executor-cores=20 \
  # --class com.vesoft.nebula.exchange.Exchange \
  # nebula-exchange-3.0-SNAPSHOT.jar -c export_to_csv.conf
  
  {
    # Spark config
    spark: {
      app: {
        name: {{nebula.name}} Exchange
      }
    }
  
    # Nebula Graph config
    # if you export nebula data to csv, please ignore these nebula config
    nebula: {
      address:{
        graph:["127.0.0.1:9669"]

        # the address of any of the meta services.
        # if your {{nebula.name}} server is in virtual network like k8s, please config the leader address of meta.
        meta:["127.0.0.1:9559"]
      }
      user: root
      pswd: nebula
      space: test
  
      # nebula client connection parameters
      connection {
        # socket connect & execute timeout, unit: millisecond
        timeout: 30000
      }
  
      error: {
        # max number of failures, if the number of failures is bigger than max, then exit the   application.
        max: 32
        # failed data will be recorded in output path, format with ngql
        output: /tmp/errors
      }
  
      # use google's RateLimiter to limit the requests send to {{nebula.name}}
      rate: {
        # the stable throughput of RateLimiter
        limit: 1024
        # Acquires a permit from RateLimiter, unit: MILLISECONDS
        # if it can't be obtained within the specified timeout, then give up the request.
        timeout: 1000
      }
    }
  
    # Processing tags
    tags: [
      {
        # you can ignore the tag name when export nebula data to csv
        name: tag-name-1
        type: {
          source: nebula
          sink: csv
        }
        metaAddress:"127.0.0.1:9559"
        space:"test"
        label:"person"
        # config the fields you want to export from nebula
        fields: [nebula-field-0, nebula-field-1, nebula-field-2]
        noFields:false  # default false, if true, just export id
        partition: 60
        # config the path to save your csv file. if your file in not in hdfs, config "file:///path/  test.csv"
        path: "hdfs://ip:port/path/person"
        separator: ","
        header: true
      }
    ]
  
    # process edges
    edges: [
      {
        # you can ignore the edge name when export nebula data to csv
        name: edge-name-1
        type: {
          source: nebula
          sink: csv
        }
        metaAddress:"127.0.0.1:9559"
        space:"test"
        label:"friend"
        # config the fields you want to export from nebula
        fields: [nebula-field-0, nebula-field-1, nebula-field-2]
        noFields:false  # default false, if true, just export id
        partition: 60
        # config the path to save your csv file. if your file in not in hdfs, config "file:///path/  test.csv"
        path: "hdfs://ip:port/path/friend"
        separator: ","
        header: true
      }
    ]
  }
  ```

  - 导出到另一个图空间：

  ```conf
  # Use the command to submit the exchange job:
  
  # spark-submit \
  # --master "spark://master_ip:7077" \
  # --driver-memory=2G --executor-memory=30G  \
  # --total-executor-cores=60 --executor-cores=20 \
  # --class com.vesoft.nebula.exchange.Exchange \
  # nebula-exchange-3.0-SNAPSHOT.jar -c export_to_nebula.conf
  
  {
    # Spark config
    spark: {
      app: {
        name: {{nebula.name}} Exchange
      }
    }
  
    # Nebula Graph config, just config the sink nebula information
    nebula: {
      address:{
        graph:["127.0.0.1:9669"]

        # the address of any of the meta services.
        # if your {{nebula.name}} server is in virtual network like k8s, please config the leader address of meta.
        meta:["127.0.0.1:9559"]
      }
      user: root
      pswd: nebula
      space: test
  
      # nebula client connection parameters
      connection {
        # socket connect & execute timeout, unit: millisecond
        timeout: 30000
      }
  
      error: {
        # max number of failures, if the number of failures is bigger than max, then exit the   application.
        max: 32
        # failed data will be recorded in output path, format with ngql
        output: /tmp/errors
      }
  
      # use google's RateLimiter to limit the requests send to {{nebula.name}}
      rate: {
        # the stable throughput of RateLimiter
        limit: 1024
        # Acquires a permit from RateLimiter, unit: MILLISECONDS
        # if it can't be obtained within the specified timeout, then give up the request.
        timeout: 1000
      }
    }
  
    # Processing tags
    tags: [
      {
        name: tag-name-1
        type: {
          source: nebula
          sink: client
        }
        # data source nebula config
        metaAddress:"127.0.0.1:9559"
        space:"test"
        label:"person"
        # mapping the fields of the original {{nebula.name}} to the fields of the target {{nebula.name}}.
        fields: [source_nebula-field-0, source_nebula-field-1, source_nebula-field-2]
        nebula.fields: [target_nebula-field-0, target_nebula-field-1, target_nebula-field-2]
        limit:10000
        vertex: _vertexId  # must be `_vertexId`
      # udf:{
      #            separator:"_"
      #            oldColNames:[field-0,field-1,field-2]
      #            newColName:new-field
      #        }
        batch: 2000
        partition: 60
      }
    ]
  
    # process edges
    edges: [
      {
        name: edge-name-1
        type: {
          source: csv
          sink: client
        }
        # data source nebula config
        metaAddress:"127.0.0.1:9559"
        space:"test"
        label:"friend"
        fields: [source_nebula-field-0, source_nebula-field-1, source_nebula-field-2]
        nebula.fields: [target_nebula-field-0, target_nebula-field-1, target_nebula-field-2]
        limit:1000
        source: _srcId # must be `_srcId`
      # udf:{
      #            separator:"_"
      #            oldColNames:[field-0,field-1,field-2]
      #            newColName:new-field
      #        }
        target: _dstId # must be `_dstId`
      # udf:{
      #            separator:"_"
      #            oldColNames:[field-0,field-1,field-2]
      #            newColName:new-field
      #        }
        ranking: source_nebula-field-2
        batch: 2000
        partition: 60
      }
    ]
  }
  ```

3. 使用如下命令导出{{nebula.name}}中的数据。
  
  !!! note

        Driver 和 Executor 进程的相关参数可以根据自身配置灵活修改。

  ```bash
  <spark_install_path>/bin/spark-submit --master "spark://<master_ip>:7077" \
  --driver-memory=2G --executor-memory=30G \
  --total-executor-cores=60 --executor-cores=20 \
  --class com.vesoft.nebula.exchange.Exchange nebula-exchange-x.y.z.jar_path> \
  -c <conf_file_path>
  ```
  
  例如导出到 CSV 文件的示例命令如下。
  
  ```bash
  $ ./spark-submit --master "spark://192.168.10.100:7077" \
  --driver-memory=2G --executor-memory=30G \
  --total-executor-cores=60 --executor-cores=20 \
  --class com.vesoft.nebula.exchange.Exchange ~/exchange-ent/nebula-exchange-ent-{{exchange.release}}.jar \
  -c ~/exchange-ent/export_to_csv.conf
  ```
  
4. 检查导出的数据。

  - 导出到 CSV 文件：
  
    查看目标路径下是否成功生成了 CSV 文件，并检查文件内容。
  
    ```bash
    $ hadoop fs -ls /vertex/player
    Found 11 items
    -rw-r--r--   3 nebula supergroup          0 2021-11-05 07:36 /vertex/player/_SUCCESS
    -rw-r--r--   3 nebula supergroup        160 2021-11-05 07:36 /vertex/player/    part-00000-17293020-ba2e-4243-b834-34495c0536b3-c000.csv
    -rw-r--r--   3 nebula supergroup        163 2021-11-05 07:36 /vertex/player/    part-00001-17293020-ba2e-4243-b834-34495c0536b3-c000.csv
    -rw-r--r--   3 nebula supergroup        172 2021-11-05 07:36 /vertex/player/    part-00002-17293020-ba2e-4243-b834-34495c0536b3-c000.csv
    -rw-r--r--   3 nebula supergroup        172 2021-11-05 07:36 /vertex/player/    part-00003-17293020-ba2e-4243-b834-34495c0536b3-c000.csv
    -rw-r--r--   3 nebula supergroup        144 2021-11-05 07:36 /vertex/player/    part-00004-17293020-ba2e-4243-b834-34495c0536b3-c000.csv
    -rw-r--r--   3 nebula supergroup        173 2021-11-05 07:36 /vertex/player/    part-00005-17293020-ba2e-4243-b834-34495c0536b3-c000.csv
    -rw-r--r--   3 nebula supergroup        160 2021-11-05 07:36 /vertex/player/    part-00006-17293020-ba2e-4243-b834-34495c0536b3-c000.csv
    -rw-r--r--   3 nebula supergroup        148 2021-11-05 07:36 /vertex/player/    part-00007-17293020-ba2e-4243-b834-34495c0536b3-c000.csv
    -rw-r--r--   3 nebula supergroup        125 2021-11-05 07:36 /vertex/player/    part-00008-17293020-ba2e-4243-b834-34495c0536b3-c000.csv
    -rw-r--r--   3 nebula supergroup        119 2021-11-05 07:36 /vertex/player/    part-00009-17293020-ba2e-4243-b834-34495c0536b3-c000.csv
    ```
  
  - 导出到另一个图空间：

    登录新的图空间，通过`SUBMIT JOB STATS`和`SHOW STATS`命令查看统计信息，确认是否导出成功。
