# OPTIONAL MATCH

!!! caution

    目前 `OPTIONAL MATCH` 为 Beta 功能，后续可能会有一定优化调整。

`OPTIONAL MATCH`通常与`MATCH`语句一起使用，作为`MATCH`语句的可选项去匹配命中的模式，如果没有命中对应的模式，对应的列返回`NULL`。

## openCypher 兼容性

本文操作仅适用于 nGQL 中的 openCypher 方式。

## 使用限制

`OPTIONAL MATCH`子句中暂不支持使用`WHERE`子句。

## 示例

`MATCH`语句中使用`OPTIONAL MATCH`的示例如下：

```ngql
nebula> MATCH (m)-[]->(n) WHERE id(m)=="player100" \
        OPTIONAL MATCH (n)-[]->(l) \
        RETURN id(m),id(n),id(l);
+-------------+-------------+-------------+
| id(m)       | id(n)       | id(l)       |
+-------------+-------------+-------------+
| "player100" | "team204"   | __NULL__    |
| "player100" | "player101" | "team204"   |
| "player100" | "player101" | "team215"   |
| "player100" | "player101" | "player100" |
| "player100" | "player101" | "player102" |
| "player100" | "player101" | "player125" |
| "player100" | "player125" | "team204"   |
| "player100" | "player125" | "player100" |
+-------------+-------------+-------------+
```

而使用多`MATCH`，不使用`OPTIONAL MATCH`时，会返回模式完全匹配的行。示例如下：

```ngql
nebula> MATCH (m)-[]->(n) WHERE id(m)=="player100" \
        MATCH (n)-[]->(l) \
        RETURN id(m),id(n),id(l);
+-------------+-------------+-------------+
| id(m)       | id(n)       | id(l)       |
+-------------+-------------+-------------+
| "player100" | "player101" | "team204"   |
| "player100" | "player101" | "team215"   |
| "player100" | "player101" | "player100" |
| "player100" | "player101" | "player102" |
| "player100" | "player101" | "player125" |
| "player100" | "player125" | "team204"   |
| "player100" | "player125" | "player100" |
+-------------+-------------+-------------+
```
