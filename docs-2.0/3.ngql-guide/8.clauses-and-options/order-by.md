# ORDER BY

`ORDER BY`子句指定输出结果的排序规则。

- 在原生 nGQL 中，必须在`YIELD`子句之后使用管道符（|）和`ORDER BY`子句。

- 在 openCypher 方式中，不允许使用管道符。在`RETURN`子句之后使用`ORDER BY`子句。

排序规则分为如下两种：

- `ASC`（默认）: 升序。
- `DESC`: 降序。

## 原生 nGQL 语法

```ngql
<YIELD clause>
ORDER BY <expression> [ASC | DESC] [, <expression> [ASC | DESC] ...];
```

!!! compatibility

    原生 nGQL 语法中，`ORDER BY`命令后必须使用引用符`$-.`。但在 2.5.0 之前的版本中不需要。

### 示例

```ngql
nebula> FETCH PROP ON player "player100", "player101", "player102", "player103" \
        YIELD properties(vertex).age AS age, properties(vertex).name AS name \
        | ORDER BY $-.age ASC, $-.name DESC;
+-----+---------------------+
| age | name                |
+-----+---------------------+
| 32  | "Rudy Gay"          |
| 33  | "LaMarcus Aldridge" |
| 36  | "Tony Parker"       |
| 42  | "Tim Duncan"        |
+-----+---------------------+

nebula> $var = GO FROM "player100" OVER follow \
        YIELD dst(edge) AS dst; \
        ORDER BY $var.dst DESC;
+-------------+
| dst         |
+-------------+
| "player125" |
| "player101" |
+-------------+
```

## OpenCypher 方式语法

```ngql
<RETURN clause>
ORDER BY <expression> [ASC | DESC] [, <expression> [ASC | DESC] ...];
```

### 示例

```ngql
nebula> MATCH (v:player) RETURN v.player.name AS Name, v.player.age AS Age  \
        ORDER BY Name DESC;
+-----------------+-----+
| Name            | Age |
+-----------------+-----+
| "Yao Ming"      | 38  |
| "Vince Carter"  | 42  |
| "Tracy McGrady" | 39  |
| "Tony Parker"   | 36  |
| "Tim Duncan"    | 42  |
+-----------------+-----+
...

# 首先以年龄排序，如果年龄相同，再以姓名排序。
nebula> MATCH (v:player) RETURN v.player.age AS Age, v.player.name AS Name  \
        ORDER BY Age DESC, Name ASC;
+-----+-------------------+
| Age | Name              |
+-----+-------------------+
| 47  | "Shaquille O'Neal" |
| 46  | "Grant Hill"      |
| 45  | "Jason Kidd"      |
| 45  | "Steve Nash"      |
+-----+-------------------+
...
```

## NULL 值的排序

升序排列时，会在输出的最后列出 NULL 值，降序排列时，会在输出的开头列出 NULL 值。

```ngql
nebula> MATCH (v:player{name:"Tim Duncan"}) --> (v2) \
        RETURN v2.player.name AS Name, v2.player.age AS Age  \
        ORDER BY Age;
+-----------------+--------------+
| Name            | Age          |
+-----------------+--------------+
| "Tony Parker"   | 36           |
| "Manu Ginobili" | 41           |
| "Spurs"         | UNKNOWN_PROP |
+-----------------+--------------+

nebula> MATCH (v:player{name:"Tim Duncan"}) --> (v2) \
        RETURN v2.player.name AS Name, v2.player.age AS Age  \
        ORDER BY Age DESC;
+-----------------+--------------+
| Name            | Age          |
+-----------------+--------------+
| "Spurs"         | UNKNOWN_PROP |
| "Manu Ginobili" | 41           |
| "Tony Parker"   | 36           |
+-----------------+--------------+
```
