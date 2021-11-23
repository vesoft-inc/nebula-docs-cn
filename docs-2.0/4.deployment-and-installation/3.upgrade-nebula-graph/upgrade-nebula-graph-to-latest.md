# 升级 Nebula Graph 历史版本至 v{{nebula.release}}

Nebula Graph 历史版本指低于 Nebula Graph v2.0.0-GA 的版本，本文介绍如何升级历史版本至 v{{nebula.release}}。

!!! note

    Nebula Graph v2.0.0-GA 或更新版本升级至 v{{nebula.release}}，请参见 [Nebula Graph v2.0.x 升级至 v{{nebula.release}}](upgrade-nebula-from-200-to-latest.md)。

## 升级限制

- 不支持轮转热升级，需完全停止整个集群服务。

- 未提供升级脚本，需手动在每台服务器上依次执行。

- **不支持**基于 Docker 容器（包括 Docker Swarm、Docker Compose、K8s）的升级。

- 必须在原服务器上原地升级，不能修改原机器的 IP 地址、配置文件，不可更改集群拓扑。

- 硬盘空间要求：各机器硬盘剩余空间都需要是原数据目录的**三倍**。

- 已知会造成数据丢失的 4 种场景，和 alter schema 以及 default value 相关，请参见 [github known issues](https://github.com/vesoft-inc/nebula-graph/issues/857)。

- 所有的客户端均需要升级，通信协议不兼容。

- 升级时间大约需要 30 分钟（取决于具体配置），请参见文末测试环境。

- 数据目录不要使用软连接切换，避免失效。

- 升级操作需要有 sudo 权限。

## 前置条件说明

### 历史版本安装目录

默认情况下，历史版本安装的根目录为`/usr/local/nebula/`（下文记为 `${nebula-old}`）。默认配置文件目录为 `${nebula-old}/etc/`。

- `${nebula-old}/etc/nebula-storaged.conf`文件中的`--data_path`参数指定了 storaged 数据目录的位置，其默认值为`data/storage`。

- `${nebula-old}/etc/nebula-metad.conf`文件中的`--data_path`参数指定了 metad 数据目录位置，其默认值为`data/meta`。

!!! Note

    Nebula Graph 的实际安装路径可能和本文示例不同，请使用实际路径。用户也可以用 `ps -ef | grep nebula` 中的参数来找到实际使用的配置文件地址。

### 新版本安装目录

本文中新版本安装目录记为 `${nebula-new}` （例如 `/usr/local/nebula-new/`)。

```
# mkdir -p ${nebula-new}
```

## 升级步骤

1. **停止所有客户端访问**。也可以通过在每台服务器上关闭 graphd 服务避免脏写。在每台服务器上运行如下命令。

   ```
   # ${nebula-old}/scripts/nebula.service stop graphd
   [INFO] Stopping nebula-graphd...
   [INFO] Done
   ```

2. 停止历史版本服务。在每台服务器上运行如下命令。

   ```
   # ${nebula-old}/scripts/nebula.service stop all
   [INFO] Stopping nebula-metad...
   [INFO] Done
   [INFO] Stopping nebula-graphd...
   [INFO] Done
   [INFO] Stopping nebula-storaged...
   [INFO] Done
   ```

   运行 `ps -ef | grep nebula` 检查所有 nebula 服务都已停止。`storaged` 进程 flush 数据可能要等待 1 分钟。

  !!! Note

        如果超过 20 分钟不能停止服务，**放弃本次升级**，并在论坛提交问题。

