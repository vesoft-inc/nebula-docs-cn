# WHERE

`WHERE`子句可以根据条件过滤输出结果。

`WHERE`子句通常用于如下查询：

- 原生 nGQL，例如`GO`和`LOOKUP`语句。

- openCypher 方式，例如`MATCH`和`WITH`语句。

## openCypher 兼容性

- 可以在`WHERE`子句中使用 Pattern，但是不能引入新变量。例如可以使用`MATCH (v:player) WHERE (v)-->()<--(v)`，不能使用`MATCH (v:player) WHERE (v)-->(t)<--(v)`（t 为新变量）。

- [过滤 Rank](#rank) 是原生 nGQL 功能。如需在 openCypher 兼容语句中直接获取 Rank 值，可以使用 rank() 函数，例如`MATCH (:player)-[e:follow]->() RETURN rank(e);`。

## 基础用法

!!! note
    下文示例中的`$$`、`$^`等是引用符号，详情请参见[引用符](../5.operators/5.property-reference.md)。

### 用布尔运算符定义条件

在`WHERE`子句中使用布尔运算符`NOT`、`AND`、`OR`和`XOR`定义条件。关于运算符的优先级，请参见[运算符优先级](../5.operators/9.precedence.md)。

```ngql
nebula> MATCH (v:player) \
        WHERE v.player.name == "Tim Duncan" \
        XOR (v.player.age < 30 AND v.player.name == "Yao Ming") \
        OR NOT (v.player.name == "Yao Ming" OR v.player.name == "Tim Duncan") \
        RETURN v.player.name, v.player.age;
+-------------------------+--------------+
| v.player.name           | v.player.age |
+-------------------------+--------------+
| "Danny Green"           | 31           |
| "Tiago Splitter"        | 34           |
| "David West"            | 38           |
...
```

```ngql
nebula> GO FROM "player100" \
        OVER follow \
        WHERE properties(edge).degree > 90 \
        OR properties($$).age != 33 \
        AND properties($$).name != "Tony Parker" \
        YIELD properties($$);
+----------------------------------+
| properties($$)                   |
+----------------------------------+
| {age: 41, name: "Manu Ginobili"} |
+----------------------------------+
```

### 过滤属性

在`WHERE`子句中使用点或边的属性定义条件。

- 过滤点属性：

    ```ngql
    nebula> MATCH (v:player)-[e]->(v2) \
            WHERE v2.player.age < 25 \
            RETURN v2.player.name, v2.player.age;
    +----------------------+---------------+
    | v2.player.name       | v2.player.age |
    +----------------------+---------------+
    | "Ben Simmons"        | 22            |
    | "Luka Doncic"        | 20            |
    | "Kristaps Porzingis" | 23            |
    +----------------------+---------------+
    ```

    ```ngql
    nebula> GO FROM "player100" OVER follow \
            WHERE $^.player.age >= 42 \
            YIELD dst(edge);
    +-------------+
    | dst(EDGE)   |
    +-------------+
    | "player101" |
    | "player125" |
    +-------------+
    ```

- 过滤边属性：

    ```ngql
    nebula> MATCH (v:player)-[e]->() \
            WHERE e.start_year < 2000 \
            RETURN DISTINCT v.player.name, v.player.age;
    +--------------------+--------------+
    | v.player.name      | v.player.age |
    +--------------------+--------------+
    | "Tony Parker"      | 36           |
    | "Tim Duncan"       | 42           |
    | "Grant Hill"       | 46           |
    ...
    ```

    ```ngql
    nebula> GO FROM "player100" OVER follow \
            WHERE follow.degree > 90 \
            YIELD dst(edge);
    +-------------+
    | dst(EDGE)   |
    +-------------+
    | "player101" |
    | "player125" |
    +-------------+
    ```

### 过滤动态计算属性

```ngql
nebula> MATCH (v:player) \
        WHERE v[toLower("AGE")] < 21 \
        RETURN v.player.name, v.player.age;
+---------------+-------+
| v.name        | v.age |
+---------------+-------+
| "Luka Doncic" | 20    |
+---------------+-------+
```

### 过滤现存属性

```ngql
nebula> MATCH (v:player) \
        WHERE exists(v.player.age) \
        RETURN v.player.name, v.player.age;
+-------------------------+--------------+
| v.player.name           | v.player.age |
+-------------------------+--------------+
| "Danny Green"           | 31           |
| "Tiago Splitter"        | 34           |
| "David West"            | 38           |
...
```

### 过滤 rank

在 nGQL 中，如果多个边拥有相同的起始点、目的点和属性，则它们的唯一区别是 rank 值。在`WHERE`子句中可以使用 rank 过滤边。

```ngql
# 创建测试数据。
nebula> CREATE SPACE IF NOT EXISTS test (vid_type=FIXED_STRING(30));
nebula> USE test;
nebula> CREATE EDGE IF NOT EXISTS e1(p1 int);
nebula> CREATE TAG IF NOT EXISTS person(p1 int);
nebula> INSERT VERTEX person(p1) VALUES "1":(1);
nebula> INSERT VERTEX person(p1) VALUES "2":(2);
nebula> INSERT EDGE e1(p1) VALUES "1"->"2"@0:(10);
nebula> INSERT EDGE e1(p1) VALUES "1"->"2"@1:(11);
nebula> INSERT EDGE e1(p1) VALUES "1"->"2"@2:(12);
nebula> INSERT EDGE e1(p1) VALUES "1"->"2"@3:(13);
nebula> INSERT EDGE e1(p1) VALUES "1"->"2"@4:(14);
nebula> INSERT EDGE e1(p1) VALUES "1"->"2"@5:(15);
nebula> INSERT EDGE e1(p1) VALUES "1"->"2"@6:(16);

# 通过 rank 过滤边，查找 rank 大于 2 的边。
nebula> GO FROM "1" \
        OVER e1 \
        WHERE rank(edge) > 2 \
        YIELD src(edge), dst(edge), rank(edge) AS Rank, properties(edge).p1 | \
        ORDER BY $-.Rank DESC;
+-----------+-----------+------+---------------------+
| src(EDGE) | dst(EDGE) | Rank | properties(EDGE).p1 |
+-----------+-----------+------+---------------------+
| "1"       | "2"       | 6    | 16                  |
| "1"       | "2"       | 5    | 15                  |
| "1"       | "2"       | 4    | 14                  |
| "1"       | "2"       | 3    | 13                  |
+-----------+-----------+------+---------------------+
```

## 过滤字符串

在`WHERE`子句中使用`STARTS WITH`、`ENDS WITH`或`CONTAINS`可以匹配字符串的特定部分。匹配时区分大小写。

### `STARTS WITH`

`STARTS WITH`会从字符串的起始位置开始匹配。

```ngql
# 查询姓名以 T 开头的 player 信息。
nebula> MATCH (v:player) \
        WHERE v.player.name STARTS WITH "T" \
        RETURN v.player.name, v.player.age;
+------------------+--------------+
| v.player.name    | v.player.age |
+------------------+--------------+
| "Tony Parker"    | 36           |
| "Tiago Splitter" | 34           |
| "Tim Duncan"     | 42           |
| "Tracy McGrady"  | 39           |
+------------------+--------------+
```

如果使用小写`t`（`STARTS WITH "t"`），会返回空集，因为数据库中没有以小写`t`开头的姓名。

```ngql
nebula> MATCH (v:player) \
        WHERE v.player.name STARTS WITH "t" \
        RETURN v.player.name, v.player.age;
Empty set (time spent 5080/6474 us)
```

### `ENDS WITH`

`ENDS WITH`会从字符串的结束位置开始匹配。

```ngql
nebula> MATCH (v:player) \
        WHERE v.player.name ENDS WITH "r" \
        RETURN v.player.name, v.player.age;
+------------------+--------------+
| v.player.name    | v.player.age |
+------------------+--------------+
| "Tony Parker"    | 36           |
| "Tiago Splitter" | 34           |
| "Vince Carter"   | 42           |
+------------------+--------------+
```

### `CONTAINS`

`CONTAINS`会检查关键字是否匹配字符串的某一部分。

```ngql
nebula> MATCH (v:player) \
        WHERE v.player.name CONTAINS "Pa" \
        RETURN v.player.name, v.player.age;
+---------------+--------------+
| v.player.name | v.player.age |
+---------------+--------------+
| "Paul George" | 28           |
| "Tony Parker" | 36           |
| "Paul Gasol"  | 38           |
| "Chris Paul"  | 33           |
+---------------+--------------+
```

### 结合 NOT 使用

用户可以结合布尔运算符`NOT`一起使用，否定字符串匹配条件。

```ngql
nebula> MATCH (v:player) \
        WHERE NOT v.player.name ENDS WITH "R" \
        RETURN v.player.name, v.player.age;
+-------------------------+--------------+
| v.player.name           | v.player.age |
+-------------------------+--------------+
| "Danny Green"           | 31           |
| "Tiago Splitter"        | 34           |
| "David West"            | 38           |
| "Russell Westbrook"     | 30           |
...
```

<!--

[Not supported yet.]

## Use patterns in WHERE

### Filter on patterns

### Filter on patterns using NOT

### Filter on properties in patterns

-->

## 过滤列表

### 匹配列表中的值

使用`IN`运算符检查某个值是否在指定列表中。

```ngql
nebula> MATCH (v:player) \
        WHERE v.player.age IN range(20,25) \
        RETURN v.player.name, v.player.age;
+-------------------------+--------------+
| v.player.name           | v.player.age |
+-------------------------+--------------+
| "Ben Simmons"           | 22           |
| "Giannis Antetokounmpo" | 24           |
| "Kyle Anderson"         | 25           |
| "Joel Embiid"           | 25           |
| "Kristaps Porzingis"    | 23           |
| "Luka Doncic"           | 20           |
+-------------------------+--------------+

nebula> LOOKUP ON player \
        WHERE player.age IN [25,28]  \
        YIELD properties(vertex).name, properties(vertex).age;
+-------------------------+------------------------+
| properties(VERTEX).name | properties(VERTEX).age |
+-------------------------+------------------------+
| "Kyle Anderson"         | 25                     |
| "Damian Lillard"        | 28                     |
| "Joel Embiid"           | 25                     |
| "Paul George"           | 28                     |
| "Ricky Rubio"           | 28                     |
+-------------------------+------------------------+
```

### 结合 NOT 使用

```ngql
nebula> MATCH (v:player) \
        WHERE v.player.age NOT IN range(20,25) \
        RETURN v.player.name AS Name, v.player.age AS Age \
        ORDER BY Age;
+---------------------+-----+
| Name                | Age |
+---------------------+-----+
| "Kyrie Irving"      | 26  |
| "Cory Joseph"       | 27  |
| "Damian Lillard"    | 28  |
| "Paul George"       | 28  |
| "Ricky Rubio"       | 28  |
...
```
