# NebulaGraph Dashboard 企业版更新说明

## 企业版 v3.1.2

- 缺陷修复
  - 修复 DEB 和 RPM 包中 nebula-stats-exporter 服务启动异常的问题。

## 企业版 v3.1.1

- 缺陷修复
  - 修复 License 上传校验的问题。

## 企业版 v3.1.0

- 功能
  - 支持[升级集群的 NebulaGraph 版本](../../nebula-dashboard-ent/4.cluster-operator/operator/version-upgrade.md)。
  - 支持[全量备份和恢复](../../nebula-dashboard-ent/4.cluster-operator/cluster-information/backup-and-restore.md)。
  - 支持[管理安装包](../../nebula-dashboard-ent/system-settings/manage-package.md)。
  - 部署 Dashboard 时，支持[使用 SQLite 数据库](../../nebula-dashboard-ent/2.deploy-connect-dashboard-ent.md)。

- 优化
  - 适配 NebulaGraph 3.2.0。
  - 监控
    - 支持全局配置监控时间范围。
    - 支持全局配置监控刷新频率。
    - 支持监控集群内所有磁盘使用量。
    - 支持展示指定维度的所有监控指标。
  - 告警
    - 支持[静默告警消息](../../nebula-dashboard-ent/4.cluster-operator/9.notification.md)。
  - 配置
    - 支持通过文件`config.yaml`修改服务的端口号。
    - 支持在更新配置页搜索配置名。
  - 优化系统报错信息。

- 缺陷修复
  - 修复诊断报告中无法获取负载和流量信息的问题。
  - 修复指标仪表盘框选不正常的问题。
  - 修复批量导入节点时，无法识别 CSV 文件中 Alias 列的中文的问题。