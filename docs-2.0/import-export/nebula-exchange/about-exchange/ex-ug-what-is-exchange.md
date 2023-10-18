# 什么是 NebulaGraph Exchange

[NebulaGraph Exchange](https://github.com/vesoft-inc/nebula-exchange)（简称 Exchange）是一款 Apache Spark&trade; 应用，用于在分布式环境中将集群中的数据批量迁移到{{nebula.name}}中，能支持多种不同格式的批式数据和流式数据的迁移。

Exchange 由 Reader、Processor 和 Writer 三部分组成。Reader 读取不同来源的数据返回 DataFrame 后，Processor 遍历 DataFrame 的每一行，根据配置文件中`fields`的映射关系，按列名获取对应的值。在遍历指定批处理的行数后，Writer 会将获取的数据一次性写入到{{nebula.name}}中。下图描述了 Exchange 完成数据转换和迁移的过程。

![NebulaGraph&reg; Exchange 由 Reader、Processor、Writer 组成，可以完成多种不同格式和来源的数据向{{nebula.name}}的迁移](https://docs-cdn.nebula-graph.com.cn/figures/ex-ug-003.png "NebulaGraph&reg; Exchange 转数据转换和迁移的过程")

## 版本系列

Exchange 有社区版和企业版两个系列，二者功能不同。社区版在 [GitHub](https://github.com/vesoft-inc/nebula-exchange) 开源开发，企业版属于{{nebula.name}}企业套餐。{{ent.ent_begin}}详情参见[版本对比](https://yueshu.com.cn/pricing/)。{{ent.ent_end}}

## 适用场景

Exchange 适用于以下场景：

- 需要将来自 Kafka、Pulsar 平台的流式数据，如日志文件、网购数据、游戏内玩家活动、社交网站信息、金融交易或地理空间服务，以及来自数据中心内所连接设备或仪器的遥测数据等转化为属性图的点或边数据，并导入{{nebula.name}}。

- 需要从关系型数据库（如 MySQL）或者分布式文件系统（如 HDFS）中读取批式数据，如某个时间段内的数据，将它们转化为属性图的点或边数据，并导入{{nebula.name}}。

- 需要将大批量数据生成{{nebula.name}}能识别的 SST 文件，再导入{{nebula.name}}。

- 需要导出{{nebula.name}}中保存的数据。

  !!! enterpriseonly
        仅企业版 Exchange 支持从{{nebula.name}}中导出数据。

## 产品优点

Exchange 具有以下优点：

- 适应性强：支持将多种不同格式或不同来源的数据导入{{nebula.name}}，便于迁移数据。

- 支持导入 SST：支持将不同来源的数据转换为 SST 文件，用于数据导入。

- 支持 SSL 加密：支持在 Exchange 与{{nebula.name}}之间建立 SSL 加密传输通道，保障数据安全。

- 支持断点续传：导入数据时支持断点续传，有助于节省时间，提高数据导入效率。

  !!! Note

        目前仅迁移 Neo4j 数据时支持断点续传。

- 异步操作：会在源数据中生成一条插入语句，发送给 Graph 服务，最后再执行插入操作。

- 灵活性强：支持同时导入多个 Tag 和 Edge type，不同 Tag 和 Edge type 可以是不同的数据来源或格式。

- 统计功能：使用 Apache Spark&trade; 中的累加器统计插入操作的成功和失败次数。

- 易于使用：采用 HOCON（Human-Optimized Config Object Notation）配置文件格式，具有面向对象风格，便于理解和操作。

## 版本兼容性

Exchange 支持 Spark 版本 2.2.x、2.4.x 和 3.x.x，针对不同 Spark 版本命名为：`nebula-exchange_spark_2.2`、`nebula-exchange_spark_2.4`和`nebula-exchange_spark_3.0`。

NebulaGraph Exchange 版本（即 JAR 包版本）、{{nebula.name}}内核版本和 Spark 版本对应关系如下。

| Exchange 版本 | {{nebula.name}}版本 | Spark 版本 |
|:----------|:-----------|:-------|
|nebula-exchange_spark_3.0-3.0-SNAPSHOT.jar|  nightly       |3.3.x、3.2.x、3.1.x、3.0.x |
|nebula-exchange_spark_2.4-3.0-SNAPSHOT.jar|  nightly       |2.4.x |
|nebula-exchange_spark_2.2-3.0-SNAPSHOT.jar|  nightly       |2.2.x |
|nebula-exchange_spark_3.0-3.4.0.jar       | 3.x.x          |3.3.x、3.2.x、3.1.x、3.0.x |
|nebula-exchange_spark_2.4-3.4.0.jar       |  3.x.x         |2.4.x |
|nebula-exchange_spark_2.2-3.4.0.jar       |  3.x.x         |2.2.x |
|nebula-exchange_spark_3.0-3.3.0.jar       |  3.x.x         |3.3.x、3.2.x、3.1.x、3.0.x |
|nebula-exchange_spark_2.4-3.3.0.jar       |  3.x.x         |2.4.x |
|nebula-exchange_spark_2.2-3.3.0.jar       |  3.x.x         |2.2.x |
|nebula-exchange_spark_3.0-3.0.0.jar       |  3.x.x         |3.3.x、3.2.x、3.1.x、3.0.x |
|nebula-exchange_spark_2.4-3.0.0.jar       |  3.x.x         |2.4.x |
|nebula-exchange_spark_2.2-3.0.0.jar       |  3.x.x         |2.2.x |
|nebula-exchange-2.6.3.jar                 |  2.6.1、2.6.0  |2.4.x |
|nebula-exchange-2.6.2.jar                 |  2.6.1、2.6.0  |2.4.x |
|nebula-exchange-2.6.1.jar                 |  2.6.1、2.6.0  |2.4.x |
|nebula-exchange-2.6.0.jar                 |  2.6.1、2.6.0  |2.4.x |
|nebula-exchange-2.5.2.jar                 |  2.5.1、2.5.0  |2.4.x |
|nebula-exchange-2.5.1.jar                 |  2.5.1、2.5.0  |2.4.x |
|nebula-exchange-2.5.0.jar                 |  2.5.1、2.5.0  |2.4.x |
|nebula-exchange-2.1.0.jar                 |  2.0.1、2.0.0  |2.4.x |
|nebula-exchange-2.0.1.jar                 |  2.0.1、2.0.0  |2.4.x |
|nebula-exchange-2.0.0.jar                 |  2.0.1、2.0.0  |2.4.x |

JAR 包有两种获取方式：[自行编译](../ex-ug-compile.md)或者从 maven 仓库下载。

## 数据源

Exchange {{exchange.release}} 支持将以下格式或来源的数据转换为{{nebula.name}}能识别的点和边数据，然后通过 nGQL 语句的形式导入{{nebula.name}}：

- 存储在 HDFS 或本地的数据：
  - [Apache Parquet](../use-exchange/ex-ug-import-from-parquet.md)
  - [Apache ORC](../use-exchange/ex-ug-import-from-orc.md)
  - [JSON](../use-exchange/ex-ug-import-from-json.md)
  - [CSV](../use-exchange/ex-ug-import-from-csv.md)

- [Apache HBase&trade;](../use-exchange/ex-ug-import-from-hbase.md)

- 数据仓库：

  - [Hive](../use-exchange/ex-ug-import-from-hive.md)
  - [MaxCompute](../use-exchange/ex-ug-import-from-maxcompute.md)

- 图数据库：[Neo4j](../use-exchange/ex-ug-import-from-neo4j.md)（Client 版本 2.4.5-M1）

- 关系型数据库：
  - [MySQL](../use-exchange/ex-ug-import-from-mysql.md)
  - [PostgreSQL](../use-exchange/ex-ug-import-from-mysql.md)
  - [Oracle](../use-exchange/ex-ug-import-from-oracle.md)

- 列式数据库：[ClickHouse](../use-exchange/ex-ug-import-from-clickhouse.md)

- 流处理软件平台：[Apache Kafka&reg;](../use-exchange/ex-ug-import-from-kafka.md)

- 发布/订阅消息平台：[Apache Pulsar 2.4.5](../use-exchange/ex-ug-import-from-pulsar.md)

- [JDBC 数据源](../use-exchange/ex-ug-import-from-jdbc.md)

除了用 nGQL 语句的形式导入数据，Exchange 还支持将数据源的数据生成 SST 文件，然后通过 Console [导入 SST 文件](../use-exchange/ex-ug-import-from-sst.md)。

{{ ent.ent_begin }} 

此外，企业版 Exchange 支持以{{nebula.name}}为源，将数据[导出到 CSV 文件或另一个图空间](../use-exchange/ex-ug-export-from-nebula.md)。

 {{ ent.ent_end }}


## 更新说明

[Release](https://github.com/vesoft-inc/nebula-exchange/releases/tag/{{exchange.tag}})

## 视频

* [{{nebula.name}}数据导入工具——Exchange](https://www.bilibili.com/video/BV1Pq4y177D9)（3 分 08 秒）
<iframe src="//player.bilibili.com/player.html?aid=546003709&bvid=BV1Pq4y177D9&cid=352387808&page=1&high_quality=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="720px" height="480px"> </iframe>
