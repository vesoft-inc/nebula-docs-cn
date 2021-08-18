Nebula Graph支持多种类型客户端，包括CLI客户端、GUI客户端和流行编程语言开发的客户端。本文将概述Nebula Graph客户端，并介绍如何使用原生CLI客户端Nebula Console。

## Nebula Graph客户端

用户可以使用已支持的[客户端或者命令行工具](../20.appendix/6.eco-tool-version.md)来连接Nebula Graph数据库。

<!-- TODO 云服务未能和 v{{ nebula.release }} 一起发布.
如果还没有Nebula Graph数据库，建议尝试云服务[Nebula Graph Cloud Service](https://cloud.nebula-graph.com.cn/)。Nebula Graph Cloud Service支持按需部署和快速搭建，并且使用Nebula Graph Studio作为默认客户端。
-->

## 使用Nebula Console连接Nebula Graph

### 前提条件

- Nebula Graph服务已启动。如何启动服务，请参见[启动和停止Nebula Graph服务](../2.quick-start/5.start-stop-service.md)。

- 运行Nebula Console的机器和运行Nebula Graph的服务器网络互通。

### 操作步骤

1. 在[Nebula Console](https://github.com/vesoft-inc/nebula-console/releases "the nebula-console Releases page")下载页面，确认需要的版本，单击**Assets**。

  !!! Note
    
        建议选择**最新**版本。

    ![Select a Nebula Graph version and click **Assets**](https://docs-cdn.nebula-graph.com.cn/docs-2.0/2.quick-start/nebula-console-releases-1.png "Click Assets to show the available Nebula Graph binary files")

2. 在**Assets**区域找到机器运行所需的二进制文件，下载文件到机器上。

    ![Click to download the package according to your hardware architecture](https://docs-cdn.nebula-graph.com.cn/docs-2.0/2.quick-start/nebula-console-releases-2-1.png "Click the package name to download it")

3. （可选）为方便使用，重命名文件为`nebula-console`。

  !!! Note

        在Windows系统中，请重命名为`nebula-console.exe`。

4. 在运行Nebula Console的机器上执行如下命令，为用户授予nebula-console文件的执行权限。

  !!! Note
    
       Windows系统请跳过此步骤。

    ```bash
    $ chmod 111 nebula-console
    ```

5. 在命令行界面中，切换工作目录至nebula-console文件所在目录。

6. 执行如下命令连接Nebula Graph。

    - Linux或macOS

    ```bash
    $ ./nebula-console -addr <ip> -port <port> -u <username> -p <password>
    [-t 120] [-e "nGQL_statement" | -f filename.nGQL]
    ```

    - Windows

    ```powershell
    > nebula-console.exe -addr <ip> -port <port> -u <username> -p <password>
    [-t 120] [-e "nGQL_statement" | -f filename.nGQL]
    ```

    参数说明如下。

    | 参数 | 说明 |
    | - | - |
    | `-h` | 显示帮助菜单。 |
    | `-addr` | 设置要连接的graphd服务的IP地址。默认地址为127.0.0.1。|
    | `-port` | 设置要连接的graphd服务的端口。默认端口为9669。|
    | `-u/-user` | 设置Nebula Graph账号的用户名。未启用身份认证时，可以使用任意已存在的用户名（默认为`root`）。 |
    | `-p/-password` | 设置用户名对应的密码。未启用身份认证时，密码可以填写任意字符。 |
    | `-t/-timeout`  | 设置整数类型的连接超时时间。单位为秒，默认值为120。 |
    | `-e/-eval` | 设置字符串类型的nGQL语句。连接成功后会执行一次该语句并返回结果，然后自动断开连接。 |
    | `-f/-file` | 设置存储nGQL语句的文件的路径。连接成功后会执行该文件内的nGQL语句并返回结果，执行完毕后自动断开连接。 |

用户可以使用`./nebula-console --help`命令获取所有参数的说明，也可以在[项目仓库](https://github.com/vesoft-inc/nebula-console/tree/v2.0.0-ga)找到更多说明。

## Nebula Console导出模式

导出模式开启时，Nebula Console会导出所有请求的结果到CSV格式文件中。关闭导出模式会停止导出。使用语法如下：

!!! Note

    - 命令不区分大小写。
    - CSV格式文件保存在当前工作目录中，即Linux命令`pwd`显示的目录。

- 开启导出模式

```ngql
nebula> :SET CSV <your_file.csv>
```

- 关闭导出模式

```ngql
nebula> :UNSET CSV
```

## 使用Nebula Console断开连接

用户可以使用`:EXIT`或者`:QUIT`从Nebula Graph断开连接。为方便使用，Nebula Console支持使用不带冒号（:）的小写命令，例如`quit`。

```ngql
nebula> :QUIT

Bye root!
```

## 常见问题

### 如何通过源码安装Nebula Console？

下载和编译Nebula Console的最新源码，请参见[GitHub nebula console](https://github.com/vesoft-inc/nebula-console#build-nebula-graph-console)页面的说明。
