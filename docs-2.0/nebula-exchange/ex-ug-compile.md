# 编译Exchange

本文介绍如何编译Nebula Exchange。用户也可以直接[下载](https://repo1.maven.org/maven2/com/vesoft/nebula-exchange/)编译完成的`.jar`文件。

## 准备工作

- 安装[Maven](https://maven.apache.org/download.cgi)。

<!-- pulsar所在的maven库5月31日被官方关闭，还没找到迁移位置，找到后这里可以删掉-->
- 下载[pulsar-spark-connector_2.11](https://oss-cdn.nebula-graph.com.cn/jar-packages/pulsar-spark-connector_2.11.zip)，解压到本地Maven库的目录`io/streamnative/connectors`中。

## 编译Exchange

1. 在根目录克隆仓库`nebula-spark-utils`。

   ```bash
   git clone -b {{exchange.branch}} https://github.com/vesoft-inc/nebula-spark-utils.git
   ```

2. 切换到目录`nebula-exchange`。

   ```bash
   cd nebula-spark-utils/nebula-exchange
   ```

3. 打包Nebula Exchange。

   ```bash
   mvn clean package -Dmaven.test.skip=true -Dgpg.skip -Dmaven.javadoc.skip=true
   ```

编译成功后，用户可以在当前目录里查看到类似如下目录结构。

```text
.
├── README-CN.md
├── README.md
├── pom.xml
├── src
│   ├── main
│   └── test
└── target
    ├── classes
    ├── classes.timestamp
    ├── maven-archiver
    ├── nebula-exchange-2.x.y-javadoc.jar
    ├── nebula-exchange-2.x.y-sources.jar
    ├── nebula-exchange-2.x.y.jar
    ├── original-nebula-exchange-2.x.y.jar
    └── site
```

在`target`目录下，用户可以找到`exchange-2.x.y.jar`文件。

!!! note
    JAR文件版本号会因Nebula Java Client的发布版本而变化。用户可以在[Releases页面](https://github.com/vesoft-inc/nebula-java/releases)查看最新版本。

迁移数据时，用户可以参考配置文件[`target/classes/application.conf`](https://github.com/vesoft-inc/nebula-spark-utils/blob/master/nebula-exchange/src/main/resources/application.conf)。

## 下载依赖包失败

如果编译时下载依赖包失败：

- 检查网络设置，确认网络正常。

- 修改Maven安装目录下`libexec/conf/settings.xml`文件的`mirror`部分：

  ```text
  <mirror>
   <id>alimaven</id>
   <mirrorOf>central</mirrorOf>
   <name>aliyun maven</name>
   <url>http://maven.aliyun.com/nexus/content/repositories/central/</url>
  </mirror>
  ```
