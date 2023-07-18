# 部署{{explorer.name}}

本文介绍如何在本地通过 RPM、DEB 和 TAR 包部署{{explorer.name}}。

## 前提条件

在部署{{explorer.name}}之前，用户需要确认以下信息：

- 已[在 LM 中加载 License Key](../../9.about-license/2.license-management-suite/3.license-manager.md)。

- {{nebula.name}}服务已经部署并启动。详细信息参考 [{{nebula.name}}安装部署](../../4.deployment-and-installation/1.resource-preparations.md "点击前往{{nebula.name}}安装部署")。

- 以下端口未被使用。

  | 端口号 | 说明 |
  | :---- | :---- |
  | 7002 | {{explorer.name}}提供的 web 服务 |

  !!! caution

       {{explorer.name}}默认使用的端口号为 7002，用户可以在安装目录下的 `conf/app.conf` 文件中修改 `httpport`，并重启服务。

- 使用的 Linux 发行版为 CentOS。

## 注意事项

{{explorer.name}}从 3.2.0 版本开始内置了 Dag Controller 安装包，用于提供图计算服务。用户可以自行决定是否启动 Dag Controller 服务。如果没有启动 Dag Controller 服务，{{explorer.name}}中的 **Workflow** 菜单将显示为灰色无法点击。

此外，如果需要使用 **Workflow** 进行复杂图计算，还需在安装{{explorer.name}}后配置 NFS 或 HDFS，namenode 默认使用 8020 端口，datanode 默认使用 50010 端口。详情参见 **Workflow** 的[资源配置](../../nebula-explorer/workflow/1.prepare-resources.md)。

<!--  !!! caution

       如果 HDFS 端口不通，可能会提示连接超时。-->

## RPM 部署

### 安装

1. 根据需要下载 RPM 包，建议选择最新版本。

2. 使用`sudo rpm -i <rpm>`命令安装 RPM 包。

   例如，安装{{explorer.name}}需要运行以下命令，默认安装路径为`/usr/local/yueshu-explorer`：

   ```bash
   sudo rpm -i yueshu-explorer-<version>.x86_64.rpm
   ```

   也可以使用`--prefix`选项安装到指定路径：
   ```bash
   sudo rpm -i yueshu-explorer-<version>.x86_64.rpm --prefix=<path> 
   ```

3. 进入解压后的文件夹，在`config`目录内修改`app-config.yaml`文件，设置`LicenseManagerURL`的值为 LM 所在的主机 IP 和端口号`9119`，例如`192.168.8.100:9119`。

4. （可选）配置 Dag Controller。参见下文 **配置 Dag Controller** 部分。

5. 进入`yueshu-explorer`文件夹，执行以下命令启动服务。

   ```bash
   cd yueshu-explorer

   # 启动{{explorer.name}}。
   sudo ./scripts/start.sh

   # （可选）启动 Dag Controller。
   sudo ./dag-ctrl/scripts/start.sh
   ```

### 启停服务

支持使用 systemctl 服务控制项目启停。

```bash
systemctl status yueshu-explorer #查看服务状态
systemctl stop yueshu-explorer #停止服务
systemctl start yueshu-explorer #启动服务
```

也可以在安装目录下使用以下命令，手动启动或停止服务。

```bash
sudo ./scripts/start.sh #启动{{explorer.name}}服务
sudo ./scripts/stop.sh #停止{{explorer.name}}服务
sudo ./dag-ctrl/scripts/start.sh #启动 Dag Controller 服务
sudo ./dag-ctrl/scripts/stop.sh #停止 Dag Controller 服务
```

### 卸载

使用以下的命令卸载{{explorer.name}}。

```bash
sudo rpm -e yueshu-explorer-<version>.x86_64
```

## DEB 部署

### 安装

1. 下载 DEB 包。

2. 使用`sudo dpkg -i <package_name>`命令安装 DEB 包。

  例如，安装{{explorer.name}}需要运行以下命令，默认安装路径为`/usr/local/yueshu-explorer`：

  ```bash
  sudo dpkg -i yueshu-explorer-{{explorer.release}}.x86_64.deb
  ```
  
  !!! note

        使用 DEB 包安装{{explorer.name}}时不支持自定义安装路径。

3. 进入解压后的文件夹，在`config`目录内修改`app-config.yaml`文件，设置`LicenseManagerURL`的值为 LM 所在的主机 IP 和端口号`9119`，例如`192.168.8.100:9119`。

4. （可选）配置 Dag Controller。参见下文 **配置 Dag Controller** 部分。

5. 进入`yueshu-explorer`文件夹，执行以下命令启动服务。

   ```bash
   cd yueshu-explorer

   # 启动{{explorer.name}}。
   sudo ./lib/start.sh

   # （可选）启动 Dag Controller。
   sudo ./dag-ctrl/scripts/start.sh
   ```

### 查看服务状态

```bash
sudo systemctl status yueshu-explorer.service
```

### 停止服务

```bash
sudo systemctl stop yueshu-explorer.service
```

### 卸载

使用以下的命令卸载{{explorer.name}}。

```bash
sudo dpkg -r yueshu-explorer
```

## TAR 包部署

### 安装及部署

1. 根据需要下载 TAR 包，建议选择最新版本。

