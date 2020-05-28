# Storage 接口

在本文档中，我们将介绍 **Nebula Graph** 的 Java 客户端接口。

## Storage 客户端

一段说明
给个例子

## Async 客户端

一段说明
给个例子

## 扫边接口（ScanEdgeInSpace）

扫描所选分区的所有边。使用扫边接口前请先插入数据，或运行 `GraphClientExample` 以插入数据。schema 如下：

```ngql
nebula> CREATE EDGE select(grade int);

# 插入边
nebula> INSERT EDGE select(grade) VALUES 201 -> 102:(3);
```

## 扫点接口（ScanVertexInPart）

扫描所选分区的所有点。使用扫边接口前请先插入数据，或运行 `GraphClientExample` 以插入数据。schema 如下：

```ngql
nebula> CREATE TAG student(name string, age int, gender string);

# 插入点
nebula> INSERT VERTEX student(name, age, gender) VALUES 201:("a", 16, "female");
```
