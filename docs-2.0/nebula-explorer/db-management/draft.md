# Schema 草图

{{explorer.name}}支持 Schema 草图功能。用户可以在画板上自行设计 Schema，可以直观展示点边关系，设计完成后可以将 Schema 应用到指定图空间。

## 功能说明

- 图形化设计 Schema。
- 应用 Schema 到指定图空间。
- 导出 Schema 为 PNG 格式图片。

## 入口

在顶部导航栏里，单击 ![Template](https://docs-cdn.nebula-graph.com.cn/figures/sketch_cion_221018.png) 图标。

## 设计 Schema

以`basketballplayer`的 Schema 为例，说明如何设计 Schema。

1. 在页面左上角单击**新建**。
2. 在画布下方选择合适颜色的 Tag 标签，按住左键拖拽至画布中，创建一个 Tag。
3. 单击 Tag，在右侧填写标签名称`player`、描述，并且添加属性`name`和`age`。
4. 再次创建一个 Tag，标签名称为`team`，属性为`name`。
5. 从 Tag `player`上的锚点连接至 Tag `team`的锚点，单击生成的边，在右侧填写边类型名称`serve`，并且添加属性`start_year`和`end_year`。
6. 从 Tag `player`上的锚点连接至自身另一个锚点，单击生成的边，在右侧填写边类型名称`follow`，并且添加属性`degree`。
7. 设计完成后，在页面上方单击 ![setup](https://docs-cdn.nebula-graph.com.cn/figures/setup-220916.png) 修改草图名称，然后在右上角单击 ![save](https://docs-cdn.nebula-graph.com.cn/figures/workflow-saveAs-220623.png) 保存草图。

<img src="https://docs-cdn.nebula-graph.com.cn/figures/ec_expl_draft_230912_cn.png" width="1000" alt="图探索创建 Schema 草图截屏">

## 应用 Schema

1. 在页面左侧的**草图列表**内选择需要导入的 Schema 草图，然后在右上角单击**应用到图空间**。
2. 选择将 Schema 导入新建图空间或者已创建的图空间，单击**确认**。

  !!! note

      - 创建图空间的参数说明参见[CREATE SPACE](../../3.ngql-guide/9.space-statements/1.create-space.md)。
      - 如果图空间中已有重名 Schema，导入操作会失败，并提示修改名称或更换图空间。

## 修改 Schema

在页面左侧的**草图列表**内选择需要修改的 Schema 草图，修改完成后在右上角单击 ![save](https://docs-cdn.nebula-graph.com.cn/figures/workflow-saveAs-220623.png) 保存。

!!! note

    已应用 Schema 的图空间**不会**同步修改。

## 删除 Schema

在页面左侧的**草图列表**内找到需要删除的 Schema 草图，在缩略图右上角单击**X**并确认即可删除。

## 导出 Schema

在页面右上角单击 ![data_output](https://docs-cdn.nebula-graph.com.cn/figures/explorer-btn-output.png) 可以导出 Schema 为 PNG 格式图片。
