# Storage 负载均衡

用户可以使用`BALANCE`语句平衡分片和 Raft leader 的分布，或者清空某些 Storage 服务器方便进行维护。详情请参见 [BALANCE](../3.ngql-guide/18.operation-and-maintenance-statements/2.balance-syntax.md)。

!!! compatibility "历史版本兼容性"

    不支持`BALANCE DATA`命令。

<!-- balance-3.1
!!! danger

    `BALANCE`命令通过创建和执行一组子任务来迁移数据和均衡分片分布，不要停止集群中的任何机器或改变机器的 IP 地址，直到所有子任务完成，否则后续子任务会失败。

## 均衡分片分布

### 示例

以横向扩容 Nebula Graph 为例，Zone 中增加新的 Storage 服务器后，新服务器上没有分片。

1. 将新增的 3 台 Storage 服务器加入集群，分别加入图空间`basketballplayer`所属的 Zone。关于 Zone 的介绍请参见[管理逻辑机架（Zone）](../4.deployment-and-installation/5.zone.md)。

  ```ngql
  nebual> ADD HOSTS 192.168.10.103:9779 INTO ZONE "zone1";
  nebual> ADD HOSTS 192.168.10.104:9779 INTO ZONE "zone2";
  nebual> ADD HOSTS 192.168.10.105:9779 INTO ZONE "zone3";
  ```

2. 执行命令 [`SHOW HOSTS`](../3.ngql-guide/7.general-query-statements/6.show/6.show-hosts.md) 检查分片的分布。

  ```ngql
  nebual> SHOW HOSTS;
  +------------------+------+-----------+----------+--------------+-----------------------------------+------------------------+---------+
  | Host             | Port | HTTP port | Status   | Leader count | Leader distribution               | Partition distribution | Version |
  +------------------+------+-----------+----------+--------------+-----------------------------------+------------------------+---------+
  | "192.168.10.100" | 9779 | 19669     | "ONLINE" | 4            | "basketballplayer:4"              | "basketballplayer:15"  | "3.1.0" |
  | "192.168.10.101" | 9779 | 19669     | "ONLINE" | 8            | "basketballplayer:8"              | "basketballplayer:15"  | "3.1.0" |
  | "192.168.10.102" | 9779 | 19669     | "ONLINE" | 3            | "basketballplayer:3"              | "basketballplayer:15"  | "3.1.0" |
  | "192.168.10.103" | 9779 | 19669     | "ONLINE" | 0            | "No valid partition"              | "No valid partition"   | "3.1.0" |
  | "192.168.10.104" | 9779 | 19669     | "ONLINE" | 0            | "No valid partition"              | "No valid partition"   | "3.1.0" |
  | "192.168.10.105" | 9779 | 19669     | "ONLINE" | 0            | "No valid partition"              | "No valid partition"   | "3.1.0" |
  +------------------+------+-----------+----------+--------------+-----------------------------------+------------------------+---------+
  ```

3. 执行命令`BALANCE IN ZONE`将当前图空间内每个 Zone 内部的分片均衡分布。

  ```ngql
  nebula> USE basketballplayer;
  nebula> BALANCE IN ZONE;
  +------------+
  | New Job Id |
  +------------+
  | 30         |
  +------------+
  ```

4. 根据返回的作业 ID，执行命令`SHOW JOB <job_id>`检查作业状态。

  ```ngql
  nebula> SHOW JOB 30;
  +-------------------------+--------------------------------------------+-------------+---------------------------------+---------------------------------+
  | Job Id(spaceId:partId)  | Command(src->dst)                          | Status      | Start Time                      | Stop Time                       |
  +-------------------------+--------------------------------------------+-------------+---------------------------------+---------------------------------+
  | 30                      | "DATA_BALANCE"                             | "FINISHED"  | "2022-01-12T02:27:00.000000000" | "2022-01-12T02:30:31.000000000" |
  | "30, 23:1"              | "192.168.10.100:9779->192.168.10.103:9779" | "SUCCEEDED" | 2022-01-12T02:27:00.000000      | 2022-01-12T02:27:30.000000      |
  | "30, 23:2"              | "192.168.10.100:9779->192.168.10.103:9779" | "SUCCEEDED" | 2022-01-12T02:27:00.000000      | 2022-01-12T02:27:01.000000      |
  ......
  | "Total:21"              | "Succeeded:21"                             | "Failed:0"  | "In Progress:0"                 | "Invalid:0"                     |
  +-------------------------+--------------------------------------------+-------------+---------------------------------+---------------------------------+
  ```

