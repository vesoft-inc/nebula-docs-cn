# Nebula Analytics

Nebula Analytics 是一款高性能图计算框架工具，支持对 Nebula Graph 数据库中的数据执行图分析。

!!! enterpriseonly

    仅企业版支持本功能。

## 适用场景

支持将数据源为 Nebula Graph 集群、HDFS 上的 CSV 文件或本地 CSV 文件中的数据导入 Nebula Analytics，并将图计算结果输出至 Nebula Graph 集群、HDFS 上的 CSV 文件或本地 CSV 文件。

## 使用限制

输入和输出均为 Nebula Graph 集群时，图计算结果只能输出到数据源所在的图空间。

## 版本兼容性

Nebula Analytics 版本和 Nebula Graph 内核的版本对应关系如下。

|Analytics client 版本|Nebula Graph 版本|
|:---|:---|
|{{analytics.release}}|{{nebula.release}}|

## 支持算法

Nebula Analytics 支持的图计算算法如下。

|           算法名        |说明             |分类        |
|:----------------------|:----------------|:-----------|
|  APSP                 | 全图最短路径      |  路径       |
|  SSSP                 | 单源最短路径      | 路径        |
|  BFS                  | 广度优先遍历      |  路径       |
|  PageRank             | 页面排序          | 节点重要度   |
|  KCore                | K核              | 节点重要度   |
|  DegreeCentrality     | 度中心性          | 节点重要度   |
|  TriangleCount        | 三角计数          | 图特征      |
| LPA                   | 标签传播          |  社区发现    |
| HANP                  | 标签传播进阶版   |  社区发现    |
| WCC                   | 联通分量          |  社区发现    |
| LOUVAIN               | 社区发现          |  社区发现   |
| Clustering Coefficient| 聚集系数          |  聚类       |

## 安装 Nebula Analytics

在多个机器安装由多个 Nebula Analytics 服务构成的集群时，需要安装路径相同，并设置节点间 SSH 免密登录。

```bash
sudo rpm -i nebula-analytics-1.0.0-centos.x86_64.rpm  --prefix /home/xxx/nebula-analytics
```

<!--
### 编译安装

编译安装 Nebula Analytics 的准备工作和编译 Nebula Graph 类似，详情参见[准备资源](4.deployment-and-installation/1.resource-preparations.md)。

1. 克隆仓库`analytics`。

  ```bash
  $ git clone -b {{plato.branch}} https://github.com/vesoft-inc/nebula-analytics.git
  ```

2. 进入目录`nebula-analytics`。

  ```bash
  $ cd nebula-analytics
  ```

3. 执行脚本安装编译依赖。

  ```bash
  $ sudo ./docker/install-dependencies.sh
  ```

4. 下载并编译静态链接库。

  ```bash
  $ ./3rdtools.sh distclean && ./3rdtools.sh install
  ```

5. 编译 Nebula Analytics

  ```bash
  $ ./build.sh
  ```
-->


## 使用方法

安装完成后，用户可以设置不同算法的参数，然后执行脚本，即可获得算法的结果，并导出为指定格式。

1. 选择 Nebula Analytics 集群的任一节点，进入目录`scripts`。

  ```bash
  $ cd scripts
  ```

