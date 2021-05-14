# 什么是Nebula Graph Studio

Nebula Graph Studio（简称Studio）是基于浏览器的可视化工具，可以管理Nebula Graph。Studio提供图形界面操作Schema、导入数据、探测图数据、执行nGQL（Nebula Graph Query Language）语句等。使用Studio，用户可以从零开始快速上手Nebula Graph。

## 部署方式

目前Studio 2.0.0仅支持用Docker部署，部署后可以连接Nebula Graph 2.0.0。详情请参见[部署Studio](../install-configure/st-ug-deploy.md)。

## 功能

Studio支持如下功能：

- 提供图形界面控制台，方便执行nGQL语句，并返回易于阅读的结果。

- 提供**Explore**函数，可以探索图数据，帮助挖掘数据之间的关系，提高数据分析效率。

## 场景

Studio适用于如下场景：

- 拥有一个数据集，希望以可视化的方式探索分析数据。用户可以使用Nebula Graph云服务、Docker Compose等方式部署Nebula Graph，然后通过Studio的图形界面探索分析数据。

- 已经部署Nebula Graph并导入数据集，希望使用图形界面执行nGQL语句或探索分析数据。

- 作为nGQL的初学者，希望通过简单的图形界面而不是命令行学习nGQL。
