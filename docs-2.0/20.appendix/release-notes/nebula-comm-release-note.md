# {{nebula.name}} {{ nebula.release }} release notes

## 功能

- 支持无索引的全表扫描。[#5416](https://github.com/vesoft-inc/nebula/pull/5416)
- 支持 UDF。 [#4804](https://github.com/vesoft-inc/nebula/pull/4804) [#5391](https://github.com/vesoft-inc/nebula/pull/5391)
- 支持在返回语句中使用像`v.tag`这样的表达式。[#5440](https://github.com/vesoft-inc/nebula/pull/5440)
- 支持 UPDATE 语句中的`json_extract`函数。 [#5457](https://github.com/vesoft-inc/nebula/pull/5457)
- 支持在 EXPLAIN 输出中使用 TCK 格式。 [#5414](https://github.com/vesoft-inc/nebula/pull/5414)
- DML 支持参数。 [#5328](https://github.com/vesoft-inc/nebula/pull/5328)

## 优化

- 支持以毫秒为单位的 TTL。 [#5430](https://github.com/vesoft-inc/nebula/pull/5430)
- 增强了聚合函数中的属性裁剪功能。 [#5301](https://github.com/vesoft-inc/nebula/pull/5301)
- 提高了遍历执行器的性能。[#5308](https://github.com/vesoft-inc/nebula/pull/5308)
- 优化了 FIND ALL PATH 性能。 [#5409](https://github.com/vesoft-inc/nebula/pull/5409)
- 为了提高性能，移除了一些 Raft 锁。[#5451](https://github.com/vesoft-inc/nebula/pull/5451)
- 优化了谓词函数过滤变长边。[#5464](https://github.com/vesoft-inc/nebula/pull/5464) [#5470](https://github.com/vesoft-inc/nebula/pull/5470) [#5481](https://github.com/vesoft-inc/nebula/pull/5481) [#5503](https://github.com/vesoft-inc/nebula/pull/5503)
- 并行遍历执行器。 [#5314](https://github.com/vesoft-inc/nebula/pull/5314)
- MATCH 支持 ID 集合。 [#5360](https://github.com/vesoft-inc/nebula/pull/5360)
- 重构了 GO planner。 [#5369](https://github.com/vesoft-inc/nebula/pull/5369)
- 在配置文件中添加了一些 Graph 性能选项。 [#5463](https://github.com/vesoft-inc/nebula/pull/5463)
- 添加了最大连接数标志。 [#5309](https://github.com/vesoft-inc/nebula/pull/5309)    

## 缺陷修复

- 修复了 RocksDB 导入数据导致 Leader lease 无效的缺陷。 [#5271](https://github.com/vesoft-inc/nebula/pull/5271)
- 修复了当用户不存在时`DESC USER`提示信息错误的缺陷。 [#5345](https://github.com/vesoft-inc/nebula/pull/5345)
- 修复了 SPACE 存在时，`CREATE IF NOT EXIST`将无法成功的缺陷。 [#5375](https://github.com/vesoft-inc/nebula/pull/5375)
- 修复了在计划中 GetNeighbors 边的方向错误的缺陷。 [#5386](https://github.com/vesoft-inc/nebula/pull/5386)
- 修复了`SHOW SESSIONS`命令中客户端 IP 格式的缺陷。 [#5388](https://github.com/vesoft-inc/nebula/pull/5388)
- 修复了在 USE 和 MATCH 时属性被剪枝的缺陷。 [#5263](https://github.com/vesoft-inc/nebula/issues/5263)
- 修复了在某些情况下过滤器未下推的缺陷。 [#5395](https://github.com/vesoft-inc/nebula/pull/5395)
- 修复了在某些情况下过滤器错误地过滤的缺陷。 [#5422](https://github.com/vesoft-inc/nebula/pull/5422)
- 修复了模式表达式中内部变量处理不正确的缺陷。 [#5424](https://github.com/vesoft-inc/nebula/pull/5424)
- 修复了涉及 EMPTY 比较的缺陷。[#5433](https://github.com/vesoft-inc/nebula/pull/5433)
- 修复了 MATCH 中请求所有列时返回重复列的缺陷。[#5443](https://github.com/vesoft-inc/nebula/pull/5443)
- 修复了在自反边涉及路径的比较错误的缺陷。 [#5444](https://github.com/vesoft-inc/nebula/pull/5444)
- 修复了 MATCH 路径中重新定义别名的缺陷。[#5446](https://github.com/vesoft-inc/nebula/pull/5446)
- 修复了插入地理位置值时的类型检查缺陷。 [#5460](https://github.com/vesoft-inc/nebula/pull/5460)
- 修复了最短路径崩溃的缺陷。 [#5472](https://github.com/vesoft-inc/nebula/pull/5472)
- 修复了 GEO 崩溃的缺陷。 [#5475](https://github.com/vesoft-inc/nebula/pull/5475)
- 修复了`MATCH...contains`报错的缺陷。 [#5485](https://github.com/vesoft-inc/nebula/pull/5485)
- 修复了并发时会话计数错误的 bug。[#5496](https://github.com/vesoft-inc/nebula/pull/5496)
- 修复了 SUBGRAPH 和 PATH 参数的缺陷。 [#5500](https://github.com/vesoft-inc/nebula/pull/5500)
- 修复了正则表达式的缺陷。[#5507](https://github.com/vesoft-inc/nebula/pull/5507)  

## 变更

- 禁用`edge list join`, 不支持在多个模式中使用边列表。 [#5268](https://github.com/vesoft-inc/nebula/pull/5268)
- 移除 GLR 解析器, 需要将`YIELD 1–-1`修改为`YIELD 1– -1`。 [#5290](https://github.com/vesoft-inc/nebula/pull/5290)


## 历史版本

[历史版本](https://www.nebula-graph.com.cn/tags/%E5%8F%91%E7%89%88%E8%AF%B4%E6%98%8E)
