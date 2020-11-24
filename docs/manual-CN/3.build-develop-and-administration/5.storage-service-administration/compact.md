# Compact

本文档将为您介绍 Compact。Compact 也称为 Compaction。

## Compact 简介

在 Nebula Graph 中，Compact 是**最为重要**的**后台**操作过程，它对于性能有**极为重要**的影响。

简单的说，Compact 过程是将已经写入硬盘的文件重新读取，组织新的数据结构和索引，将其**更利于读操作**，然后再写回硬盘。经过 Compact 过程后，读性能会有倍数的提升。特别是，当向 Nebula Graph 写入过大量数据后，都需要主动触发一次 Compact，来保证之后的读性能。同时，由于在 Compact 过程中，会发生长时间的硬盘 IO，因此一般该操作会放在业务低谷（例如凌晨）。

**Nebula Graph** 提供两种类型的 compact， 相应的操作方法：

- `自动 compact`

`自动 compact` 会在系统有读写或者重启时**自动进行**，以提升短时间内的读速度。默认情况下，`自动 compact` 默认是**开启状态**，但可能会在**业务高峰时自动启动**，导致意外抢占 IO 影响前台性能。如果期望**完全手动控制** compact，可以运行以下命令来关闭：

```ngql
nebula> UPDATE CONFIGS storage:rocksdb_column_family_options = {disable_auto_compactions = true};
```
参数 `disable_auto_compactions` 默认值为`false` （允许`自动 compact`）。

- `全量 compact`

主要目的是完成某个 `space` 下全量文件合并、启动过期数据删除 (TTL) 等大规模后台操作。可以通过如下命令手动触发：

```ngql
nebula> USE <your_space>;
nebula> SUBMIT JOB COMPACT;
```

该命令同时会返回一个 job_id, 可以通过如下命令查看进度：

```ngql
nebula> SHOW JOB <job_id>;
```

> 由于`全量 compact` 会有大量 IO 操作，请在业务低谷启动。

## 操作建议

下面是一些操作建议，使得 Nebula Graph 持续保持较好的性能：

1. 大量写入数据前，设置`disable_auto_compactions = true`。这是为了避免写入过程中无意义的 IO 浪费;
2. 导入数据完成后，运行 `SUBMIT JOB COMPACT` 命令;
3. 在每日凌晨业务低谷期，周期性运行 `SUBMIT JOB COMPACT`;
4. 日间业务期间，可以设置`disable_auto_compactions = false`；
5. 为控制 compact 的读写流量上线，在`nebula-storaged.conf` 配置文件中，设置如下两项：

```plain
--local-config=true  （从本地配置文件读取并启动）
--rate_limit=20（单位 MB/s）
```

## FAQ

### Q: 多个 space 可以同时进行`全量 compact`吗

A：可以。但此时 IO 会更大。

### Q: `全量 compact` 大约需要多少时间

如果设置了 `--rate_limit=20`，可以用硬盘占用量除以`rate_limit`大体估算。如果未设置，经验值大约为 50 MB/s.

### Q: `--rate_limit` 可以动态调整吗

A：还不可以。

### Q: `全量 compact` 启动后可以手动停止吗

A: 由于 RocksDB 的限制，如果启动后，只能等待完成，不能停止。

<!--
另外，两种方法的线程数均可通过如下命令调整。


```ngql
nebula> UPDATE CONFIGS storage:rocksdb_db_options  = \
        { max_subcompactions = 4, max_background_jobs = 4};
```
-->