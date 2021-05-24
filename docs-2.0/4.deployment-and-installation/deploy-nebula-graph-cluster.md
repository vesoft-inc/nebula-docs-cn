# 部署Nebula Graph集群

Nebula Graph不提供官方的集群部署工具，需要手动部署，下文将介绍手动部署的简单流程。

## 前提条件

准备用于部署集群的服务器。

## 手动部署流程

### 安装Nebula Graph

在集群的每一台服务器上安装Nebula Graph。安装方式请参见：

- [使用RPM或DEB安装包安装Nebula Graph](2.compile-and-install-nebula-graph/2.install-nebula-graph-by-rpm-or-deb.md)

- [编译安装Nebula Graph](2.compile-and-install-nebula-graph/1.install-nebula-graph-by-compiling-the-source-code.md)

### 修改配置文件
修改每个服务器上的Nebula Graph配置文件。

Nebula Graph的所有配置文件均位于安装目录的`etc`目录内，包括`nebula-graphd.conf`、`nebula-metad.conf`和`nebula-storaged.conf`，用户可以只修改对应服务的配置文件。配置文件的详细说明请参见：

- [Meta服务配置](../5.configurations-and-logs/1.configurations/2.meta-config.md)

- [Graph服务配置](../5.configurations-and-logs/1.configurations/3.graph-config.md)

- [Storage服务配置](../5.configurations-and-logs/1.configurations/4.storage-config.md)

### 启动集群

启动各个服务器上的对应服务。启动Nebula Graph服务的命令如下：

```bash
sudo /usr/local/nebula/scripts/nebula.service start <metad|graphd|storaged|all>
```

`/usr/local/nebula`是Nebula Graph的默认安装路径，如果修改过安装路径，请使用实际路径。更多启停服务的内容，请参见[管理Nebula Graph服务](../2.quick-start/5.start-stop-service.md)。

### 检查集群

连接Graph服务，执行命令`SHOW HOSTS`检查集群状态。
