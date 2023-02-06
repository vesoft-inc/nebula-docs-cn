# NebulaGraph 社区版 {{ nebula.release }} release notes

## 功能

- 支持[终止会话](../../3.ngql-guide/17.query-tuning-statements/2.kill-session.md)。[#5146](https://github.com/vesoft-inc/nebula/pull/5146) 
- 支持 [Memory Tracker](../../5.configurations-and-logs/1.configurations/4.storage-config.md)，优化内存管理。[#5082](https://github.com/vesoft-inc/nebula/pull/5082)

## 优化

- 优化作业管理。 [#5212](https://github.com/vesoft-inc/nebula/pull/5212) [#5093](https://github.com/vesoft-inc/nebula/pull/5093) [#5099](https://github.com/vesoft-inc/nebula/pull/5099) [#4872](https://github.com/vesoft-inc/nebula/pull/4872)

- 修改 Graph 服务配置参数`session_reclaim_interval_secs`的默认值更改为 60 秒。 [#5246](https://github.com/vesoft-inc/nebula/pull/5246)

- 调整配置文件中`stderrthreshold`的默认级别。 [#5188](https://github.com/vesoft-inc/nebula/pull/5188) 

- 优化全文索引。 [#5077](https://github.com/vesoft-inc/nebula/pull/5077) [#4900](https://github.com/vesoft-inc/nebula/pull/4900) [#4925](https://github.com/vesoft-inc/nebula/pull/4925) 

- 限制优化器中计划树的最大深度以避免堆栈溢出。 [#5050](https://github.com/vesoft-inc/nebula/pull/5050)

- 优化模式表达式作为谓词时的处理方案。 [#4916](https://github.com/vesoft-inc/nebula/pull/4916)

## 缺陷修复

- 修复查询计划生成与优化时的问题。 [#4863](https://github.com/vesoft-inc/nebula/pull/4863) [#4813](https://github.com/vesoft-inc/nebula/pull/4813)

- 修复索引相关的缺陷：

  - 全文索引 [#5214](https://github.com/vesoft-inc/nebula/pull/5214) [#5260](https://github.com/vesoft-inc/nebula/pull/5260)
  - 字符串索引 [5126](https://github.com/vesoft-inc/nebula/pull/5126)

- 修复查询语句的缺陷：

  - 变量 [#5192](https://github.com/vesoft-inc/nebula/pull/5192)
  - 过滤条件和表达式 [#4952](https://github.com/vesoft-inc/nebula/pull/4952) [#4893](https://github.com/vesoft-inc/nebula/pull/4893) [#4863](https://github.com/vesoft-inc/nebula/pull/4863)
  - 点或边的属性 [#5230](https://github.com/vesoft-inc/nebula/pull/5230) [#4846](https://github.com/vesoft-inc/nebula/pull/4846) [#4841](https://github.com/vesoft-inc/nebula/pull/4841) [#5238](https://github.com/vesoft-inc/nebula/pull/5238)
  - 函数与聚合 [#5135](https://github.com/vesoft-inc/nebula/pull/5135) [#5121](https://github.com/vesoft-inc/nebula/pull/5121) [#4884](https://github.com/vesoft-inc/nebula/pull/4884)
  - 使用非法的数据类型 [#5242](https://github.com/vesoft-inc/nebula/pull/5242)
  - 子句与算子 [#5241](https://github.com/vesoft-inc/nebula/pull/5241) [#4965](https://github.com/vesoft-inc/nebula/pull/4965)

- 修复 DDL 和 DML 语句相关的缺陷：

  - ALTER TAG [#5105](https://github.com/vesoft-inc/nebula/pull/5105) [#5136](https://github.com/vesoft-inc/nebula/pull/5136)
  - UPDATE [#4933](https://github.com/vesoft-inc/nebula/pull/4933)

- 修复其它功能的缺陷：

  - TTL [#4961](https://github.com/vesoft-inc/nebula/pull/4961)
  - 身份验证 [#4885](https://github.com/vesoft-inc/nebula/pull/4885)
  - 服务 [#4896](https://github.com/vesoft-inc/nebula/pull/4896)

## 变更

- 新增的属性名不能与已存在或被删除的属性名同名，否则新增属性会失败。 [#5130](https://github.com/vesoft-inc/nebula/pull/5130)
- 限制修改 Schema 时的类型转换。 [#5098](https://github.com/vesoft-inc/nebula/pull/5098)
- 创建`NOT NULL`类型的属性时，必须指定默认值。 [#5105](https://github.com/vesoft-inc/nebula/pull/5105)
- 在配置文件中添加多线程查询参数`query_concurrently`，默认值为`true`。 [#5119](https://github.com/vesoft-inc/nebula/pull/5119)
- 从配置文件中改移除 KV 分离存储功能参数`kv_separation`，默认关闭该功能。 [#5119](https://github.com/vesoft-inc/nebula/pull/5119)
- 修改配置文件中`local_config`的默认值为`true`。 [#5119](https://github.com/vesoft-inc/nebula/pull/5119)
- 统一使用`v.tag.property`的方式获取属性值，需要指明 Tag。使用`v.property`的方式访问`v`点上某个 Tag 的属性在之前的版本中被错误地允许。 [#5230](https://github.com/vesoft-inc/nebula/pull/5230)
- 删除命令`SHOW HOSTS`中的`HTTP port`列。 [#5056](https://github.com/vesoft-inc/nebula/pull/5056)
- 禁用`OPTIONAL MATCH <pattern> WHERE <condition>`形式的查询。 [#5273](https://github.com/vesoft-inc/nebula/pull/5273)
- 禁用 TOSS。 [#5119](https://github.com/vesoft-inc/nebula/pull/5119)
- 重命名 Listener 的 pid 文件名和 log 目录名。 [#5119](https://github.com/vesoft-inc/nebula/pull/5119)

## 历史版本

[历史版本](https://nebula-graph.com.cn/tags/release-note/)
