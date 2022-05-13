# 审计日志

Nebula Graph 的审计日志功能可以将 Graph 服务接受到的所有操作进行分类存储，然后提供给终端用户查看，终端用户可以根据需要，追踪指定类型的操作。

!!! enterpriseonly

    仅企业版支持本功能。

## 日志类别

|类别|语句|说明|
|:--|:--|:--|
|`login` |-| 客户端尝试连接 Graph 服务时，记录相关信息。 |
|`exit`  |-| 断开与 Graph 服务的连接时，记录相关信息。 |
|`ddl` |`CREATE SPACE`、`DROP SPACE`、`CREATE TAG`、`DROP TAG`、`ALTER TAG`、`DELETE TAG`、`CREATE EDGE`、`DROP EDGE`、`ALTER EDGE`、`CREATE INDEX`、`REBUILD INDEX`、`DROP INDEX`、`CREATE FULLTEXT INDEX`、`REBUILD FULLTEXT INDEX`、`DROP FULLTEXT INDEX`|记录 DDL 语句的信息。 |
|`dql` |`MATCH`、`LOOKUP`、`GO`、`FETCH`、`GET SUBGRAPH`、`FIND PATH`、`UNWIND`、`GROUP BY`、`ORDER BY`、`YIELD`、`LIMIT`、`RETURN`|记录 DQL 语句的信息。|
|`dml` |`INSERT VERTEX`、`DELETE VERTEX`、`UPDATE VERTEX`、`UPSERT VERTEX`、`INSERT EDGE`、`DELETE EDGE`、`UPDATE EDGE`、`UPSERT EDGE`|记录 DML 语句的信息。 |
|`dcl`|`CREATE USER`、`GRANT ROLE`、`REVOKE ROLE`、`CHANGE PASSWORD`、`ALTER USER`、`DROP USER`、`CREATE SNAPSHOT`、`DROP SNAPSHOT`、`ADD LISTENER`、`REMOVE LISTENER`、`BALANCE`、`SUBMIT JOB`、`STOP JOB`、`RECOVER JOB`、`ADD DRAINER`、`REMOVE DRAINER`|记录 DCL 语句的信息。|
|`util`|`SHOW HOSTS`、`SHOW USERS`、`SHOW ROLES`、`SHOW SNAPSHOTS`、`SHOW SPACES`、`SHOW PARTS`、`SHOW TAGS`、`SHOW EDGES`、`SHOW INDEXES`、`SHOW CREATE SPACE`、`SHOW CREATE TAG/EDGE`、`SHOW CREATE INDEX`、`SHOW INDEX STATUS`、`SHOW LISTENER`、`SHOW TEXT SEARCH CLIENTS`、`SHOW DRAINER CLIENTS`、`SHOW FULLTEXT INDEXES`、`SHOW CONFIGS`、`SHOW CHARSET`、`SHOW COLLATION`、`SHOW STATS`、`SHOW SESSIONS`、`SHOW META LEADER`、`SHOW DRAINERS`、`SHOW QUERIES`、`SHOW JOB`、`SHOW JOBS`、`DESCRIBE INDEX`、`DESCRIBE EDGE`、`DESCRIBE TAG`、`DESCRIBE SPACE`、`DESCRIBE USER`、`USE SPACE`、`SIGN IN TEXT SERVICE`、`SIGN OUT TEXT SERVICE`、`SIGN IN DRAINER SERVICE`、`SIGN OUT DRAINER SERVICE`、`EXPLAIN`、`PROFILE`、`KILL QUERY`、`DOWNLOAD HDFS`、`INGEST`|记录工具类语句的信息。 |
|`unknown`|-|记录未能识别的语句。|

## 设置审计日志

使用审计日志需要修改集群内的所有 Graph 服务的配置（`nebula-graphd.conf`），默认路径为`/usr/local/nebula/etc/nebula-graphd.conf`。

!!! note

    修改配置后，需要重启 Graph 服务才能生效。

与审计日志相关的参数说明如下。

