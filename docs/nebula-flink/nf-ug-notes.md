
# 特殊说明

## Catalog

Flink 1.11.0 之前，如果依赖 Flink 的 source/sink 读写外部数据源时，用户必须手动读取对应数据系统的 Schema（模式）。例如，如果要读写 Nebula Graph 的数据，则必须先保证明确地知晓 Nebula Graph 中的 Schema 信息。由此带来的问题是：当 Nebula Graph 中的 Schema 发生变化时，用户需要手动更新对应的 Flink 任务以保持类型匹配，否则，任何不匹配都会造成运行时报错使作业失败，整个操作冗余且繁琐，体验极差。

Flink 1.11.0 版本后，用户使用 Flink SQL 时可以自动获取表的  Schema 而不再需要输入 DDL，即 Flink 在不了解外部系统数据的 Schema 时仍能完成数据匹配。

目前 Nebula Flink Connector 已经支持数据的读写，要实现 Schema 的匹配则需要为 Flink Connector 实现 Catalog 管理。但是，为了确保 Nebula Graph 中的数据安全，Nebula Flink Connector 仅支持 Catalog 的读操作，不允许进行 Catalog 的修改和写入。

访问 Nebula Graph 指定类型的数据时，完整路径格式如下：`<graphSpace>.<VERTEX.tag>` 或者 `<graphSpace>.<EDGE.edge>`。

具体使用方式如下：

```java
// 其中 address 可以配置为多个 IP 地址，格式为 "ip1:port,ip2:port"
String catalogName  = "testCatalog";
String defaultSpace = "flinkSink";
String username     = "root";
String password     = "nebula";
String address      = "127.0.0.1:45500";
String table        = "VERTEX.player"

// define Nebula catalog
Catalog catalog = NebulaCatalogUtils.createNebulaCatalog(catalogName, defaultSpace, address, username, password);
// define Flink table environment
StreamExecutionEnvironment bsEnv = StreamExecutionEnvironment.getExecutionEnvironment();
tEnv = StreamTableEnvironment.create(bsEnv);
// register customed nebula catalog
tEnv.registerCatalog(catalogName, catalog);
// use customed nebula catalog
tEnv.useCatalog(catalogName);

// show graph spaces of nebula
String[] spaces = tEnv.listDatabases();

// // show tags and edges of Nebula Graph
tEnv.useDatabase(defaultSpace);
String[] tables = tEnv.listTables();

// check tage player exist in defaultSpace
ObjectPath path = new ObjectPath(defaultSpace, table);
assert catalog.tableExists(path) == true

// get nebula tag schema
CatalogBaseTable table = catalog.getTable(new ObjectPath(defaultSpace, table));
table.getSchema();
```

关于 Catalog 接口的详细信息，参考 [Flink-table 代码](https://github.com/apache/flink/blob/master/flink-table/flink-table-common/src/main/java/org/apache/flink/table/catalog/Catalog.java)。

## Exactly-once

Flink Connector 的 Exactly-once 是指 Flink 借助 checkpoint 机制保证每个输入事件只对最终结果影响一次，在数据处理过程中即使出现故障，也不会出现数据重复和丢失的情况。

为了提供端到端的 Exactly-once 语义，Flink 的外部数据系统也必须提供提交或回滚的方法，然后通过 Flink 的 checkpoint 机制协调。Flink 提供了实现端到端的 Exactly-once 的抽象，即实现二阶段提交的抽象类 `TwoPhaseCommitSinkFunction`。

要为数据输出端实现 Exactly-once，需要实现四个函数：

- `beginTransaction`：在事务开始前，在目标文件系统的临时目录中创建一个临时文件，随后可以在数据处理时将数据写入此文件。

- `preCommit`：预提交阶段。在这个阶段，刷新文件到存储，关闭文件不再写入。为下一个 checkpoint 的任何后续文件写入启动一个新事务。

- `commit`：提交阶段。在这个阶段，将预提交阶段的文件原子地移动到真正的目标目录。二阶段提交过程会增加输出数据可见性的延迟。

- `abort`：终止阶段。在这个阶段，删除临时文件。

由以上函数可看出，Flink 的二阶段提交对外部数据源有要求，即 source 数据源必须具备重发功能，sink 数据池必须支持事务提交和幂等写。

Nebula Graph v1.1.0 虽然不支持事务，但其写入操作是幂等的，即同一条数据的多次写入结果是一致的。因此可以通过 checkpoint 机制实现 Nebula Flink Connector 的 At-least-Once 机制，根据多次写入的幂等性可以间接实现 sink 的 Exactly-once。

要使用 NebulaSink 的容错性，请确保在 Flink 的执行环境中开启了 checkpoint 配置，代码如下所示。

```java
StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
env.enableCheckpointing(10000) // checkpoint every 10000 msecs
   .getCheckpointConfig()
   .setCheckpointingMode(CheckpointingMode.AT_LEAST_ONCE);
```
