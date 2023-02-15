# 升级 NebulaGraph v3.x 至 v{{nebula.release}}

NebulaGraph v3.x 升级至 v{{nebula.release}}，只需要使用 v{{nebula.release}}的 RPM/DEB 包进行升级操作即可，或者[编译 v{{nebula.release}}](../2.compile-and-install-nebula-graph/1.install-nebula-graph-by-compiling-the-source-code.md) 之后重新安装。


!!! caution

    在升级部署了全文索引的 NebulaGraph 前，需要手动删除 Elasticsearch (ES) 中的全文索引。在升级后需要重新使用`SIGN IN`语句登录 ES 并重新创建全文索引。用户可通过 cURL 命令手动删除 ES 中全文索引。命令为`curl -XDELETE -u <es_username>:<es_password> '<es_access_ip>:<port>/<fullindex_name>'`，例如`curl -XDELETE -u elastic:elastic 'http://192.168.8.223:9200/nebula_index_2534'`。如果 ES 没有设置用户名及密码，则无需指定`-u`选项。 
   

## RPM/DEB 包升级步骤

1. 下载 [RPM/DEB 包](https://www.nebula-graph.com.cn/download)。

2. 停止所有 NebulaGraph 服务。详情请参见[管理 NebulaGraph 服务](../../2.quick-start/3.quick-start-on-premise/5.start-stop-service.md)。建议更新前备份配置文件。

  !!! caution

        如果用户需要保留无 Tag 的点，在集群内所有 Graph 服务的配置文件（`nebula-graphd.conf`）中新增`--graph_use_vertex_key=true`；在所有 Storage 服务的配置文件（`nebula-storaged.conf`）中新增`--use_vertex_key=true`。

3. 执行如下命令升级：

   - RPM 包

      ```bash
      $ sudo rpm -Uvh <package_name>
      ```
      
      若安装时指定路径，那么升级时也需要指定路径
      
      ```bash
      $ sudo rpm  -Uvh --prefix=<installation_path> <package_name> 
      ```
   
   - DEB 包

      ```bash
      $ sudo dpkg -i <package_name>
      ```

4. 在每台服务器上启动所需的服务。详情请参见[管理 NebulaGraph 服务](../../2.quick-start/3.quick-start-on-premise/5.start-stop-service.md#_1)。

## 编译新版本源码升级步骤

1. 备份旧版本的配置文件。配置文件保存在 NebulaGraph 安装路径的`etc`目录内。

2. 更新仓库并编译源码。详情请参见[使用源码安装 NebulaGraph](../2.compile-and-install-nebula-graph/1.install-nebula-graph-by-compiling-the-source-code.md)。

  !!! note

        编译时注意设置安装路径，和旧版本的安装路径保持一致。

## Docker Compose 部署

!!! caution
    
    Docker Compose 部署的 NebulaGraph 建议重新部署新版本后导入数据。
