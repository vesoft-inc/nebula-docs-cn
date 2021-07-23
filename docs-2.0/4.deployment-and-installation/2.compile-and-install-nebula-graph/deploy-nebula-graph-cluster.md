# 使用RPM/DEB包部署Nebula Graph集群

Nebula Graph不提供官方的集群部署工具，用户可以使用RPM或DEB文件手动部署集群。本文提供了部署集群的示例。

## 部署方案

| 机器名称 |IP地址          | graphd进程数量   | storaged进程数量    |  metad进程数量   |
| :----- |:---------------|:------------- | :----------------- | :---------------- |
| A      | 192.168.10.111 |1               | 1                  | 1                |
| B      | 192.168.10.112 |1               | 1                  | 1                |
| C      | 192.168.10.113 |1               | 1                  | 1                |
| D      | 192.168.10.114 |1               | 1                  | -                |
| E      | 192.168.10.115 |1               | 1                  | -                |

## 前提条件

准备5台用于部署集群的机器。

## 手动部署流程

### 1.安装Nebula Graph

在集群的每一台服务器上都安装Nebula Graph，安装后暂不需要启动服务。安装方式请参见：

- [使用RPM或DEB包安装Nebula Graph](2.compile-and-install-nebula-graph/2.install-nebula-graph-by-rpm-or-deb.md)

- [使用源码安装Nebula Graph](2.compile-and-install-nebula-graph/1.install-nebula-graph-by-compiling-the-source-code.md)

### 2.修改配置文件

修改每个服务器上的Nebula Graph配置文件。

Nebula Graph的所有配置文件均位于安装目录的`etc`目录内，包括`nebula-graphd.conf`、`nebula-metad.conf`和`nebula-storaged.conf`，用户可以只修改所需服务的配置文件。各个机器需要修改的配置文件如下。

| 机器名称 |待修改配置文件    |
| :----- |:---------------|
| A      | `nebula-graphd.conf`、`nebula-storaged.conf`、`nebula-metad.conf`|
| B      | `nebula-graphd.conf`、`nebula-storaged.conf`、`nebula-metad.conf`|
| C      | `nebula-graphd.conf`、`nebula-storaged.conf`、`nebula-metad.conf` |
| D      | `nebula-graphd.conf`、`nebula-storaged.conf` |
| E      | `nebula-graphd.conf`、`nebula-storaged.conf` |

用户可以参考如下配置文件的内容，仅展示集群通信的部分设置，未展示的内容为默认设置，便于用户了解集群间各个服务器的关系。

!!! note

    主要修改的配置是`meta_server_addrs`，所有配置文件都需要填写所有Meta服务的IP地址和端口，同时需要修改`local_ip`为机器本身的联网IP地址。配置参数的详细说明请参见：

    - [Meta服务配置](../5.configurations-and-logs/1.configurations/2.meta-config.md)

    - [Graph服务配置](../5.configurations-and-logs/1.configurations/3.graph-config.md)

    - [Storage服务配置](../5.configurations-and-logs/1.configurations/4.storage-config.md)

- 机器A配置

  - `nebula-graphd.conf`

    ```bash
    ########## networking ##########
    # Comma separated Meta Server Addresses
    --meta_server_addrs=192.168.10.111:9559,192.168.10.112:9559,192.168.10.113:9559
    # Local IP used to identify the nebula-graphd process.
    # Change it to an address other than loopback if the service is distributed or
    # will be accessed remotely.
    --local_ip=192.168.10.111
    # Network device to listen on
    --listen_netdev=any
    # Port to listen on
    --port=9669
    ```

  - `nebula-storaged.conf`
  
    ```bash
    ########## networking ##########
    # Comma separated Meta server addresses
    --meta_server_addrs=192.168.10.111:9559,192.168.10.112:9559,192.168.10.113:9559
    # Local IP used to identify the nebula-storaged process.
    # Change it to an address other than loopback if the service is distributed or
    # will be accessed remotely.
    --local_ip=192.168.10.111
    # Storage daemon listening port
    --port=9779
    ```

  - `nebula-metad.conf`

    ```bash
    ########## networking ##########
    # Comma separated Meta Server addresses
    --meta_server_addrs=192.168.10.111:9559,192.168.10.112:9559,192.168.10.113:9559
    # Local IP used to identify the nebula-metad process.
    # Change it to an address other than loopback if the service is distributed or
    # will be accessed remotely.
    --local_ip=192.168.10.111
    # Meta daemon listening port
    --port=9559
    ```

