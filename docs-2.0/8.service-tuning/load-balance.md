# Storage负载均衡

用户可以使用`BALANCE`语句平衡分片和Raft leader的分布，或者删除冗余的Storage服务器。

## 均衡分片分布

`BALANCE DATA`语句会开始一个任务，将Nebula Graph集群中的分片平均分配到所有Storage服务器。通过创建和执行一组子任务来迁移数据和均衡分片分布。

!!! danger

    不要停止集群中的任何机器或改变机器的IP地址，直到所有子任务完成，否则后续子任务会失败。

### 示例

以横向扩容Nebula Graph为例，集群中增加新的Storage服务器后，新服务器上没有分片。

1. 执行命令[`SHOW HOSTS`](../3.ngql-guide/7.general-query-statements/6.show/6.show-hosts.md)检查分片的分布。

    ```ngql
    nebual> SHOW HOSTS;
    +-------------+------+----------+--------------+-----------------------------------+------------------------+
    | Host        | Port | Status   | Leader count | Leader distribution               | Partition distribution |
    +-------------+------+----------+--------------+-----------------------------------+------------------------+
    | "storaged0" | 9779 | "ONLINE" | 4            | "basketballplayer:4"              | "basketballplayer:15"  |
    | "storaged1" | 9779 | "ONLINE" | 8            | "basketballplayer:8"              | "basketballplayer:15"  |
    | "storaged2" | 9779 | "ONLINE" | 3            | "basketballplayer:3"              | "basketballplayer:15"  |
    | "storaged3" | 9779 | "ONLINE" | 0            | "No valid partition"              | "No valid partition"   |
    | "storaged4" | 9779 | "ONLINE" | 0            | "No valid partition"              | "No valid partition"   |
    | "Total"     |      |          | 15           | "basketballplayer:15"             | "basketballplayer:45"  |
    +-------------+------+----------+--------------+-----------------------------------+------------------------+
    ```

2. 执行命令`BALANCE DATA`将所有分片均衡分布。

    ```ngql
    nebula> BALANCE DATA;
    +------------+
    | ID         |
    +------------+
    | 1614237867 |
    +------------+
    ```

3. 根据返回的任务ID，执行命令`BALANCE DATA <balance_id>`检查任务状态。

    ```ngql
    nebula> BALANCE DATA 1614237867;
    +--------------------------------------------------------------+-------------------+
    | balanceId, spaceId:partId, src->dst                          | status            |
    +--------------------------------------------------------------+-------------------+
    | "[1614237867, 11:1, storaged1:9779->storaged3:9779]"         | "SUCCEEDED"       |
    | "[1614237867, 11:1, storaged2:9779->storaged4:9779]"         | "SUCCEEDED"       |
    | "[1614237867, 11:2, storaged1:9779->storaged3:9779]"         | "SUCCEEDED"       |
    ...
    | "Total:22, Succeeded:22, Failed:0, In Progress:0, Invalid:0" | 100               |
    +--------------------------------------------------------------+-------------------+
    ```

