# {{nebula.name}} {{ nebula.release }} release notes

## 功能

- 增强全文索引功能。 [#5567](https://github.com/vesoft-inc/nebula/pull/5567) [#5575](https://github.com/vesoft-inc/nebula/pull/5575) [#5577](https://github.com/vesoft-inc/nebula/pull/5577) [#5580](https://github.com/vesoft-inc/nebula/pull/5580) [#5584](https://github.com/vesoft-inc/nebula/pull/5584)

## 优化

- 支持使用MATCH语句检索 VID 或属性索引时使用变量。 [#5486](https://github.com/vesoft-inc/nebula/pull/5486) [#5553](https://github.com/vesoft-inc/nebula/pull/5553)

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
