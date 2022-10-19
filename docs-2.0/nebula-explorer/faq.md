# 常见问题 FAQ

本文列出了使用 Explorer 时可能遇到的常见问题，用户可以使用文档中心或者浏览器的搜索功能查找相应问题。

## 如果 Graph 服务返回的查询结果数据量过大，会导致 Dag Controller 服务崩溃吗？

Dag Controller 服务仅仅提供调度功能，不会崩溃，但是数据量过大可能会导致 NebulaGraph Analytics 服务读写 HDFS 或者 NebulaGraph 时内存不足而崩溃。

## 如果一个作业中的某个任务失败，能否从失败的任务开始重新执行？

暂不支持，只能整体重新执行。

## 如果任务结果保存很慢，或任务间数据传输很慢，如何加速？

Dag Controller 包含图查询组件和图计算组件。图查询是发送请求给 Graph 进程进行查询，因此只能增大 Graph 服务的内存进行加速；图计算是由 NebulaGraph Analytics 提供的分布式节点进行计算，可以增大计算集群规模进行加速。

## HDFS 服务器无法连接时，任务状态一直为`running`怎么办？

为 HDFS 连接设置超时时间、次数，配置如下：

```bash
<configuration>
<property>
    <name>ipc.client.connect.timeout</name>
    <value>3000</value>
</property>

<property>
    <name>ipc.client.connect.max.retries.on.timeouts</name>
    <value>3</value>
</property>
</configuration>
```

## 任务运行失败，报错`Err:dial unix: missing address`怎么办？

修改`dag-ctrl/etc/dag-ctrl-api.yaml`配置文件，配置 SSH 的`UserName`。

## 任务运行失败，报错`bash: /home/xxx/nebula-analytics/scripts/run_algo.sh: No such file or directory`怎么办？

修改`dag-ctrl/etc/tasks.yaml`配置文件，配置算法执行路径`exec_file`。

## 任务运行失败，报错`/lib64/libm.so.6: version 'GLIBC_2.29' not found (required by /home/vesoft/jdk-18.0.1/jre/lib/amd64/server/libjvm.so)`怎么办？

由于 JDK18 版本太新，而操作系统版本太旧，`YUM`无法下载`GLIBC_2.29`，可以安装 JDK1.8，请同步修改`nebula-analytics/scripts/set_env.sh`中的 JDK 地址。

## 任务运行失败，报错`handshake failed: ssh: unable to authenticate, attempted methods [none publickey], no supported methods remain`怎么办？

重新配置`.ssh`文件夹及`.ssh/authorized_keys`文件的权限，`.ssh`文件夹权限为`744`，`.ssh/authorized_keys`文件权限为`600`。

## 任务运行失败，报错`There are 0 NebulaGraph Analytics available. clusterSize should be less than or equal to it`怎么办？

可能是因为如下原因：

- 未配置 NebulaGraph Analytics。请按本文档配置 NebulaGraph Analytics。

- 已配置 NebulaGraph Analytics，但是无法与 Dag Controller 联通。例如 地址错误、未配置 SSH、两个服务的启动用户不一致（导致 SSH 登录失败）等。

## 任务运行失败，报错`broadcast.hpp:193] Check failed: (size_t)recv_bytes >= sizeof(chunk_tail_t) recv message too small: 0`怎么办？

任务要处理的数据量过小，但是配置的计算节点数与进程数太多。需要在提交作业时设置较小的`clusterSize`和`processes`。