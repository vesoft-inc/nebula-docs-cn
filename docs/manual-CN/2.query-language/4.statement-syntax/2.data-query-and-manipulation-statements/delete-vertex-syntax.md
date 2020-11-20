# Delete Vertex 语法

**Nebula Graph** 支持给定点 ID（或 hash ID、UUID），删除这些点和与其相关联的入边和出边，语法如下：

```ngql
DELETE VERTEX <vid_list>
```

例如，

```ngql
nebula> DELETE VERTEX 121;
```

以上示例删除 ID 为 `121` 的点。

系统内部会找出与这些点相关联的出边和入边，并将其全部删除，然后再删除点相关的信息。整个过程当前还无法保证原子性，因此若操作失败请重试。
