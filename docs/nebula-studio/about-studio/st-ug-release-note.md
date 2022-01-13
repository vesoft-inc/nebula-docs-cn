# Studio 版本更新说明

## v3.1.0(2021.10.29)

- 功能增强：
  - 适配 Nebula 2.6.0。
  - 新增在 Kubernetes 集群里使用 Helm 部署并启动 Studio。
  - 新增 GEO 数据类型。
  - 图探索
    - 新增配置节点图标功能。

- 修复：
  - Schema
    - 修复以关键字命名的 Tag/Edge 或其下属性时会报错的问题。
    - 修复数据类型不完善的问题，补充 date/time/datetime/int32/int16/int8 等类型枚举。

- 兼容：
  - 去除 Studio 对 nebula-importer 的依赖，用 http-gateway 兼容相关功能。

## v3.0.0（2021.08.13）

- 功能增强：

  - 适配 Nebula 2.5.0。
  - 配置 Schema 中支持给 Space、Tag、Edge Type、Index 添加 COMMENT。
