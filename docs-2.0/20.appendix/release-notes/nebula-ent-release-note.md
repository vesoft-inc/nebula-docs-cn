# NebulaGraph 企业版 {{ nebula.release }} release notes

## 功能

- 支持[增量备份](../../backup-and-restore/nebula-br-ent/1.br-ent-overview.md)。
- 支持 Tag/Edge type 级别的[细粒度权限管理](../../7.data-security/1.authentication/3.role-list.md)。
- 支持[终止会话](../../3.ngql-guide/17.query-tuning-statements/2.kill-session.md)。
- 支持 [Memory Tracker](../../5.configurations-and-logs/1.configurations/4.storage-config.md)，优化内存管理。
- 支持[黑匣子监控工具](../../6.monitor-and-metrics/3.bbox/3.1.bbox.md)。
- 支持 [json_extract](../../3.ngql-guide/6.functions-and-expressions/2.string.md) 函数。
- 支持 [extract](../../3.ngql-guide/6.functions-and-expressions/2.string.md) 函数。

## 优化

- 支持`GET SUBGRAPH`时过滤点。
- 支持`GetNeighbors`过滤点。
- 支持时间戳和日期时间相互转换。
- 支持模式表达式引用局部定义变量。
- 优化作业管理。
- 优化全文索引。
- 优化模式表达式作为谓词时的处理方案。
- 优化 GO 语句的 JOIN 性能。
- 优化 k-hop 查询性能。
- 优化查询最短路径的性能。
- 优化点属性过滤的下推。
- 优化边过滤的下推。
- 优化查询子图的循环条件。
- 优化属性裁剪的规则。
- 移除无效的 Project 操作符。
- 移除无效的 AppendVertices 操作符。
- 减少连接操作的数据复制量。
- 减少 Traverse 和 AppendVertices 操作符的数据复制量。
- 修改 Graph 服务配置参数`session_reclaim_interval_secs`的默认值更改为 60 秒。
- 调整配置文件中`stderrthreshold`的默认级别。
- 通过下标获取属性值，减少属性查询的时间。
- 限制优化器中计划树的最大深度以避免堆栈溢出。

## 缺陷修复

- 修复查询计划生成与优化时的问题。

- 修复索引相关的缺陷：

  - 全文索引
  - 字符串索引

- 修复查询语句的缺陷：

  - 变量
  - 过滤条件和表达式
  - 点或边的属性
  - 参数
  - 函数与聚合
  - 使用非法的数据类型
  - 时区、日期、时间等
  - 子句与算子

- 修复 DDL 和 DML 语句相关的缺陷：

  - ALTER TAG 
  - UPDATE

- 修复其它功能的缺陷：

  - TTL
  - 数据同步
  - 身份验证
  - 服务
  - 日志
  - 监控和统计

## 变更

- 如果您打算从 3.1 升级到 3.4 版本，请按照[升级文档](../../4.deployment-and-installation/3.upgrade-nebula-graph/upgrade-nebula-ent-from-3.x-3.4.md)的指导进行操作。
- 新增的属性名不能与已存在或被删除的属性名同名，否则新增属性会失败。
- 限制修改 Schema 时的类型转换。
- 创建`NOT NULL`类型的属性时，必须指定默认值。
- 在配置文件中添加多线程查询参数`query_concurrently`，默认值为`true`。
- 从配置文件中改移除 KV 分离存储功能参数`kv_separation`，默认关闭该功能。
- 修改配置文件中`local_config`的默认值为`true`。
- 统一使用`v.tag.property`的方式获取属性值，需要指明 Tag。使用`v.property`的方式访问`v`点上某个 Tag 的属性在之前的版本中被错误地允许。
- 删除命令`SHOW HOSTS`中的`HTTP port`列。
- 禁用`OPTIONAL MATCH <pattern> WHERE <condition>`形式的查询。
- 禁用`COUNT(DISTINCT *)`形式的函数。
- 禁用 TOSS。
- 重命名 Listener 的 pid 文件名和 log 目录名。

## 历史版本

[历史版本](https://nebula-graph.com.cn/tags/release-note/)
