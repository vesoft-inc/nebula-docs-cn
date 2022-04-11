# 大小写区分

## 标识符区分大小写

以下语句会出现错误，因为`my_space`和`MY_SPACE`是两个不同的图空间。

```ngql
nebula> CREATE SPACE IF NOT EXISTS my_space (vid_type=FIXED_STRING(30));
nebula> use MY_SPACE;
[ERROR (-8)]: SpaceNotFound:
```

## 关键字不区分大小写

以下语句是等价的，因为`show`和`spaces`是关键字。

```ngql
nebula> show spaces;  
nebula> SHOW SPACES;
nebula> SHOW spaces;
nebula> show SPACES;
```

## 函数不区分大小写

函数名称不区分大小写，例如`count()`、`COUNT()`、`couNT()`是等价的。

```ngql
nebula> WITH [NULL, 1, 1, 2, 2] As a \
        UNWIND a AS b \
        RETURN count(b), COUNT(*), couNT(DISTINCT b);
+----------+----------+-------------------+
| count(b) | COUNT(*) | couNT(distinct b) |
+----------+----------+-------------------+
| 4        | 5        | 2                 |
+----------+----------+-------------------+
```
