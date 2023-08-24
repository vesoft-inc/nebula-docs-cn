# {{nebula.name}} {{ nebula.release }} release notes

## 优化

- 当`MATCH`语句查询不存在的属性时不再进行全表扫描。
- 支持`MATCH...STARTS WITH`语句的下推。

## 缺陷修复

- 修复连续重启 drainer 导致无法正常停止 drainer 的问题。
- 修复单个大查询可能导致 Graph 服务崩溃的问题。
- 修复`FIND ALL PATH`语句导致内存不足的问题。
- 修复`MATCH`语句中添加路径变量导致`all()`函数下推优化失效的问题。
- 修复低版本 Linux 内核使用 Boost 生成 UUID 时报错的问题。
- 修复`MATCH...shortestpath()`语句进行循环检测时报错的问题。
- 修复使用管道符（`|`）删除边时 Graph 服务崩溃的问题。
- 修复`MATCH`语句进行多跳查询时边属性无法显示的问题。
- 修复`shortestPath()`函数导致 Graph 服务崩溃的问题。
- 修复`FIND ALL PATH`语句查找点的自环时未返回自环路径的问题。
- 修复`GO`的复合语句中多个子句使用同一个变量时，重复执行该复合语句会返回不同结果的问题。
- 修复`CREATE SPACE...AS`语句克隆出的图空间中，新建索引会覆盖旧索引的问题。
- 修复`GO...UNION ALL`语句在某些场景下报错的问题。

## 历史版本

[历史版本](https://yueshu.com.cn/tags/%E5%8F%91%E7%89%88%E8%AF%B4%E6%98%8E)
