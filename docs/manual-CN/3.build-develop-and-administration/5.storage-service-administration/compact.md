# Compact

本文档将为您介绍 Compact。

Nebula Graph KV 基于 RocksDB 的默认 compact 做了定制。**Nebula Graph** 提供两种类型的 compact 和相应的操作方法：

- 启动和停止（简称启停） compact，调用 RocksDB 默认的 compact，主要目的是在写入时自动进行小规模的 sst 文件合并，以保证短时间内的读速度。通常在日间业务时自动触发；

```sql
nebula> UPDATE CONFIG storage:disable_auto_compactions=false/true;
```

- 通过 `SUBMIT JOB COMPACT` 来主动触发，调用 **Nebula Graph** 自定义的 compact，通常建议在凌晨业务低谷时进行，以完成大规模的 sst 文件合并、TTL 等大规模后台操作。

另外，两种方法的线程数均可通过如下命令调整。日间可以将调整线程数调低，夜间可以增加线程数。

```ngql
nebula> UPDATE CONFIGS storage:rocksdb_db_options  = \
        { max_subcompactions = 4, max_background_jobs = 4};
```
