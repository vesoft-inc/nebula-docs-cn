# Compact

本文档将为您介绍 Compact。

Nebula Graph KV 基于 RocksDB 的默认 compact 做了定制。**Nebula Graph** 提供两种类型的 compact 相应的操作方法：

- 调用 RocksDB 默认的 compact：主要目的是在写入时自动进行小规模的 sst 文件合并，以保证短时间内的读速度。通常在日间业务时自动触发。运行以下命令启动 RocksDB 默认 compact；

```sql
nebula> UPDATE CONFIGS storage:rocksdb_column_family_options = {disable_auto_compactions = true};
```

`disable_auto_compactions` 参数默认为关闭（即 `false`）。导入数据前，建议将其开启。导入数据后，请务必将其改回 `false`，然后执行 `SUBMIT JOB COMPACT` 命令主动触发 compact。

- 调用 **Nebula Graph** 自定义的 compact：主要目的是完成大规模的 sst 文件合并、TTL 等大规模后台操作。通常建议在凌晨业务低谷时进行。通过 `SUBMIT JOB COMPACT` 来主动触发。

另外，两种方法的线程数均可通过如下命令调整。

```ngql
nebula> UPDATE CONFIGS storage:rocksdb_db_options  = \
        { max_subcompactions = 4, max_background_jobs = 4};
```

## Compact rate limiter

在 RocksDB 中，后台会实时运行 compact 操作，这会对磁盘进行大量的写操作。为避免大量写操作导致的读延迟，您可以使用 Rate Limiter 控制写入速度上限。

您可以在 storage 服务的配置文件（默认路径为 `/usr/local/nebula/etc`）中调节以下 Rate Limiter 参数：

- num_compaction_threads：compact 总线程数。设置为 0 时不限制线程数。
- rate_limit：写入速度限制，单位为字节/秒。设置为 0 时不限制写入速度。