5. 等待所有子任务完成，负载均衡进程结束，执行命令`SHOW HOSTS`确认分片已经均衡分布。

  !!! Note

        `BALANCE IN ZONE`不会均衡 leader 的分布。均衡 leader 请参见[均衡 leader 分布](#leader)。

  ```ngql
  nebula> SHOW HOSTS;
  +------------------+------+-----------+----------+--------------+-----------------------------------+------------------------+---------+
  | Host             | Port | HTTP port | Status   | Leader count | Leader distribution               | Partition distribution | Version |
  +------------------+------+-----------+----------+--------------+-----------------------------------+------------------------+---------+
  | "192.168.10.100" | 9779 | 19669     | "ONLINE" | 4            | "basketballplayer:4"              | "basketballplayer:8"   | "3.1.0" |
  | "192.168.10.101" | 9779 | 19669     | "ONLINE" | 8            | "basketballplayer:8"              | "basketballplayer:8"   | "3.1.0" |
  | "192.168.10.102" | 9779 | 19669     | "ONLINE" | 3            | "basketballplayer:3"              | "basketballplayer:8"   | "3.1.0" |
  | "192.168.10.103" | 9779 | 19669     | "ONLINE" | 0            | "No valid partition"              | "basketballplayer:7"   | "3.1.0" |
  | "192.168.10.104" | 9779 | 19669     | "ONLINE" | 0            | "No valid partition"              | "basketballplayer:7"   | "3.1.0" |
  | "192.168.10.105" | 9779 | 19669     | "ONLINE" | 0            | "No valid partition"              | "basketballplayer:7"   | "3.1.0" |
  +------------------+------+-----------+----------+--------------+-----------------------------------+------------------------+---------+
  ```

如果有子任务失败，请重启作业，详情参见[作业管理](../3.ngql-guide/18.operation-and-maintenance-statements/4.job-statements.md)。如果重做负载均衡仍然不能解决问题，请到 [Nebula Graph 社区](https://discuss.nebula-graph.com.cn/)寻求帮助。

## 停止负载均衡作业

停止负载均衡作业，请执行命令`STOP JOB <job_id>`。

- 如果没有正在执行的负载均衡作业，会返回错误。

- 如果有正在执行的负载均衡作业，会返回`Job stopped`。

!!! note

    - `STOP JOB <job_id>`不会停止正在执行的子任务，而是取消所有后续子任务，状态会置为`INVALID`，然后等待正在执行的子任执行完毕根据结果置为`SUCCEEDED`或`FAILED`。用户可以执行命令`SHOW JOB <job_id>`检查停止的作业状态。
    - 宕机重启后，作业状态变为`QUEUE`，子任务如果之前是`INVALID`或`FAILED`，状态会置为`IN_PROGRESS`，如果是`IN_PROGRESS`或`SUCCEEDED`则保持不变。

一旦所有子任务都完成或停止，用户可以再次执行命令`RECOVER JOB <job_id>`重启作业，子任务按原有的状态继续执行。

## 移除 Storage 服务器

移除指定的 Storage 服务器来缩小集群规模，可以使用命令`BALANCE IN ZONE REMOVE <ip>:<port> [,<ip>:<port> ...]`将指定 Storage 服务器清空，然后使用命令`DROP HOSTS <ip>:<port> [,<ip>:<port> ...]`将指定 Storage 服务器移除。

### 示例

如果需要移除以下两台 Storage 服务器。

|IP 地址|端口|
|:---|:---|
|192.168.10.104|9779|
|192.168.10.105|9779|

1. 执行如下命令清空指定 Storage 服务器：

  ```ngql
  nebula> BALANCE IN ZONE REMOVE 192.168.10.104:9779,192.168.10.105:9779;
  ```

2. 等待作业完成后，执行如下命令移除指定 Storage 服务：

  ```ngql
  nebula> DROP HOSTS 192.168.10.104:9779,192.168.10.105:9779;
  ```
-->

## 均衡 leader 分布

用户可以使用命令`BALANCE LEADER`均衡 leader 分布。

### 示例

```ngql
nebula> BALANCE LEADER;
```

用户可以执行`SHOW HOSTS`检查结果。

```ngql
nebula> SHOW HOSTS;
+------------------+------+-----------+----------+--------------+-----------------------------------+------------------------+---------+
| Host             | Port | HTTP port | Status   | Leader count | Leader distribution               | Partition distribution | Version |
+------------------+------+-----------+----------+--------------+-----------------------------------+------------------------+---------+
| "192.168.10.100" | 9779 | 19669     | "ONLINE" | 4            | "basketballplayer:3"              | "basketballplayer:8"   | "3.1.0" |
| "192.168.10.101" | 9779 | 19669     | "ONLINE" | 8            | "basketballplayer:3"              | "basketballplayer:8"   | "3.1.0" |
| "192.168.10.102" | 9779 | 19669     | "ONLINE" | 3            | "basketballplayer:3"              | "basketballplayer:8"   | "3.1.0" |
| "192.168.10.103" | 9779 | 19669     | "ONLINE" | 0            | "basketballplayer:2"              | "basketballplayer:7"   | "3.1.0" |
| "192.168.10.104" | 9779 | 19669     | "ONLINE" | 0            | "basketballplayer:2"              | "basketballplayer:7"   | "3.1.0" |
| "192.168.10.105" | 9779 | 19669     | "ONLINE" | 0            | "basketballplayer:2"              | "basketballplayer:7"   | "3.1.0" |
+------------------+------+-----------+----------+--------------+-----------------------------------+------------------------+---------+
```

!!! caution

    在 Nebula Graph {{ nebula.release }} 中，Leader 切换会导致短时的大量请求错误（Storage Error `E_RPC_FAILURE`），处理方法见 [FAQ](../20.appendix/0.FAQ.md)。
