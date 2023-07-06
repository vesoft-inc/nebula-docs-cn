# {{dashboard_ent.name}}更新说明

## v3.5.0

- 功能

  - 支持通过{{dashboard_ent.name}}[一键部署 License Manager (LM)](../../nebula-dashboard-ent/3.connect-dashboard.md)。  
  - 支持[全量备份至本地](../../nebula-dashboard-ent/4.cluster-operator/operator/backup-and-restore.md)。
  - 增加[慢查询分析](../../nebula-dashboard-ent/4.cluster-operator/analysis-diagnosis/slow-query-analyst.md)功能。
  - 支持配置[集群诊断](../../nebula-dashboard-ent/4.cluster-operator/analysis-diagnosis/cluster-diagnosis.md)的打分公式。
  - [更新配置](../../nebula-dashboard-ent/4.cluster-operator/operator/update-config.md)增加**新增配置**、查看当前配置的**生效值**以及**查看不一致配置**功能。
  - 支持在[通知设置](../../nebula-dashboard-ent/system-settings/notification-endpoint.md)中为 webhook 配置 body。
  - 支持[自定义监控面板](../../nebula-dashboard-ent/4.cluster-operator/2.monitor.md)。

- 优化
  
  - 集群拓扑一致性：扩缩容后无需用户手动刷新与授权。
  - [集群总览](../../nebula-dashboard-ent/4.cluster-operator/1.overview.md)页面优化。
  - 集群间[数据同步](../../nebula-dashboard-ent/4.cluster-operator/7.data-synchronization.md)优化。
  - 扩容新增节点配置默认与集群中第一个节点保持一致。
  - 优化集群诊断报告内容。
  - 支持在`config.yaml`文件中修改`Prometheus`服务的端口号。


## v3.4.2

- 优化

  - 支持在备份恢复页面查看数据备份恢复的进度。
  - 内置{{nebula.name}} v3.4.1 安装包。

## v3.4.1

- 缺陷修复

  - 修复 RPM 包因为权限问题无法执行 `nebula-agent` 的问题。
  - 修复 goconfig 文件夹权限问题导致无法查看集群导入信息的问题。
  - 修复当许可证过期时间小于`30`天且`gracePeriod`大于`0`时页面提示错误的问题。

## v3.4.0

- 功能
  - 支持查看{{nebula.name}}集群[运行日志](../../nebula-dashboard-ent/4.cluster-operator/cluster-information/runtime-log.md)。
  - 支持查看{{nebula.name}}集群[审计日志](../../nebula-dashboard-ent/4.cluster-operator/cluster-information/audit-log.md)。
  - 支持[作业管理](../../nebula-dashboard-ent/4.cluster-operator/cluster-information/job-management.md)。
  - 备份恢复支持[增量备份](../../nebula-dashboard-ent/4.cluster-operator/operator/backup-and-restore.md)。
  - 内置 [dashboard.service](../../nebula-dashboard-ent/2.deploy-connect-dashboard-ent.md) 脚本，支持一键管理{{dashboard_ent.name}}服务和查看{{dashboard_ent.name}}版本。
  - 新增产品反馈页面。

- 优化

  - 创建集群时自动检测安装包是否适配操作系统。
  - 批量导入节点时支持指定{{nebula.name}}安装目录。
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
  - {{nebula.name}}许可证到期提醒。
  - 支持红旗操作系统 Asianux Linux 7 (Core)。
  - 优化连接数据库、创建集群、扩缩容、批量导入节点等多处交互。
  - 优化接口报错提示。
  - 节点监控的总览页中显示监控指标名称。
  - 优化`num_queries`等监控指标的计算方式，调整为时序聚合显示。

- 缺陷修复

  - 修复服务监控的总览页面中选择监控时间范围不生效的问题。
  - 修复缩容时删除空节点没有删除对应{{nebula.name}}文件的问题。
  - 修复切换诊断报告语言时，同时切换了全局语言的问题。
  - 修复某个导入集群任务阻塞导致其他导入任务一直处于等待状态的问题。
