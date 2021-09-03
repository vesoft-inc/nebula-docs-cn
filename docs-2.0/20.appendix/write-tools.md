# 导入工具选择

有多种方式可以写入Nebula Graph {{ nebula.release }}：

- 使用 [命令行 -f 的方式](../2.quick-start/3.connect-to-nebula-graph.md)导入: 可以导入少量准备好的nGQL文件，适合少量手工测试数据准备；
- 使用 [studio 导入](../nebula-studio/quick-start/st-ug-import-data.md): 可以用过浏览器导入本机多个 csv 文件，单个文件不超过 100 MB，格式有限制； 
- 使用 [importer 导入](../nebula-importer/use-importer.md): 导入单机多个 csv 文件，大小没有限制，格式灵活；
- 使用 [Exchange 导入](../nebula-exchange/about-exchange/ex-ug-what-is-exchange.md): 从 Neo4j, Hive, MySQL等多种源分布式导入，需要有 Spark 集群；
- 使用 [Spark-connector](../nebula-spark-connector.md)/[Flink-connector](../nebula-flink-connector.md) 导入：有相应组件(Spark/Flink)，撰写少量代码；
- 使用 [C++/GO/Java/Python SDK](../20.appendix/6.eco-tool-version.md)：编写程序的方式导入，需要有一定编程和调优能力。

下图给出了几种方式的定位：

 ![image](../images/write-choice.png)

