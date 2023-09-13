# 页面概览

本文介绍{{explorer.name}}的基本组成，帮忙用户了解{{explorer.name}}的各功能。

{{explorer.name}}由顶部导航栏、左侧导航栏、和画布三大模块组成。

<img src="https://docs-cdn.nebula-graph.com.cn/figures/ec_expl_overview_230912_cn.png" width="1200" alt="图探索页面概览截屏">

## 顶部导航栏

| 图标/元素                                                    | 说明                                                 |
| ------------------------------------------------------------ | ---------------------------------------------------- |
| **{{explorer.name}}**                                                 | 可视化探索及分析数据。详情参见[开始探索](graph-explorer/ex-ug-query-exploration.md)、[节点筛选](graph-explorer/node-filtering.md)、[探索拓展](graph-explorer/ex-ug-graph-exploration.md)、[图计算](graph-explorer/graph-algorithm.md)。     |
| **Visual Query**                                             | 可视化构造场景进行数据查询。详情参见[可视化查询](12.query-visually.md)。           |
| **Workflow**                                                 | 可视化构造自定义工作流进行复杂图计算。需要在 ![setting](https://docs-cdn.nebula-graph.com.cn/figures/navbar-setting-0105.png) 里开启工作流才能显示 Workflow 页面。详情参见[工作流简介](workflow/workflows.md)。|
| ![Schema_drafting](https://docs-cdn.nebula-graph.com.cn/figures/schema_drafting_221110.png) | 在画板上自行设计 Schema，可以直观展示点边关系。详情参见[Schema 草图](db-management/draft.md)。|
| ![create_schema](https://docs-cdn.nebula-graph.com.cn/figures/studio-nav-schema.png) | 对{{nebula.name}}图空间进行管理。详情参见[创建 Schema](db-management/10.create-schema.md)。       |
| ![import_data](https://docs-cdn.nebula-graph.com.cn/figures/studio-btn-download.png) | 将数据批量导入{{nebula.name}}。详情参见[导入数据](db-management/11.import-data.md)。          |
| ![Console](https://docs-cdn.nebula-graph.com.cn/figures/nav-console2.png) | 对{{nebula.name}}内的数据使用 nGQL 进行查询操作。详情参见[控制台](db-management/explorer-console.md)。 |
| ![Template](https://docs-cdn.nebula-graph.com.cn/figures/icon-navbar-queryTemplate.png)| nGQL 语句的模板列表。详情参见[查询语句模板](db-management/ngql-template.md)。|
| ![db_user_management](https://docs-cdn.nebula-graph.com.cn/figures/db_user_management_221024.png) | 数据库用户管理。详情参见[数据库用户管理](db-management/dbuser_management.md)。   |
| ![setting](https://docs-cdn.nebula-graph.com.cn/figures/navbar-setting-0105.png) | 全局设置。可以设置{{explorer.name}}页面的语言、开启 Beta 功能、画布查询结果最大数量等。    |
| ![help](https://docs-cdn.nebula-graph.com.cn/figures/navbar-help.png) | 帮助页面，指导和帮忙用户使用{{nebula.name}}。          |
| ![feedback](https://docs-cdn.nebula-graph.com.cn/figures/navbar-feedback-230105.png) | 反馈页面。可以反馈故障、提交建议、参与调研或联系{{nebula.name}}团队。          |
| ![clear_connection](https://docs-cdn.nebula-graph.com.cn/figures/session_221024.png) | 显示连接信息和版本信息。支持修改密码和退出登录。    |

## 左侧导航栏

!!! note

    登录{{explorer.name}}后，用户需选择并单击一个目标图空间，然后才可解锁左侧导航栏的查询及分析功能。详情参见[选择图空间](graph-explorer/13.choose-graphspace.md)。

用户可以通过单击{{explorer.name}}页面左侧的图标进行图数据导入、图数据分析与探索等操作。左侧导航栏的图标及描述如下：

| 图标  | 说明 |
| ----- | ---- |
| ![query](https://docs-cdn.nebula-graph.com.cn/figures/nav-query2_cn.png) | 输入 VID、Tag 和子图等信息后，匹配的数据会显示到画布上。更多信息，参见[查询方式](graph-explorer/ex-ug-query-exploration.md)。     |
| ![filter](https://docs-cdn.nebula-graph.com.cn/figures/nav-filter_cn.png) | 对画布中显示的点进行过滤。更多信息，参见[节点筛选](graph-explorer/node-filtering.md)。     |
| ![expand](https://docs-cdn.nebula-graph.com.cn/figures/nav-expand_cn.png) | 选择页面上的节点并进行自定义拓展，包括方向、步数、过滤条件等。更多信息，参见[探索拓展](graph-explorer/ex-ug-graph-exploration.md)。    |
| ![commonNeighbor](https://docs-cdn.nebula-graph.com.cn/figures/nav-commonNeighbor_cn.png) | 选择页面上至少两个点并查看它们的共同邻居。更多信息，参见[探索拓展](graph-explorer/ex-ug-graph-exploration.md)。     |
| ![findPath](https://docs-cdn.nebula-graph.com.cn/figures/nav-findPath_cn.png) | 查询起点到终点之间的所有路径、最短路径和非循环路径。更多信息，参见[探索拓展](graph-explorer/ex-ug-graph-exploration.md)。     |
| ![propertyView](https://docs-cdn.nebula-graph.com.cn/figures/nav-propertyView_cn.png) | 选择是否显画布中的点或边的属性值。更多信息，参见[探索拓展](graph-explorer/graph-algorithm.md)。     |
| ![graph-algorithm](https://docs-cdn.nebula-graph.com.cn/figures/rightclickmenu-graphCalculation.png)| 基于画布中的点边进行图计算。更多信息，参见[图计算](graph-explorer/ex-ug-graph-exploration.md)。|
| ![propertyCalculation](https://docs-cdn.nebula-graph.com.cn/figures/icon-nav-propertyCalculation.png)| 基于画布中已聚合的边进行属性计算。更多信息，参见[属性计算](graph-explorer/property-calculation.md)。 |
| ![snapshot](https://docs-cdn.nebula-graph.com.cn/figures/snapshot-history_cn.png) | 查看历史快照信息。更多信息，参见[画布快照](canvas-operations/canvas-snapshot.md)。     |
| ![graphSpace](https://docs-cdn.nebula-graph.com.cn/figures/nav-graphSpace_cn.png) | 查看所有图空间，单击图空间可创建相应图空间的画布。更多信息，参见[选择图空间](graph-explorer/13.choose-graphspace.md)。     |

## 画布

!!! note

    登录{{explorer.name}}后，用户需选择并单击一个目标图空间，才可进入画布页面。详情参见[选择图空间](graph-explorer/13.choose-graphspace.md)。

图数据可视化地展示在画布中。{{explorer.name}}的画布由以下部分组成：

- 顶部页签
- 可视化模式
- 数据存储
- 搜索框
- 多布局
- 缩略图
- 数据概览

更多信息，参见[画布操作](canvas-operations/canvas-overview.md)。
