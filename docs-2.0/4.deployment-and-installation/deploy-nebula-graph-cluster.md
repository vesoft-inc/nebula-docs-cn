# 部署Nebula Graph集群

Nebula Graph不提供官方的集群部署工具，需要手动部署，下文将介绍手动部署的简单流程。

## 部署方案

| 机器名称 |IP地址          | graphd进程数量   | storaged进程数量    |  metad进程数量   |
| :----- |:---------------|:------------- | :----------------- | :---------------- |
| A      | xxx.xxx.10.111 |1               | 1                  | 1                |
| B      | xxx.xxx.10.112 |1               | 1                  | 1                |
| C      | xxx.xxx.10.113 |1               | 1                  | 1                |
| D      | xxx.xxx.10.114 |1               | 1                  | -                |
| E      | xxx.xxx.10.115 |1               | 1                  | -                |

## 前提条件

准备5台用于部署集群的机器。

## 手动部署流程

### 1.安装Nebula Graph

在集群的每一台服务器上都安装Nebula Graph，安装后暂不需要启动服务。安装方式请参见：

- [使用RPM或DEB安装包安装Nebula Graph](2.compile-and-install-nebula-graph/2.install-nebula-graph-by-rpm-or-deb.md)

- [编译安装Nebula Graph](2.compile-and-install-nebula-graph/1.install-nebula-graph-by-compiling-the-source-code.md)

### 2.修改配置文件

修改每个服务器上的Nebula Graph配置文件。

Nebula Graph的所有配置文件均位于安装目录的`etc`目录内，包括`nebula-graphd.conf`、`nebula-metad.conf`和`nebula-storaged.conf`，用户可以只修改所需服务的配置文件。各个机器需要修改的配置文件如下。

| 机器名称 |待修改配置文件    | 
| :----- |:---------------|
| A      | `nebula-graphd.conf`、`nebula-storaged.conf`、`nebula-metad.conf`|
| B      | `nebula-graphd.conf`、`nebula-storaged.conf`、`nebula-metad.conf`|
| C      | `nebula-graphd.conf`、`nebula-storaged.conf`、`nebula-metad.conf` |
| D      | `nebula-graphd.conf`、`nebula-storaged.conf` |
| E      | `nebula-graphd.conf`、`nebula-storaged.conf` |

您可以参考如下配置文件，便于您了解集群间各个服务器的关系。

!!! note

    主要修改的配置是`meta_server_addrs`，所有配置文件都需要填写所有Meta服务的IP地址和端口，同时需要修改`local_ip`为机器本身的联网IP地址。配置参数的详细说明请参见：

    - [Meta服务配置](../5.configurations-and-logs/1.configurations/2.meta-config.md)

    - [Graph服务配置](../5.configurations-and-logs/1.configurations/3.graph-config.md)

    - [Storage服务配置](../5.configurations-and-logs/1.configurations/4.storage-config.md)