3. 在每台服务器上运行如下命令。

   1. 安装新的二进制文件。

    - 如果从 RPM/DEB 安装，从 [release page](https://github.com/vesoft-inc/nebula-graph/releases) 下载对应操作系统的安装包。

       ```
       # sudo rpm --force -i --prefix=${nebula-new}  ${nebula-package-name.rpm} # for centos/redhat
       # sudo dpkg -i --instdir==${nebula-new} ${nebula-package-name.deb} # for ubuntu
       ```

       具体步骤请参见 [从 RPM/DEB 安装](../2.compile-and-install-nebula-graph/2.install-nebula-graph-by-rpm-or-deb.md)。

    - 如果从源代码安装。具体步骤请参见 [从源代码安装](../2.compile-and-install-nebula-graph/1.install-nebula-graph-by-compiling-the-source-code.md)。这里列出几个关键命令：

      - clone 源代码
  
        ```
        # git clone --branch {{nebula.branch}} https://github.com/vesoft-inc/nebula-graph.git
        ```

      - 设置 CMake

        ```
        # cmake -DCMAKE_INSTALL_PREFIX=${nebula-new} -DENABLE_TESTING=OFF -DCMAKE_BUILD_TYPE=Release .. 
        ```

   2. 拷贝配置文件。

       ```
       # cp -rf ${nebula-old}/etc ${nebula-new}/
       ```

4. 在曾经运行 metad 的服务器上（通常为 3 台），拷贝 metad 数据、配置文件到新目录。

   - 拷贝 metad 数据

     在 `${nebula-old}/etc/nebula-metad.conf` 中找到 `--data_path` 项（其默认值为 `data/meta`）

     - 如果历史版本配置**未更改** `--data_path` 项，则可以运行如下命令，将 metad 数据拷贝到新目录。

       ```
       # mkdir -p ${nebula-new}/data/meta/
       # cp -r ${nebula-old}/data/meta/* ${nebula-new}/data/meta/
       ```

     - 如果历史版本配置更改了默认的 metad 目录，请根据实际目录拷贝。

   - 拷贝并修改配置文件

     - 编辑新的 metad 配置文件：

       ```
       # vim ${nebula-new}/nebula-metad.conf
       ```

     - [可选] 增加配置项：

       `--null_type=false`: 升级后的 Schema 的属性是否要支持 [`NULL`](../../3.ngql-guide/3.data-types/5.null.md)，**默认为 true**。不希望支持 NULL 的话，设置为 false。此时，升级后的 Schema 如果要增加属性（ALTER TAG/EDGE）必须指定 [default 值](../../3.ngql-guide/10.tag-statements/1.create-tag.md)，否则会读不出数据。

       `--string_index_limit=32`: 升级后 string 对应的 [索引的长度](../../3.ngql-guide/14.native-index-statements/1.create-native-index.md)，不加的话系统默认为 64。

    !!! Note

        请确保在每个 metad 服务器都完成了以上操作。

5. 在每个 storaged 服务器上，修改 storaged 配置文件。

   + [可选] 如果历史版本 storaged 数据目录 `--data_path=data/storage` 不是默认值，有更改。

      ```
      # vim ${nebula-new}/nebula-storaged.conf
      ```
      `--data_path`设置为新的 storaged 数据目录地址。

   + 创建新版本 storaged 数据目录。

      ```
      # mkdir -p ${nebula-new}/data/storage/
      ```

   如果`${nebula-new}/etc/nebula-storaged.conf` 中的 `--data_path` 有改动，请按实际路径创建。

6. 启动新版本的 metad 进程。

   - 在每个 metad 的服务器上运行如下命令。

      ```
      # ${nebula-new}/scripts/nebula.service start metad
      [INFO] Starting nebula-metad...
      [INFO] Done
      ```

   - 检查每个 metad 进程是否正常。

      ```
      # ps -ef |grep nebula-metad
      ```

   - 检查 metad 日志`${nebula-new}/logs/` 下的 ERROR 日志。
  
  !!! Note

        如果服务异常：请查看目录`${nebula-new}/logs`内的 metad 相关日志，并在论坛提交问题。**放弃本次升级，在原目录正常启动 nebula 服务。**

7. 升级 storaged 数据格式。

   在每个 storaged 服务器运行如下命令。

   ```
   # ${nebula-new}/bin/db_upgrader  \
   --src_db_path=<old_storage_directory_path> \
   --dst_db_path=<new_storage_directory_path>  \
   --upgrade_meta_server=<meta_server_ip1>:<port1>[,<meta_server_ip2>:<port2>,...] \
   --upgrade_version=<old_nebula_version> \
   ```
    
   参数说明：

   - `--src_db_path`：**历史版本** storaged 的数据目录的绝对路径，多个目录用逗号分隔，不加空格。

   - `--dst_db_path`：**新版本** storaged 的数据目录的绝对路径，多个目录用逗号分隔。逗号分隔的目录必须和`--src_db_path`中一一对应。

   - `--upgrade_meta_server` ：步骤 6 中启动的所有新 metad 的地址。

   - `--upgrade_version`：如果历史版本为 v1.2.x，则填写 1；如果历史版本为 v2.0.0-RC，则填写 2。不可填写其他数字。
    
  !!! danger

        请勿颠倒`--src_db_path`和`--dst_db_path`的顺序，否则会升级失败且破坏历史版本的数据。

   例如，从 v1.2.x 升级：

   ```
   # /usr/local/nebula_new/bin/db_upgrader \
   --src_db_path=/usr/local/nebula/data/storage/data1/,/usr/local/nebula/data/storage/data2/ \
   --dst_db_path=/usr/local/nebula_new/data/storage/data1/,/usr/local/nebula_new/data/storage/data2/\
   --upgrade_meta_server=192.168.*.14:45500,192.168.*.15:45500,192.168.*.16:45500 \
   --upgrade_version=1
   ```

   从 v2.0.0-RC 升级：

   ```
   # /usr/local/nebula_new/bin/db_upgrader \
   --src_db_path=/usr/local/nebula/data/storage/ \
   --dst_db_path=/usr/local/nebula_new/data/storage/ \
   --upgrade_meta_server=192.168.*.14:9559,192.168.*.15:9559,192.168.*.16:9559 \
   --upgrade_version=2
   ```

  !!! Note
  
      - 如果工具抛出异常请在论坛提交问题。**放弃本次升级，关闭所有已经启动的 metad，在原目录正常启动 nebula 服务。**
      - 请确保在每个 storaged 服务器都完成了以上操作。

8. 在每个 storaged 服务器启动新版本的 storaged 服务。

   ```
   # ${nebula-new}/scripts/nebula.service start storaged
   # ${nebula-new}/scripts/nebula.service status storaged
   ```

  !!! Note

        如果有 storaged 未正常启动，请将日志`${nebula-new}/logs/`在论坛提交问题。**放弃本次升级，关闭所有已经启动的 metad 和 storaged，在原目录正常启动 nebula 服务。**

9. 在每个 graphd 服务器启动新版本的 graphd 服务。

   ```
   # ${nebula-new}/scripts/nebula.service start graphd
   # ${nebula-new}/scripts/nebula.service status graphd
   ```
  !!! Note

        如果有 graphd 未正常启动，请将日志`${nebula-new}/logs/`在论坛提交问题。**放弃本次升级，关闭所有已经启动的 metad,storaged,graphd. 在原目录正常启动 nebula 服务。**

10.  使用 [新版本 Nebula Console](https://github.com/vesoft-inc/nebula-console) 连接新的 Nebula Graph，验证服务是否可用、数据是否正常。命令行参数，如 graphd 的 IP、端口都不变。

    ```ngql
    nebula> SHOW HOSTS;
    nebula> SHOW SPACES;
    nebula> USE <space_name>
    nebula> SHOW PARTS;
    nebula> SUBMIT JOB STATS;
    nebula> SHOW STATS;
    ```

  !!! Note

        历史版本 Nebula Console 可能会有兼容性问题。

11.  升级其他客户端。

    所有的客户端都必须升级到支持 Nebula Graph v{{nebula.release}}  的版本。包括但不限于 [Python](https://github.com/vesoft-inc/nebula-python)、[Java](https://github.com/vesoft-inc/nebula-java)、[go](https://github.com/vesoft-inc/nebula-go)、[C++](https://github.com/vesoft-inc/nebula-cpp)、[Flink-connector](https://github.com/vesoft-inc/nebula-flink-connector)、[Algorithm](https://github.com/vesoft-inc/nebula-algorithm)、[Exchange](https://github.com/vesoft-inc/nebula-exchange)、[Spark-connector](https://github.com/vesoft-inc/nebula-spark-connector)、[Nebula Bench](https://github.com/vesoft-inc/nebula-bench)。请找到各 repo 对应的 branch。

  !!! Note

        不兼容历史版本的通信协议。需重新源代码编译或者下载二进制包。
        
        运维提醒：升级后的数据目录为`${nebula-new}/`。如有硬盘容量监控、日志、ELK 等，请做相应改动。

## 升级失败回滚

如果升级失败，请停止新版本的所有服务，启动历史版本的所有服务。

所有周边客户端也切换为**历史版本**。

## 附 1：升级测试环境

本文测试升级的环境如下：

- 机器配置：32 核 CPU、62 GB 内存、SSD

- 数据规模：Nebula Graph 1.2 版本 LDBC 测试数据 100 GB（1 个图空间、24 个分片、data 目录 92 GB）

- 并发参数：`--max_concurrent=5`、`--max_concurrent_parts=24`、`--write_batch_num=100`

升级共耗时** 21 分钟**（其中 compaction 耗时 13 分钟）。工具并发参数说明如下：

|参数名称|默认值|
|:---|:---|
|`--max_concurrent`|5|
|`--max_concurrent_parts`|10|
|`--write_batch_num`|100|

## 附 2：Nebula Graph v2.0.0 代码地址和 commit id

| 地址 | commit id |
|:---|:---|
| [graphd](https://github.com/vesoft-inc/nebula-graph/releases/tag/v2.0.0) | 91639db |
| [storaged 和 metad](https://github.com/vesoft-inc/nebula-storage/tree/v2.0.0) | 761f22b |
| [common](https://github.com/vesoft-inc/nebula-common/tree/v2.0.0) | b2512aa |

## FAQ

Q：升级过程中是否可以通过客户端写入数据？

A：不可以。这个过程中写入的数据状态是未定义的。

Q：除了 v1.2.x 和 v2.0.0-RC 外，其他版本是否支持升级？

A：未验证过。理论上 v1.0.0 - v1.2.0 都可以采用 v1.2.x 的升级版本。 v2.0.0-RC 之前的日常研发版本（nightly）无升级方案。

Q：如果某台机器只有 graphd 服务，没有 storaged 服务，如何升级？

A：只需要升级 graphd 对应的 binary （或者 RPM 包）。

Q：操作报错 `Permission denied`。

A：部分命令需要有 sudo 权限。

Q：是否有 gflags 发生改变？

A: 目前已知的 gflags 改变整理在 [github issues](https://github.com/vesoft-inc/nebula/issues/2501)。

Q：删除数据重新安装，和升级有何不同？

A：v2.x 的默认配置（包括端口）与 v1.x 不同。升级方案沿用老的配置，删除重新安装沿用新的配置。

Q：是否有工具或者办法验证新旧版本数据是否一致？

A：没有。
