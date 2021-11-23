# 索引介绍

Nebula Graph 支持两种类型索引：原生索引和全文索引。

## 原生索引

原生索引可以基于指定的属性查询数据，有如下特点：

- 包括 Tag 索引和 Edge type 索引。

- 必须手动重建索引（`REBUILD INDEX`）。

- 支持创建同一个 Tag 或 Edge type 的多个属性的索引（复合索引），但是不能跨 Tag 或 Edge type。

### 原生索引操作

- [CREATE INDEX](1.create-native-index.md)

- [SHOW CREATE INDEX](2.1.show-create-index.md)

- [SHOW INDEXES](2.show-native-indexes.md)

- [DESCRIBE INDEX](3.describe-native-index.md)

- [REBUILD INDEX](4.rebuild-native-index.md)

- [SHOW INDEX STATUS](5.show-native-index-status.md)

- [DROP INDEX](6.drop-native-index.md)

- [LOOKUP](../7.general-query-statements/5.lookup.md)

- [MATCH](../7.general-query-statements/2.match.md)

## 全文索引

全文索引用于对字符串属性进行前缀搜索、通配符搜索、正则表达式搜索和模糊搜索，有如下特点：

- 只允许创建一个属性的索引。

- 只能创建指定长度（不超过 256 字节）字符串的索引。

- 不支持逻辑操作，例如`AND`、`OR`、`NOT`。

!!! Note

    如果需要进行整个字符串的匹配，请使用原生索引。

### 全文索引操作

在对全文索引执行任何操作之前，请确保已经部署全文索引。详情请参见 [部署全文索引](../../4.deployment-and-installation/6.deploy-text-based-index/2.deploy-es.md) 和 [部署 listener](../../4.deployment-and-installation/6.deploy-text-based-index/3.deploy-listener.md)。

部署完成后，Elasticsearch 集群上会自动创建全文索引。不支持重建或修改全文索引。如果需要删除全文索引，请在 Elasticsearch 集群上手动删除。

使用全文索引请参见 [使用全文索引查询](../15.full-text-index-statements/1.search-with-text-based-index.md)。

## NULL 值说明

不支持对值为 NULL 的属性创建索引。

## 范围查询

原生索引除了可以查询单个结果之外，还可以执行范围查询。当前仅支持对数字、日期和时间类型的属性进行范围查询。
