# GROUP BY

`GROUP BY`子句可以用于聚合数据。

## openCypher 兼容性

本文操作仅适用于原生 nGQL。

用户也可以使用 openCypher 方式的 [count()](../6.functions-and-expressions/15.aggregating.md) 函数聚合数据。

```ngql
nebula>  MATCH (v:player)<-[:follow]-(:player) RETURN v.player.name AS Name, count(*) as cnt ORDER BY cnt DESC;
+----------------------+-----+
| Name                 | cnt |
+----------------------+-----+
| "Tim Duncan"         | 10  |
| "LeBron James"       | 6   |
| "Tony Parker"        | 5   |
| "Chris Paul"         | 4   |
| "Manu Ginobili"      | 4   |
+----------------------+-----+
...
```

## 语法

`GROUP BY`子句可以聚合相同值的行，然后进行计数、排序和计算等操作。

`GROUP BY`子句可以在管道符（|）之后和`YIELD`子句之前使用。

```ngql
| GROUP BY <var> YIELD <var>, <aggregation_function(var)>
```
`aggregation_function()`函数支持`avg()`、`sum()`、`max()`、`min()`、`count()`、`collect()`、`std()`。

!!! note

    nGQL 语法同时兼容 openCypher 语法中 `GROUP BY` 的隐式用法。即当涉及聚合函数的时候，默认隐式使用 `GROUP BY`；如果不写出 `GROUP BY` 关键词，没有聚合函数的 YIELD 列也是被隐式地 `GROUP BY`。例如：查询 34 岁以上的球员中完全重叠服役的区间。

    ```ngql
    nebula> LOOKUP ON player WHERE player.age > 34 YIELD id(vertex) AS v |
            GO FROM $-.v OVER serve YIELD serve.start_year AS start_year, serve.end_year AS end_year | 
            YIELD $-.start_year, $-.end_year, count(*) AS count | ORDER BY $-.count DESC | LIMIT 5
    +---------------+-------------+-------+
    | $-.start_year | $-.end_year | count |
    +---------------+-------------+-------+
    | 2018          | 2019        | 3     |
    | 1998          | 2004        | 2     |
    | 2012          | 2013        | 2     |
    | 2007          | 2012        | 2     |
    | 2010          | 2011        | 2     |
    +---------------+-------------+-------+ 
    ```

## 示例

```ngql
# 查找所有连接到 player100 的点，并根据他们的姓名进行分组，返回姓名的出现次数。
nebula> GO FROM "player100" OVER follow BIDIRECT \
        YIELD properties($$).name as Name \
        | GROUP BY $-.Name \
        YIELD $-.Name as Player, count(*) AS Name_Count;
+---------------------+------------+
| Player              | Name_Count |
+---------------------+------------+
| "Shaquille O'Neal"  | 1          |
| "Tiago Splitter"    | 1          |
| "Manu Ginobili"     | 2          |
| "Boris Diaw"        | 1          |
| "LaMarcus Aldridge" | 1          |
| "Tony Parker"       | 2          |
| "Marco Belinelli"   | 1          |
| "Dejounte Murray"   | 1          |
| "Danny Green"       | 1          |
| "Aron Baynes"       | 1          |
+---------------------+------------+
```

## 用函数进行分组和计算

```ngql
# 查找所有连接到 player100 的点，并根据起始点进行分组，返回 degree 的总和。
nebula> GO FROM "player100" OVER follow \
        YIELD src(edge) AS player, properties(edge).degree AS degree \
        | GROUP BY $-.player \
        YIELD sum($-.degree);
+----------------+
| sum($-.degree) |
+----------------+
| 190            |
+----------------+
```

`sum()`函数详情请参见[内置数学函数](../6.functions-and-expressions/1.math.md)。
