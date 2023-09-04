# NebulaGraph 企业版 {{ nebula.release }} release notes

## 优化

- 优化读取目的点的 Tag 的性能。

## 缺陷修复

- 修复连续重启 drainer 导致无法正常停止 drainer 的问题。
- 修复单个大查询导致 Graph 服务崩溃的问题。
- 修复集群主从切换时 Schema 被覆盖的问题。
- 修复在触发`GraphMemoryExceeded`的前提下重复执行`FIND ALL PATH`语句导致 Graph 服务崩溃的问题。
- 修复使用管道符（`|`）删除边时 Graph 服务崩溃的问题。
- 修复低版本 Linux 内核使用 Boost 生成 UUID 时报错的问题。
- 修复`CREATE SPACE...AS`语句克隆出的图空间中，新建索引会覆盖旧索引的问题。
- 修复`GO...UNION ALL`语句在某些场景下报错的问题。
- 修复`FIND ALL PATH`语句查找点的自环时未返回自环路径的问题。
- 修复`shortestPath()`函数导致 Graph 服务崩溃的问题。
- 修复`GetDstBySrc`算子没有截断超级节点的问题。

## 历史版本

[历史版本](https://www.nebula-graph.com.cn/tags/%E5%8F%91%E7%89%88%E8%AF%B4%E6%98%8E)
