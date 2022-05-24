### Graph

| 参数                                           | 说明                                      |
| ---------------------------------------------- | ----------------------------------------- |
| `num_active_queries`                             | 当前正在执行的查询数。                    |
| `num_active_sessions`                            | 当前活跃的会话数量。                      |
| `num_aggregate_executors`                        | 聚合（Aggregate）算子执行时间。               |
| `num_auth_failed_sessions_bad_username_password` | 因用户名密码错误导验证失败的会话数量。    |
| `num_auth_failed_sessions_out_of_max_allowed`    | 因为超过`FLAG_OUT_OF_MAX_ALLOWED_CONNECTIONS`参数导致的验证登录的失败的 session 数量。|
| `num_auth_failed_sessions`                       | 登录验证失败的会话数量。                  |
| `num_indexscan_executors`                        | 索引扫描（IndexScan）算子执行时间。           |
| `num_killed_queries`                             | 被终止的查询数量。                        |
| `num_opened_sessions`                            | 服务端建立过的会话数量。                  |
| `num_queries`                                    | 查询次数。                                |
| `num_query_errors_leader_changes`                | 因查询错误而导致的 Leader 变更的次数。      |
| `num_query_errors`                               | 查询错误次数。                            |
| `num_reclaimed_expired_sessions`                 | 服务端主动回收的过期的会话数量。          |
| `num_rpc_sent_to_metad_failed`                   | Graphd 服务发给 Metad 的 RPC 请求失败的数量。          |
| `num_rpc_sent_to_metad`                          | Graphd 服务发给 Metad 服务的 RPC 请求数量。          |
| `num_rpc_sent_to_storaged_failed`                | Graphd 服务发给 Storaged 服务的 RPC 请求失败的数量。 |
| `num_rpc_sent_to_storaged`                       | Graphd 服务发给 Storaged 服务的 RPC 请求数量。        |
| `num_sentences`                                  | Graphd 服务接收的语句数。                        |
| `num_slow_queries`                               | 慢查询次数。                              |
| `num_sort_executors`                             | 排序（Sort）算子执行时间。                    |
| `optimizer_latency_us`                           | 优化器阶段延迟时间。                          |
| `query_latency_us`                               | 查询平均延迟时间。                            |
| `slow_query_latency_us`                          | 慢查询平均延迟时间。                          |
| `num_queries_hit_memory_watermark`               | 达到内存水位线的语句的数量。 |

### Meta

| 参数                       | 说明                                |
| -------------------------- | ----------------------------------- |
| `commit_log_latency_us`      | Raft 协议中 Commit 日志的延迟时间。 |
| `commit_snapshot_latency_us` | Raft 协议中 Commit 快照的延迟时间。 |
| `heartbeat_latency_us`       | 心跳延迟时间。                          |
| `num_heartbeats`             | 心跳次数。                          |
| `num_raft_votes`             | Raft 协议中投票的次数。             |
| `transfer_leader_latency_us` | Raft 协议中转移 Leader 的延迟时间。 |
| `num_agent_heartbeats`        | AgentHBProcessor 心跳次数。|
| `agent_heartbeat_latency_us`  | AgentHBProcessor 延迟时间。|

### Storage

| 参数                         | 说明                                                |
| ---------------------------- | --------------------------------------------------- |
| `add_edges_atomic_latency_us`  | 添加边单次延迟。                                    |
| `add_edges_latency_us`         | 添加边的平均延迟时间。                                  |
| `add_vertices_latency_us`      | 添加点的平均延迟时间。                                  |
| `commit_log_latency_us`        | Raft 协议中 Commit 日志的延迟时间。                 |
| `commit_snapshot_latency_us`   | Raft 协议中 Commit 快照的延迟时间。                 |
| `delete_edges_latency_us`      | 删除边的平均延迟时间。                                  |
| `delete_vertices_latency_us`   | 删除点的平均延迟时间。                                  |
| `get_neighbors_latency_us`     | 查询邻居平均延迟时间。                                  |
| `num_get_prop`                 | GetPropProcessor 执行的次数。                       |
| `num_get_neighbors_errors`     | GetNeighborsProcessor 执行出错的次数。               |
| `get_prop_latency_us`          | GetPropProcessor 执行的延迟时间。|
| `num_edges_deleted`            | 删除的边数量。                                      |
| `num_edges_inserted`           | 插入的边数量。                                      |
| `num_raft_votes`               | Raft 协议中投票的次数。                             |
| `num_rpc_sent_to_metad_failed` | Storaged 服务发给 Metad 服务的 RPC 请求失败的数量。 |
| `num_rpc_sent_to_metad`        | Storaged 服务发给 Metad 服务的 RPC 请求数量。       |
| `num_tags_deleted`             | 删除的 Tag 数量。                                   |
| `num_vertices_deleted`         | 删除的点数量。                                      |
| `num_vertices_inserted`        | 插入的点数量。                                      |
| `transfer_leader_latency_us`   | Raft 协议中转移 Leader 的延迟时间。                 |
| `lookup_latency_us`            | LookupProcessor 执行的延迟时间。                        |
| `num_lookup_errors`            | LookupProcessor 执行时出错的次数。|
| `num_scan_vertex`              | ScanVertexProcessor 执行的次数。|
| `num_scan_vertex_errors`       | ScanVertexProcessor 执行时出错的次数。|
| `update_edge_latency_us`       | UpdateEdgeProcessor 执行的延迟时间。|
| `num_update_vertex`            | UpdateVertexProcessor 执行的次数。|
| `num_update_vertex_errors`     | UpdateVertexProcessor 执行时出错的次数。|
| `kv_get_latency_us`            | Getprocessor 的延迟时间。|
| `kv_put_latency_us`            | PutProcessor 的延迟时间。|
| `kv_remove_latency_us`         | RemoveProcessor 的延迟时间。|
| `num_kv_get_errors`            | GetProcessor 执行出错次数。|
| `num_kv_get`                   | GetProcessor 执行次数。|
| `num_kv_put_errors`            | PutProcessor 执行出错次数。|
| `num_kv_put`                   | PutProcessor 执行次数。|
| `num_kv_remove_errors`         | RemoveProcessor 执行出错次数。|
| `num_kv_remove`                | RemoveProcessor 执行次数。|
| `forward_tranx_latency_us`     | 传输平均延迟时间。|

### 图空间级别监控指标

| 参数                                           | 说明                                      |
| ---------------------------------------------- | ----------------------------------------- |
| `num_active_queries`                             | 当前正在执行的查询数。                    |
| `num_queries`                                    | 查询次数。                                |
| `num_sentences`                                  | Graphd 服务接收的语句数。                        |
| `optimizer_latency_us`                           | 优化器阶段延迟时间。                          |
| `query_latency_us`                               | 查询平均延迟时间。                            |
| `num_slow_queries`                               | 慢查询次数。                              |
| `num_query_errors`                               | 查询报错语句数量。|
| `num_query_errors_leader_changes`                | 因查询错误而导致的 Leader 变更的次数。      |
| `num_killed_queries`                             | 被终止的查询数量。                        |
| `num_aggregate_executors`                        | 聚合（Aggregate）算子执行时间。               |
| `num_sort_executors`                             | 排序（Sort）算子执行时间。                    |
| `num_indexscan_executors`                        | 索引扫描（IndexScan）算子执行时间。           |
| `num_oom_queries`                                | 导致内存耗尽的语句数量。|

