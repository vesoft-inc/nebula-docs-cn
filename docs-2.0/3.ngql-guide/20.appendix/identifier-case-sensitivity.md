# 大小写区分

## 标识符区分大小写

以下语句会出现错误，因为`my_space`和`MY_SPACE`是两个不同的图空间。

```ngql
nebula> CREATE SPACE my_space;
nebula> use MY_SPACE;
[ERROR (-8)]: SpaceNotFound:
```

## 关键字和保留字不区分大小写

以下语句是等价的，因为`show`和`paces`是关键字。

```ngql
nebula> show spaces;  
nebula> SHOW SPACES;
nebula> SHOW spaces;
nebula> show SPACES;
```