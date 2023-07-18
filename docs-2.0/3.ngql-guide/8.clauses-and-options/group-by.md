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


## 隐式分组

在上述 nGQL 语句中明确写出`GROUP BY`并起到分组字段作用的用法称为`GROUP BY`显示用法；而在 openCypher 语句中`GROUP BY`的用法是隐式的，即在语句中不用写出`GROUP BY`也可起到分组字段的作用。nGQL 语句中显示地`GROUP BY`用法与 openCypher 语句中的隐式地`GROUP BY`用法相同，并且 nGQL 语句兼容 openCypher 的用法，即也支持隐式地使用`GROUP BY`。有关`GROUP BY`的隐式用法，请参见[how-to-make-group-by-in-a-cypher-query](https://stackoverflow.com/questions/52722671/how-to-make-group-by-in-a-cypher-query)。

例如：查询 34 岁以上的球员中完全重叠服役的区间。

```ngql
nebula> LOOKUP ON player WHERE player.age > 34 YIELD id(vertex) AS v | \
        GO FROM $-.v OVER serve YIELD serve.start_year AS start_year, serve.end_year AS end_year | \
        YIELD $-.start_year, $-.end_year, count(*) AS count | \
        ORDER BY $-.count DESC | LIMIT 5;
+---------------+-------------+-------+
| $-.start_year | $-.end_year | count |
+---------------+-------------+-------+
| 2018          | 2019        | 3     |
| 2007          | 2012        | 2     |
| 1998          | 2004        | 2     |
| 2017          | 2018        | 2     |
| 2010          | 2011        | 2     |
+---------------+-------------+-------+
```