# 升级 Nebula Graph 2.x 至 {{nebula.release}} 版本

本文以 Nebula Graph 2.6.1 版本升级到 {{nebula.release}} 版本为例，介绍 Nebula Graph 2.x 版本升级到 3.x 版本的方法。

## 适用版本

本文适用于将 Nebula Graph 从 2.0.0 及之后的 2.x 版本升级到 {{nebula.release}} 版本。不适用于 2.0.0 之前的历史版本（含 1.x 版本）。如需升级历史版本，将其根据最新的 2.x 版本文档升级到最新的 2.x 版本，然后根据本文的说明升级到 3.x 版本。

!!! caution

    如需从 2.0.0 之前的版本（含 1.x 版本）升级到 {{nebula.release}}，还需找到 {{nebula.release}} 版本文件中`share/resources`目录下的`date_time_zonespec.csv`文件，将其复制到 Nebula Graph 安装路径下的相同目录内。也可从 [GitHub](https://github.com/vesoft-inc/nebula/blob/master/resources/date_time_zonespec.csv) 下载该文件。

## 升级限制

- 不支持轮转热升级，需完全停止整个集群服务。

- 未提供升级脚本，需手动在每台服务器上依次执行。

- 不支持基于 Docker 容器（包括 Docker Swarm、Docker Compose、K8s）的升级。

- 必须在原服务器上原地升级，不能修改原机器的 IP 地址、配置文件，不可更改集群拓扑。

- 硬盘空间要求：各机器硬盘剩余空间都需要是原数据目录的**三倍以上**。

- 已知会造成数据丢失的 4 种场景，和 alter schema 以及 default value 相关，参见 [github known issues](https://github.com/vesoft-inc/nebula-graph/issues/857)。

- 数据目录不要使用软连接切换，避免失效。

- 部分升级操作需要有 sudo 权限。

## 升级影响

- 数据膨胀
  
  Nebula Graph 3.x 版本扩展了原有的数据格式，每个点多出一个 key，所以升级后数据会占用更大的空间。
  
  新增 key 的格式为： Type 字段（1 字节）+ Partition ID 字段（3 字节）+ VID（大小根据类型而定）。key 的 value 为空。多占用的空间可以根据点的数量和 VID 的数据类型计算。例如，数据集中有 1 亿个点，且 VID 为 INT64，则升级后这个 key 会占用 1 亿 * （1 + 3 + 8）= 12 亿字节，约等于 1.2 GB。

- 客户端兼容

  升级后旧版本客户端将无法连接 Nebula Graph，需将所有客户端都升级到兼容 Nebula Graph {{nebula.release}} 的版本。

- 配置变化

  少数配置参数发生改变，详情参考版本发布说明和参数文档。

- 语法兼容

  nGQL 语法有部分不兼容：

  - 禁用`YIELD`子句返回自定义变量。

  - `FETCH`、`GO`、`LOOKUP`、`FIND PATH`、`GET SUBGRAPH`语句中必须添加`YIELD`子句。

  - MATCH 语句中获取点属性时，必须指定 Tag，例如从`return v.name`变为`return v.player.name`。

!!! caution

    可能存在其它暂未发现的影响，建议升级前详细查看版本发布说明和产品手册，并密切关注[论坛](https://discuss.nebula-graph.com.cn/)与 [GitHub](https://github.com/vesoft-inc/nebula/issues) 的最新动态。

## 升级准备

- 根据操作系统和架构下载 Nebula Graph {{nebula.release}} 版本的 TAR 文件并解压，升级过程中需要其中的二进制文件。TAR 包下载地址参见 [Download 页面](https://nebula-graph.io/download/)。

  !!! note
        编译源码或者下载RPM/DEB包也可以获取新版二进制文件。

- 根据 Storage 和 Meta 服务配置中`data_path`参数的值找到数据文件的位置，并备份数据。默认路径为`nebula/data/storage`和`nebula/data/meta`。

- 备份配置文件。

- 统计所有图空间升级前的数据量，供升级后比较。统计方法如下：

  1. 运行`SUBMIT JOB STATS`。
  2. 运行`SHOW JOBS`并记录返回结果。

## 升级步骤

1. 停止所有 Nebula Graph 服务。

  ```
  <nebula_install_path>/scripts/nebula.service stop all
  ```

  `nebula_install_path`代表 Nebula Graph 的安装目录。

  `storaged` 进程 flush 数据要等待约 1 分钟。运行命令后可继续运行`nebula.service status all`命令以确认所有服务都已停止。启动和停止服务的详细说明参见[管理服务](../manage-service.md)。

  !!! Note

        如果超过 20 分钟不能停止服务，放弃本次升级，在[论坛](https://discuss.nebula-graph.com.cn/)或 [GitHub](https://github.com/vesoft-inc/nebula/issues) 提问。

2. 在**升级准备**中解压 TAR 包的目的路径下，用此处`bin`目录中的新版二进制文件替换 Nebula Graph 安装路径下`bin`目录中的旧版二进制文件。

  !!! note
        每台部署了 Nebula Graph 服务的机器上都要更新相应服务的二进制文件。

3. 编辑所有 Graph 服务的配置文件，修改以下参数以适应新版本的取值范围。如参数值已在规定范围内，忽略该步骤。

  - 为`session_idle_timeout_secs`参数设置一个在 [1,604800] 区间的值，推荐值为 28800。
  - 为`client_idle_timeout_secs`参数设置一个在 [1,604800] 区间的值，推荐值为 28800。

  这些参数在 2.x 版本中的默认值不在新版本的取值范围内，如不修改会升级失败。详细参数说明参见[Graph 服务配置](../../5.configurations-and-logs/1.configurations/3.graph-config.md)。

4. 启动所有 Meta 服务。

  ```
  <nebula_install_path>/scripts/nebula-metad.service start
  ```

  启动后，Meta 服务选举 leader。该过程耗时数秒。

  启动后可以任意启动一个 Graph 服务节点，使用 Nebula Graph 连接该节点并运行[`SHOW HOSTS meta`](../../3.ngql-guide/7.general-query-statements/6.show/6.show-hosts.md)和[`SHOW META LEADER`](../../3.ngql-guide/7.general-query-statements/6.show/19.show-meta-leader.md)，如果能够正常返回 Meta 节点的状态，则 Meta 服务启动成功。

  !!! note
        如果启动异常，放弃本次升级，并在[论坛](https://discuss.nebula-graph.com.cn/)或 [GitHub](https://github.com/vesoft-inc/nebula/issues) 提问。

5. 使用`bin`目录下的新版 db_upgrader 文件升级数据格式。

  !!! caution
        本步骤会备份 Storage 服务中保存的数据，但为防止备份失败，升级数据格式前，务必按照本文**升级准备**部分的说明备份数据。

  命令语法：

  ```
  <nebula_install_path>/bin/db_upgrader \
  --src_db_path=<old_storage_data_path> \
  --dst_db_path=<data_backup_path> \
  --upgrade_meta_server=<meta_server_ip>:<port>[, <meta_server_ip>:<port> ...] \
  --upgrade_version=2:3
  ```

  - `old_storage_data_path`代表数据的存储路径，由 Storage 服务配置文件中的`data_path`参数定义。
  - `data_backup_path`代表自定义的数据备份路径。
  - `meta_server_ip`和`port`分别代表 Meta 服务各节点的 IP 地址和端口号。
  - `2:3`代表从 Nebula Graph 2.x 版本升级到 3.x 版本。

  本文示例：

  ```
  <nebula_install_path>/bin/db_upgrader \
  --src_db_path=/usr/local/nebula/data/storage \
  --dst_db_path=/home/vesoft/nebula/data-backup \
  --upgrade_meta_server=192.168.8.132:9559 \
  --upgrade_version=2:3
  ```

  !!! note
        如果出现异常，放弃本次升级，并在[论坛](https://discuss.nebula-graph.com.cn/)或 [GitHub](https://github.com/vesoft-inc/nebula/issues) 提问。

6. 启动所有 Graph 和 Storage 服务。

  !!! note
        如果启动异常，放弃本次升级，并在[论坛](https://discuss.nebula-graph.com.cn/)或 [GitHub](https://github.com/vesoft-inc/nebula/issues) 提问。

7. 连接新版 Nebula Graph，验证服务是否可用、数据是否正常。连接方法参见[连接服务](../connect-to-nebula-graph.md)。

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

  也可根据 {{nebula.release}} 版本的新功能测试，新功能列表参见[发布说明](../../20.appendix/releasenote.md)。

## 升级失败回滚

如果升级失败，停止新版本的所有服务，从备份中恢复配置文件和二进制文件，启动历史版本的服务。

所有周边客户端也切换为旧版。

## FAQ

Q：升级过程中是否可以通过客户端写入数据？

A：不可以。升级过程中需要停止所有服务。

Q：如果某台机器只有 Graph 服务，没有 Storage 服务，如何升级？

A：只需要升级 Graph 服务对应的二进制文件和配置文件。

Q：操作报错 `Permission denied`。

A：部分命令需要有 sudo 权限。

<!--
Q：是否有 gflags 发生改变？

A: 有部分 glags 改变了，详情参见版本发布说明和配置说明文档。
-->

Q：是否有工具或者办法验证新旧版本数据是否一致？

A：没有。如果只是检查数据量，可以在升级完成后再次运行`SUBMIT JOB STATS`和`SHOW STATS`统计数据量，并与升级之前做对比。

Q: Storage `OFFLINE`并且`Leader count`是`0`怎么处理？

A：运行以下命令手动添加 Storage 主机：

```ngql
ADD HOSTS <ip>:<port>[, <ip>:<port> ...];
```

例如：

```
ADD HOSTS 192.168.10.100:9779, 192.168.10.101:9779, 192.168.10.102:9779;
```

如果有多个 Meta 服务节点，手动`ADD HOSTS`之后，部分 Storage 节点需等待数个心跳（`heartbeat_interval_secs`）的时间才能正常连接到集群。

如果添加 Storage 主机后问题仍然存在，在[论坛](https://discuss.nebula-graph.com.cn/)或 [GitHub](https://github.com/vesoft-inc/nebula/issues) 提问。

Q：为什么升级后用`SHOW JOBS`查询到的 Job 的 ID 与升级前一样，但 Job 名称等信息不同了？

A： Nebula Graph 2.5.0 版本调整了 Job 的定义，详情参见 [Pull request](https://github.com/vesoft-inc/nebula-common/pull/562/files)。如果是从 2.5.0 之前的版本升级，会出现该问题。

Q: 有哪些语法不兼容 ?

A: 参见[Release Note](../../20.appendix/releasenote.md) Incompatibility 部分。
