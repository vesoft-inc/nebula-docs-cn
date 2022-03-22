# 管理快照

Explorer 的快照功能可保存图探索得到的可视化结果，以便再次打开浏览器时还原保存的图数据。

## 创建快照

1. 在画布右上角，单击相机![snapshot](https://docs-cdn.nebula-graph.com.cn/figures/graph-snapshot.png)图标。
2. 填写快照名称和备注（选填）。
3. 单击**提交**。

!!! note

    已创建的快照被存放在历史快照中。更多信息，参见下文。


## 历史快照

在 Explorer 页面左侧导航栏，单击![snapshot_history](https://docs-cdn.nebula-graph.com.cn/figures/snapshot-history.png)图标进入历史快照列表页面。用户可切换图空间查看相应图空间的历史快照，还可以导入历史快照至画布，下载历史快照至本地，以及删除快照。

在目标历史快照右侧的**操作**列下：

- 单击![snapshot_import](https://docs-cdn.nebula-graph.com.cn/figures/snapshot-import.png)导入历史快照至新画布中。
- 单击![snapshot_export](https://docs-cdn.nebula-graph.com.cn/figures/snapshot-export.png)以 JSON 的格式下载历史快照至本地。
- 单击![snapshot_delete](https://docs-cdn.nebula-graph.com.cn/figures/snapshot-delete.png)删除历史快照。

在历史快照列表左上方，单击**导入快照**可导入之前下载的 JSON 格式文件至快照列表中，以便用户之间离线共享快照数据。系统会根据 JSON 文件中记录的图空间信息将导入的快照自动放置于相应的图空间中。

!!! note

    目前最多存储 50 个历史快照。 

