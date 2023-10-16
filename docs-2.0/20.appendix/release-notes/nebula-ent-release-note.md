# {{nebula.name}} {{ nebula.release }} release notes

## v3.6.0

- 功能
  - 支持管理 [Zone](../../4.deployment-and-installation/5.zone.md)。Zone 是{{nebula.name}}中存储（Storage）节点的逻辑机架，它将多个 Storage 节点划分成可管理的逻辑区域，实现资源隔离。
  - 支持 [HTTP2](../../5.configurations-and-logs/1.configurations/3.graph-config.md) 协议。
  - 支持 SSL 双向认证（[mTLS](../../7.data-security/4.ssl.md)）。
  - 支持自动监控 SSL 证书的[更新](../../7.data-security/4.ssl.md)。
  - 支持使用 [INNER JOIN](../../3.ngql-guide/8.clauses-and-options/joins.md) 进行连接查询。
  - 支持使用 [FIND SINGLE SHORTEST PATH](../../3.ngql-guide/16.subgraph-and-path/2.find-path.md) 查找单条最短路径。
  - 支持使用 [enable_record_slow_query](../../5.configurations-and-logs/1.configurations/3.graph-config.md) 配置项记录慢查询（不包括 DML）。

- 增强
  - 性能
    - 优化深度查询的性能。
    - 优化 Aggregate 算子的性能。
  - 高可用
    - partial success 添加统计信息。
    - 支持记录上次成功访问 LM 至今的时间，方便查看 LM 宕机的时间。
    - 当节点硬盘出现故障无法写入时触发重新选举，保证集群能够正常提供服务。
  - 易用性
    - 修改用户时可以单独修改密码或白名单列表。

- 缺陷修复
  - 修复 Meta 数据一致性的问题。
  - 修复部分过期数据在最底层不会被回收的问题。
  - 修复查询自循环点的所有路径时结果不正确的问题。
  - 修复向 Meta 服务的 Follower 发送请求的日志不正确的问题。

## v3.5.1

- 增强

  - 当`MATCH`语句查询不存在的属性时不再进行全表扫描。
  - 支持`MATCH...STARTS WITH`语句的下推。

- 缺陷修复

  - 修复连续重启 drainer 导致无法正常停止 drainer 的问题。
  - 修复单个大查询可能导致 Graph 服务崩溃的问题。
  - 修复`FIND ALL PATH`语句导致内存不足的问题。
  - 修复`MATCH`语句中添加路径变量导致`all()`函数下推优化失效的问题。
  - 修复低版本 Linux 内核使用 Boost 生成 UUID 时报错的问题。
  - 修复`MATCH...shortestpath()`语句进行循环检测时报错的问题。
  - 修复使用管道符（`|`）删除边时 Graph 服务崩溃的问题。
  - 修复`MATCH`语句进行多跳查询时边属性无法显示的问题。
  - 修复`shortestPath()`函数导致 Graph 服务崩溃的问题。
  - 修复`FIND ALL PATH`语句查找点的自环时未返回自环路径的问题。
  - 修复`GO`的复合语句中多个子句使用同一个变量时，重复执行该复合语句会返回不同结果的问题。
  - 修复`CREATE SPACE...AS`语句克隆出的图空间中，新建索引会覆盖旧索引的问题。
  - 修复`GO...UNION ALL`语句在某些场景下报错的问题。

## v3.5.0

- 功能

  - 支持通过 License Center 和 License Manager 管理 License。 
  - 支持`MATCH`语句的无索引全表扫描。
  - 支持在返回语句中使用像`v.tag`这样的表达式。
  - 支持 UPDATE 语句中的`json_extract`函数。 
  - 支持在 EXPLAIN 输出中使用 TCK 格式。 
  - DML 支持参数。
  - 增强全文索引功能。

- 增强

  - 支持以毫秒为单位的 TTL。
  - 增强了聚合函数中的属性裁剪功能。
  - 提高了遍历执行器的性能。
  - 重构了 ALL PATH 以提高性能。
  - 为了提高性能，移除了一些 Raft 锁。
  - 优化了谓词函数过滤变长边。
  - 并行遍历执行器。 
  - MATCH 支持 ID 集合。
  - 重构了 GO planner。 
  - 在配置文件中添加了一些 Graph 性能选项。
  - 添加了最大连接数标志。 
  - 支持使用`MATCH`语句检索 VID 或属性索引时使用变量。

- 缺陷修复

  - 修复了 RocksDB 导入数据导致 Leader lease 无效的缺陷。 
  - 修复了当用户不存在时`DESC USER`提示信息错误的缺陷。
  - 修复了 SPACE 存在时，`CREATE IF NOT EXIST`将无法成功的缺陷。 
  - 修复了在计划中 GetNeighbors 边的方向错误的缺陷。
  - 修复了`SHOW SESSIONS`命令中客户端 IP 格式的缺陷。
  - 修复了在 USE 和 MATCH 时属性被剪枝的缺陷。 
  - 修复了在某些情况下过滤器未下推的缺陷。
  - 修复了在某些情况下过滤器错误地过滤的缺陷。
  - 修复了模式表达式中内部变量处理不正确的缺陷。 
  - 修复了涉及 EMPTY 比较的缺陷。
  - 修复了 MATCH 中请求所有列时返回重复列的缺陷。
  - 修复了在自反边涉及路径的比较错误的缺陷。
  - 修复了 MATCH 路径中重新定义别名的缺陷。
  - 修复了插入地理空间值时的类型检查缺陷。
  - 修复了最短路径崩溃的缺陷。
  - 修复了 GEO 崩溃的缺陷。
  - 修复了在逻辑表达式评估中存储崩溃的缺陷。
  - 修复了`MATCH...contains`报错的缺陷。
  - 修复了并发时会话计数错误的 bug。
  - 修复了 SUBGRAPH 和 PATH 参数的缺陷。 
  - 修复了正则表达式的缺陷。
  - 修复了非表达式下推的缺陷。
  - 修复了集群切换的缺陷。

- 弃用

  - 禁用`edge list join`, 不支持在多个模式中使用边列表。
  - 移除 GLR 解析器, 需要将`YIELD 1–-1`修改为`YIELD 1– -1`。
  
## 历史版本

[历史版本](https://yueshu.com.cn/tags/%E5%8F%91%E7%89%88%E8%AF%B4%E6%98%8E)
