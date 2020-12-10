# 编译 nebula-algorithm

## 前提条件

编译 nebula-algorithm 之前，必须先编译 [Nebula Spark Connector](../spark-connector/sc-ug-compile.md)。

## 操作步骤

依次运行以下命令下载并编译打包 nebula-algorithm。

```shell
$ git clone -b v1.0 https://github.com/vesoft-inc/nebula-java.git
$ cd nebula-java/tools/nebula-algorithm
$ mvn package -DskipTests
```

编译成功后，您可以在当前目录里看到如下目录结构。

```text
nebula-java
    ├── pom.xml
    ├── src
    │   ├── main
    │   └── test
    └── target
        ├── classes
        ├── classes.1846592514.timestamp
        ├── maven-archiver
        ├── maven-status
        ├── nebula-algorithm-1.x.y-tests.jar
        ├── nebula-algorithm-1.x.y.jar
        ├── original-nebula-algorithm-1.x.y.jar
        ├── test-classes
        └── test-classes.1846592514.timestamp
```

在 `target` 目录下，您可以看到 `nebula-algorithm-1.x.y.jar` 文件。
> **说明**：JAR 文件版本号会因 Nebula Java Client 的发布版本而异。您可以在 [nebula-java 仓库的 Releases 页面](https://github.com/vesoft-inc/nebula-java/releases "点击前往 GitHub 网站") 查看最新的 v1.x 版本。

## 后续操作

在使用 nebula-algorithm 时，您可以参考 `target/classes/application.conf` 根据实际情况修改配置文件。详细信息请参考 [使用示例](na-ug-example.md)。
