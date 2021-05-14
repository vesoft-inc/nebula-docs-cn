# 编译 nebula-algorithm

## 前提条件

编译 nebula-algorithm 之前，必须先编译 [Nebula Spark Connector](../spark-connector/sc-ug-compile.md)。

## 操作步骤

切换到 `nebula-java/tools/nebula-algorithm` 目录，并编译打包 nebula-algorithm。

```bash
$ cd nebula-java/tools/nebula-algorithm
$ mvn clean package -Dgpg.skip -Dmaven.javadoc.skip=true -Dmaven.test.skip=true
```

编译成功后，用户可以在当前目录里看到如下目录结构。

```text
.
├── README.md
├── pom.xml
├── src
│   ├── main
│   └── test
└── target
    ├── classes
    ├── classes.682519136.timestamp
    ├── maven-archiver
    ├── maven-status
    ├── nebula-algorithm-1.x.y-tests.jar
    ├── nebula-algorithm-1.x.y.jar
    ├── original-nebula-algorithm-1.x.y.jar
    ├── test-classes
    └── test-classes.682519136.timestamp
```

在 `target` 目录下，用户可以看到 `nebula-algorithm-1.x.y.jar` 文件。

!!! Note

    JAR 文件版本号会因 Nebula Java Client 的发布版本而异。用户可以在 [nebula-java 仓库的 Releases 页面](https://github.com/vesoft-inc/nebula-java/releases "点击前往 GitHub 网站") 查看最新的 v1.x 版本。

## 后续操作

在使用 nebula-algorithm 时，用户可以参考 `target/classes/application.conf` 根据实际情况修改配置文件。详细信息请参考 [使用示例](na-ug-example.md)。
