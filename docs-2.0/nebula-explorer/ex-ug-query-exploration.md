# 开始探索

为了探索图数据，用户需要查询出一些初始数据，在这些初始数据的基础上，才能进一步的分析、过滤。本文介绍如何查询初始数据。

## 前提条件

已选择目标图空间。详情参见[选择图空间](13.choose-graphspace.md)。

!!! compatibility "历史版本兼容性"

    针对 3.0.0 以下版本的 Nebula Graph，需要创建索引后才可以使用查询功能。更多信息，参见[创建索引](../3.ngql-guide/14.native-index-statements/1.create-native-index.md)。

## 操作步骤

在 Explorer 页面左侧单击**开始**图标![query](https://docs-cdn.nebula-graph.com.cn/figures/nav-query2_cn.png)然后查询数据。查询到的数据会显示在画布中。查询方式如下：

- VID 查询
- Tag 查询
- 子图查询

### VID 查询

用户可输入点的 ID（VID）查询目标点。

支持手动输入、随机导入、文件导入 VID。

!!! note

    查询区域中每行仅支持填入一个 VID，用回车键分隔。

下图以图空间`basketballplayer`及相关数据为例演示如何查询数据。

![VID QUERY](https://docs-cdn.nebula-graph.com.cn/figures/vid-query-22-04-06_cn.gif)

### Tag 查询

用户可以选择 Tag 和对应索引查询目标点，还可以设置结果数量限制和筛选条件。

!!! note

    请确保对应的图空间中已存在相应的 Tag 和索引，否则无法选择。详情参见[创建 Tag](../3.ngql-guide/10.tag-statements/1.create-tag.md) 和[创建索引](../3.ngql-guide/14.native-index-statements/1.create-native-index.md)。

下图为查询 10 个年龄大于 30 岁，且不等于 40 岁的球员的示例。

![tag](https://docs-cdn.nebula-graph.com.cn/figures/query_tag_cn.png)

### 子图查询

用户可以输入一个或多个 VID，指定查询的步数、边类型及流入流出的方向查询子图数据。VID 为必选项，可选项步数默认值为 1，边类型默认值为全部。

!!! note

    当输入多个 VID 时，VID 之间以`Enter`键隔开。

下图为 VID 值为 `Kings`和`Suns`，步数为`2` ，边类型为`server`和`like`的入边的示例。

![tag](https://docs-cdn.nebula-graph.com.cn/figures/query_subgraph_cn.png)
