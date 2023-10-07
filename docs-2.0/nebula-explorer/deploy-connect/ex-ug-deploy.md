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

3. 进入解压后的文件夹，在`config`目录内修改`app-config.yaml`文件。设置`LicenseManagerURL`的值为 LM 所在的主机 IP 和端口号`9119`，例如`192.168.8.100:9119`。
   
    更多配置介绍参见文末**配置文件说明**部分。

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
   
    更多配置介绍参见文末**配置文件说明**部分。

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
   
    更多配置介绍参见文末**配置文件说明**部分。

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

## 配置文件说明

```yaml
Name: 图探索
Version: {{explorer.release}}
Database: 悦数
Host: 0.0.0.0  # 指定能访问{{explorer.name}}的地址。
Port: 7002  # 访问{{explorer.name}}的默认端口。

# 使用 SSL 加密访问或内联框架时，需要配置以下参数。当前仅支持自签名证书，方法可参考内联框架章节。
# CertFile: "./config/Explorer.crt"  # SSL 公钥证书的路径。
# KeyFile: "./config/Explorer.key" # SSL 密钥的路径。

MaxBytes: 1073741824 # Http 可接受请求的最大 ContentLength，默认为 1048576。取值范围：0 ~ 8388608。
Timeout: 30000 # 访问超时时间。

# {{explorer.name}}的部署模式，支持单实例和多实例。可选值为：single 和 multi。默认值为 single。
# 多实例模式下，本地的存储服务(数据导入)将被禁止，以保证实例之间的数据一致性。
# AppInstance: "multi" 
Log:  # {{explorer.name}}运行日志设置。详细配置说明参见 https://go-zero.dev/en/docs/tutorials/go-zero/configuration/log/
  Mode: file  # 日志保存方式。可选值为：console 和 file。console 表示服务日志会记录在 webserver.log里；file 表示服务日志会分别记录在 access.log、error.log、severe.log、slow.log 和 stat.log 里。
  Level: error # 日志输出级别。可选值为：debug、info、error 和 severe。
  KeepDays: 7  # 日志保留天数。
Env: "local"
Debug:  
  Enable: false # 是否开启 Debug 模式。
Auth:
  TokenName: "explorer_token" # 登录后的 token 名称。
  AccessSecret: "login_secret" # 登录后的 token 密钥。
  AccessExpire: 259200 # 登录后的 token 有效期，单位为秒。
File:
  UploadDir: "./data/upload/"  # 导入数据时的上传文件存储路径。
  TasksDir: "./data/tasks"  # 任务文件存储路径。包括导入任务、工作流任务等。
  TaskIdPath: "./data/taskId.data" # 任务 ID 存储路径。
DB:
  Enable: true
  LogLevel: 4  # 数据库运行日志级别。1、2、3、4 分别对应 Silent、ERROR、Warn、INFO。
  IgnoreRecordNotFoundError: false  
  AutoMigrate: true  # 是否自动创建数据库表。默认为 true。
  Type: "sqlite3"  # 后端使用的数据库类型。支持 mysql 和 sqlite3。
  Host: "127.0.0.1:3306"  # 数据库 IP 和端口。
  Name: "nebula"  # 数据库名称。
  User: "root"  # 数据库用户名。
  Password: "123456"  # 数据库密码。
  SqliteDbFilePath: "./data/tasks.db"   # 仅 sqlite3 需要填写该参数。数据库文件地址。
  MaxOpenConns: 30  # 连接池最大活跃连接数。
  MaxIdleConns: 10  # 连接池最大空闲连接数。
Analytics:
  Host: "http://127.0.0.1:9002"  # 工作流的 DAG 服务地址。
  # RPC_HDFS_PASSWORD: "passward" # HDFS RPC 服务的密码。
OAuth:
  Enable: false 
  ClientID: "10274xxxx-v2kn8oe6xxxxx.apps.googleusercontent.com" # OAuth 服务的 客户端 ID。
  ClientSecret: "GOCSPX-8Enxxxxx" # OAuth 服务的 客户端密钥。
  AuthURL: "https://accounts.google.com/o/oauth2/v2/auth" # OAuth 服务的 URL。
  TokenURL: "https://oauth2.googleapis.com/token" # 获取访问 token 的 URL。
  Scopes: "https://www.googleapis.com/auth/userinfo.email" # OAuth 服务的 scope。

  UserInfoURL: "https://www.googleapis.com/oauth2/v1/userinfo" # 获取用户信息的 URL。
  UsernameKey: "email" # 用户名字段。
  Organization: "vesoft"  # OAuth 供应商名称。
  TokenName: "oauth_token" # cookie 里的 token 名称。
  RedirectURL: "http://127.0.0.1:7002/login" # OAuth 服务的重定向 URL。
  AvatarKey: "picture" # 用户信息中头像的密钥。
IframeMode:
  Enable: false  # 是否开启内联框架模式。
  # Origins:     # 内联框架来源白名单。默认允许任何来源。
  #   - "http://192.168.8.8"
LicenseManagerURL: http://192.168.8.100:9119 # License Manager 所在的主机 IP，端口默认为9119。
CorsOrigins: [] # 允许发起跨域请求的域名列表。
```

## 后续操作

[连接{{explorer.name}}](ex-ug-connect.md)