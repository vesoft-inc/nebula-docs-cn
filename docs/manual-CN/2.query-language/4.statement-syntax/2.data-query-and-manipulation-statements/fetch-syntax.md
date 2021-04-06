# Fetch 语法

`FETCH` 语句用于获取点和边的属性。

## 获取点属性

`FETCH PROP ON` 可返回点的一系列属性，目前已支持一条语句返回多个点属性。`FETCH` 获取点属性支持与[管道](../../3.language-structure/pipe-syntax.md) 及[用户自定义变量](../../3.language-structure/user-defined-variables.md)一起使用。

```ngql
FETCH PROP ON {<tag_name> | <tag_name_list> | *} <vertex_id_list> [YIELD [DISTINCT] <return_list>]
```

`FETCH <tag_name_list>` 操作仅适用于 1.0.1 版本或更高版本。如果您使用的 **Nebula Graph** 版本早于 1.0.1，则在一次 FETCH 查询中只能获取一种类型点的属性。

`*` 返回指定 `VID` 点的所有属性。

`<tag_name_list>::=[tag_name [, tag_name]]` 为标签名称，与 return_list 中的标签相同。

`<vertex_id_list>::=[vertex_id [, vertex_id]]` 是一组用 "," 分隔开的点 `VID` 列表。

`[YIELD [DISTINCT] <return_list>]` 为返回的属性列表，`YIELD` 语法参看 [YIELD Syntax](yield-syntax.md) 。

### 示例

```ngql
-- 返回点 100 的所有属性。
nebula> FETCH PROP ON * 100;

-- 返回点100，102 的 player、team tag 上的所有属性。
nebula> FETCH PROP ON * 100, 102;

-- 返回点 100、201 的所有属性。
nebula> FETCH PROP ON player, team 100, 201;

-- 如未指定 YIELD 字段，则返回点 100, tag 为 player 的所有属性。
nebula> FETCH PROP ON player 100;

-- 返回点 100 的姓名与年龄属性。
nebula> FETCH PROP ON player 100 YIELD player.name, player.age;

-- 通过 hash 生成 int64 点 ID，返回其姓名和年龄属性。
nebula> FETCH PROP ON player hash("nebula")  YIELD player.name, player.age;

-- 支持与管道一起使用
nebula> YIELD 100 AS id | FETCH PROP ON player $-.id;

-- 沿边 follow 寻找点 100 的所有近邻，返回其姓名和年龄属性。
nebula> GO FROM 100 OVER follow YIELD follow._dst AS id | FETCH PROP ON player $-.id YIELD player.name, player.age;

-- 与上述语法相同。
nebula> $var = GO FROM 100 OVER follow YIELD follow._dst AS id; FETCH PROP ON player $var.id YIELD player.name, player.age;

-- 获取 100、101、102 三个点，返回姓名和年龄都不相同的记录。
nebula> FETCH PROP ON player 100,101,102 YIELD DISTINCT player.name, player.age;

```

## 获取边属性

使用 `FETCH` 获取边属性的用法与点属性大致相同，且可同时获取相同类型多条边的属性。

```ngql
FETCH PROP ON <edge_type> <vid> -> <vid>[@<rank>] [, <vid> -> <vid> ...] [YIELD [DISTINCT] <return_list>]
```

`<edge_type>` 指定边的类型，需与 `<return_list>` 相同。

`<vid> -> <vid>` 从起始点到终止点，多条边需使用逗号隔开。

`<rank>` 指定相同类型边 rank，可选。如未指定，则默认返回 rank 为 0 的边。

`[YIELD [DISTINCT] <return_list>]` 为返回的属性列表。

### 获取边属性示例

```ngql
-- 本语句未指定 YIELD，因此获取从点 100 到点 200 边 serve 的所有属性。
nebula> FETCH PROP ON serve 100 -> 200;

-- 仅返回属性 start_year。
nebula> FETCH PROP ON serve 100 -> 200 YIELD serve.start_year;

-- 获取点 100 出边 follow 的 degree 属性。
nebula> GO FROM 100 OVER follow YIELD follow.degree;

-- 同上述语句。
nebula> GO FROM 100 OVER follow YIELD follow._src AS s, serve._dst AS d \
 | FETCH PROP ON follow $-.s -> $-.d YIELD follow.degree;

-- 同上述语句。
nebula> $var = GO FROM 100 OVER follow YIELD follow._src AS s, follow._dst AS d;\
 FETCH PROP ON follow $var.s -> $var.d YIELD follow.degree;
```
