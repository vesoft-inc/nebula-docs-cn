# Exchange 常见问题

## 编译问题

### Q：部分非 central 仓库的包下载失败，报错`Could not resolve dependencies for project xxx`

请检查 Maven 安装目录下`libexec/conf/settings.xml`文件的`mirror`部分：

```text
<mirror>
    <id>alimaven</id>
    <mirrorOf>central</mirrorOf>
    <name>aliyun maven</name>
    <url>http://maven.aliyun.com/nexus/content/repositories/central/</url>
</mirror>
```

检查`mirrorOf`的值是否配置为`*`，如果为`*`，请修改为`central`或`*,!SparkPackagesRepo,!bintray-streamnative-maven`。

**原因**：Exchange 的`pom.xml`中有两个依赖包不在 Maven 的 central 仓库中，`pom.xml`配置了这两个依赖所在的仓库地址。如果 maven 中配置的镜像地址对应的`mirrorOf`值为`*`，那么所有依赖都会在 central 仓库下载，导致下载失败。

### Q：编译 Exchange 时无法下载 SNAPSHOT 包

现象：编译时提示`Could not find artifact com.vesoft:client:jar:xxx-SNAPSHOT`。

原因：本地 maven 没有配置用于下载 SNAPSHOT 的仓库。maven 中默认的 central 仓库用于存放正式发布版本，而不是开发版本（SNAPSHOT）。

解决方案：在 maven 的 setting.xml文件的`profiles`作用域内中增加以下配置：

```
  <profile>
     <activation>
        <activeByDefault>true</activeByDefault>
     </activation>
     <repositories>
        <repository>
            <id>snapshots</id>
            <url>https://oss.sonatype.org/content/repositories/snapshots/</url>
            <snapshots>
               <enabled>true</enabled>
            </snapshots>
      </repository>
     </repositories>
  </profile>
```

## 执行问题

### Q：Yarn-Cluster 模式下如何提交？

在 Yarn-Cluster 模式下提交任务，请参考如下命令：

```bash
$SPARK_HOME/bin/spark-submit --class com.vesoft.nebula.exchange.Exchange \
--master yarn-cluster \
--files application.conf \
--conf spark.driver.extraClassPath=./ \
--conf spark.executor.extraClassPath=./ \
nebula-exchange-3.0.0.jar \
-c application.conf
```

### Q：报错`method name xxx not found`

一般是端口配置错误，需检查 Meta 服务、Graph 服务、Storage 服务的端口配置。

### Q：报 NoSuchMethod、MethodNotFound 错误（`Exception in thread "main" java.lang.NoSuchMethodError`等）

绝大多数是因为 JAR 包冲突和版本冲突导致的报错，请检查报错服务的版本，与 Exchange 中使用的版本进行对比，检查是否一致，尤其是 Spark 版本、Scala 版本、Hive 版本。

### Q：Exchange 导入 Hive 数据时报错`Exception in thread "main" org.apache.spark.sql.AnalysisException: Table or view not found`

检查提交 exchange 任务的命令中是否遗漏参数`-h`，检查 table 和 database 是否正确，在 spark-sql 中执行用户配置的 exec 语句，验证 exec 语句的正确性。

### Q：运行时报错`com.facebook.thrift.protocol.TProtocolException: Expected protocol id xxx`

请检查 Nebula Graph 服务端口配置是否正确。

- 如果是源码、RPM 或 DEB 安装，请配置各个服务的配置文件中`--port`对应的端口号。

- 如果是 docker 安装，请配置 docker 映射出来的端口号，查看方式如下：

    在`nebula-docker-compose`目录下执行`docker-compose ps`，例如：

    ```bash
    $ docker-compose ps
                  Name                             Command                  State                                                         Ports
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    nebula-docker-compose_graphd_1      /usr/local/nebula/bin/nebu ...   Up (healthy)   0.0.0.0:33205->19669/tcp, 0.0.0.0:33204->19670/tcp, 0.0.0.0:9669->9669/tcp
    nebula-docker-compose_metad0_1      ./bin/nebula-metad --flagf ...   Up (healthy)   0.0.0.0:33165->19559/tcp, 0.0.0.0:33162->19560/tcp, 0.0.0.0:33167->9559/tcp, 9560/tcp
    nebula-docker-compose_metad1_1      ./bin/nebula-metad --flagf ...   Up (healthy)   0.0.0.0:33166->19559/tcp, 0.0.0.0:33163->19560/tcp, 0.0.0.0:33168->9559/tcp, 9560/tcp
    nebula-docker-compose_metad2_1      ./bin/nebula-metad --flagf ...   Up (healthy)   0.0.0.0:33161->19559/tcp, 0.0.0.0:33160->19560/tcp, 0.0.0.0:33164->9559/tcp, 9560/tcp
    nebula-docker-compose_storaged0_1   ./bin/nebula-storaged --fl ...   Up (healthy)   0.0.0.0:33180->19779/tcp, 0.0.0.0:33178->19780/tcp, 9777/tcp, 9778/tcp, 0.0.0.0:33183->9779/tcp, 9780/tcp
    nebula-docker-compose_storaged1_1   ./bin/nebula-storaged --fl ...   Up (healthy)   0.0.0.0:33175->19779/tcp, 0.0.0.0:33172->19780/tcp, 9777/tcp, 9778/tcp, 0.0.0.0:33177->9779/tcp, 9780/tcp
    nebula-docker-compose_storaged2_1   ./bin/nebula-storaged --fl ...   Up (healthy)   0.0.0.0:33184->19779/tcp, 0.0.0.0:33181->19780/tcp, 9777/tcp, 9778/tcp, 0.0.0.0:33185->9779/tcp, 9780/tcp
    ```

    查看`Ports`列，查找 docker 映射的端口号，例如：

    - Graph 服务可用的端口号是 9669。

    - Meta 服务可用的端口号有 33167、33168、33164。

    - Storage 服务可用的端口号有 33183、33177、33185。

