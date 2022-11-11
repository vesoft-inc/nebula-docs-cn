# 控制台

Explorer 的控制台功能允许用户手动输入 nGQL 语句，并可视化地呈现查询结果。本文介绍控制台的界面。

## 入口

在顶部导航栏里，单击 ![console](https://docs-cdn.nebula-graph.com.cn/figures/nav-console2.png) 图标。

## 页面介绍

![控制台界面截图](https://docs-cdn.nebula-graph.com.cn/figures/console_ovewview_221111_cn.png)

下表列出了控制台界面上的各种功能。

| 编号  |  功能 | 说明  |
| :-- | :--|   :--   |
|  1  |  选择图空间  | 选择执行 nGQL 的图空间。不支持在控制台执行`USE <space_name>`语句切换图空间。  |
|  2  | 收藏夹 | 点击![save](https://docs-cdn.nebula-graph.com.cn/figures/studio-btn-save.png) 按钮，展开收藏夹，点击其中一个语句，输入框中即自动输入该语句。 |
|  3  |  历史清单   |  点击 ![history](https://docs-cdn.nebula-graph.com.cn/figures/studio-btn-history.png) 按钮，在语句运行记录列表里，点击其中一个语句，输入框中即自动输入该语句。列表里提供最近 15 次语句运行记录。  |
|  4  |  清空输入框  | 点击 ![clear](https://docs-cdn.nebula-graph.com.cn/figures/studio-btn-clear.png) 按钮，清空输入框中已经输入的内容。   |
|  5  |  运行  |  在输入框中输入 nGQL 语句后，点击 ![play](https://docs-cdn.nebula-graph.com.cn/figures/studio-btn-play.png) 按钮即开始运行语句。   |
|  6  |  保存为模板  |  将输入框中输入的 nGQL 语句保存为模板。详情参见[查询语句模板](ngql-template.md)。   |
|  7  |  输入框   |  输入 nGQL 语句的区域。可以同时输入多个语句按顺序执行，语句之间以 `;` 分隔。支持用`//`添加注释。 |
|  8  |  自定义参数展示   | 点击 ![查询](https://docs-cdn.nebula-graph.com.cn/figures/down.png)按钮可展开查看自定义参数，用于参数化查询。详情信息可见[管理参数](../../nebula-console.md)。|
|  9  |  语句运行状态   |  运行 nGQL 语句后，这里显示语句运行状态。如果语句运行成功，语句以绿色显示。如果语句运行失败，语句以红色显示。   |
|  10  | 添加到收藏夹 | 点击![save](https://docs-cdn.nebula-graph.com.cn/figures/studio-btn-save.png) 按钮，将语句存入收藏夹中，已收藏的语句该按钮以黄色展示。|
|  11  |  导出 CSV 文件或 PNG 格式图片 |  运行 nGQL 语句返回结果后，返回结果为表格形式时，点击 ![download](https://docs-cdn.nebula-graph.com.cn/figures/studio-btn-download.png) 按钮即能将结果以 CSV 文件的形式导出。</br>切换到可视化窗口，点击 ![download](https://docs-cdn.nebula-graph.com.cn/figures/studio-btn-download.png) 按钮即能将结果以 CSV 文件或 PNG 图片的形式导出。   |
|  12  |  展开/隐藏执行结果  | 点击 ![up](https://docs-cdn.nebula-graph.com.cn/figures/studio-btn-up.png) 按钮，隐藏此条 nGQL 语句返回的结果。 |
|  13  |  关闭执行结果  | 点击 ![close](https://docs-cdn.nebula-graph.com.cn/figures/studio-btn-close.png)按钮，关闭此条 nGQL 语句返回的结果。 |
|  14  |  表格窗口 |  显示语句运行结果。如果语句会返回结果，窗口会以表格形式呈现返回的结果。 |
|  15  |  可视化窗口 | 显示语句运行结果。如果语句会返回完整的点边结果，窗口会以可视化形式呈现返回的结果。点击右方 ![expand](https://docs-cdn.nebula-graph.com.cn/figures/studio-btn-back.png)按钮，展开数据概览面板。 |