# Nebula Spark Connector

Nebula Spark Connector是一个Spark连接器，提供通过Spark标准形式读写Nebula Graph数据的能力。Nebula Spark Connector由Reader和Writer两部分组成。

- Reader
  
  提供一个Spark SQL接口，您可以使用该接口编程读取Nebula Graph图数据，单次读取一个点或边类型的数据，并将读取的结果组装成Spark的DataFrame。

- Writer

  提供一个Spark SQL接口，您可以使用该接口编程将DataFrame格式的数据逐条或批量写入Nebula Graph。

更多使用说明请参见[Nebula Spark Connector](https://github.com/vesoft-inc/nebula-spark-utils/blob/v2.0.0/nebula-spark-connector/README_CN.md)。

## 适用场景

Nebula Spark Connector适用于以下场景：

- 在不同的Nebula Graph集群之间迁移数据。

- 在同一个Nebula Graph集群内不同图空间之间迁移数据。

- Nebula Graph与其他数据源之间迁移数据。

## 优势

- 提供多种连接配置项，如超时时间、连接重试次数、执行重试次数等。

- 提供多种数据配置项，如写入数据时设置对应列为点ID、起始点ID、目的点ID或属性。

- Reader支持无属性读取和全属性读取。

- Reader支持将Nebula Graph数据读取成Graphx的VertexRD和EdgeRDD，支持非Long型点ID。

- Nebula Spark Connector 2.0统一了SparkSQL的扩展数据源，统一采用DataSourceV2进行Nebula Graph数据扩展。