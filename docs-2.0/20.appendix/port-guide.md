# 产品端口全集

以下是{{nebula.name}}内核及周边工具使用的默认端口信息：

| 序号 | 所属产品/服务          | 类型 | 默认端口                      | 说明                                                         |
| :--- | :--------------------- | :--- | :---------------------------- | :----------------------------------------------------------- |
| 1    | {{nebula.name}}            | TCP  | 9669                          | Graph 服务的 RPC 守护进程监听端口（通常用于客户端连接Graph服务）。 |
| 2    | {{nebula.name}}            | TCP  | 19669                         | Graph 服务的 HTTP 端口。                                     |
| 3    | {{nebula.name}}            | TCP  | 19670                         | Graph 服务的 HTTP/2 端口。（3.x 后已弃用该端口）                    |
| 4    | {{nebula.name}}            | TCP  | 9559                          | Meta 服务的 RPC 守护进程监听端口。（通常由 Graph 服务和 Storage 服务发起请求，用于获取和更新图数据库的元数据信息。 |
| 5    | {{nebula.name}}            | TCP  | 9560                          | Meta 服务之间的 Raft 通信端口。                              |
| 6    | {{nebula.name}}            | TCP  | 19559                         | Meta 服务的 HTTP 端口。                                      |
| 7    | {{nebula.name}}            | TCP  | 19560                         | Meta 服务的 HTTP/2 端口。（3.x 后已弃用该端口）                     |
| 8    | {{nebula.name}}            | TCP  | 9777                          | Storage 服务中，Drainer 服务占用端口（仅在企业版集群中暴露）。 |
| 9    | {{nebula.name}}            | TCP  | 9778                          | Storage 服务中，Admin 服务占用端口。                         |
| 10   | {{nebula.name}}            | TCP  | 9779                          | Storage 服务的 RPC 守护进程监听端口。（通常由 Graph 服务发起请求，用于执行数据存储相关的操作，例如读取、写入或删除数据。） |
| 11   | {{nebula.name}}            | TCP  | 9780                          | Storage 服务之间的 Raft 通信端口。                           |
| 12   | {{nebula.name}}            | TCP  | 19779                         | Storage 服务的 HTTP 端口。                                   |
| 13   | {{nebula.name}}            | TCP  | 19780                         | Storage 服务的 HTTP/2 端口。（3.x 后已弃用该端口）                  |
| 14   | {{nebula.name}}            | TCP  | 8888                          | 备份和恢复功能的 Agent 服务端口。Agent 是集群中每台机器的一个守护进程，用于启停{{nebula.name}}服务和上传、下载备份文件。 |
| 15   | {{nebula.name}}            | TCP  | 9789、9790、9788 | 全文索引中 Raft Listener 的端口，从 Storage 服务读取数据，然后将它们写入 Elasticsearch 集群。<br/>也是集群间数据同步中 Storage Listener 的端口。用于同步主集群的 Storage 数据。端口 9790、9788 由端口 9789 加一减一后自动生成。 |
| 16   | {{nebula.name}}            | TCP  | 9200                          | {{nebula.name}}使用该端口与 Elasticsearch 进行 HTTP 通信，以执行全文搜索查询和管理全文索引。 |
| 17   | {{nebula.name}}            | TCP  | 9569、9570、9568| 集群间数据同步功能中 Meta Listener 的端口，用于同步主集群的 Meta 数据。端口 9570、9568 由端口 9569 加一减一后自动生成。 |
| 18   | {{nebula.name}}            | TCP  | 9889、9890、9888 | 集群间数据同步功能中 Drainer 服务端口。用于同步 Storage、Meta 数据给从集群。端口 9890、9888 由端口 9889 加一减一后自动生成。|
| 19   | NebulaGraph Studio     | TCP  | 7001                          | Studio 提供 Web 服务占用端口。                               |
| 20   | {{dashboard_ent.name}} | TCP  | 8090                          | Nebula HTTP Gateway 依赖服务端口。为集群服务提供 HTTP 接口，执行 nGQL 语句与{{nebula.name}}数据库进行交互。 |
| 21   | {{dashboard_ent.name}} | TCP  | 9200                          | Nebula Stats Exporter 依赖服务端口。收集集群的性能指标，包括服务 IP 地址、版本和监控指标（例如查询数量、查询延迟、心跳延迟 等）。 |
| 22   | {{dashboard_ent.name}} | TCP  | 9100                          | Node Exporter 依赖服务端口。收集集群中机器的资源信息，包括 CPU、内存、负载、磁盘和流量。 |
| 23   | {{dashboard_ent.name}} | TCP  | 9091                          | Prometheus 服务的端口。存储监控数据的时间序列数据库。        |
| 24   | NebulaGraph Dashboard | TCP  | 7003                          | Dashboard 社区版 提供 Web 服务占用端口。                     |
| 25   | {{dashboard_ent.name}} | TCP  | 7005                          | {{dashboard_ent.name}}提供 Web 服务占用端口。                     |
| 26   | {{dashboard_ent.name}} | TCP  | 9093                          | Alertmanager 服务的端口。接收 Prometheus 告警，发送告警通知给{{dashboard_ent.name}}。 |
| 27   | {{explorer.name}}  | TCP  | 7002                          | {{explorer.name}}提供的 Web 服务占用端口。                           |
| 28   | License Manager  | TCP  | 9119                          | License Manager (LM) 服务的端口。LM 服务用于管理 License（仅在企业版集群中使用）。| 
