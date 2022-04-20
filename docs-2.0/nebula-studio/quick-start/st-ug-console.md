# 控制台界面

本文介绍 Studio 的控制台界面。

![控制台界面截图](https://docs-cdn.nebula-graph.com.cn/figures/st-ug-015-cn.png)

下表列出了控制台界面上的各种功能。

| 编号  |  功能 | 说明  |
| :-- | :--|   :--   |
|  1  |  工具栏   |  点击 **控制台** 页签进入控制台页面。 |
|  2  |  选择图空间  | 在 **当前图空间** 列表中选择一个图空间。 <br/> **说明**：Studio 不支持直接在输入框中运行 `USE <space_name>` 语句。  |
|  3  | 收藏夹 | 点击![save](https://docs-cdn.nebula-graph.com.cn/figures/studio-btn-save.png) 按钮，展开收藏夹，点击其中一个语句，输入框中即自动输入该语句。 |
|  4  |  历史清单   |  点击 ![history](https://docs-cdn.nebula-graph.com.cn/figures/studio-btn-history.png) 按钮，在语句运行记录列表里，点击其中一个语句，输入框中即自动输入该语句。列表里提供最近 15 次语句运行记录。  |
|  5  |  清空输入框  | 点击 ![clear](https://docs-cdn.nebula-graph.com.cn/figures/studio-btn-clear.png) 按钮，清空输入框中已经输入的内容。   |
|  6  |  运行  |  在输入框中输入 nGQL 语句后，点击 ![play](https://docs-cdn.nebula-graph.com.cn/figures/studio-btn-play.png) 按钮即开始运行语句。   |
|  7  |  自定义参数展示   | 点击 ![查询](https://docs-cdn.nebula-graph.com.cn/figures/down.png)按钮可展开自定义参数，用于参数化查询，详情信息可见[管理参数](../../nebula-console.md)。|
|  8  |  输入框   |  在输入框中输入 nGQL 语句后，点击 ![play](https://docs-cdn.nebula-graph.com.cn/figures/studio-btn-play.png) 按钮运行语句。用户可以同时输入多个语句同时运行，语句之间以 `;` 分隔。 |
|  9  |  语句运行状态   |  运行 nGQL 语句后，这里显示语句运行状态。如果语句运行成功，语句以绿色显示。如果语句运行失败，语句以红色显示。   |
|  10  | 添加到收藏夹 | 点击![save](https://docs-cdn.nebula-graph.com.cn/figures/studio-btn-save.png) 按钮，将语句存入收藏夹中，已收藏的语句该按钮以黄色展示。|
|  11  |  导出 CSV 文件或 PNG 格式图片 |  运行 nGQL 语句返回结果后，返回结果为表格形式时，点击 ![download](https://docs-cdn.nebula-graph.com.cn/figures/studio-btn-download.png) 按钮即能将结果以 CSV 文件的形式导出。切换到可视化窗口，点击 ![download](https://docs-cdn.nebula-graph.com.cn/figures/studio-btn-download.png) 按钮即能将结果以 CSV 文件或 PNG 图片的形式导出。   |
|  12  |  展开/隐藏执行结果  | 点击 ![up](https://docs-cdn.nebula-graph.com.cn/figures/studio-btn-up.png) 按钮，隐藏此条 nGQL 语句返回的结果或点击 ![down](https://docs-cdn.nebula-graph.com.cn/figures/studio-btn-down.png)按钮，展开此条 nGQL 语句返回的结果. |
|  13  |  关闭执行结果  | 点击 ![close](https://docs-cdn.nebula-graph.com.cn/figures/studio-btn-close.png)按钮，关闭此条 nGQL 语句返回的结果。 |
|  14  |  表格窗口 |  显示语句运行结果。如果语句会返回结果，窗口会以表格形式呈现返回的结果。 |
|  15  |  可视化窗口 | 显示语句运行结果。如果语句会返回完整的点边结果，窗口会以可视化形式呈现返回的结果。点击右方 ![expand](https://docs-cdn.nebula-graph.com.cn/figures/studio-btn-back.png)按钮，展开数据概览面板。 |