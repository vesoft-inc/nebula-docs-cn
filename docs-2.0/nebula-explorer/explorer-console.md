# 控制台

Explorer 的控制台功能允许用户手动输入 nGQL 语句，并将查询结果导入 Explorer 的画布中进行可视化呈现。

!!! note

    使用控制台功能前，确保用户已选择目标图空间。

## 输入 nGQL 语句

1. 在左侧导航栏，单击![console_input](figs/nav-console.png)。
2. 在控制台页面的输入框中，填写 nGQL 查询语句。更多信息，参见 [nGQL 命令汇总](../2.quick-start/6.cheatsheet-for-ngql-command.md)。
3. 单击![run](figs/console_run.png)图标。
4. （可选）单击![history](figs/console_history.png)查看历史执行的命令。
5. （可选）单击![clear](figs/console_delete.png)清除当前输入框中的语句。

## nGQL 语句结果展示

在控制台页面的下方区域，显示执行命令的输出结果。

结果以表格的形式展现，用户可单击**导出 CSV 文件**将表格的显示的数据保存至本地。

在表格最下方显示执行命令的耗时，单位秒（s）。

## 导入 nGQL 语句结果至画布

可以将查询的结果直接导入至画布中。单击**查看子图**：

- **清除插入**：清除画布中的数据，然后插入查询结果的数据至画布中。
- **增量插入**：在画布的数据基础上，新增查询结果的数据至画布中。画布中相同的数据会被覆盖。


