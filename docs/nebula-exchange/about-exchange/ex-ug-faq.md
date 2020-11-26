# 常见问题

**Exchange 支持哪些版本的 Nebula Graph？**

你可以查看 Exchange 的 [使用限制](ex-ug-limitations.md) 获取 Exchange 对 Nebula Graph 的最新支持信息。

**Exchange 与 Spark Writer 有什么关系？**

Exchange 是在 Spark Writer 的基础上开发的 Spark 应用程序，都是用于在分布式环境中将集群中的数据批量迁移到 Nebula Graph 中，但是，后期的维护工作将集中在 Exchange 上。与 Spark Writer 相比，Exchange 有以下改进：

- 支持更丰富的数据源，如 MySQL、Neo4j、Hive、HBase、Kafka、Pulsar 等。
- 修复了 Spark Writer 里的部分问题。例如，Spark Writer 将存储在 HDFS 的文件读成 DataFrame 后默认数据类型为 String，如果 Nebula Graph 的 Schema 中数据类型为 int、double 等，则无法完成导入。该问题在 Exchange 中已修复。
