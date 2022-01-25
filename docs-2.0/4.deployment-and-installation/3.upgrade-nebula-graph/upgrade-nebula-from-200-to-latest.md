# 升级 Nebula Graph 至 {{nebula.release}} 版本

Nebula Graph 支持以多种方式从 2.x 版本升级到 {{nebula.release}} 版本。

## 适用版本

本文适用于将 Nebula Graph 从 2.6.0 及之后的 2.x 版本升级到 {{nebula.release}} 版本。

!!! caution

    Nebula Graph 2.6.0 之前的历史版本不支持直接升级到 {{nebula.release}} 版本。如需升级历史版本到 {{nebula.release}} ，先将其升级到最新的 2.x 版本，方法参见相应版本的升级文档。

## 数据量变化

TODO

## 使用 RPM/DEB 包升级

1. 停止所有 Nebula Graph 服务，方法参见[管理 Nebula Graph 服务](../../2.quick-start/5.start-stop-service.md)。建议更新前备份配置文件。

2. （可选）备份旧版本的配置文件。

3. 检查当前配置文件`nebula-graphd.conf`中`session_idle_timeout_secs`参数的值是否在 1~604800 之间。如不是，调整参数值。参数说明和默认值参见 [Graph 服务配置](../../5.configurations-and-logs/1.configurations/3.graph-config.md)。

4. 下载 {{nebula.release}} 版本的 [RPM/DEB 包](https://nebula-graph.com.cn/download/)。

5. 执行如下命令升级。

  - RPM 包

    ```bash
    $ sudo rpm -Uvh <package_name>
    ```

    例如：

    ```bash
    sudo rpm -Uvh nebula-graph-3.0.0.el7.x86_64.rpm
    ```

    若安装时指定了路径，那么升级时也需要指定相同的路径：

    ```bash
    $ sudo rpm  -Uvh --prefix=<installation_path> <package_name> 
    ```

  - DEB 包

    ```bash
    $ sudo dpkg -i <package_name>
    ```

    例如：

    ```bash
    sudo dpkg -i nebula-graph-3.0.0.ubuntu2004.amd64.deb
    ```

6. 在每台服务器上启动所需的 Nebula Graph 服务，方法参见[管理 Nebula Graph 服务](../../2.quick-start/5.start-stop-service.md)。

7. 将所有 Storage 服务加入默认的逻辑机架，详情参见[管理逻辑机架](../5.zone.md)。

  例如，如果在 IP 地址为`192.168.10.1`、`192.168.10.2`、`192.168.10.3`的机器上各部署了一份 Storage 服务，端口号都是`9779`，运行以下命令将这些 Storage 服务节点加入默认 Zone：

  ```
  ADD HOSTS 192.168.10.1:9779, 192.168.10.2:9779, 192.168.10.3:9779;
  ```

## 编译新版本源码升级步骤

1. 备份旧版本的配置文件。配置文件保存在 Nebula Graph 安装路径的`etc`目录内。

2. 更新仓库并编译源码。详情请参见[使用源码安装 Nebula Graph](../2.compile-and-install-nebula-graph/1.install-nebula-graph-by-compiling-the-source-code.md)。

  !!! note

        编译时注意设置安装路径，和旧版本的安装路径保持一致。

## Docker Compose 部署升级步骤

1. 修改目录`nebula-docker-compose`内的文件`docker-compose.yaml`，将`image`后的所有版本都修改为`{{nebula.branch}}`。

2. 在目录`nebula-docker-compose`内执行命令`docker-compose pull`，更新所有服务的镜像版本。
 
3. 执行命令`docker-compose down`停止 Nebula Graph 服务。

4. 执行命令`docker-compose up -d`启动 Nebula Graph 服务。
