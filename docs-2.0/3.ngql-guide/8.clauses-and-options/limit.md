# LIMIT

`LIMIT`子句限制输出结果的行数。

## openCypher兼容性

- 在nGQL扩展中，必须使用管道符（|），可以忽略偏移量。

- 在openCypher方式中，不允许使用管道符，可以使用`Skip`指明偏移量。

>**说明**：在nGQL扩展或openCypher方式中使用`LIMIT`时，使用`ORDER BY`子句限制输出顺序非常重要，否则会输出一个不可预知的子集。

## nGQL扩展语法

在nGQL扩展中，`LIMIT`的工作原理与`SQL`相同，必须和管道符一起使用。`LIMIT`子句接收一个或两个参数。参数的值必须是非负整数。

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
        YIELD $$.player.name AS Friend, $$.player.age AS Age \
        | ORDER BY Age,Friend \
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

>**说明**：两个整数组成的分数表达式会自动向下取整。例如${8}\over{6}$向下取整为1。

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

您可以单独使用`SKIP <offset>`设置偏移量，后面不需要添加`LIMIT <number_rows>`。

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

您也可以同时使用`SKIP <offset>`和`LIMIT <number_rows>`，返回中间的部分数据。

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