# Nebula Graph {{ nebula.release }} release notes

## 变更

- 默认不支持插入无 Tag 的点。如需使用无 Tag 的点，在集群内所有 Graph 服务的配置文件（`nebula-graphd.conf`）中新增`--graph_use_vertex_key=true`；在所有 Storage 服务的配置文件（`nebula-storaged.conf`）中新增`--use_vertex_key=true`。

## 优化

- 支持查询[集群间同步进度](../synchronization-and-migration/replication-between-clusters.md)。

- 增强`AtomicLogBuffer`的内存使用，避免重建索引和数据同步时的 OOM 问题。

- 统一配置文件的示例和描述。

- 调整心跳日志的级别。

## 缺陷修复

- 修复 Web 服务收到特殊攻击消息时崩溃的问题。
- 修复删除全文索引导致的崩溃问题。
- 修复并发 map 导致的崩溃问题。
- 修复 Raft 在某些场景下的崩溃问题。
- 修复删除有索引的点和边时，语句中的 VID 的长度超出定义长度时，Storage 服务崩溃的问题。
- 修复表达式的语法错误导致崩溃的问题。
- 修复`LOOKUP`语句导致崩溃的问题。
- 修复复合`MATCH`语句导致崩溃的问题。
- 修复多`MATCH`语句优化阶段崩溃的问题。
- 修复收集变量类型导致崩溃的问题。
- 修复表达式非法导致崩溃的问题。
- 修复只有图空间路径没有分区路径时 Storage 服务崩溃的问题。
- 修复`BALANCE LEADER`任务执行器的死锁问题。
- 修复构建`BALANCE`计划时无限循环的问题。
- 修复重建全文索引失败的问题。
- 修复使用 logrotate 的问题。
- 修复数据恢复时机器密钥丢失的问题。
- 修复取消快照 future 时主机无法停止的问题。
- 修复缓存大小溢出和死锁的问题。
- 修复 MetaDaemon 缺少`RETURN`子句的问题。
- 修复 Raft 的脑裂问题。
- 修复 Meta listener 验证 License 的问题。
- 修复 Meta listener 不清理数据的问题。
- 修复 drainer 同步脏数据的问题。
- 修复 drainer 守护进程无法正常退出的问题。
- 修复审计日志无法异步使用的问题。
- 修复多`MATCH`语句并发异常的问题。
- 修复无法正常重新执行重建 Tag 索引任务的问题。
- 修复停止执行中的任务后，重建 Tag 索引任务总是失败的问题。
- 修复由于 UTF8 字符被截断导致 ElasticSearch 写入错误的问题。
- 修复写入 ElasticSearch 前删除截断文本的问题。
- 修复使用 ElasticSearch 保存审计日志时，没有记录 DML 和 DQL 类型的审计日志的问题。
- 修复当`ENABLE_BREAKPAD`启用时，如果日志目录不存在，会导致服务无法启动的问题。
- 修复如果 GOD 角色的用户名不为`root`，Meta 服务初始化时会自动创建`root`用户的问题。

## 历史版本

[历史版本](https://nebula-graph.com.cn/tags/release-note/)
