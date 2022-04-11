# 画布概览

用户可在画布中可视化地探索图数据。本文主要介绍画布的组成及相关功能。

画布概览图如下：

![canvas](../figs/canvas-overview.png)

## 顶部页签

用户可以通过单击画布顶部加号![canvas_tab](../figs/list-add.png)图标同时操作多个画布。

![canvas_overview](../figs/canvas-graphspace.png)

- 不同画布上的数据可以来自同一个图空间也可以来自不同的图空间。
- 除了最左边页签的第一个画布外，用户可以自定义画布的名称。

## 可视化模式

用户可以选择 **2D 模式**和 **3D 模式**可视化地在画布上探索图数据。更多信息，参见[可视化模式](visualization-mode.md)。

## 数据存储

用户可以通过创建快照，或以图片、CSV 文件的方式导出画布以存储当前画布数据。

在页面右上方：

- 单击![snapshot](../figs/graph-snapshot.png)创建快照。更多信息，参见[画布快照](canvas-snapshot.md)。
- 单击![PNG](../figs/topbar-exportPNG.png)以图片形式存储画布数据。
- 单击![CSV](../figs/topbar-exportCSV.png)以 CSV 文件的方式存储画布数据。


## 搜索框

在页面左上方的搜索框中，输入 VID 或者 Tag 的属性值定位目标点。

## 多布局

Explorer 支持 6 种布局方式展示画布上的数据之间的关系。

| 力导向图 | 层次图 | 环形图 | 网格  | 神经网络 | 辐射  |
| -------- | ------ | ------ | ----- | -------- | ----- |
| ![graphView](../figs/Thumbnail-graphView.png)    | ![treeView](../figs/Thumbnail-treeView.png)  | ![sphereView](../figs/Thumbnail-sphereView.png)  | ![grid](../figs/Thumbnail-Grid.png) | ![neural](../figs/Thumbnail-neuralNetwork.png)    | ![radial](../figs/Thumbnail-Radial.png) |

![layouts](../figs/layout.gif)

## 缩略图

全屏展示画布中的图，收起缩略图，缩小或放大画布中的图等。同时在缩略图的左下角显示了画布中的图占总图的百分比。

![](../figs/thumbnail.png)

## 数据概览

在页面右侧，单击![list-left](../figs/list-left.png)展开数据概览面板。

![dataView](../figs/dataview.png)

- 可以在数据概览面板中看到画布中的 Tag 数、Edge type 数，及对应的点和边的数量。
- 在数据概览面板，单击 Tag 颜色图标，可自定义 Tag 相同的点的颜色、尺寸、图标。

  !!! note
        Tag 完全相同的 VID 点的颜色相同。在画布中右键单击单个点可手动修改一个点的样式。
