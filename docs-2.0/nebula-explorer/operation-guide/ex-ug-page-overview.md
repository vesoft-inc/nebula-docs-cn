# 页面概览

本文主要介绍 Explorer 的主页面。

## 概览

![Explorer](../figs/ex-ug-006.png)
Explorer 的主页面分为五个部分：

- 标签栏
- 侧边栏
- 画布
- 缩略图
- 关系列表

## 标签栏

- 导出图形：支持导出当前视图的 CSV 文件或 SVG（图片）文件。

## 侧边栏

侧边栏包括四个部分，用户可以点击按钮对图进行探索、修改画布上点的内容等等。

- 查询探索：在进行探索之前，用户需要在查询数据并显示在画布中。

- 画布操作：包括框选画布中的点、拖动画布、选中多条点边功能。

- 图探索拓展：包括对点的拓展、查找两个点的共同邻居、查找两个点的路径、显示属性切换等功能。

- 删除及撤销：对画布中显示的数据删除、撤回上一步操作。

- 设置和帮助：切换图空间、查找帮助、修改设置等。

### 查询探索

- 开始：单击 ![query](../figs/nav-query.png)图标，通过VID、Tag和子图，查询数据并显示到页面上。

### 画布操作

- 框选模式：单击![frameSelect](../figs/nav-frameSelect.png) 图标，支持框选画布中的点和边。

- 拖动画布：单击![moveCanvas](../figs/nav-moveCanvas.png) 图标，支持拖动画布的位置。

- 选中多条点边：单击![singleSelect](../figs/nav-singleSelect.png) 图标，可以方便的点击画布中的点和边，单击空白处取消选择。

### 图探索扩展

- 拓展：单击 ![expand](../figs/rightclickmenu-expand.png)图标，选择页面上的节点并进行自定义拓展，包括拓展方向、拓展步数、过滤条件等。
- 共同邻居：单击 ![commonNeighbor](../figs/rightclickmenu-commonNeighbor.png)图标，选择页面上 2 个点并查看它们的共同邻居。
- 路径查询：单击 ![findPath](../figs/rightclickmenu-findPath.png)图标，可以查询起点到终点之间的 `all paths` 、 `Shortest path` 或者是 `Noloop path` 的路径。
- 查看属性：单击 ![propertyView](../figs/nav-propertyView.png)图标，选择是否显示画板中的点或边的属性值。

### 删除及撤销

- 隐藏：单击![miss](../figs/nav-miss.png) 图标，可以隐藏画板中选中的点。
- 隐藏其他：单击![missreverse](../figs/nav-missReverse.png) 图标，可以隐藏画布中未选择的所有点。
- 撤销：单击 ![Revoke](../figs/nav-Revoke.png)图标，撤销上一步操作。

### 设置及帮助

- 选择图空间：单击 ![graphSpace](../figs/nav-graphSpace.png)图标，切换当前图空间。
- 帮助：单击 ![help](../figs/nav-help.png)图标，查看更多信息。
- 设置：单击 ![setup](../figs/nav-setup.png)图标，可以查看用户名和快捷键、修改语言设置、清除 Explorer 链接等。
## 画布

画布主要分为：

- 图：显示通过VID、Tag或子图查询的数据。

- 点边概览：默认隐藏，在当前画布选中点和边时才显示。点击如图标识，用户可以打开菜单，查看当前子图中选中的点和边的详细数据。

  ![review](../figs/ex-ug-027.png)

更多详细操作参考 [画布操作](../operation-guide/ex-ug-canvas.md)。

## 缩略图

用户可以通过缩略图上的按钮，完成图模式的切换，全屏展示画布中的图，收起缩略图，缩小或放大画布中的图等。同时在缩略图的左下角显示了画布中的图占总图的百分比。

- 图模式切换：用户可以切换画布中图的展示模式。

  | 图标 | ![force](../figs/Thumbnail-graphView.png) | ![dagre](../figs/Thumbnail-treeView.png) | ![circular](../figs/Thumbnail-sphereView.png) | 
  | ---- | ---- |----| ----|
  | 展示模式 | force（力导向图） | dagre（层次图） | circular（环形图） |
## 关系列表

点击右侧的 ![unfold](../figs/sidebar-unfold.png)图标，用户可以打开菜单，查看画板中 Tag 和 Edge 的数量、搜索 Tag 和 Edge ，同时也支持修改点的颜色和图标。