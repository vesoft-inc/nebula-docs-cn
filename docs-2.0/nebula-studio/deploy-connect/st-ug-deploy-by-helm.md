# 使用 Helm 部署 Studio

本文介绍如何在 Kubernetes 中使用 Helm 部署并启动 Studio。

## 前提条件

安装 Studio 前，用户需要安装以下软件并确保安装版本的正确性：

| 软件                                                         | 版本要求  |
| ------------------------------------------------------------ | --------- |
| [Kubernetes](https://kubernetes.io)                          | \>= 1.14  |
| [Helm](https://helm.sh)                                      | \>= 3.2.0 |

## 安装

1. 克隆 Studio 的源代码到主机。

  ```bash
  $ git clone https://github.com/vesoft-inc/nebula-studio.git
  ```

2. 进入`nebula-studio`目录。

  ```bash
  $ cd nebula-studio
  ```

3. 更新并安装 Nebula Graph Studio chart，命名为`my-studio`。

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

进入 Studio 登录界面后，用户需要连接 Nebula Graph。详细信息，参考 [连接数据库](st-ug-connect.md)。

## Nebula Graph Studio chart 配置参数说明

| 参数 | 默认值 | 描述 |
|:---|:---|:---|
| replicaCount | 0 | Deployment 的副本数。 |
| image.httpGateway.name | vesoft/nebula-http-gateway | nebula-http-gateway 镜像的仓库地址。 |
| image.nebulaStudio.name | vesoft/nebula-graph-studio | nebula-graph-studio 镜像的仓库地址。 |
| image.nginx.name | nginx | nginx 镜像的仓库地址。 |
| image.httpGateway.version | v2.1.1 | nebula-http-gateway 的版本。 |
| image.nebulaStudio.version | v3.1.0 | nebula-graph-studio 的版本。 |
| image.nginx.version | alpine | nginx 的版本。 |
| service.type | ClusterIP | 服务类型，必须为`NodePort`，`ClusterIP`或`LoadBalancer`其中之一。 |
| service.port | 7001 | nebula-graph-studio 中 web 服务的端口。 |
| resources.httpGateway | {} | nebula-http-gateway 的资源限制/请求。 |
| resources.nebulaStudio | {} | nebula-studio 的资源限制/请求。 |
| resources.nginx | {} | nginx 的资源限制/请求。 |
| persistent.storageClassName | "" | storageClass 名称，如果不指定就使用默认值。 |
| persistent.size | 5Gi | 存储盘大小。 |
