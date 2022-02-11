# 什么是 Nebula Spark Connector

[Nebula Spark Connector](https://github.com/vesoft-inc/nebula-java/tree/v1.0/tools "点击前往 GitHub")（在本手册中简称为 Spark Connector）是一个 Spark 连接器，提供了通过 Spark 标准形式读写 Nebula Graph 数据库的能力，由以下两部分组成：

- Reader：提供了一个 Spark SQL 接口，用户可以使用 Spark SQL 接口编程读取 Nebula Graph 图数据，单次读取一个点或 Edge type 的数据，并将读取的结果组装成 Spark 的 DataFrame。参考 [Nebula Spark Connector Reader](reader/sc-ug-what-is-reader.md)。

- Writer：提供了一个 Spark SQL 接口，用户可以使用 Spark SQL 接口编程将 DataFrame 格式的数据逐条或批量写入 Nebula Graph。参考 [Nebula Spark Connector Writer](writer/sc-ug-what-is-writer.md)。

用户可以将 Nebula Spark Connector 应用于以下场景：

- 在不同的 Nebula Graph 集群之间迁移数据。
- 在同一个 Nebula Graph 集群内不同图空间之间迁移数据。
- Nebula Graph 与其他数据源之间迁移数据。
