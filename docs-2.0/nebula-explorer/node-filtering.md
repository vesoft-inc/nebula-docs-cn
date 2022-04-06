# 节点筛选

用户可以根据过滤条件筛选画布中的点和边。支持仅通过 Tag 或通过一组或多组筛选条件对画布中显示的点进行过滤。

## 前提条件

使用**节点筛选**功能前，确保画布中有点数据。具体操作，参见[开始探索](ex-ug-query-exploration.md)。

## 使用说明

- 使用 **Tag** 过滤画布中的点及关联的边时：

  - **筛选条件**面板显示图空间中的所有 Tag。

  - Tag 图例被置灰且画布中的对应 Tag 的点及关联的边会被隐藏。

  - 对于多 Tag 的点，如果其任一 Tag 被选中为过滤项，则该点会被隐藏。

  - 支持通过搜索框输入对应的 Tag 进行筛选。

- 使用**筛选条件**过滤画布中的点及关联的边时：

  - 每一组筛选条件只针对带此 Tag 的数据，筛选条件包括：Tag、属性、运算符、值。如满足条件，画布中的点会被自动添加选中状态，不满足条件的点及关联的边可被设置为**隐藏**或**置灰**。其他 Tag 数据状态不受影响。

  - 如果筛选条件中配置了已被选中（置灰状态）的 Tag，画布中不会展示对应的数据。

- 每次进行**节点筛选**操作时，只能选择一个 Tag。如果要过滤多个 Tag，需要多次进行**添加筛选条件**操作。

## 示例

### 示例1 过滤画布中 Tag 为 **player** 的所有点

1. 在左侧导航栏中，单击**节点筛选**图标![node-filter](https://docs-cdn.nebula-graph.com.cn/figures/nav-filter.png)。
2. 在**筛选条件**面板中，单击**player**。
3. 画布中显示只有 Tag 为 team 的点。
  ![node-filter](https://docs-cdn.nebula-graph.com.cn/figures/vertex-filtering-example1_cn.png)

    上图中被过滤出的橙色点即 Tag 为 team 的点。

### 示例2 筛选画布中年龄大于 33 岁的球员

1. 在左侧导航栏中，单击**节点筛选**图标![node-filter](https://docs-cdn.nebula-graph.com.cn/figures/nav-filter.png)。
2. 单击**添加筛选条件**，然后设置筛选项（本示例设置的值分别为`player`、`age`、`>`、`33`）。
3. （可选）重复第二步骤，添加多个筛选条件（本示例只需添加一次）。
4. 单击**隐藏**将不满足过滤条件的点隐藏，或者单击**置灰**将不满足过滤条件的点显示为灰色（本示例设置为**置灰**）。
4. 打开**启动筛选**开关。

    ![filter_node](https://docs-cdn.nebula-graph.com.cn/figures/vertex-filtering-example2_cn.png)


