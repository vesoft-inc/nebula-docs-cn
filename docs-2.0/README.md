# 欢迎阅读Nebula Graph {{ nebula.release }} 文档

!!! note "本文档更新时间{{ now().year }}-{{ now().month }}-{{ now().day }}, [GitHub commit](https://github.com/vesoft-inc/nebula-docs-cn) {{ git.short_commit }}."

Nebula Graph是一款开源的、分布式的、易扩展的原生图数据库，能够承载数十亿个点和数万亿条边的超大规模数据集，并且提供毫秒级查询。

## 教学视频

- [YouTube](https://www.youtube.com/channel/UC73V8q795eSEMxDX4Pvdwmw/)

- [bilibili](https://space.bilibili.com/472621355)

## 快速开始

* [简介](1.introduction/1.what-is-nebula-graph.md)
* [开始流程](2.quick-start/1.quick-start-workflow.md)
* [FAQ](2.quick-start/0.FAQ.md)

<!--
## 介绍

- [什么是Nebula Graph](1.introduction/1.what-is-nebula-graph.md)

## 快速入门（适合初学者）

- [快速入门](2.quick-start/1.quick-start-workflow.md)

- [Docker Compose部署Nebula Graph](2.quick-start/2.deploy-nebula-graph-with-docker-compose.md)

- [连接Nebula Graph](2.quick-start/3.connect-to-nebula-graph.md)

- [基础操作语法](2.quick-start/4.nebula-graph-crud.md)

## nGQL指南（适合所有用户）

<!-- to be updated -->
- nGQL概述
  - [Nebula Graph查询语言（nGQL）](3.ngql-guide/1.nGQL-overview/1.overview.md)
  - [图建模](3.ngql-guide/1.nGQL-overview/2.graph-modeling.md)
  - [模式](3.ngql-guide/1.nGQL-overview/3.graph-patterns.md)
- 数据类型
  - [数值](3.ngql-guide/3.data-types/1.numeric.md)
  - [布尔](3.ngql-guide/3.data-types/2.boolean.md)
  - [字符串](3.ngql-guide/3.data-types/3.string.md)
  - [日期时间](3.ngql-guide/3.data-types/4.date-and-time.md)
  - [NULL](3.ngql-guide/3.data-types/5.null.md)
  - [列表](3.ngql-guide/3.data-types/6.list.md)
  - [集合](3.ngql-guide/3.data-types/7.set.md)
  - [映射](3.ngql-guide/3.data-types/8.map.md)
  - [类型转换](3.ngql-guide/3.data-types/9.type-conversion.md)

- 变量和复合查询
  - [复合查询](3.ngql-guide/4.variable-and-composite-queries/1.composite-queries.md)
  - [自定义变量](3.ngql-guide/4.variable-and-composite-queries/2.user-defined-variables.md)
  - [引用属性](3.ngql-guide/4.variable-and-composite-queries/3.property-reference.md)

- 运算符
  - [比较符](3.ngql-guide/5.operators/1.comparison.md)
  - [布尔符](3.ngql-guide/5.operators/2.boolean.md)
  - [管道符](3.ngql-guide/5.operators/4.pipe.md)
  - [属性引用符](3.ngql-guide/5.operators/5.property-reference.md)
  - [集合运算符](3.ngql-guide/5.operators/6.set.md)
  - [字符串运算符](3.ngql-guide/5.operators/7.string.md)
  - [列表运算符](3.ngql-guide/5.operators/8.list.md)
  - [运算符优先级](3.ngql-guide/5.operators/9.precedence.md)

- 函数和表达式
  - [数学函数](3.ngql-guide/6.functions-and-expressions/1.math.md)
  - [字符串函数](3.ngql-guide/6.functions-and-expressions/2.string.md)
  - [日期时间函数](3.ngql-guide/6.functions-and-expressions/3.date-and-time.md)
  - [Schema函数](3.ngql-guide/6.functions-and-expressions/4.schema.md)
  - [CASE表达式](3.ngql-guide/6.functions-and-expressions/5.case-expressions.md)
  - [列表函数](3.ngql-guide/6.functions-and-expressions/6.list.md)
  - [count函数](3.ngql-guide/6.functions-and-expressions/7.count.md)
  - [collect函数](3.ngql-guide/6.functions-and-expressions/10.collect.md)
  - [reduce函数](3.ngql-guide/6.functions-and-expressions/11.reduce.md)
  - [hash函数](3.ngql-guide/6.functions-and-expressions/12.hash.md)
  - [谓词函数](3.ngql-guide/6.functions-and-expressions/8.predicate.md)
  - [自定义函数](3.ngql-guide/6.functions-and-expressions/9.user-defined-functions.md)

- 通用查询语句
  - [Match](3.ngql-guide/7.general-query-statements/2.match.md)
  - [LOOKUP](3.ngql-guide/7.general-query-statements/5.lookup.md)
  - [GO](3.ngql-guide/7.general-query-statements/3.go.md)
  - [FETCH](3.ngql-guide/7.general-query-statements/4.fetch.md)
  - [UNWIND](3.ngql-guide/7.general-query-statements/7.unwind.md)
  - SHOW
    - [SHOW CHARSET](3.ngql-guide/7.general-query-statements/6.show/1.show-charset.md)
    - [SHOW COLLATION](3.ngql-guide/7.general-query-statements/6.show/2.show-collation.md)
    - [SHOW CREATE SPACE](3.ngql-guide/7.general-query-statements/6.show/4.show-create-space.md)
    - [SHOW CREATE TAGS/EDGES](3.ngql-guide/7.general-query-statements/6.show/5.show-create-tags-edges.md)
    - [SHOW HOSTS](3.ngql-guide/7.general-query-statements/6.show/6.show-hosts.md)
    - [SHOW INDEX STATUS](3.ngql-guide/7.general-query-statements/6.show/7.show-index-status.md)
    - [SHOW INDEXES](3.ngql-guide/7.general-query-statements/6.show/8.show-indexes.md)
    - [SHOW PARTS](3.ngql-guide/7.general-query-statements/6.show/9.show-parts.md)
    - [SHOW ROLES](3.ngql-guide/7.general-query-statements/6.show/10.show-roles.md)
    - [SHOW SNAPSHOTS](3.ngql-guide/7.general-query-statements/6.show/11.show-snapshots.md)
    - [SHOW SPACES](3.ngql-guide/7.general-query-statements/6.show/12.show-spaces.md)
    - [SHOW STATS](3.ngql-guide/7.general-query-statements/6.show/14.show-stats.md)
    - [SHOW TAGS/EDGES](3.ngql-guide/7.general-query-statements/6.show/15.show-tags-edges.md)
    - [SHOW USERS](3.ngql-guide/7.general-query-statements/6.show/16.show-users.md)

- 子句和选项
  - [GROUP BY](3.ngql-guide/8.clauses-and-options/group-by.md)
  - [LIMIT and SKIP](3.ngql-guide/8.clauses-and-options/limit.md)
  - [ORDER BY](3.ngql-guide/8.clauses-and-options/order-by.md)
  - [RETURN](3.ngql-guide/8.clauses-and-options/return.md)
  - [TTL](3.ngql-guide/8.clauses-and-options/ttl-options.md)
  - [WHERE](3.ngql-guide/8.clauses-and-options/where.md)
  - [YIELD](3.ngql-guide/8.clauses-and-options/yield.md)
  - [WITH](3.ngql-guide/8.clauses-and-options/with.md)

- 图空间语句
  - [CREATE SPACE](3.ngql-guide/9.space-statements/1.create-space.md)
  - [USE SPACE](3.ngql-guide/9.space-statements/2.use-space.md)
  - [SHOW SPACES](3.ngql-guide/9.space-statements/3.show-spaces.md)
  - [DESCRIBE SPACE](3.ngql-guide/9.space-statements/4.describe-space.md)
  - [DROP SPACE](3.ngql-guide/9.space-statements/5.drop-space.md)

- 标签语句
  - [CREATE TAG](3.ngql-guide/10.tag-statements/1.create-tag.md)
  - [DROP TAGS](3.ngql-guide/10.tag-statements/2.drop-tag.md)
  - [ALTER TAG](3.ngql-guide/10.tag-statements/3.alter-tag.md)
  - [SHOW TAGS](3.ngql-guide/10.tag-statements/4.show-tags.md)
  - [DESCRIBE TAG](3.ngql-guide/10.tag-statements/5.describe-tag.md)

- 边类型语句
  - [CREATE EDGE](3.ngql-guide/11.edge-type-statements/1.create-edge.md)
  - [DROP EDGE](3.ngql-guide/11.edge-type-statements/2.drop-edge.md)
  - [ALTER EDGE](3.ngql-guide/11.edge-type-statements/3.alter-edge.md)
  - [SHOW EDGES](3.ngql-guide/11.edge-type-statements/4.show-edges.md)
  - [DESCRIBE EDGE](3.ngql-guide/11.edge-type-statements/5.describe-edge.md)

- 点语句
  - [INSERT VERTEX](3.ngql-guide/12.vertex-statements/1.insert-vertex.md)
  - [DELETE VERTEX](3.ngql-guide/12.vertex-statements/4.delete-vertex.md)
  - [UPDATE VERTEX](3.ngql-guide/12.vertex-statements/2.update-vertex.md)
  - [UPSERT VERTEX](3.ngql-guide/12.vertex-statements/3.upsert-vertex.md)

- 边语句
  - [INSERT EDGE](3.ngql-guide/13.edge-statements/1.insert-edge.md)
  - [DELETE EDGE](3.ngql-guide/13.edge-statements/4.delete-edge.md)
  - [UPDATE EDGE](3.ngql-guide/13.edge-statements/2.update-edge.md)
  - [UPSERT EDGE](3.ngql-guide/13.edge-statements/3.upsert-edge.md)

- 原生索引
  - [索引介绍](3.ngql-guide/14.native-index-statements/README.md)
  - [CREATE INDEX](3.ngql-guide/14.native-index-statements/1.create-native-index.md)
  - [SHOW INDEX](3.ngql-guide/14.native-index-statements/2.show-native-indexes.md)
  - [SHOW CREATE INDEX](3.ngql-guide/14.native-index-statements/2.1.show-create-index.md)
  - [DESCRIBE INDEX](3.ngql-guide/14.native-index-statements/3.describe-native-index.md)
  - [REBUILD INDEX](3.ngql-guide/14.native-index-statements/4.rebuild-native-index.md)
  - [SHOW INDEX STATUS](3.ngql-guide/14.native-index-statements/5.show-native-index-status.md)
  - [DROP INDEX](3.ngql-guide/14.native-index-statements/6.drop-native-index.md)

- 全文索引
  - [索引介绍](3.ngql-guide/14.native-index-statements/README.md)
  - [全文索引限制](4.deployment-and-installation/6.deploy-text-based-index/1.text-based-index-restrictions.md)
  - [部署全文索引](4.deployment-and-installation/6.deploy-text-based-index/2.deploy-es.md)
  - [部署Raft listener](4.deployment-and-installation/6.deploy-text-based-index/3.deploy-listener.md)
  - [全文搜索](3.ngql-guide/15.full-text-index-statements/1.search-with-text-based-index.md)

- 子图和路径
  - [GET SUBGRAPH](3.ngql-guide/16.subgraph-and-path/1.get-subgraph.md)
  - [FIND PATH](3.ngql-guide/16.subgraph-and-path/2.find-path.md)

- 查询调优
  - [EXPLAIN和PROFILE](3.ngql-guide/17.query-tuning-statements/1.explain-and-profile.md)

- 运维

  - [BALANCE](3.ngql-guide/18.operation-and-maintenance-statements/2.balance-syntax.md)
  - [作业管理](3.ngql-guide/18.operation-and-maintenance-statements/4.job-statements.md)

- 附录

  - [注释](3.ngql-guide/20.appendix/comments.md)
  - [大小写区分](3.ngql-guide/20.appendix/identifier-case-sensitivity.md)
  - [关键字](3.ngql-guide/20.appendix/keywords-and-reserved-words.md)
  - [点ID和分片ID](3.ngql-guide/20.appendix/vid-partition.md)

## 部署和安装 (适合开发和DBA)

- [准备资源](4.deployment-and-installation/1.resource-preparations.md)
- 编译安装Nebula Graph
  - [源码编译安装](4.deployment-and-installation/2.compile-and-install-nebula-graph/1.install-nebula-graph-by-compiling-the-source-code.md)
  - [RPM/DEB包安装](4.deployment-and-installation/2.compile-and-install-nebula-graph/2.install-nebula-graph-by-rpm-or-deb.md)
- [部署Nebula Graph集群](4.deployment-and-installation/deploy-nebula-graph-cluster.md)
- [升级Nebula Graph](4.deployment-and-installation/3.upgrade-nebula-graph.md)
-->
