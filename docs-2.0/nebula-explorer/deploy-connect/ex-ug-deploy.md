# 部署 Explorer

本文介绍如何在本地通过 RPM 和 tar 包部署 Explorer。

## RPM 部署

### 前提条件

在部署 Explorer 之前，用户需要确认以下信息：

- Nebula Graph 服务已经部署并启动。详细信息参考[Nebula Graph安装部署](../../4.deployment-and-installation/1.resource-preparations.md "点击前往 Nebula Graph 安装部署")。

- 以下端口未被使用。

  | 端口号 | 说明 |
  | ---- | ---- |
  | 7002 | Explorer 提供的 web 服务 |
  | 8070 | Nebula-http-gateway 的 HTTP 服务 |
  
- 使用的 Linux 发行版为 CentOS ，安装有版本为 v10.16.0 + 以上的 Node.js。

### 安装

1. 根据需要下载 RPM 包，建议选择最新版本。

  !!! enterpriseonly

        Explorer 仅在企业版提供，点击 [定价](https://nebula-graph.com.cn/pricing/) 查看更多。

2. 使用`sudo rpm -i <rpm>`命令安装RPM包。

   例如，安装 Explorer 需要运行以下命令：

   ```bash
   $ sudo rpm -i nebula-graph-explorer-<version>.x86_64.rpm
   ```


### 卸载

使用以下的命令卸载 Explorer 。

```bash
$ sudo rpm -e nebula-graph-explorer-<version>.x86_64
```

### 异常处理

如果在安装过程中自动启动失败或是需要手动启动或停止服务，请使用以下命令.

- 手动启动服务
   
   ```bash
   $ sudo sh ./scripts/start.sh
   ```

- 手动停止服务

   ```bash  
   $ sudo sh ./scripts/stop.sh
   ```

## tar 包部署

### 前提条件

在部署 Explorer 之前，用户需要确认以下信息：

- Nebula Graph 服务已经部署并启动。详细信息参考[Nebula Graph安装部署](../../4.deployment-and-installation/1.resource-preparations.md "点击前往 Nebula Graph 安装部署")。

- 使用的 Linux 发行版为 CentOS ，安装有版本为 v10.16.0 + 以上的 Node.js。

- 以下端口未被使用。

  | 端口号 | 说明 |
  | ---- | ---- |
  | 7002 | Explorer 提供的 web 服务 |
  | 8070 | Nebula-http-gateway 的 HTTP 服务 |

### 安装

1. 根据需要下载 tar 包，建议选择最新版本。

  !!! enterpriseonly

        Explorer 仅在企业版提供，点击 [定价](https://nebula-graph.com.cn/pricing/) 查看更多。

2. 使用 `tar -xvf` 解压 tar 包。

   ```bash
   tar -xvf nebula-graph-explorer-<version>.tar.gz
   ```

### 部署

!!! Note

    根目录 nebula-graph-explorer 下一共有两个安装包：nebula-graph-explorer 和 nebula-http-gateway。用户需要在同一台机器上分别部署并启动服务，才能完成 Explorer 的部署。

1. 部署 nebula-http-gateway 并启动。

   ```bash
   $ cd nebula-http-gateway
   $ nohup ./nebula-httpd &
   ```

2. 部署 nebula-graph-explorer

   ```bash
   $ cd nebula-graph-explorer
   $ npm run start
   ```

### 停止服务

用户可以采用`kill pid`的方式来关停服务：

```bash
$ kill $(lsof -t -i :8070) # 停止 nebula-http-gateway
$ cd nebula-graph-explorer
$ npm run stop # 停止 nebula-graph-explorer
```

## 后续操作

启动成功后，在浏览器地址栏输入 `http://<ip_address>:7002`。

在浏览器窗口中看到以下登录界面表示已经成功部署并启动了 Explorer。

![Nebula Graph Explorer 登录页面](../figs/ex-ug-001.png)

进入 Explorer 登录界面后，用户需要连接 Nebula Graph。详细信息，参考[连接数据库](../deploy-connect/ex-ug-connect.md)。
