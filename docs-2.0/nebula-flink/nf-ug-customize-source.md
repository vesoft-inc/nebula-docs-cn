# 自定义 source (NebulaSource)

Nebula Flink Connector 支持以 `addSource` 或者 `createInput` 方式将 Nebula Graph 图数据库注册为 Flink 的数据源（source）。其中，通过 `addSource` 读取 source 数据得到的是 Flink 的 `DataStreamSource`，表示 DataStream 的起点，而通过 `createInput` 读取 source 数据得到的是 Flink 的 `DataSource`。`DataSource` 会作为进一步转换的数据集。`DataSource` 可以通过 `withParameters` 封装配置参数进行其他操作。

NebulaSource 的实现类图如下所示。

![Nebula Flink Connector 的 source 实现类图](https://docs-cdn.nebula-graph.com.cn/nebula-java-tools-docs/fl-ug-001.png "source 实现类图")

## `addSource`

`addSource` 方式通过 `NebulaSourceFunction` 类实现，该类继承自 `RichSourceFunction` 并实现了以下方法：

- `open`：准备 Nebula Graph 的连接信息，并获取 Nebula Graph 图数据库 Meta 服务和 Storage 服务的连接。
- `close`：在数据读取完成后释放资源，并断开与 Nebula Graph 图数据库服务的连接。
- `run`：开始读取数据，并将数据填充到 `sourceContext`。
- `cancel`：取消 Flink 作业时调用这个方法以关闭资源。

## `createInput`

`createInput` 方式通过 `NebulaInputFormat` 类实现，该类继承自 `RichInputFormat` 并实现了以下方法：

- `openInputFormat`：准备 `inputFormat` 以获取连接。
- `closeInputFormat`：数据读取完成后释放资源。断开与 Nebula Graph 图数据库服务的连接。
- `open`：开始 `inputFormat` 的数据读取，将读取的数据转换为 Flink 的数据格式，构造迭代器。
- `close`：在数据读取完成后打印读取日志。
- `reachedEnd`：判断是否读取完成。
- `nextRecord`：通过迭代器获取下一条数据。

## 应用实践

用户可以按以下步骤使用 Nebula Flink Connector 读取 Nebula Graph 的图数据：

1. 构造 `NebulaSourceFunction` 和 `NebulaOutputFormat`。
2. 通过 Flink 的 `addSource` 或者 `createInput` 方式将 Nebula Graph 注册为数据源。

在构造的 `NebulaSourceFunction` 和 `NebulaOutputFormat` 中，对客户端参数和执行参数作如下配置：

- `NebulaClientOptions` 需要配置：
  - Nebula Graph 图数据库 Meta 服务的 IP 地址及端口号。如果有多个服务，使用逗号分隔，例如 `“ip1:port1,ip2:port2"`。
  - Nebula Graph 图数据库的账号及其密码。
- `VertexExecutionOptions` 需要配置：
  - 需要读取点数据的 Nebula Graph 图数据库中的图空间名称。
  - 需要读取的 Tag（点类型）名称。一次只能一个 Tag。
  - 要读取的 Tag 属性。
  - 是否读取指定 Tag 的所有属性，默认为 `false`。如果配置为 `true` 则 Tag 属性的配置无效。
  - 单次读取的数据量限值，默认为 2000 个点数据。
- `EdgeExecutionOptions` 需要配置：
  - 需要读取边数据的 Nebula Graph 图数据库中的图空间名称。
  - 需要读取的 Edge type。一次只能一个 Edge type。
  - 需要读取的 Edge type 属性。
  - 是否读取指定 Edge type 的所有属性，默认为 `false`。如果配置为 `true` 则 Edge type 属性的配置无效。
  - 单次读取的数据量限值，默认值为 2000 个边数据。

假设需要读取点数据的 Nebula Graph 图数据库信息如下：

- Meta 服务为本地单副本部署，使用默认端口
- 图空间名称：`flinkSource`
- Tag：`player`
- Tag 属性：`name` 和 `age`
- 单次最多读取 100 个点数据

以下为自定义 NebulaSource 的代码示例。

```xml
// 构造 Nebula Graph 客户端连接需要的参数
NebulaClientOptions nebulaClientOptions = new NebulaClientOptions
                .NebulaClientOptionsBuilder()
                .setAddress("127.0.0.1:45500")
                .build();
// 创建 connectionProvider
NebulaConnectionProvider metaConnectionProvider = new NebulaMetaConnectionProvider(nebulaClientOptions);

// 构造读取 Nebula Graph 数据需要的参数
List<String> cols = Arrays.asList("name", "age");
VertexExecutionOptions sourceExecutionOptions = new VertexExecutionOptions.ExecutionOptionBuilder()
                .setGraphSpace("flinkSource")
                .setTag(tag)
                .setFields(cols)
                .setLimit(100)
                .builder();

// 构造 NebulaInputFormat
NebulaInputFormat inputFormat = new NebulaInputFormat(metaConnectionProvider)
                .setExecutionOptions(sourceExecutionOptions);

// 方式 1 使用 createInput 方式将 Nebula Graph 注册为数据源
DataSource<Row> dataSource1 = ExecutionEnvironment.getExecutionEnvironment()
         .createInput(inputFormat);

// 方式 2 使用 addSource 方式将 Nebula Graph 注册为数据源
NebulaSourceFunction sourceFunction = new NebulaSourceFunction(metaConnectionProvider)
                .setExecutionOptions(sourceExecutionOptions);
 DataStreamSource<Row> dataSource2 = StreamExecutionEnvironment.getExecutionEnvironment()
         .addSource(sourceFunction);
```

## 示例程序

用户可以参考 GitHub 上的示例程序 [testNebulaSource](https://github.com/vesoft-inc/nebula-java/tree/v1.0/examples/src/main/java/org/apache/flink/FlinkDemo.java) 编写自己的 Flink 应用程序。

以 testNebulaSource 为例：该程序以 Nebula Graph 图数据库为 source，以 Print 为 sink，从 Nebula Graph 图数据库中读取 59,671,064 条点数据后再打印。将该程序打包提交到 Flink 集群执行，结果如下图所示。

![Flink Dashboard 上显示的 testNebulaSource 执行结果](https://docs-cdn.nebula-graph.com.cn/nebula-java-tools-docs/fl-ug-002.png "testNebulaSource 执行结果")

由上图可知，source 发送数据 59,671,064 条，sink 接收数据 59,671,064 条。
