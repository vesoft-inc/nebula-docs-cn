# YIELD

`YIELD`定义nGQL查询的输出结果。

`YIELD`可以引导子句或语句：

- `YIELD`子句可以用于nGQL扩展语句中，例如`GO`、`FETCH`或`LOOKUP`。

- `YIELD`语句可以在独立查询或复合查询中使用。

## openCypher兼容性

本文操作仅适用于nGQL扩展。关于openCypher方式如何定义输出结果，请参见[`RETURN`](return.md)。

`YIELD`在nGQL和openCypher中有不同的函数：

- 在openCypher中，`YIELD`用于在`CALL[…YIELD]`子句中指定过程调用的输出。

  !!! Note

        nGQL暂不支持`CALL[…YIELD]`。

- 在nGQL中，`YIELD`和openCypher中的`RETURN`类似。

## YIELD子句

### 语法

```ngql
YIELD [DISTINCT] <col> [AS <alias>] [, <col> [AS <alias>] ...];
```

|参数|说明|
|:---|:---|
|`DISTINCT`|聚合输出结果，返回去重后的结果集。|
|`col`|要返回的字段。如果没有为字段设置别名，返回结果中的列名为`col`。|
|`alias`|`col`的别名。使用关键字`AS`进行设置，设置后返回结果中的列名为该别名。|

### 使用YIELD子句

- `GO`语句中使用`YIELD`：

    ```ngql
    nebula> GO FROM "player100" OVER follow \
            YIELD $$.player.name AS Friend, $$.player.age AS Age;
    +-----------------+-----+
    | Friend          | Age |
    +-----------------+-----+
    | "Tony Parker"   | 36  |
    +-----------------+-----+
    | "Manu Ginobili" | 41  |
    +-----------------+-----+
    ```

- `FETCH`语句中使用`YIELD`：

    ```ngql
    nebula> FETCH PROP ON player "player100" \
            YIELD player.name;
    +-------------+--------------+
    | VertexID    | player.name  |
    +-------------+--------------+
    | "player100" | "Tim Duncan" |
    +-------------+--------------+
    ```

- `LOOKUP`语句中使用`YIELD`：

    ```ngql
    nebula> LOOKUP ON player WHERE player.name == "Tony Parker" \
            YIELD player.name, player.age;
    =======================================
    | VertexID | player.name | player.age |
    =======================================
    | 101      | Tony Parker | 36         |
    ---------------------------------------
    ```

## YIELD语句

### 语法

```ngql
YIELD [DISTINCT] <col> [AS <alias>] [, <col> [AS <alias>] ...]
[WHERE <conditions>];
```

|参数|说明|
|-|-|
|`DISTINCT`|聚合输出结果，返回去重后的结果集。|
|`col`|要按返回的字段。如果没有为字段设置别名，返回结果中的列名为`col`。|
|`alias`|`col`的别名。使用关键字`AS`进行设置，设置后返回结果中的列名为该别名。|
|`conditions`|在`WHERE`子句中设置的过滤条件。详情请参见[`WHERE`](where.md)。|

### 复合查询中使用YIELD语句

在[复合查询](../4.variable-and-composite-queries/1.composite-queries.md)中，`YIELD`语句可以接收、过滤、修改之前语句的结果集，然后输出。

```ngql
# 查找player100关注的player，并计算他们的平均年龄。
nebula> GO FROM "player100" OVER follow \
        YIELD follow._dst AS ID \
        | FETCH PROP ON player $-.ID \
        YIELD player.age AS Age \
        | YIELD AVG($-.Age) as Avg_age, count(*)as Num_friends;
+---------+-------------+
| Avg_age | Num_friends |
+---------+-------------+
| 38.5    | 2           |
+---------+-------------+
```

```ngql
# 查找player101关注的player，返回degree大于90的player。
nebula> $var1 = GO FROM "player101" OVER follow \
        YIELD follow.degree AS Degree, follow._dst as ID; \
        YIELD $var1.ID AS ID WHERE $var1.Degree > 90;
+-------------+
| ID          |
+-------------+
| "player100" |
+-------------+
| "player125" |
+-------------+
```

### 独立使用YIELD语句

`YIELD`可以计算表达式并返回结果。

```ngql
nebula> YIELD rand32(1, 6);
+-------------+
| rand32(1,6) |
+-------------+
| 3           |
+-------------+

nebula> YIELD "Hel" + "\tlo" AS string1, ", World!" AS string2;
+-------------+------------+
| string1     | string2    |
+-------------+------------+
| "Hel    lo" | ", World!" |
+-------------+------------+

nebula> YIELD hash("Tim") % 100;
+-----------------+
| (hash(Tim)%100) |
+-----------------+
| 42              |
+-----------------+

nebula> YIELD \
      CASE 2+3 \
      WHEN 4 THEN 0 \
      WHEN 5 THEN 1 \
      ELSE -1 \
      END \
      AS result;
+--------+
| result |
+--------+
| 1      |
+--------+
```