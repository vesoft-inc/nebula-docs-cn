# NebulaGraph 社区版 {{ nebula.release }} release notes

## 优化

- 优化了 k-hop 查询性能。[#4560](https://github.com/vesoft-inc/nebula/pull/4560) [#4736](https://github.com/vesoft-inc/nebula/pull/4736)  [#4566](https://github.com/vesoft-inc/nebula/pull/4566) [#4582](https://github.com/vesoft-inc/nebula/pull/4582) [#4558](https://github.com/vesoft-inc/nebula/pull/4558) [#4556](https://github.com/vesoft-inc/nebula/pull/4556) [#4555](https://github.com/vesoft-inc/nebula/pull/4555) [#4516](https://github.com/vesoft-inc/nebula/pull/4516) [#4531](https://github.com/vesoft-inc/nebula/pull/4531) [#4522](https://github.com/vesoft-inc/nebula/pull/4522) [#4754](https://github.com/vesoft-inc/nebula/pull/4754) [#4762](https://github.com/vesoft-inc/nebula/pull/4762)

- 优化 `GO` 语句 JOIN 性能。 [#4599](https://github.com/vesoft-inc/nebula/pull/4599) [#4750](https://github.com/vesoft-inc/nebula/pull/4750)

- 支持 `GET SUBGRAPH` 过滤点。 [#4357](https://github.com/vesoft-inc/nebula/pull/4357)

- 支持 `GetNeighbors` 过滤点。 [#4671](https://github.com/vesoft-inc/nebula/pull/4671)

- 优化了 `FIND SHORTEST PATH` 的循环处理。 [#4672](https://github.com/vesoft-inc/nebula/pull/4672)

- 支持时间戳和日期时间相互转换。 [#4626](https://github.com/vesoft-inc/nebula/pull/4526)

- 支持模式表达式引用局部定义变量。 [#4498](https://github.com/vesoft-inc/nebula/pull/4498)

- 优化 job manager。 [#4446](https://github.com/vesoft-inc/nebula/pull/4446) [#4442](https://github.com/vesoft-inc/nebula/pull/4442) [#4444](https://github.com/vesoft-inc/nebula/pull/4444) [#4460](https://github.com/vesoft-inc/nebula/pull/4460) [#4500](https://github.com/vesoft-inc/nebula/pull/4500) [#4633](https://github.com/vesoft-inc/nebula/pull/4633) [#4654](https://github.com/vesoft-inc/nebula/pull/4654) [#4663](https://github.com/vesoft-inc/nebula/pull/4663) [#4722](https://github.com/vesoft-inc/nebula/pull/4722) [#4742](https://github.com/vesoft-inc/nebula/pull/4742)

- 添加实验功能的 flag，<!--`TOSS` 的 `enable_toss` 和 -->`BALANCE DATA` 的 `enable_data_balance`。 [#4728](https://github.com/vesoft-inc/nebula/pull/4728)

- 启动进程时统计日志打印到控制台。 [#4550](https://github.com/vesoft-inc/nebula/pull/4550)

- 支持 `JSON_EXTRACT` 函数。 [#4743](https://github.com/vesoft-inc/nebula/pull/4743)


## 缺陷修复

- 修复了收集变量类型引起的崩溃。 [#4724](https://github.com/vesoft-inc/nebula/pull/4724)

- 修复了多 `MATCH` 优化阶段的崩溃问题。 [#4780](https://github.com/vesoft-inc/nebula/pull/4780)

- 修复聚合表达式类型推导的错误。 [#4706](https://github.com/vesoft-inc/nebula/pull/4706)

- 修复了 `OPTIONAL MATCH` 语句的错误结果为给出错误消息，因为 `OPTIONAL MATCH` 语句中 `WHERE` 子句不支持引用其他 `MATCH` 语句定义的变量。 [#4670](https://github.com/vesoft-inc/nebula/pull/4670)

- 修复了 `LOOKUP` 语句中参数表达式的缺陷。 [#4664](https://github.com/vesoft-inc/nebula/pull/4664)

- 修复 `LOOKUP` 中 `YIELD DISTINCT` 返回不同结果集的缺陷。 [#4651](https://github.com/vesoft-inc/nebula/pull/4651)

- 修复 `ColumnExpression` 编解码不匹配的缺陷。 [#4413](https://github.com/vesoft-inc/nebula/pull/4413)

- 修复 `GO` 语句中 `id($$)` 过滤器不正确的缺陷。  [#4768](https://github.com/vesoft-inc/nebula/pull/4768)

- 修复了 `MATCH` 语句中 `IN` 表达式相关谓词的索引选取扫描的缺陷。 [#4748](https://github.com/vesoft-inc/nebula/pull/4748)

- 修复了 `MATCH` 语句中优化器处理的错误。 [#4771](https://github.com/vesoft-inc/nebula/pull/4771)

- 修复了 `MATCH` 语句中使用 `pattern` 表达式作为过滤器时错误输出的缺陷。 [#4778](https://github.com/vesoft-inc/nebula/pull/4778)

- 修复 Tag、Edge、Tag 索引、Edge 索引显示数据不正确的缺陷。 [#4616](https://github.com/vesoft-inc/nebula/pull/4616)

- 修复了日期时间格式的缺陷。 [#4524](https://github.com/vesoft-inc/nebula/pull/4524)

- 修复 datetime 点返回值发生变化的缺陷。 [#4448](https://github.com/vesoft-inc/nebula/pull/4448)

- 修复开启 `enable_breakpad` 时，日志目录不存在时启动服务失败的缺陷。 [#4623](https://github.com/vesoft-inc/nebula/pull/4623)

- 修复了 metad 停止后，状态仍然在线的缺陷。 [#4610](https://github.com/vesoft-inc/nebula/pull/4610)

- 修复了日志文件损坏的缺陷。 [#4409](https://github.com/vesoft-inc/nebula/pull/4409)

- 修复了 `ENABLE_CCACHE` 选项不起作用的缺陷。 [#4648](https://github.com/vesoft-inc/nebula/pull/4648)

- 全文索引名称中不支持大写字母。 [#4628](https://github.com/vesoft-inc/nebula/pull/4628)

- 禁用 `COUNT(DISTINCT *)` 。 [#4553](https://github.com/vesoft-inc/nebula/pull/4553)

### 变更

- 默认不支持无 Tag 的点。 [#4629](https://github.com/vesoft-inc/nebula/pull/4629) 
  
## 历史版本

[历史版本](https://nebula-graph.com.cn/tags/release-note/)
