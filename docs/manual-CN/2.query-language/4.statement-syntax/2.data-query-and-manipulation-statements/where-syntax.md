# WHERE 语法

`WHERE` 子句可以为查询返回的数据指定搜索条件。`WHERE` 子句语法如下：

```ngql
WHERE <expression> [ AND | OR <expression> ...])
```

目前，`WHERE` 语句适用于 `GO` 和 `LOOKUP` 语句。注意部分 `WHERE` 过滤条件尚未在 `LOOKUP` 语句中支持。详情参考 [LOOKUP 文档](lookup-syntax.md)。

通常，筛选条件是关于点、边的表达式的逻辑组合。

> 作为语法，逻辑与可用 `AND` 或 `&&` 表示，同理，逻辑或可用 `OR` 或 `||` 表示。

## 示例

```ngql
-- 边 follow 的 degree 属性大于 90。
nebula> GO FROM 100 OVER follow WHERE follow.degree > 90;
-- 返回以下值：
===============
| follow._dst |
===============
| 101         |
---------------

-- 找到与起点 player 104 的 age 值相等的点。
nebula> GO FROM 104 OVER follow WHERE $^.player.age == $$.player.age;
-- 返回以下值：
===============
| follow._dst |
===============
| 103         |
---------------

-- 多种逻辑组合。
nebula> GO FROM 100 OVER follow WHERE follow.degree > 90 OR $$.player.age != 33 AND $$.player.name != "Tony Parker";
-- 返回以下值：
===============
| follow._dst |
===============
| 101         |
---------------
| 106         |
---------------

--下面 WHERE 语句中的条件总是为 TRUE。
nebula> GO FROM 101 OVER follow WHERE 1 == 1 OR TRUE;
-- 返回以下值：
===============
| follow._dst |
===============
| 100         |
---------------
| 102         |
---------------
```

## 使用 WHERE 对边 rank 筛选

`WHERE` 子句支持对边 rank 进行筛选。例如：

```ngql
nebula> CREATE SPACE test;
nebula> USE test;
nebula> CREATE EDGE e1(p1 int);
nebula> CREATE TAG person(p1 int);
nebula> INSERT VERTEX person(p1) VALUES 1:(1);
nebula> INSERT VERTEX person(p1) VALUES 2:(2);
nebula> INSERT EDGE e1(p1) VALUES 1->2@0:(10);
nebula> INSERT EDGE e1(p1) VALUES 1->2@1:(11);
nebula> INSERT EDGE e1(p1) VALUES 1->2@2:(12);
nebula> INSERT EDGE e1(p1) VALUES 1->2@3:(13);
nebula> INSERT EDGE e1(p1) VALUES 1->2@4:(14);
nebula> INSERT EDGE e1(p1) VALUES 1->2@5:(15);
nebula> INSERT EDGE e1(p1) VALUES 1->2@6:(16);
nebula> GO FROM 1 OVER e1 WHERE e1._rank>2 YIELD e1._src, e1._dst, e1._rank AS Rank, e1.p1 | ORDER BY Rank DESC;
====================================
| e1._src | e1._dst | Rank | e1.p1 |
====================================
| 1       | 2       | 6    | 16    |
------------------------------------
| 1       | 2       | 5    | 15    |
------------------------------------
| 1       | 2       | 4    | 14    |
------------------------------------
| 1       | 2       | 3    | 13    |
------------------------------------
```