- 机器B配置

  - `nebula-graphd.conf`

    ```bash
    ########## networking ##########
    # Comma separated Meta Server Addresses
    --meta_server_addrs=192.168.10.111:9559,192.168.10.112:9559,192.168.10.113:9559
    # Local IP used to identify the nebula-graphd process.
    # Change it to an address other than loopback if the service is distributed or
    # will be accessed remotely.
    --local_ip=192.168.10.112
    # Network device to listen on
    --listen_netdev=any
    # Port to listen on
    --port=9669
    ```

  - `nebula-storaged.conf`

    ```bash
    ########## networking ##########
    # Comma separated Meta server addresses
    --meta_server_addrs=192.168.10.111:9559,192.168.10.112:9559,192.168.10.113:9559
    # Local IP used to identify the nebula-storaged process.
    # Change it to an address other than loopback if the service is distributed or
    # will be accessed remotely.
    --local_ip=192.168.10.112
    # Storage daemon listening port
    --port=9779
    ```

  - `nebula-metad.conf`

    ```bash
    ########## networking ##########
    # Comma separated Meta Server addresses
    --meta_server_addrs=192.168.10.111:9559,192.168.10.112:9559,192.168.10.113:9559
    # Local IP used to identify the nebula-metad process.
    # Change it to an address other than loopback if the service is distributed or
    # will be accessed remotely.
    --local_ip=192.168.10.112
    # Meta daemon listening port
    --port=9559
    ```

- 机器C配置

  - `nebula-graphd.conf`

    ```bash
    ########## networking ##########
    # Comma separated Meta Server Addresses
    --meta_server_addrs=192.168.10.111:9559,192.168.10.112:9559,192.168.10.113:9559
    # Local IP used to identify the nebula-graphd process.
    # Change it to an address other than loopback if the service is distributed or
    # will be accessed remotely.
    --local_ip=192.168.10.113
    # Network device to listen on
    --listen_netdev=any
    # Port to listen on
    --port=9669
    ```

  - `nebula-storaged.conf`

    ```bash
    ########## networking ##########
    # Comma separated Meta server addresses
    --meta_server_addrs=192.168.10.111:9559,192.168.10.112:9559,192.168.10.113:9559
    # Local IP used to identify the nebula-storaged process.
    # Change it to an address other than loopback if the service is distributed or
    # will be accessed remotely.
    --local_ip=192.168.10.113
    # Storage daemon listening port
    --port=9779
    ```

  - `nebula-metad.conf`

    ```bash
    ########## networking ##########
    # Comma separated Meta Server addresses
    --meta_server_addrs=192.168.10.111:9559,192.168.10.112:9559,192.168.10.113:9559
    # Local IP used to identify the nebula-metad process.
    # Change it to an address other than loopback if the service is distributed or
    # will be accessed remotely.
    --local_ip=192.168.10.113
    # Meta daemon listening port
    --port=9559
    ```

- 机器D配置

  - `nebula-graphd.conf`

    ```bash
    ########## networking ##########
    # Comma separated Meta Server Addresses
    --meta_server_addrs=192.168.10.111:9559,192.168.10.112:9559,192.168.10.113:9559
    # Local IP used to identify the nebula-graphd process.
    # Change it to an address other than loopback if the service is distributed or
    # will be accessed remotely.
    --local_ip=192.168.10.114
    # Network device to listen on
    --listen_netdev=any
    # Port to listen on
    --port=9669
    ```

  - `nebula-storaged.conf`

    ```bash
    ########## networking ##########
    # Comma separated Meta server addresses
    --meta_server_addrs=192.168.10.111:9559,192.168.10.112:9559,192.168.10.113:9559
    # Local IP used to identify the nebula-storaged process.
    # Change it to an address other than loopback if the service is distributed or
    # will be accessed remotely.
    --local_ip=192.168.10.114
    # Storage daemon listening port
    --port=9779
    ```

