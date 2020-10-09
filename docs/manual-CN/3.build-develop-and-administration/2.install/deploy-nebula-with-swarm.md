# 使用 Docker Swarm 部署 Nebula Graph 集群

本文档介绍如何使用 Docker Swarm 部署 Nebula Graph 集群。

## 前提条件

安装 Nebula Graph 前确保所有机器已安装 Docker、Docker Compose、HAProxy 和 Keepalived。

机器准备：

| IP | 内存（Gb） | CPU（核数） |
| --- | --- | --- |
| 192.168.1.166 | 16 | 4 |
| 192.168.1.167 | 16 | 4 |
| 192.168.1.168 | 16 | 4 |

## 创建 Nebula Graph 集群

### 初始化 Docker Swarm 集群

在机器 `192.168.1.166` 上执行以下命令初始化 Docker Swarm 集群：

```bash
$ docker swarm init --advertise-addr 192.168.1.166
```

返回以下信息：

```bash
Swarm initialized: current node (dxn1zf6l61qsb1josjja83ngz) is now a manager.
To add a worker to this swarm, run the following command:
 docker swarm join \
 --token SWMTKN-1-49nj1cmql0jkz5s954yi3oex3nedyz0fb0xx14ie39trti4wxv-8vxv8rssmk743ojnwacrr2e7c \
 192.168.1.166:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
```

### 创建集群工作节点

根据 `docker swarm init` 命令的提示内容，创建 Swarm 集群的工作节点，在机器 `192.168.1.167`、`192.168.1.168` 上分别执行以下命令：

```bash
$ docker swarm join \
 --token SWMTKN-1-49nj1cmql0jkz5s954yi3oex3nedyz0fb0xx14ie39trti4wxv-8vxv8rssmk743ojnwacrr2e7c \
 192.168.1.166:2377
```

### 验证集群

```bash
$ docker node ls
```

返回以下信息：

```bash
ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
h0az2wzqetpwhl9ybu76yxaen *   KF2-DATA-166        Ready               Active              Reachable           18.06.1-ce
q6jripaolxsl7xqv3cmv5pxji     KF2-DATA-167        Ready               Active              Leader              18.06.1-ce
h1iql1uvm7123h3gon9so69dy     KF2-DATA-168        Ready               Active                                  18.06.1-ce
```

### 配置 Docker Stack

运行以下命令对 Docker Stack 进行配置：

```bash
vi docker-stack.yml
```

请根据您的 IP 地址与端口号进行配置。示例配置文件参考[这里](docker-stack.yml)。

在 `nebula.env` 文件中加入如下内容：

```yml
TZ=UTC
USER=root
```

### 启动集群

运行以下命令启动 Nebula Graph 集群：

```bash
$ docker stack deploy nebula -c docker-stack.yml
```

## 集群负载均衡及高可用配置

目前，Nebula Graph 的客户端（1.X）未提供负载均衡，而是随机选一个 `graphd` 服务连接。因此生产使用时需自行配置负载均衡和高可用。

### 负载均衡配置

HAProxy 使用 Docker Compose 配置。分别编辑以下三个文件：

在 `Dockerfile` 文件中加入以下内容：

```bash
FROM haproxy:1.7
COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg
EXPOSE 3640
```

在 `docker-compose.yml` 文件加入以下内容：

```yml
version: "3.2"
services:
  haproxy:
    container_name: haproxy
    build: .
    volumes:
      - ./haproxy.cfg:/usr/local/etc/haproxy/haproxy.cfg
    ports:
      - 3640:3640
    restart: always
    networks:
      - app_net
networks:
  app_net:
    external: true
```

在 `haproxy.cfg` 文件加入以下内容：

请根据您的 IP 地址与端口号进行配置。

```cfg
global
    daemon
    maxconn 30000
    log 127.0.0.1 local0 info
    log 127.0.0.1 local1 warning

defaults
    log-format %hr\ %ST\ %B\ %Ts
    log  global
    mode http
    option http-keep-alive
    timeout connect 5000ms
    timeout client 10000ms
    timeout server 50000ms
    timeout http-request 20000ms

# custom your own frontends && backends && listen conf
#CUSTOM

listen graphd-cluster
    bind *:3640
    mode tcp
    maxconn 300
    balance roundrobin
    server server1 192.168.1.166:3699 maxconn 300 check
    server server2 192.168.1.167:3699 maxconn 300 check
    server server3 192.168.1.168:3699 maxconn 300 check

listen stats
    bind *:1080
    stats refresh 30s
    stats uri /stats
```

### 启动 HAProxy

```bash
$ docker-compose up -d
```

### 高可用配置

在 `192.168.1.166`、`192.168.1.167` 和 `192.168.1.168` 进行以下操作：

安装 Keepalived：

```bash
apt-get update && apt-get upgrade && apt-get install keepalived -y
```

**注意**：配置 Keepalived 需预先准备好虚拟 IP，在以下配置中 `192.168.1.99` 即为虚拟 IP。

更改 Keepalived 配置文件 `/etc/keepalived/keepalived.conf`（三台机器中 priority 必须设置成不同值以确定优先级）。示例配置文件参考[这里](keepalived.conf)。

```text
# 启动keepalived
systemctl start keepalived
# 使keepalived开机自启
systemctl enable keeplived
# 重启keepalived
systemctl restart keepalived
```

## FAQ

### 如何实现离线部署

将镜像更改为私有镜像库即可实现离线部署。
