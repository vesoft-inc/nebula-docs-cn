# 错误码

{{nebula.name}}运行出现问题时，会返回错误码。本文介绍错误码的详细信息。

!!! note
    {{comm.comm_begin}}
    - 如果出现错误但没有返回错误码，或错误码描述不清，请在[论坛](https://discuss.nebula-graph.com.cn/)或 [GitHub](https://github.com/vesoft-inc/nebula/issues) 反馈。
    {{comm.comm_end}}
    - 返回`0`表示执行成功。

|错误名称|错误码|说明|
|:---|:---|:---|
|`E_DISCONNECTED`|`-1`| 连接断开 |
|`E_FAIL_TO_CONNECT`|`-2`| 无法建立连接 |
|`E_RPC_FAILURE`|`-3`| RPC 失败 |
|`E_LEADER_CHANGED`|`-4`| Raft leader 变更|
|`E_SPACE_NOT_FOUND`|`-5`| 图空间不存在 |
|`E_TAG_NOT_FOUND`|`-6`| Tag 不存在 |
|`E_EDGE_NOT_FOUND`|`-7`| Edge type不存在 |
|`E_INDEX_NOT_FOUND`|`-8`| 索引不存在|
|`E_EDGE_PROP_NOT_FOUND`|`-9`| 边属性不存在|
|`E_TAG_PROP_NOT_FOUND`|`-10`| Tag 属性不存在|
|`E_ROLE_NOT_FOUND`|`-11`| 当前角色不存在|
|`E_CONFIG_NOT_FOUND`|`-12`| 当前配置不存在|
|`E_MACHINE_NOT_FOUND`|`-13`| 当前主机不存在|
|`E_LISTENER_NOT_FOUND`|`-15`| listener 不存在|
|`E_PART_NOT_FOUND`|`-16`| 当前分区不存在|
|`E_KEY_NOT_FOUND`|`-17`| key 不存在|
|`E_USER_NOT_FOUND`|`-18`| 用户不存在|
|`E_STATS_NOT_FOUND`|`-19`| 统计信息不存在|
|`E_SERVICE_NOT_FOUND`|`-20`| 没有找到当前服务|
|`E_DRAINER_NOT_FOUND`|`-21`| drainer 不存在|
|`E_DRAINER_CLIENT_NOT_FOUND`|`-22`| drainer 客户端不存在|
|`E_PART_STOPPED`|`-23`| 当前 partition 已经被停止|
|`E_BACKUP_FAILED`|`-24`| 备份失败|
|`E_BACKUP_EMPTY_TABLE`|`-25`| 备份的表为空|
|`E_BACKUP_TABLE_FAILED`|`-26`| 备份表失败|
|`E_PARTIAL_RESULT`|`-27`| multiget 无法获得所有数据|
|`E_REBUILD_INDEX_FAILED`|`-28`| 重建索引失败|
|`E_INVALID_PASSWORD`|`-29`| 密码无效|
|`E_FAILED_GET_ABS_PATH`|`-30`| 无法获得绝对路径|
|`E_BAD_USERNAME_PASSWORD`|`-1001`| 身份验证失败|
|`E_SESSION_INVALID`|`-1002`| 无效会话|
|`E_SESSION_TIMEOUT`|`-1003`| 会话超时|
|`E_SYNTAX_ERROR`|`-1004`| 语法错误|
|`E_EXECUTION_ERROR`|`-1005`| 执行错误|
|`E_STATEMENT_EMPTY`|`-1006`| 语句为空|
|`E_BAD_PERMISSION`|`-1008`| 权限不足|
|`E_SEMANTIC_ERROR`|`-1009`| 语义错误|
|`E_TOO_MANY_CONNECTIONS`|`-1010`| 超出最大连接数|
|`E_PARTIAL_SUCCEEDED`|`-1011`| 访问存储失败（仅有部分请求成功）|
|`E_NO_HOSTS`|`-2001`| 主机不存在|
|`E_EXISTED`|`-2002`| 主机已经存在|
|`E_INVALID_HOST`|`-2003`| 无效主机|
|`E_UNSUPPORTED`|`-2004`| 当前命令、语句、功能不支持|
|`E_NOT_DROP`|`-2005`|不允许删除|
|`E_CONFIG_IMMUTABLE`|`-2007`| 配置项不能改变|
|`E_CONFLICT`|`-2008`| 参数与 meta 数据冲突|
|`E_INVALID_PARM`|`-2009`| 无效的参数|
|`E_WRONGCLUSTER`|`-2010`| 错误的集群|
|`E_ZONE_NOT_ENOUGH`|`-2011`| listener 冲突|
|`E_ZONE_IS_EMPTY`|`-2012`| 主机不存在|
|`E_SCHEMA_NAME_EXISTS`|`-2013`| Schema 名字已存在|
|`E_RELATED_INDEX_EXISTS`|`-2014`| 与 Tag 或 Edge Type 相关的索引存在，不能被删除 |
|`E_RELATED_SPACE_EXISTS`|`-2015`| 仍有图空间在主机上，不能被删除|
|`E_STORE_FAILURE`|`-2021`| 存储数据失败|
|`E_STORE_SEGMENT_ILLEGAL`|`-2022`| 存储段非法|
|`E_BAD_BALANCE_PLAN`|`-2023`| 无效的数据均衡计划|
|`E_BALANCED`|`-2024`| 集群已经处于数据均衡状态|
|`E_NO_RUNNING_BALANCE_PLAN`|`-2025`| 没有正在运行的数据均衡计划|
|`E_NO_VALID_HOST`|`-2026`| 缺少有效的主机|
|`E_CORRUPTED_BALANCE_PLAN`|`-2027`| 已经损坏的数据均衡计划|
|`E_IMPROPER_ROLE`|`-2030`| 回收用户角色失败|
|`E_INVALID_PARTITION_NUM`|`-2031`| 无效的分区数量|
|`E_INVALID_REPLICA_FACTOR`|`-2032`| 无效的副本因子|
|`E_INVALID_CHARSET`|`-2033`| 无效的字符集|
|`E_INVALID_COLLATE`|`-2034`| 无效的字符排序规则|
|`E_CHARSET_COLLATE_NOT_MATCH`|`-2035`| 字符集和字符排序规则不匹配|
|`E_SNAPSHOT_FAILURE`|`-2040`| 生成快照失败|
|`E_BLOCK_WRITE_FAILURE`|`-2041`| 写入块数据失败|
|`E_ADD_JOB_FAILURE`|`-2044`| 增加新的任务失败|
|`E_STOP_JOB_FAILURE`|`-2045`| 停止任务失败|
|`E_SAVE_JOB_FAILURE`|`-2046`| 保存任务信息失败|
|`E_BALANCER_FAILURE`|`-2047`| 数据均衡失败|
|`E_JOB_NOT_FINISHED`|`-2048`| 当前任务还没有完成|
|`E_TASK_REPORT_OUT_DATE`|`-2049`| 任务报表失效|
|`E_JOB_NOT_IN_SPACE`|`-2050`| 当前任务不在图空间内|
|`E_JOB_NEED_RECOVER`|`-2051`| 当前任务需要恢复|
|`E_JOB_ALREADY_FINISH`|`-2052`| 任务已经失败或完成 |
|`E_JOB_SUBMITTED`|`-2053`| 任务默认状态 |
|`E_JOB_NOT_STOPPABLE`|`-2054`| 给定任务不支持停止 |
|`E_JOB_HAS_NO_TARGET_STORAGE`|`-2055`| leader 分布未上报，因此无法将任务发送到存储 |
|`E_INVALID_JOB`|`-2065`| 无效的任务|
|`E_BACKUP_BUILDING_INDEX`|`-2066`| 备份终止（正在创建索引）|
|`E_BACKUP_SPACE_NOT_FOUND`|`-2067`| 备份时图空间不存在|
|`E_RESTORE_FAILURE`|`-2068`| 备份恢复失败|
|`E_SESSION_NOT_FOUND`|`-2069`| 会话不存在|
|`E_LIST_CLUSTER_FAILURE`|`-2070`| 获取集群信息失败|
|`E_LIST_CLUSTER_GET_ABS_PATH_FAILURE`|`-2071`| 获取集群信息时无法获取绝对路径|
|`E_LIST_CLUSTER_NO_AGENT_FAILURE`|`-2072`| 获取集群信息时无法获得 agent|
|`E_QUERY_NOT_FOUND`|`-2073`| query 未找到|
|`E_AGENT_HB_FAILURE`|`-2074`| agent 没有汇报心跳|
|`E_HOST_CAN_NOT_BE_ADDED`|`-2082`| 该主机不能被添加，因为它不是一个 Storage 主机|
|`E_ACCESS_ES_FAILURE`|`-2090`| 访问 Elasticsearch 失败|
|`E_GRAPH_MEMORY_EXCEEDED`|`-2600`| Graph 内存超出|
|`E_CONSENSUS_ERROR`|`-3001`| 选举时无法达成共识|
|`E_KEY_HAS_EXISTS`|`-3002`| key 已经存在|
|`E_DATA_TYPE_MISMATCH`|`-3003`| 数据类型不匹配|
|`E_INVALID_FIELD_VALUE`|`-3004`| 无效的字段值|
|`E_INVALID_OPERATION`|`-3005`| 无效的操作|
|`E_NOT_NULLABLE`|`-3006`| 当前值不允许为空|
|`E_FIELD_UNSET`|`-3007`| 字段非空或者没有默认值时，字段值必须设置|
|`E_OUT_OF_RANGE`|`-3008`| 取值超出了当前类型的范围|
|`E_DATA_CONFLICT_ERROR`|`-3010`| 数据冲突|
|`E_WRITE_STALLED`|`-3011`| 写入被延迟|
|`E_IMPROPER_DATA_TYPE`|`-3021`| 不正确的数据类型|
|`E_INVALID_SPACEVIDLEN`|`-3022`| VID 长度无效|
|`E_INVALID_FILTER`|`-3031`| 无效的过滤器|
|`E_INVALID_UPDATER`|`-3032`| 无效的字段更新|
|`E_INVALID_STORE`|`-3033`| 无效的 KV 存储|
|`E_INVALID_PEER`|`-3034`| peer 无效|
|`E_RETRY_EXHAUSTED`|`-3035`| 重试次数耗光|
|`E_TRANSFER_LEADER_FAILED`|`-3036`| leader 转换失败|
|`E_INVALID_STAT_TYPE`|`-3037`| 无效的统计类型|
|`E_INVALID_VID`|`-3038`| VID 无效|
|`E_LOAD_META_FAILED`|`-3040`| 加载元信息失败|
|`E_FAILED_TO_CHECKPOINT`|`-3041`| 生成 checkpoint 失败|
|`E_CHECKPOINT_BLOCKED`|`-3042`| 生成 checkpoint 被阻塞|
|`E_FILTER_OUT`|`-3043`| 数据被过滤|
|`E_INVALID_DATA`|`-3044`| 无效的数据|
|`E_MUTATE_EDGE_CONFLICT`|`-3045`| 并发写入同一条边发生冲突|
|`E_MUTATE_TAG_CONFLICT`|`-3046`| 并发写入同一个点发生冲突|
|`E_OUTDATED_LOCK`|`-3047`| 锁已经失效|
|`E_INVALID_TASK_PARA`|`-3051`| 无效的任务参数|
|`E_USER_CANCEL`|`-3052`| 用户取消了任务|
|`E_TASK_EXECUTION_FAILED`|`-3053`| 任务执行失败|
|`E_PLAN_IS_KILLED`|`-3060`| 执行计划被清除|
|`E_NO_TERM`|`-3070`| 收到请求时心跳流程未完成|
|`E_OUTDATED_TERM`|`-3071`| 收到旧 leader 的过时心跳（已选举出新的 leader）|
|`E_WRITE_WRITE_CONFLICT`|`-3073`| 并发写入时与后到的请求发生冲突|
|`E_RAFT_UNKNOWN_PART`|`-3500`| 未知的分区|
|`E_RAFT_LOG_GAP`|`-3501`| raft 日志落后|
|`E_RAFT_LOG_STALE`|`-3502`| raft 日志过期|
|`E_RAFT_TERM_OUT_OF_DATE`|`-3503`| 心跳信息已经过期|
|`E_RAFT_UNKNOWN_APPEND_LOG`|`-3504`| 未知的追加日志|
|`E_RAFT_WAITING_SNAPSHOT`|`-3511`| 等待快照完成|
|`E_RAFT_SENDING_SNAPSHOT`|`-3512`| 发送快照过程出错|
|`E_RAFT_INVALID_PEER`|`-3513`| 无效的接收端|
|`E_RAFT_NOT_READY`|`-3514`| Raft 没有启动|
|`E_RAFT_STOPPED`|`-3515`| Raft 已经停止|
|`E_RAFT_BAD_ROLE`|`-3516`| 错误的角色|
|`E_RAFT_WAL_FAIL`|`-3521`| 写入 WAL 失败|
|`E_RAFT_HOST_STOPPED`|`-3522`| 主机已经停止|
|`E_RAFT_TOO_MANY_REQUESTS`|`-3523`| 请求数量过多|
|`E_RAFT_PERSIST_SNAPSHOT_FAILED`|`-3524`| 持久化快照失败|
|`E_RAFT_RPC_EXCEPTION`|`-3525`| RPC 异常|
|`E_RAFT_NO_WAL_FOUND`|`-3526`| 没有发现 WAL 日志|
|`E_RAFT_HOST_PAUSED`|`-3527`| 主机暂停|
|`E_RAFT_WRITE_BLOCKED`|`-3528`| 写入被堵塞|
|`E_RAFT_BUFFER_OVERFLOW`|`-3529`| 缓存溢出|
|`E_RAFT_ATOMIC_OP_FAILED`|`-3530`| 原子操作失败|
|`E_LEADER_LEASE_FAILED`|`-3531`| leader 租约过期|
|`E_RAFT_CAUGHT_UP`|`-3532`| Raft 已经同步数据|
|`E_STORAGE_MEMORY_EXCEEDED`|`-3600`|Storage 内存超出|
|`E_LOG_GAP`|`-4001`| drainer 日志落后|
|`E_LOG_STALE`|`-4002`| drainer 日志过期|
|`E_INVALID_DRAINER_STORE`|`-4003`| drainer 数据存储无效|
|`E_SPACE_MISMATCH`|`-4004`| 图空间不匹配|
|`E_PART_MISMATCH`|`-4005`| 分区不匹配|
|`E_DATA_CONFLICT`|`-4006`| 数据冲突|
|`E_REQ_CONFLICT`|`-4007`| 请求冲突|
|`E_DATA_ILLEGAL`|`-4008`| 数据非法|
|`E_CACHE_CONFIG_ERROR`|`-5001`| 缓存配置错误|
|`E_NOT_ENOUGH_SPACE`|`-5002`| 空间不足|
|`E_CACHE_MISS`|`-5003`| 没有命中缓存|
|`E_POOL_NOT_FOUND`|`-5005`| 写缓存失败|
|`E_NODE_NUMBER_EXCEED_LIMIT`|`-7001`| 机器节点数超出限制|
|`E_PARSING_LICENSE_FAILURE`|`-7002`| 解析证书失败|
|`E_UNKNOWN`|`-8000`| 未知错误|

<!--
|``|`-14`| zone 不存在|
|``|`-2012`| zone 数量不足|
|``|`-2013`| Zone 为空|
|``|`-5004`| |
|``|`-2043`| |
|``|`-2006`| |
|``|`-2029`| 缺少有效的 drainer|
|``|`-3061`| 客户端和服务端版本不兼容|
|``|`-3062`| 获取 ID 序号失败|
-->
