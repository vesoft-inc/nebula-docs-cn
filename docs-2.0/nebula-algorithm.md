# Nebula Algorithm

[Nebula Algorithm](https://github.com/vesoft-inc/nebula-spark-utils/tree/master/nebula-algorithm) （简称Algorithm）是一款基于[GraphX](https://spark.apache.org/graphx/)的Spark应用程序，通过提交Spark任务的形式使用完整的算法工具对Nebula Graph数据库中的数据执行图计算，也可以通过编程形式调用lib库下的算法针对DataFrame执行图计算。

## 前提条件

在使用 Algorithm 之前，用户需要确认以下信息：

- Nebula Graph 服务已经部署并启动。详细信息，参考[Nebula Graph安装部署](4.deployment-and-installation/1.resource-preparations.md "点击前往 Nebula Graph 安装部署")。

- Spark 版本为 2.4.x 。

- （可选）如果用户需要在Github中克隆最新的Algorithm，并自行编译打包，可以选择安装[Maven](https://maven.apache.org/download.cgi)。

## 使用限制

点ID的数据必须为整数，即点ID可以是INT类型，或者是String类型但数据本身为整数。

对于非整数的String类型数据，推荐使用调用算法接口的方式，可以使用SparkSQL的`dense_rank`函数进行编码，将String类型转换为Long类型。

## 支持算法

Nebula Algorithm支持的图计算算法如下。

 |           算法名          |说明|应用场景|
 |:------------------------|:-----------|:----|
 |         PageRank         |  页面排序  | 网页排序、重点节点挖掘|
 |         Louvain          |  社区发现  | 社团挖掘、层次化聚类|
 |          KCore           |    K核    |社区发现、金融风控|
 |     LabelPropagation     |  标签传播  |资讯传播、广告推荐、社区发现|
 |    ConnectedComponent    |  联通分量  |社区发现、孤岛发现|
 |StronglyConnectedComponent| 强联通分量  |社区发现|
 |       ShortestPath       |  最短路径   |路径规划、网络规划|
 |       TriangleCount      | 三角形计数  |网络结构分析|
 |   BetweennessCentrality  | 介数中心性  |关键节点挖掘，节点影响力计算|
 |        DegreeStatic      |   度统计   |图结构分析|

## 实现方法

Nebula Algorithm实现图计算的流程如下：

1. 利用Nebula Spark Connector从Nebula Graph数据库中读取图数据为DataFrame。

2. 将DataFrame转换为GraphX的图。

3. 调用GraphX提供的图算法（例如PageRank）或者自行实现的算法（例如Louvain社区发现）。

详细的实现方法可以参见相关[Scala文件](https://github.com/vesoft-inc/nebula-spark-utils/tree/master/nebula-algorithm/src/main/scala/com/vesoft/nebula/algorithm/lib)。

## 获取Nebula Algorithm

### 编译打包

1. 克隆仓库`nebula-spark-utils`。

  ```bash
  $ git clone -b {{algorithm.release}} https://github.com/vesoft-inc/nebula-spark-utils.git
  ```

2. 进入目录`nebula-algorithm`。

  ```bash
  $ cd nebula-spark-utils/nebula-algorithm
  ```

3. 编译打包。

  ```bash
  $ mvn clean package -Dgpg.skip -Dmaven.javadoc.skip=true -Dmaven.test.skip=true
  ```

编译完成后，在目录`nebula-algorithm/target`下生成类似文件`nebula-algorithm-2.0.0.jar`。

### Maven远程仓库下载

[下载地址](https://repo1.maven.org/maven2/com/vesoft/nebula-algorithm/2.0.0/)

## 使用方法

### 调用算法接口（推荐）

`lib`库中提供了10种常用图计算算法，用户可以通过编程调用的形式调用算法。

1. 在文件`pom.xml`中添加依赖。

  ```bash
  <dependency>
  <groupId>com.vesoft</groupId>
  <artifactId>nebula-algorithm</artifactId>
  <version>2.0.0</version>
  </dependency>
  ```

2. 传入参数调用算法（以PageRank为例）。更多算法请参见[测试用例](https://github.com/vesoft-inc/nebula-spark-utils/tree/master/nebula-algorithm/src/test/scala/com/vesoft/nebula/algorithm/lib)。

  !!! note
        执行算法的DataFrame默认第一列是起始点，第二列是目的点，第三列是边权重（非Nebula Graph中的Rank）。

  ```bash
  val prConfig = new PRConfig(5, 1.0)
  val louvainResult = PageRankAlgo.apply(spark, data, prConfig, false)
  ```

### 直接提交算法包
  
!!! note
    使用封装好的算法包有一定的局限性，例如落库到Nebula Graph时，落库的图空间中创建的Tag的属性名称必须和代码内预设的名称保持一致。如果用户有开发能力，推荐使用第一种方法。

1. 设置[配置文件](https://github.com/vesoft-inc/nebula-spark-utils/blob/master/nebula-algorithm/src/main/resources/application.conf)。

  ```bash
  {
      # Spark相关配置
      spark: {
      app: {
          name: LPA
          # Spark分片数量
          partitionNum:100
      }
      master:local
      }

      data: {
      # 数据源，可选值为nebula、csv、json。
      source: nebula
      # 数据落库，即图计算的结果写入的目标，可选值为nebula、csv、json。
      sink: nebula
      # 算法是否需要权重。
      hasWeight: false
      }
 
      # Nebula Graph相关配置
      nebula: {
      # 数据源。Nebula Graph作为图计算的数据源时，nebula.read的配置才生效。
      read: {
          # 所有Meta服务的IP地址和端口，多个地址用英文逗号（,）分隔。格式: "ip1:port1,ip2:port2"。
          # 使用docker-compose部署，端口需要填写docker-compose映射到外部的端口
          # 可以用`docker-compose ps`查看
          metaAddress: "192.168.*.10:9559"
          # Nebula Graph图空间名称
          space: basketballplayer
          # Nebula Graph Edge type, 多个labels时，多个边的数据将合并。
          labels: ["serve"]
          # Nebula Graph每个Edge type的属性名称，此属性将作为算法的权重列，请确保和Edge type对应。
          weightCols: ["start_year"]
      }
 
      # 数据落库。图计算结果落库到Nebula Graph时，nebula.write的配置才生效。
      write:{
          # Graph服务的IP地址和端口, 多个地址用英文逗号（,）分隔。格式: "ip1:port1,ip2:port2"。
          # 使用docker-compose部署，端口需要填写docker-compose映射到外部的端口
          # 可以用`docker-compose ps`查看
          graphAddress: "192.168.*.11:9669"
          # 所有Meta服务的IP地址和端口，多个地址用英文逗号（,）分隔。格式: "ip1:port1,ip2:port2"。
          # 使用docker-compose部署，端口需要填写docker-compose映射到外部的端口
          # 可以用`docker-compose ps`查看
          metaAddress: "192.168.*.12:9559"
          user:root
          pswd:nebula
          # 在提交图计算任务之前需要自行创建图空间及Tag
          # Nebula Graph图空间名称
          space:nb
          # Nebula Graph Tag名称，图计算结果会写入该Tag。Tag中的属性名称固定如下：
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
      # 数据源。图计算的数据源为csv文件或json文件时，local.read的配置才生效。
      read:{
          filePath: "hdfs://127.0.0.1:9000/edge/work_for.csv"
          # 如果CSV文件没有表头，使用[_c0, _c1, _c2, ..., _cn]表示其表头，有表头或者是json文件时，直接使用表头名称即可。
          # 起始点ID列的表头。
          srcId:"_c0"
          # 目的点ID列的表头。
          dstId:"_c1"
          # 权重列的表头
          weight: "_c2"
          # csv文件是否有表头
          header: false
          # csv文件的分隔符
          delimiter:","
      }

      # 数据落库。图计算结果落库到csv文件或text文件时，local.write的配置才生效。
      write:{
          resultPath:/tmp/
      }
      }


      algorithm: {
      # 需要执行的算法，可选值为：pagerank、louvain、connectedcomponent、
      # labelpropagation、shortestpaths、degreestatic、kcore、
      # stronglyconnectedcomponent、trianglecount、betweenness
      executeAlgo: pagerank
 
      # PageRank参数
      pagerank: {
          maxIter: 10
          resetProb: 0.15  # 默认为0.15
      }
 
      # Louvain参数
      louvain: {
          maxIter: 20
          internalIter: 10
          tol: 0.5
      }

     # ConnectedComponent/StronglyConnectedComponent参数
     connectedcomponent: {
         maxIter: 20
     }

     # LabelPropagation参数
     labelpropagation: {
         maxIter: 20
     }

      # ShortestPath参数
      shortestpaths: {
          # several vertices to compute the shortest path to all vertices.
          landmarks: "1"
      }

      # DegreeStatic参数
      degreestatic: {}

      # KCore参数
      kcore:{
          maxIter:10
          degree:1
      }

      # TriangleCount参数
      trianglecount:{}
 
      # BetweennessCentrality参数
      betweenness:{
          maxIter:5
      }
  }
  }
  ```

2. 提交图计算任务。

  ```bash
  ${SPARK_HOME}/bin/spark-submit --master <mode> --class com.vesoft.nebula.algorithm.Main <nebula-algorithm-2.0.0.jar_path> -p <application.conf_path>
  ```

  示例：

  ```bash
  ${SPARK_HOME}/bin/spark-submit --master "local" --class com.vesoft.nebula.algorithm.Main /root/nebula-spark-utils/nebula-algorithm/target/nebula-algorithm-2.0.0.jar -p /root/nebula-spark-utils/nebula-algorithm/src/main/resources/application.conf
  ```

## 视频

* [图计算工具——Nebula Algorithm 介绍](https://www.bilibili.com/video/BV1fB4y1T7XK)（2分36秒）
<iframe src="//player.bilibili.com/player.html?aid=588577467&bvid=BV1fB4y1T7XK&cid=351282857&page=1&high_quality=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="720px" height="480px"> </iframe>
