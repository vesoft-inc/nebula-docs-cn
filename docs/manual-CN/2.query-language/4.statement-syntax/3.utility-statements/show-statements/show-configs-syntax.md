# SHOW CONFIGS 语法

```ngql
SHOW CONFIGS [graph|meta|storage]
```

`SHOW CONFIGS` 语句显示参数信息。 `SHOW CONFIGS` 输出以下列：module（模块信息）、name（参数名称）、type（参数类型）、mode（参数模式）和 value（参数值）。

例如：

```ngql
nebula> SHOW CONFIGS graph;
==============================================================
| module | name                    | type  | mode    | value |
==============================================================
| GRAPH  | v                       | INT64 | MUTABLE | 0     |
--------------------------------------------------------------
| GRAPH  | minloglevel             | INT64 | MUTABLE | 2     |
--------------------------------------------------------------
| GRAPH  | slow_op_threshhold_ms   | INT64 | MUTABLE | 50    |
--------------------------------------------------------------
| GRAPH  | heartbeat_interval_secs | INT64 | MUTABLE | 3     |
--------------------------------------------------------------
| GRAPH  | meta_client_retry_times | INT64 | MUTABLE | 3     |
--------------------------------------------------------------
```

更多关于 `SHOW CONFIGS [graph|meta|storage]` 的信息，参见 [configs syntax](../../../../3.build-develop-and-administration/3.configurations/2.configs-syntax.md)。
