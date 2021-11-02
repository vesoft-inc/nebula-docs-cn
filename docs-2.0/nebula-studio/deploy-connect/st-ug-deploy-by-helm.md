# 使用Helm部署Studio

本文介绍如何在Kubernetes中使用Helm部署并启动Studio。

## 前提条件

安装Studio前，用户需要安装以下软件并确保安装版本的正确性：

| 软件                                                         | 版本要求  |
| ------------------------------------------------------------ | --------- |
| [Kubernetes](https://kubernetes.io)                          | \>= 1.14  |
| [Helm](https://helm.sh)                                      | \>= 3.2.0 |

## 安装

1. 克隆Studio的源代码到主机。

  ```bash
  $ git clone https://github.com/vesoft-inc/nebula-studio.git
  ```

2. 进入`nebula-studio`目录。

  ```bash
  $ cd nebula-studio
  ```

3. 更新并安装Nebula Graph Studio chart，命名为`my-studio`。

  ```bash
  $ helm upgrade --install my-studio --set service.type=NodePort --set service.port={30070} deployment/helm
  ```

4. 启动成功后，在浏览器地址栏输入`http://{address-of-node}:{30070}/`。
   如果在浏览器窗口中能看到以下登录界面，表示已经成功部署并启动 Studio。

   ![Nebula Graph Studio 登录界面](../figs/st-ug-001-1.png "Nebula Graph Studio 登录界面")

## 卸载

```bash
$ helm uninstall my-studio
```

## 后续操作

进入Studio登录界面后，用户需要连接Nebula Graph。详细信息，参考[连接数据库](st-ug-connect.md)。

## Nebula Graph Studio chart配置参数说明

| 参数 | 默认值 | 描述 |
|:---|:---|:---|
| replicaCount | 0 | Deployment的副本数。 |
| image.httpGateway.name | vesoft/nebula-http-gateway | nebula-http-gateway镜像的仓库地址。 |
| image.nebulaStudio.name | vesoft/nebula-graph-studio | nebula-graph-studio镜像的仓库地址。 |
| image.nginx.name | nginx | nginx镜像的仓库地址。 |
| image.httpGateway.version | v2.1.1 | nebula-http-gateway的版本。 |
| image.nebulaStudio.version | v3.1.0 | nebula-graph-studio的版本。 |
| image.nginx.version | alpine | nginx的版本。 |
| service.type | ClusterIP | 服务类型，必须为`NodePort`，`ClusterIP`或`LoadBalancer`其中之一。 |
| service.port | 7001 | nebula-graph-studio中web服务的端口。 |
| resources.httpGateway | {} | nebula-http-gateway的资源限制/请求。 |
| resources.nebulaStudio | {} | nebula-studio的资源限制/请求。 |
| resources.nginx | {} | nginx的资源限制/请求。 |
| persistent.storageClassName | "" | storageClass名称，如果不指定就使用默认值。 |
| persistent.size | 5Gi | 存储盘大小。 |
