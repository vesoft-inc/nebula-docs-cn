# 开始探索

!!! note

    使用查询功能前，需要选中并单击目标图空间。

!!! compatibility "历史版本兼容性"

    针对 3.0.0 以下版本的 Nebula Graph，需要创建索引后才可以使用查询功能。更多信息，参见[创建索引](../3.ngql-guide/14.native-index-statements/1.create-native-index.md)。

用户进行图数据的探索和分析前，首先需要先单击**开始**图标![query](https://docs-cdn.nebula-graph.com.cn/figures/nav-query2.png)然后查询目标数据。查询到的数据会显示在画布中。查询方式如下：

- VID 查询
- Tag 查询
- 子图查询

## VID 查询

用户可输入点的 ID（VID）查询目标点然后基于目标点进行探索和分析。

支持手动输入、随机导入、文件导入 VID。

!!! note

    - 输入或者导入的数据必须存在于图数据库中。
    - 查询区域中每行仅支持填入一个 VID。

以下以图空间`nba`及相关数据为例演示如何查询数据。

![VID QUERY](https://docs-cdn.nebula-graph.com.cn/figures/vid_query.gif)

## Tag 查询

!!! note

使用 **Tag 查询** 方式查询数据，确保对应的图空间中已存在相应的 Tag 和索引。更多信息，参见[创建 Tag](../3.ngql-guide/10.tag-statements/1.create-tag.md) 和[创建索引](../3.ngql-guide/14.native-index-statements/1.create-native-index.md)。

用户可以对输出的结果进行数量上的限制和对结果进行过滤。

以下查询 10 个年龄大于 30 岁，且不等于 40 岁的球员。

![tag](https://docs-cdn.nebula-graph.com.cn/figures/query_tag.png)

## 子图查询

**子图查询**方式的必选值为 VID。用户可以输入一个或多个 VID，指定查询的步数、边类型及流入流出的方向查询子图数据。以下给出 VID 值为 `Kings`和`Suns`，步数为`2` ，边类型为`server`和`like`的入边的示例。

!!! note

    当输入多个 VID 时，VID 之间以`Enter`键隔开。

![tag](https://docs-cdn.nebula-graph.com.cn/figures/query_subgraph.png)