# ORDER BY

`ORDER BY`子句指定输出结果的排序规则。

- 在原生nGQL中，必须在`YIELD`子句之后使用管道符（|）和`ORDER BY`子句。

- 在openCypher方式中，不允许使用管道符。在`RETURN`子句之后使用`ORDER BY`子句。

排序规则分为如下两种：

- `ASC`（默认）: 升序。
- `DESC`: 降序。

## 原生nGQL语法

```ngql
<YIELD clause>
ORDER BY <expression> [ASC | DESC] [, <expression> [ASC | DESC] ...];
```

!!! compatibility

    原生nGQL语法中，`ORDER BY`命令后必须使用引用符`$-.`。但在2.5.0之前的版本中不需要。

### 示例

```ngql
nebula> FETCH PROP ON player "player100", "player101", "player102", "player103" \
        YIELD player.age AS age, player.name AS name \
        | ORDER BY $-.age ASC, $-.name DESC;
+-------------+-----+---------------------+
| VertexID    | age | name                |
+-------------+-----+---------------------+
| "player103" | 32  | "Rudy Gay"          |
+-------------+-----+---------------------+
| "player102" | 33  | "LaMarcus Aldridge" |
+-------------+-----+---------------------+
| "player101" | 36  | "Tony Parker"       |
+-------------+-----+---------------------+
| "player100" | 42  | "Tim Duncan"        |
+-------------+-----+---------------------+
```

## OpenCypher方式语法

```ngql
<RETURN clause>
ORDER BY <expression> [ASC | DESC] [, <expression> [ASC | DESC] ...];
```

### 示例

```ngql
nebula> MATCH (v:player) RETURN v.name AS Name, v.age AS Age  \
        ORDER BY Name DESC;
+-----------------+-----+
| Name            | Age |
+-----------------+-----+
| "Yao Ming"      | 38  |
+-----------------+-----+
| "Vince Carter"  | 42  |
+-----------------+-----+
| "Tracy McGrady" | 39  |
+-----------------+-----+
| "Tony Parker"   | 36  |
+-----------------+-----+
| "Tim Duncan"    | 42  |
+-----------------+-----+
...

# 首先以年龄排序，如果年龄相同，再以姓名排序。
nebula> MATCH (v:player) RETURN v.age AS Age, v.name AS Name  \
        ORDER BY Age DESC, Name ASC;
+-----+-------------------+
| Age | Name              |
+-----+-------------------+
| 47  | "Shaquille O'Neal" |
+-----+-------------------+
| 46  | "Grant Hill"      |
+-----+-------------------+
| 45  | "Jason Kidd"      |
+-----+-------------------+
| 45  | "Steve Nash"      |
+-----+-------------------+
...
```

## NULL值的排序

升序排列时，会在输出的最后列出NULL值，降序排列时，会在输出的开头列出NULL值。

```ngql
nebula> MATCH (v:player{name:"Tim Duncan"}) --> (v2) \
        RETURN v2.name AS Name, v2.age AS Age  \
        ORDER BY Age;
+-----------------+----------+
| Name            | Age      |
+-----------------+----------+
| "Tony Parker"   | 36       |
+-----------------+----------+
| "Manu Ginobili" | 41       |
+-----------------+----------+
| "Spurs"         | __NULL__ |
+-----------------+----------+

nebula> MATCH (v:player{name:"Tim Duncan"}) --> (v2) \
        RETURN v2.name AS Name, v2.age AS Age  \
        ORDER BY Age DESC;
+-----------------+----------+
| Name            | Age      |
+-----------------+----------+
| "Spurs"         | __NULL__ |
+-----------------+----------+
| "Manu Ginobili" | 41       |
+-----------------+----------+
| "Tony Parker"   | 36       |
+-----------------+----------+
```
