Nebula Graph 支持多种类型客户端，包括 CLI 客户端、GUI 客户端和流行编程语言开发的客户端。本文将概述 Nebula Graph 客户端，并介绍如何使用原生 CLI 客户端 Nebula Console。

## Nebula Graph 客户端

用户可以使用已支持的 [客户端或者命令行工具](https://docs.nebula-graph.com.cn/{{nebula.release}}/20.appendix/6.eco-tool-version/) 来连接 Nebula Graph 数据库。<!--这里用外链。-->

<!-- TODO 云服务未能和 v{{ nebula.release }} 一起发布。
如果还没有 Nebula Graph 数据库，建议尝试云服务 [Nebula Graph Cloud Service](https://cloud.nebula-graph.com.cn/)。Nebula Graph Cloud Service 支持按需部署和快速搭建，并且使用 Nebula Graph Studio 作为默认客户端。
-->

## 使用 Nebula Console 连接 Nebula Graph

### 前提条件

- Nebula Graph 服务已 [启动](https://docs.nebula-graph.com.cn/{{nebula.release}}/4.deployment-and-installation/manage-service/)。<!--这里用外链。-->

- 运行 Nebula Console 的机器和运行 Nebula Graph 的服务器网络互通。

### 操作步骤

1. 在 [Nebula Console](https://github.com/vesoft-inc/nebula-console/releases "the nebula-console Releases page") 下载页面，确认需要的版本，单击** Assets**。

  !!! Note

        建议选择**最新**版本。

    ![Select a Nebula Graph version and click **Assets**](../reuse/console260.png "Click Assets to show the available Nebula Graph binary files")

2. 在** Assets **区域找到机器运行所需的二进制文件，下载文件到机器上。

    ![Click to download the package according to your hardware architecture](../reuse/assets260.png "Click the package name to download it")

3. （可选）为方便使用，重命名文件为`nebula-console`。

  !!! Note

        在 Windows 系统中，请重命名为`nebula-console.exe`。

4. 在运行 Nebula Console 的机器上执行如下命令，为用户授予 nebula-console 文件的执行权限。

  !!! Note

       Windows 系统请跳过此步骤。

    ```bash
    $ chmod 111 nebula-console
    ```

5. 在命令行界面中，切换工作目录至 nebula-console 文件所在目录。

6. 执行如下命令连接 Nebula Graph。

  - Linux 或 macOS

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
    | `-addr` | 设置要连接的 graphd 服务的 IP 地址。默认地址为 127.0.0.1。|
    | `-port` | 设置要连接的 graphd 服务的端口。默认端口为 9669。|
    | `-u/-user` | 设置 Nebula Graph 账号的用户名。未启用身份认证时，可以使用任意已存在的用户名（默认为`root`）。 |
    | `-p/-password` | 设置用户名对应的密码。未启用身份认证时，密码可以填写任意字符。 |
    | `-t/-timeout`  | 设置整数类型的连接超时时间。单位为秒，默认值为 120。 |
    | `-e/-eval` | 设置字符串类型的 nGQL 语句。连接成功后会执行一次该语句并返回结果，然后自动断开连接。 |
    | `-f/-file` | 设置存储 nGQL 语句的文件的路径。连接成功后会执行该文件内的 nGQL 语句并返回结果，执行完毕后自动断开连接。 |

用户可以使用`./nebula-console --help`命令获取所有参数的说明，也可以在 [项目仓库](https://github.com/vesoft-inc/nebula-console/tree/{{console.branch}}) 找到更多说明。

## Nebula Console 命令

Nebula Console 提供部分命令，可以导出 CSV 文件、导出 DOT 文件、导入测试数据集等。

!!! note

    命令不区分大小写。

### 导出 CSV 文件

CSV 文件用于保存命令执行的返回结果。

!!! note

    - CSV 文件保存在当前工作目录中，即 Linux 命令`pwd`显示的目录。

    - 命令只对下一条查询语句生效。

导出 CSV 文件命令如下：

```ngql
nebula> :CSV <file_name.csv>
```

### 导出 DOT 文件

DOT 文件同样用于保存命令执行的返回结果，其保存的结果信息和 CSV 文件不同。

!!! Note

    - DOT 文件保存在当前工作目录中，即 Linux 命令`pwd`显示的目录。

    - DOT 文件的内容可以复制后在 [GraphvizOnline](https://dreampuf.github.io/GraphvizOnline/) 网页中粘贴，生成可视化的执行计划图。

    - 命令只对下一条查询语句生效。

导出 DOT 文件命令如下：

```ngql
nebula> :dot <file_name.dot>
```

示例：

```ngql
nebula> :dot a.dot
nebula> PROFILE FORMAT="dot" GO FROM "player100" OVER follow;
```

### 加载测试数据集

测试数据集名称为 nba，详细 Schema 信息和数据信息请使用相关`SHOW`命令查看。

加载测试数据集命令如下：

```ngql
nebula> :play nba
```

### 重复执行

重复执行下一个命令 N 次，然后打印平均执行时间。命令如下：

```ngql
nebula> :repeat N
```

示例：

```ngql
nebula> :repeat 3
nebula> GO FROM "player100" OVER follow;
+-------------+
| follow._dst |
+-------------+
| "player101" |
| "player125" |
+-------------+
Got 2 rows (time spent 2602/3214 us)

Fri, 20 Aug 2021 06:36:05 UTC

+-------------+
| follow._dst |
+-------------+
| "player101" |
| "player125" |
+-------------+
Got 2 rows (time spent 583/849 us)

Fri, 20 Aug 2021 06:36:05 UTC

+-------------+
| follow._dst |
+-------------+
| "player101" |
| "player125" |
+-------------+
Got 2 rows (time spent 496/671 us)

Fri, 20 Aug 2021 06:36:05 UTC

Executed 3 times, (total time spent 3681/4734 us), (average time spent 1227/1578 us)
```

### 睡眠

睡眠 N 秒。常用于修改 Schema 的操作中，因为修改 Schema 是异步实现的，需要在下一个心跳周期才同步数据。命令如下：

```ngql
nebula> :sleep N
```

### 断开连接

用户可以使用`:EXIT`或者`:QUIT`从 Nebula Graph 断开连接。为方便使用，Nebula Console 支持使用不带冒号（:）的小写命令，例如`quit`。

示例：

```ngql
nebula> :QUIT

Bye root!
```

## 常见问题

### 如何通过源码安装 Nebula Console？

下载和编译 Nebula Console 的最新源码，请参见 [GitHub nebula console](https://github.com/vesoft-inc/nebula-console#build-nebula-graph-console) 页面的说明。
