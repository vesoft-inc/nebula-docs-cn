# 升级{{nebula.name}} 至 {{nebula.release}} 版本

本文以{{nebula.name}} 2.6.1 版本升级到 {{nebula.release}} 版本为例，介绍{{nebula.name}}2.x、3.x 版本升级到 {{nebula.release}} 版本的方法。


<!-- 
- 3.0.0版本默认开启无tag点，升级2.x至3.0.0需要升级工具。
- 针对版本间的升级3.0.0到3.2.x，不需要升级工具，此时需要单独的版本间的升级文档。
- 在3.3.0版本默认关闭无tag点，数据结构无变化，此时升级2.x至3.x不要升级工具，也不需要单独的版本间的升级文档。-->

## 适用版本

本文适用于将{{nebula.name}} 从 2.5.0 及之后的 2.x、3.x 版本升级到 {{nebula.release}} 版本。不适用于 2.5.0 之前的历史版本（含 1.x 版本）。如需升级历史版本，将其根据最新的 2.x 版本文档升级到 2.5 版本，然后根据本文的说明升级到 {{nebula.release}} 版本。

<!-- 结论：社区版 2.5之前的版本 不支持升级到3.4及以上 ，原因：2.x（x<5）之前的版本和3.x都没记录meta版本号，升级到3.4（记录版本号）时，无法识别是哪种，所以就在手册写禁止2.5之前的升级，而允许3.x的升级，因为2.5和2.6是有记录meta版本号的，所以可以升级至3.x；
ps：如果2.x（x<5）来做到3.4的升级，升级过程不会报错，因为是按照3.x来做的处理，某些情况下数据可能不正确（这里的某些比较复杂），所以就禁止了 -->

