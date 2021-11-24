# 部署 Explorer

本文介绍如何在本地通过 RPM 和 tar 包部署 Explorer。

## Nebula Graph 版本支持

!!! Note

    Explorer 的版本单独发布，不与 Nebula Graph 内核同步，其命名方式也不遵守命名规则，两者兼容对应关系如下表。

| Nebula Graph 版本 | Explorer 版本 |
| --- | --- |
| 2.5.x | 2.0.0 |
| 2.6.x | 2.1.0 |

## RPM 部署

### 前提条件

在部署 Explorer 之前，用户需要确认以下信息：

- Nebula Graph 服务已经部署并启动。详细信息参考 [Nebula Graph 安装部署](../../4.deployment-and-installation/1.resource-preparations.md "点击前往 Nebula Graph 安装部署")。

- 以下端口未被使用。

  | 端口号 | 说明 |
  | ---- | ---- |
  | 7002 | Explorer 提供的 web 服务 |

  !!! caution

       Explorer 默认使用的端口号为 7002，用户可以在安装目录下的 `conf/app.conf` 文件中修改 `httpport`，并重启服务。

- 使用的 Linux 发行版为 CentOS。
- 安装有版本为 1.13 及以上的 Go。

### 安装

1. 根据需要下载 RPM 包，建议选择最新版本。

  !!! enterpriseonly

        Explorer 仅在企业版提供，点击[定价](https://nebula-graph.com.cn/pricing/) 查看更多。

2. 使用`sudo rpm -i <rpm>`命令安装 RPM 包。

   例如，安装 Explorer 需要运行以下命令，默认安装路径为`/usr/local/nebula-explorer`：

   ```bash
   $ sudo rpm -i nebula-explorer-<version>.x86_64.rpm
   ```

   也可以使用以下命令安装到指定路径：
   ```bash
   $ sudo rpm -i nebula-explorer-xxx.rpm --prefix=<path> 
   ```

3. 拷贝 License 至安装路径下。

   ```bash
   $ cp -r <license> <explorer_path>
   ```

   例如：
   ```bash
   $ cp -r nebula.license /usr/local/nebula-explorer
   ```

  !!! enterpriseonly

        License 仅在企业版提供，请发送邮件至 inquiry@vesoft.com。

4. 添加 License 后需要使用以下命令停止并重启服务。

   ```bash
   $ systemctl stop nebula-explorer #停止服务
   $ systemctl start nebula-explorer #启动服务
   ```

### 启停服务

支持使用 systemctl 服务控制项目启停。
```bash
$ systemctl status nebula-explorer #查看服务状态
$ systemctl stop nebula-explorer #停止服务
$ systemctl start nebula-explorer #启动服务
```
也可以在安装目录下使用以下命令，手动启动或停止服务：
```bash
$ cd ./scripts/rpm
$ bash ./start.sh #启动服务
$ bash ./stop.sh #停止服务
```

### 卸载

使用以下的命令卸载 Explorer。

```bash
$ sudo rpm -e nebula-explorer-<version>.x86_64
```
## tar 包部署

### 前提条件

在部署 Explorer 之前，用户需要确认以下信息：

- Nebula Graph 服务已经部署并启动。详细信息参考 [Nebula Graph 安装部署](../../4.deployment-and-installation/1.resource-preparations.md "点击前往 Nebula Graph 安装部署")。

- 以下端口未被使用。

  | 端口号 | 说明 |
  | :---- | :---- |
  | 7002 | Explorer 提供的 web 服务 |

  !!! caution

       Explorer 默认使用的端口号为 7002，用户可以在安装目录下的 `conf/app.conf` 文件中修改 `httpport`，并重启服务。

- 使用的 Linux 发行版为 CentOS。
- 安装有版本为 1.13 及以上的 Go。

### 安装及部署

1. 根据需要下载 tar 包，建议选择最新版本。

  !!! enterpriseonly

        Explorer 仅在企业版提供，点击[定价](https://nebula-graph.com.cn/pricing/) 查看更多。

2. 使用 `tar -xvf` 解压 tar 包。

   ```bash
   $ tar -xvf nebula-graph-explorer-<version>.tar.gz
   ```

3. 拷贝 License 至`nebula-explorer`目录下。

   ```bash
   $ cp -r <license> <explorer_path>
   ```

   例如：
   ```bash
   $ cp -r nebula.license /usr/local/nebula-explorer
   ```

  !!! enterpriseonly

        License 仅在企业版提供，请发送邮件至 inquiry@vesoft.com。

4. 进入`nebula-explorer`文件夹，启动 explorer。

  ```bash
  $ cd nebula-explorer
  $ ./nebula-httpd &
  ```

### 停止服务

用户可以采用`kill pid`的方式来关停服务：

```bash
$ kill $(lsof -t -i :7002)
```

## 后续操作

启动成功后，在浏览器地址栏输入 `http://<ip_address>:7002`。

在浏览器窗口中看到以下登录界面表示已经成功部署并启动了 Explorer。

![Nebula Explorer 登录页面](../figs/ex-ug-002-1.png)

进入 Explorer 登录界面后，用户需要连接 Nebula Graph。详细信息，参考[连接数据库](../deploy-connect/ex-ug-connect.md)。
