# 使用限制

本文描述 Exchange 2.x 的一些使用限制。

## 版本兼容性

Nebula Exchange 版本（即 JAR 包版本）和 Nebula Graph 内核的版本对应关系如下。

|Exchange client 版本|Nebula Graph 版本|
|:---|:---|
|2.5-SNAPSHOT|nightly|
|{{exchange.release}}|2.6.0、{{nebula.release}}|
|2.5.1|2.5.0、2.5.1|
|2.5.0|2.5.0、2.5.1|
|2.1.0|2.0.0、2.0.1|
|2.0.1|2.0.0、2.0.1|
|2.0.0|2.0.0、2.0.1|

JAR 包有两种获取方式：[自行编译](../ex-ug-compile.md) 或者从 maven 仓库下载。

如果正在使用 Nebula Graph 1.x，请使用 [Nebula Exchange 1.x](https://github.com/vesoft-inc/nebula-java/tree/v1.0/tools "Click to go to GitHub")。

## 使用环境

Exchange 2.x 支持以下操作系统：

- CentOS 7
- macOS

## 软件依赖

为保证 Exchange 正常工作，请确认机器上已经安装如下软件：

- Apache Spark：2.4.x

- Java：1.8

- Scala：2.10.7、2.11.12 或 2.12.10

在以下使用场景，还需要部署 Hadoop Distributed File System (HDFS)：

- 迁移 HDFS 的数据
- 生成 SST 文件
