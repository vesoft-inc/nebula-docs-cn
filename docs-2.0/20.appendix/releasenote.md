# Nebula Graph {{ nebula.release }} release notes

## Feature

- 支持session管理。https://github.com/vesoft-inc/nebula-graph/pull/280
- 支持慢查询终止，已知问题：所以query的查询与终止都会有延迟，这与实现方案有关。https://github.com/vesoft-inc/nebula-graph/pull/1152
- Lookup语句增强表达式解析索引的能力。https://github.com/vesoft-inc/nebula-graph/pull/1188
- 支持配置机器内存水位，一定程度上缓解OOM的问题。https://github.com/vesoft-inc/nebula-graph/pull/1067
- Find Path支持边过滤。https://github.com/vesoft-inc/nebula-graph/pull/1091
- Subgraph支持只返回图结构，不包含属性。https://github.com/vesoft-inc/nebula-graph/pull/1134
- timestamp函数支持无参数执行。https://github.com/vesoft-inc/nebula-common/pull/515
- 支持查询各个服务的版本。https://github.com/vesoft-inc/nebula-graph/pull/944
- index和TTL可以同时支持。#382
- 支持在指定属性创建全文索引。#460
- 创建space及schema支持comment。https://github.com/vesoft-inc/nebula-graph/pull/895
- 支持全文索引重建。

## Enhancement
- listener接口优化，支持获取全量数据，#465，#484
- meta的leader表重新组织，#439
- 增加DiskManager用于检查磁盘剩余容量，#461
- 优化raft的heartbeat实现#438
- storage支持并发执行go/fetch/lookup #503
- 加强了exists函数对map的支持。https://github.com/vesoft-inc/nebula-graph/pull/973
- 加强聚合函数的使用方式，比如COUNT(v)+AVG(v)。https://github.com/vesoft-inc/nebula-graph/pull/968

## Bug fix

- 权限导致的多语句执行问题。https://github.com/vesoft-inc/nebula-graph/pull/1165
- 修复unwind导致没有结果的问题。https://github.com/vesoft-inc/nebula-graph/pull/1018
- 修复聚合函数在某些场景下导致的crash问题。https://github.com/vesoft-inc/nebula-graph/pull/1015
- 修复OR表达式在索引匹配中的问题。https://github.com/vesoft-inc/nebula-graph/pull/1005
- 修复函数的大小写敏感问题。https://github.com/vesoft-inc/nebula-graph/issues/927
- 修复查询索引创建信息时没有检查tag/edge类型的问题。https://github.com/vesoft-inc/nebula-graph/pull/933
- 修复substring函数的bug。https://github.com/vesoft-inc/nebula-common/pull/491
- 修复meta不能正确返回leader change。#423
- 修复LIMIT，ORDER，GROUP语句使用变量的问题。https://github.com/vesoft-inc/nebula-graph/pull/1314
- 修复db_dump工具打印int类型VID的问题。https://github.com/vesoft-inc/nebula-storage/pull/533
- 修复balance任务恢复后仍显示FAIL的问题。https://github.com/vesoft-inc/nebula-storage/pull/528

## Changes & Known issues

- Subgraph 语法变化

    ```ngql
    # 增加WITH PROP关键字用于输出属性
    GET SUBGRAPH WITH PROP FROM <vids>

    # 原有语法将只输出图结构
    GET SUBGRAPH FROM <vids>#
    ```
    
该版本已知 bug/issue 见 https://github.com/vesoft-inc/nebula-graph/issues
