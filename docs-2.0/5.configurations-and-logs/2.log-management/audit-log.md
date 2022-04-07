# 审计日志

Nebula Graph 的审计日志功能可以将 Graph 服务接受到的所有操作进行分类存储，用户可以根据需要，追踪指定类型的操作。

!!! enterpriseonly

    仅企业版支持本功能。

## 日志类别

|类别|说明|
|:--|:--|
|`LOGIN` |客户端尝试连接 Graph 服务时，记录相关信息。 |
|`EXIT`  | 断开与 Graph 服务的连接时，记录相关信息。 |
|`DDL` |记录 DDL 语句的信息，包括元数据的变化信息。例如`CREATE SPACE`、`ALTER TAG`、`REBUILD INDEX`等。 |
|`DQL` |记录 DQL 语句的信息，包括查询、排序等信息。例如`MATCH`、`GO`、`GET SUBGRAPH`、`ORDER BY`、`YIELD`、`RETURN`等。|
|`DML` |记录 DML 语句的信息，包括实际数据的变化信息。例如`INSERT VERTEX`、`INSERT EDGE`、`DELETE EDGE`等。 |
|`DCL`|记录 DCL 语句的信息，包括用户创建授权、快照、作业等运维信息。例如`CREATE USER`、`CREATE SNAPSHOT`、`ADD LISTENER`、`BALANCE`等。|
|`UTIL`|记录工具类语句的信息，包括`SHOW`、`DESCRIBE`、`USE`、`SIGN IN`、`KILL QUERY`、`INGEST`等语句。 |
|`unknown`|记录未能识别的语句。|

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
|       |   |   |

## 审计日志格式

不同的存储方案和不同的格式，日志内的字段是相同的。以默认路径（`logs/audit/audit.log`）和默认 XML 格式为例说明各个字段的含义。

```bash
<AUDIT_RECORD
  CATEGORY="util"
  TIMESTAMP="2022-03-29 06:42:32"
  TERMINAL=""
  CONNECTION_ID="1648536147065194"
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
<AUDIT_RECORD
  CATEGORY="ddl"
  TIMESTAMP="2022-03-29 06:42:40"
  TERMINAL=""
  CONNECTION_ID="1648536147065194"
  CONNECTION_STATUS="0"
  CONNECTION_MESSAGE=""
  USER="root"
  CLIENT_HOST="127.0.0.1"
  HOST="192.168.8.111"
  SPACE="basketballplayer"
  QUERY=" create tag test1(name string)"
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