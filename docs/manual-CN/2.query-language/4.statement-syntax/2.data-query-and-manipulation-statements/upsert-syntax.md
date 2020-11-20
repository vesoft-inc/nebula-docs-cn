# UPSERT 语法

`UPSERT` 用于插入新的点或边或更新现有的点或边。如果点或边不存在，则会新建该点或边。`UPSERT` 是 `INSERT` 和 `UPDATE` 的组合。

`UPSERT` 操作相比于 `INSERT` 操作性能会低很多，因为 `UPSERT` 是在 partition 级别的 read-modify-write 串行化操作，因此不适用于大并发更改写入的场景。

- 如果点或边不存在，则会新建该点或边，无论 WHEN 条件是否满足，且未经 SET 指定的属性字段使用该字段的默认值，如果默认值不存在则报错；
- 如果该点或者边存在，并且 WHEN 条件满足，则会更新；
- 如果该点或者边存在, 并且 WHEN 条件不满足，则不会有任何操作。

```ngql
UPSERT {VERTEX <vid> | EDGE <edge>} SET <update_columns> [WHEN <condition>] [YIELD <columns>]
```

- `vid` 表示需要更新的 vertex ID。
- `edge` 表示需要更新的 edge，edge 的格式为 `<src> -> <dst> [@rank] OF <edge_type>`。
- `update_columns` 表示需要更新的 tag 或 edge 上的 columns，比如 `tag1.col1 = $^.tag2.col2 + 1` 表示把这个点的 `tag1.col1` 更新成 `tag2.col2 + 1`。

    **注意：**  `$^`表示 `UPDATE` 中需要更新的点。

- `condition` 是一些约束条件，只有满足这个条件，`UPDATE` 才会真正执行，支持表达式操作。
- `columns` 表示需要返回的 columns，此处 `YIELD` 可返回 update 以后最新的 columns 值。

例如：

```ngql
nebula> INSERT VERTEX player(name, age) VALUES 111:("Ben Simmons", 22); -- 插入一个新点。
nebula> UPSERT VERTEX 111 SET player.name = "Dwight Howard", player.age = $^.player.age + 11 WHEN $^.player.name == "Ben Simmons" && $^.player.age > 20 YIELD $^.player.name AS Name, $^.player.age AS Age; -- 对该点进行 UPSERT 操作。
=======================
| Name          | Age |
=======================
| Dwight Howard | 33  |
-----------------------
```

```ngql
nebula> FETCH PROP ON * 111; -- 返回为空，点 111 不存在
Empty set (Time spent: 3.069/4.382 ms)
nebula> UPSERT VERTEX 111 SET player.age = $^.player.age + 1;
```

当点 111 不存在，player 的 age 有默认值时，点 111 的 player.age 为默认值 + 1；此处 player.age 未设置默认值，因此报错。

```ngql
nebula> CREATE TAG person(followers int, age int DEFAULT 0); -- 创建示例 tag person

nebula> UPSERT VERTEX 300 SET person.followers = $^.person.age + 1,  person.age = 8; -- followers 为 1，age 为 8

nebula> UPSERT VERTEX 300 SET person.age = 8, person.followers = $^.person.age + 1; -- followers 为 9，age 为 8
```
