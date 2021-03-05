# 部署Nebula Graph集群

Nebula Graph暂不提供官方的集群部署工具，需要您手动部署，下文将介绍手动部署的简单流程。

## 手动部署流程

1. 准备用于部署集群的服务器。

2. 在服务器上安装Nebula Graph。

3. 修改每个服务器上的Nebula Graph配置文件。配置文件包括`nebula-graphd.conf`、`nebula-metad.conf`和`nebula-storaged.conf`，您可以只修改对应服务的配置文件。

   >**说明**：请重点关注IP地址和端口的设置，确保集群中各个服务可以通过网络互相访问。

4. 启动各个服务器上的对应服务。例如在提供Storage服务的服务器上启动Storage服务，无需启动Meta服务和Graph服务。

5. 连接Graph服务，测试集群能否正常工作。