4. 等待所有子任务完成，负载均衡进程结束，执行命令`SHOW HOSTS`确认分片已经均衡分布。

  !!! Note

        `BALANCE DATA`不会均衡leader的分布。均衡leader请参见[均衡leader分布](#leader)。

    ```ngql
    nebula> SHOW HOSTS;
    +-------------+------+----------+--------------+-----------------------------------+------------------------+
    | Host        | Port | Status   | Leader count | Leader distribution               | Partition distribution |
    +-------------+------+----------+--------------+-----------------------------------+------------------------+
    | "storaged0" | 9779 | "ONLINE" | 4            | "basketballplayer:4"              | "basketballplayer:9"   |
    | "storaged1" | 9779 | "ONLINE" | 8            | "basketballplayer:8"              | "basketballplayer:9"   |
    | "storaged2" | 9779 | "ONLINE" | 3            | "basketballplayer:3"              | "basketballplayer:9"   |
    | "storaged3" | 9779 | "ONLINE" | 0            | "No valid partition"              | "basketballplayer:9"   |
    | "storaged4" | 9779 | "ONLINE" | 0            | "No valid partition"              | "basketballplayer:9"   |
    | "Total"     |      |          | 15           | "basketballplayer:15"             | "basketballplayer:45"  |
    +-------------+------+----------+--------------+-----------------------------------+------------------------+
    ```

如果有子任务失败，请重新执行`BALANCE DATA`。如果重做负载均衡仍然不能解决问题，请到[Nebula Graph社区](https://discuss.nebula-graph.com.cn/)寻求帮助。

## 停止负载均衡任务

停止负载均衡任务，请执行命令`BALANCE DATA STOP`。

- 如果没有正在执行的负载均衡任务，会返回错误。

- 如果有正在执行的负载均衡任务，会返回停止的任务ID（`balance_id`）。

`BALANCE DATA STOP`不会停止正在执行的子任务，而是取消所有后续子任务。用户可以执行命令`BALANCE DATA <balance_id>`检查停止的任务状态。

一旦所有子任务都完成或停止，用户可以再次执行命令`BALANCE DATA`。

- 如果前一个负载均衡任务的任何一个子任务失败，Nebula Graph会重新启动之前的负载均衡任务。

- 如果前一个负载均衡任务的任何一个子任务都没有失败，Nebula Graph会启动一个新的的负载均衡任务。

## 重置负载均衡任务

如果停止负载均衡任务后重新执行仍然失败，可以尝试用命令`BALANCE DATA RESET PLAN`重置负载均衡任务，该操作会清空旧的任务。之后再使用`BALANCE DATA`命令，会新建负载均衡任务，而不是执行旧的任务。

## 移除Storage服务器

移除指定的Storage服务器来缩小集群规模，可以使用命令`BALANCE DATA REMOVE <host_list>`。

### 示例

如果需要移除以下两台Storage服务器。

|服务器名称|IP地址|端口|
|:---|:---|:---|
|storage3|192.168.0.8|9779|
|storage4|192.168.0.9|9779|

请执行如下命令：

```ngql
BALANCE DATA REMOVE 192.168.0.8:9779,192.168.0.9:9779;
```

Nebula Graph将启动一个负载均衡任务，迁移storage3和storage4中的分片，然后将服务器从集群中移除。

!!! note

    已下线节点状态会显示为 OFFLINE。该记录一天后删除，或更改 meta 配置项 `removed_threshold_sec`。

## 均衡leader分布

`BALANCE DATA`只能均衡分片分布，不能均衡Raft leader分布。用户可以使用命令`BALANCE LEADER`均衡leader分布。

### 示例

```ngql
nebula> BALANCE LEADER;
```

用户可以执行`SHOW HOSTS`检查结果。

```ngql
nebula> SHOW HOSTS;
+-------------+------+----------+--------------+-----------------------------------+------------------------+
| Host        | Port | Status   | Leader count | Leader distribution               | Partition distribution |
+-------------+------+----------+--------------+-----------------------------------+------------------------+
| "storaged0" | 9779 | "ONLINE" | 3            | "basketballplayer:3"              | "basketballplayer:9"   |
| "storaged1" | 9779 | "ONLINE" | 3            | "basketballplayer:3"              | "basketballplayer:9"   |
| "storaged2" | 9779 | "ONLINE" | 3            | "basketballplayer:3"              | "basketballplayer:9"   |
| "storaged3" | 9779 | "ONLINE" | 3            | "basketballplayer:3"              | "basketballplayer:9"   |
| "storaged4" | 9779 | "ONLINE" | 3            | "basketballplayer:3"              | "basketballplayer:9"   |
| "Total"     |      |          | 15           | "basketballplayer:15"             | "basketballplayer:45"  |
+-------------+------+----------+--------------+-----------------------------------+------------------------+
```

!!! caution

    在 Nebula Graph {{ nebula.release }} 中，Leader 切换会导致短时的大量请求错误（Storage Error `E_RPC_FAILURE`），处理方法见[FAQ](../20.appendix/0.FAQ.md)。
