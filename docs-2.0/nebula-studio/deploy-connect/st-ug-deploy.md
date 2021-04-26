# 部署 Studio

云服务版 Studio 只能在 Nebula Graph Cloud Service 上使用。当您在 Nebula Graph Cloud Service 上创建 Nebula Graph 实例时即自动完成云服务版本 Studio 的部署，一键直连即可使用，不需要自己部署。详细信息参考[《Nebula Graph Cloud Service 用户手册》](https://cloud-docs.nebula-graph.com.cn/cn/posts/manage-instances/dbaas-ug-connect-nebulastudio/ "点击前往 Nebula Graph Cloud Service 用户手册")。但是，您需要自己部署 Studio，本文描述如何通过 Docker 和 RPM 部署 Studio。

## Docker 部署Studio
### 前提条件

在部署 Docker 版 Studio 之前，您需要确认以下信息：

- Nebula Graph 服务已经部署并启动。详细信息，参考[Nebula Graph 安装部署](https://docs.nebula-graph.com.cn/2.0.1/4.deployment-and-installation/1.resource-preparations/ "点击前往 Nebula Graph 安装部署")。
  > **说明**：您可以使用Docker Compose或RPM方式部署并启动 Nebula Graph 服务。如果您刚开始使用 Nebula Graph，建议您使用 Docker Compose 部署 Nebula Graph。详细信息参考 [使用 Docker Compose 部署 Nebula Graph](https://docs.nebula-graph.com.cn/2.0.1/2.quick-start/2.deploy-nebula-graph-with-docker-compose/ "点击前往Nebula Graph 安装部署")。

- 在即将运行 Docker 版 Studio 的机器上安装并启动 Docker Compose。详细信息参考 [Docker Compose 文档](https://docs.docker.com/compose/install/ "点击前往 Docker 文档中心")。

- （可选）在中国大陆从 Docker Hub 拉取 Docker 镜像的速度可能比较慢，您可以使用 `registry-mirrors` 参数配置加速镜像。例如，如果您要使用 Docker 中国区官方镜像、网易镜像和中国科技大学的镜像，则按以下格式配置 `registry-mirrors` 参数：

  ```json
  {
  "registry-mirrors": [
    "https://registry.docker-cn.com",
    "http://hub-mirror.c.163.com",
    "https://docker.mirrors.ustc.edu.cn"
    ]
  }
  ```

  配置文件的路径和方法因您的操作系统和/或 Docker Desktop 版本而异。详细信息参考 [Docker Daemon 配置文档](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file "点击前往 Docker 文档中心")。

### 操作步骤

在命令行工具中按以下步骤依次运行命令，部署并启动 Docker 版 Studio：

1. 下载 Studio 的部署配置文件。

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

4. 构建并启动 Studio 服务。其中，`-d` 表示在后台运行服务容器。

   ```bash
   docker-compose up -d
   ```

    当屏幕返回以下信息时，表示 Docker 版 Studio 已经成功启动。

    ```bash
    Creating docker_importer_1 ... done
    Creating docker_client_1   ... done
    Creating docker_web_1      ... done
    Creating docker_nginx_1    ... done
    ```

5. 启动成功后，在浏览器地址栏输入 `http://ip address:7001`。
   > **说明**：在运行 Docker 版 Studio 的机器上，您可以运行 `ifconfig` 或者 `ipconfig` 获取本机 IP 地址。如果您使用这台机器访问 Studio，可以在浏览器地址栏里输入 `http://localhost:7001`。

    如果您在浏览器窗口中能看到以下登录界面，表示您已经成功部署并启动 Studio。

    ![Nebula Graph Studio 登录界面](../figs/st-ug-001.png "Nebula Graph Studio 登录界面")

## RPM 部署Studio
### 前提条件

在部署 Docker 版 Studio 之前，您需要确认以下信息：

- Nebula Graph 服务已经部署并启动。详细信息，参考[Nebula Graph 安装部署](https://docs.nebula-graph.com.cn/2.0.1/4.deployment-and-installation/1.resource-preparations/ "点击前往 Nebula Graph 安装部署")。
  > **说明**：您可以使用Docker Compose或RPM方式部署并启动 Nebula Graph 服务。如果您刚开始使用 Nebula Graph，建议您使用 Docker Compose 部署 Nebula Graph。详细信息参考 [使用 Docker Compose 部署 Nebula Graph](https://docs.nebula-graph.com.cn/2.0.1/2.quick-start/2.deploy-nebula-graph-with-docker-compose/ "点击前往Nebula Graph 安装部署")。
- 您的使用的 Linux 发行版为 CentOS ，安装有 losf 和版本为 v10.16.0 + 以上的 Node.js。
- 确保在安装开始前，以下端口处于未被使用状态。

| 端口号 | 服务 |
| ---- | ---- |
| 7001 | Studio的web服务 |
| 8080 | Nebula-http-gateway，Client的http服务 |
| 5699 | Nebula-importer，数据导入服务 |

### 安装

您可以根据自己的需求，选择并下载RPM包，建议您选择最新版本。
| RPM 包 | 版本|
| ----- | ----- |
| [nebula-graph-studio-2.2.0-1.x86_64.rpm](https://oss-cdn.nebula-graph.io/nebula-graph-studio/nebula-graph-studio-2.2.0-1.x86_64.rpm) |  2.0.1 |
| [nebula-graph-studio-2.1.9-1.x86_64.rpm](https://oss-cdn.nebula-graph.io/nebula-graph-studio/nebula-graph-studio-2.1.9-1.x86_64.rpm) |  2.0 GA |
| [nebula-graph-studio-1.2.7-2.x86_64.rpm](https://oss-cdn.nebula-graph.io/nebula-graph-studio/nebula-graph-studio-1.2.7-1.x86_64.rpm) |  1.x |

以 Nebula 2.0.1 版本为例，您可以使用以下命令进行安装。
```bash
$ sudo rpm -i nebula-graph-studio-2.2.0-1.x86_64.rpm
```
### 删除
您可以使用以下的命令删除安装。
```bash
$ sudo rpm -e nebula-graph-studio-2.2.0-1.x86_64.rpm
```

### 异常处理

如果您在安装过程中自动启动失败或是您需要手动启动/停止服务，我们提供了以下的命令。
```bash
// 手动启动服务
$ bash /usr/local/nebula-graph-studio/scripts/start.sh

// 手动停止服务
$ bash /usr/local/nebula-graph-studio/scripts/stop.sh
```

如果您在启动服务中，报错 ERROR: bind EADDRINUSE 0.0.0.0:7001，您可以通过以下命令查看端口7001是否被占用。
```bash
$ losf -i:7001
```

如果端口被占用，且无法结束该端口上进程，您可以通过以下命令修改Studio服务启动端口，并重新启动服务。
```bash
//修改studio服务启动端口
 $ vi config/config.default.js

 //修改
 ...
     config.cluster = {
         listen: {
             port: 7001, // 修改这个端口号，改成任意一个当前可用的即可
             hostname: '0.0.0.0',
         },
     };
 ...

 //重新启动npm
 $ npm run start
```
## 后续操作

进入 Studio 登录界面后，您需要连接 Nebula Graph。详细信息，参考 [连接数据库](st-ug-connect.md)。
