# Nebula Spark Connector Writer 应用示例

本文以一个示例说明如何使用 Nebula Spark Connector Writer 向 Nebula Graph 写入点和边数据。

## 前提条件

使用 Nebula Spark Connector Writer 前，用户需要确认以下信息：

- 机器上已经安装了以下软件：
  - Apache Spark&trade; 2.3.0 及更高版本
  - Scala
  - Java：1.8

- 已经成功编译 Nebula Spark Connector，并已经将 `nebula-spark-1.x.y.jar` 复制到本地 Maven 库。详细信息参考[编译 Nebula Spark Connector](../sc-ug-compile.md)。

- 待写入的点和边数据源。在本示例中所用的数据源为 JSON 文件，用户可以从 [nebula-java 库](https://github.com/vesoft-inc/nebula-java/tree/v1.0/examples/src/main/resources "点击前往 GitHub 网站") 中下载。

- Nebula Graph 的 Graph 服务 IP 地址及端口号。在本示例中，对应的信息为 `127.0.0.1:3699`。

- 在 Nebula Graph 中创建 Schema，并获取以下信息：
  - 图空间名称和分区数量。在本示例中，对应的信息为 `nb` 和 `100`。
  - 点的信息，包括 Tag 和 VID 映射策略（`hash`<!--或者 `uuid`-->）。
  - 边的信息，包括起点和终点对应的 Tag，以及 VID 映射策略（`hash`<!--或者 `uuid`-->）。

- （可选）如果是批量写入，需要确认单次写入的最大数据条数，默认为 2000。详见本文 `batchInsert` 配置项说明。

## 操作步骤

参考以下步骤使用 Nebula Spark Connector Writer 向 Nebula Graph 写入数据。

### 第 1 步

在 Maven 项目的 POM 文件中加入 `nebula-spark` 依赖。

```pom
<dependency>
  <groupId>com.vesoft</groupId>
  <artifactId>nebula-spark</artifactId>
  <version>1.x.y</version>
</dependency>
```

!!! Note

    `<version>` 建议配置为最新发布的 Nebula Java Client 版本号。用户可以在 [nebula-java 仓库的 Releases 页面](https://github.com/vesoft-inc/nebula-java/releases "点击前往 GitHub 网站") 查看最新的 v1.x 版本。

### 第 2 步

根据逐条或批量写入需求，参考以下示例在 Spark 应用程序中完成配置。

#### 逐条写入数据

示例代码如下：

```shell
// 构造点和边数据的 DataFrame，
// 这里使用 nebula-java 库 v1.0 分支里 nebula-java/examples/src/main/resources 目录下的示例数据，
// 示例数据在本地的存储路径为 examples/src/main/resources
  val vertexDF = spark.read.json("examples/src/main/resources/vertex")
      vertexDF.show()
  val edgeDF = spark.read.json("examples/src/main/resources/edge")
      edgeDF.show()

// 写入点
  vertexDF.write
    .nebula("127.0.0.1:3699", "nb", "100")
    .writeVertices("player", "vertexId", "hash")
  
// 写入边
  edgeDF.write
    .nebula("127.0.0.1:3699", "nb", "100")
    .wirteEdges("follow", "src_id", "dst_id")
```

示例代码中的配置说明如下：

- `nebula(address: String, space: String, partitionNum: String)`
  - `address`：Nebula Graph 的 Graph 服务地址及端口，可以配置多个地址，以英文逗号分隔，如 `“ip1:port,ip2:port”`，端口默认为 `3699`。
  - `space`：Nebula Graph 中即将写入数据的图空间名称。
  - `partitionNum`：在 Nebula Graph 中创建图空间时指定的 `partitionNum` 的值。如果未指定，这里填写 `100`。

- `writeVertices(tag: String, vertexField: String, policy: String = "")`
  - `tag`：点对应的 Nebula Graph 图空间中的 Tag 名称。
  - `vertexField`：DataFrame 中可作为 Nebula Graph 点 VID 的列。例如，如果 DataFrame 有三列，分别为 a、b、c，其中 a 列作为点 VID 列，则该参数设置为 `"a"`。
  - `policy`：如果 DataFrame 中 `vertexField` 列的数据类型非数值型，则需要配置 Nebula Graph 中 VID 的映射策略，即该参数设置为 `"hash"`<!--或者 `uuid`-->。如果 `vertexField` 列的数据类型为整数型，则不需要配置。

- `writeEdges(edge: String, srcVertexField: String, dstVertexField: String, policy: String = "")`
  - `edge`：边对应的 Nebula Graph 图空间中的 Edge type 名称。
  - `srcVertexField` 和 `dstVertexField`：DataFrame 中可作为边起点和边终点的列。列值必须同为整数型或同为非数值型。
  - `policy`：如果 DataFrame 中 `srcVertexField` 列和 `dstVertexField` 列的数据类型非数值型，则需要配置 Nebula Graph 中 VID 的映射策略，即该参数设置为  `"hash"`<!--或者 `uuid`-->。如果 `srcVertexField` 列和 `dstVertexField` 列的数据类型为整数型，则不需要配置。

#### 批量写入数据

示例代码如下：

```shell
// 构造点和边数据的 DataFrame，
// 这里使用 nebula-java 库 v1.0 分支里 nebula-java/examples/src/main/resources 目录下的示例数据，
// 示例数据在本地的存储路径为 examples/src/main/resources
val vertexDF = spark.read.json("examples/src/main/resources/vertex")
  vertexDF.show()
val edgeDF = spark.read.json("examples/src/main/resources/edge")
  edgeDF.show()

// 批量写入点
new NebulaBatchWriterUtils()
      .batchInsert("127.0.0.1:3699", "nb", 2000)
      .batchToNebulaVertex(vertexDF, "player", "vertexId")
  
// 批量写入边
new NebulaBatchWriterUtils()
      .batchInsert("127.0.0.1:3699", "nb", 2000)
      .batchToNebulaEdge(edgeDF, "follow", "source", "target")
```

示例代码中的配置说明如下：

- `batchInsert(address: String, space: String, batch: Int = 2000)`：
  - `address`：Nebula Graph 的 Graph 服务地址及端口，可以配置多个地址，以英文逗号分隔，如 `“ip1:port,ip2:port”`，端口默认为 `3699`。
  - `space`：Nebula Graph 中即将写入数据的图空间名称。
  - `batch`：批量写入时一批次的数据条数，可选，默认为 2000。

- `batchToNebulaVertex(data: DataFrame, tag: String, vertexField: String, policy: String = "")`：
  - `data`：待写入 Nebula Graph 的 DataFrame 数据。
  - `tag`：Nebula Graph 图空间中对应的 Tag 名称。
  - `vertexField`：DataFrame 中可作为 Nebula Graph 点 VID 的列。例如，如果 DataFrame 有三列，分别为 a、b、c，其中 a 列作为点 VID 列，则该参数设置为 `"a"`。
  - `policy`：如果 DataFrame 中 `vertexField` 列的数据类型非数值型，则需要配置 Nebula Graph 中 VID 的映射策略，即该参数设置为 `"hash"`<!--或者 `uuid`-->。如果 `vertexField` 列的数据类型为整数型，则不需要配置。

- `batchToNebulaEdge(data: DataFrame,  edge: String, srcVertexField: String, dstVertexField: String, rankField: String = "",  policy: String = "")`：
  - `data`：待写入 Nebula Graph 的 DataFrame 数据。
  - `edge`：Nebula Graph 中对应的 Edge type。
  - `srcVertexField` 和 `dstVertexField`：DataFrame 中可作为边起点和边终点的列。列值必须同为整数型或同为非数值型。
  - `rankField`：DataFrame 中可作为边 `rank` 值的列，可选配。
  - `policy`：可选。如果 DataFrame 中 `srcVertexField` 列和 `dstVertexField` 列的数据类型非数值型，则需要配置 Nebula Graph 中 VID 的映射策略，即该参数设置为  `"hash"`<!--或者 `uuid`-->。如果 `srcVertexField` 列和 `dstVertexField` 列的数据类型为整数型，则不需要配置。
