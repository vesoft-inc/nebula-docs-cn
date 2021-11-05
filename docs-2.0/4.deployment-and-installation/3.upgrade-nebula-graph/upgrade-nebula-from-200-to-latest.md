# 升级Nebula Graph v2.0.x至v{{nebula.release}}

Nebula Graph v2.0.x升级至v{{nebula.release}}，只需要使用v{{nebula.release}}的RPM/DEB包进行升级操作即可，或者[编译v{{nebula.release}}](../2.compile-and-install-nebula-graph/1.install-nebula-graph-by-compiling-the-source-code.md)之后重新安装。

!!! note

    Nebula Graph v2.0.x指v2.0.0-GA和v2.0.1版本。如果Nebula Graph版本过低（v2.0.0-RC、v2.0.0-beta、v1.x），请参见[升级 Nebula Graph 历史版本至 v{{nebula.release}}](upgrade-nebula-graph-to-latest.md)。

## RPM/DEB包升级步骤

1. 下载[RPM/DEB包](https://github.com/vesoft-inc/nebula-graph/releases/tag/v{{nebula.release}})。

2. 停止所有Nebula Graph服务。详情请参见[管理Nebula Graph服务](../../2.quick-start/5.start-stop-service.md)。建议更新前备份配置文件。

3. 执行如下命令升级：

   - RPM包

      ```bash
      $ sudo rpm -Uvh <package_name>
      ```
      
      若安装时指定路径，那么升级时也需要指定路径
      
      ```bash
      $ sudo rpm  -Uvh --prefix=<installation_path> <package_name> 
      ```
   - DEB包

      ```bash
      $ sudo dpkg -i <package_name>
      ```

4. 在每台服务器上启动所需的服务。详情请参见[管理Nebula Graph服务](../../2.quick-start/5.start-stop-service.md#_1)。

## 编译新版本源码升级步骤

1. 备份旧版本的配置文件。配置文件保存在Nebula Graph安装路径的`etc`目录内。

2. 更新仓库并编译源码。详情请参见[使用源码安装Nebula Graph](../2.compile-and-install-nebula-graph/1.install-nebula-graph-by-compiling-the-source-code.md)。

  !!! note

        编译时注意设置安装路径，和旧版本的安装路径保持一致。

## Docker Compose部署升级步骤

1. 修改目录`nebula-docker-compose`内的文件`docker-compose.yaml`，将`image`后的所有版本都修改为`{{nebula.branch}}`。

2. 在目录`nebula-docker-compose`内执行命令`docker-compose pull`，更新所有服务的镜像版本。
 
3. 执行命令`docker-compose down`停止Nebula Graph服务。

4. 执行命令`docker-compose up -d`启动Nebula Graph服务。
