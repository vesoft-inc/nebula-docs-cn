# 信息总览

用户可以在**信息总览**页面查看{{nebula.name}}内核相关信息，包括 Storage 服务信息、Storage Leader 分布、{{nebula.name}}各个服务的版本信息及所在节点信息、分片的分布情况及详细信息。

## 入口

1. 在{{dashboard_ent.name}}顶部导航栏，单击**集群管理**。
2. 单击目标集群右侧**详情**。
3. 在左侧导航栏，单击**集群信息**->**信息总览**。

!!! note

    在查看集群信息之前，用户需要选择任意一个在线的 Graph 服务地址，输入登录{{nebula.name}}的账号（非{{dashboard_ent.name}}登录账号）和对应密码。

<img src="https://docs-cdn.nebula-graph.com.cn/figures/ec_dash_info_230912_cn.png" width="1200" alt="运维监控信息总览截屏">

## Storage Leader 分布

显示 Leader 数量及 Leader 的分布。

- 单击右上角的 **Balance Leader** 按钮可以快速在{{nebula.name}}集群中均衡分布 Leader。关于 Leader 的详细信息，参见 [Storage 服务](../../../1.introduction/3.nebula-graph-architecture/4.storage-service.md)。

- 单击右上角的**详情**，查看 Leader 分布的详细信息。

## 版本

显示{{nebula.name}}所有服务版本及服务地址。单击右上角的**详情**，查看更多信息。

## 服务信息

展示 Storage 服务的基本信息。参数说明如下：

| 参数 | 说明 |
| :--- | :--- |
| `Host` | 主机地址 |
| `Port` | 主机端口号 |
| `Status` | 主机状态 |
| `Git Info Sha` | 版本 Commit ID |
| `Leader Count` | Leader 总数 |
| `Partition Distribution` | 分片分布 |
| `Leader Distribution` | Leader 分布 |

单击右上角的**详情**，查看更多信息。

## Partition 分布

左上方选择指定图空间：

- 查看指定图空间的分片分布情况。显示所有 Storage 服务的 IP 地址、端口，及对应 Storage 服务中的分片数量。
- 单击 **Balance Data** 均衡分布当前图空间中的所有分片。
- 单击 **Balance Data Remove** 迁移指定的 Storage 服务中的所有分片至其他 Storage 服务中，操作前系统会先引导用户选择 Storage 服务所在的节点 IP。


<!-- 增加balance data 
 -->
单击右上角的**详情**，查看更多信息。

## 分片信息

显示分片信息。用户需要在左上角选择图空间，查看分片信息。参数说明如下：

|参数|说明|
|:---|:---|
|`Partition ID`|分片序号。|
|`Leader`|分片的 leader 副本的 IP 地址和端口。|
|`Peers`|分片所有副本的 IP 地址和端口。|
|`Losts`|分片的故障副本的 IP 地址和端口。|

单击右上角的**详情**，查看更多信息，通过右上角的输入框，输入分片 ID，筛选展示的数据。

<!-- 长时任务目前先不融合进信息总览页，等之后慢查询治理做了后放一起

## 长时任务

展示所有作业的信息。查看作业信息之前，用户需要在右上角选择图空间。暂不支持在线管理作业，详情请参见[作业管理](../../3.ngql-guide/4.job-statements.md)。参数说明如下：

| 参数 | 说明 |
| :--- | :--- |
| `Job ID` | 显示作业 ID。 |
| `Command` | 显示命令类型。 |
| `Status` | 显示作业或任务的状态。状态说明参见[作业状态](../../3.ngql-guide/4.job-statements.md#_2)。 |
|`Start Time`|显示作业或任务开始执行的时间。|
| `Stop Time` | 显示作业或任务结束执行的时间，结束后的状态包括`FINISHED`、`FAILED`或`STOPPED`。 | -->
