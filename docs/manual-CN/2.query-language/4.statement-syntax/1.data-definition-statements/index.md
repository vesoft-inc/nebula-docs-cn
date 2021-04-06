# Schema 索引

```ngql
CREATE {TAG | EDGE} INDEX [IF NOT EXISTS] <index_name> ON {<tag_name> | <edge_name>} (prop_name_list)
```

**Nebula Graph** 支持两种类型的索引：**Tag 索引**和 **Edge Type 索引**。

## 使用限制

1. 对应 Tag 或者 Edge Type 已经存在。
2. 索引只用于 [LOOKUP 语句](../2.data-query-and-manipulation-statements/lookup-syntax.md)，目的为查找点 VID；
3. 索引**并没有**查询加速功能。[GO 语句](../2.data-query-and-manipulation-statements/go-syntax.md)等所有图遍历语句**都不使用**索引；
4. 只对于需要“通过属性查找点 VID”的**属性**建立索引，不要对其他属性增加索引。
5. 不支持多个 Tag 的属性之间建立组合索引。只允许在同一个 Tag/Edge Type 的多个属性上建立索引。
6. 索引会**显著降低**在线写入性能，经验值是 2-10 倍。

对于索引的原理和优化见[附录](../../../5.appendix/index.md)。

## 创建索引

`CREATE INDEX` 用于为已有 Tag/Edge-type 创建索引。

### 创建单属性索引

```ngql
nebula> CREATE TAG INDEX player_index_0 on player(name);
```

上述语句在所有标签为 _player_ 的点上为属性 _name_ 创建了一个索引。

```ngql
nebula> CREATE EDGE INDEX follow_index_0 on follow(degree);
```

上述语句在 _follow_ 边类型的所有边上为属性 _degree_ 创建了一个索引。

### 创建组合索引

schema 索引还支持为相同 tag 或 edge 中的多个属性同时创建索引，这种包含多种属性的索引在 **Nebula Graph** 中称为组合索引。

```ngql
nebula> CREATE TAG INDEX player_index_1 on player(name,age);
```

上述语句在所有标签为 _player_ 的点上为属性 _name_ 和 _age_ 创建了一个组合索引。


## 列出索引

```ngql
SHOW {TAG | EDGE} INDEXES
```

`SHOW INDEXES` 用于列出已创建完成的 Tag/Edge-type 的索引信息。使用以下命令列出索引：

```ngql
nebula> SHOW TAG INDEXES;
=============================
| Index ID | Index Name     |
=============================
| 22       | player_index_0 |
-----------------------------
| 23       | player_index_1 |
-----------------------------

nebula> SHOW EDGE INDEXES;
=============================
| Index ID | Index Name     |
=============================
| 24       | follow_index_0 |
-----------------------------

```

## 返回索引信息

```ngql
DESCRIBE {TAG | EDGE} INDEX <index_name>
```

`DESCRIBE INDEX` 用于返回指定索引信息。例如，使用以下命令返回索引信息：

```ngql
nebula> DESCRIBE TAG INDEX player_index_0;
==================
| Field | Type   |
==================
| name  | string |
------------------

nebula> DESCRIBE TAG INDEX player_index_1;
==================
| Field | Type   |
==================
| name  | string |
------------------
| age   | int    |
------------------
```

## 删除索引

```ngql
DROP {TAG | EDGE} INDEX [IF EXISTS] <index_name>
```

`DROP INDEX` 用于删除指定名称的 Tag/Edge-type 索引。例如，使用以下命令删除名为 _player_index_0_ 的索引：

```ngql
nebula> DROP TAG INDEX player_index_0;
```

## 重构索引

```ngql
REBUILD {TAG | EDGE} INDEX <index_name> OFFLINE
```

如果索引在插入数据之前创建，此时无需执行索引重构操作；
如果创建索引时，数据库里已经存有数据（但没有索引），则不会自动对旧的数据进行索引。此时需要执行索引重构操作，否则会造成索引与数据不一致。

重构完成后，可使用 `SHOW {TAG | EDGE} INDEX STATUS` 命令查看索引是否重构成功。例如：

```ngql
nebula> CREATE TAG person(name string, age int, gender string, email string);
Execution succeeded (Time spent: 10.051/11.397 ms)

nebula> CREATE TAG INDEX single_person_index ON person(name);
Execution succeeded (Time spent: 2.168/3.379 ms)

nebula> REBUILD TAG INDEX single_person_index OFFLINE;
Execution succeeded (Time spent: 2.352/3.568 ms)

nebula> SHOW TAG INDEX STATUS;
==========================================
| Name                | Tag Index Status |
==========================================
| single_person_index | SUCCEEDED        |
------------------------------------------
```

## 使用索引

索引创建完成并插入相关数据后，即可使用 [LOOKUP](../2.data-query-and-manipulation-statements/lookup-syntax.md) 语句进行数据查询。
