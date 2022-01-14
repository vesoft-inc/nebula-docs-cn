# 获取 Nebula Exchange

本文介绍如何获取 Nebula Exchange 的 JAR 文件。

## 直接下载 JAR 文件

社区版 Exchange 的 JAR 文件可以直接[下载](https://github.com/vesoft-inc/nebula-exchange/releases)。

要下载企业版 Exchange，需先[获取 Nebula Graph 企业版套餐](https://nebula-graph.com.cn/pricing/)。

## 编译源代码获取 JAR 文件

社区版 Exchange 的 JAR 文件还可以通过编译源代码获取。下文介绍如何编译 Exchange 源代码。

!!! enterpriseonly

    企业版 Exchange 仅能在 Nebula Graph 企业版套餐中获取。

### 前提条件

- 安装 [Maven](https://maven.apache.org/download.cgi)。
- 根据数据源安装需要的 Spark 版本，从各数据源导出数据支持的 Spark 版本参见[软件依赖](about-exchange/ex-ug-limitations.md)。

### 操作步骤

1. 在根目录克隆仓库`nebula-exchange`。

  ```bash
  git clone -b {{exchange.branch}} https://github.com/vesoft-inc/nebula-exchange.git
  ```

2. 切换到目录`nebula-exchange`。

  ```bash
  cd nebula-exchange
  ```

3. 根据 Exchange 使用环境中的 Spark 版本打包 Exchange。

  - Spark 2.2：

    ```bash
    mvn clean package -Dmaven.test.skip=true -Dgpg.skip -Dmaven.javadoc.skip=true \
    -pl nebula-exchange_spark_2.2 -am -Pscala-2.11 -Pspark-2.2
    ```

  - Spark 2.4：

    ```bash
    mvn clean package -Dmaven.test.skip=true -Dgpg.skip -Dmaven.javadoc.skip=true \
    -pl nebula-exchange_spark_2.4 -am -Pscala-2.11 -Pspark-2.4
    ```

  - Spark 3.0：

    ```bash
    mvn clean package -Dmaven.test.skip=true -Dgpg.skip -Dmaven.javadoc.skip=true \
    -pl nebula-exchange_spark_3.0 -am -Pscala-2.12 -Pspark-3.0
    ```

编译成功后，可以在`nebula-exchange_spark_x.x/target/`目录里找到`nebula-exchange_spark_x.x-{{exchange.branch}}.jar`文件。`x.x`代表 Spark 版本，例如`2.4`。

!!! note
    JAR 文件版本号会因 Nebula Java Client 的发布版本而变化。用户可以在 [Releases 页面](https://github.com/vesoft-inc/nebula-java/releases)查看最新版本。

迁移数据时，用户可以参考配置文件 [`target/classes/application.conf`](https://github.com/vesoft-inc/nebula-exchange/blob/master/nebula-exchange/src/main/resources/application.conf)。

### 下载依赖包失败

如果编译时下载依赖包失败：

- 检查网络设置，确认网络正常。

- 修改 Maven 安装目录下`libexec/conf/settings.xml`文件的`mirror`部分：

  ```text
  <mirror>
   <id>alimaven</id>
   <mirrorOf>central</mirrorOf>
   <name>aliyun maven</name>
   <url>http://maven.aliyun.com/nexus/content/repositories/central/</url>
  </mirror>
  ```
