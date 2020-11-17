# 部署 Studio

Studio 目前有两种发行版本：Docker 版本和云服务版本。本文主要描述如何部署Docker 版本 Studio。

云服务版本 Studio 只能在 Nebula Graph Cloud Service 上使用，不需要您手动部署。详细信息参考[《Nebula Graph Cloud Service 用户手册》](https://cloud-docs.nebula-graph.com.cn/cn/posts/manage-instances/dbaas-ug-connect-nebulastudio/ "点击前往 Nebula Graph Cloud Service 用户手册")。

## 前提条件

在部署 Docker 版本 Studio 之前，您需要确认以下信息：

- Nebula Graph 服务已经部署并启动。详细信息，参考[《Nebula Graph 用户手册》](https://docs.nebula-graph.io/manual-EN/3.build-develop-and-administration/2.install/1.install-with-rpm-deb/ "点击前往 Nebula Graph 用户手册")。
  > **说明**：您可以使用多种方式部署并启动 Nebula Graph 服务。如果您刚开始使用 Nebula Graph，建议您使用 Docker Compose 部署 Nebula Graph。详细信息参考 [使用 Docker Compose 部署 Nebula Graph](https://github.com/vesoft-inc/nebula-docker-compose/blob/master/README_zh-CN.md "点击前往 GitHub 网站")。
  >

- 在即将运行 Docker 版本 Studio 的机器上安装并启动 Docker Compose。详细信息参考 [Docker Compose 文档](https://docs.docker.com/compose/install/ "点击即进入 Docker 文档中心")。

- （可选）在中国大陆从 Docker Hub 拉取 Docker 镜像速度可能比较慢。您可以通过 `registry-mirrors` 参数配置加速镜像，例如：
  - Docker中国区官方：`https://registry.docker-cn.com`
  - 网易：`http://hub-mirror.c.163.com`
  - 中国科技大学：`https://docker.mirrors.ustc.edu.cn`
  配置方法因您的操作系统而异。详细信息参考 [Docker Daemon 配置文档](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file "点击前往 Docker 官方网站")。

## 操作步骤

按以下步骤部署并启动 Docker 版本 Studio：

1. 下载 Studio 的安装部署源码。

    ```bash
    git clone https://github.com/vesoft-inc/nebula-web-docker.git
    ```

2. 切换到 `nebula-web-docker` 目录。

    ```bash
    cd nebula-web-docker
    ```

3. 拉取 Studio 的 Docker 镜像。

    ```bash
    docker-compose pull
    ```

4. 构建容器并启动 Studio 服务。其中，`-d` 表示在后台运行服务容器。

   ```bash
   docker-compose up -d
   ```

    当屏幕返回以下信息时，表示 Docker 版本 Studio 已经成功启动。

    ```bash
    Creating docker_importer_1 ... done
    Creating docker_client_1   ... done
    Creating docker_web_1      ... done
    Creating docker_nginx_1    ... done
    ```

5. 启动成功后，在浏览器地址栏输入 `http://localhost:7001`。

    如果您在浏览器窗口中能看到以下登录界面，表示您已经成功部署并启动 Studio。

    ![Nebula Graph Studio 登录界面](https://docs-cdn.nebula-graph.com.cn/nebula-studio-docs/st-ug-001.png "Nebula Graph Studio 登录界面")

## 后续操作

进入 Studio 登录界面后，您需要连接 Nebula Graph。详细信息，参考 [连接数据库](st-ug-connect.md)。
