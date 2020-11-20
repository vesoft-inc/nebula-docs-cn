# UPDATE EDGE 语法

**Nebula Graph** 支持 `UPDATE EDGE` 一条边的属性，支持 CAS 操作，支持返回相关的属性。`UPDATE EDGE` 一次只能更新一条边的一个 edge type 上的属性。

```ngql
UPDATE EDGE <edge> SET <update_columns> [WHEN <condition>] [YIELD <columns>]
```

**注意：**`WHEN` 和 `YIELD` 是可选的。

- `edge` 表示需要更新的 edge，edge 的格式为 `<src> -> <dst> [@rank] OF <edge_type>`。
- `update_columns` 表示需要更新的 edge 上的属性。
- `condition` 是一些约束条件，只有满足这个条件，update 才会真正执行，支持表达式操作。
- `columns` 表示需要返回的 columns，此处 YIELD 可返回 update 以后最新的 columns 值。

举例如下：

```ngql
nebula> UPDATE EDGE 100 -> 200@0 OF serve SET start_year = serve.start_year + 1 \
YIELD $^.player.name AS name, serve.start_year AS start;
```
