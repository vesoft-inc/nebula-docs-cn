# 编译 Nebula Flink Connector

逐行运行以下命令编译 Nebula Flink Connector。

```bash
$ git clone -b v1.0 https://github.com/vesoft-inc/nebula-java.git
$ cd nebula-java/tools/nebula-flink
$ mvn clean compile package install -Dgpg.skip -Dmaven.javadoc.skip=true
```

编译成功后，您可以在 `nebula-flink/target/` 目录下看到 `nebula-flink-1.x.y.jar` 文件，如下所示。将这个文件复制到本地 Maven 库的 `com/vesoft/nebula-flink/` 目录中。

> **说明**：JAR 文件版本号会因 Nebula Java Client 的发布版本而异。您可以在 [nebula-java 仓库的 Releases 页面](https://github.com/vesoft-inc/nebula-java/releases "点击前往 GitHub 网站") 查看最新的 v1.x 版本。

```text
.
├── classes
├── generated-sources
├── generated-test-sources
├── maven-archiver
├── maven-status
├── nebula-flink-1.x.y-sources.jar
├── nebula-flink-1.x.y-test-sources.jar
├── nebula-flink-1.x.y-tests.jar
├── nebula-flink-1.x.y.jar
├── original-nebula-flink-1.x.y.jar
├── surefire-reports
└── test-classes
```
