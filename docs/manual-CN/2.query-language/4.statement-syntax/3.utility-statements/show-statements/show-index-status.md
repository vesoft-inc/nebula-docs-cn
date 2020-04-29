# SHOW INDEX STATUS 语法

```ngql
SHOW {TAG | EDGE} INDEX STATUS
```

`SHOW INDEX STATUS` 用于列出已创建完成的 Tag/Edge-type 的索引状态信息。使用以下命令列出 tag 索引的状态信息：

```ngql
nebula> SHOW TAG INDEX STATUS;
==========================================
| Name                | Tag Index Status |
==========================================
| single_person_index | SUCCEEDED        |
------------------------------------------
```

如何创建索引请参考[索引](../../1.data-definition-statements/index.md)文档。
