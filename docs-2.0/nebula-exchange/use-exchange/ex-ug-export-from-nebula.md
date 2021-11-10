# 导出Nebula Graph数据

本文以一个示例说明如何使用Exchange将Nebula Graph中的数据导出到CSV文件中。

!!! enterpriseonly

    仅企业版Exchange支持导出Nebula Graph数据到CSV文件。

## 环境准备

本示例在Linux系统的虚拟机环境下完成，导出数据前准备的软硬件信息如下。

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
| Hadoop | 2.10.1 |
| Scala | 2.12.11 |
| Spark | 2.4.7 |
| Nebula Graph | {{nebula.release}} |

### 数据集

在本示例中，作为数据源的Nebula Graph存储着[basketballplayer数据集](https://docs.nebula-graph.io/2.0/basketballplayer-2.X.ngql)，其中的Schema要素如下表所示。

| 要素  | 名称 | 属性 |
| :--- | :--- | :--- |
| Tag | `player` | `name string, age int` |
| Tag | `team` | `name string` |
| Edge type | `follow` | `degree int` |
| Edge type | `serve` | `start_year int, end_year int` |

## 操作步骤

1. 从[Nebula Graph企业版套餐](https://nebula-graph.com.cn/pricing/)中获取企业版Exchange的JAR文件。

2. 修改配置文件。
  
  企业版Exchange提供了导出Nebula Graph数据专用的配置文件模板`export_application.conf`，其中各配置项的说明参见[Exchange配置](../  parameter-reference/ex-ug-parameter.md)。本示例使用的配置文件核心内容如下：
  
  ```conf
  ...
  
    # Processing tags
    # There are tag config examples for different dataSources.
    tags: [
      # export NebulaGraph tag data to csv, only support export to CSV for now.
      {
        name: player
        type: {
          source: Nebula
          sink: CSV
        }
        # the path to save the NebulaGrpah data, make sure the path doesn't exist.
        path:"hdfs://192.168.8.177:9000/vertex/player"
        # if no need to export any properties when export NebulaGraph tag data
        # if noField is configured true, just export vertexId
        noField:false
        # define properties to export from NebulaGraph tag data
        # if return.fields is configured as empty list, then export all properties
        return.fields:[]
        # nebula space partition number
        partition:10
      }
  
  ...
  
    ]
  
    # Processing edges
    # There are edge config examples for different dataSources.
    edges: [
      # export NebulaGraph tag data to csv, only support export to CSV for now.
      {
        name: follow
        type: {
          source: Nebula
          sink: CSV
        }
        # the path to save the NebulaGrpah data, make sure the path doesn't exist.
        path:"hdfs://192.168.8.177:9000/edge/follow"
        # if no need to export any properties when export NebulaGraph edge data
        # if noField is configured true, just export src,dst,rank
        noField:false
        # define properties to export from NebulaGraph edge data
        # if return.fields is configured as empty list, then export all properties
        return.fields:[]
        # nebula space partition number
        partition:10
      }
  
  ...
  
    ]
  }
  ```
  
3. 使用如下命令导出Nebula Graph中的数据。
  
  ```bash
  <spark_install_path>/bin/spark-submit --master "local" --class com.vesoft.nebula.exchange.Exchange nebula-exchange-x.y.z.jar_path> -c <export_application.conf_path>
  ```
  
  本示例使用的导出命令如下。
  
  ```bash
  $ ./spark-submit --master "local" --class com.vesoft.nebula.exchange.Exchange \
    ~/exchange-ent/nebula-exchange-ent-{{exchange.release}}.jar -c ~/exchange-ent/export_application.conf
  ```
  
4. 检查导出的数据。

  1. 查看目标路径下是否成功生成了CSV文件。
  
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
  
  2. 检查CSV文件内容，确定数据导出成功。
