# 编译 Exchange

按以下步骤编译 Exchange v1.x：

1. 克隆 `nebula-java` 源代码。

   ```bash
   git clone -b v1.0 https://github.com/vesoft-inc/nebula-java.git
   ```

2. 切换到 `nebula-java` 目录，并打包 Nebula Java 1.x。

   ```bash
   cd nebula-java
   mvn clean install -Dgpg.skip -Dmaven.javadoc.skip=true -Dmaven.test.skip=true
   ```

3. 进入 `tools/exchange` 目录，并编译 Exchange v1.x。

   ```bash
   cd nebula-java/tools/exchange
   mvn clean package -Dgpg.skip -Dmaven.javadoc.skip=true -Dmaven.test.skip=true
   ```

编译成功后，您可以在当前目录里看到如下目录结构。

```
├── README.md
├── dependency-reduced-pom.xml
├── pom.xml
├── scripts
│   ├── README.md
│   ├── mock_data.py
│   ├── pulsar_producer.py
│   ├── requirements.txt
│   └── verify_nebula.py
├── src
│   └── main
└── target
    ├── classes
    ├── classes.timestamp
    ├── exchange-1.x.y-javadoc.jar
    ├── exchange-1.x.y-sources.jar
    ├── exchange-1.x.y.jar
    ├── generated-test-sources
    ├── maven-archiver
    ├── maven-status
    ├── original-exchange-1.x.y.jar
    ├── site
    ├── test-classes
    └── test-classes.timestamp
```

在 `target` 目录下，您可以看到 `exchange-1.x.y.jar` 文件。

> **说明**：JAR 文件版本号会因 Nebula Java Client 的发布版本而异。您可以在 [nebula-java 仓库的 Releases 页面](https://github.com/vesoft-inc/nebula-java/releases "点击前往 GitHub 网站") 查看最新的 v1.x 版本。

在迁移数据时，您可以参考 `target/classes/application.conf`、`target/classes/server_application.conf`、`target/classes/stream_application.conf` 根据实际情况修改配置文件。
