# NebulaGraph Explorer 版本更新说明

## v3.1.0

- 功能
  - 增加[工作流](../../nebula-explorer/workflow/workflows.md)功能，支持将图查询和图计算任务串联起来构成工作流。
  - 增加[子图计算](../../nebula-explorer/graph-explorer/graph-algorithm.md)功能。
  - 增加基于画布的 [N 步节点检测](../../nebula-explorer/canvas-operations/visualization-mode.md)功能。

- 优化
  - 适配 NebulaGraph 3.2.0。
  - 支持持久化存储画布快照。将快照数据改为保存在服务端，以免用户清空浏览器数据等情况下快照丢失。
  - 支持在鸟瞰模式下[设置点边的最大展示数量](../../nebula-explorer/canvas-operations/visualization-mode.md)。
  - 2D 模式切换至 3D 模式时，默认增加 Z 轴上的分布，避免 3D 模式下的扁平感。

- 缺陷修复：
  - 修复导入快照时在当前图空间下无法查看的问题。
  - 修复打开太多页签时，新增的页签无法选中的问题。
  - 修复在控制台中执行`FIND PATH`语句时，`<edge_type_list>`中加入特殊字符导致执行出错的问题。
