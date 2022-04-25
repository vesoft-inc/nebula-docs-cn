# Nebula Algorithm

[Nebula Algorithm](https://github.com/vesoft-inc/nebula-algorithm) （简称 Algorithm）是一款基于 [GraphX](https://spark.apache.org/graphx/) 的 Spark 应用程序，通过提交 Spark 任务的形式使用完整的算法工具对 Nebula Graph 数据库中的数据执行图计算，也可以通过编程形式调用 lib 库下的算法针对 DataFrame 执行图计算。

## 版本兼容性

Nebula Algorithm 版本和 Nebula Graph 内核的版本对应关系如下。

|Algorithm client 版本|Nebula Graph 版本|
|:---|:---|
|3.0-SNAPSHOT         |  nightly       |
|{{algorithm.release}}|  {{nebula.release}}  |
|  2.6.x              |  2.6.x  |
|  2.5.0              |  2.5.0、2.5.1  |
|  2.1.0              |  2.0.0、2.0.1  |



## 前提条件

在使用 Algorithm 之前，用户需要确认以下信息：

- Nebula Graph 服务已经部署并启动。详细信息，参考 [Nebula Graph 安装部署](4.deployment-and-installation/1.resource-preparations.md "点击前往 Nebula Graph 安装部署")。

- Spark 版本为 2.4.x。

- Scala 版本为 2.11。

- （可选）如果用户需要在 Github 中克隆最新的 Algorithm，并自行编译打包，可以选择安装 [Maven](https://maven.apache.org/download.cgi)。

## 使用限制

- 直接提交算法包时，点 ID 的数据必须为整数，即点 ID 可以是 INT 类型，或者是 String 类型但数据本身为整数。

- 对于非整数的 String 类型数据，推荐使用调用算法接口的方式，可以使用 SparkSQL 的`dense_rank`函数进行编码，将 String 类型转换为 Long 类型。

- 图计算会输出点的数据集，算法结果会以DataFrame形式作为点的属性存储。用户可以根据业务需求，自行对算法结果做进一步操作，例如统计、筛选。

## 支持算法

Nebula Algorithm 支持的图计算算法如下。

 |           算法名          |说明|应用场景|属性名称      |属性数据类型|
 |:------------------------|:-----------|:----|:---|:---|
 |         PageRank         |  页面排序  | 网页排序、重点节点挖掘|  pagerank        |double/string|
 |         Louvain          |  社区发现  | 社团挖掘、层次化聚类| louvain        | int/string  |
 |          KCore           |    K 核    |社区发现、金融风控|          kcore         | int/string  |
 |     LabelPropagation     |  标签传播  |资讯传播、广告推荐、社区发现|         lpa           | int/string  |
 |         Hanp             |标签传播进阶版|社区发现、推荐       |         hanp         | int/string  |
 |    ConnectedComponent    |  联通分量  |社区发现、孤岛发现|     cc           | int/string  |
 |StronglyConnectedComponent| 强联通分量  |社区发现|          scc          | int/string  |
 |       ShortestPath       |  最短路径   |路径规划、网络规划|      shortestpath     |   string    |
 |       TriangleCount      | 三角形计数  |网络结构分析|      trianglecount     | int/string  |
 |  GraphTriangleCount      | 全图三角形计数 |网络结构及紧密程度分析|
 |   BetweennessCentrality  | 中介中心性  |关键节点挖掘，节点影响力计算|       betweenness     |double/string|
 |   ClosenessCentrality    | 接近中心性  |关键节点挖掘、节点影响力计算|       closeness       |double/string|
 |        DegreeStatic      |   度统计   |图结构分析|degree,inDegree,outDegree| int/string  |
 | ClusteringCoefficient    | 聚集系数    |推荐、电信诈骗分析|   clustercoefficient   |double/string|
 |       Jaccard            | 杰卡德相似度计算| 相似度计算、推荐|     jaccard        |    string   |
 |         BFS              | 广度优先遍历| 层序遍历、最短路径规划|      bfs          |    string   |
 |       Node2Vec           |     -     | 图分类         |       node2vec       |    string   |

!!! note

    如果需要将算法结果写入到 Nebula Graph 中，请确保对应图空间中的 Tag 有和上表对应的属性名称和数据类型。

## 实现方法

Nebula Algorithm 实现图计算的流程如下：

1. 利用 Nebula Spark Connector 从 Nebula Graph 数据库中读取图数据为 DataFrame。

2. 将 DataFrame 转换为 GraphX 的图。

3. 调用 GraphX 提供的图算法（例如 PageRank）或者自行实现的算法（例如 Louvain 社区发现）。

详细的实现方法可以参见相关 [Scala 文件](https://github.com/vesoft-inc/nebula-algorithm/tree/master/nebula-algorithm/src/main/scala/com/vesoft/nebula/algorithm/lib)。

## 获取 Nebula Algorithm

### 编译打包

1. 克隆仓库`nebula-algorithm`。

  ```bash
  $ git clone -b {{algorithm.branch}} https://github.com/vesoft-inc/nebula-algorithm.git
  ```

2. 进入目录`nebula-algorithm`。

  ```bash
  $ cd nebula-algorithm
  ```

3. 编译打包。

  ```bash
  $ mvn clean package -Dgpg.skip -Dmaven.javadoc.skip=true -Dmaven.test.skip=true
  ```

编译完成后，在目录`nebula-algorithm/target`下生成类似文件`nebula-algorithm-3.x.x.jar`。

### Maven 远程仓库下载

[下载地址](https://repo1.maven.org/maven2/com/vesoft/nebula-algorithm/)

## 使用方法

### 调用算法接口（推荐）

`lib`库中提供了 10 种常用图计算算法，用户可以通过编程调用的形式调用算法。

1. 在文件`pom.xml`中添加依赖。

  ```bash
  <dependency>
       <groupId>com.vesoft</groupId>
       <artifactId>nebula-algorithm</artifactId>
       <version>{{algorithm.release}}</version>
  </dependency>
  ```

2. 传入参数调用算法（以 PageRank 为例）。更多调用示例请参见[示例](https://github.com/vesoft-inc/nebula-algorithm/tree/master/example/src/main/scala/com/vesoft/nebula/algorithm)。

  !!! note

        执行算法的 DataFrame 默认第一列是起始点，第二列是目的点，第三列是边权重（非 Nebula Graph 中的 Rank）。

  ```bash
  val prConfig = new PRConfig(5, 1.0)
  val louvainResult = PageRankAlgo.apply(spark, data, prConfig, false)
  ```

  如果用户的节点 ID 是 String 类型，可以参考 PageRank 的[示例](https://github.com/vesoft-inc/nebula-algorithm/blob/master/example/src/main/scala/com/vesoft/nebula/algorithm/PageRankExample.scala)。示例中进行了 ID 转换，将 String 类型编码为 Long 类型， 并在算法结果中将 Long 类型 ID 解码为原始的 String 类型。

### 直接提交算法包
  
!!! note
    使用封装好的算法包有一定的局限性，例如落库到 Nebula Graph 时，落库的图空间中创建的 Tag 的属性名称必须和代码内预设的名称保持一致。如果用户有开发能力，推荐使用第一种方法。

1. 设置[配置文件](https://github.com/vesoft-inc/nebula-algorithm/blob/{{algorithm.branch}}/nebula-algorithm/src/main/resources/application.conf)。

  ```bash
  {
      # Spark 相关配置
      spark: {
      app: {
          name: LPA
          # Spark 分片数量
          partitionNum:100
      }
      master:local
      }

      data: {
      # 数据源，可选值为 nebula、csv、json。
      source: nebula
      # 数据落库，即图计算的结果写入的目标，可选值为 nebula、csv、json。
      sink: nebula
      # 算法是否需要权重。
      hasWeight: false
      }
 
      # Nebula Graph 相关配置
      nebula: {
      # 数据源。Nebula Graph 作为图计算的数据源时，nebula.read 的配置才生效。
      read: {
          # 所有 Meta 服务的 IP 地址和端口，多个地址用英文逗号（,）分隔。格式："ip1:port1,ip2:port2"。
          # 使用 docker-compose 部署，端口需要填写 docker-compose 映射到外部的端口
          # 可以用`docker-compose ps`查看
          metaAddress: "192.168.*.10:9559"
          # Nebula Graph 图空间名称
          space: basketballplayer
          # Nebula Graph Edge type, 多个 labels 时，多个边的数据将合并。
          labels: ["serve"]
          # Nebula Graph 每个 Edge type 的属性名称，此属性将作为算法的权重列，请确保和 Edge type 对应。
          weightCols: ["start_year"]
      }
 
      # 数据落库。图计算结果落库到 Nebula Graph 时，nebula.write 的配置才生效。
      write:{
          # Graph 服务的 IP 地址和端口，多个地址用英文逗号（,）分隔。格式："ip1:port1,ip2:port2"。
          # 使用 docker-compose 部署，端口需要填写 docker-compose 映射到外部的端口
          # 可以用`docker-compose ps`查看
          graphAddress: "192.168.*.11:9669"
          # 所有 Meta 服务的 IP 地址和端口，多个地址用英文逗号（,）分隔。格式："ip1:port1,ip2:port2"。
          # 使用 docker-compose 部署，端口需要填写 docker-compose 映射到外部的端口
          # 可以用`docker-compose ps`查看
          metaAddress: "192.168.*.12:9559"
          user:root
          pswd:nebula
          # 在提交图计算任务之前需要自行创建图空间及 Tag
          # Nebula Graph 图空间名称
          space:nb
          # Nebula Graph Tag 名称，图计算结果会写入该 Tag。Tag 中的属性名称固定如下：
          # PageRank：pagerank
          # Louvain：louvain
          # ConnectedComponent：cc
          # StronglyConnectedComponent：scc
          # LabelPropagation：lpa
          # ShortestPath：shortestpath
          # DegreeStatic：degree、inDegree、outDegree
          # KCore：kcore
          # TriangleCount：tranglecpunt
          # BetweennessCentrality：betweennedss
          tag:pagerank
      }
      }  

      local: {
      # 数据源。图计算的数据源为 csv 文件或 json 文件时，local.read 的配置才生效。
      read:{
          filePath: "hdfs://127.0.0.1:9000/edge/work_for.csv"
          # 如果 CSV 文件没有表头，使用 [_c0, _c1, _c2, ..., _cn] 表示其表头，有表头或者是 json 文件时，直接使用表头名称即可。
          # 起始点 ID 列的表头。
          srcId:"_c0"
          # 目的点 ID 列的表头。
          dstId:"_c1"
          # 权重列的表头
          weight: "_c2"
          # csv 文件是否有表头
          header: false
          # csv 文件的分隔符
          delimiter:","
      }

      # 数据落库。图计算结果落库到 csv 文件或 text 文件时，local.write 的配置才生效。
      write:{
          resultPath:/tmp/
      }

      algorithm: {
      # 需要执行的算法，可选值为：
      # pagerank、louvain、connectedcomponent、labelpropagation、shortestpaths、
      # degreestatic、kcore、stronglyconnectedcomponent、trianglecount、
      # betweenness、graphtriangleCount。
      executeAlgo: pagerank
 
      # PageRank 参数
      pagerank: {
          maxIter: 10
          resetProb: 0.15  
      }
 
      # Louvain 参数
      louvain: {
          maxIter: 20
          internalIter: 10
          tol: 0.5
      }

      # ...
      }
      }
  }
  ```

2. 提交图计算任务。

  ```bash
  ${SPARK_HOME}/bin/spark-submit --master <mode> --class com.vesoft.nebula.algorithm.Main <nebula-algorithm-{{algorithm.release}}.jar_path> -p <application.conf_path>
  ```

  示例：

  ```bash
  ${SPARK_HOME}/bin/spark-submit --master "local" --class com.vesoft.nebula.algorithm.Main /root/nebula-algorithm/target/nebula-algorithm-3.0-SNAPSHOT.jar -p /root/nebula-algorithm/src/main/resources/application.conf
  ```

## 视频

* [图计算工具——Nebula Algorithm 介绍](https://www.bilibili.com/video/BV1fB4y1T7XK)（2 分 36 秒）
<iframe src="//player.bilibili.com/player.html?aid=588577467&bvid=BV1fB4y1T7XK&cid=351282857&page=1&high_quality=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="720px" height="480px"> </iframe>
