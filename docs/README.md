!!! danger "Nebula Graph 内核 2.x 已发布。 Nebula Graph 内核 1.x 与 2.x数据格式、通信协议、客户端等均双向不兼容，代码仓库不相同。2.x 请参考[新版本文档](https://docs.nebula-graph.com.cn/)。"

!!! note "Nebula Graph 内核 1.2.1 已发布，修复多处bug，通信协议、数据格式与 {{nebula.release}} 双向兼容。参考[新版本文档](https://docs.nebula-graph.com.cn/1.2.1/)"

!!! note "本文档更新时间{{ now().year }}-{{ now().month }}-{{ now().day }}, [GitHub commit](https://github.com/vesoft-inc/nebula-docs-cn/tree/v{{nebula.release}}) {{ git.short_commit }}."

# Nebula Graph {{nebula.release}} 是什么

**Nebula Graph** 是一款开源的图数据库，擅长处理千亿个顶点和万亿条边的超大规模数据集。

下图为 **Nebula Graph {{nebula.release}}** 产品架构图：

![image](https://docs-cdn.nebula-graph.com.cn/README/Nebula-Arch.png)

与其他图数据库产品相比，**Nebula Graph** 具有如下优势：

* 全对称分布式架构
* 存储与计算分离
* 水平可扩展性
* RAFT 协议下的数据强一致
* 类 SQL 查询语言
* 用户鉴权

## [快速使用](manual-CN/1.overview/2.quick-start/1.get-started.md)

## 常见问题

* [FAQ](manual-CN/1.overview/2.quick-start/2.FAQ.md)

## 支持的客户端(对应v1.x版本)

* [Go](https://github.com/vesoft-inc/nebula-go)
* [Python](https://github.com/vesoft-inc/nebula-python)
* [Java](https://github.com/vesoft-inc/nebula-java)
* [Nebula Graph Studio](https://github.com/vesoft-inc/nebula-web-docker)


