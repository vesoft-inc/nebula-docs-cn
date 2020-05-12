# SHOW INDEXES 语法

```ngql
SHOW {TAG | EDGE} INDEXES
```

`SHOW INDEXES` 用于列出已创建完成的标签或边类型的索引信息。`SHOW INDEXES` 返回以下字段：索引 ID 和 索引名称。

例如：

```ngql
nebula> SHOW TAG INDEXES;
=============================
| Index ID | Index Name     |
=============================
| 6        | player_index_1 |
-----------------------------
| 7        | player_index_0 |
-----------------------------
```

如何创建索引请参考 [索引](../../1.data-definition-statements/index.md) 文档。