### Q：运行时报错`Exception in thread "main" com.facebook.thrift.protocol.TProtocolException: The field 'code' has been assigned the invalid value -4`

检查 Exchange 版本与 Nebula Graph 版本是否匹配，详细信息可参考[使用限制](../nebula-exchange/about-exchange/ex-ug-limitations.md)。

### Q：将 Hive 中的数据导入 Nebula Graph 时出现乱码如何解决？

如果 Hive 中数据的属性值包含中文字符，可能出现该情况。解决方案是在导入命令中的 JAR 包路径前加上以下选项：

```bash
--conf spark.driver.extraJavaOptions=-Dfile.encoding=utf-8
--conf spark.executor.extraJavaOptions=-Dfile.encoding=utf-8
```

即：

```bash
<spark_install_path>/bin/spark-submit --master "local" \
--conf spark.driver.extraJavaOptions=-Dfile.encoding=utf-8 \
--conf spark.executor.extraJavaOptions=-Dfile.encoding=utf-8 \
--class com.vesoft.nebula.exchange.Exchange \
<nebula-exchange-3.x.y.jar_path> -c <application.conf_path>
```

如果是在 YARN 中，则用以下命令：

```bash
<spark_install_path>/bin/spark-submit \
--class com.vesoft.nebula.exchange.Exchange \
--master yarn-cluster \
--files <application.conf_path> \
--conf spark.driver.extraClassPath=./ \
--conf spark.executor.extraClassPath=./ \
--conf spark.driver.extraJavaOptions=-Dfile.encoding=utf-8 \
--conf spark.executor.extraJavaOptions=-Dfile.encoding=utf-8 \
<nebula-exchange-3.x.y.jar_path> \
-c application.conf
```

### Q：Hive 数据导入时提示 schema 版本不一致

Spark 日志提示 `Hive Schema version 1.2.0 does not match metastore's schema version 2.1.0 Metastore is not upgraded or corrupt` 的原因是 Hive 环境中配置的 metastore schema 版本和 Spark 使用的 metastore 版本不一致。

解决方法：

1. 将 Hive 环境中存储 Hive metastore 信息的 MySQL version 信息更新为 Spark 中使用的 metastore 版本。

    假设 Hive 在 MySQL 中存储 metastore 的数据库是`hive`，需要按如下方式修改 `hive.VERSION` 表中的 `version` 字段：

    ```
    update hive.VERSION set SCHEMA_VERSION="2.1.0" where VER_ID=1
    ```

2. 在 Hive 环境的 `hive-site.xml` 文件中增加如下配置：

    ```
    <property>
    <name>hive.metastore.schema.verification</name>
    <value>false</value>
    </property>
    ```

3. 重启 Hive。

### Q: 生成 SST 时提示 org.rocksdb.RocksDBException: While open a file for appending: /path/sst/1-xxx.sst: No such file or directory

排查方法：

1. 检查`/path`是否存在，如没有或者路径设置错误，创建或修正路径。
2. 检查 Spark 在每台机器上的当前用户对`/path`是否有操作权限，如没有，添加权限。

## 配置问题

### Q：哪些配置项影响导入性能？

- batch：每次发送给 Nebula Graph 服务的 nGQL 语句中包含的数据条数。

- partition：Spark 数据的分区数，表示数据导入的并发数。

- nebula.rate：向 Nebula Graph 发送请求前先去令牌桶获取令牌。

    - limit：表示令牌桶的大小。

    - timeout：表示获取令牌的超时时间。

根据机器性能可适当调整这四项参数的值。如果在导入过程中，Storage 服务的 leader 变更，可以适当调小这四项参数的值，降低导入速度。

## 其他问题

### Q：Exchange 支持哪些版本的 Nebula Graph？

请参见 Exchange 的[使用限制](about-exchange/ex-ug-limitations.md)。

### Q：Exchange 与 Spark Writer 有什么关系？

Exchange 是在 Spark Writer 基础上开发的 Spark 应用程序，二者均适用于在分布式环境中将集群的数据批量迁移到 Nebula Graph 中，但是后期的维护工作将集中在 Exchange 上。与 Spark Writer 相比，Exchange 有以下改进：

- 支持更丰富的数据源，如 MySQL、Neo4j、Hive、HBase、Kafka、Pulsar 等。

- 修复了 Spark Writer 的部分问题。例如 Spark 读取 HDFS 里的数据时，默认读取到的源数据均为 String 类型，可能与 Nebula Graph 定义的 Schema 不同，所以 Exchange 增加了数据类型的自动匹配和类型转换，当 Nebula Graph 定义的 Schema 中数据类型为非 String 类型（如 double）时，Exchange 会将 String 类型的源数据转换为对应的类型（如 double）。

### Q：Exchange 传输数据的性能如何？

Exchange 的性能测试数据和测试方法参见 [Nebula Exchange test result](https://github.com/vesoft-inc/nebula-exchange/blob/{{exchange.branch}}/bench/exchange-test.md)。
