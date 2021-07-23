# Nebula Graph v2.0.0升级至v2.0.1

Nebula Graph v2.0.0升级至v2.0.1，只需要使用v2.0.1的RPM/DEB包进行升级操作即可，或者[编译v2.0.1](2.compile-and-install-nebula-graph/1.install-nebula-graph-by-compiling-the-source-code.md)之后重新安装。

!!! note
    如果Nebula Graph版本过低，需要先升级至v2.0.0，详情请参见[升级 Nebula Graph 历史版本至 v2.0.0](3.upgrade-nebula-graph.md)。

## RPM/DEB包升级步骤

1. 下载[RPM/DEB包](https://github.com/vesoft-inc/nebula-graph/releases/tag/v2.0.1)。

2. 停止所有Nebula Graph服务。详情请参见[管理Nebula Graph服务](../2.quick-start/5.start-stop-service.md#_1)。

3. 执行如下命令升级：

   - RPM包

      ```bash
      $ sudo rpm -Uivh <package_name>
      ```

   - DEB包

      ```bash
      $ sudo dpkg -i <package_name>
      ```

4. 在每台服务器上启动所需的服务。详情请参见[管理Nebula Graph服务](../2.quick-start/5.start-stop-service.md#_1)。

## 编译新版本源码升级步骤

1. 备份旧版本的配置文件。配置文件保存在Nebula Graph安装路径的`etc`目录内。

2. 更新仓库并编译源码。详情请参见[使用源码安装Nebula Graph](2.compile-and-install-nebula-graph/1.install-nebula-graph-by-compiling-the-source-code.md)。

  !!! note

        编译时注意设置安装路径，和旧版本的安装路径保持一致。

## Docker Compose部署升级步骤

请参见[如何更新Nebula Graph服务的Docker镜像](../2.compile-and-install-nebula-graph/3.deploy-nebula-graph-with-docker-compose.md#nebula_graphdocker)。