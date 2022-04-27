# 部署 Explorer

本文介绍如何在本地通过 RPM 和 TAR 包部署 Explorer。

## Nebula Graph 版本支持


| Nebula Graph 版本 | Explorer 版本 |
| --- | --- |
| 3.0.0 ~ 3.1.x | 3.0.0  |
| 2.5.x ~ 3.0.0| 2.2.0|
| 2.6.x | 2.1.0 |
| 2.5.x | 2.0.0 |

## 前提条件

在部署 Explorer 之前，用户需要确认以下信息：

- Nebula Graph 服务已经部署并启动。详细信息参考 [Nebula Graph 安装部署](../../4.deployment-and-installation/1.resource-preparations.md "点击前往 Nebula Graph 安装部署")。

- 以下端口未被使用。

  | 端口号 | 说明 |
  | :---- | :---- |
  | 7002 | Explorer 提供的 web 服务 |

  !!! caution

       Explorer 默认使用的端口号为 7002，用户可以在安装目录下的 `conf/app.conf` 文件中修改 `httpport`，并重启服务。

- 使用的 Linux 发行版为 CentOS。
- 准备 License。

  !!! enterpriseonly

        License 仅在企业版提供，申请 License 需填写 [Nebula Explorer 试用申请](https://wj.qq.com/s2/9414111/81f4)。

## RPM 部署
### 安装

1. 根据需要下载 RPM 包，建议选择最新版本。

  !!! enterpriseonly

        用户可以[在线申请](https://wj.qq.com/s2/9414111/81f4)试用 Explorer 企业版；如需购买，通过邮箱(inquiry@vesoft.com)联系销售人员。点击[定价](https://nebula-graph.com.cn/pricing/)查看更多。

2. 使用`sudo rpm -i <rpm>`命令安装 RPM 包。

   例如，安装 Explorer 需要运行以下命令，默认安装路径为`/usr/local/nebula-explorer`：

   ```bash
   sudo rpm -i nebula-explorer-<version>.x86_64.rpm
   ```

   也可以使用以下命令安装到指定路径：
   ```bash
   sudo rpm -i nebula-explorer-xxx.rpm --prefix=<path> 
   ```

3. 拷贝 License 至安装路径下。

   ```bash
   cp -r <license> <explorer_path>
   ```

   例如：
   ```bash
   cp -r nebula.license /usr/local/nebula-explorer
   ```

4. 添加 License 后需要使用以下命令停止并重启服务。

   ```bash
   systemctl stop nebula-explorer #停止服务
   systemctl start nebula-explorer #启动服务
   ```

### 启停服务

支持使用 systemctl 服务控制项目启停。

```bash
systemctl status nebula-explorer #查看服务状态
systemctl stop nebula-explorer #停止服务
systemctl start nebula-explorer #启动服务
```
也可以在安装目录下使用以下命令，手动启动或停止服务。

```bash
cd ./scripts/rpm
bash ./start.sh #启动服务
bash ./stop.sh #停止服务
```

### 卸载

使用以下的命令卸载 Explorer。

```bash
sudo rpm -e nebula-explorer-<version>.x86_64
```

## 使用 DEB 包部署

### 安装

1. 下载 DEB 包。

  !!! enterpriseonly

        用户可以[在线申请](https://wj.qq.com/s2/9414111/81f4)试用 Explorer 企业版；如需购买，通过邮箱(inquiry@vesoft.com)联系销售人员。点击[定价](https://nebula-graph.com.cn/pricing/)查看更多。


2. 使用`sudo dpkg -i <package_name>`命令安装 DEB 包。

  例如，安装 Explorer 需要运行以下命令，默认安装路径为`/usr/local/nebula-explorer`：

  ```bash
  sudo dpkg -i nebula-explorer-{{explorer.release}}.x86_64.deb
  ```
  
  !!! note

        使用 DEB 包安装 Explorer 时不支持自定义安装路径。

3. 拷贝 License 至`nebula-explorer`目录下。

   ```bash
   sudo cp -r <license> <explorer_path>
   ```

   例如：
   ```bash
   sudo cp -r nebula.license /usr/local/nebula-explorer
   ```

4. 执行以下命令启动服务。

  ```bash
  sudo systemctl start nebula-explorer.service
  ```

  或者在`nebula-explorer/lib`目录下执行以下命令，启动服务。

   ```bash
   sudo bash ./start.sh
   ```

### 查看服务状态

```bash
sudo systemctl status nebula-explorer.service
```

### 停止服务

```bash
sudo systemctl stop nebula-explorer.service
```

### 卸载

使用以下的命令卸载 Explorer。

```bash
sudo dpkg -r nebula-explorer
```

## TAR 包部署

### 安装及部署

1. 根据需要下载 TAR 包，建议选择最新版本。

  !!! enterpriseonly

        Explorer 仅在企业版提供，点击[定价](https://nebula-graph.com.cn/pricing/)查看更多。

2. 使用 `tar -xvf` 解压 tar 包。

   ```bash
   tar -xvf nebula-graph-explorer-<version>.tar.gz
   ```

3. 拷贝 License 至`nebula-explorer`目录下。

   ```bash
   cp -r <license> <explorer_path>
   ```

   例如：
   ```bash
   cp -r nebula.license /usr/local/nebula-explorer
   ```

4. 进入`nebula-explorer`文件夹，启动 Explorer。

  ```bash
  cd nebula-explorer
  ./nebula-httpd &
  ```

### 停止服务

用户可以采用`kill pid`的方式来关停服务：

```bash
kill $(lsof -t -i :7002)
```

## 后续操作

启动成功后，在浏览器地址栏输入 `http://<ip_address>:7002`。

在浏览器窗口中看到以下登录界面表示已经成功部署并启动了 Explorer。

![Nebula Explorer 登录页面](https://docs-cdn.nebula-graph.com.cn/figures/explorer_deploy_cn.png)

!!! note

    首次登录 Nebula Explorer 的时候，页面显示*最终用户许可协议*的内容，请仔细阅读并单击**同意**。

进入 Explorer 登录界面后，用户需要连接 Nebula Graph。详细信息，参考[连接数据库](../deploy-connect/ex-ug-connect.md)。
