# Nebula Graph {{ nebula.release }} release notes

## Feature

- 新增TOSS功能。[#2525](https://github.com/vesoft-inc/nebula/pull/2525)
- 新增Group&Zone功能。[#181](https://github.com/vesoft-inc/nebula-storage/pull/181)
- 新增Geo Spatial功能。[#2954](https://github.com/vesoft-inc/nebula/pull/2954)、[#2979](https://github.com/vesoft-inc/nebula/pull/2979)、[#3043](https://github.com/vesoft-inc/nebula/pull/3043)
- 新增传输加密功能。[#2584](https://github.com/vesoft-inc/nebula/pull/2584)
- 新增服务端返回JSON格式的查询结果。[#2824](https://github.com/vesoft-inc/nebula/pull/2824)
- 新增图空间的meta克隆。[#2763](https://github.com/vesoft-inc/nebula/pull/2763)
- 新增LOOKUP中使用IN表达式。[#2906](https://github.com/vesoft-inc/nebula/pull/2906)
- 集成Breakpad。[#2536](https://github.com/vesoft-inc/nebula/pull/2536)
- 新增将metad的本地文件夹复制到远程。 [#2532](https://github.com/vesoft-inc/nebula/pull/2532)
- 新增DELETE TAG。[#2520](https://github.com/vesoft-inc/nebula/pull/2520)
- 新增concat函数。 [#2540](https://github.com/vesoft-inc/nebula/pull/2540)
- 新增SHOW META LEADER。[#2542](https://github.com/vesoft-inc/nebula/pull/2542)

## Enhancement

- 优化indexscan的Limit下推计算。[#2905](https://github.com/vesoft-inc/nebula/pull/2905)、[#2823](https://github.com/vesoft-inc/nebula/pull/2823)、[#2796](https://github.com/vesoft-inc/nebula/pull/2796)
- 优化GO语句每步采样和Limit下推计算。[#2904](https://github.com/vesoft-inc/nebula/pull/2904)、[#2853](https://github.com/vesoft-inc/nebula/pull/2853)、[#2831](https://github.com/vesoft-inc/nebula/pull/2831)
- 优化YIELD语句的格式。[#2555](https://github.com/vesoft-inc/nebula/pull/2555)、[#2572](https://github.com/vesoft-inc/nebula/pull/2572)、[#2779](https://github.com/vesoft-inc/nebula/pull/2779)、[#2895](https://github.com/vesoft-inc/nebula/pull/2895)、[#2944](https://github.com/vesoft-inc/nebula/pull/2944)
- 默认开启prefix bloom filter以提升性能。[#2860](https://github.com/vesoft-inc/nebula/pull/2860)
- 支持服务端验证客户端版本，可配套使用的客户端版本才允许连接（客户端版本从2.6.0开始）。[#2965](https://github.com/vesoft-inc/nebula/pull/2965)
- 优化流量控制。[#2557](https://github.com/vesoft-inc/nebula/pull/2557)
- SHOW JOBS只显示本SPACE的JOB。[#2872](https://github.com/vesoft-inc/nebula/pull/2872)
- 为除GUEST之外的所有角色授予作业权限。[#2928](https://github.com/vesoft-inc/nebula/pull/2928)
- 优化内存水位检测。[#2885](https://github.com/vesoft-inc/nebula/pull/2885)
- 支持Storage的慢查询终止。[#2534](https://github.com/vesoft-inc/nebula/pull/2534)

## Bug fix

- 修复`raftpart::reset`时清理部分RocksDB数据的问题。[#2522](https://github.com/vesoft-inc/nebula/pull/2522)
- 修复了插入不匹配的日期时间类型的问题。[#2527](https://github.com/vesoft-inc/nebula/pull/2527)
- 修复了设置毫秒失败但微秒有效的问题。[#2781](https://github.com/vesoft-inc/nebula/pull/2781)
- 修复了批量插入过多数据（百万行）时Meta服务崩溃的问题。[#2813](https://github.com/vesoft-inc/nebula/pull/2813)
- 修复了当图空间中不存在边Schema时获取边信息导致崩溃的问题。[#2571](https://github.com/vesoft-inc/nebula/pull/2571)
- 修复了属性数据类型为 `FIXED_STRING` 时 GO WHERE 子句表达式解析错误。[#2762](https://github.com/vesoft-inc/nebula/pull/2762)
- 修复了FIND ALL PATH查询不到的错误。 [#2773](https://github.com/vesoft-inc/nebula/pull/2773)
- 修复了没有配置角色的用户却有查找SPACE的角色权限问题。[#2778](https://github.com/vesoft-inc/nebula/pull/2778)
- 修复了CASE表达式错误。 [#2819](https://github.com/vesoft-inc/nebula/pull/2819)
- 修复了使用time函数时死循环问题。[#2820](https://github.com/vesoft-inc/nebula/pull/2820)
- 修复了当节点被shutdown后，JOB仍显示为运行中的问题。[#2843](https://github.com/vesoft-inc/nebula/pull/2843)
- 修复了在多个副本的情况下，`Insert`语句可能导致副本之间属性值不一致的问题。 [#2862](https://github.com/vesoft-inc/nebula/pull/2862)
- 修复了USE后提交作业时图空间不对的问题。 [#3010](https://github.com/vesoft-inc/nebula/pull/3010)
- 修复了当列不为空时获取thrift结构属性出错的问题。[#3012](https://github.com/vesoft-inc/nebula/pull/3012)
- 修复了Meta服务未同步，graphd也能运行的问题。 [#3069](https://github.com/vesoft-inc/nebula/pull/3069)
- 修复了使用FIND PATH WITH PROP时，悬挂边会返回空顶点的问题。 [#3008](https://github.com/vesoft-inc/nebula/pull/3008)
- 修复了YIELD DISTINCT map类型时的崩溃问题。 [#3051](https://github.com/vesoft-inc/nebula/pull/3051)
- 修复了设置错误的IP或者HOST时服务仍然可以启动的问题。 [#3057](https://github.com/vesoft-inc/nebula/pull/3057)
- 修复了在一个语句中更改相同属性的错误。[#3036](https://github.com/vesoft-inc/nebula/pull/3036)
- 修复了在边上多步过滤无效的问题。[#3144](https://github.com/vesoft-inc/nebula/pull/3144)

## 历史版本

[历史版本](https://nebula-graph.com.cn/tags/release-note/)

