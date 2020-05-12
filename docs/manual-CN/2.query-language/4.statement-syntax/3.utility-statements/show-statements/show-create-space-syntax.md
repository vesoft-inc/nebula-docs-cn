# SHOW CREATE SPACE 语法

```ngql
SHOW CREATE SPACE <space_name>
```

`SHOW CREATE SPACE` 返回指定 space 及其创建语法。如果 space 包含默认值，则同时返回默认值。

```ngql
nebula> SHOW CREATE SPACE NBA;
=========================================================================================================
| Space | Create Space                                                                                  |
=========================================================================================================
| NBA  | CREATE SPACE gods (partition_num = 1, replica_factor = 1, charset = utf8, collate = utf8_bin) |
---------------------------------------------------------------------------------------------------------
```
