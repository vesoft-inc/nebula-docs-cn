本文介绍如何使用原生命令行客户端 Nebula Console 连接 Nebula Graph。

Nebula Graph 支持多种类型的客户端，包括命令行客户端、可视化界面客户端和流行编程语言客户端。详情参见[客户端列表](../14.client/1.nebula-client.md)。

## 前提条件

- Nebula Graph 服务已[启动](https://docs.nebula-graph.com.cn/{{nebula.release}}/4.deployment-and-installation/manage-service/)。<!--必须用外链，因为这篇文档是复用的，用内部链接会出错。-->

- 运行 Nebula Console 的机器和运行 Nebula Graph 的服务器网络互通。

- Nebula Console 的版本兼容 Nebula Graph 的版本。

  !!! note
  
        版本相同的 Nebula Console 和 Nebula Graph 兼容程度最高，版本不同的 Nebula Console 连接 Nebula Graph 时，可能会有兼容问题，或者无法连接并报错`incompatible version between client and server`。

## 操作步骤

1. 进入 Nebula Graph 安装路径的 `bin` 目录中，找到 Nebula Console 的二进制文件。

  !!! note
        `bin` 目录中仅有 Linux 系统可用的二进制文件，Windows系统二进制文件的获取方式参见[获取 Nebula Console](../nebula-console.md)。

2. 执行如下命令连接 Nebula Graph。

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
  | `-h/-help` | 显示帮助菜单。 |
  | `-addr/-address` | 设置要连接的 Graph 服务的 IP 地址。默认地址为 127.0.0.1。如果 Nebula Graph 部署在 [Nebula Cloud](https://docs.nebula-graph.com.cn/2.6.2/nebula-cloud/1.what-is-cloud/) 上，需要创建 [Private Link](https://docs.nebula-graph.com.cn/2.6.2/nebula-cloud/5.solution/5.2.connection-configuration-and-use)，并设置该参数的值为专用终结点的 IP 地址。 |
  | `-P/-port` | 设置要连接的 Graph 服务的端口。默认端口为 9669。|
  | `-u/-user` | 设置 Nebula Graph 账号的用户名。未启用身份认证时，可以使用任意已存在的用户名（默认为`root`）。 |
  | `-p/-password` | 设置用户名对应的密码。未启用身份认证时，密码可以填写任意字符。 |
  | `-t/-timeout`  | 设置整数类型的连接超时时间。单位为秒，默认值为 120。 |
  | `-e/-eval` | 设置字符串类型的 nGQL 语句。连接成功后会执行一次该语句并返回结果，然后自动断开连接。 |
  | `-f/-file` | 设置存储 nGQL 语句的文件的路径。连接成功后会执行该文件内的 nGQL 语句并返回结果，执行完毕后自动断开连接。 |
  | `-enable_ssl` | 连接 Nebula Graph 时使用 SSL 加密。 |
  | `-ssl_root_ca_path` | 指定 CA 证书的存储路径。 |
  | `-ssl_cert_path` | 指定 CRT 证书的存储路径。 |
  | `-ssl_private_key_path` | 指定私钥文件的存储路径。 |

  更多参数参见[项目仓库](https://github.com/vesoft-inc/nebula-console/tree/{{console.branch}})。
