# {{nebula.name}} {{ nebula.release }} release notes

## 功能

- 支持通过 License Center 和 License Manager 管理 License。 
- 支持`MATCH`语句的无索引全表扫描。
- 支持在返回语句中使用像`v.tag`这样的表达式。
- 支持 UPDATE 语句中的`json_extract`函数。 
- 支持在 EXPLAIN 输出中使用 TCK 格式。 
- DML 支持参数。
- 增强全文索引功能。

## 优化

- 支持以毫秒为单位的 TTL。
- 增强了聚合函数中的属性裁剪功能。
- 提高了遍历执行器的性能。
- 重构了 ALL PATH 以提高性能。
- 为了提高性能，移除了一些 Raft 锁。
- 优化了谓词函数过滤变长边。
- 并行遍历执行器。 
- MATCH 支持 ID 集合。
- 重构了 GO planner。 
- 在配置文件中添加了一些 Graph 性能选项。
- 添加了最大连接数标志。 
- 支持使用`MATCH`语句检索 VID 或属性索引时使用变量。

## 缺陷修复

- 修复了 RocksDB 导入数据导致 Leader lease 无效的缺陷。 
- 修复了当用户不存在时`DESC USER`提示信息错误的缺陷。
- 修复了 SPACE 存在时，`CREATE IF NOT EXIST`将无法成功的缺陷。 
- 修复了在计划中 GetNeighbors 边的方向错误的缺陷。
- 修复了`SHOW SESSIONS`命令中客户端 IP 格式的缺陷。
- 修复了在 USE 和 MATCH 时属性被剪枝的缺陷。 
- 修复了在某些情况下过滤器未下推的缺陷。
- 修复了在某些情况下过滤器错误地过滤的缺陷。
- 修复了模式表达式中内部变量处理不正确的缺陷。 
- 修复了涉及 EMPTY 比较的缺陷。
- 修复了 MATCH 中请求所有列时返回重复列的缺陷。
- 修复了在自反边涉及路径的比较错误的缺陷。
- 修复了 MATCH 路径中重新定义别名的缺陷。
- 修复了插入地理位置值时的类型检查缺陷。
- 修复了最短路径崩溃的缺陷。
- 修复了 GEO 崩溃的缺陷。
- 修复了在逻辑表达式评估中存储崩溃的缺陷。
- 修复了`MATCH...contains`报错的缺陷。
- 修复了并发时会话计数错误的 bug。
- 修复了 SUBGRAPH 和 PATH 参数的缺陷。 
- 修复了正则表达式的缺陷。
- 修复了非表达式下推的缺陷。
- 修复了集群切换的缺陷。

## 变更

- 禁用`edge list join`, 不支持在多个模式中使用边列表。
- 移除 GLR 解析器, 需要将`YIELD 1–-1`修改为`YIELD 1– -1`。
  
## 历史版本

[历史版本](https://yueshu.com.cn/tags/%E5%8F%91%E7%89%88%E8%AF%B4%E6%98%8E)
