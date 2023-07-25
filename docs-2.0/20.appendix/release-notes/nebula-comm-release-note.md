# {{nebula.name}} {{ nebula.release }} release notes

## 功能

- 增强全文索引功能。 [#5567](https://github.com/vesoft-inc/nebula/pull/5567) [#5575](https://github.com/vesoft-inc/nebula/pull/5575) [#5577](https://github.com/vesoft-inc/nebula/pull/5577) [#5580](https://github.com/vesoft-inc/nebula/pull/5580) [#5584](https://github.com/vesoft-inc/nebula/pull/5584) [#5587](https://github.com/vesoft-inc/nebula/pull/5587)

## 优化

- 支持使用`MATCH`子句检索 VID 或属性索引时使用变量。 [#5486](https://github.com/vesoft-inc/nebula/pull/5486) [#5553](https://github.com/vesoft-inc/nebula/pull/5553)
- 支持并行启动 RocksDB 实例以加快 Storage 服务的启动速度。 [#5521](https://github.com/vesoft-inc/nebula/pull/5521)
- 优化 RocksDB 迭代器执行`DeleteRange`操作后的前缀搜索性能。 [#5525](https://github.com/vesoft-inc/nebula/pull/5525)
- 优化 appendLog 发送逻辑以避免 follower 宕机后影响写性能。 [#5571](https://github.com/vesoft-inc/nebula/pull/5571)
- 优化`MATCH`语句查询不存在的属性时的性能。 [#5634](https://github.com/vesoft-inc/nebula/pull/5634)

## 缺陷修复

- 修复 Meta 数据不一致的问题。 [#5517](https://github.com/vesoft-inc/nebula/pull/5517)
- 修复 RocksDB 导入操作导致 leader 租约无效的问题。 [#5534](https://github.com/vesoft-inc/nebula/pull/5534)
- 修复存储的统计逻辑错误的问题。 [#5547](https://github.com/vesoft-inc/nebula/pull/5547)
- 修复设置无效请求参数的标志导致 Web 服务崩溃的问题。 [#5566](https://github.com/vesoft-inc/nebula/pull/5566)
- 修复列出会话时打印过多日志的问题。 [#5618](https://github.com/vesoft-inc/nebula/pull/5618)
- 修复单个大查询导致 Graph 服务崩溃的问题。 [#5619](https://github.com/vesoft-inc/nebula/pull/5619)
- 修复执行`Find All Path`语句导致 Graph 服务崩溃的问题。 [#5621](https://github.com/vesoft-inc/nebula/pull/5621) [#5640](https://github.com/vesoft-inc/nebula/pull/5640)
- 修复部分过期数据在最底层不会被回收的问题。 [#5447](https://github.com/vesoft-inc/nebula/pull/5447) [#5622](https://github.com/vesoft-inc/nebula/pull/5622)
- 修复在`MATCH`语句中添加路径变量会导致`all()`函数下推优化失效的问题。 [#5631](https://github.com/vesoft-inc/nebula/pull/5631)
- 修复`MATCH`语句中通过最短路径查询自环时返回结果错误的问题。 [#5636](https://github.com/vesoft-inc/nebula/pull/5636)
- 修复通过管道符删除边导致 Graph 服务崩溃的问题。 [#5645](https://github.com/vesoft-inc/nebula/pull/5645)
- 修复`MATCH`语句中匹配多跳时返回结果缺少边属性的问题。 [#5646](https://github.com/vesoft-inc/nebula/pull/5646)

## 历史版本

[历史版本](https://www.nebula-graph.com.cn/tags/%E5%8F%91%E7%89%88%E8%AF%B4%E6%98%8E)
