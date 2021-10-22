# LIMIT

`LIMIT`子句限制输出结果的行数。

- 在原生nGQL中，必须使用管道符（|），可以忽略偏移量。

- 在openCypher方式中，不允许使用管道符，可以使用`SKIP`指明偏移量。

  !!! Note

        在原生nGQL或openCypher方式中使用`LIMIT`时，使用`ORDER BY`子句限制输出顺序非常重要，否则会输出一个不可预知的子集。

## 原生nGQL语法

在原生nGQL中，`LIMIT`的工作原理与`SQL`相同，必须和管道符一起使用。`LIMIT`子句接收一个或两个参数。参数的值必须是非负整数。

```ngql
YIELD <var>
[| LIMIT [<offset_value>,] <number_rows>];
```

|参数|说明|
|:--|:--|
|`var`|排序的列或计算结果。|
|`offset_value`|偏移量，即定义从哪一行开始返回。索引从`0`开始。默认值为`0`，表示从第一行开始返回。|
|`number_rows`|返回的总行数。|

### 示例

```ngql
# 从排序结果中返回第2行开始的3行数据。
nebula> GO FROM "player100" OVER follow REVERSELY \
        YIELD properties($$).name AS Friend, properties($$).age AS Age \
        | ORDER BY $-.Age, $-.Friend \
        | LIMIT 1, 3;
+-------------------+-----+
| Friend            | Age |
+-------------------+-----+
| "Danny Green"     | 31  |
+-------------------+-----+
| "Aron Baynes"     | 32  |
+-------------------+-----+
| "Marco Belinelli" | 32  |
+-------------------+-----+
```

## openCypher方式语法

```ngql
RETURN <var>
[SKIP <offset>]
[LIMIT <number_rows>];
```

|参数|说明|
|:--|:--|
|`var`|排序的列或计算结果。|
|`offset`|偏移量，即定义从哪一行开始返回。索引从`0`开始。默认值为`0`，表示从第一行开始返回。|
|`number_rows`|返回的总行数量。|

`offset`和`number_rows`可以使用表达式，但是表达式的结果必须是非负整数。

!!! Note

    两个整数组成的分数表达式会自动向下取整。例如`8/6`向下取整为1。

### 示例

```ngql
nebula> MATCH (v:player) RETURN v.name AS Name, v.age AS Age \
        ORDER BY Age LIMIT 5;
+-------------------------+-----+
| Name                    | Age |
+-------------------------+-----+
| "Luka Doncic"           | 20  |
+-------------------------+-----+
| "Ben Simmons"           | 22  |
+-------------------------+-----+
| "Kristaps Porzingis"    | 23  |
+-------------------------+-----+
| "Giannis Antetokounmpo" | 24  |
+-------------------------+-----+
| "Kyle Anderson"         | 25  |
+-------------------------+-----+

nebula> MATCH (v:player) RETURN v.name AS Name, v.age AS Age \
        ORDER BY Age LIMIT rand32(5);
+-------------------------+-----+
| Name                    | Age |
+-------------------------+-----+
| "Luka Doncic"           | 20  |
+-------------------------+-----+
| "Ben Simmons"           | 22  |
+-------------------------+-----+
| "Kristaps Porzingis"    | 23  |
+-------------------------+-----+
| "Giannis Antetokounmpo" | 24  |
+-------------------------+-----+
```

### SKIP示例

用户可以单独使用`SKIP <offset>`设置偏移量，后面不需要添加`LIMIT <number_rows>`。

```ngql
nebula> MATCH (v:player{name:"Tim Duncan"}) --> (v2) \
        RETURN v2.name AS Name, v2.age AS Age \
        ORDER BY Age DESC SKIP 1;
+-----------------+-----+
| Name            | Age |
+-----------------+-----+
| "Manu Ginobili" | 41  |
+-----------------+-----+
| "Tony Parker"   | 36  |
+-----------------+-----+

nebula> MATCH (v:player{name:"Tim Duncan"}) --> (v2) \
        RETURN v2.name AS Name, v2.age AS Age \
        ORDER BY Age DESC SKIP 1+1;
+---------------+-----+
| Name          | Age |
+---------------+-----+
| "Tony Parker" | 36  |
+---------------+-----+
```

用户也可以同时使用`SKIP <offset>`和`LIMIT <number_rows>`，返回中间的部分数据。

```ngql
nebula> MATCH (v:player{name:"Tim Duncan"}) --> (v2) \
        RETURN v2.name AS Name, v2.age AS Age \
        ORDER BY Age DESC SKIP 1 LIMIT 1;
+-----------------+-----+
| Name            | Age |
+-----------------+-----+
| "Manu Ginobili" | 41  |
+-----------------+-----+
```
<!--
## 性能提示

Nebula Graph {{ nebula.release }} 未实现 `LIMIT` 语句的存储层下推优化, 类似 `MATCH (n:T) RETURN n LIMIT 10` 语句或者 `LOOKUP on i_T | LIMIT 10` 语句会发生 graphd 资源占用过大的问题：一个 graphd 会从所有的 storaged 获取全部T类型的点，然后返回 10 个。如果全部数据量很大，graphd 此时通常会消耗大量内存，甚至 OOM。
-->