- 机器A配置

  - `nebula-graphd.conf`

    ```bash
    ########## basics ##########
    # Whether to run as a daemon process
    --daemonize=true
    # The file to host the process id
    --pid_file=pids/nebula-graphd.pid
    # Whether to enable optimizer
    --enable_optimizer=true

    ########## logging ##########
    # The directory to host logging files
    --log_dir=logs
    # Log level, 0, 1, 2, 3 for INFO, WARNING, ERROR, FATAL respectively
    --minloglevel=0
    # Verbose log level, 1, 2, 3, 4, the higher of the level, the more verbose of the logging
    --v=0
    # Maximum seconds to buffer the log messages
    --logbufsecs=0
    # Whether to redirect stdout and stderr to separate output files
    --redirect_stdout=true
    # Destination filename of stdout and stderr, which will also reside in log_dir.
    --stdout_log_file=graphd-stdout.log
    --stderr_log_file=graphd-stderr.log
    # Copy log messages at or above this level to stderr in addition to logfiles. The numbers of severity levels INFO, WARNING, ERROR, and FATAL are 0, 1, 2, and 3, respectively.
    --stderrthreshold=2

    ########## query ##########
    # Whether to treat partial success as an error.
    # This flag is only used for Read-only access, and Modify access always treats partial success as an error.
    --accept_partial_success=false

    ########## networking ##########
    # Comma separated Meta Server Addresses
    --meta_server_addrs=xxx.xxx.10.111:9559,xxx.xxx.10.112:9559,xxx.xxx.10.113:9559
    # Local IP used to identify the nebula-graphd process.
    # Change it to an address other than loopback if the service is distributed or
    # will be accessed remotely.
    --local_ip=xxx.xxx.10.111
    # Network device to listen on
    --listen_netdev=any
    # Port to listen on
    --port=9669
    # To turn on SO_REUSEPORT or not
    --reuse_port=false
    # Backlog of the listen socket, adjust this together with net.core.somaxconn
    --listen_backlog=1024
    # Seconds before the idle connections are closed, 0 for never closed
    --client_idle_timeout_secs=0
    # Seconds before the idle sessions are expired, 0 for no expiration
    --session_idle_timeout_secs=0
    # The number of threads to accept incoming connections
    --num_accept_threads=1
    # The number of networking IO threads, 0 for # of CPU cores
    --num_netio_threads=0
    # The number of threads to execute user queries, 0 for # of CPU cores
    --num_worker_threads=0
    # HTTP service ip
    --ws_ip=0.0.0.0
    # HTTP service port
    --ws_http_port=19669
    # HTTP2 service port
    --ws_h2_port=19670

    # The default charset when a space is created
    --default_charset=utf8
    # The defaule collate when a space is created
    --default_collate=utf8_bin

    ########## authorization ##########
    # Enable authorization
    --enable_authorize=false

    ########## Authentication ##########
    # User login authentication type, password for nebula authentication, ldap for ldap authentication, cloud for cloud authentication
    --auth_type=password
    ```

  - `nebula-storaged.conf`
  
    ```bash
    ########## basics ##########
    # Whether to run as a daemon process
    --daemonize=true
    # The file to host the process id
    --pid_file=pids/nebula-storaged.pid

    ########## logging ##########
    # The directory to host logging files
    --log_dir=logs
    # Log level, 0, 1, 2, 3 for INFO, WARNING, ERROR, FATAL respectively
    --minloglevel=0
    # Verbose log level, 1, 2, 3, 4, the higher of the level, the more verbose of the logging
    --v=0
    # Maximum seconds to buffer the log messages
    --logbufsecs=0
    # Whether to redirect stdout and stderr to separate output files
    --redirect_stdout=true
    # Destination filename of stdout and stderr, which will also reside in log_dir.
    --stdout_log_file=storaged-stdout.log
    --stderr_log_file=storaged-stderr.log
    # Copy log messages at or above this level to stderr in addition to logfiles. The numbers of severity levels INFO, WARNING, ERROR, and FATAL are 0, 1, 2, and 3, respectively.
    --stderrthreshold=2

    ########## networking ##########
    # Comma separated Meta server addresses
    --meta_server_addrs=xxx.xxx.10.111:9559,xxx.xxx.10.112:9559,xxx.xxx.10.113:9559
    # Local IP used to identify the nebula-storaged process.
    # Change it to an address other than loopback if the service is distributed or
    # will be accessed remotely.
    --local_ip=xxx.xxx.10.111
    # Storage daemon listening port
    --port=9779
    # HTTP service ip
    --ws_ip=0.0.0.0
    # HTTP service port
    --ws_http_port=19779
    # HTTP2 service port
    --ws_h2_port=19780
    # heartbeat with meta service
    --heartbeat_interval_secs=10

    ######### Raft #########
    # Raft election timeout
    --raft_heartbeat_interval_secs=30
    # RPC timeout for raft client (ms)
    --raft_rpc_timeout_ms=500
    ## recycle Raft WAL
    --wal_ttl=14400

    ########## Disk ##########
    # Root data path. Split by comma. e.g. --data_path=/disk1/path1/,/disk2/path2/
    # One path per Rocksdb instance.
    --data_path=data/storage

    # The default reserved bytes for one batch operation
    --rocksdb_batch_size=4096
    # The default block cache size used in BlockBasedTable.
    # The unit is MB.
    --rocksdb_block_cache=4
    # The type of storage engine, `rocksdb', `memory', etc.
    --engine_type=rocksdb

    # Compression algorithm, options: no,snappy,lz4,lz4hc,zlib,bzip2,zstd
    # For the sake of binary compatibility, the default value is snappy.
    # Recommend to use:
    #   * lz4 to gain more CPU performance, with the same compression ratio with snappy
    #   * zstd to occupy less disk space
    #   * lz4hc for the read-heavy write-light scenario
    --rocksdb_compression=lz4

    # Set different compressions for different levels
    # For example, if --rocksdb_compression is snappy,
    # "no:no:lz4:lz4::zstd" is identical to "no:no:lz4:lz4:snappy:zstd:snappy"
    # In order to disable compression for level 0/1, set it to "no:no"
    --rocksdb_compression_per_level=

    # Whether or not to enable rocksdb's statistics, disabled by default
    --enable_rocksdb_statistics=false

    # Statslevel used by rocksdb to collection statistics, optional values are
    #   * kExceptHistogramOrTimers, disable timer stats, and skip histogram stats
    #   * kExceptTimers, Skip timer stats
    #   * kExceptDetailedTimers, Collect all stats except time inside mutex lock AND time spent on compression.
    #   * kExceptTimeForMutex, Collect all stats except the counters requiring to get time inside the mutex lock.
    #   * kAll, Collect all stats
    --rocksdb_stats_level=kExceptHistogramOrTimers

    # Whether or not to enable rocksdb's prefix bloom filter, disabled by default.
    --enable_rocksdb_prefix_filtering=false
    # Whether or not to enable the whole key filtering.
    --enable_rocksdb_whole_key_filtering=true
    # The prefix length for each key to use as the filter value.
    # can be 12 bytes(PartitionId + VertexID), or 16 bytes(PartitionId + VertexID + TagID/EdgeType).
    --rocksdb_filtering_prefix_length=12

    ############## rocksdb Options ##############
    # rocksdb DBOptions in json, each name and value of option is a string, given as "option_name":"option_value" separated by comma
    --rocksdb_db_options={}
    # rocksdb ColumnFamilyOptions in json, each name and value of option is string, given as "option_name":"option_value" separated by comma
    --rocksdb_column_family_options={"write_buffer_size":"67108864","max_write_buffer_number":"4","max_bytes_for_level_base":"268435456"}
    # rocksdb BlockBasedTableOptions in json, each name and value of option is string, given as "option_name":"option_value" separated by comma
    --rocksdb_block_based_table_options={"block_size":"8192"}
    ```

  - `nebula-metad.conf`

    ```bash
    ########## basics ##########
    # Whether to run as a daemon process
    --daemonize=true
    # The file to host the process id
    --pid_file=pids/nebula-metad.pid

    ########## logging ##########
    # The directory to host logging files
    --log_dir=logs
    # Log level, 0, 1, 2, 3 for INFO, WARNING, ERROR, FATAL respectively
    --minloglevel=0
    # Verbose log level, 1, 2, 3, 4, the higher of the level, the more verbose of the logging
    --v=0
    # Maximum seconds to buffer the log messages
    --logbufsecs=0
    # Whether to redirect stdout and stderr to separate output files
    --redirect_stdout=true
    # Destination filename of stdout and stderr, which will also reside in log_dir.
    --stdout_log_file=metad-stdout.log
    --stderr_log_file=metad-stderr.log
    # Copy log messages at or above this level to stderr in addition to logfiles. The numbers of severity levels INFO, WARNING, ERROR, and FATAL are 0, 1, 2, and 3, respectively.
    --stderrthreshold=2

    ########## networking ##########
    # Comma separated Meta Server addresses
    --meta_server_addrs=xxx.xxx.10.111:9559,xxx.xxx.10.112:9559,xxx.xxx.10.113:9559
    # Local IP used to identify the nebula-metad process.
    # Change it to an address other than loopback if the service is distributed or
    # will be accessed remotely.
    --local_ip=xxx.xxx.10.111
    # Meta daemon listening port
    --port=9559
    # HTTP service ip
    --ws_ip=0.0.0.0
    # HTTP service port
    --ws_http_port=19559
    # HTTP2 service port
    --ws_h2_port=19560

    ########## storage ##########
    # Root data path, here should be only single path for metad
    --data_path=data/meta

    ########## Misc #########
    # The default number of parts when a space is created
    --default_parts_num=100
    # The default replica factor when a space is created
    --default_replica_factor=1

    --heartbeat_interval_secs=10
    ```

- 机器B配置

  - `nebula-graphd.conf`

    ```bash
    ########## basics ##########
    # Whether to run as a daemon process
    --daemonize=true
    # The file to host the process id
    --pid_file=pids/nebula-graphd.pid
    # Whether to enable optimizer
    --enable_optimizer=true

    ########## logging ##########
    # The directory to host logging files
    --log_dir=logs
    # Log level, 0, 1, 2, 3 for INFO, WARNING, ERROR, FATAL respectively
    --minloglevel=0
    # Verbose log level, 1, 2, 3, 4, the higher of the level, the more verbose of the logging
    --v=0
    # Maximum seconds to buffer the log messages
    --logbufsecs=0
    # Whether to redirect stdout and stderr to separate output files
    --redirect_stdout=true
    # Destination filename of stdout and stderr, which will also reside in log_dir.
    --stdout_log_file=graphd-stdout.log
    --stderr_log_file=graphd-stderr.log
    # Copy log messages at or above this level to stderr in addition to logfiles. The numbers of severity levels INFO, WARNING, ERROR, and FATAL are 0, 1, 2, and 3, respectively.
    --stderrthreshold=2

    ########## query ##########
    # Whether to treat partial success as an error.
    # This flag is only used for Read-only access, and Modify access always treats partial success as an error.
    --accept_partial_success=false

    ########## networking ##########
    # Comma separated Meta Server Addresses
    --meta_server_addrs=xxx.xxx.10.111:9559,xxx.xxx.10.112:9559,xxx.xxx.10.113:9559
    # Local IP used to identify the nebula-graphd process.
    # Change it to an address other than loopback if the service is distributed or
    # will be accessed remotely.
    --local_ip=xxx.xxx.10.112
    # Network device to listen on
    --listen_netdev=any
    # Port to listen on
    --port=9669
    # To turn on SO_REUSEPORT or not
    --reuse_port=false
    # Backlog of the listen socket, adjust this together with net.core.somaxconn
    --listen_backlog=1024
    # Seconds before the idle connections are closed, 0 for never closed
    --client_idle_timeout_secs=0
    # Seconds before the idle sessions are expired, 0 for no expiration
    --session_idle_timeout_secs=0
    # The number of threads to accept incoming connections
    --num_accept_threads=1
    # The number of networking IO threads, 0 for # of CPU cores
    --num_netio_threads=0
    # The number of threads to execute user queries, 0 for # of CPU cores
    --num_worker_threads=0
    # HTTP service ip
    --ws_ip=0.0.0.0
    # HTTP service port
    --ws_http_port=19669
    # HTTP2 service port
    --ws_h2_port=19670

    # The default charset when a space is created
    --default_charset=utf8
    # The defaule collate when a space is created
    --default_collate=utf8_bin

    ########## authorization ##########
    # Enable authorization
    --enable_authorize=false

    ########## Authentication ##########
    # User login authentication type, password for nebula authentication, ldap for ldap authentication, cloud for cloud authentication
    --auth_type=password
    ```

  - `nebula-storaged.conf`

    ```bash
    ########## basics ##########
    # Whether to run as a daemon process
    --daemonize=true
    # The file to host the process id
    --pid_file=pids/nebula-storaged.pid

    ########## logging ##########
    # The directory to host logging files
    --log_dir=logs
    # Log level, 0, 1, 2, 3 for INFO, WARNING, ERROR, FATAL respectively
    --minloglevel=0
    # Verbose log level, 1, 2, 3, 4, the higher of the level, the more verbose of the logging
    --v=0
    # Maximum seconds to buffer the log messages
    --logbufsecs=0
    # Whether to redirect stdout and stderr to separate output files
    --redirect_stdout=true
    # Destination filename of stdout and stderr, which will also reside in log_dir.
    --stdout_log_file=storaged-stdout.log
    --stderr_log_file=storaged-stderr.log
    # Copy log messages at or above this level to stderr in addition to logfiles. The numbers of severity levels INFO, WARNING, ERROR, and FATAL are 0, 1, 2, and 3, respectively.
    --stderrthreshold=2

    ########## networking ##########
    # Comma separated Meta server addresses
    --meta_server_addrs=xxx.xxx.10.111:9559,xxx.xxx.10.112:9559,xxx.xxx.10.113:9559
    # Local IP used to identify the nebula-storaged process.
    # Change it to an address other than loopback if the service is distributed or
    # will be accessed remotely.
    --local_ip=xxx.xxx.10.112
    # Storage daemon listening port
    --port=9779
    # HTTP service ip
    --ws_ip=0.0.0.0
    # HTTP service port
    --ws_http_port=19779
    # HTTP2 service port
    --ws_h2_port=19780
    # heartbeat with meta service
    --heartbeat_interval_secs=10

    ######### Raft #########
    # Raft election timeout
    --raft_heartbeat_interval_secs=30
    # RPC timeout for raft client (ms)
    --raft_rpc_timeout_ms=500
    ## recycle Raft WAL
    --wal_ttl=14400

    ########## Disk ##########
    # Root data path. Split by comma. e.g. --data_path=/disk1/path1/,/disk2/path2/
    # One path per Rocksdb instance.
    --data_path=data/storage

    # The default reserved bytes for one batch operation
    --rocksdb_batch_size=4096
    # The default block cache size used in BlockBasedTable.
    # The unit is MB.
    --rocksdb_block_cache=4
    # The type of storage engine, `rocksdb', `memory', etc.
    --engine_type=rocksdb

    # Compression algorithm, options: no,snappy,lz4,lz4hc,zlib,bzip2,zstd
    # For the sake of binary compatibility, the default value is snappy.
    # Recommend to use:
    #   * lz4 to gain more CPU performance, with the same compression ratio with snappy
    #   * zstd to occupy less disk space
    #   * lz4hc for the read-heavy write-light scenario
    --rocksdb_compression=lz4

    # Set different compressions for different levels
    # For example, if --rocksdb_compression is snappy,
    # "no:no:lz4:lz4::zstd" is identical to "no:no:lz4:lz4:snappy:zstd:snappy"
    # In order to disable compression for level 0/1, set it to "no:no"
    --rocksdb_compression_per_level=

    # Whether or not to enable rocksdb's statistics, disabled by default
    --enable_rocksdb_statistics=false

    # Statslevel used by rocksdb to collection statistics, optional values are
    #   * kExceptHistogramOrTimers, disable timer stats, and skip histogram stats
    #   * kExceptTimers, Skip timer stats
    #   * kExceptDetailedTimers, Collect all stats except time inside mutex lock AND time spent on compression.
    #   * kExceptTimeForMutex, Collect all stats except the counters requiring to get time inside the mutex lock.
    #   * kAll, Collect all stats
    --rocksdb_stats_level=kExceptHistogramOrTimers

    # Whether or not to enable rocksdb's prefix bloom filter, disabled by default.
    --enable_rocksdb_prefix_filtering=false
    # Whether or not to enable the whole key filtering.
    --enable_rocksdb_whole_key_filtering=true
    # The prefix length for each key to use as the filter value.
    # can be 12 bytes(PartitionId + VertexID), or 16 bytes(PartitionId + VertexID + TagID/EdgeType).
    --rocksdb_filtering_prefix_length=12

    ############## rocksdb Options ##############
    # rocksdb DBOptions in json, each name and value of option is a string, given as "option_name":"option_value" separated by comma
    --rocksdb_db_options={}
    # rocksdb ColumnFamilyOptions in json, each name and value of option is string, given as "option_name":"option_value" separated by comma
    --rocksdb_column_family_options={"write_buffer_size":"67108864","max_write_buffer_number":"4","max_bytes_for_level_base":"268435456"}
    # rocksdb BlockBasedTableOptions in json, each name and value of option is string, given as "option_name":"option_value" separated by comma
    --rocksdb_block_based_table_options={"block_size":"8192"}
    ```

  - `nebula-metad.conf`

    ```bash
    ########## basics ##########
    # Whether to run as a daemon process
    --daemonize=true
    # The file to host the process id
    --pid_file=pids/nebula-metad.pid

    ########## logging ##########
    # The directory to host logging files
    --log_dir=logs
    # Log level, 0, 1, 2, 3 for INFO, WARNING, ERROR, FATAL respectively
    --minloglevel=0
    # Verbose log level, 1, 2, 3, 4, the higher of the level, the more verbose of the logging
    --v=0
    # Maximum seconds to buffer the log messages
    --logbufsecs=0
    # Whether to redirect stdout and stderr to separate output files
    --redirect_stdout=true
    # Destination filename of stdout and stderr, which will also reside in log_dir.
    --stdout_log_file=metad-stdout.log
    --stderr_log_file=metad-stderr.log
    # Copy log messages at or above this level to stderr in addition to logfiles. The numbers of severity levels INFO, WARNING, ERROR, and FATAL are 0, 1, 2, and 3, respectively.
    --stderrthreshold=2

    ########## networking ##########
    # Comma separated Meta Server addresses
    --meta_server_addrs=xxx.xxx.10.111:9559,xxx.xxx.10.112:9559,xxx.xxx.10.113:9559
    # Local IP used to identify the nebula-metad process.
    # Change it to an address other than loopback if the service is distributed or
    # will be accessed remotely.
    --local_ip=xxx.xxx.10.112
    # Meta daemon listening port
    --port=9559
    # HTTP service ip
    --ws_ip=0.0.0.0
    # HTTP service port
    --ws_http_port=19559
    # HTTP2 service port
    --ws_h2_port=19560

    ########## storage ##########
    # Root data path, here should be only single path for metad
    --data_path=data/meta

    ########## Misc #########
    # The default number of parts when a space is created
    --default_parts_num=100
    # The default replica factor when a space is created
    --default_replica_factor=1

    --heartbeat_interval_secs=10
    ```

- 机器C配置

  - `nebula-graphd.conf`

    ```bash
    ########## basics ##########
    # Whether to run as a daemon process
    --daemonize=true
    # The file to host the process id
    --pid_file=pids/nebula-graphd.pid
    # Whether to enable optimizer
    --enable_optimizer=true

    ########## logging ##########
    # The directory to host logging files
    --log_dir=logs
    # Log level, 0, 1, 2, 3 for INFO, WARNING, ERROR, FATAL respectively
    --minloglevel=0
    # Verbose log level, 1, 2, 3, 4, the higher of the level, the more verbose of the logging
    --v=0
    # Maximum seconds to buffer the log messages
    --logbufsecs=0
    # Whether to redirect stdout and stderr to separate output files
    --redirect_stdout=true
    # Destination filename of stdout and stderr, which will also reside in log_dir.
    --stdout_log_file=graphd-stdout.log
    --stderr_log_file=graphd-stderr.log
    # Copy log messages at or above this level to stderr in addition to logfiles. The numbers of severity levels INFO, WARNING, ERROR, and FATAL are 0, 1, 2, and 3, respectively.
    --stderrthreshold=2

    ########## query ##########
    # Whether to treat partial success as an error.
    # This flag is only used for Read-only access, and Modify access always treats partial success as an error.
    --accept_partial_success=false

    ########## networking ##########
    # Comma separated Meta Server Addresses
    --meta_server_addrs=xxx.xxx.10.111:9559,xxx.xxx.10.112:9559,xxx.xxx.10.113:9559
    # Local IP used to identify the nebula-graphd process.
    # Change it to an address other than loopback if the service is distributed or
    # will be accessed remotely.
    --local_ip=xxx.xxx.10.113
    # Network device to listen on
    --listen_netdev=any
    # Port to listen on
    --port=9669
    # To turn on SO_REUSEPORT or not
    --reuse_port=false
    # Backlog of the listen socket, adjust this together with net.core.somaxconn
    --listen_backlog=1024
    # Seconds before the idle connections are closed, 0 for never closed
    --client_idle_timeout_secs=0
    # Seconds before the idle sessions are expired, 0 for no expiration
    --session_idle_timeout_secs=0
    # The number of threads to accept incoming connections
    --num_accept_threads=1
    # The number of networking IO threads, 0 for # of CPU cores
    --num_netio_threads=0
    # The number of threads to execute user queries, 0 for # of CPU cores
    --num_worker_threads=0
    # HTTP service ip
    --ws_ip=0.0.0.0
    # HTTP service port
    --ws_http_port=19669
    # HTTP2 service port
    --ws_h2_port=19670

    # The default charset when a space is created
    --default_charset=utf8
    # The defaule collate when a space is created
    --default_collate=utf8_bin

    ########## authorization ##########
    # Enable authorization
    --enable_authorize=false

    ########## Authentication ##########
    # User login authentication type, password for nebula authentication, ldap for ldap authentication, cloud for cloud authentication
    --auth_type=password
    ```

  - `nebula-storaged.conf`

    ```bash
    ########## basics ##########
    # Whether to run as a daemon process
    --daemonize=true
    # The file to host the process id
    --pid_file=pids/nebula-storaged.pid

    ########## logging ##########
    # The directory to host logging files
    --log_dir=logs
    # Log level, 0, 1, 2, 3 for INFO, WARNING, ERROR, FATAL respectively
    --minloglevel=0
    # Verbose log level, 1, 2, 3, 4, the higher of the level, the more verbose of the logging
    --v=0
    # Maximum seconds to buffer the log messages
    --logbufsecs=0
    # Whether to redirect stdout and stderr to separate output files
    --redirect_stdout=true
    # Destination filename of stdout and stderr, which will also reside in log_dir.
    --stdout_log_file=storaged-stdout.log
    --stderr_log_file=storaged-stderr.log
    # Copy log messages at or above this level to stderr in addition to logfiles. The numbers of severity levels INFO, WARNING, ERROR, and FATAL are 0, 1, 2, and 3, respectively.
    --stderrthreshold=2

    ########## networking ##########
    # Comma separated Meta server addresses
    --meta_server_addrs=xxx.xxx.10.111:9559,xxx.xxx.10.112:9559,xxx.xxx.10.113:9559
    # Local IP used to identify the nebula-storaged process.
    # Change it to an address other than loopback if the service is distributed or
    # will be accessed remotely.
    --local_ip=xxx.xxx.10.113
    # Storage daemon listening port
    --port=9779
    # HTTP service ip
    --ws_ip=0.0.0.0
    # HTTP service port
    --ws_http_port=19779
    # HTTP2 service port
    --ws_h2_port=19780
    # heartbeat with meta service
    --heartbeat_interval_secs=10

    ######### Raft #########
    # Raft election timeout
    --raft_heartbeat_interval_secs=30
    # RPC timeout for raft client (ms)
    --raft_rpc_timeout_ms=500
    ## recycle Raft WAL
    --wal_ttl=14400

    ########## Disk ##########
    # Root data path. Split by comma. e.g. --data_path=/disk1/path1/,/disk2/path2/
    # One path per Rocksdb instance.
    --data_path=data/storage

    # The default reserved bytes for one batch operation
    --rocksdb_batch_size=4096
    # The default block cache size used in BlockBasedTable.
    # The unit is MB.
    --rocksdb_block_cache=4
    # The type of storage engine, `rocksdb', `memory', etc.
    --engine_type=rocksdb

    # Compression algorithm, options: no,snappy,lz4,lz4hc,zlib,bzip2,zstd
    # For the sake of binary compatibility, the default value is snappy.
    # Recommend to use:
    #   * lz4 to gain more CPU performance, with the same compression ratio with snappy
    #   * zstd to occupy less disk space
    #   * lz4hc for the read-heavy write-light scenario
    --rocksdb_compression=lz4

    # Set different compressions for different levels
    # For example, if --rocksdb_compression is snappy,
    # "no:no:lz4:lz4::zstd" is identical to "no:no:lz4:lz4:snappy:zstd:snappy"
    # In order to disable compression for level 0/1, set it to "no:no"
    --rocksdb_compression_per_level=

    # Whether or not to enable rocksdb's statistics, disabled by default
    --enable_rocksdb_statistics=false

    # Statslevel used by rocksdb to collection statistics, optional values are
    #   * kExceptHistogramOrTimers, disable timer stats, and skip histogram stats
    #   * kExceptTimers, Skip timer stats
    #   * kExceptDetailedTimers, Collect all stats except time inside mutex lock AND time spent on compression.
    #   * kExceptTimeForMutex, Collect all stats except the counters requiring to get time inside the mutex lock.
    #   * kAll, Collect all stats
    --rocksdb_stats_level=kExceptHistogramOrTimers

    # Whether or not to enable rocksdb's prefix bloom filter, disabled by default.
    --enable_rocksdb_prefix_filtering=false
    # Whether or not to enable the whole key filtering.
    --enable_rocksdb_whole_key_filtering=true
    # The prefix length for each key to use as the filter value.
    # can be 12 bytes(PartitionId + VertexID), or 16 bytes(PartitionId + VertexID + TagID/EdgeType).
    --rocksdb_filtering_prefix_length=12

    ############## rocksdb Options ##############
    # rocksdb DBOptions in json, each name and value of option is a string, given as "option_name":"option_value" separated by comma
    --rocksdb_db_options={}
    # rocksdb ColumnFamilyOptions in json, each name and value of option is string, given as "option_name":"option_value" separated by comma
    --rocksdb_column_family_options={"write_buffer_size":"67108864","max_write_buffer_number":"4","max_bytes_for_level_base":"268435456"}
    # rocksdb BlockBasedTableOptions in json, each name and value of option is string, given as "option_name":"option_value" separated by comma
    --rocksdb_block_based_table_options={"block_size":"8192"}
    ```

  - `nebula-metad.conf`

    ```bash
    ########## basics ##########
    # Whether to run as a daemon process
    --daemonize=true
    # The file to host the process id
    --pid_file=pids/nebula-metad.pid

    ########## logging ##########
    # The directory to host logging files
    --log_dir=logs
    # Log level, 0, 1, 2, 3 for INFO, WARNING, ERROR, FATAL respectively
    --minloglevel=0
    # Verbose log level, 1, 2, 3, 4, the higher of the level, the more verbose of the logging
    --v=0
    # Maximum seconds to buffer the log messages
    --logbufsecs=0
    # Whether to redirect stdout and stderr to separate output files
    --redirect_stdout=true
    # Destination filename of stdout and stderr, which will also reside in log_dir.
    --stdout_log_file=metad-stdout.log
    --stderr_log_file=metad-stderr.log
    # Copy log messages at or above this level to stderr in addition to logfiles. The numbers of severity levels INFO, WARNING, ERROR, and FATAL are 0, 1, 2, and 3, respectively.
    --stderrthreshold=2

    ########## networking ##########
    # Comma separated Meta Server addresses
    --meta_server_addrs=xxx.xxx.10.111:9559,xxx.xxx.10.112:9559,xxx.xxx.10.113:9559
    # Local IP used to identify the nebula-metad process.
    # Change it to an address other than loopback if the service is distributed or
    # will be accessed remotely.
    --local_ip=xxx.xxx.10.113
    # Meta daemon listening port
    --port=9559
    # HTTP service ip
    --ws_ip=0.0.0.0
    # HTTP service port
    --ws_http_port=19559
    # HTTP2 service port
    --ws_h2_port=19560

    ########## storage ##########
    # Root data path, here should be only single path for metad
    --data_path=data/meta

    ########## Misc #########
    # The default number of parts when a space is created
    --default_parts_num=100
    # The default replica factor when a space is created
    --default_replica_factor=1

    --heartbeat_interval_secs=10
    ```

- 机器D配置

  - `nebula-graphd.conf`

    ```bash
    ########## basics ##########
    # Whether to run as a daemon process
    --daemonize=true
    # The file to host the process id
    --pid_file=pids/nebula-graphd.pid
    # Whether to enable optimizer
    --enable_optimizer=true

    ########## logging ##########
    # The directory to host logging files
    --log_dir=logs
    # Log level, 0, 1, 2, 3 for INFO, WARNING, ERROR, FATAL respectively
    --minloglevel=0
    # Verbose log level, 1, 2, 3, 4, the higher of the level, the more verbose of the logging
    --v=0
    # Maximum seconds to buffer the log messages
    --logbufsecs=0
    # Whether to redirect stdout and stderr to separate output files
    --redirect_stdout=true
    # Destination filename of stdout and stderr, which will also reside in log_dir.
    --stdout_log_file=graphd-stdout.log
    --stderr_log_file=graphd-stderr.log
    # Copy log messages at or above this level to stderr in addition to logfiles. The numbers of severity levels INFO, WARNING, ERROR, and FATAL are 0, 1, 2, and 3, respectively.
    --stderrthreshold=2

    ########## query ##########
    # Whether to treat partial success as an error.
    # This flag is only used for Read-only access, and Modify access always treats partial success as an error.
    --accept_partial_success=false

    ########## networking ##########
    # Comma separated Meta Server Addresses
    --meta_server_addrs=xxx.xxx.10.111:9559,xxx.xxx.10.112:9559,xxx.xxx.10.113:9559
    # Local IP used to identify the nebula-graphd process.
    # Change it to an address other than loopback if the service is distributed or
    # will be accessed remotely.
    --local_ip=xxx.xxx.10.114
    # Network device to listen on
    --listen_netdev=any
    # Port to listen on
    --port=9669
    # To turn on SO_REUSEPORT or not
    --reuse_port=false
    # Backlog of the listen socket, adjust this together with net.core.somaxconn
    --listen_backlog=1024
    # Seconds before the idle connections are closed, 0 for never closed
    --client_idle_timeout_secs=0
    # Seconds before the idle sessions are expired, 0 for no expiration
    --session_idle_timeout_secs=0
    # The number of threads to accept incoming connections
    --num_accept_threads=1
    # The number of networking IO threads, 0 for # of CPU cores
    --num_netio_threads=0
    # The number of threads to execute user queries, 0 for # of CPU cores
    --num_worker_threads=0
    # HTTP service ip
    --ws_ip=0.0.0.0
    # HTTP service port
    --ws_http_port=19669
    # HTTP2 service port
    --ws_h2_port=19670

    # The default charset when a space is created
    --default_charset=utf8
    # The defaule collate when a space is created
    --default_collate=utf8_bin

    ########## authorization ##########
    # Enable authorization
    --enable_authorize=false

    ########## Authentication ##########
    # User login authentication type, password for nebula authentication, ldap for ldap authentication, cloud for cloud authentication
    --auth_type=password
    ```

  - `nebula-storaged.conf`

    ```bash
    ########## basics ##########
    # Whether to run as a daemon process
    --daemonize=true
    # The file to host the process id
    --pid_file=pids/nebula-storaged.pid

    ########## logging ##########
    # The directory to host logging files
    --log_dir=logs
    # Log level, 0, 1, 2, 3 for INFO, WARNING, ERROR, FATAL respectively
    --minloglevel=0
    # Verbose log level, 1, 2, 3, 4, the higher of the level, the more verbose of the logging
    --v=0
    # Maximum seconds to buffer the log messages
    --logbufsecs=0
    # Whether to redirect stdout and stderr to separate output files
    --redirect_stdout=true
    # Destination filename of stdout and stderr, which will also reside in log_dir.
    --stdout_log_file=storaged-stdout.log
    --stderr_log_file=storaged-stderr.log
    # Copy log messages at or above this level to stderr in addition to logfiles. The numbers of severity levels INFO, WARNING, ERROR, and FATAL are 0, 1, 2, and 3, respectively.
    --stderrthreshold=2

    ########## networking ##########
    # Comma separated Meta server addresses
    --meta_server_addrs=xxx.xxx.10.111:9559,xxx.xxx.10.112:9559,xxx.xxx.10.113:9559
    # Local IP used to identify the nebula-storaged process.
    # Change it to an address other than loopback if the service is distributed or
    # will be accessed remotely.
    --local_ip=xxx.xxx.10.114
    # Storage daemon listening port
    --port=9779
    # HTTP service ip
    --ws_ip=0.0.0.0
    # HTTP service port
    --ws_http_port=19779
    # HTTP2 service port
    --ws_h2_port=19780
    # heartbeat with meta service
    --heartbeat_interval_secs=10

    ######### Raft #########
    # Raft election timeout
    --raft_heartbeat_interval_secs=30
    # RPC timeout for raft client (ms)
    --raft_rpc_timeout_ms=500
    ## recycle Raft WAL
    --wal_ttl=14400

    ########## Disk ##########
    # Root data path. Split by comma. e.g. --data_path=/disk1/path1/,/disk2/path2/
    # One path per Rocksdb instance.
    --data_path=data/storage

    # The default reserved bytes for one batch operation
    --rocksdb_batch_size=4096
    # The default block cache size used in BlockBasedTable.
    # The unit is MB.
    --rocksdb_block_cache=4
    # The type of storage engine, `rocksdb', `memory', etc.
    --engine_type=rocksdb

    # Compression algorithm, options: no,snappy,lz4,lz4hc,zlib,bzip2,zstd
    # For the sake of binary compatibility, the default value is snappy.
    # Recommend to use:
    #   * lz4 to gain more CPU performance, with the same compression ratio with snappy
    #   * zstd to occupy less disk space
    #   * lz4hc for the read-heavy write-light scenario
    --rocksdb_compression=lz4

    # Set different compressions for different levels
    # For example, if --rocksdb_compression is snappy,
    # "no:no:lz4:lz4::zstd" is identical to "no:no:lz4:lz4:snappy:zstd:snappy"
    # In order to disable compression for level 0/1, set it to "no:no"
    --rocksdb_compression_per_level=

    # Whether or not to enable rocksdb's statistics, disabled by default
    --enable_rocksdb_statistics=false

    # Statslevel used by rocksdb to collection statistics, optional values are
    #   * kExceptHistogramOrTimers, disable timer stats, and skip histogram stats
    #   * kExceptTimers, Skip timer stats
    #   * kExceptDetailedTimers, Collect all stats except time inside mutex lock AND time spent on compression.
    #   * kExceptTimeForMutex, Collect all stats except the counters requiring to get time inside the mutex lock.
    #   * kAll, Collect all stats
    --rocksdb_stats_level=kExceptHistogramOrTimers

    # Whether or not to enable rocksdb's prefix bloom filter, disabled by default.
    --enable_rocksdb_prefix_filtering=false
    # Whether or not to enable the whole key filtering.
    --enable_rocksdb_whole_key_filtering=true
    # The prefix length for each key to use as the filter value.
    # can be 12 bytes(PartitionId + VertexID), or 16 bytes(PartitionId + VertexID + TagID/EdgeType).
    --rocksdb_filtering_prefix_length=12

    ############## rocksdb Options ##############
    # rocksdb DBOptions in json, each name and value of option is a string, given as "option_name":"option_value" separated by comma
    --rocksdb_db_options={}
    # rocksdb ColumnFamilyOptions in json, each name and value of option is string, given as "option_name":"option_value" separated by comma
    --rocksdb_column_family_options={"write_buffer_size":"67108864","max_write_buffer_number":"4","max_bytes_for_level_base":"268435456"}
    # rocksdb BlockBasedTableOptions in json, each name and value of option is string, given as "option_name":"option_value" separated by comma
    --rocksdb_block_based_table_options={"block_size":"8192"}
    ```

- 机器E配置

  - `nebula-graphd.conf`

    ```bash
    ########## basics ##########
    # Whether to run as a daemon process
    --daemonize=true
    # The file to host the process id
    --pid_file=pids/nebula-graphd.pid
    # Whether to enable optimizer
    --enable_optimizer=true

    ########## logging ##########
    # The directory to host logging files
    --log_dir=logs
    # Log level, 0, 1, 2, 3 for INFO, WARNING, ERROR, FATAL respectively
    --minloglevel=0
    # Verbose log level, 1, 2, 3, 4, the higher of the level, the more verbose of the logging
    --v=0
    # Maximum seconds to buffer the log messages
    --logbufsecs=0
    # Whether to redirect stdout and stderr to separate output files
    --redirect_stdout=true
    # Destination filename of stdout and stderr, which will also reside in log_dir.
    --stdout_log_file=graphd-stdout.log
    --stderr_log_file=graphd-stderr.log
    # Copy log messages at or above this level to stderr in addition to logfiles. The numbers of severity levels INFO, WARNING, ERROR, and FATAL are 0, 1, 2, and 3, respectively.
    --stderrthreshold=2

    ########## query ##########
    # Whether to treat partial success as an error.
    # This flag is only used for Read-only access, and Modify access always treats partial success as an error.
    --accept_partial_success=false

    ########## networking ##########
    # Comma separated Meta Server Addresses
    --meta_server_addrs=xxx.xxx.10.111:9559,xxx.xxx.10.112:9559,xxx.xxx.10.113:9559
    # Local IP used to identify the nebula-graphd process.
    # Change it to an address other than loopback if the service is distributed or
    # will be accessed remotely.
    --local_ip=xxx.xxx.10.115
    # Network device to listen on
    --listen_netdev=any
    # Port to listen on
    --port=9669
    # To turn on SO_REUSEPORT or not
    --reuse_port=false
    # Backlog of the listen socket, adjust this together with net.core.somaxconn
    --listen_backlog=1024
    # Seconds before the idle connections are closed, 0 for never closed
    --client_idle_timeout_secs=0
    # Seconds before the idle sessions are expired, 0 for no expiration
    --session_idle_timeout_secs=0
    # The number of threads to accept incoming connections
    --num_accept_threads=1
    # The number of networking IO threads, 0 for # of CPU cores
    --num_netio_threads=0
    # The number of threads to execute user queries, 0 for # of CPU cores
    --num_worker_threads=0
    # HTTP service ip
    --ws_ip=0.0.0.0
    # HTTP service port
    --ws_http_port=19669
    # HTTP2 service port
    --ws_h2_port=19670

    # The default charset when a space is created
    --default_charset=utf8
    # The defaule collate when a space is created
    --default_collate=utf8_bin

    ########## authorization ##########
    # Enable authorization
    --enable_authorize=false

    ########## Authentication ##########
    # User login authentication type, password for nebula authentication, ldap for ldap authentication, cloud for cloud authentication
    --auth_type=password
    ```

  - `nebula-storaged.conf`

    ```bash
    ########## basics ##########
    # Whether to run as a daemon process
    --daemonize=true
    # The file to host the process id
    --pid_file=pids/nebula-storaged.pid

    ########## logging ##########
    # The directory to host logging files
    --log_dir=logs
    # Log level, 0, 1, 2, 3 for INFO, WARNING, ERROR, FATAL respectively
    --minloglevel=0
    # Verbose log level, 1, 2, 3, 4, the higher of the level, the more verbose of the logging
    --v=0
    # Maximum seconds to buffer the log messages
    --logbufsecs=0
    # Whether to redirect stdout and stderr to separate output files
    --redirect_stdout=true
    # Destination filename of stdout and stderr, which will also reside in log_dir.
    --stdout_log_file=storaged-stdout.log
    --stderr_log_file=storaged-stderr.log
    # Copy log messages at or above this level to stderr in addition to logfiles. The numbers of severity levels INFO, WARNING, ERROR, and FATAL are 0, 1, 2, and 3, respectively.
    --stderrthreshold=2

    ########## networking ##########
    # Comma separated Meta server addresses
    --meta_server_addrs=xxx.xxx.10.111:9559,xxx.xxx.10.112:9559,xxx.xxx.10.113:9559
    # Local IP used to identify the nebula-storaged process.
    # Change it to an address other than loopback if the service is distributed or
    # will be accessed remotely.
    --local_ip=xxx.xxx.10.115
    # Storage daemon listening port
    --port=9779
    # HTTP service ip
    --ws_ip=0.0.0.0
    # HTTP service port
    --ws_http_port=19779
    # HTTP2 service port
    --ws_h2_port=19780
    # heartbeat with meta service
    --heartbeat_interval_secs=10

    ######### Raft #########
    # Raft election timeout
    --raft_heartbeat_interval_secs=30
    # RPC timeout for raft client (ms)
    --raft_rpc_timeout_ms=500
    ## recycle Raft WAL
    --wal_ttl=14400

    ########## Disk ##########
    # Root data path. Split by comma. e.g. --data_path=/disk1/path1/,/disk2/path2/
    # One path per Rocksdb instance.
    --data_path=data/storage

    # The default reserved bytes for one batch operation
    --rocksdb_batch_size=4096
    # The default block cache size used in BlockBasedTable.
    # The unit is MB.
    --rocksdb_block_cache=4
    # The type of storage engine, `rocksdb', `memory', etc.
    --engine_type=rocksdb

    # Compression algorithm, options: no,snappy,lz4,lz4hc,zlib,bzip2,zstd
    # For the sake of binary compatibility, the default value is snappy.
    # Recommend to use:
    #   * lz4 to gain more CPU performance, with the same compression ratio with snappy
    #   * zstd to occupy less disk space
    #   * lz4hc for the read-heavy write-light scenario
    --rocksdb_compression=lz4

    # Set different compressions for different levels
    # For example, if --rocksdb_compression is snappy,
    # "no:no:lz4:lz4::zstd" is identical to "no:no:lz4:lz4:snappy:zstd:snappy"
    # In order to disable compression for level 0/1, set it to "no:no"
    --rocksdb_compression_per_level=

    # Whether or not to enable rocksdb's statistics, disabled by default
    --enable_rocksdb_statistics=false

    # Statslevel used by rocksdb to collection statistics, optional values are
    #   * kExceptHistogramOrTimers, disable timer stats, and skip histogram stats
    #   * kExceptTimers, Skip timer stats
    #   * kExceptDetailedTimers, Collect all stats except time inside mutex lock AND time spent on compression.
    #   * kExceptTimeForMutex, Collect all stats except the counters requiring to get time inside the mutex lock.
    #   * kAll, Collect all stats
    --rocksdb_stats_level=kExceptHistogramOrTimers

    # Whether or not to enable rocksdb's prefix bloom filter, disabled by default.
    --enable_rocksdb_prefix_filtering=false
    # Whether or not to enable the whole key filtering.
    --enable_rocksdb_whole_key_filtering=true
    # The prefix length for each key to use as the filter value.
    # can be 12 bytes(PartitionId + VertexID), or 16 bytes(PartitionId + VertexID + TagID/EdgeType).
    --rocksdb_filtering_prefix_length=12

    ############## rocksdb Options ##############
    # rocksdb DBOptions in json, each name and value of option is a string, given as "option_name":"option_value" separated by comma
    --rocksdb_db_options={}
    # rocksdb ColumnFamilyOptions in json, each name and value of option is string, given as "option_name":"option_value" separated by comma
    --rocksdb_column_family_options={"write_buffer_size":"67108864","max_write_buffer_number":"4","max_bytes_for_level_base":"268435456"}
    # rocksdb BlockBasedTableOptions in json, each name and value of option is string, given as "option_name":"option_value" separated by comma
    --rocksdb_block_based_table_options={"block_size":"8192"}
    ```



### 3.启动集群

启动各个服务器上的对应进程。说明如下。

| 机器名称 |待启动的进程    | 
| :----- |:---------------|
| A      | graphd、storaged、metad|
| B      | graphd、storaged、metad|
| C      | graphd、storaged、metad |
| D      | graphd、storaged |
| E      | graphd、storaged |

启动Nebula Graph进程的命令如下：

```bash
sudo /usr/local/nebula/scripts/nebula.service start <metad|graphd|storaged|all>
```

!!! note

    - graphd、storaged和metad都启动时，可以用all代替。

    - `/usr/local/nebula`是Nebula Graph的默认安装路径，如果修改过安装路径，请使用实际路径。更多启停服务的内容，请参见[管理Nebula Graph服务](../2.quick-start/5.start-stop-service.md)。

### 4.检查集群

连接任何一个已启动graphd进程的机器，执行命令`SHOW HOSTS`检查集群状态。例如：

```bash
$ ./nebula-console --addr xxx.xxx.10.111 --port 9669 -u root -p nebula

