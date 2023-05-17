{{ ent.ent_begin }}
# 数据导入导出概述

{{nebula.name}}提供了一套全面的数据导入导出工具集，这些工具在开源社区版本的基础上进行了扩展和优化，旨在满足多样化的数据交互需求。本文列出相关的导入导出工具。
## 导入工具
{{ ent.ent_end }}


{{ comm.comm_begin }}
# 导入工具选择

{{ comm.comm_end}}

有多种方式可以将数据写入{{nebula.name}} {{ nebula.release }}：

- 使用[命令行 -f 的方式](../2.quick-start/3.quick-start-on-premise/3.connect-to-nebula-graph.md)导入：可以导入少量准备好的 nGQL 文件，适合少量手工测试数据准备；
  {{ comm.comm_begin }}
- 使用 [Studio 导入](../nebula-studio/quick-start/st-ug-import-data.md)：可以用过浏览器导入本机多个 csv 文件，格式有限制； 
  {{ comm.comm_end }}
- 使用 [Importer 导入](../nebula-importer/use-importer.md)：导入单机多个 csv 文件，大小没有限制，格式灵活；数据量十亿级以内；
- 使用 [Exchange 导入](../nebula-exchange/about-exchange/ex-ug-what-is-exchange.md)：从 Neo4j, Hive, MySQL 等多种源分布式导入，需要有 Spark 集群；数据量十亿级以上
- 使用 [Spark-connector](../nebula-spark-connector.md)/[Flink-connector](../nebula-flink-connector.md) 导入：有相应组件 (Spark/Flink)，撰写少量代码；
- 使用 [C++/GO/Java/Python SDK](../20.appendix/6.eco-tool-version.md)：编写程序的方式导入，需要有一定编程和调优能力。

下图给出了几种方式的定位：

 ![image](https://docs-cdn.nebula-graph.com.cn/figures/write-choice.png)

{{ ent.ent_begin }}

## 导出工具

目前支持使用[Exchange 导出](../nebula-exchange/use-exchange/ex-ug-export-from-nebula.md)功能将{{nebula.name}} {{ nebula.release }}数据导出至 CSV 文件或另一个图空间（支持不同{{nebula.name}}集群）中。

{{ ent.ent_end }}