# 常见问题

**Exchange 支持哪些版本的 Nebula Graph？**

您可以查看 Exchange 的 [使用限制](ex-ug-limitations.md) 获取 Exchange 对 Nebula Graph 的最新支持信息。

**Exchange 与 Spark Writer 有什么关系？**

Exchange 是在 Spark Writer 基础上开发的 Spark 应用程序，二者均适用于在分布式环境中将集群的数据批量迁移到 Nebula Graph 中，但是，后期的维护工作将集中在 Exchange 上。与 Spark Writer 相比，Exchange 有以下改进：

- 支持更丰富的数据源，如 MySQL、Neo4j、Hive、HBase、Kafka、Pulsar 等。
- 修复了 Spark Writer 的部分问题。例如，迁移 HDFS 的源数据时，Spark Writer 输出的 DataFrame 默认为 String 类型，如果 Nebula Graph 的 Schema 中数据类型为 int、double 等，则无法完成数据导入。该问题在 Exchange 中已修复。
