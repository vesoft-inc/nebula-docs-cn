# 日志配置

Nebula Graph 默认使用 [glog](https://github.com/google/glog) 打印日志，使用 [gflags](https://gflags.github.io/gflags/) 控制日志级别，并在运行时通过 HTTP 接口动态修改日志级别，方便跟踪问题。

Nebula Graph 企业版还支持[审计日志](audit-log.md)。

## 日志目录

日志的默认目录为`/usr/local/nebula/logs/`。

如果在 Nebula Graph 运行过程中删除日志目录，日志不会继续打印，但是不会影响业务。重启服务可以恢复正常。

## 配置说明
- `minloglevel`：最小日志级别，即不会记录低于这个级别的日志。可选值为`0`（INFO）、`1`（WARNING）、`2`（ERROR）、`3`（FATAL）。建议在调试时设置为`0`，生产环境中设置为`1`。如果设置为`4`，Nebula Graph 不会记录任何日志。

- `v`：日志详细级别，值越大，日志记录越详细。可选值为`0`、`1`、`2`、`3`。

Meta 服务、Graph 服务和 Storage 服务的日志级别可以在各自的配置文件中查看，默认路径为`/usr/local/nebula/etc/`。

## 查看日志级别

使用如下命令查看当前所有的 gflags 参数（包括日志参数）：

```bash
$ curl <ws_ip>:<ws_port>/flags
```

|参数|说明|
|:---|:---|
|`ws_ip`|HTTP 服务的 IP 地址，可以在配置文件中查看。默认值为`127.0.0.1`。|
|`ws_port`|HTTP 服务的端口，可以在配置文件中查看。默认值分别为`19559`（Meta）、`19669`（Graph）`19779`（Storage）。|

示例如下：

- 查看 Meta 服务当前的最小日志级别：

    ```bash
    $ curl 127.0.0.1:19559/flags | grep 'minloglevel'
    ```

- 查看 Storage 服务当前的日志详细级别：
  
    ```bash
    $ curl 127.0.0.1:19779/flags | grep -w 'v'
    ```

## 修改日志级别

使用如下命令修改日志级别：

```bash
$ curl -X PUT -H "Content-Type: application/json" -d '{"<key>":<value>[,"<key>":<value>]}' "<ws_ip>:<ws_port>/flags"
```

|参数|说明|
|:---|:---|
|`key`|待修改的日志类型，可选值请参见[配置说明](#_3)。|
|`value`|日志级别，可选值请参见[配置说明](#_3)。|
|`ws_ip`|HTTP 服务的 IP 地址，可以在配置文件中查看。默认值为`127.0.0.1`。|
|`ws_port`|HTTP 服务的端口，可以在配置文件中查看。默认值分别为`19559`（Meta）、`19669`（Graph）`19779`（Storage）。|

示例如下：

```bash
$ curl -X PUT -H "Content-Type: application/json" -d '{"minloglevel":0,"v":3}' "127.0.0.1:19779/flags" # storaged
$ curl -X PUT -H "Content-Type: application/json" -d '{"minloglevel":0,"v":3}' "127.0.0.1:19669/flags" # graphd
$ curl -X PUT -H "Content-Type: application/json" -d '{"minloglevel":0,"v":3}' "127.0.0.1:19559/flags" # metad

```

如果在 Nebula Graph 运行时修改了日志级别，重启服务后会恢复为配置文件中设置的级别，如果需要永久修改，请修改[配置文件](../1.configurations/1.configurations.md)。

## RocksDB 日志

RocksDB 的日志通常在 `/usr/local/nebula/data/storage/nebula/$id/data/LOG`, 其中 `$id` 为实例号。该日志通常用于调试 RocksDB 参数。