- 机器E配置

  - `nebula-graphd.conf`

    ```bash
    ########## networking ##########
    # Comma separated Meta Server Addresses
    --meta_server_addrs=192.168.10.111:9559,192.168.10.112:9559,192.168.10.113:9559
    # Local IP used to identify the nebula-graphd process.
    # Change it to an address other than loopback if the service is distributed or
    # will be accessed remotely.
    --local_ip=192.168.10.115
    # Network device to listen on
    --listen_netdev=any
    # Port to listen on
    --port=9669
    ```

  - `nebula-storaged.conf`

    ```bash
    ########## networking ##########
    # Comma separated Meta server addresses
    --meta_server_addrs=192.168.10.111:9559,192.168.10.112:9559,192.168.10.113:9559
    # Local IP used to identify the nebula-storaged process.
    # Change it to an address other than loopback if the service is distributed or
    # will be accessed remotely.
    --local_ip=192.168.10.115
    # Storage daemon listening port
    --port=9779
    ```

### 3.启动集群

依次启动各个服务器上的对应进程。说明如下。

| 机器名称 |待启动的进程    | 
| :----- |:---------------|
| A      | graphd、storaged、metad|
| B      | graphd、storaged、metad|
| C      | graphd、storaged、metad |
| D      | graphd、storaged |
| E      | graphd、storaged |

启动Nebula Graph进程的命令如下：

```bash
sudo /usr/local/nebula/scripts/nebula.service start <metad|graphd|storaged|all>
```

!!! note

    - graphd、storaged和metad都启动时，可以用all代替。

    - `/usr/local/nebula`是Nebula Graph的默认安装路径，如果修改过安装路径，请使用实际路径。更多启停服务的内容，请参见[管理Nebula Graph服务](../2.quick-start/5.start-stop-service.md)。

### 4.检查集群

安装原生CLI客户端[Nebula Console](../2.quick-start/3.connect-to-nebula-graph.md#_1)，然后连接任何一个已启动graphd进程的机器，执行命令`SHOW HOSTS`检查集群状态。例如：

```bash
$ ./nebula-console --addr 192.168.10.111 --port 9669 -u root -p nebula

2021/05/25 01:41:19 [INFO] connection pool is initialized successfully
Welcome to Nebula Graph!

> SHOW HOSTS;
+------------------+------+----------+--------------+----------------------+------------------------+
| Host             | Port | Status   | Leader count | Leader distribution  | Partition distribution |
+------------------+------+----------+--------------+----------------------+------------------------+
| "192.168.10.111" | 9779 | "ONLINE" | 0            | "No valid partition" | "No valid partition"   |
+------------------+------+----------+--------------+----------------------+------------------------+
| "192.168.10.112" | 9779 | "ONLINE" | 0            | "No valid partition" | "No valid partition"   |
+------------------+------+----------+--------------+----------------------+------------------------+
| "192.168.10.113" | 9779 | "ONLINE" | 0            | "No valid partition" | "No valid partition"   |
+------------------+------+----------+--------------+----------------------+------------------------+
| "192.168.10.114" | 9779 | "ONLINE" | 0            | "No valid partition" | "No valid partition"   |
+------------------+------+----------+--------------+----------------------+------------------------+
| "192.168.10.115" | 9779 | "ONLINE" | 0            | "No valid partition" | "No valid partition"   |
+------------------+------+----------+--------------+----------------------+------------------------+
| "Total"          |      |          | 0            |                      |                        |
+------------------+------+----------+--------------+----------------------+------------------------+
```
