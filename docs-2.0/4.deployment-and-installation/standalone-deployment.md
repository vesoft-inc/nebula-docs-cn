# 存算合并版 Nebula Graph

存算合并版 Nebula Graph 将存储服务（Meta 和 Storage）和计算服务（Graph）合并至一个进程，用于部署在单台机器上。本文介绍存算合并版 Nebula Graph 的使用场景、安装步骤等。

!!! danger

    存算合并版 Nebula Graph 不用于生产环境。

## 背景信息

传统的 Nebula Graph 架构由 3 个服务构成，每个服务都有可执行的二进制文件和对应的进程，进程之间通过 RPC 协议进行调用。而在存算合并版 Nebula Graph 中，Nebula Graph 中 3 个服务对应的 3 个进程被合为 1 个进程。

关于 Nebula Graph 的更多信息，参见[架构总览](../1.introduction/3.nebula-graph-architecture/1.architecture-overview.md)。

## 使用场景

数据规模小，可用性需求不大的场景。例如，受限于机器数量的测试环境或者仅用于验证功能的场景。

## 使用限制

- 仅支持单副本服务。
- 不支持高可用和可靠性。

## 环境准备

关于安装存算合并版 Nebula Graph 所需的环境，参见[编译 Nebula Graph 源码要求](1.resource-preparations.md)。

## 安装步骤

目前仅支持使用源码安装存算合并版 Nebula Graph。其安装步骤与多进程的 Nebula Graph 步骤类似，用户只需在**使用 CMake 生成 makefile 文件**步骤的命令中添加`-DENABLE_STANDALONE_VERSION=on`。示例如下：

```bash
cmake -DCMAKE_INSTALL_PREFIX=/usr/local/nebula -DENABLE_TESTING=OFF -DENABLE_STANDALONE_VERSION=on -DCMAKE_BUILD_TYPE=Release ..
``` 

有关具体的安装步骤，参见[使用源码安装](2.compile-and-install-nebula-graph/1.install-nebula-graph-by-compiling-the-source-code.md)。

用户完成存算合并版 Nebula Graph 后，可以参见[连接服务](connect-to-nebula-graph.md)连接 Nebula Graph。

## 配置文件

存算合并版 Nebula Graph 的配置文件的路径默认为`/usr/local/nebula/etc`。

用户可执行`sudo cat nebula-standalone.conf.default`查看配置文件内容。配置文件参数和描述和多进程的 Nebula Graph 大体一致，除以下参数外：

| 参数             | 预设值      | 说明                  |
| ---------------- | ----------- | --------------------- |
| `meta_port`      | `9559`      | Meta 服务的端口号。    |
| `storage_port`   | `9779`      | Storage 服务的端口号。 |
| `meta_data_path` | `data/meta` | Meta 数据存储路径。    |

用户可以执行命令查看配置项列表与说明。具体操作，请参见[配置管理](../5.configurations-and-logs/1.configurations/1.configurations.md)。