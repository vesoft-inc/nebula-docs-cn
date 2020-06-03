# UPDATE 语法

**Nebula Graph** 支持 `UPDATE` 一个点或者一条边的属性，支持 CAS 操作，支持返回相关的属性。`UPDATE` 一次只能更新一个点/边的一个 tag/edge type。

## 更新点

```ngql
UPDATE VERTEX <vid> SET <update_columns> [WHEN <condition>] [YIELD <columns>]
```

**注意：**`WHEN` 和 `YIELD` 是可选的。

- `vid` 表示需要更新的 vertex ID。
- `update_columns` 表示需要更新的 tag 上的 columns，比如 `tag1.col1 = $^.tag2.col2 + 1` 表示把这个点的 `tag1.col1` 更新成 `tag2.col2 + 1`。

    **注意：**  `$^`表示 `UPDATE` 中需要更新的点。

- `condition` 是一些约束条件，只有满足这个条件，`UPDATE` 才会真正执行，支持表达式操作。
- `columns` 表示需要返回的 columns，此处 `YIELD` 可返回 update 以后最新的 columns 值。

举例如下：

```ngql
nebula> UPDATE VERTEX 101 SET player.age = $^.player.age + 1 \
WHEN $^.player.name == "Tony Parker" \
YIELD $^.player.name AS name, $^.player.age AS age;
```

这个例子里面，101 有一个 tag，即 player。

## 更新边

```ngql
UPDATE EDGE <edge> SET <update_columns> [WHEN <condition>] [YIELD <columns>]
```

**注意：**`WHEN` 和 `YIELD` 是可选的。

- `edge` 表示需要更新的 edge，edge 的格式为 `<src> -> <dst> [@ranking] OF <edge_type>`。
- `update_columns` 表示需要更新的 edge 上的属性。
- `condition` 是一些约束条件，只有满足这个条件，update 才会真正执行，支持表达式操作。
- `columns` 表示需要返回的 columns，此处 YIELD 可返回 update 以后最新的 columns 值。

举例如下：

```ngql
nebula> UPDATE EDGE 100 -> 200@0 OF serve SET start_year = serve.start_year + 1 \
YIELD $^.player.name AS name, serve.start_year AS start;
```
