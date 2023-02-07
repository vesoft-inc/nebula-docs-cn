# 升级企业版 NebulaGraph 3.x 至 3.4.0  

本文以企业版 NebulaGraph 3.1.0 为例，介绍如何升级至 3.4.0。

## 升级说明

- 此升级操作仅适用于升级企业版 NebulaGraph 3.x 至 3.4.0。<!--因为企业版 NebulaGraph 3.4 中一个分片对应一个 RocksDB 实例不同于 3.4 之前的一个图空间对应一个 RocksDB 实例。--> 如果您的企业版 NebulaGraph 版本低于 3.0.0，请先升级到企业版 3.x 再升级到 3.4.0。具体操作请参见[升级 NebulaGraph 2.x 至 3.1.0](https://docs.nebula-graph.com.cn/3.1.0/4.deployment-and-installation/3.upgrade-nebula-graph/upgrade-nebula-graph-to-latest/)。

- 执行升级操作的集群 IP 地址必须与原集群相同。
  
- 机器硬盘剩余空间至少需为原数据目录的 1.5 倍。
  

## 升级步骤

1. [联系我们获取](https://www.nebula-graph.com.cn/contact)企业版 NebulaGraph v3.4.0 的安装包并安装。
   
  !!! note

        不同安装包的升级步骤相同。本文以 RPM 包且安装目录为`/usr/local/nebulagraph-ent-3.4`为例。具体操作请参见[安装 RPM 包](../2.compile-and-install-nebula-graph/2.install-nebula-graph-by-rpm-or-deb.md)。 
   
  !!! caution

        请确保 3.4.0 集群的 Meta 服务和 Storage 服务的配置文件中的`--data_path`参数设置的存储路径数量与 3.x 集群的配置文件中的`--data_path`参数配置的路径数量相同。否则，升级后的集群无法启动。

2. 停止企业版 NebulaGraph v3.x 服务。详情请参见[管理 NebulaGraph 服务](../../2.quick-start/3.quick-start-on-premise/5.start-stop-service.md)。
  运行命令后可继续运行`nebula.service status all`命令以确认所有服务都已停止。
   
3. 在企业版 NebulaGraph v3.4.0 的安装目录下，分别执行以下命令以升级 Storage 和 Meta 服务。<!-- 不需要事先创建`data`目录 -->

  - 升级 Storage 服务：

    命令：

    ```bash
    sudo ./bin/db_upgrader  --max_concurrent_parts=<num> --src_db_path=<source_storage_data_path> --dst_db_path=<destination_storage_data_path>
    ```

    | 参数            | 说明                         |
    | :-------------- | :--------------------------- |
    | `--max_concurrent_parts` | 指定同时升级的分片数量，默认值为 `1`。<br/>建议根据磁盘性能适当调大。 |
    | `--src_db_path` | 指定源数据目录的绝对路径。下述示例源数据的目录为`/usr/local/nebula-ent-3.1.0/data/storage`。  |
    | `--dst_db_path` | 指定目标数据目录的绝对路径。本文示例的目标数据目录为`/usr/local/nebula-ent-3.4/data/storage`。|

    示例：

    ```bash
    sudo ./bin/db_upgrader --max_concurrent_parts=20 --src_db_path=/usr/local/nebula-ent-3.1.0/data/storage --dst_db_path=/usr/local/nebula-ent-3.4/data/storage
    ```

    如果有多个源数据目录，请分别指定不同的源数据目录和目标数据目录并执行命令。例如，有两个源数据目录`/usr/local/nebula-ent-3.1.0/data/storage`和`/usr/local/nebula-ent-3.1.0/data2/storage`，则执行以下命令：

    ```bash
    sudo ./bin/db_upgrader --src_db_path=/usr/local/nebula-ent-3.1.0/data/storage --dst_db_path=/usr/local/nebula-ent-3.4/data/storage

    sudo ./bin/db_upgrader --src_db_path=/usr/local/nebula-ent-3.1.0/data2/storage --dst_db_path=/usr/local/nebula-ent-3.4/data2/storage
    ```

  - 升级 Meta 服务：

    命令：

    ```bash
    sudo ./bin/meta_upgrader --src_meta_path=<source_meta_data_path> --dst_meta_path=<destination_meta_data_path>
    ```

    | 参数            | 说明                         |
    | :-------------- | :--------------------------- |
    | `--src_meta_path` | 指定源 Meta 数据目录的绝对路径。下述示例源数据的目录为`/usr/local/nebula-ent-3.1.0/data/meta`。  |
    | `--dst_meta_path` | 指定目标 Meta 数据目录的绝对路径。本文示例的目标数据目录为`/usr/local/nebula-ent-3.4/data/meta`。|

    示例：

    ```bash
    sudo ./bin/meta_upgrader --src_meta_path=/usr/local/nebula-ent-3.1.0/data/meta --dst_meta_path=/usr/local/nebula-ent-3.4/data/meta
    ```

    如果有多个源 Meta 数据目录，请指定不同的源 Meta 数据目录和目标 Meta 数据目录并分别执行命令。

  服务升级完成后，会在 v3.4.0 的安装目录下生成`data`目录，其中包含升级后的数据文件。

4. 上传 License 文件至 v3.4.0 的安装目录下的`share/resources`内。

5. 启动和连接企业版 NebulaGraph v3.4.0 服务后，验证数据是否正确。参考命令如下：
   
  ```
  nebula> SHOW HOSTS;
  nebula> SHOW HOSTS storage;
  nebula> SHOW SPACES;
  nebula> USE <space_name>
  nebula> SHOW PARTS;
  nebula> SUBMIT JOB STATS;
  nebula> SHOW STATS;
  nebula> MATCH (v) RETURN v LIMIT 5;
  ```

## Docker Compose 部署

!!! caution
    
    Docker Compose 部署的 NebulaGraph 建议重新部署新版本后导入数据。




  
