# 编译 Nebula Spark Connector

逐行运行以下命令编译 Nebula Spark Connector。

```bash
$ git clone -b v1.0 https://github.com/vesoft-inc/nebula-java.git
$ cd nebula-java/tools/nebula-spark
$ mvn clean compile package install -Dgpg.skip -Dmaven.javadoc.skip=true
```

编译成功后，您可以在 `nebula-spark/target/` 目录下看到 `nebula-spark-1.x.y.jar` 文件，如下图所示。

> **说明**：JAR 文件版本号会因 Nebula Java Client 的发布版本而异。您可以在 [nebula-java 仓库的 Releases 页面](https://github.com/vesoft-inc/nebula-java/releases "点击前往 GitHub 网站") 查看最新的 v1.x 版本。

将这个文件复制到本地 Maven 库以下路径 `com/vesoft/nebula-spark/`。

```text
.
├── classes
│   ├── META-INF
│   │   └── services
│   └── com
│       └── vesoft
├── classes.-1151735588.timestamp
├── generated-sources
│   └── annotations
├── maven-archiver
│   └── pom.properties
├── maven-status
│   └── maven-compiler-plugin
│       └── compile
├── nebula-spark-1.x.y-tests.jar
├── nebula-spark-1.x.y.jar
└── original-nebula-spark-1.x.y.jar
```