!!! caution

    如需从 2.0.0 之前的版本（含 1.x 版本）升级到 {{nebula.release}}，还需找到 {{nebula.release}} 版本文件中`share/resources`目录下的`date_time_zonespec.csv`文件，将其复制到{{nebula.name}}安装路径下的相同目录内。也可从 [GitHub](https://github.com/vesoft-inc/nebula/blob/master/resources/date_time_zonespec.csv) 下载该文件。


- 不支持轮转热升级，需完全停止整个集群服务。

- 未提供升级脚本，需手动在每台服务器上依次执行。

- 不支持基于 Docker 容器（包括 Docker Swarm、Docker Compose、K8s）的升级。

- 必须在原服务器上原地升级，不能修改原机器的 IP 地址、配置文件，不可更改集群拓扑。

<!-- - 硬盘空间要求：各机器硬盘剩余空间都需要是原数据目录的**二倍**。其中一倍空间用于容纳手动备份的数据，另一倍空间用于容纳复制到`dst_db_path`的 WAL，以及原有数据中新增的用于支持无 tag 点的 key。 -->

- 已知会造成数据丢失的 4 种场景，和 alter schema 以及 default value 相关，参见 [github known issues](https://github.com/vesoft-inc/nebula-graph/issues/857)。

- 数据目录不要使用软连接切换，避免失效。

- 部分升级操作需要有 sudo 权限。

## 升级影响

<!-- - 数据膨胀
  
  {{nebula.name}} 3.x 版本扩展了原有的数据格式，每个点多出一个 key，所以升级后数据会占用更大的空间。
  
  新增 key 的格式为： Type 字段（1 字节）+ Partition ID 字段（3 字节）+ VID（大小根据类型而定）。key 的 value 为空。多占用的空间可以根据点的数量和 VID 的数据类型计算。例如，数据集中有 1 亿个点，且 VID 为 INT64，则升级后这个 key 会占用 1 亿 * （1 + 3 + 8）= 12 亿字节，约等于 1.2 GB。 -->

- 客户端兼容

  升级后旧版本客户端将无法连接{{nebula.name}}，需将所有客户端都升级到兼容{{nebula.name}} {{nebula.release}} 的版本。

- 配置变化

  少数配置参数发生改变，详情参考版本发布说明和参数文档。

- 语法兼容

  nGQL 语法有部分不兼容：

  - 禁用`YIELD`子句返回自定义变量。

  - `FETCH`、`GO`、`LOOKUP`、`FIND PATH`、`GET SUBGRAPH`语句中必须添加`YIELD`子句。

  - MATCH 语句中获取点属性时，必须指定 Tag，例如从`return v.name`变为`return v.player.name`。

- 全文索引

  在升级部署了全文索引的{{nebula.name}}前，需要手动删除 Elasticsearch (ES) 中的全文索引。在升级后需要重新使用`SIGN IN`语句登录 ES 并重新创建全文索引。用户可通过 cURL 命令手动删除 ES 中全文索引。命令为`curl -XDELETE -u <es_username>:<es_password> '<es_access_ip>:<port>/<fullindex_name>'`，例如`curl -XDELETE -u elastic:elastic 'http://192.168.8.223:9200/nebula_index_2534'`。如果 ES 没有设置用户名及密码，则无需指定`-u`选项。 

!!! caution

    可能存在其它暂未发现的影响，建议升级前详细查看版本发布说明和产品手册，并密切关注[论坛](https://discuss.nebula-graph.com.cn/)与 [GitHub](https://github.com/vesoft-inc/nebula/issues) 的最新动态。

## 升级准备

- 根据操作系统和架构下载{{nebula.name}} {{nebula.release}} 版本的包文件并解压，升级过程中需要其中的二进制文件。下载地址参见 [Download 页面](https://nebula-graph.io/download/)。

  !!! note

        编译源码或者下载 RPM/DEB、TAR 包都可以获取新版二进制文件。

- 根据 Storage 和 Meta 服务配置中`data_path`参数的值找到数据文件的位置，并备份数据。默认路径为`nebula/data/storage`和`nebula/data/meta`。

  !!! danger
        升级时不会自动备份原有数据。务必手动备份数据，防止丢失。

- 备份配置文件。

- 统计所有图空间升级前的数据量，供升级后比较。统计方法如下：

  1. 运行`SUBMIT JOB STATS`。
  2. 运行`SHOW JOBS`并记录返回结果。

## 升级步骤

1. 停止所有{{nebula.name}}服务。

  ```
  <nebula_install_path>/scripts/nebula.service stop all
  ```

  `nebula_install_path`代表{{nebula.name}}的安装目录。

  `storaged` 进程 flush 数据要等待约 1 分钟。运行命令后可继续运行`nebula.service status all`命令以确认所有服务都已停止。启动和停止服务的详细说明参见[管理服务](../manage-service.md)。

  !!! note

        如果超过 20 分钟不能停止服务，放弃本次升级，在[论坛](https://discuss.nebula-graph.com.cn/)或 [GitHub](https://github.com/vesoft-inc/nebula/issues) 提问。

  !!! caution

        从 3.0.0 开始，支持插入无 Tag 的点。如果用户需要保留无 Tag 的点，在集群内所有 Graph 服务的配置文件（`nebula-graphd.conf`）中新增`--graph_use_vertex_key=true`；在所有 Storage 服务的配置文件（`nebula-storaged.conf`）中新增`--use_vertex_key=true`。

2. 在**升级准备**中下载的包的目的路径下，用此处`bin`目录中的新版二进制文件替换{{nebula.name}}安装路径下`bin`目录中的旧版二进制文件。

  !!! note
        每台部署了{{nebula.name}}服务的机器上都要更新相应服务的二进制文件。

3. 编辑所有 Graph 服务的配置文件，修改以下参数以适应新版本的取值范围。如参数值已在规定范围内，忽略该步骤。
   <!-- 在3.0.0后可忽略该步骤，因为3.0.0及之后配置文件中改了该字段的默认值。 -->

  - 为`session_idle_timeout_secs`参数设置一个在 [1,604800] 区间的值，推荐值为 28800。
  - 为`client_idle_timeout_secs`参数设置一个在 [1,604800] 区间的值，推荐值为 28800。

  这些参数在 2.x 版本中的默认值不在新版本的取值范围内，如不修改会升级失败。详细参数说明参见[Graph 服务配置](../../5.configurations-and-logs/1.configurations/3.graph-config.md)。

4. 启动所有 Meta 服务。

  ```
  <nebula_install_path>/scripts/nebula-metad.service start
  ```

  启动后，Meta 服务选举 leader。该过程耗时数秒。

  启动后可以任意启动一个 Graph 服务节点，使用{{nebula.name}}连接该节点并运行[`SHOW HOSTS meta`](../../3.ngql-guide/7.general-query-statements/6.show/6.show-hosts.md)和[`SHOW META LEADER`](../../3.ngql-guide/7.general-query-statements/6.show/19.show-meta-leader.md)，如果能够正常返回 Meta 节点的状态，则 Meta 服务启动成功。

  !!! note
        如果启动异常，放弃本次升级，并在[论坛](https://discuss.nebula-graph.com.cn/)或 [GitHub](https://github.com/vesoft-inc/nebula/issues) 提问。


5. 启动所有 Graph 和 Storage 服务。

  !!! note
        如果启动异常，放弃本次升级，并在[论坛](https://discuss.nebula-graph.com.cn/)或 [GitHub](https://github.com/vesoft-inc/nebula/issues) 提问。

6. 连接新版{{nebula.name}}，验证服务是否可用、数据是否正常。连接方法参见[连接服务](../connect-to-nebula-graph.md)。

  目前尚无有效方式判断升级是否完全成功，可用于测试的参考命令如下：

  ```ngql
  nebula> SHOW HOSTS;
  nebula> SHOW HOSTS storage;
  nebula> SHOW SPACES;
  nebula> USE <space_name>
  nebula> SHOW PARTS;
  nebula> SUBMIT JOB STATS;
  nebula> SHOW STATS;
  nebula> MATCH (v) RETURN v LIMIT 5;
  ```

  也可根据 {{nebula.release}} 版本的新功能测试，新功能列表参见[发布说明](../../20.appendix/release-notes/nebula-comm-release-note.md)。

## 升级失败回滚

如果升级失败，停止新版本的所有服务，从备份中恢复配置文件和二进制文件，启动历史版本的服务。

所有周边客户端也切换为旧版。

## FAQ

### 升级过程中是否可以通过客户端写入数据？

不可以。升级过程中需要停止所有服务。

### 升级过程中出现`Space 0 not found`。

当升级过程中出现`Space 0 not found`告警信息时，用户可以忽略这个信息。升级过程会从磁盘读取所有 Space ID，而`0`（路径为`<nebula_storagepath>/data/storage/nebula/0`）并不会存在磁盘上。Space `0` 用来存储 Storage 服务的元信息，并不包含用户数据，因此不会影响升级。

### 如果某台机器只有 Graph 服务，没有 Storage 服务，如何升级？

只需要升级 Graph 服务对应的二进制文件和配置文件。

### 操作报错 `Permission denied`。

部分命令需要有 sudo 权限。

<!--
Q：是否有 gflags 发生改变？

A: 有部分 glags 改变了，详情参见版本发布说明和配置说明文档。
-->

### 是否有工具或者办法验证新旧版本数据是否一致？

没有。如果只是检查数据量，可以在升级完成后再次运行`SUBMIT JOB STATS`和`SHOW STATS`统计数据量，并与升级之前做对比。

### Storage `OFFLINE`并且`Leader count`是`0`怎么处理？

运行以下命令手动添加 Storage 主机：

```ngql
ADD HOSTS <ip>:<port>[, <ip>:<port> ...];
```

例如：

```
ADD HOSTS 192.168.10.100:9779, 192.168.10.101:9779, 192.168.10.102:9779;
```

如果有多个 Meta 服务节点，手动`ADD HOSTS`之后，部分 Storage 节点需等待数个心跳（`heartbeat_interval_secs`）的时间才能正常连接到集群。

如果添加 Storage 主机后问题仍然存在，在[论坛](https://discuss.nebula-graph.com.cn/)或 [GitHub](https://github.com/vesoft-inc/nebula/issues) 提问。

### 为什么升级后用`SHOW JOBS`查询到的 Job 的 ID 与升级前一样，但 Job 名称等信息不同了？

{{nebula.name}} 2.5.0 版本调整了 Job 的定义，详情参见 [Pull request](https://github.com/vesoft-inc/nebula-common/pull/562/files)。如果是从 2.5.0 之前的版本升级，会出现该问题。

### 有哪些语法不兼容 ?

A: 参见[Release Note](../../20.appendix/release-notes/nebula-comm-release-note.md) Incompatibility 部分。
