# 常见问题 FAQ

本文列出了使用{{explorer.name}}时可能遇到的常见问题，用户可以使用文档中心或者浏览器的搜索功能查找相应问题。

## 如果 Graph 服务返回的查询结果数据量过大，会导致 Dag Controller 服务崩溃吗？

Dag Controller 服务仅仅提供调度功能，不会崩溃，但是数据量过大可能会导致{{plato.name}}服务读写 HDFS 或者{{nebula.name}}时内存不足而崩溃。

## 如果一个作业中的某个任务失败，能否从失败的任务开始重新执行？

暂不支持，只能整体重新执行。

## 如果任务结果保存很慢，或任务间数据传输很慢，如何加速？

Dag Controller 包含图查询组件和图计算组件。图查询是发送请求给 Graph 进程进行查询，因此只能增大 Graph 服务的内存进行加速；图计算是由{{plato.name}}提供的分布式节点进行计算，可以增大计算集群规模进行加速。

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

## 任务运行失败，报错`bash: /home/xxx/yueshu-analytics/scripts/run_algo.sh: No such file or directory`怎么办？

修改`dag-ctrl/etc/tasks.yaml`配置文件，配置算法执行路径`exec_file`。

## 任务运行失败，报错`/lib64/libm.so.6: version 'GLIBC_2.29' not found (required by /home/vesoft/jdk-18.0.1/jre/lib/amd64/server/libjvm.so)`怎么办？

由于 JDK18 版本太新，而操作系统版本太旧，`YUM`无法下载`GLIBC_2.29`，可以安装 JDK1.8，请同步修改`yueshu-analytics/scripts/set_env.sh`中的 JDK 地址。

## 任务运行失败，报错`handshake failed: ssh: unable to authenticate, attempted methods [none publickey], no supported methods remain`怎么办？

重新配置`.ssh`文件夹及`.ssh/authorized_keys`文件的权限，`.ssh`文件夹权限为`744`，`.ssh/authorized_keys`文件权限为`600`。

## 任务运行失败，报错`There are 0 Yueshu Analytics available. clusterSize should be less than or equal to it`怎么办？

按如下流程排查：

1. 检查节点间 SSH 免密登录配置是否配置成功。可以在 Dag Controller 机器上执行`ssh <user_name>@<node_ip>`命令看能否成功登录。

  !!! note

        Dag Controller 和{{plato.name}}在同一台机器时，也需要配置免密登录。

2. 检查 Dag Controller 的配置文件。

  - 检查`etc/dag-ctrl-api.yaml`中的 SSH 用户和启动 Dag Controller 服务的用户、配置 SSH 免密登录的用户是不是一致。

  - 检查`etc/tasks.yaml`中的算法路径是否正确。

  - 检查`scripts/set_env.sh`中的 Hadoop 和 Java 的路径是否正确。

3. 修改上述配置后需要重启 Dag Controller 使配置生效。

## 任务运行失败，报错`no available namenodes: dial tcp xx.xx.xx.xx:8020: connect: connection timed out`怎么办？

请检查 HDFS 的 namenode 端口 8020 是否开放。

## 任务运行失败，报错`org.apache.hadoop.net.ConnectTimeoutException: 60000 millis timeout`怎么办？

请检查 HDFS 的 datanode 端口 50010 是否开放。

如果没有开放端口，还可能报类似如下错误：

- `Check failed: false close hdfs-file failed`
- `org.apache.hadoop.ipc.RemoteException(java.io.IOException): File /analytics/xx/tasks/analytics_xxx/xxx.csv could only be replicated to 0 nodes instead of minReplication`


## 任务运行失败，报错`broadcast.hpp:193] Check failed: (size_t)recv_bytes >= sizeof(chunk_tail_t) recv message too small: 0`怎么办？

任务要处理的数据量过小，但是配置的计算节点数与进程数太多。需要在提交作业时设置较小的`clusterSize`和`processes`。

## 如何实现高可用架构

用户可以使用第三方高可用软件（例如 [HAProxy](https://www.haproxy.org/)）实现{{explorer.name}}的高可用架构。

例如，用户可以在多台机器上部署{{explorer.name}}服务、数据库服务，然后使用 HAProxy 实现各自的负载均衡。

然后将数据库服务的对外接口填写到{{explorer.name}}的配置中，示例如下：

```yaml
# {{explorer.name}}的部署模式，支持单实例和多实例。可选值为：single 和 multi。默认值为 single。
# 多实例模式下，本地的存储服务(数据导入)将被禁止，以保证实例之间的数据一致性。
AppInstance: "multi" 

# 数据库配置
DB:
  Enable: true
  LogLevel: 4  # 数据库运行日志级别。1、2、3、4 分别对应 Silent、ERROR、Warn、INFO。
  IgnoreRecordNotFoundError: false  
  AutoMigrate: true  # 是否自动创建数据库表。默认为 true。
  Type: "mysql"  # 后端使用的数据库类型。可选值为 mysql 和 sqlite3。PolarDB 完全兼容 MySQL, 如果是 PolarDB，填写 mysql 即可。
  Host: "192.168.8.200:3306"  # 数据库高可用服务的对外 IP 和端口。
  Name: "nebula"  # 数据库名称。
  User: "root"  # 数据库用户名。
  Password: "123456"  # 数据库密码。
  # SqliteDbFilePath: "./data/tasks.db"   # 仅 sqlite3 需要填写该参数。数据库文件地址。
  MaxOpenConns: 30  # 连接池最大活跃连接数。
  MaxIdleConns: 10  # 连接池最大空闲连接数。
LicenseManagerURL: http://192.168.8.100:9119 # License Manager 所在的主机 IP，端口默认为9119。
```

最后访问 HAProxy 提供的{{explorer.name}}对外接口即可。

关于详细的配置方案，可以联系售后工作人员咨询。