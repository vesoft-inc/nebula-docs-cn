# 算法简介

图计算可以检测图结构，例如图中社区的检测、图的划分等，也可以揭示各个点之间关联关系的内在特征，例如点的中心性、相似性等。本文介绍相关算法和参数。

<!--
NebulaGraph 支持多种图计算工具，本文介绍这些工具支持的算法和参数。
-->
!!! note

    本文仅介绍 NebulaGraph Analytics 的参数，NebulaGraph Algorithm 的参数请先参见对应的[算法文件](https://github.com/vesoft-inc/nebula-algorithm/tree/{{algorithm.branch}}/example/src/main/scala/com/vesoft/nebula/algorithm)。

<!--
!!! note

    不同图计算工具支持的算法不同，参数也不同。详情参见下文说明。
-->

!!! note

    执行图计算时不仅需要设置算法的参数，对数据源也有要求。数据源需要包含起点和终点。PageRank、DegreeWithTime、SSSP、APSP、LPA、HANP、Louvain 算法还需要包含权重（weight）。

    - 如果数据源来自 HDFS，需要指定 CSV 文件，包含`src`和`dst`列，部分算法还需要包含`weight`列。

    - 如果数据源来自 NebulaGraph，需要指定边类型，该类型的边提供`src`和`dst`列，部分算法还需要指定边类型的某个属性作为`weight`列。

## 节点重要度算法

### PageRank

PageRank（页面排序）算法根据点之间的关系（边）计算点的相关性和重要性，通常使用在搜索引擎页面排名中。如果一个网页被很多其他网页链接，说明这个网页比较重要（PageRank 值较高）；如果一个 PageRank 值很高的网页链接到其他网页，那么被链接到的网页的 PageRank 值会提高。

参数说明如下。

<!--
- NebulaGraph Algorithm

  |参数|默认值|说明|
  |:--|:--|:--|
  |`maxIter`|`10`|最大迭代次数。|
  |`resetProb`|`0.15`||
-->

- NebulaGraph Analytics

  - 传入参数

    |参数|默认值|说明|
    |:--|:--|:--|
    |`ITERATIONS`|`10`|最大迭代次数。|
    |`IS_DIRECTED`|`true`|是否考虑边的方向。如果设置为`false`，系统会自动添加反向边。|
    |`EPS`|`0.0001`|收敛精度，两轮迭代的结果差值小于这个值，结束迭代。|
    |`DAMPING`|`0.85`|阻尼系数，访问页面后的跳转概率。|

  - 输出参数

    |参数|类型|说明|
    |:--|:--|:--|
    |`VID`|创建图空间时`vid_type`决定| 点 ID。|
    |`VALUE`|double| 点的 PageRank 值。|

### KCore

KCore 算法用于计算出没有小于 K 度的点组成的子图，通常使用在社区发现、金融风控等场景。其计算结果是判断点重要性最常用的参考值之一，体现了点的传播能力。

参数说明如下。

<!--
- NebulaGraph Algorithm

  |参数|默认值|说明|
  |:--|:--|:--|
  |`maxIter`|`10`|最大迭代次数。|
  |`degree`|`1`||
-->

- NebulaGraph Analytics

  - 传入参数

    |参数|默认值|说明|
    |:--|:--|:--|
    |`TYPE`|`vertex`|计算类型。取值：`vertex`、`subgraph`。`vertex`表示为每个点计算核心度，`subgraph`表示计算邻居。|
    |`KMIN`|`1`|范围计算时设置 K 的最小值。仅在`TYPE`=`subgraph`时生效。|
    |`KMAX`|`1000000`|范围计算时设置 K 的最大值。仅在`TYPE`=`subgraph`时生效。|

  - `TYPE=vertex`时的输出参数

    |参数|类型|说明|
    |:--|:--|:--|
    |`VID`|创建图空间时`vid_type`决定| 点 ID。|
    |`VALUE`|int| 输出点的核心度。|

  - `TYPE=subgraph`时的输出参数

    |参数|类型|说明|
    |:--|:--|:--|
    |`VID`|创建图空间时`vid_type`决定| 点 ID。|
    |`VALUE`|与`VID`类型相同| 输出点的邻居。|

### DegreeCentrality（NStepDegree）

DegreeCentrality（度中心性） 算法用于查找图中的流行点。度中心性测量来自点的传入或传出（或两者）关系的数量，具体取决于关系投影的方向。一个点的度越大就意味着这个点的度中心性越高，该点在网络中就越重要。

!!! note

    NebulaGraph Analytics 仅粗略估算度中心性。

参数说明如下。

<!--
- NebulaGraph Algorithm（这里叫DegreeStatic？）

  |参数|默认值|说明|
  |:--|:--|:--|
  |``|``||
  |``|``||
  |``|``||
  |``|``||
-->

- NebulaGraph Analytics

  - 传入参数

    |参数|默认值|说明|
    |:--|:--|:--|
    |`STEP`|`3`|计算度数。`-1`表示无穷大。|
    |`BITS`|`6`|用于基数估计的 hyperloglog 位宽。|
    |`TYPE`|`both`|计算的边的方向。取值：`in`、`out`、`both`。|

  - `TYPE=both`时的输出参数

    |参数|类型|说明|
    |:--|:--|:--|
    |`VID`|创建图空间时`vid_type`决定| 点 ID。|
    |`BOTH_DEGREE`|int| 输出点的双向度中心性。|
    |`OUT_DEGREE`|int| 输出点的出方向度中心性。|
    |`IN_DEGREE`|int| 输出点的入方向度中心性。|

  - `TYPE=out`时的输出参数

    |参数|类型|说明|
    |:--|:--|:--|
    |`VID`|创建图空间时`vid_type`决定| 点 ID。|
    |`OUT_DEGREE`|int| 输出点的出方向度中心性。|

  - `TYPE=in`时的输出参数

    |参数|类型|说明|
    |:--|:--|:--|
    |`VID`|创建图空间时`vid_type`决定| 点 ID。|
    |`IN_DEGREE`|int| 输出点的入方向度中心性。|

### DegreeWithTime

DegreeWithTime 算法是基于边的时间范围统计邻居，查找出图中的流行点。

!!! note

    仅 NebulaGraph Analytics 支持该算法。

参数说明如下。

- 传入参数

  |参数|默认值|说明|
  |:--|:--|:--|
  |`TYPE`|`both`|计算的边的方向。取值：`in`、`out`、`both`。|
  |`BEGIN_TIME`|-|起始时间。格式为`yyyy-MM-dd HH:mm:ss.SSS`。|
  |`END_TIME`|-|结束时间。格式为`yyyy-MM-dd HH:mm:ss.SSS`。|

- `TYPE=both`时的输出参数

  |参数|类型|说明|
  |:--|:--|:--|
  |`VID`|创建图空间时`vid_type`决定| 点 ID。|
  |`BOTH_DEGREE`|int| 输出点的双向流行度。|
  |`OUT_DEGREE`|int| 输出点的出方向流行度。|
  |`IN_DEGREE`|int| 输出点的入方向流行度。|

- `TYPE=out`时的输出参数

  |参数|类型|说明|
  |:--|:--|:--|
  |`VID`|创建图空间时`vid_type`决定| 点 ID。|
  |`OUT_DEGREE`|int| 输出点的出方向流行度。|

- `TYPE=in`时的输出参数

  |参数|类型|说明|
  |:--|:--|:--|
  |`VID`|创建图空间时`vid_type`决定| 点 ID。|
  |`IN_DEGREE`|int| 输出点的入方向流行度。|

### BetweennessCentrality

BetweennessCentrality（中介中心性）算法是一种检测点对图中信息流的影响量的方法，用于查找从图的一部分到另一部分时作为桥梁的点。每个点都会根据通过该点的最短路径的数量获得一个分数，即中介中心性分数。

参数说明如下。

<!--
- NebulaGraph Algorithm

  |参数|默认值|说明|
  |:--|:--|:--|
  |`maxIter`|`5`|最大迭代次数。|
-->

- NebulaGraph Analytics

  - 传入参数

    |参数|默认值|说明|
    |:--|:--|:--|
    |`ITERATIONS`|`10`|最大迭代次数。|
    |`IS_DIRECTED`|`true`|是否考虑边的方向。如果设置为`false`，系统会自动添加反向边。|
    |`CHOSEN`|`-1`| 选取的点ID，`-1`表示随机选。|
    |`CONSTANT`|`2`|系数。|

  - 输出参数

    |参数|类型|说明|
    |:--|:--|:--|
    |`VID`|创建图空间时`vid_type`决定| 点 ID。|
    |`VALUE`|double| 点的中介中心性分数。|

### ClosenessCentrality

ClosenessCentrality（紧密中心性）算法用于计算一个点到所有其他可达点的最短距离的平均值的倒数。值越大，点在图中的位置越靠近中心，也可以用来衡量信息从该点传输到其他点的时间长短。

参数说明如下。

<!--
- NebulaGraph Algorithm

  |参数|默认值|说明|
  |:--|:--|:--|
  |``|``||
  |``|``||
  |``|``||
  |``|``||
-->

- NebulaGraph Analytics

  - 传入参数

    |参数|默认值|说明|
    |:--|:--|:--|
    |`IS_DIRECTED`|`true`|是否考虑边的方向。如果设置为`false`，系统会自动添加反向边。|
    |`NUM_SAMPLES`|`10`|采样的点数量。|

  - 输出参数

    |参数|类型|说明|
    |:--|:--|:--|
    |`VID`|创建图空间时`vid_type`决定| 点 ID。|
    |`VALUE`|double| 点的紧密中心性分数。|

## 路径算法

### APSP

APSP（全图最短路径）算法用于寻找图中两点之间的所有最短路径。

!!! note

    仅 NebulaGraph Analytics 支持该算法。

参数说明如下。

- 输出参数

  |参数|类型|说明|
  |:--|:--|:--|
  |`VID1`|创建图空间时`vid_type`决定| 起点的 ID。|
  |`VID2`|创建图空间时`vid_type`决定| 终点的 ID。|
  |`DISTANCE`|double| 输出`VID1`到`VID2`的距离。|

### SSSP

SSSP（单源最短路径）算法用于计算给定的一个点（起始点）出发到其余各点的最短路径长度。通常使用在网络路由、路径设计等场景。

参数说明如下。

<!--
- NebulaGraph Algorithm

  |参数|默认值|说明|
  |:--|:--|:--|
  |`sourceid`|-|起始点的 VID。|
-->

- NebulaGraph Analytics

  - 传入参数

    |参数|默认值|说明|
    |:--|:--|:--|
    |`ROOT`|-|起始点的 VID。|

  - 输出参数

    |参数|类型|说明|
    |:--|:--|:--|
    |`VID`|创建图空间时`vid_type`决定| 点 ID。|
    |`DISTANCE`|double| 输出`ROOT`到`VID`的距离。|

### BFS

BFS（广度优先遍历）算法是一种基础的图遍历算法，它给定一个起始点，以递增的跳数访问其他点，即先遍历点的所有相邻点，再往相邻点的相邻点延伸。

参数说明如下。

<!--
- NebulaGraph Algorithm

  |参数|默认值|说明|
  |:--|:--|:--|
  |``|``||
  |``|``||
  |``|``||
  |``|``||
-->

- NebulaGraph Analytics

  - 传入参数

    |参数|默认值|说明|
    |:--|:--|:--|
    |`IS_DIRECTED`|`true`|是否考虑边的方向。如果设置为`false`，系统会自动添加反向边。|
    |`ROOT`|-|起始点的 VID。|

  - 输出参数

    |参数|类型|说明|
    |:--|:--|:--|
    |`ROOT`|创建图空间时`vid_type`决定| 起始点的 ID。|
    |`VISITED`|int| 输出`ROOT`访问过的点数量。|

<!--
### Node2Vec

Node2Vec算法在 DeepWalk 的基础上提出了更加合理的图特征学习方法，提出了用于网络中可伸缩特征学习的半监督算法，使用 SGD 优化一个自定义的基于图的目标函数，该方法可以最大化的在 D 维特征空间保留节点的网络领域信息；在随机游走的基础上设计了一种二阶随机游走的过程，相当于对 DeepWalk 算法的一种扩展，它保留了邻居节点的图特征。适用于节点功能相似性比较、节点结构相似性比较、社团聚类等场景。

!!! note
    
    仅 NebulaGraph Algorithm 支持该算法。

参数说明如下。

|参数|默认值|说明|
|:--|:--|:--|
|`maxIter`|`10`|最大迭代次数。|
|`lr`|`0.025`||
|`dataNumPartition`|`10`||
|`modelNumPartition`|`10`||
|`dim`|`10`|映射维度。|
|`window`|`3`||
|`walkLength`|`5`|随机步长。|
|`numWalks`|`3`|每个节点的随机步长数。|
|`p`|`1.0`|回退参数。|
|`q`|`1.0`|前进参数。|
|`directed`|`false`||
|`degree`|`30`||
|`embSeparate`|`","`||
|`modelPath`|`"hdfs://127.0.0.1:9000/model"`||
-->

## 社区发现算法

### LPA

LPA（标签传播）算法是一种基于图的半监督学习方法，其基本思路是用已标记点的标签信息去预测未标记点的标签信息。利用样本间的关系建图，点包括已标注和未标注数据，其边表示两个点的相似度，点的标签按相似度传递给其他点。标签数据就像是一个源头，可以对无标签数据进行标注，点的相似度越大，标签越容易传播。

参数说明如下。

<!--
- NebulaGraph Algorithm

  |参数|默认值|说明|
  |:--|:--|:--|
  |`maxIter`|`20`|最大迭代次数。|
  |``|``||
  |``|``||
  |``|``||
-->

- NebulaGraph Analytics

  - 传入参数

    |参数|默认值|说明|
    |:--|:--|:--|
    |`ITERATIONS`|`10`|最大迭代次数。|
    |`IS_DIRECTED`|`true`|是否考虑边的方向。如果设置为`false`，系统会自动添加反向边。|
    |`IS_CALC_MODULARITY`|`false`|是否计算模块度。|

  - 输出参数

    |参数|类型|说明|
    |:--|:--|:--|
    |`VID`|创建图空间时`vid_type`决定| 点的 ID。|
    |`LABEL`|与`VID`类型相同| 输出标签相同的点的 ID。|

### HANP

HANP（Hop Attenuation & Node Preference）算法是LPA算法的优化算法，考虑了标签的其他信息，例如度的信息、距离信息等，同时在传播时引入了衰减系数，防止过渡传播。

参数说明如下。

<!--
- NebulaGraph Algorithm

  |参数|默认值|说明|
  |:--|:--|:--|
  |`hopAttenuation`|`0.1`|衰减因子。|
  |`maxIter`|`10`|最大迭代次数。|
  |`preference`|`1.0`||
-->

- NebulaGraph Analytics

  - 传入参数

    |参数|默认值|说明|
    |:--|:--|:--|
    |`ITERATIONS`|`10`|最大迭代次数。|
    |`IS_DIRECTED`|`true`|是否考虑边的方向。如果设置为`false`，系统会自动添加反向边。|
    |`PREFERENCE`|`1.0`|对邻居节点度的偏向性。`m>0`表示偏向节点度高的邻居，`m<0`表示偏向节点度低的邻居，`m=0`表示不考虑邻居节点度。|
    |`HOP_ATT`|`0.1`|衰减因子。取值范围`0`~`1`。值越大衰减的越快，可以传递的次数越少。|

  - 输出参数

    |参数|类型|说明|
    |:--|:--|:--|
    |`VID`|创建图空间时`vid_type`决定| 点的 ID。|
    |`LABEL`|与`VID`类型相同| 输出标签相同的点的 ID。|

### ConnectedComponent

ConnectedComponent（联通分量）算法用于计算出图中的一个子图，当中所有节点都相互连接。考虑路径方向的为强联通分量（strongly connected component），不考虑路径方向的为弱联通分量（weakly connected component）。

!!! note

    NebulaGraph Analytics 仅支持弱联通分量。

参数说明如下。

<!--
- NebulaGraph Algorithm

  |参数|默认值|说明|
  |:--|:--|:--|
  |`maxIter`|`10`|最大迭代次数。|
-->

- NebulaGraph Analytics

  - 传入参数

    |参数|默认值|说明|
    |:--|:--|:--|
    |`IS_DIRECTED`|`true`|是否考虑边的方向。如果设置为`false`，系统会自动添加反向边。|
    |`IS_CALC_MODULARITY`|`false`|是否计算模块度。|

  - 输出参数

    |参数|类型|说明|
    |:--|:--|:--|
    |`VID`|创建图空间时`vid_type`决定| 点的 ID。|
    |`LABEL`|与`VID`类型相同| 输出标签相同的点的 ID。|

### Louvain

Louvain 算法是基于模块度的社区发现算法，该算法在效率和效果上都表现较好，并且能够发现层次性的社区结构，其优化目标是最大化整个社区网络的模块度。模块度用于区分社区内和社区间链路密度的差异，是衡量每个点划分社区的好坏。通常情况下，一个优秀的分群方法将会使得社区内部的模块度高于社区与社区之间。

参数说明如下。

<!--
- NebulaGraph Algorithm

  |参数|默认值|说明|
  |:--|:--|:--|
  |`maxIter`|`20`|最大迭代次数。|
  |`internalIter`|`10`||
  |`tol`|`0.5`||
-->

- NebulaGraph Analytics

  - 传入参数

    |参数|默认值|说明|
    |:--|:--|:--|
    |`IS_DIRECTED`|`true`|是否考虑边的方向。如果设置为`false`，系统会自动添加反向边。|
    |`OUTER_ITERATION`|`20`|第一阶段最大迭代次数。|
    |`INNER_ITERATION`|`10`|第二阶段最大迭代次数。|
    |`IS_CALC_MODULARITY`|`false`|是否计算模块度。|

  - 输出参数

    |参数|类型|说明|
    |:--|:--|:--|
    |`VID`|创建图空间时`vid_type`决定| 点的 ID。|
    |`LABEL`|与`VID`类型相同| 输出标签相同的点的 ID。|

## 图特征算法

### TriangleCount

TriangleCount（三角计数）算法用于统计图中三角形个数。三角形越多，代表图中节点关联程度越高，组织关系越严密。

参数说明如下。

<!--
- NebulaGraph Algorithm

  |参数|默认值|说明|
  |:--|:--|:--|
  |``|``||
  |``|``||
  |``|``||
  |``|``||
-->

- NebulaGraph Analytics

  - 传入参数

    |参数|默认值|说明|
    |:--|:--|:--|
    |`OPT`|`3`|计算类型。取值：`1`（统计整个图）、`2`（通过每个点统计）、`3`（列出所有三角形）。|
    |`REMOVED_DUPLICATION_EDGE`|`true`|是否排除重复边。|
    |`REMOVED_SELF_EDGE`|`true`|是否排除自环边。|

  - `OPT=1`时的输出参数

    |参数|类型|说明|
    |:--|:--|:--|
    |`COUNT`|int| 输出全图的三角形数量。|

  - `OPT=2`时的输出参数

    |参数|类型|说明|
    |:--|:--|:--|
    |`VID`|创建图空间时`vid_type`决定|输出每个点的 ID。|
    |`COUNT`|int| 输出每个点的三角形数量。|

  - `OPT=3`时的输出参数

    |参数|类型|说明|
    |:--|:--|:--|
    |`VID1`|与`VID`类型相同| 输出构成三角形的点 A 的 ID。|
    |`VID2`|与`VID`类型相同| 输出构成三角形的点 B 的 ID。|
    |`VID3`|与`VID`类型相同| 输出构成三角形的点 C 的 ID。|

## 聚类算法

### ClusteringCoefficient

ClusteringCoefficient（聚集系数）算法用于计算图中节点的聚集程度。在各类反映真实世界的网络结构，特别是社交网络结构中，各个点之间倾向于形成密度相对较高的网络群，也就是说，相对于在两个点之间随机连接而得到的网络，真实世界网络的聚集系数更高。

参数说明如下。

<!--
- NebulaGraph Algorithm

  |参数|默认值|说明|
  |:--|:--|:--|
  |``|``||
  |``|``||
  |``|``||
  |``|``||
-->

- NebulaGraph Analytics

  - 传入参数

    |参数|默认值|说明|
    |:--|:--|:--|
    |`TYPE`|`local`|聚集类型。取值：`local`（为每个点计算聚集系数）、`global`（为全图计算聚集系数）。|
    |`REMOVED_DUPLICATION_EDGE`|`true`|是否排除重复边。|
    |`REMOVED_SELF_EDGE`|`true`|是否排除自环边。|

  - `TYPE=local`时的输出参数

    |参数|类型|说明|
    |:--|:--|:--|
    |`VID`|创建图空间时`vid_type`决定| 点的 ID。|
    |`VALUE`|double| 输出每个点的聚集系数。|

  - `TYPE=global`时的输出参数

    |参数|类型|说明|
    |:--|:--|:--|
    |`VID`|创建图空间时`vid_type`决定| 点的 ID。|
    |`VALUE`|double| 输出全图的聚集系数。只有一行数据。|

## 相似度算法

### Jaccard

Jaccard（杰卡德相似度）算法用于计算两个点（或集合）的相似程度，预测他们之间的关系。适用于社交网上的好友推荐、关系预测等场景。

参数说明如下。

<!--
- NebulaGraph Algorithm

  |参数|默认值|说明|
  |:--|:--|:--|
  |``|``||
  |``|``||
  |``|``||
  |``|``||
-->

- NebulaGraph Analytics

  - 传入参数

    |参数|默认值|说明|
    |:--|:--|:--|
    |`IDS1`|-|若干个 VID 构成的集合A。多个 VID 之间用英文逗号（,）隔开。不可为空。|
    |`IDS2`|-|若干个 VID 构成的集合B。多个 VID 之间用英文逗号（,）隔开。可以为空，为空时表示所有点。|
    |`REMOVED_SELF_EDGE`|`true`|是否排除自环边。|

  - 输出参数

    |参数|类型|说明|
    |:--|:--|:--|
    |`VID1`|创建图空间时`vid_type`决定| 第一个点的 ID。|
    |`VID2`|创建图空间时`vid_type`决定| 第二个点的 ID。|
    |`VALUE`|double| `VID1`和`VID2`的相似度。|