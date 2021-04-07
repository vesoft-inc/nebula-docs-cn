# 常见问题

**Exchange 支持哪些版本的 Nebula Graph？**

您可以查看 Exchange 的 [使用限制](ex-ug-limitations.md) 获取 Exchange 对 Nebula Graph 的最新支持信息。

**Exchange 与 Spark Writer 有什么关系？**

Exchange 是在 Spark Writer 基础上开发的 Spark 应用程序，二者均适用于在分布式环境中将集群的数据批量迁移到 Nebula Graph 中，但是，后期的维护工作将集中在 Exchange 上。与 Spark Writer 相比，Exchange 有以下改进：

- 支持更丰富的数据源，如 MySQL、Neo4j、Hive、HBase、Kafka、Pulsar 等。

- 修复了 Spark Writer 的部分问题。例如，Spark 读取 HDFS 里的数据时，默认读取到的源数据均为 String 类型，可能与 Nebula Graph 定义的 Schema 不同，所以，Exchange 增加了数据类型的自动匹配和类型转换，当 Nebula Graph 定义的 Schema 中数据类型为非 String 类型（如 double）时，Exchange 会将 String 类型的源数据转换为对应的类型（如 double）。
