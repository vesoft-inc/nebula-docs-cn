# 索引的原理和写入优化

关于索引原理见这篇博文[分布式图数据库 Nebula Graph 的 Index 实践](https://nebula-graph.com.cn/posts/how-indexing-works-in-nebula-graph/).

在实践中，带索引的写入会比不带索引的写入明显慢（2-10）倍。以下是一些优化建议：

## 关于建模部分的优化

1. 索引的**唯一作用和目的**是通过属性查找点VID，也即只用于[LOOKUP 语句](../2.query-language/4.statement-syntax/2.data-query-and-manipulation-statements/lookup-syntax.md)。

2. 建模时避免使用索引——也即避免"只有通过属性才能找到点 VID” 的情况。如果不可避免，知晓使用索引会降低写入性能。

3. 索引**没有**任何查询加速的功能。

4. 索引使用(也即 `LOOKUP` 语句)中, 整数类型的等于比较(`==`)的读性能比较好, 大于(>)小于(<)不等于(!=)的读性能比较差。
字符串类型的等于比较(==)读性能比较好，**不允许**使用包含(contain), 前缀(prefix), 后缀(suffix), 模糊查询。其他规则见 `LOOKUP` 语句一节。

5. 如果建模时发现必须使用索引，只对于需要“通过属性查找点 VID”的**属性**建立索引。不要对其他属性增加索引，不会有任何正面作用，只会降低写性能。

## 关于工程部分的优化

1. 初次导入/初始化的时候，只构建 schema，**不要** `create index`。

2. 完成批量写入后，先运行 [`submit job compaction`](../3.build-develop-and-administration/5.storage-service-administration/compact.md),
等任务完成后,再运行 [`rebuild index`](../2.query-language/4.statement-syntax/1.data-definition-statements/index.md)。

3. 日常数据写入前，运行一次任务`submit job compaction`，可以提升后续的写入性能。

4. Spark 导入工具 (Exchange) 无法对索引写入做深度优化，其做法也是使用插入语句。