2021/05/25 01:41:19 [INFO] connection pool is initialized successfully
Welcome to Nebula Graph!

> SHOW HOSTS
+------------------+------+----------+--------------+----------------------+------------------------+
| Host             | Port | Status   | Leader count | Leader distribution  | Partition distribution |
+------------------+------+----------+--------------+----------------------+------------------------+
| "xxx.xxx.10.111" | 9779 | "ONLINE" | 0            | "No valid partition" | "No valid partition"   |
+------------------+------+----------+--------------+----------------------+------------------------+
| "xxx.xxx.10.112" | 9779 | "ONLINE" | 0            | "No valid partition" | "No valid partition"   |
+------------------+------+----------+--------------+----------------------+------------------------+
| "xxx.xxx.10.113" | 9779 | "ONLINE" | 0            | "No valid partition" | "No valid partition"   |
+------------------+------+----------+--------------+----------------------+------------------------+
| "xxx.xxx.10.114" | 9779 | "ONLINE" | 0            | "No valid partition" | "No valid partition"   |
+------------------+------+----------+--------------+----------------------+------------------------+
| "xxx.xxx.10.115" | 9779 | "ONLINE" | 0            | "No valid partition" | "No valid partition"   |
+------------------+------+----------+--------------+----------------------+------------------------+
| "Total"          |      |          | 0            |                      |                        |
+------------------+------+----------+--------------+----------------------+------------------------+
```