2. 确认数据源和输出路径。配置方法如下：
   
  - 数据源为 Nebula Graph 集群
   
    1. 修改配置文件`nebula.conf`，设置 Nebula Graph 集群相关信息。

      ```bash
      # 连接 Nebula Graph 时的重试次数。
      --retry=3  
      # 要读取或写入的图空间名称。
      --space=baskeyballplayer  

      # 读取 Nebula Graph 设置
      # Nebula Graph 的 metad 服务地址。
      --meta_server_addrs=192.168.8.100:9559, 192.168.8.101:9559, 192.168.8.102:9559
      # 要读取的边的名称。
      --edges=LIKES  
      # 要读取的作为边的权重属性的名称。可以是属性名，也可以是 _rank。
      #--edge_data_fields 
      # 每次扫描读取的行数。
      --read_batch_size=10000  

      # 写回 Nebula Graph 设置
      # Nebula Graph 的 graphd 服务地址。
      --graph_server_addrs=192.168.8.100:9669  
      # Nebula Graph 的登录用户名。
      --user=root  
      # Nebula Graph 的登录密码。
      --password=nebula  
      # 写回 Nebula Graph 时采用的模式: insert 和 update。
      --mode=insert  
      # 写回到 Nebula Graph 的 Tag 名称。
      --tag=pagerank  
      # 写回到 Nebula Graph 的 Tag 对应的属性名称。
      --prop=pr  
      # 写回到 Nebula Graph 的 Tag 对应的属性的类型。
      --type=double 
      # 写回时，每次写入的行数。
      --write_batch_size=1000 
      # 写回失败的数据所存储的文件。
      --err_file=/home/xxx/analytics/err.txt 
      ```
    
    2. 修改需要使用的算法脚本，例如`run_pagerank.sh`，设置相关参数。

      ```bash
      # 集群所有机器所运行的进程数之和，推荐每台机器为 1 或者 NUMA 架构的 node 数。
      WNUM=3 
      # 每个进程的线程数，推荐最大设置为机器的硬件线程数。
      WCORES=4  
      # 数据源路径
      # 可以通过文件 nebula.conf 设置从 Nebula Graph 读取：
      INPUT=${INPUT:="nebula:$PROJECT/scripts/nebula.conf"}  
      # 也可以通过本地或 HDFS 上的 CSV 文件读取：
      # #INPUT=${INPUT:="$PROJECT/data/graph/v100_e2150_ua_c3.csv"}

      # 图计算结果输出路径
      # 可以输出至 Nebula Graph 集群，如果数据源也为 Nebula Graph，结果会输出至 nebula.conf 指定的图空间。
      OUTPUT=${OUTPUT:="nebula:$PROJECT/scripts/nebula.conf"}
      # 也可以输出至本地或 HDFS 上的 CSV 文件：
      # OUTPUT=${OUTPUT:='hdfs://192.168.8.100:9000/_test/output'}

      # true 为有向图，false 为无向图。
      IS_DIRECTED=${IS_DIRECTED:=true}
      # 是否进行 ID 编码
      NEED_ENCODE=${NEED_ENCODE:=true}
      # 数据源的点 ID 类型，例如：string、int32、int64。
      VTYPE=${VTYPE:=int32}
      # 编码类型。distributed 为分布式点ID编码，single 为单机点 ID 编码。
      ENCODER=${ENCODER:="distributed"}
      # PageRank 算法的参数。不同算法的参数不同。
      EPS=${EPS:=0.0001}
      DAMPING=${DAMPING:=0.85}
      # 迭代次数
      ITERATIONS=${ITERATIONS:=100}
      ```

  - 数据源为本地或 HDFS 上的 CSV 文件

    修改需要使用的算法脚本，例如`run_pagerank.sh`，设置相关参数。

    ```bash
    # 集群所有机器所运行的进程数之和，推荐每台机器为 1 或者 NUMA 架构的 node 数。
    WNUM=3 
    # 每个进程的线程数，推荐最大设置为机器的硬件线程数。
    WCORES=4  
    # 数据源路径
    # 可以通过文件 nebula.conf 设置从 Nebula Graph 读取：
    # INPUT=${INPUT:="nebula:$PROJECT/scripts/nebula.conf"}  
    # 也可以通过本地或 HDFS 上的 CSV 文件读取：
    INPUT=${INPUT:="$PROJECT/data/graph/v100_e2150_ua_c3.csv"}

    # 图计算结果输出路径
    # 可以输出至 Nebula Graph 集群，如果数据源也为 Nebula Graph，结果会输出至 nebula.conf 指定的图空间。
    # OUTPUT=${OUTPUT:="nebula:$PROJECT/scripts/nebula.conf"}
    # 也可以输出至本地或 HDFS 上的 CSV 文件：
    OUTPUT=${OUTPUT:='hdfs://192.168.8.100:9000/_test/output'}

    # true 为有向图，false 为无向图。
    IS_DIRECTED=${IS_DIRECTED:=true}
    # 是否进行 ID 编码
    NEED_ENCODE=${NEED_ENCODE:=true}
    # 数据源的点 ID 类型，例如：string、int32、int64。
    VTYPE=${VTYPE:=int32}
    # 编码类型。distributed 为分布式点ID编码，single 为单机点 ID 编码。
    ENCODER=${ENCODER:="distributed"}
    # PageRank 算法的参数。不同算法的参数不同。
    EPS=${EPS:=0.0001}
    DAMPING=${DAMPING:=0.85}
    # 迭代次数
    ITERATIONS=${ITERATIONS:=100}
    ```

3. 修改配置文件`cluster`，设置执行算法的 Nebula Analytics 集群节点和任务分配权重。

  ```bash
  # Nebula Analytics 集群节点 IP 地址:任务分配权重
  192.168.8.200:1
  192.168.8.201:1
  192.168.8.202:1
  ```

4. 执行算法脚本。例如：

  ```bash
  ./run_pagerank.sh
  ```

5. 在输出路径查看计算结果。

  - 输出至 Nebula Graph 集群，请根据`nebula.conf`的设置查看计算结果。

  - 输出至 HDFS 上的 CSV 文件或本地 CSV 文件，请根据图计算脚本内的`OUTPUT`设置查看计算结果，计算结果为`.gz`格式的压缩文件。
