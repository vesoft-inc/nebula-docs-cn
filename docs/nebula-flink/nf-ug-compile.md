# 编译 Nebula Flink Connector

按以下步骤编译 Nebula Flink Connector v1.x：

1. 克隆 `nebula-java` 源代码。

   ```bash
   git clone -b v1.0 https://github.com/vesoft-inc/nebula-java.git
   ```

2. 切换到 `nebula-java` 目录，并打包 Nebula Java 1.x。

   ```bash
   cd nebula-java
   mvn clean install -Dgpg.skip -Dmaven.javadoc.skip=true -Dmaven.test.skip=true
   ```

3. 进入 `tools/nebula-flink` 目录，并编译 Nebula Flink Connector v1.x。

   ```bash
   cd nebula-java/tools/nebula-flink
   mvn clean package -Dgpg.skip -Dmaven.javadoc.skip=true -Dmaven.test.skip=true
   ```

编译成功后，您可以在当前目录里看到如下目录结构。

```text
.
├── README.md
├── pom.xml
├── src
│   ├── main
│   └── test
└── target
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
    └── test-classes
```

在 `target` 目录下，您可以看到 `nebula-flink-1.x.y.jar` 文件。

> **说明**：JAR 文件版本号会因 Nebula Java Client 的发布版本而异。您可以在 [nebula-java 仓库的 Releases 页面](https://github.com/vesoft-inc/nebula-java/releases "点击前往 GitHub 网站") 查看最新的 v1.x 版本。
