# 日志配置

Nebula Graph使用[glog](https://github.com/google/glog)打印日志，使用[gflags](https://gflags.github.io/gflags/)控制日志级别，并在运行时通过HTTP接口动态修改日志级别，方便跟踪问题。

## 日志目录

日志的默认目录为`/usr/local/nebula/logs/`。

如果您在Nebula Graph运行过程中删除日志目录，日志不会继续打印，但是不会影响业务。重启服务可以恢复正常。

## 配置说明

- `minloglevel`：最小日志级别，即不会记录低于这个级别的日志。可选值为`0`（INFO）、`1`（WARNING）、`2`（ERROR）、`3`（FATAL）。建议您在调试时设置为`0`，生产环境中设置为`1`。如果设置为`4`，Nebula Graph不会记录任何日志。

- `v`：日志详细级别，值越大，日志记录越详细。可选值为`0`、`1`、`2`、`3`。

Meta服务、Graph服务和Storage服务的日志级别可以在各自的配置文件中查看，默认路径为`/usr/local/nebula/etc/`。

## 查看日志级别

使用如下命令查看当前所有的gflags参数（包括日志参数）：

```bash
$ curl <ws_ip>:<ws_port>/flags 
```

|参数|说明|
|:---|:---|
|`ws_ip`|HTTP服务的IP地址，可以在配置文件中查看。默认值为`127.0.0.1`。|
|`ws_port`|HTTP服务的端口，可以在配置文件中查看。默认值分别为`19559`（metad）、`19669`（graphd）`19779`（storaged）。|

示例如下：

- 查看Meta服务当前的最小日志级别：

    ```bash
    $ curl 127.0.0.1:19559/flags | grep 'minloglevel'
    ```

- 查看Storage服务当前的日志详细级别：
  
    ```bash
    $ curl 127.0.0.1:19779/flags |grep -w 'v'
    ```

## 修改日志级别

使用如下命令修改日志级别：

```bash
curl -X PUT -H "Content-Type: application/json" -d '{"<key>":<value>[,"<key>":<value>]}' "<ws_ip>:<ws_port>/flags"
```

|参数|说明|
|:---|:---|
|`key`|待修改的日志类型，可选值请参见[配置说明](#配置说明)。|
|`value`|日志级别，可选值请参见[配置说明](#配置说明)。|
|`ws_ip`|HTTP服务的IP地址，可以在配置文件中查看。默认值为`127.0.0.1`。|
|`ws_port`|HTTP服务的端口，可以在配置文件中查看。默认值分别为`19559`（metad）、`19669`（graphd）`19779`（storaged）。|

>**说明**：如果您在Nebula Graph运行时修改了日志级别，重启服务后会恢复为配置文件中设置的级别，如果需要永久修改，请修改配置文件。

示例如下：

```bash
curl -X PUT -H "Content-Type: application/json" -d '{"minloglevel":1,"v":3}' "127.0.0.1:19779/flags"
```
