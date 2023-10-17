# {{nebula.name}} release notes

## v3.6.0

- 功能
  - 支持管理 [Zone](../../4.deployment-and-installation/5.zone.md)。Zone 是{{nebula.name}}中存储（Storage）节点的逻辑机架，它将多个 Storage 节点划分成可管理的逻辑区域，实现资源隔离。
  - 支持 [HTTP2](../../5.configurations-and-logs/1.configurations/3.graph-config.md) 协议。
  - 支持 SSL 双向认证（[mTLS](../../7.data-security/4.ssl.md)）。
  - 支持[自动监控](../../7.data-security/4.ssl.md) SSL 证书的更新。
  - 支持使用 [INNER JOIN](../../3.ngql-guide/8.clauses-and-options/joins.md) 进行连接查询。
  - 支持使用 [FIND SINGLE SHORTEST PATH](../../3.ngql-guide/16.subgraph-and-path/2.find-path.md) 查找单条最短路径。
  - 支持使用 [enable_record_slow_query](../../5.configurations-and-logs/1.configurations/3.graph-config.md) 配置项记录慢查询（不包括 DML）。

- 增强
  - 性能
    - 优化深度查询的性能。
    - 优化 Aggregate 算子的性能。
  - 高可用
    - 部分成功（partial success）增加监控指标`resp_part_completeness`。
    - 支持记录上次成功访问 LM 至今的时长，方便查看 LM 宕机的时间。
    - 当节点硬盘出现故障无法写入时触发重新选举，保证集群能够正常提供服务。
  - 易用性
    - 修改用户时可以单独修改密码或白名单列表。

- 缺陷修复
  - 修复 Meta 数据一致性的问题。
  - 修复部分过期数据在最底层不会被回收的问题。
  - 修复查询自循环点的所有路径时结果不正确的问题。
  - 修复向 Meta 服务的 Follower 发送请求的日志不正确的问题。
