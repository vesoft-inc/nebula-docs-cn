# 页面概览

本文介绍 Nebula Explorer 的基本组成，帮忙用户了解 Nebula Explorer 的各功能。

Nebula Explorer 由顶部导航栏、左侧导航栏、和画布三大模块组成。

![explorer-overview](https://docs-cdn.nebula-graph.com.cn/figures/explorer-overview_cn.png)

## 顶部导航栏

| 图标/元素                                                    | 说明                                                 |
| ------------------------------------------------------------ | ---------------------------------------------------- |
| **Explorer**                                                 | 可视化探索及分析数据。详情参见[开始探索](ex-ug-query-exploration.md)、[节点筛选](node-filtering.md)、[探索拓展](ex-ug-graph-exploration.md)。     |
| **Visual Query**                                             | 可视化构造场景进行数据查询。详情参见[可视化查询](12.query-visually.md)。           |
| ![create_schema](https://docs-cdn.nebula-graph.com.cn/figures/studio-nav-schema.png) | 对 Nebula Graph 图空间进行管理。详情参见[创建 Schema](10.create-schema.md)。       |
| ![import_data](https://docs-cdn.nebula-graph.com.cn/figures/studio-btn-download.png) | 将数据批量导入 Nebula Graph。详情参见[导入数据](11.import-data.md)。          |
| ![Console](https://docs-cdn.nebula-graph.com.cn/figures/nav-console2.png) | 对 Nebula Graph 内的数据使用 nGQL 进行查询操作。详情参见[控制台](explorer-console.md)。 |
| ![language](https://docs-cdn.nebula-graph.com.cn/figures/navbar-language.png) | 选择 Nebula Explorer 页面的语言，支持中文和英文。    |
| ![help](https://docs-cdn.nebula-graph.com.cn/figures/navbar-help.png) | 帮助页面，指导和帮忙用户使用 Nebula Graph。          |
| ![clear_connection](https://docs-cdn.nebula-graph.com.cn/figures/image-icon10.png) | 显示内核版本并可以断开与 Nebula Explorer 的连接。    |


## 左侧导航栏

!!! note

    登录 Explorer 后，用户需选择并单击一个目标图空间，然后才可解锁左侧导航栏的查询及分析功能。详情参见[选择图空间](13.choose-graphspace.md)。

用户可以通过单击 Explorer 页面左侧的图标进行图数据导入、图数据分析与探索等操作。左侧导航栏的图标及描述如下：

| 图标  | 说明 |
| ----- | ---- |
| ![query](https://docs-cdn.nebula-graph.com.cn/figures/nav-query2_cn.png) | 输入 VID、Tag 和子图等信息后，匹配的数据会显示到画布上。更多信息，参见[查询方式](ex-ug-query-exploration.md)。     |
| ![filter](https://docs-cdn.nebula-graph.com.cn/figures/nav-filter_cn.png) | 对画布中显示的点进行过滤。更多信息，参见[节点筛选](node-filtering.md)。     |
| ![expand](https://docs-cdn.nebula-graph.com.cn/figures/nav-expand_cn.png) | 选择页面上的节点并进行自定义拓展，包括方向、步数、过滤条件等。更多信息，参见[探索拓展](ex-ug-graph-exploration.md)。    |
| ![commonNeighbor](https://docs-cdn.nebula-graph.com.cn/figures/nav-commonNeighbor_cn.png) | 选择页面上至少两个点并查看它们的共同邻居。更多信息，参见[探索拓展](ex-ug-graph-exploration.md)。     |
| ![findPath](https://docs-cdn.nebula-graph.com.cn/figures/nav-findPath_cn.png) | 查询起点到终点之间的所有路径、最短路径和非循环路径。更多信息，参见[探索拓展](ex-ug-graph-exploration.md)。     |
| ![propertyView](https://docs-cdn.nebula-graph.com.cn/figures/nav-propertyView_cn.png) | 选择是否显画布中的点或边的属性值。更多信息，参见[探索拓展](ex-ug-graph-exploration.md)。     |
| ![snapshot](https://docs-cdn.nebula-graph.com.cn/figures/snapshot-history_cn.png) | 查看历史快照信息。更多信息，参见[画布快照](canvas-operations/canvas-snapshot.md)。     |
| ![graphSpace](https://docs-cdn.nebula-graph.com.cn/figures/nav-graphSpace_cn.png) | 查看所有图空间，单击图空间可创建相应图空间的画布。更多信息，参见[选择图空间](13.choose-graphspace.md)。     |
| ![Help](https://docs-cdn.nebula-graph.com.cn/figures/nav-help_cn.png) | 查看 Explorer 操作文档、论坛内容等。     |
| ![Setup](https://docs-cdn.nebula-graph.com.cn/figures/nav-setup2.png) | 查看用户名和快捷键、修改语言设置、限制返回结果数量、清除 Explorer 链接等。|

## 画布

!!! note

    登录 Explorer 后，用户需选择并单击一个目标图空间，才可进入画布页面。详情参见[选择图空间](13.choose-graphspace.md)。

图数据可视化地展示在画布中。Explorer 的画布由以下部分组成：

- 顶部页签
- 可视化模式
- 数据存储
- 搜索框
- 多布局
- 缩略图
- 数据概览

更多信息，参见[画布操作](canvas-operations/canvas-overview.md)。
