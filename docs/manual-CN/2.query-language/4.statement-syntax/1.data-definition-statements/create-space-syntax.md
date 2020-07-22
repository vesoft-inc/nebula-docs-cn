# CREATE SPACE 语法

```ngql
CREATE SPACE [IF NOT EXISTS] <space_name>
   [(partition_num = <part_num>, replica_factor = <raft_copy>, charset = <charset>, collate = <collate>)]
```

以上语句用于创建一个新的图空间。不同的图空间是物理隔离的。

## IF NOT EXISTS

创建图空间可使用 `IF NOT EXISTS` 关键字，这个关键字会自动检测对应的图空间是否存在，如果不存在则创建新的，如果存在则直接返回。

**注意：** 这里判断图空间是否存在只是比较图空间的名字(不包括属性)。

## Space Name 图空间名

* **space_name**

    图空间的名称在集群中标明了一个唯一的空间。命名规则详见 [Schema Object Names](../../3.language-structure/schema-object-names.md)

## 自定义图空间选项

在创建图空间的时候，可以传入如下四个自定义选项：

* _partition_num_

    _partition_num_ 表示数据分片数量。默认值为 100。建议为硬盘数量的 5 倍。

* _replica_factor_

    _replica_factor_ 表示副本数量。默认值是 1，生产集群建议为 3。由于采用多数表决原理，因此需为奇数。

* _charset_

    _charset_ 表示字符集，定义了字符以及字符的编码，默认为 utf8。

* _collate_

    _collate_ 表示字符序，定义了字符的比较规则，默认为 utf8_bin。

如果没有自定义选项，**Nebula Graph** 会使用默认的值（partition_number、replica_factor、charset 和 collate）来创建图空间。

## 示例

```ngql
nebula> CREATE SPACE my_space_1; -- 使用默认选项创建图空间
nebula> CREATE SPACE my_space_2(partition_num=10); -- 使用默认 replica_factor 创建图空间
nebula> CREATE SPACE my_space_3(replica_factor=1);  -- 使用默认 partition_number 创建图空间
nebula> CREATE SPACE my_space_4(partition_num=10, replica_factor=1);
```

## 检查 partition 分布正常

在某些大集群上，由于启动时间先后不一，可能会导致 partition 分布不均，可以通过如下命令（SHOW HOSTS）检查机器和分布。

```ngql
nebula> SHOW HOSTS;
================================================================================================
| Ip            | Port  | Status | Leader count | Leader distribution | Partition distribution |
================================================================================================
| 192.168.8.210 | 34600 | online | 13           | test: 13            | test: 37               |
------------------------------------------------------------------------------------------------
| 192.168.8.210 | 34900 | online | 12           | test: 12            | test: 38               |
```

若发现机器都已在线，但 partition 分布不均，可以通过如下命令 （BALANCE LEADER）来命令 partition 重分布。

```ngql
nebula> BALANCE LEADER;
```

具体见 [SHOW HOSTS](../3.utility-statements/show-statements/show-hosts-syntax.md) 和 [BALANCE](../../../3.build-develop-and-administration/5.storage-service-administration/storage-balance.md)。