|参数|预设值|说明|
|:--|:--|:--|
| `enable_audit` | `false` | 是否开启审计日志。 |
| `audit_log_handler` | `file` | 审计日志的存储方案。可选值为`file`（本地文件）和`es`（Elasticsearch）。 |
| `audit_log_file` | `./logs/audit/audit.log` | 仅在`audit_log_handler=file`时生效。审计日志的存储路径，支持相对路径或绝对路径。 |
| `audit_log_strategy` | `synchronous` | 仅在`audit_log_handler=file`时生效。审计日志的同步方案。可选值为`asynchronous`和`synchronous`。设置为`asynchronous`时，日志事件使用内存缓冲，不会阻塞主线程，但是可能会因为缓存不够而导致日志缺失；设置为`synchronous`时，日志事件每次都刷新并同步到文件中。 |
| `audit_log_max_buffer_size` | `1048576` |仅在`audit_log_handler=file`、`audit_log_strategy=asynchronous`时生效。审计日志的缓存大小。单位：字节。  |
| `audit_log_format` | `xml` | 仅在`audit_log_handler=file`时生效。审计日志的格式。可选值为`xml`、`json`和`csv`。 |
| `audit_log_es_address` | - | 仅在`audit_log_handler=es`时生效。Elasticsearch 服务器的地址。格式为`IP1:port1, IP2:port2, ...`。 |
| `audit_log_es_user` | - | 仅在`audit_log_handler=es`时生效。登录 Elasticsearch 服务器的用户名。 |
| `audit_log_es_password`     | -  | 仅在`audit_log_handler=es`时生效。Elasticsearch 用户名对应的密码。  |
| `audit_log_es_batch_size`      | `1000`  | 仅在`audit_log_handler=es`时生效。每次发送至 Elasticsearch 服务器的日志条数。  |
| `audit_log_exclude_spaces`      | -  | 不需要记录日志的图空间列表。多个图空间用英文逗号（,）分隔。  |
| `audit_log_categories`      | `login,exit`  | 需要记录日志的分类列表。多个类别用英文逗号（,）分隔。  |

## 审计日志格式

不同的存储方案和不同的格式，日志内的字段是相同的。以默认路径（`logs/audit/audit.log`）和默认 XML 格式为例说明各个字段的含义。

```bash
<AUDIT_RECORD
  CATEGORY="util"
  TIMESTAMP="2022-04-07 02:31:38"
  TERMINAL=""
  CONNECTION_ID="1649298693144580"
  CONNECTION_STATUS="0"
  CONNECTION_MESSAGE=""
  USER="root"
  CLIENT_HOST="127.0.0.1"
  HOST="192.168.8.111"
  SPACE=""
  QUERY="use basketballplayer1"
  QUERY_STATUS="-1005"
  QUERY_MESSAGE="SpaceNotFound: "
/>
<AUDIT_RECORD
  CATEGORY="util"
  TIMESTAMP="2022-04-07 02:31:39"
  TERMINAL=""
  CONNECTION_ID="1649298693144580"
  CONNECTION_STATUS="0"
  CONNECTION_MESSAGE=""
  USER="root"
  CLIENT_HOST="127.0.0.1"
  HOST="192.168.8.111"
  SPACE=""
  QUERY="use basketballplayer"
  QUERY_STATUS="0"
  QUERY_MESSAGE=""
/>
```

|字段|说明|
|:--|:--|
|`CATEGORY`| 日志类别。|
|`TIMESTAMP`| 日志生成时间。 |
|`TERMINAL`| 保留字段，暂不支持。|
|`CONNECTION_ID`| 连接的会话ID。 |
|`CONNECTION_STATUS`| 连接的状态码。`0`表示成功，其他数字代表不同的错误信息。|
|`CONNECTION_MESSAGE`| 如果连接出错，会显示报错信息。|
|`USER`| 连接的用户名。 |
|`CLIENT_HOST`| 客户端的 IP 地址。 |
|`HOST`| 连接的机器的 IP 地址。 |
|`SPACE`| 执行查询的图空间。|
|`QUERY`| 查询语句。|
|`QUERY_STATUS`| 查询状态。`0`表示成功，其他数字代表不同的错误信息。|
|`QUERY_MESSAGE`| 如果查询出错，会显示报错信息。|
