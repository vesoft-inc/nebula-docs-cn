# Compaction

本文介绍 Compaction 的相关信息。

Nebula Graph 中，`Compaction`是最重要的后台操作，对性能有极其重要的影响。

`Compaction`操作会读取硬盘上的数据，然后重组数据结构和索引，然后再写回硬盘，可以成倍提升读取性能。将大量数据写入 Nebula Graph 后，为了提高读取性能，需要手动触发`Compaction`操作（全量`Compaction`）。

!!! Note

    `Compaction`操作会长时间占用硬盘的 IO，建议在业务低峰期（例如凌晨）执行该操作。

Nebula Graph 有两种类型的`Compaction`操作：自动`Compaction`和全量`Compaction`。

## 自动`Compaction`

自动`Compaction`是在系统读取数据、写入数据或系统重启时自动触发`Compaction`操作，提升短时间内的读取性能。默认情况下，自动`Compaction`是开启状态，可能在业务高峰期触发，导致意外抢占 IO 影响业务。

<!--
如果需要完全手动控制`Compaction`操作，用户可以关闭自动`Compaction`。

### 关闭自动`Compaction`

!!! danger

    命令`UPDATE CONFIGS`会将未设置的参数恢复为默认值，因此修改前需要使用`SHOW CONFIGS STORAGE`查看`rocksdb_column_family_options`配置，然后一起重新传入值。

```ngql
# 查看当前 rocksdb_column_family_options 设置，复制 value 列内容。
nebula> SHOW CONFIGS STORAGE;
+-----------+-------------------------------------+-------+-----------+------------------------------------------------------------------------------------------------------+
| module    | name                                | type  | mode      | value                                                                                                |
+-----------+-------------------------------------+-------+-----------+------------------------------------------------------------------------------------------------------+
| "STORAGE" | "v"                                 | "int" | "MUTABLE" | 0                                                                                                    |
...
| "STORAGE" | "rocksdb_column_family_options"     | "map" | "MUTABLE" | {max_bytes_for_level_base: "268435456", max_write_buffer_number: "4", write_buffer_size: "67108864"} |
+-----------+-------------------------------------+-------+-----------+------------------------------------------------------------------------------------------------------+
...

# 修改 rocksdb_column_family_options 设置，在复制的 value 内容中添加 disable_auto_compactions: true
nebula> UPDATE CONFIGS storage:rocksdb_column_family_options = {disable_auto_compactions: true, max_bytes_for_level_base: 268435456, max_write_buffer_number: 4, write_buffer_size: 67108864};

# 查看是否修改成功。
nebula> SHOW CONFIGS STORAGE;
+-----------+-------------------------------------+-------+-----------+--------------------------------------------------------------------------------------------------------------------------------------+
| module    | name                                | type  | mode      | value                                                                                                                                |
+-----------+-------------------------------------+-------+-----------+--------------------------------------------------------------------------------------------------------------------------------------+
| "STORAGE" | "v"                                 | "int" | "MUTABLE" | 0                                                                                                                                    |
...
| "STORAGE" | "rocksdb_column_family_options"     | "map" | "MUTABLE" | {disable_auto_compactions: true, max_bytes_for_level_base: "268435456", max_write_buffer_number: "4", write_buffer_size: "67108864"} |
+-----------+-------------------------------------+-------+-----------+--------------------------------------------------------------------------------------------------------------------------------------+
...
```
-->

## 全量`Compaction`

全量`Compaction`可以对图空间进行大规模后台操作，例如合并文件、删除 TTL 过期数据等，该操作需要手动发起。使用如下语句执行全量`Compaction`操作：

!!! Note

    建议在业务低峰期（例如凌晨）执行该操作，避免大量占用硬盘 IO 影响业务。

```ngql
nebula> USE <your_graph_space>;
nebula> SUBMIT JOB COMPACT;
```

上述命令会返回作业的 ID，用户可以使用如下命令查看`Compaction`状态：

```ngql
nebula> SHOW JOB <job_id>;
```

## 操作建议

为保证 Nebula Graph 的性能，请参考如下操作建议：

<!--
- 数据写入时为避免浪费 IO，请在大量数据写入前关闭自动`Compaction`。详情请参见[关闭自动`Compaction`](#compaction_2)。
-->

- 数据导入完成后，请执行`SUBMIT JOB COMPACT`。

- 业务低峰期（例如凌晨）执行`SUBMIT JOB COMPACT`。

<!--
- 白天时设置`disable_auto_compactions`为`false`，提升短时间内的读取性能。
-->

- 为控制`Compaction`的读写速率，请在配置文件`nebula-storaged.conf`中设置如下参数：

    ```bash
    # 读写速率限制为 20MB/S。
    --rocksdb_rate_limit=20 (in MB/s)
    ```

## FAQ

### Compaction 相关的日志在哪？

默认情况下，`/usr/local/nebula/data/storage/nebula/{1}/data/` 目录下的文件名为 `LOG` 文件，或者类似 `LOG.old.1625797988509303`，找到如下的部分。

```text
** Compaction Stats [default] **
Level    Files   Size     Score Read(GB)  Rn(GB) Rnp1(GB) Write(GB) Wnew(GB) Moved(GB) W-Amp Rd(MB/s) Wr(MB/s) Comp(sec) CompMergeCPU(sec) Comp(cnt) Avg(sec) KeyIn KeyDrop
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  L0      2/0    2.46 KB   0.5      0.0     0.0      0.0       0.0      0.0       0.0   1.0      0.0      0.0      0.53              0.51         2    0.264       0      0
 Sum      2/0    2.46 KB   0.0      0.0     0.0      0.0       0.0      0.0       0.0   1.0      0.0      0.0      0.53              0.51         2    0.264       0      0
 Int      0/0    0.00 KB   0.0      0.0     0.0      0.0       0.0      0.0       0.0   0.0      0.0      0.0      0.00              0.00         0    0.000       0      0
```

如果当前的 `L0` 文件数量较多，对读性能影响较大，可以触发 compaction。

### 可以同时在多个图空间执行全量`Compaction`操作吗？

可以，但是此时的硬盘 IO 会很高，可能会影响效率。

### 全量`Compaction`操作会耗费多长时间？

如果已经设置读写速率限制，例如`rate_limit`限制为 20MB/S 时，用户可以通过 `硬盘使用量/rate_limit` 预估需要耗费的时间。如果没有设置读写速率限制，根据经验，速率大约为 50MB/S。

### 可以动态调整`rate_limit`吗？

不可以。

### 全量`Compaction`操作开始后可以停止吗？

不可以停止，必须等待操作完成。这是 RocksDB 的限制。
