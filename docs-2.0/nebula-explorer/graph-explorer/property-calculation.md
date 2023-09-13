# 属性计算

当画布中的点存在大量关系时，为了增强图的可读性和可分析性，可以将起点、终点、边类型相同的边进行聚合。聚合后的边可以对其中的某个属性进行计算并展示。

## 前提条件

画布中有[聚合边](../canvas-operations/visualization-mode.md)。

## 注意事项

- 当前仅支持求和计算。
- 只支持聚合 INT 类型的属性。
- 支持选择多个 Edge type 分别进行聚合。
- 支持选择多个属性分别进行聚合。
- 一条边只能显示一个聚合结果。可以将鼠标悬停在聚合边上查看所有结果。

## 操作步骤

### 方式 1

1. 在左侧导航栏，单击![propertyCalculation](https://docs-cdn.nebula-graph.com.cn/figures/icon-nav-propertyCalculation.png)图标，打开**属性计算**窗口。

2. 单击 **+** 号，设置边类型、属性和计算方式。可以选择多个属性分别进行聚合。

3. 单击**确认**。

单击 **+** 号可以增加更多 Edge type 的属性计算。

<img src="https://docs-cdn.nebula-graph.com.cn/figures/ec_expl_calculation_230913_cn.png" width="1200" alt="图探索属性计算截屏">

### 方式 2

1. 在画布中的聚合边上单击鼠标右键，选择**属性计算**。

2. 设置属性和计算方式。

3. 单击**确认**。
