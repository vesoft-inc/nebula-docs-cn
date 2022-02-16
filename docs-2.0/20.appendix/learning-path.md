# Nebula Graph 学习路径

本文介绍 Nebula Graph 学习路径，用户可以通过路径中的文档及视频由浅入深地学习图数据库 Nebula Graph。

 ![learning path](learning-path.png)

## 1. 关于 Nebula Graph

### 1.1 什么是 Nebula Graph？

| 文档                                                         | 视频                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [什么是 Nebula Graph](https://docs.nebula-graph.com.cn/{{nebula.release}}/1.introduction/1.what-is-nebula-graph/) | [Nebula Graph 介绍](https://www.bilibili.com/video/BV1kf4y1v7LM)、[万亿级别的图数据库 Nebula Graph](https://www.bilibili.com/video/BV1aK4y1e7Q4?spm_id_from=333.999.0.0)|


### 1.2 图相关术语

  | 视频                                                         |
  | ------------------------------------------------------------ |
  | [图世界的那些概念、术语](https://www.bilibili.com/video/BV17X4y1A7p9) |
  | [图数据库简述](https://www.bilibili.com/video/BV1vJ41187nN)|


### 1.3 数据模型
  
  | 文档                                                         |
  | ------------------------------------------------------------ |
  | [数据模型](https://docs.nebula-graph.com.cn/{{nebula.release}}/1.introduction/2.data-model/) |



### 1.4 路径
  
| 文档                                                         | 视频                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------- |
| [路径](https://docs.nebula-graph.com.cn/{{nebula.release}}/1.introduction/2.1.path/) | [路径类型](https://www.bilibili.com/video/BV1Uf4y1t72L) |



### 1.5 产品架构

  | 文档                                                         | 视频                                                         |
  | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | [Meta 服务](https://docs.nebula-graph.com.cn/{{nebula.release}}/1.introduction/3.nebula-graph-architecture/2.meta-service/) | -                                                            |
  | [Graph 服务](https://docs.nebula-graph.com.cn/{{nebula.release}}/1.introduction/3.nebula-graph-architecture/3.graph-service/) | - |
  | [Storage 服务](https://docs.nebula-graph.com.cn/{{nebula.release}}/1.introduction/3.nebula-graph-architecture/4.storage-service/) | - |
  


## 2. 快速入门

### 2.1 安装 Nebula Graph

  | 文档                                                         | 视频                                                         |
  | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | [使用 RPM/DEB 包](https://docs.nebula-graph.com.cn/{{nebula.release}}/4.deployment-and-installation/2.compile-and-install-nebula-graph/2.install-nebula-graph-by-rpm-or-deb/) | -                                                            |
  | [使用 TAR 包](https://docs.nebula-graph.com.cn/{{nebula.release}}/4.deployment-and-installation/2.compile-and-install-nebula-graph/4.install-nebula-graph-from-tar/) | -                                                            |
  | [使用 Docker](https://docs.nebula-graph.com.cn/{{nebula.release}}/4.deployment-and-installation/2.compile-and-install-nebula-graph/3.deploy-nebula-graph-with-docker-compose/) | - |
  | [使用源码](https://docs.nebula-graph.com.cn/{{nebula.release}}/4.deployment-and-installation/2.compile-and-install-nebula-graph/1.install-nebula-graph-by-compiling-the-source-code/) | [图数据库入门教程（零）通过编译源码来安装 Nebula Graph](https://www.bilibili.com/video/BV1YJ411i7Jn?spm_id_from=333.999.0.0)                                                             |
  |-|[如何选择部署方式？](https://www.bilibili.com/video/BV1vy4y1K7S5)|

### 2.2 启动 Nebula Graph

  | 文档                                                         |
  | ------------------------------------------------------------ |
  | [启停 Nebula Graph](https://docs.nebula-graph.com.cn/{{nebula.release}}/2.quick-start/5.start-stop-service/) |

### 2.3 连接 Nebula Graph

  | 文档
  | ------------------------------------------------------------ |
  | [连接 Nebula Graph](https://docs.nebula-graph.com.cn/{{nebula.release}}/2.quick-start/3.connect-to-nebula-graph/) |

### 2.4 使用 nGQL 命令

  | 文档|
  | ------------------------------------------------------------ |
  | [nGQL 命令汇总](https://docs.nebula-graph.com.cn/{{nebula.release}}/2.quick-start/6.cheatsheet-for-ngql-command/) |  

## 3. 进阶操作

### 3.1 部署多机集群

  | 文档 |
  | ------------------------------------------------------------ |
  | [使用 RPM/DEB 包部署 Nebula Graph 多机集群](https://docs.nebula-graph.com.cn/{{nebula.release}}/4.deployment-and-installation/2.compile-and-install-nebula-graph/deploy-nebula-graph-cluster/) |  

### 3.2 升级集群版本

  | 文档                                                         |
  | ------------------------------------------------------------ |
  | [升级 Nebula Graph](https://docs.nebula-graph.com.cn/{{nebula.release}}/4.deployment-and-installation/3.upgrade-nebula-graph/upgrade-nebula-graph-to-latest/) |

### 3.3 配置Nebula

  | 文档                                                         |
  | ------------------------------------------------------------ |
  | [配置 Meta](https://docs.nebula-graph.com.cn/{{nebula.release}}/5.configurations-and-logs/1.configurations/2.meta-config/) |
  | [配置 Graph](https://docs.nebula-graph.com.cn/{{nebula.release}}/5.configurations-and-logs/1.configurations/3.graph-config/) |
  | [配置 Storage](https://docs.nebula-graph.com.cn/{{nebula.release}}/5.configurations-and-logs/1.configurations/4.storage-config/) |
  | [配置 Linux 内核](https://docs.nebula-graph.com.cn/{{nebula.release}}/5.configurations-and-logs/1.configurations/6.kernel-config/) |

### 3.4 配置日志

| 文档 |
| ------------------------------------------------------------ |
|[日志配置](https://docs.nebula-graph.com.cn/{{nebula.release}}/5.configurations-and-logs/2.log-management/logs/) |

### 3.5 运维与管理

- 账号鉴权和授权

  | 文档                                                         |
  | ------------------------------------------------------------ |
  | [本地身份验证](https://docs.nebula-graph.com.cn/{{nebula.release}}/7.data-security/1.authentication/1.authentication/#_2) |
  | [OpenLDAP](https://docs.nebula-graph.com.cn/{{nebula.release}}/7.data-security/1.authentication/4.ldap/) |
  | [管理用户](https://docs.nebula-graph.com.cn/{{nebula.release}}/7.data-security/1.authentication/2.management-user/) |
  | [内置角色](https://docs.nebula-graph.com.cn/{{nebula.release}}/7.data-security/1.authentication/3.role-list/) |

- 平衡分片分布

  | 文档 |
  | ------------------------------------------------------------ |
  |[Storage 负载均衡](https://docs.nebula-graph.com.cn/{{nebula.release}}/8.service-tuning/load-balance/)|

- 监控

  | 文档                                                         |
  | ------------------------------------------------------------ |
  | [Nebula 指标](https://docs.nebula-graph.com.cn/{{nebula.release}}/6.monitor-and-metrics/1.query-performance-metrics/) |
  | [RocksDB 统计数据](https://docs.nebula-graph.com.cn/{{nebula.release}}/6.monitor-and-metrics/2.rocksdb-statistics/) |

- 数据快照

  | 文档 |
  | ------------------------------------------------------------ |
  |[创建快照](https://docs.nebula-graph.com.cn/{{nebula.release}}/7.data-security/3.manage-snapshot/#_5)|

<!--
- 资源隔离

  | 文档 |
  | ------------------------------------------------------------ |
  |[Group & Zone](https://docs.nebula-graph.com.cn/{{nebula.release}}/7.data-security/5.zone/)|
-->

- SSL 加密

  | 文档|
  | ------------------------------------------------------------ |
  |[SSL 加密](https://docs.nebula-graph.com.cn/{{nebula.release}}/7.data-security/4.ssl/)|


### 3.6 性能调优

  | 文档     |视频|
  | ------------------- |------------------- |
  | [图建模](https://docs.nebula-graph.com.cn/{{nebula.release}}/8.service-tuning/2.graph-modeling/) |[Nebula 高性能图 schema 设计](https://www.bilibili.com/video/BV1r64y1R72i?)|
  | [系统建模](https://docs.nebula-graph.com.cn/{{nebula.release}}/8.service-tuning/3.system-design/) |-|
  | [Compaction 策略](https://docs.nebula-graph.com.cn/{{nebula.release}}/8.service-tuning/compaction/) |-|


 
### 3.7 周边工具

- 可视化

  | 可视化工具     | 文档                                                         | 视频                                                         |
  | -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | 数据可视化     | [Nebula Graph Studio](https://docs.nebula-graph.com.cn/{{nebula.release}}/nebula-studio/about-studio/st-ug-what-is-graph-studio/) | [Nebula Studio 图探索功能](https://www.bilibili.com/video/BV1QN411Z7Vh)和[Nebula Graph Studio 可视化建模](https://www.bilibili.com/video/BV19A411L77h?spm_id_from=333.999.0.0) |
  | 数据监控和运维 | [Nebula Dashboard 企业版](https://docs.nebula-graph.com.cn/{{nebula.release}}/nebula-dashboard-ent/1.what-is-dashboard-ent/)和 [Nebula Dashboard 社区版](https://docs.nebula-graph.com.cn/{{nebula.release}}/nebula-dashboard/1.what-is-dashboard/) | [可视化监控 Nebula Dashboard](https://www.bilibili.com/video/BV1qQ4y1k7gb?)                                                            |
  | 数据分析       | [Nebula Explorer 企业版](https://docs.nebula-graph.com.cn/{{nebula.release}}/nebula-explorer/about-explorer/ex-ug-what-is-explorer/) | [可视化图探索 Nebula Explorer](https://www.bilibili.com/video/BV1fP4y1h7Fx?)                                                            |


- 数据导入与导出

  | 导入与导出 | 文档                                                         | 视频                                                         |
  | -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | 数据导入       | [Nebula Importer](https://docs.nebula-graph.com.cn/{{nebula.release}}/nebula-importer/use-importer/) | [Nebula Importer](https://www.bilibili.com/video/BV1ny4y1u7i4) |
  | 数据导入       | [Nebula Spark Connector](https://docs.nebula-graph.com.cn/{{nebula.release}}/nebula-spark-connector/) | -                                                            |
  | 数据导入       | [Nebula Flink Connector](https://docs.nebula-graph.com.cn/{{nebula.release}}/nebula-flink-connector/) | -                                                            |
  | 数据导入       | [Nebula Exchange 社区版](https://docs.nebula-graph.com.cn/{{nebula.release}}/nebula-exchange/about-exchange/ex-ug-what-is-exchange/) | [Nebula Graph 数据导入工具——Exchange](https://www.bilibili.com/video/BV1Pq4y177D9)、[Exchange 导入 SST 数据](https://www.bilibili.com/video/BV1y34y1o7Di?)  |
  | 数据导出       | [Nebula Exchange 企业版](https://docs.nebula-graph.com.cn/{{nebula.release}}/nebula-exchange/about-exchange/ex-ug-what-is-exchange/) | -                                                            |
  
- 性能测试

  | 文档                                                         |
  | ------------------------------------------------------------ |
  | [Nebula Bench](https://docs.nebula-graph.com.cn/{{nebula.release}}/nebula-bench/) |

<!-- - 集群运维

  | 文档  |视频|
  | -------- |---------|
  | [Nebula Operator](https://docs.nebula-graph.com.cn/{{nebula.release}}/nebula-operator/1.introduction-to-nebula-operator/) |[Nebula Operator](https://www.bilibili.com/video/BV1rP4y1x7fX)、[ 云原生的演进](https://www.bilibili.com/video/BV1A5411N7vs)|
 -->
- 图算法 

  | 文档   |视频|
  | ------- |------ |
  | [Nebula Algorithm](https://docs.nebula-graph.com.cn/{{nebula.release}}/nebula-algorithm/) |[Nebula Algorithm 介绍](https://www.bilibili.com/video/BV1fB4y1T7XK)|

- 客户端

  | 文档                                                         |
  | ------------------------------------------------------------ |
  | [Nebula Console](https://docs.nebula-graph.com.cn/2.6.1/2.quick-start/3.connect-to-nebula-graph/) |
  | [Nebula CPP](https://docs.nebula-graph.com.cn/2.6.1/14.client/3.nebula-cpp-client/) |
  | [Nebula Java](https://docs.nebula-graph.com.cn/2.6.1/14.client/4.nebula-java-client/) |
  | [Nebula Python](https://docs.nebula-graph.com.cn/2.6.1/14.client/5.nebula-python-client/) |
  | [Nebula Go](https://docs.nebula-graph.com.cn/2.6.1/14.client/6.nebula-go-client/) |


## 4. 高阶操作

  | 文档                                                         |
  | ------------------------------------------------------------ |
  | [API & SDK](https://docs.nebula-graph.com.cn/{{nebula.release}}/20.appendix/6.eco-tool-version/#apisdk) |


## 5. 最佳实践

  | 文档 & 视频                                                         |
  | ------------------------------------------------------------ |
  | [LDBC 数据导入及 nGQL 实践](https://nebula-graph.com.cn/posts/query-graph-with-ldbc-dataset/) |
  | [基于 Nebula Graph 的 Betweenness Centrality 算法](https://nebula-graph.com.cn/posts/introduction-to-betweenness-centrality-algorithm/) |
  | [百亿级图数据在快手安全情报的应用与挑战](https://nebula-graph.com.cn/posts/kuaishou-security-intelligence-platform-with-nebula-graph/) |
  | [美团图数据库平台建设及业务实践](https://nebula-graph.com.cn/posts/meituan-graph-database-platform-practice/) |
  | [Akulaku 的智能风控实践](https://nebula-graph.com.cn/posts/intelligent-risk-control-practice-akulaku/) |
  | [微信使用 Nebula Graph 的定制化开发](https://nebula-graph.com.cn/posts/nebula-graph-for-social-networking/) |
  | [知乎使用 Nebula Graph 实践](https://mp.weixin.qq.com/s/K2QinpR5Rplw1teHpHtf4w) |
  |[Nebula Graph 在微众银行的数据治理业务的实践](https://www.bilibili.com/video/BV1Pr4y1F7kA)|
  |[图数据库在安全风控场景的应用 @BOSS 直聘](https://www.bilibili.com/video/BV1Rh41117G9)|
  |[更多文档](https://nebula-graph.com.cn/posts/)   、[视频](https://space.bilibili.com/472621355/channel/series)                |
## 6. 常见问题

  | 文档                                                         |
  | ------------------------------------------------------------ |
  | [常见问题 FAQ](https://docs.nebula-graph.com.cn/{{nebula.release}}/20.appendix/0.FAQ/#faq) |
## 7. 实操作业

 用户可以通过完成以下实操作业来检测是否玩转 Nebula Graph。

  | 作业内容                                                | 参考                                                         |
  | ------------------------------------------------------- | ------------------------------------------------------------ |
  | 编译内核                                                | [使用源码安装 Nebula Graph](https://docs.nebula-graph.com.cn/{{nebula.release}}/4.deployment-and-installation/2.compile-and-install-nebula-graph/1.install-nebula-graph-by-compiling-the-source-code/)                                                             |
  | 部署可视化工具 Studio、Dashboard、Explorer             | [部署 Studio](https://docs.nebula-graph.com.cn/{{nebula.release}}/nebula-studio/deploy-connect/st-ug-deploy/)、[部署 Dashboard](https://docs.nebula-graph.com.cn/{{nebula.release}}/nebula-dashboard/2.deploy-dashboard/)、[部署 Explorer](https://docs.nebula-graph.com.cn/{{nebula.release}}/nebula-explorer/deploy-connect/ex-ug-deploy/)                                                            |
  | 使用 K6 压测 Nebula Graph                               | [K6 在 Nebula Graph 上的压测实践](https://nebula-graph.com.cn/posts/practice-k6-at-nebula-graph/) |
  | 导入 LDBC 数据                                          | [LDBC 数据导入及 nGQL 实践](https://mp.weixin.qq.com/s/tbLGuuX6vNzLIw6o8ZGKpw)                                                           |
  | 查询 LDBC 数据（点查、K度邻居查询、路径查询、子图查询） | [LDBC](chrome-extension://gfbliohnnapiefjpjlpjnehglfpaknnc/pages/pdf_viewer.html?r=http://ldbcouncil.org/ldbc_snb_docs/ldbc-snb-specification.pdf) 和 [interactive-short-1.cypher](https://github.com/ldbc/ldbc_snb_interactive/blob/main/cypher/queries/interactive-short-1.cypher) |


## 8. 通过 CI/CP 考试

图数据库 Nebula Graph 提供2个不同等级的图数据库技能认证考试：

- Nebula Graph Certified Insider (NGCI)：通过该考试证明用户对图数据库及 Nebula Graph 有基础的了解，是合格的 Nebula Graph 使用者。

- Nebula Graph Certified Professional (NGCP)：通过该考试证明用户对图数据库及 Nebula Graph 有深入的了解，是 Nebula Graph 专业人士。

考试用书[《开源分布式图数据库 Nebula Graph 完全指南》](https://docs.nebula-graph.com.cn/site/pdf/NebulaGraph-book.pdf)

单击[Nebula Graph （第N期） 个人技能认证](https://discuss.nebula-graph.com.cn/t/topic/5253)查看考试入口及考试开放和截止时间。
