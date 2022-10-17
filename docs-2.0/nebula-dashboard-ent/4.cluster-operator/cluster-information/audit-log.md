# 审计日志

NebulaGraph 企业版的审计日志功能可以将 Graph 服务接受到的所有操作进行分类存储。为便于用户查看审计日志，NebulaGraph Dashboard 企业版支持快速查看审计日志。

## 入口

1. 在 Dashboard 企业版顶部导航栏，单击**集群管理**。
2. 单击目标集群右侧**详情**。
3. 在左侧导航栏，单击**集群信息**->**审计日志**。

!!! note

    需要在配置文件内启用审计日志才能正常查看。如果 NebulaGraph 未开启审计日志，请根据页面提示单击**更新配置**修改相关参数。参数说明参见[NebulaGraph 审计日志](../../../5.configurations-and-logs/2.log-management/audit-log.md)。

## 查看审计日志

根据审计日志的存储方案，查看审计日志的方法不同：

- 存储方案为本地文件（`audit_log_handler = file`）

  默认展示所有 Graph 服务上的审计日志文件。可以在上方筛选主机或搜索文件名称。
  
  在文件名右侧`操作`列单击`查看日志`，默认展示最新 300 行的审计日志，以及审计日志的文件路径和最后修改时间。
  
  - 最多支持展示 1000 行审计日志。
  - 单击右上角**刷新**可以查看最新审计日志。
  - 支持复制窗口内日志内容、复制文件路径

- 存储方案为 Elasticsearch（`audit_log_handler = es`）

  需要设置提供 Elasticsearch 服务的 Kibana 平台地址，保存后单击**访问 Kibana**。跳转至 Kibana 平台后可以查看 Elasticsearch 上存储的审计日志。
