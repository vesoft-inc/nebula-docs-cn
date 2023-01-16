# 使用限制

本文描述 NebulaGraph Spark Connector 的使用限制。

## NebulaGraph 版本

NebulaGraph Spark Connector 目前仅支持 NebulaGraph v1.0.1 和 v1.1.0，不支持 NebulaGraph v2.0。

## 软件依赖

NebulaGraph Spark Connector 默认依赖以下软件：

- Apache Spark&trade; 2.3.0 及更高版本
- Scala
- Java：1.8

## 功能限制

目前 NebulaGraph Spark Connector 在使用时有以下功能限制：

- Reader：目前无法用于读取 NebulaGraph 中属性为空的点和边数据。
- Writer：用于向 NebulaGraph 写入边数据时，作为起点与终点 VID 的数据必须同时为整数型或非数值型。
