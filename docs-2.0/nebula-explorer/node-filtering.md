# 节点筛选

用户可通过一组或多组筛选条件对画布中显示的点进行过滤。筛选条件包括：Tag、属性、运算符、值。

!!! note

    每一组筛选条件只针对带此 Tag 的数据，满足条件会被自动添加选中状态，不满足则置灰。其他 Tag 数据状态不受影响。 

## 前提条件

使用**节点筛选**功能前，确保画布中有点数据。具体操作，参见[开始探索](ex-ug-query-exploration.md)。

## 示例

以下示例为筛选画布中年龄大于 33 岁的球员。

1. 在左侧导航栏中，单击**节点筛选**图标![node-filter](https://docs-cdn.nebula-graph.com.cn/figures/nav-filter.png)。
2. 单击**添加筛选条件**，然后填入对应值（如下图所示）。
3. （可选）重复第二步骤，添加多个筛选条件。
4. 打开**启动筛选**开关。

![](https://docs-cdn.nebula-graph.com.cn/figures/node-filtering.png)