2. 使用 `tar -xvf` 解压 tar 包。

   ```bash
   tar -xvf yueshu-explorer-<version>.tar.gz
   ```

3. 进入解压后的文件夹，在`config`目录内修改`app-config.yaml`文件，设置`LicenseManagerURL`的值为 LM 所在的主机 IP 和端口号`9119`，例如`192.168.8.100:9119`。

4. （可选）配置 Dag Controller。参见下文 **配置 Dag Controller** 部分。

5. 进入`yueshu-explorer`文件夹，执行以下命令启动服务。

  ```bash
  cd yueshu-explorer

  # 启动{{explorer.name}}和 Dag Controller。
  sudo ./scripts/start.sh

  # 单独启动{{explorer.name}}。
  sudo nohup ./yueshu-explorer-server > explorer.log 2>&1 &
  ```

### 停止服务

用户可以采用`kill pid`的方式来关停服务：

```bash
kill $(lsof -t -i :7002)
```

## 配置 Dag Controller

Dag Controller 是一款任务编排调度工具，可以编排调度有向无环图（DAG）类型的作业，该作业由多个任务组成，且任务之间存在先后关系，组成一个有向无环图（DAG）。

Dag Controller 可以结合{{plato.name}}进行复杂的图计算。例如 Dag Controller 将算法调用请求发送给{{plato.name}}，{{plato.name}}保存结果至{{nebula.name}}或 HDFS，Dag Controller 再将上次的计算结果作为下一个算法任务的输入创建新的任务。

### 配置步骤

1. 配置 Dag Controller 机器 SSH 免密登录{{plato.name}}机器，以及{{plato.name}}集群内所有节点间的 SSH 相互免密登录。

  例如机器 A（Dag Controller）通过 SSH 免密登录至{{plato.name}}集群 B 中的机器 B-1。请在机器 A 上执行如下命令：

  ```
  //执行后按提示生成密钥，默认按回车即可。
  $ ssh-keygen -t rsa

  //将机器 A 的公钥文件安装到机器 B-1 对应的用户下，即可从机器 A 免密登录机器 B-1。
  $ ssh-copy-id -i ~/.ssh/id_rsa.pub <B_user>@<B_IP>
  ```

  按同样方法设置 A 免密登录机器 B-2、B-3 等，以及集群 B 内所有机器的互相免密登录。

2. 在 Dag Controller 机器上执行`eval $(ssh-agent)`启动 ssh-agent，然后执行`ssh-add ~/.ssh/id_rsa`将私钥交给 ssh-agent 管理。

  !!! note

        ssh-agent是密钥管理器，用来管理多个密钥，并为其他需要使用 SSH 密钥对的程序提供代理。

3. 配置`dag-ctrl-api.yaml`文件，路径为`dag-ctrl/etc/dag-ctrl-api.yaml`。配置{{plato.name}}机器的用户名及端口，如果有多台机器，请确保使用相同用户名和端口。

  ```yaml
  # 配置名称。
  Name: task-api

  Host: 0.0.0.0     # Dag Controller 服务的 IP。
  Port: 9002        # Dag Controller 服务的端口。
  Timeout: 60000    # HTTP 接口请求的超时时间。

  Log:              # 日志打印相关参数。详情参见 https://go-zero.dev/cn/docs/blog/tool/logx/
    Mode: file      # 保存模式。
    KeepDays: 7     # 保存时长。
    Path: logs      # 保存目录。
    Level: info     # 保存级别。
    Compress: false  # 是否压缩。

  # {{plato.name}}机器的用户名以及 SSH 端口。
  SSH:
   UserName: vesoft
   Port: 22  

  # 任务和作业的并行线程池大小。
  JobPool:
   Sleep: 3    # 3 秒检查一次有没有未执行的作业。
   Size: 3    # 同时可以执行 3 个作业。
  TaskPool:
   CheckStatusSleep: 1    # 1 秒检查一次任务状态。
   Size: 10    #同时可以执行 10 个任务。  
  Dag:
   VarDataListMaxSize: 100    # 如果读取 HDFS 的列，则限制为每次 100 条数据。  

  # 其他
  Debug:
    Enable: false  #是否开启 Debug。

  # {{explorer.name}}和 Dag Controller 通信的密钥。无需修改。
  RsaPriKey: |
    -----BEGIN RSA PRIVATE KEY-----
    MIICXAIBAAKBgQDcR0keIMmmV...
    -----END RSA PRIVATE KEY-----  
  RsaPubKey: |
    -----BEGIN RSA PUBLIC KEY-----
    MIGJAoGBANxHSR4gyaZX7uet7...
    -----END RSA PUBLIC KEY-----
  ```

4. 配置`tasks.yaml`文件，路径为`dag-ctrl/etc/tasks.yaml`。只需配置算法文件的具体路径（`exec_file`参数）。当前所有`exec_file`参数都配置为`run_algo.sh`文件的路径。

  !!! note

      - 算法文件在{{plato.name}}安装路径下的`scripts`目录内。
      - 如果有多台机器，请确保算法文件路径一致。
      - 其它参数是算法的执行参数，后续在[可视化工作流页面](../workflow/2.create-workflow.md)配置。

  ```bash
  exec_file: /home/xxx/yueshu-analytics/scripts/run_algo.sh
  ```

## 后续操作

[连接{{explorer.name}}](ex-ug-connect.md)