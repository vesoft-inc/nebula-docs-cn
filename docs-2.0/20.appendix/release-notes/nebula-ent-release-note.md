# NebulaGraph 企业版 {{ nebula.release }} release notes

## 缺陷修复

- 修复了 MATCH 语句出现错误过滤的缺陷。
- 修复了表达式包含未定义参数时崩溃的缺陷。
- 修复了一元 NOT 表达式的下推缺陷。
- 修复了使用`USE SPACE`和`MATCH`组合使用的缺陷。
- 修复了涉及 EMPTY 的比较缺陷。
- 修复了查询最短路径时崩溃的缺陷。
- 修复了 Storaged 上的 eval contains 过滤器缺陷。
- 修复了与正则表达式有关的 MATCH 语句的缺陷。
- 修复了 GEO 数据类型导致崩溃的缺陷。
- 修复了 thrift 服务器启动失败时，无法通过信号停止 Graphd 的缺陷。

## 历史版本

[历史版本](https://www.nebula-graph.com.cn/tags/%E5%8F%91%E7%89%88%E8%AF%B4%E6%98%8E)
