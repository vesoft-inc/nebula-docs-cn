# 图计算

为了更好地挖掘、分析图数据，用户可以基于画布中的点边进行图计算，并直接查看图计算结果。

!!! note

    本功能仅对画布中现存的点进行图计算，如果需要进行复杂图计算，推荐使用 [Workflow](../workflow/workflows.md) 进行复杂的可视化图计算。

## 前提条件

确保画布中有图计算所需的点边数据。具体操作，参见[开始探索](ex-ug-query-exploration.md)。

## 操作步骤

1. 在左侧导航栏，单击![graph-algorithm](https://docs-cdn.nebula-graph.com.cn/figures/rightclickmenu-graphCalculation.png)图标，打开**图计算**窗口。

2. 选择算法并设置相关参数。关于算法和参数的说明，请参见[算法简介](../../graph-computing/algorithm-description.md)。

3. 单击**运行**，画布下方会弹出图计算结果。

4. 在结果页面可以：

   - 单击**自动补齐一度路径关系**将画布中所有点之间的一度路径关系补齐。
   - 单击**导出CSV**下载 CSV 格式的图计算结果文件。

<img src="https://docs-cdn.nebula-graph.com.cn/figures/ec_expl_algorithm_230913_cn.png" width="1200" alt="图探索子图计算截屏">