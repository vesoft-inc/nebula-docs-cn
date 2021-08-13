# Nebula Spark Connector

Nebula Spark Connector是一个Spark连接器，提供通过Spark标准形式读写Nebula Graph数据的能力。Nebula Spark Connector由Reader和Writer两部分组成。

- Reader
  
  提供一个Spark SQL接口，用户可以使用该接口编程读取Nebula Graph图数据，单次读取一个点或Edge type的数据，并将读取的结果组装成Spark的DataFrame。

- Writer

  提供一个Spark SQL接口，用户可以使用该接口编程将DataFrame格式的数据逐条或批量写入Nebula Graph。

更多使用说明请参见[Nebula Spark Connector](https://github.com/vesoft-inc/nebula-spark-utils/blob/{{sparkconnector.branch}}/nebula-spark-connector/README_CN.md)。

## 适用场景

Nebula Spark Connector适用于以下场景：

- 在不同的Nebula Graph集群之间迁移数据。

- 在同一个Nebula Graph集群内不同图空间之间迁移数据。

- Nebula Graph与其他数据源之间迁移数据。

- 结合[Nebula Algorithm](nebula-algorithm.md)进行图计算。

## 特性

Nebula Spark Connector {{sparkconnector.release}}版本特性如下：

- 提供多种连接配置项，如超时时间、连接重试次数、执行重试次数等。

- 提供多种数据配置项，如写入数据时设置对应列为点ID、起始点ID、目的点ID或属性。

- Reader支持无属性读取和全属性读取。

- Reader支持将Nebula Graph数据读取成Graphx的VertexRDD和EdgeRDD，支持非Long型点ID。

- Nebula Spark Connector 2.0统一了SparkSQL的扩展数据源，统一采用DataSourceV2进行Nebula Graph数据扩展。

- 支持`insert`和`update`两种写入模式。`insert`模式会插入（覆盖）数据，`update`模式仅会更新已存在的数据。

## 获取Nebula Spark Connector

### 编译打包

1. 克隆仓库`nebula-spark-utils`。

  ```bash
  $ git clone -b {{sparkconnector.release}} https://github.com/vesoft-inc/nebula-spark-utils.git
  ```

2. 进入目录`nebula-spark-connector`。

  ```bash
  $ cd nebula-spark-utils/nebula-spark-connector
  ```

3. 编译打包。

  ```bash
  $ mvn clean package -Dmaven.test.skip=true -Dgpg.skip -Dmaven.javadoc.skip=true
  ```

编译完成后，在目录`nebula-spark-connector/target`下生成类似文件`nebula-spark-connector-{{sparkconnector.release}}-SHANPSHOT.jar`。

### Maven远程仓库下载

[下载地址](https://repo1.maven.org/maven2/com/vesoft/nebula-spark-connector/)

## 使用方法

使用Nebula Spark Connector读写Nebula Graph数据库时，只需要编写以下代码即可实现。

```scala
# 从Nebula Graph读取点边数据。
spark.read.nebula().loadVerticesToDF()
spark.read.nebula().loadEdgesToDF()
 
# 将dataframe数据作为点和边写入Nebula Graph中。
dataframe.write.nebula().writeVertices()
dataframe.write.nebula().writeEdges()
```

`nebula()`接收两个配置参数，包括连接配置和读写配置。

### 从Nebula Graph读取数据

```scala
val config = NebulaConnectionConfig
  .builder()
  .withMetaAddress("127.0.0.1:9559")
  .withConenctionRetry(2)
  .withExecuteRetry(2)
  .withTimeout(6000)
  .build()
     
val nebulaReadVertexConfig: ReadNebulaConfig = ReadNebulaConfig
  .builder()
  .withSpace("test")
  .withLabel("person")
  .withNoColumn(false)
  .withReturnCols(List("birthday"))
  .withLimit(10)
  .withPartitionNum(10)
  .build()
val vertex = spark.read.nebula(config, nebulaReadVertexConfig).loadVerticesToDF()
  
val nebulaReadEdgeConfig: ReadNebulaConfig = ReadNebulaConfig
  .builder()
  .withSpace("test")
  .withLabel("knows")
  .withNoColumn(false)
  .withReturnCols(List("degree"))
  .withLimit(10)
  .withPartitionNum(10)
  .build()
val edge = spark.read.nebula(config, nebulaReadEdgeConfig).loadEdgesToDF()
```

- `NebulaConnectionConfig`是连接Nebula Graph的配置，说明如下。

  |参数|是否必须|说明|
  |:---|:---|:---|
  |`withMetaAddress`  |是| 所有Meta服务的地址，多个地址用英文逗号（,）隔开，格式为`ip1:port1,ip2:port2,...`。读取数据不需要配置`withGraphAddress`。  |
  |`withConnectionRetry`  |否| Nebula Java Client连接Nebula Graph的重试次数。默认值为`1`。  |
  |`withExecuteRetry`  |否| Nebula Java Client执行查询语句的重试次数。默认值为`1`。  |
  |`withTimeout`  |否| Nebula Java Client请求响应的超时时间。默认值为`6000`，单位：毫秒（ms）。  |

- `ReadNebulaConfig`是读取Nebula Graph数据的配置，说明如下。

  |参数|是否必须|说明|
  |:---|:---|:---|
  |`withSpace`  |是|  Nebula Graph图空间名称。  |
  |`withLabel`  |是|  Nebula Graph图空间内的Tag或Edge type名称。  |
  |`withNoColumn`  |否|  是否不读取属性。默认值为`false`，表示读取属性。取值为`true`时，表示不读取属性，此时`withReturnCols`配置无效。  |
  |`withReturnCols`  |否|  配置要读取的点或边的属性集。格式为`List(property1,property2,...)`，默认值为`List()`，表示读取全部属性。  |
  |`withLimit`  |否|  配置Nebula Java Storage Client一次从服务端读取的数据行数。默认值为1000。  |
  |`withPartitionNum`  |否|  配置读取Nebula Graph数据时Spark的分区数。默认值为100。该值的配置最好不超过图空间的的分片数量（partition_num）。|

### 向Nebula Graph写入数据

```scala
val config = NebulaConnectionConfig
  .builder()
  .withMetaAddress("127.0.0.1:9559")
  .withGraphAddress("127.0.0.1:9669")
  .withConenctionRetry(2)
  .build()
 
val nebulaWriteVertexConfig: WriteNebulaVertexConfig = WriteNebulaVertexConfig      
  .builder()
  .withSpace("test")
  .withTag("person")
  .withVidField("id")
  .withVidPolicy("hash")
  .withVidAsProp(true)
  .withUser("root")
  .withPasswd("nebula")
  .withBatch(1000)
  .build()    
df.write.nebula(config, nebulaWriteVertexConfig).writeVertices()
  
val nebulaWriteEdgeConfig: WriteNebulaEdgeConfig = WriteNebulaEdgeConfig      
  .builder()
  .withSpace("test")
  .withEdge("friend")
  .withSrcIdField("src")
  .withSrcPolicy(null)
  .withDstIdField("dst")
  .withDstPolicy(null)
  .withRankField("degree")
  .withSrcAsProperty(true)
  .withDstAsProperty(true)
  .withRankAsProperty(true)
  .withUser("root")
  .withPasswd("nebula")
  .withBatch(1000)
  .build()
df.write.nebula(config, nebulaWriteEdgeConfig).writeEdges()
```

默认写入模式为`insert`，可以通过`withWriteMode`配置修改为`update`：

```scala
val config = NebulaConnectionConfig
  .builder()
  .withMetaAddress("127.0.0.1:9559")
  .withGraphAddress("127.0.0.1:9669")
  .build()
val nebulaWriteVertexConfig = WriteNebulaVertexConfig
  .builder()
  .withSpace("test")
  .withTag("person")
  .withVidField("id")
  .withVidAsProp(true)
  .withBatch(1000)
  .withWriteMode(WriteMode.UPDATE)
  .build()
df.write.nebula(config, nebulaWriteVertexConfig).writeVertices()
```

- `NebulaConnectionConfig`是连接Nebula Graph的配置，说明如下。

  |参数|是否必须|说明|
  |:---|:---|:---|
  |`withMetaAddress`  |是| 所有Meta服务的地址，多个地址用英文逗号（,）隔开，格式为`ip1:port1,ip2:port2,...`。 |
  |`withGraphAddress`  |是| Graph服务的地址，多个地址用英文逗号（,）隔开，格式为`ip1:port1,ip2:port2,...`。 |
  |`withConnectionRetry`  |否| Nebula Java Client连接Nebula Graph的重试次数。默认值为`1`。  |

- `WriteNebulaVertexConfig`是写入点的配置，说明如下。

  |参数|是否必须|说明|
  |:---|:---|:---|
  |`withSpace`  |是|  Nebula Graph图空间名称。  |
  |`withTag`  |是|  写入点时需要关联的Tag名称。  |
  |`withVidField`  |是|  DataFrame中作为点ID的列。  |
  |`withVidPolicy`  |否|  写入点ID时，采用的映射函数，Nebula Graph 2.0仅支持HASH。默认不做映射。  |
  |`withVidAsProp`  |否|  DataFrame中作为点ID的列是否也作为属性写入。默认值为`false`。如果配置为`true`，请确保Tag中有和`VidField`相同的属性名。  |
  |`withUser`  |否|  Nebula Graph用户名。若未开启[身份验证](7.data-security/1.authentication/1.authentication.md)，无需配置用户名和密码。   |
  |`withPasswd`  |否|  Nebula Graph用户名对应的密码。  |
  |`withBatch`  |是|  一次写入的数据行数。默认值为`1000`.  |
  |`withWriteMode`|否|写入模式。可选值为`insert`和`update`。默认为`insert`。|

- `WriteNebulaEdgeConfig`是写入边的配置，说明如下。

  |参数|是否必须|说明|
  |:---|:---|:---|
  |`withSpace`  |是|  Nebula Graph图空间名称。  |
  |`withEdge`  |是|  写入边时需要关联的Edge type名称。  |
  |`withSrcIdField`  |是|  DataFrame中作为起始点的列。  |
  |`withSrcPolicy`  |否| 写入起始点时，采用的映射函数，Nebula Graph 2.0仅支持HASH。默认不做映射。   |
  |`withDstIdField`  |是| DataFrame中作为目的点的列。   |
  |`withDstPolicy`  |否| 写入目的点时，采用的映射函数，Nebula Graph 2.0仅支持HASH。默认不做映射。   |
  |`withRankField`  |否| DataFrame中作为rank的列。默认不写入rank。   |
  |`withSrcAsProperty`  |否| DataFrame中作为起始点的列是否也作为属性写入。默认值为`false`。如果配置为`true`，请确保Edge type中有和`SrcIdField`相同的属性名。   |
  |`withDstAsProperty`  |否| DataFrame中作为目的点的列是否也作为属性写入。默认值为`false`。如果配置为`true`，请确保Edge type中有和`DstIdField`相同的属性名。   |
  |`withRankAsProperty`  |否| DataFrame中作为rank的列是否也作为属性写入。默认值为`false`。如果配置为`true`，请确保Edge type中有和`RankField`相同的属性名。   |
  |`withUser`  |否|  Nebula Graph用户名。若未开启[身份验证](7.data-security/1.authentication/1.authentication.md)，无需配置用户名和密码。  |
  |`withPasswd`  |否|  Nebula Graph用户名对应的密码。  |
  |`withBatch`  |是|  一次写入的数据行数。默认值为`1000`.  |
  |`withWriteMode`|否|写入模式。可选值为`insert`和`update`。默认为`insert`。|
