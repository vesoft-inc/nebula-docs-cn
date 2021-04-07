# 使用限制

本文描述 Nebula Spark Connector 的使用限制。

## Nebula Graph 版本

Nebula Spark Connector 目前仅支持 Nebula Graph v1.0.1 和 v1.1.0，不支持 Nebula Graph v2.0。

## 软件依赖

Nebula Spark Connector 默认依赖以下软件：

- Apache Spark&trade; 2.3.0 及更高版本
- Scala
- Java：1.8

## 功能限制

目前 Nebula Spark Connector 在使用时有以下功能限制：

- Reader：目前无法用于读取 Nebula Graph 中属性为空的点和边数据。
- Writer：用于向 Nebula Graph 写入边数据时，作为起点与终点 VID 的数据必须同时为整数型或非数值型。
