# 点标识符和分区

本文档提供有关点标识符（简称 `VID`）和分区的一些介绍。

在 **Nebula Graph** 中，点是用点标识符（即 `VID`）标识的。插入点时，必须指定 `VID`（int64）。`VID` 可以由应用程序生成，也可以使用 **Nebula Graph** 提供的哈希函数生成。

`VID` 在一个图空间中必须唯一。即在同一个图空间中，拥有相同 `VID` 的点被当做同一个点。不同图空间中的 `VID` 彼此独立。此外，一个 `VID` 可以拥有多种 `TAG`。

向 **Nebula Graph** 集群中插入数据时，点和边会分布到不同的分区中，而这些分区又分布在多台机器上。应用程序如果希望将某些点落在同一个分区中（也即在同一台机器上），可根据以下公式自行控制 `VID` 的生成。

`VID` 和分区的对应关系为：

```text
VID mod partition_number = partition ID + 1
```

其中，

- `mod` 是取模操作。
- `partition_number` 是 `VID` 所处图空间的的分区数量，即 [CREATE SPACE](../2.query-language/4.statement-syntax/1.data-definition-statements/create-space-syntax.md) 语句中 `partition_num` 的值。
- `partition ID` 即该 `VID` 所在分区的 ID。

例如，如果有 100 个分区，那 `VID` 为 1、101、1001 的点将存储在同一个分区上。

此外，`partition ID` 和机器之间的对应关系是随机的。因此不可以假设任何两个分区分布在同一台机器上。
