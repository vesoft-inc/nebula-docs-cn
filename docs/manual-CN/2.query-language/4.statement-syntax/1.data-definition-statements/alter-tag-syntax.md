# 修改 Tag

```ngql
ALTER TAG <tag_name>
    <alter_definition> [, alter_definition] ...]
    [ttl_definition [, ttl_definition] ... ]

<alter_definition>::=
    ADD (prop_name data_type)
    | DROP (prop_name)
    | CHANGE (prop_name data_type)

ttl_definition::=
    TTL_DURATION = ttl_duration, TTL_COL = prop_name
```

`ALTER TAG` 语句可改变标签的结构，例如，可以添加或删除属性，更改已有属性的类型，也可将属性设置为 TTL（生存时间），或更改 TTL 时间。

**注意：** 修改标签结构时，**Nebula Graph** 将自动检测是否存在索引。修改时需要两步判断。首先，判断这个标签是否关联索引。其次，检查所有关联的索引，判断待删除或更改的 column item 是否存在于索引的 column 中，如果存在则拒绝修改。如果不存在，即使有关联的索引也允许修改。

请参考[索引文档](index.md)了解索引详情。

一个 `ALTER` 语句允许使用多个 `ADD`，`DROP`，`CHANGE` 语句，语句之间需用逗号隔开。但是不要在一个语句中添加，删除或更改相同的属性。如果必须进行此操作，请将其作为 `ALTER` 语句的子语句。

```ngql
nebula> CREATE TAG t1 (name string, age int);
nebula> ALTER TAG t1 ADD (id int, address string);
nebula> ALTER TAG t1 TTL_DURATION = 2, TTL_COL = "age";
```

**注意：** `TTL_COL` 仅支持 `INT` 和 `TIMESTAMP` 类型的属性。
