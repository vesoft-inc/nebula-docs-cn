# 什么是 Nebula Flink Connector

[Nebula Flink Connector](https://github.com/vesoft-inc/nebula-java/tree/v1.0/tools "点击前往 GitHub 网站") 是一个自定义的 Flink 连接器，支持 Flink 从 Nebula Graph 图数据库中读取数据（source），或者将其他外部数据源读取的数据写入 Nebula Graph 图数据库（sink）。

用户可以将 Nebula Flink Connector 应用于以下场景：

- 在不同的 Nebula Graph 集群之间迁移数据。
- 在同一个 Nebula Graph 集群内不同图空间之间迁移数据。
- Nebula Graph 与其他数据源之间迁移数据。

用户可以参考以下文档使用 Nebula Flink Connector：

- [使用限制](nf-ug-limitations.md)
- [自定义 source (NebulaSource)](nf-ug-customize-source.md)
- [自定义 sink (NebulaSink)](nf-ug-customize-sink.md)
- [特殊说明](nf-ug-notes.md)
