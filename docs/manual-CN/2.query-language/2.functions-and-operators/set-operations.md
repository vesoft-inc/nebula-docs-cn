# 集合操作（`UNION`，`INTERSECT`， `MINUS`）

您可以使用集合运算符 `UNION`、`UNION ALL`、`INTERSECT` 和 `MINUS` 进行多个组合查询。所有集合运算符具有相同的优先级。如果 nGQL 语句包含多个集合运算符，则 **Nebula Graph** 将对其进行从左到右处理，除非使用括号明确指定了顺序。

复合查询中，`GO` 语句返回的结果必须列数相同，且数据类型相同（比如均为数字类型或字符类型）。

## UNION，UNION DISTINCT，UNION ALL

`UNION DISTINCT`（简称 `UNION`）返回数据集 A 和 B 的并集（不包含重复元素）。

`UNION ALL` 返回数据集 A 和 B 的并集（包含重复元素）。`UNION` 语法为

```ngql
<left> UNION [DISTINCT | ALL] <right> [ UNION [DISTINCT | ALL] <right> ...]
```

`<left>` 和 `<right>` 必须列数相同，且数据类型相同。如果数据类型不同，将按照[类型转换](../1.data-types/type-conversion.md)进行转换。

### 示例

```ngql
nebula> GO FROM 1 OVER e1 \
        UNION \
        GO FROM 2 OVER e1;
```

以上语句返回点 `1` 和 `2`（沿边 `e1`）关联的唯一的点。

```ngql
nebula> GO FROM 1 OVER e1 \
        UNION ALL\
        GO FROM 2 OVER e1;
```

以上语句返回点 `1` 和 `2` 关联的所有点，其中存在重复点。

`UNION` 亦可与 `YIELD` 同时使用，例如以下语句：

```ngql
nebula> GO FROM 1 OVER e1 YIELD e1._dst AS id, e1.prop1 AS col_1, $$.tag.prop2 AS col_2; -- query 1
=======================
| id  | col_1| col_2  |
=======================
| 104 |   1  |    2   |    -- line 1
-----------------------
| 215 |   4  |    3   |    -- line 3
-----------------------

nebula> GO FROM 2,3 OVER e1 YIELD e1._dst AS id, e1.prop1 AS col_1, $$.tag.prop2 AS col_2;  -- query 2
======================
| id  | col_1| col_2 |
======================
| 104 |   1  |    2  |    -- line 1
----------------------
| 104 |   2  |    2  |    -- line 2
----------------------
```

```ngql
nebula> GO FROM 1 OVER e1 YIELD e1._dst AS id, e1.prop1 AS col_1, $$.tag.prop2 AS col_2   \
        UNION /* DISTINCT */     \
        GO FROM 2,3 OVER e1 YIELD e1._dst AS id, e1.prop1 AS col_1, $$.tag.prop2 AS col_2;
```

以上语句返回

```ngql
=======================
| id  | col_1| col_2  |    -- UNION or UNION DISTINCT. The column names come from query 1
=======================
| 104 |  1   |    2   |    -- line 1
-----------------------
| 104 |  2   |    2   |    -- line 2
-----------------------
| 215 |  4   |    3   |    -- line 3
-----------------------
```

请注意第一行与第二行返回相同 id 的点，但是返回的值不同。`DISTINCT` 检查返回结果中的重复值。所以第一行与第二行的返回结果不同。
`UNION ALL` 返回结果为

```ngql
nebula> GO FROM 1 OVER e1 YIELD e1._dst AS id, e1.prop1 AS col_1, $$.tag.prop2 AS col_2   \
        UNION ALL   \
        GO FROM 2,3 OVER e1 YIELD e1._dst AS id, e1.prop1 AS col_1, $$.tag.prop2 AS col_2;

======================
| id  | col_1| col_2 |    -- UNION ALL
======================
| 104 |   1  |   2   |    -- line 1
----------------------
| 104 |   1  |   2   |    -- line 1
----------------------
| 104 |   2  |   2   |    -- line 2
----------------------
| 215 |   4  |   3   |    -- line 3
----------------------
```

## INTERSECT

`INTERSECT` 返回集合 A 和 B 的交集（A ⋂ B）。

```ngql
<left> INTERSECT <right>
```

与 `UNION` 类似， `<left>` 和 `<right>` 必须列数相同，且数据类型相同。
此外，只返回 `<left>` 右 `<right>` 相同的行。例如：

```ngql
nebula> GO FROM 1 OVER e1 YIELD e1._dst AS id, e1.prop1 AS col_1, $$.tag.prop2 AS col_2
INTERSECT
GO FROM 2,3 OVER e1 YIELD e1._dst AS id, e1.prop1 AS col_1, $$.tag.prop2 AS col_2;
```

返回

```ngql
=======================
| id  | col_1 | col_2 |
=======================
| 104 |   1   |    2  |    -- line 1
-----------------------
```

## MINUS

返回 A - B 数据的差集，此处请注意运算顺序。例如：

```ngql
nebula> GO FROM 1 OVER e1 YIELD e1._dst AS id, e1.prop1 AS col_1, $$.tag.prop2 AS col_2
MINUS
GO FROM 2,3 OVER e1 YIELD e1._dst AS id, e1.prop1 AS col_1, $$.tag.prop2 AS col_2;
```

返回

```ngql
========================
| id  | col_1 | col_2  |
========================
| 215 |   4   |    3   |     -- line 3
------------------------
```

如果更改 `MINUS` 顺序

```ngql
nebula> GO FROM 2,3 OVER e1 YIELD e1._dst AS id, e1.prop1 AS col_1, $$.tag.prop2 AS col_2
MINUS
GO FROM 1 OVER e1 YIELD e1._dst AS id, e1.prop1 AS col_1, $$.tag.prop2 AS col_2;
```

则返回

```ngql
=======================
| id  | col_1 | col_2 |    -- column named from query 2
=======================
| 104 |    2  |    2  |    -- line 2
-----------------------
```

## 集合操作和管道的优先级

请注意当一条查询同时包含管道 `|` 和集合操作时，管道的优先级高于集合操作。管道用法请参考[管道文档](../3.language-structure/pipe-syntax.md)。语句 `GO FROM 1 UNION GO FROM 2 | GO FROM 3` 等价于语句 `GO FROM 1 UNION (GO FROM 2 | GO FROM 3)`。

例如：

```ngql
nebula> GO FROM 100 OVER follow YIELD follow._dst AS play_dst  \
        UNION \
        GO FROM 200 OVER serve REVERSELY YIELD serve._dst AS play_dst \
        | GO FROM $-.play_dst OVER follow YIELD follow._dst AS play_dst;
```

![image](https://user-images.githubusercontent.com/42762957/84130415-d46c8a00-aa75-11ea-8a29-b8bef5e1d55f.png)

红色框内的语句先执行，然后再执行绿色框内的语句。

```ngql
nebula> (GO FROM 100 OVER follow YIELD follow._dst AS play_dst  \
        UNION \
        GO FROM 200 OVER serve REVERSELY YIELD serve._dst AS play_dst) \
        | GO FROM $-.play_dst OVER follow YIELD follow._dst AS play_dst;
```

以上语句中，括号改变了执行的优先级，括号内的语句先执行。
