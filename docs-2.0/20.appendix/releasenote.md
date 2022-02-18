# Nebula Graph {{ nebula.release }} release notes

## Feature

- 新增[备份与恢复工具BR](../nebula-br/1.what-is-br.md)。 [#3469](https://github.com/vesoft-inc/nebula/pull/3469) [#1](https://github.com/vesoft-inc/nebula-agent/pull/1) [#22](https://github.com/vesoft-inc/nebula-br/pull/22)

- 支持 [openCypher 多 MATCH 查询](../3.ngql-guide/7.general-query-statements/2.match.md)。 [#3519](https://github.com/vesoft-inc/nebula/pull/3519) [#3318](https://github.com/vesoft-inc/nebula/pull/3318)

- 新增[存算合并版](../4.deployment-and-installation/standalone-deployment.md)。 [#3310](https://github.com/vesoft-inc/nebula/pull/3310)

- 新增[存储引擎的 kv 分离](../5.configurations-and-logs/1.configurations/4.storage-config.md)。 [#3281](https://github.com/vesoft-inc/nebula/pull/3281)

- 新增`LOOKUP`支持 topN 下推。 [#3499](https://github.com/vesoft-inc/nebula/pull/3499)

- 新增[不带 Tag 的点](../3.ngql-guide/12.vertex-statements/1.insert-vertex.md)。 [#3316](https://github.com/vesoft-inc/nebula/pull/3316) [#3335](https://github.com/vesoft-inc/nebula/pull/3335) [#3328](https://github.com/vesoft-inc/nebula/pull/3328) [#3286](https://github.com/vesoft-inc/nebula/pull/3286)

- 新增[参数化查询](../nebula-console.md)。 [#3379](https://github.com/vesoft-inc/nebula/pull/3379)

- 新增[不指定 VID 的查询](../3.ngql-guide/7.general-query-statements/2.match.md)，通过`LIMIT`子句限制输出结果。 [#3320](https://github.com/vesoft-inc/nebula/pull/3320) [#3329](https://github.com/vesoft-inc/nebula/pull/3329) [#3262](https://github.com/vesoft-inc/nebula/pull/3262)

- 新增 [duration](../3.ngql-guide/3.data-types/4.date-and-time.md) 数据类型和函数。 [#3338](https://github.com/vesoft-inc/nebula/pull/3338)

- 支持 Schema 使用大部分 1~4 字节的 [UTF-8 编码字符](../3.ngql-guide/1.nGQL-overview/keywords-and-reserved-words.md)。 [#3380](https://github.com/vesoft-inc/nebula/pull/3380)  [#3440](https://github.com/vesoft-inc/nebula/pull/3440)

- 新增[查看指定用户权限](../7.data-security/1.authentication/2.management-user.md)。 [#3300](https://github.com/vesoft-inc/nebula/pull/3300)

<!--
- 新增 traverse 算子。 [#3308](https://github.com/vesoft-inc/nebula/pull/3308)
- 支持Snowflake IDs。 [#3500](https://github.com/vesoft-inc/nebula/pull/3500)
-->

## Enhancement

- 重构集群管理。 [#3343](https://github.com/vesoft-inc/nebula/pull/3343)

- 当日志磁盘空间不足时，支持改变日志级别。 [#3576](https://github.com/vesoft-inc/nebula/pull/3576)

- 支持反引号中的任何字符串作为 Tag 名称。 [#3424](https://github.com/vesoft-inc/nebula/pull/3424)

- Storage 服务通过心跳将 partition 的磁盘路径信息发送到 Meta 服务。 [#3369](https://github.com/vesoft-inc/nebula/pull/3369) [#3416](https://github.com/vesoft-inc/nebula/pull/3416)

- 添加对无效密码尝试的限制。 [#3573](https://github.com/vesoft-inc/nebula/pull/3573) [#3629](https://github.com/vesoft-inc/nebula/pull/3629)

- TOSS 支持`DELETE`操作的一致性。 [#3374](https://github.com/vesoft-inc/nebula/pull/3374)

- 支持对接 logrotate。 [#3541](https://github.com/vesoft-inc/nebula/pull/3541)

- 支持更多的统计。 [#3446](https://github.com/vesoft-inc/nebula/pull/3446) [#3605](https://github.com/vesoft-inc/nebula/pull/3605) [#3590](https://github.com/vesoft-inc/nebula/pull/3590)

- 增强日期解析器。 [#3179](https://github.com/vesoft-inc/nebula/pull/3179)

- 删除 meta 服务中的读锁以减少读写锁的副作用。 [#3256](https://github.com/vesoft-inc/nebula/pull/3256)

- 重构存储索引，解决节点间耦合严重的问题。 [#3196](https://github.com/vesoft-inc/nebula/pull/3196)

- 支持指定`round()`函数的浮点精度。 [#3178](https://github.com/vesoft-inc/nebula/pull/3178)ß

- ES 客户端支持 https。 [#3150](https://github.com/vesoft-inc/nebula/pull/3150)

- 将版本信息移到心跳之外。 [#3378](https://github.com/vesoft-inc/nebula/pull/3378)

- 支持空的列表、集合、映射。 [#3302](https://github.com/vesoft-inc/nebula/pull/3302)

- 支持创建地理索引时指定 s2 区域覆盖参数。[#3396](https://github.com/vesoft-inc/nebula/pull/3396)

- `SHOW HOSTS`中新增版本信息的显示。[#3702](https://github.com/vesoft-inc/nebula/pull/3702)

## Bug fix

- 修复 nGQL 中未指定值时使用默认值的情况下，存在内存没有释放的问题。 [#3666](https://github.com/vesoft-inc/nebula/pull/3666)

- 修复无法使用`coalesce()`函数的问题。 [#3653](https://github.com/vesoft-inc/nebula/pull/3653)

- 修复批量插入时，由于 Tag 已创建索引而导致查找结果错误的问题。[#3627](https://github.com/vesoft-inc/nebula/pull/3627)

- 修复表达式超过深度时的崩溃问题。 [#3606](https://github.com/vesoft-inc/nebula/pull/3606)

- 禁用 nGQL 的`YIELD`子句和`WHERE`子句中的聚合函数。 [#3597](https://github.com/vesoft-inc/nebula/pull/3597)

- 修复在`UNWIND`、`WHERE`子句中使用聚合函数时的崩溃问题。 [#3397](https://github.com/vesoft-inc/nebula/pull/3397) [#3355](https://github.com/vesoft-inc/nebula/pull/3355)

- 修复使用旧 Schema 版本值重建标签索引的问题。[#3332](https://github.com/vesoft-inc/nebula/pull/3332)

- 修复使用`GO...REVERSELY`查询结果会包含过期边的问题。 [#3536](https://github.com/vesoft-inc/nebula/pull/3536)

- 修复 CentOS6 中估计内存信息的错误。 [#3534](https://github.com/vesoft-inc/nebula/pull/3534)

- 修复当`LOOKUP`语句包含一个过滤器，该过滤器由一个逻辑 AND 表达式和一个只有一个元素的 IN 表达式组成时的崩溃问题。 [#3525](https://github.com/vesoft-inc/nebula/pull/3525)

- 修复 metad 在高负载下挂起的问题。 [#3482](https://github.com/vesoft-inc/nebula/pull/3482)

- 修复`UNWIND`子图的崩溃问题。 [#3506](https://github.com/vesoft-inc/nebula/pull/3506)

- 修复重建索引时`DROP SPACE`的崩溃问题。[#3406](https://github.com/vesoft-inc/nebula/pull/3406)

- 修复 cgroup v2 下读取内存统计的问题。 [#3419](https://github.com/vesoft-inc/nebula/pull/3419)

- 修复`DROP TAG INDEX`会删除同名边索引，删除边索引时也会删除同名 TAG 索引的问题。[#3413](https://github.com/vesoft-inc/nebula/pull/3413)

- 修复克隆空间后无法显示边的问题。 [#3351](https://github.com/vesoft-inc/nebula/pull/3351)

- 修复索引存在检查的问题。[#3315](https://github.com/vesoft-inc/nebula/pull/3315)

- 修复执行`ALTER`语句后获取类型属性时可能导致存储获取空指针的问题。 [#3325](https://github.com/vesoft-inc/nebula/pull/3325)

- 优化 raft 从而确保系统更稳定。 [#3172](https://github.com/vesoft-inc/nebula/pull/3172) [#3435](https://github.com/vesoft-inc/nebula/pull/3435) [#3358](https://github.com/vesoft-inc/nebula/pull/3358) [#3322](https://github.com/vesoft-inc/nebula/pull/3322) [#3031](https://github.com/vesoft-inc/nebula/pull/3031)

- 内存比率大于 1.0 时取消内存检查。[#3289](https://github.com/vesoft-inc/nebula/pull/3289)

- 修复使用 Ninja 编译时的错误。 [#3195](https://github.com/vesoft-inc/nebula/pull/3195)

- 修复同时创建同名 Tag 和 Edge type 可能都成功的问题。[#3735](https://github.com/vesoft-inc/nebula/pull/3735)

- 修复当不同的图空间中存在相同的 Tag 或 Edge type 的内部 ID 时，创建全文索引失败的问题。 [#3747](https://github.com/vesoft-inc/nebula/pull/3747)

- 修复`YIELD`子句和 `GO` 语句中变量不一致的问题。[#3430](https://github.com/vesoft-inc/nebula/pull/3430)

- 修复当 Schema 版本大于 256 时的崩溃问题。[#3893](https://github.com/vesoft-inc/nebula/pull/3893)

## Incompatibility

Nebula Graph {{ nebula.release }} 不支持 v2.x 的大部分生态工具，请升级[生态工具](6.eco-tool-version.md)。

- 在配置文件中添加的 Storage 主机无法直接读写，配置文件的作用仅仅是将 Storage 主机注册至 Meta 服务中。必须使用`ADD HOSTS`命令后，才能正常读写 Storage 主机。[#3343](https://github.com/vesoft-inc/nebula/pull/3343)

- 禁用 ZONE 和 GROUP。[#3776](https://github.com/vesoft-inc/nebula/pull/3776) [#3825](https://github.com/vesoft-inc/nebula/pull/3825)  [#3330](https://github.com/vesoft-inc/nebula/pull/3330)

- 禁用`BALANCE DATA`。  [#3756](https://github.com/vesoft-inc/nebula/pull/3756)

- 将默认会话超时时间从`0`修改为`28800`秒，范围从`1`到`604800`秒。 [#3357](https://github.com/vesoft-inc/nebula/pull/3357) [#3807](https://github.com/vesoft-inc/nebula/pull/3807)

- 添加`SHOW LOCAL SESSIONS`和`SHOW LOCAL QUERIES`命令，并弃用`SHOW ALL QUERIES`。 [#3488](https://github.com/vesoft-inc/nebula/pull/3488)

- 从点至少有一个 Tag 修改为可以没有 Tag。`DELETE VERTEX`修改为默认只删除点，不再删除该点关联的出边和入边，此时将默认存在悬挂边。 [#3316](https://github.com/vesoft-inc/nebula/pull/3316) [#3335](https://github.com/vesoft-inc/nebula/pull/3335) [#3328](https://github.com/vesoft-inc/nebula/pull/3328) [#3286](https://github.com/vesoft-inc/nebula/pull/3286)

- 禁用`YIELD`子句返回自定义变量。 [#3271](https://github.com/vesoft-inc/nebula/pull/3271)

- `FETCH`、`GO`、`LOOKUP`、`FIND PATH`、`GET SUBGRAPH`语句中必须添加`YIELD`子句。[#2957](https://github.com/vesoft-inc/nebula/pull/2957) [#3056](https://github.com/vesoft-inc/nebula/pull/3056) [#3139](https://github.com/vesoft-inc/nebula/pull/3139)

- 新增非保留关键字`s2_max_level`、`s2_max_cells`。[#3396](https://github.com/vesoft-inc/nebula/pull/3396)

- MATCH 语句中获取点属性时，必须指定 Tag，例如从`return v.name`变为`return v.player.name`。[#3255](https://github.com/vesoft-inc/nebula/pull/3255)

## 历史版本

[历史版本](https://nebula-graph.com.cn/tags/release-note/)
