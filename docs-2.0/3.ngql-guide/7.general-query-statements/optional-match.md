# OPTIONAL MATCH

`OPTIONAL MATCH`通常与`MATCH`语句一起使用，作为`MATCH`语句的可选项去匹配命中的模式，如果没有命中对应的模式，对应的列返回`NULL`。

## openCypher 兼容性

本文操作仅适用于 nGQL 中的 openCypher 方式。

## 示例

`MATCH`语句中使用`OPTIONAL MATCH`的示例如下：

```ngql
nebula> MATCH (m)-[]->(n) WHERE id(m)=="player100" \
        OPTIONAL MATCH (n)-[]->(l) WHERE id(n)=="player125" \
        RETURN id(m),id(n),id(l);
+-------------+-------------+-------------+
| id(m)       | id(n)       | id(l)       |
+-------------+-------------+-------------+
| "player100" | "team204"   | __NULL__    |
| "player100" | "player101" | __NULL__    |
| "player100" | "player125" | "team204"   |
| "player100" | "player125" | "player100" |
+-------------+-------------+-------------+
```

而使用多`MATCH`，不使用`OPTIONAL MATCH`时，会返回模式完全匹配的行。示例如下：

```ngql
nebula> MATCH (m)-[]->(n) WHERE id(m)=="player100" \
        MATCH (n)-[]->(l) WHERE id(n)=="player125" \
        RETURN id(m),id(n),id(l);
+-------------+-------------+-------------+
| id(m)       | id(n)       | id(l)       |
+-------------+-------------+-------------+
| "player100" | "player125" | "team204"   |
| "player100" | "player125" | "player100" |
+-------------+-------------+-------------+
```
