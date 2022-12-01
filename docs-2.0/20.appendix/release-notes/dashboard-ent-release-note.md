# NebulaGraph Dashboard 企业版更新说明

## 企业版 v3.2.3

- 优化

  - 如果 NebulaGraph 企业版版本高于 3.3.0，隐藏备份恢复页面。

## 企业版 v3.2.2

- 优化

  - 删除无用的公共文件夹。

- 缺陷修复

  - 修复 RPM 和 DEB 包无法向 Dashboard 自动注册服务的问题。

## 企业版 v3.2.1

- 优化

  - 下载列表添加 NebulaGraph 3.3.0 版本。

- 缺陷修复

  - 修复在社区版 NebulaGraph 3.3.0 中使用 BR 工具失败的问题。

## 企业版 v3.2.0

- 功能

  - 集群安全：
    - 单点登录方式新增 [OAuth2.0 认证](../..//nebula-dashboard-ent/5.account-management.md)。

- 优化

  - 监控：
    - 新增服务单进程指标监控。
    - 磁盘监控优化。
    - 新增部分 Storage 监控指标。
  - 告警：
    - 支持配置[多条件告警](../..//nebula-dashboard-ent/4.cluster-operator/9.notification.md)，条件同时满足时触发告警。
    - 磁盘告警优化。
  - 安全：
    - 支持 [SSH 密钥连接](../../nebula-dashboard-ent/4.cluster-operator/operator/node.md)方式。
  - 易用性：
    - 包结构调整。保证通过 Dashboard 安装的 NebulaGraph 集群和单独安装部署的集群包结构一致。
    - 新增展示各节点操作系统信息。
    - 支持修改 prometheus 和 alertmanager 端口号。
    - 支持搜索监控指标及查看指标详情。
    - 支持服务运行日志分片以及设置日志保留天数。

- 缺陷修复

  - 修复在服务管理页面查看监控页面时不跳转的问题。
  - 修复服务监控页面无法设置基线的问题。
  - 修复导入集群时授权失败的问题。
