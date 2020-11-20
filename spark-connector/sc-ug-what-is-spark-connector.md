# 什么是 Nebula Spark Connector

[Nebula Spark Connector](https://github.com/vesoft-inc/nebula-java/tree/master/tools/nebula-spark)（在本手册中简称为 Spark Connector）是一个 Spark 连接器，提供了通过 Spark 标准形式读写 Nebula Graph 数据库的能力，由以下两部分组成：

- Reader：为您提供了一个 Spark SQL 接口，您可以使用 Spark SQL 接口编程读取 Nebula Graph 图数据，单次读取一个点或边类型的数据，并将读取的结果组装成 Spark 的 DataFrame。参考 [Nebula Spark Connector Reader](reader/screader-ug-what-is-sparkconnector-reader.md)。

- Writer：为您提供了一个 Spark SQL 接口，您可以使用 Spark SQL 接口编程将 DataFrame 格式的数据写入 Nebula Graph。参考 [Nebula Spark Connector Writer](writer/scwriter-ug-what-is-sparkconnector-writer.md)。
