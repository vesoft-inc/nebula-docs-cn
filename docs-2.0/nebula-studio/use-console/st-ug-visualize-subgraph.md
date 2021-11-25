# 查看子图

在 Studio 里，用户可以在 **控制台** 上运行 `FIND SHORTEST | ALL PATH` 语句查询得到指定点之间的所有路径或最短路径，然后再通过 **查看子图** 功能将查询得到的路径导入 **图探索** 进行可视化展示。

关于 `FIND SHORTEST | ALL PATH` 语句的详细信息，参考 [nGQL 用户手册](../../3.ngql-guide/16.subgraph-and-path/2.find-path.md "点击前往 Nebula Graph 网站")。

## 支持版本

Studio v{{ studio.release }} 及以后版本。请更新版本，详细操作参考[版本更新](../about-studio/st-ug-check-updates.md)。

## 前提条件

在 **控制台** 上运行 `FIND PATH` 语句并查看子图之前，用户需要确认以下信息：

- Studio 版本为 v{{ studio.release }} 及以后版本。
- Studio 已经连接到 Nebula Graph 数据库。详细信息参考[连接数据库](../deploy-connect/st-ug-connect.md)。
- 已经导入数据集。详细操作参考[导入数据](../quick-start/st-ug-import-data.md)。

!!! Note

    用户也可以在 [Studio](https://playground.nebula-graph.com.cn/explore) 在线使用查看子图功能。

## 操作步骤

按以下步骤在 **控制台** 运行 `FIND PATH` 语句并将结果导入 **图探索**：

1. 在工具栏里，点击 **控制台** 页签。

2. 在 **当前 Space** 中选择一个图空间。在本示例中，选择 **basketballplayer**。

3. 在命令行中，输入 `FIND SHORTEST PATH` 或者 `FIND ALL PATH` 语句，并点击 ![表示运行的图标](../figs/st-ug-008.png "Run 图标") 图标。

   查询语句示例如下：

   ```nGQL
   nebula> FIND ALL PATH FROM "player114" to "player100" OVER follow;
   ```

   查询得到如下图所示路径信息。

   ![结果窗口显示返回的路径信息](../figs/st-ug-045-1.png "返回的路径结果")

4. 点击 **查看子图** 按钮。

5. 如果 **图探索** 页面此前已有数据，选择一种数据插入方式：

   - **增量插入**：在画图板原来的数据基础上插入新的数据。

   - **清除插入**：清除画图板上原来的数据后，再插入新的数据。

数据插入成功后，用户可以看到查询结果的可视化表现。并支持在页面中，完成点的拓展、移动画布、修改点的颜色及 icon、显示点边属性等操作。

![在画布上显示返回的路径结果](../figs/st-ug-046.png "路径结果的可视化表现")

## 后续操作

数据导入图探索后，用户可以对数据进行拓展分析。
