# Nebula Graph {{ nebula.release }} release notes

## Feature

- 支持session管理。[#280](https://github.com/vesoft-inc/nebula-graph/pull/280)
- 支持慢查询终止，已知问题：所以query的查询与终止都会有延迟，这与实现方案有关。[#1152](https://github.com/vesoft-inc/nebula-graph/pull/1152)
- Lookup语句增强表达式解析索引的能力。[#1188](https://github.com/vesoft-inc/nebula-graph/pull/1188)
- 支持配置机器内存水位，一定程度上缓解OOM的问题。[1067](https://github.com/vesoft-inc/nebula-graph/pull/1067)
- Find Path支持边过滤。[#1091](https://github.com/vesoft-inc/nebula-graph/pull/1091)
- Subgraph支持只返回图结构，不包含属性。[#1134](https://github.com/vesoft-inc/nebula-graph/pull/1134)
- timestamp函数支持无参数执行。[#515](https://github.com/vesoft-inc/nebula-common/pull/515)
- 支持查询各个服务的版本。[#944](https://github.com/vesoft-inc/nebula-graph/pull/944)
- index和TTL可以同时支持。[#382](https://github.com/vesoft-inc/nebula-storage/pull/382)
- 支持在指定属性创建全文索引。[#460](https://github.com/vesoft-inc/nebula-storage/pull/460)
- 创建space及schema支持comment。[#895](https://github.com/vesoft-inc/nebula-graph/pull/895)
- 支持全文索引重建。[#1123](https://github.com/vesoft-inc/nebula-graph/pull/1123)

## Enhancement
- listener接口优化，支持获取全量数据，[#465](https://github.com/vesoft-inc/nebula-storage/pull/465)、[#484](https://github.com/vesoft-inc/nebula-storage/pull/484)
- meta的leader表重新组织。[#439](https://github.com/vesoft-inc/nebula-storage/pull/439)
- 增加DiskManager用于检查磁盘剩余容量。[#461](https://github.com/vesoft-inc/nebula-storage/pull/461)
- 优化raft的heartbeat实现。[#438](https://github.com/vesoft-inc/nebula-storage/pull/438)
- storage支持并发执行go/fetch/lookup。 [#503](https://github.com/vesoft-inc/nebula-storage/pull/503)
- 加强了exists函数对map的支持。[#973](https://github.com/vesoft-inc/nebula-graph/pull/973)
- 加强聚合函数的使用方式，比如COUNT(v)+AVG(v)。[#968](https://github.com/vesoft-inc/nebula-graph/pull/968)

## Bug fix

- 权限导致的多语句执行问题。[#1165](https://github.com/vesoft-inc/nebula-graph/pull/1165)
- 修复unwind导致没有结果的问题。[#1018](https://github.com/vesoft-inc/nebula-graph/pull/1018)
- 修复聚合函数在某些场景下导致的crash问题。[#1015](https://github.com/vesoft-inc/nebula-graph/pull/1015)
- 修复OR表达式在索引匹配中的问题。[#1005](https://github.com/vesoft-inc/nebula-graph/pull/1005)
- 修复函数的大小写敏感问题。[#927](https://github.com/vesoft-inc/nebula-graph/issues/927)
- 修复查询索引创建信息时没有检查tag/edge类型的问题。[#933](https://github.com/vesoft-inc/nebula-graph/pull/933)
- 修复substring函数的bug。[#491](https://github.com/vesoft-inc/nebula-common/pull/491)
- 修复meta不能正确返回leader change。[#423](https://github.com/vesoft-inc/nebula-storage/pull/423)
- 修复LIMIT，ORDER，GROUP语句使用变量的问题。[#1314](https://github.com/vesoft-inc/nebula-graph/pull/1314)
- 修复db_dump工具打印int类型VID的问题。[#533](https://github.com/vesoft-inc/nebula-storage/pull/533)
- 修复balance任务恢复后仍显示FAIL的问题。[#528](https://github.com/vesoft-inc/nebula-storage/pull/528)

## Changes & Known issues

- Subgraph语法变化。

    ```ngql
    # 2.5.0版本增加WITH PROP关键字用于输出属性
    GET SUBGRAPH WITH PROP FROM <vids>

    # 原有语法将只输出图结构
    GET SUBGRAPH FROM <vids>#
    ```
    
- 在`ORDER BY`命令后必须使用引用符`$-.`。但在更早的版本中不需要。

    ```ngql
    # 2.5.0版本的ORDER BY命令后需要使用引用符`$-.`。
    nebula> LOOKUP ON player \
            YIELD player.age As playerage \
            | GROUP BY $-.playerage \
            YIELD $-.playerage as age, count(*) AS number \
            | ORDER BY $-.number DESC, $-.age DESC;

    # 之前版本不需要使用引用符`$-.`。
    nebula> LOOKUP ON player \
            YIELD player.age As playerage \
            | GROUP BY $-.playerage \
            YIELD $-.playerage as age, count(*) AS number \
            | ORDER BY number DESC, age DESC;
    ```
    
该版本已知bug/issue请参见[issues](https://github.com/vesoft-inc/nebula-graph/issues)。
