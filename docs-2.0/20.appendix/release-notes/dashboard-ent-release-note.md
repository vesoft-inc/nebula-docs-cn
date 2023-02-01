# NebulaGraph Dashboard 企业版更新说明

## 企业版 v3.4.0

- 功能
  - 支持查看 NebulaGraph 集群[运行日志](../../nebula-dashboard-ent/4.cluster-operator/cluster-information/runtime-log.md)。
  - 支持查看 NebulaGraph 集群[审计日志](../../nebula-dashboard-ent/4.cluster-operator/cluster-information/audit-log.md)。
  - 支持[作业管理](../../nebula-dashboard-ent/4.cluster-operator/cluster-information/job-management.md)。
  - 备份恢复支持[增量备份](../../nebula-dashboard-ent/4.cluster-operator/operator/backup-and-restore.md)。
  - 内置 [dashboard.service](../../nebula-dashboard-ent/2.deploy-connect-dashboard-ent.md) 脚本，支持一键管理 Dashboard 服务和查看 Dashboard 版本。
  - 新增产品反馈页面。

- 优化

  - 创建集群时自动检测安装包是否适配操作系统。
  - 批量导入节点时支持指定 NebulaGraph 安装目录。
  - 删除集群时支持同时删除安装目录。
  - 导入集群和服务监控中显示依赖服务。
  - 告警规则静默支持中途取消。
  - 支持强杀 Graph 服务进程。
  - 支持展示和修改多个服务的配置信息。
  - 支持修改 Meta 服务配置。
  - 操作记录支持记录**更新配置**和**删除备份**操作。
  - LDAP 开启后支持自动注册。
  - 任务中心日志信息更加详细。
  - 浏览器兼容提示。
  - NebulaGraph 许可证到期提醒。
  - 支持红旗操作系统 Asianux Linux 7 (Core)。
  - 优化连接数据库、创建集群、扩缩容、批量导入节点等多处交互。
  - 优化接口报错提示。
  - 节点监控的总览页中显示监控指标名称。
  - 优化`num_queries`等监控指标的计算方式，调整为时序聚合显示。

- 缺陷修复

  - 修复服务监控的总览页面中选择监控时间范围不生效的问题。
  - 修复缩容时删除空节点没有删除对应 NebulaGraph 文件的问题。
  - 修复切换诊断报告语言时，同时切换了全局语言的问题。
  - 修复某个导入集群任务阻塞导致其他导入任务一直处于等待状态的问题。