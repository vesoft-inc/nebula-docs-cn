# WITH

`WITH`子句可以获取并处理查询前半部分的结果，并将处理结果作为输入传递给查询的后半部分。

## openCypher 兼容性

本文操作仅适用于 openCypher 方式。

!!! Note

    在原生 nGQL 中，有与`WITH`类似的[管道符](../5.operators/4.pipe.md)，但它们的工作方式不同。不要在 openCypher 方式中使用管道符，也不要在原生 nGQL 中使用`WITH`子句。

## 组成复合查询

使用`WITH`子句可以组合语句，将一条语句的输出转换为另一条语句的输入。

### 示例 1

1. 匹配一个路径。
2. 通过`nodes()`函数将路径上的所有点输出到一个列表。
3. 将列表拆分为行。
4. 去重后返回点的信息。

```ngql
nebula> MATCH p=(v:player{name:"Tim Duncan"})--() \
        WITH nodes(p) AS n \
        UNWIND n AS n1 \
        RETURN DISTINCT n1;
+-----------------------------------------------------------+
| n1                                                        |
+-----------------------------------------------------------+
| ("player100" :player{age: 42, name: "Tim Duncan"})        |
| ("player101" :player{age: 36, name: "Tony Parker"})       |
| ("team204" :team{name: "Spurs"})                          |
| ("player102" :player{age: 33, name: "LaMarcus Aldridge"}) |
| ("player125" :player{age: 41, name: "Manu Ginobili"})     |
| ("player104" :player{age: 32, name: "Marco Belinelli"})   |
| ("player144" :player{age: 47, name: "Shaquille O'Neal"})  |
| ("player105" :player{age: 31, name: "Danny Green"})       |
| ("player113" :player{age: 29, name: "Dejounte Murray"})   |
| ("player107" :player{age: 32, name: "Aron Baynes"})       |
| ("player109" :player{age: 34, name: "Tiago Splitter"})    |
| ("player108" :player{age: 36, name: "Boris Diaw"})        |
+-----------------------------------------------------------+
```

### 示例 2

1. 匹配点 ID 为`player100`的点。
2. 通过`labels()`函数将点的所有 Tag 输出到一个列表。
3. 将列表拆分为行。
4. 返回结果。

```ngql
nebula> MATCH (v) \
        WHERE id(v)=="player100" \
        WITH labels(v) AS tags_unf \
        UNWIND tags_unf AS tags_f \
        RETURN tags_f;
+----------+
| tags_f   |
+----------+
| "player" |
+----------+
```

## 过滤聚合查询

`WITH`可以在聚合查询中作为过滤器使用。

```ngql
nebula> MATCH (v:player)-->(v2:player) \
        WITH DISTINCT v2 AS v2, v2.player.age AS Age \
        ORDER BY Age \
        WHERE Age<25 \
        RETURN v2.player.name AS Name, Age;
+----------------------+-----+
| Name                 | Age |
+----------------------+-----+
| "Luka Doncic"        | 20  |
| "Ben Simmons"        | 22  |
| "Kristaps Porzingis" | 23  |
+----------------------+-----+
```

## collect() 之前处理输出

在`collect()`函数将输出结果转换为列表之前，可以使用`WITH`子句排序和限制输出结果。

```ngql
nebula> MATCH (v:player) \
        WITH v.player.name AS Name \
        ORDER BY Name DESC \
        LIMIT 3 \
        RETURN collect(Name);
+-----------------------------------------------+
| collect(Name)                                 |
+-----------------------------------------------+
| ["Yao Ming", "Vince Carter", "Tracy McGrady"] |
+-----------------------------------------------+
```

## 结合 RETURN 语句使用

在`WITH`子句中设置别名，并通过`RETURN`子句输出结果。

```ngql
nebula> WITH [1, 2, 3] AS list  RETURN 3 IN list AS r;
+------+
| r    |
+------+
| true |
+------+

nebula> WITH 4 AS one, 3 AS two RETURN one > two AS result;
+--------+
| result |
+--------+
| true   |
+--------+
```
