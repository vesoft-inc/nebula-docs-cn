# 注释

本文介绍 nGQL 中的注释方式。

## 历史版本兼容性

* Nebula Graph 1.x 支持四种注释方式：`#`、`--`、`//`、`/* */`。
* Nebula Graph 2.x 中，`--`不再是注释符。

## Examples

```ngql
nebula> # 这行什么都不做。
nebula> RETURN 1+1;     # 这条注释延续到行尾。
nebula> RETURN 1+1;     // 这条注释延续到行尾。
nebula> RETURN 1 /* 这是一条行内注释 */ + 1 == 2;
nebula> RETURN 11 +            \
/* 多行注释       \
用反斜线来换行。   \
*/ 12;
```

nGQL 语句中的反斜线（\）代表换行。

## OpenCypher 兼容性

* 在 nGQL 中，用户必须在行末使用反斜线（\）来换行，即使是在使用`/* */`符号的多行注释内。
* 在 openCypher 中不需要使用反斜线换行。

```openCypher
/* openCypher 风格：
这条注释
延续了不止
一行 */
MATCH (n:label)
RETURN n;
```

```ngql
/* 原生 nGQL 风格：  \
这条注释       \
延续了不止     \
一行 */       \
MATCH (n:tag) \
RETURN n;
```
