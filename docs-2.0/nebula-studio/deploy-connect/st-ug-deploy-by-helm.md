# 使用 Helm 部署 Nebula Graph Studio

本文介绍如何在通过 Kubernetes 集群里用 Helm 来部署并启动 Studio。

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

3. 安装 Studio 到 Helm Chart，命名为 `my-studio`。
   ```bash
   $ helm upgrade --install my-studio --set service.type=NodePort --set service.port=30070 deployment/helm
   ```

## 卸载

```bash
$ helm uninstall my-studio
```

## 后续操作

进入 Studio 登录界面后，用户需要连接 Nebula Graph。详细信息，参考[连接数据库](st-ug-connect.md)。

## Nebula Graph Studio Chart配置参数说明

| 参数 | 默认值 | 描述 |
|:---|:---|:---|
| replicaCount | 0 | StatefulSet 的副本计数 |
| image.httpGateway.repository | vesoft/nebula-http-gateway | HTTP Gateway 镜像的仓库地址。 |
| image.nebulaImporter.repository | vesoft/nebula-importer | Nebula Importer 镜像的仓库地址。 |
| image.nebulaStudio.repository | vesoft/nebula-graph-studio | Studio 镜像的仓库地址。 |
| image.nginx.repository | nginx | nginx 镜像的仓库地址。 |
| image.httpGateway.tag | v2 | HTTP Gateway 的版本。 |
| image.nebulaImporter.tag | v2 | Nebula Importer 的版本。 |
| image.nebulaStudio.tag | v3 | Studio 的版本。 |
| image.nginx.tag | alpine | nginx 的版本。 |
| service.type | ClusterIP | 服务类型，必须为`NodePort`，`ClusterIP`或`LoadBalancer`其中之一。 |
| service.port | 7001 | Studio 中 web 服务的端口。 |
| resources.httpGateway | {} | HTTP gateway 的资源限制/请求。 |
| resources.nebulaImporter | {} | Nebular Importer 的资源限制/请求。 |
| resources.nebulaStudio | {} | Studio 的资源限制/请求。 |
| resources.nginx | {} | nginx 的资源限制/请求。 |
| persistent.storageClassName | "" | storageClass名称，如果不指定就使用默认值。 |
| persistent.size | 5Gi | 上传数据持久化存储的大小。 |
