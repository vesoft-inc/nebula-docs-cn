# Delete Edge 语法

 `DELETE EDGE` 语句用于删除边。给定一个 edge 类型，及其起点与终点，**Nebula Graph** 支持删除这条边及其相关属性和 rank，也支持指定 rank 删除边，语法如下：

```ngql
DELETE EDGE <edge_type> <vid> -> <vid>[@<rank>] [, <vid> -> <vid> ...]
```

例如，

```ngql
nebula> DELETE EDGE follow 100 -> 200;
```

以上示例删除一条起点为 `100`， 终点为 `200`， 边类型为 `follow` 的边。

系统内部会找出与这条边相关联的属性，并将其全部删除。整个过程当前还无法保证原子性，因此当遇到失败时请重试。
