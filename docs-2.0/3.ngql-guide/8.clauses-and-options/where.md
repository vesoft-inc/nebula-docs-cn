# WHERE

`WHERE`子句可以根据条件过滤输出结果。

`WHERE`子句通常用于如下查询：

- nGQL扩展，例如`GO`和`LOOKUP`语句。

- openCypher方式，例如`MATCH`和`WITH`语句。

## openCypher兼容性

- 不支持在模式中使用`WHERE`子句（TODO: planning），例如`WHERE (v)-->(v2)`。

- [过滤rank](#rank)是原生nGQL功能。只支持在nGQL扩展的语句（例如`GO`和`LOOKUP`）中使用，因为openCypher中没有rank的概念。

## 基础用法

### 用布尔运算符定义条件

在`WHERE`子句中使用布尔运算符`NOT`、`AND`、`OR`和`XOR`定义条件。关于运算符的优先级，请参见[运算符优先级](../5.operators/9.precedence.md)。

```ngql
nebula> MATCH (v:player) \
        WHERE v.name == "Tim Duncan" \
        XOR (v.age < 30 AND v.name == "Yao Ming") \
        OR NOT (v.name == "Yao Ming" OR v.name == "Tim Duncan") \
        RETURN v.name, v.age;
+-------------------------+-------+
| v.name                  | v.age |
+-------------------------+-------+
| "Marco Belinelli"       | 32    |
+-------------------------+-------+
| "Aron Baynes"           | 32    |
+-------------------------+-------+
| "LeBron James"          | 34    |
+-------------------------+-------+
| "James Harden"          | 29    |
+-------------------------+-------+
| "Manu Ginobili"         | 41    |
+-------------------------+-------+
...
```

```ngql
nebula> GO FROM "player100" \
        OVER follow \
        WHERE follow.degree > 90 \
        OR $$.player.age != 33 \
        AND $$.player.name != "Tony Parker";
+-------------+
| follow._dst |
+-------------+
| "player101" |
+-------------+
| "player125" |
+-------------+
```

### 过滤属性

在`WHERE`子句中使用点或边的属性定义条件。

- 过滤点属性：

    ```ngql
    nebula> MATCH (v:player)-[e]->(v2) \
            WHERE v2.age < 25 \
            RETURN v2.name, v2.age;
    +----------------------+--------+
    | v2.name              | v2.age |
    +----------------------+--------+
    | "Luka Doncic"        | 20     |
    +----------------------+--------+
    | "Kristaps Porzingis" | 23     |
    +----------------------+--------+
    | "Ben Simmons"        | 22     |
    +----------------------+--------+
    ```

    ```ngql
    nebula> GO FROM "player100" \
            OVER follow \
            WHERE $^.player.age >= 42;
    +-------------+
    | follow._dst |
    +-------------+
    | "player101" |
    +-------------+
    | "player125" |
    +-------------+
    ```

- 过滤边属性：

    ```ngql
    nebula> MATCH (v:player)-[e]->() \
            WHERE e.start_year < 2000 \
            RETURN DISTINCT v.name, v.age;
    +--------------------+-------+
    | v.name             | v.age |
    +--------------------+-------+
    | "Shaquille O'Neal" | 47    |
    +--------------------+-------+
    | "Steve Nash"       | 45    |
    +--------------------+-------+
    | "Ray Allen"        | 43    |
    +--------------------+-------+
    | "Grant Hill"       | 46    |
    +--------------------+-------+
    | "Tony Parker"      | 36    |
    +--------------------+-------+
    ...
    ```

    ```ngql
    nebula> GO FROM "player100" \
            OVER follow \
            WHERE follow.degree > 90;
    +-------------+
    | follow._dst |
    +-------------+
    | "player101" |
    +-------------+
    | "player125" |
    +-------------+
    ```

### 过滤动态计算属性

```ngql
nebula> MATCH (v:player) \
        WHERE v[toLower("AGE")] < 21 \
        RETURN v.name, v.age;
+---------------+-------+
| v.name        | v.age |
+---------------+-------+
| "Luka Doncic" | 20    |
+---------------+-------+
```

### 过滤现存属性

```ngql
nebula> MATCH (v:player) \
        WHERE exists(v.age) \
        RETURN v.name, v.age;
+-------------------------+-------+
| v.name                  | v.age |
+-------------------------+-------+
| "Boris Diaw"            | 36    |
+-------------------------+-------+
| "DeAndre Jordan"        | 30    |
+-------------------------+-------+
```

### 过滤rank

在nGQL中，如果多个边拥有相同的起始点、目的点和属性，则它们的唯一区别是rank值。在`WHERE`子句中可以使用rank过滤边。

```ngql
# 创建测试数据。
nebula> CREATE SPACE test;
nebula> USE test;
nebula> CREATE EDGE e1(p1 int);
nebula> CREATE TAG person(p1 int);
nebula> INSERT VERTEX person(p1) VALUES "1":(1);
nebula> INSERT VERTEX person(p1) VALUES "2":(2);
nebula> INSERT EDGE e1(p1) VALUES "1"->"2"@0:(10);
nebula> INSERT EDGE e1(p1) VALUES "1"->"2"@1:(11);
nebula> INSERT EDGE e1(p1) VALUES "1"->"2"@2:(12);
nebula> INSERT EDGE e1(p1) VALUES "1"->"2"@3:(13);
nebula> INSERT EDGE e1(p1) VALUES "1"->"2"@4:(14);
nebula> INSERT EDGE e1(p1) VALUES "1"->"2"@5:(15);
nebula> INSERT EDGE e1(p1) VALUES "1"->"2"@6:(16);

# 通过rank过滤边，查找rank大于2的边。
nebula> GO FROM "1" \
        OVER e1 \
        WHERE e1._rank>2 \
        YIELD e1._src, e1._dst, e1._rank AS Rank, e1.p1 | \
        ORDER BY Rank DESC;
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

## 过滤字符串

在`WHERE`子句中使用`STARTS WITH`、`ENDS WITH`或`CONTAINS`可以匹配字符串的特定部分。匹配时区分大小写。

### `STARTS WITH`

`STARTS WITH`会从字符串的起始位置开始匹配。

```ngql
# 查询姓名以T开头的player信息。
nebula> MATCH (v:player) \
        WHERE v.name STARTS WITH "T" \
        RETURN v.name, v.age;
+------------------+-------+
| v.name           | v.age |
+------------------+-------+
| "Tracy McGrady"  | 39    |
+------------------+-------+
| "Tony Parker"    | 36    |
+------------------+-------+
| "Tim Duncan"     | 42    |
+------------------+-------+
| "Tiago Splitter" | 34    |
+------------------+-------+
```

如果您使用小写`t`（`STARTS WITH "t"`），会返回空集，因为数据库中没有以小写`t`开头的姓名。

```ngql
nebula> MATCH (v:player) \
        WHERE v.name STARTS WITH "t" \
        RETURN v.name, v.age;
Empty set (time spent 5080/6474 us)
```

### `ENDS WITH`

`ENDS WITH`会从字符串的结束位置开始匹配。

```ngql
nebula> MATCH (v:player) \
        WHERE v.name ENDS WITH "r" \
        RETURN v.name, v.age;
+------------------+-------+
| v.name           | v.age |
+------------------+-------+
| "Vince Carter"   | 42    |
+------------------+-------+
| "Tony Parker"    | 36    |
+------------------+-------+
| "Tiago Splitter" | 34    |
+------------------+-------+
```

### `CONTAINS`

`CONTAINS`会检查关键字是否匹配字符串的某一部分。

```ngql
nebula> MATCH (v:player) \
        WHERE v.name CONTAINS "Pa" \
        RETURN v.name, v.age;
+---------------+-------+
| v.name        | v.age |
+---------------+-------+
| "Paul George" | 28    |
+---------------+-------+
| "Tony Parker" | 36    |
+---------------+-------+
| "Paul Gasol"  | 38    |
+---------------+-------+
| "Chris Paul"  | 33    |
+---------------+-------+
```

### 结合NOT使用

您可以结合布尔运算符`NOT`一起使用，否定字符串匹配条件。

```ngql
nebula> MATCH (v:player) \
        WHERE NOT v.name ENDS WITH "R" \
        RETURN v.name, v.age;
+-------------------------+-------+
| v.name                  | v.age |
+-------------------------+-------+
| "Rajon Rondo"           | 33    |
+-------------------------+-------+
| "Rudy Gay"              | 32    |
+-------------------------+-------+
| "Dejounte Murray"       | 29    |
+-------------------------+-------+
| "Chris Paul"            | 33    |
+-------------------------+-------+
| "Carmelo Anthony"       | 34    |
+-------------------------+-------+
...
```

<!--

[Not supported yet.]

## Use patterns in WHERE

### Filter on patterns

### Filter on patterns using NOT

### Filter on properties in patterns

### Filter on edge type

-->

## 过滤列表

### 匹配列表中的值

使用`IN`运算符检查某个值是否在指定列表中。

```ngql
nebula> MATCH (v:player) \
        WHERE v.age IN range(20,25) \
        RETURN v.name, v.age;
+-------------------------+-------+
| v.name                  | v.age |
+-------------------------+-------+
| "Ben Simmons"           | 22    |
+-------------------------+-------+
| "Kristaps Porzingis"    | 23    |
+-------------------------+-------+
| "Luka Doncic"           | 20    |
+-------------------------+-------+
| "Kyle Anderson"         | 25    |
+-------------------------+-------+
| "Giannis Antetokounmpo" | 24    |
+-------------------------+-------+
| "Joel Embiid"           | 25    |
+-------------------------+-------+
```

### 结合NOT使用

```ngql
nebula> MATCH (v:player) \
        WHERE v.age NOT IN range(20,25) \
        RETURN v.name AS Name, v.age AS Age \
        ORDER BY Age;
+---------------------+-----+
| Name                | Age |
+---------------------+-----+
| "Kyrie Irving"      | 26  |
+---------------------+-----+
| "Cory Joseph"       | 27  |
+---------------------+-----+
| "Damian Lillard"    | 28  |
+---------------------+-----+
| "Paul George"       | 28  |
+---------------------+-----+
| "Ricky Rubio"       | 28  |
+---------------------+-----+
...
```