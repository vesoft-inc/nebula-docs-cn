# Nebula Graph {{ nebula.release }} release notes

## 企业版

### 功能

- 增加 [Elasticsearch 查询函数](../3.ngql-guide/6.functions-and-expressions/17.ES-function.md)，支持向独立部署的 Elasticsearch 发送 GET 请求读取数据。 [#924](https://github.com/vesoft-inc/nebula-ent/pull/924)

- 增加 [extract() 函数](../3.ngql-guide/6.functions-and-expressions/2.string.md)。 [#4098](https://github.com/vesoft-inc/nebula/pull/4098)

### 优化

- 优化配置文件，增加部分配置。 [#4310](https://github.com/vesoft-inc/nebula/pull/4310)

- 增加优化规则，移除无用的 AppendVertices 操作符。 [#4277](https://github.com/vesoft-inc/nebula/pull/4277)

- 增加优化规则，优化边过滤的下推。 [#4270](https://github.com/vesoft-inc/nebula/pull/4270)

- 增加优化规则，优化点属性过滤的下推。 [#4260](https://github.com/vesoft-inc/nebula/pull/4260)

- 剔除点的预测过滤器。 [#4249](https://github.com/vesoft-inc/nebula/pull/4249)

- 减少移动数据时连接操作的数据复制量。 [#4283](https://github.com/vesoft-inc/nebula/pull/4283)

- 通过下标获取属性值，减少属性查询的时间。 [#4242](https://github.com/vesoft-inc/nebula/pull/4242)

- 优化查询最短路径的性能。 [#4071](https://github.com/vesoft-inc/nebula/pull/4071)

- 优化查询子图的循环条件。 [#4226](https://github.com/vesoft-inc/nebula/pull/4226)

- 减少移动数据时 Traverse 和 AppendVertices 操作符的数据复制量。 [#4176](https://github.com/vesoft-inc/nebula/pull/4176)

- 改善优化规则，去除无效的项目操作符。 [#4157](https://github.com/vesoft-inc/nebula/pull/4157)

- 使用 Arena Allocator 优化内存分配。 [#4239](https://github.com/vesoft-inc/nebula/pull/4239)

### 缺陷修复

- 修复 Web 服务在接收一些特殊攻击消息时崩溃的问题。 [#4334](https://github.com/vesoft-inc/nebula/pull/4334)

- 修复并发扫描属性时 Storage 服务崩溃的问题。 [#4268](https://github.com/vesoft-inc/nebula/pull/4268)

- 修复插入超过限制长度的边时 Storage 服务崩溃的问题。 [#4305](https://github.com/vesoft-inc/nebula/pull/4305)

- 修复启用查询并发模式时服务崩溃的问题。 [#4288](https://github.com/vesoft-inc/nebula/pull/4288)

- 修复查找具有 NULL 属性的索引时 Storage 服务崩溃的问题。 [#4234](https://github.com/vesoft-inc/nebula/pull/4234)

- 修复重启后独立守护进程退出的缺陷。 [#4269](https://github.com/vesoft-inc/nebula/pull/4269)

- 修复 GraphViz 在线工具由于两次 JSON 转换导致 Join 点格式的解释结果不正确的缺陷。 [#4280](https://github.com/vesoft-inc/nebula/pull/4280)

- 修复属性查找的缺陷，不允许在 Schema 中使用英文句号（.）。 [#4194](https://github.com/vesoft-inc/nebula/pull/4194)

- 修复恢复数据时机器丢失 key 的缺陷。 [#4311](https://github.com/vesoft-inc/nebula/pull/4311)

- 修复使用相同语句返回相同顶点不同属性时，结果显示`BAD TYPE`的缺陷。 [#4151](https://github.com/vesoft-inc/nebula/pull/4151)

- 修复无索引时，语句`MATCH p=(:team)-->() RETURN p LIMIT 1`的报错信息缺陷。 [#4053](https://github.com/vesoft-inc/nebula/pull/4053)

- 增强运算符`AND`和`OR`的报错信息。 [#4304](https://github.com/vesoft-inc/nebula/pull/4304)

- 修复索引条件下没有统计信息的缺陷。 [#4353](https://github.com/vesoft-inc/nebula/pull/4353)

## 历史版本

[历史版本](https://nebula-graph.com.cn/tags/release-note/)
