# NebulaGraph Importer

NebulaGraph Importer（简称 Importer）是一款{{nebula.name}}的 CSV 文件单机导入工具，可以读取并导入多种数据源的 CSV 文件数据。

## 功能

- 支持多种数据源，包括本地、S3、OSS、HDFS、FTP、SFTP。
- 支持导入 CSV 格式文件的数据。单个文件内可以包含多种 Tag、多种 Edge type 或者二者混合的数据。
- 支持同时连接多个 Graph 服务进行导入并且动态负载均衡。
- 支持失败后重连、重试。
- 支持多维度显示统计信息，包括导入时间、导入百分比等。统计信息支持打印在 Console 或日志中。

## 优势

- 轻量快捷：不需要复杂环境即可使用，快速导入数据。

- 灵活筛选：通过配置文件可以实现对 CSV 文件数据的灵活筛选。

## 版本兼容性

NebulaGraph Importer 版本和{{nebula.name}}内核的版本对应关系如下。

|{{nebula.name}}版本|NebulaGraph Importer 版本|
|:---|:---|
| 3.x.x      |  3.x.x、4.x.x        | 
| 2.x.x      |  2.x.x、3.x.x        |

!!! note

    Importer 4.0.0 对 Importer 进行了重做，性能得到了提高，但配置文件不兼容旧版本。建议使用新版 Importer。

## 更新说明

[Release notes](https://github.com/vesoft-inc/nebula-importer/releases/tag/{{importer.tag}})

## 前提条件

在使用 NebulaGraph Importer 之前，请确保：

- 已部署{{nebula.name}}服务。部署方式如下：
  
  - [RPM/DEB 包安装](../4.deployment-and-installation/2.compile-and-install-nebula-graph/2.install-nebula-graph-by-rpm-or-deb.md)
    {{comm.comm_begin}}  
  - [Docker Compose 部署](../2.quick-start/1.quick-start-overview.md)
  
  - [源码编译安装](../4.deployment-and-installation/2.compile-and-install-nebula-graph/1.install-nebula-graph-by-compiling-the-source-code.md)
    {{comm.comm_end}}
- {{nebula.name}}中已创建 Schema，包括图空间、Tag 和 Edge type，或者通过参数`manager.hooks.before.statements`设置。

## 操作步骤

### 创建 CSV 文件

准备好待导入的 CSV 文件并配置 YAML 文件，即可使用本工具向{{nebula.name}}批量导入数据。

!!! note

    YAML 配置文件说明请参见下文的[配置文件说明](#_8)。

### 下载二进制包运行

1. 在 [Release](https://github.com/vesoft-inc/nebula-importer/releases/tag/{{importer.tag}}) 页面下载和安装二进制包，并添加执行权限。

  !!! note
        使用 RPM/DEB 包安装的文件路径为`/usr/bin/nebula-importer`。

2. 在`nebula-importer`的安装目录下，执行以下命令导入数据。

  ```bash
  $ ./<binary_file_name> --config <yaml_config_file_path>
  ```

### 源码编译运行

编译源码需要部署 Golang 环境。详情请参见 [Golang 环境搭建](https://github.com/vesoft-inc/nebula-importer/blob/{{importer.branch}}/docs/golang-install.md)。

1. 克隆仓库。

  ```bash
  $ git clone -b {{importer.branch}} https://github.com/vesoft-inc/nebula-importer.git
  ```

  !!! note
  
        请使用正确的分支。不同分支的 rpc 协议不同。

2. 进入目录`nebula-importer`。

  ```bash
  $ cd nebula-importer
  ```

3. 编译源码。

  ```bash
  $ make build
  ```

4. 开始导入数据。

  ```bash
  $ ./bin/nebula-importer --config <yaml_config_file_path>
  ```

### Docker 方式运行

使用 Docker 可以不必在本地安装 Go 语言环境，只需要拉取 NebulaGraph Importer 的[镜像](https://hub.docker.com/r/vesoft/nebula-importer)，并将本地配置文件和 CSV 数据文件挂载到容器中。命令如下：

```bash
$ docker pull vesoft/nebula-importer:<version>
$ docker run --rm -ti \
      --network=host \
      -v <config_file>:<config_file> \
      -v <data_dir>:<data_dir> \
      vesoft/nebula-importer:<version> \
      --config <config_file>
```

- `<config_file>`：填写 YAML 配置文件的绝对路径。
- `<data_dir>`：填写 CSV 数据文件的绝对路径。如果文件不在本地，请忽略该参数。
- `<version>`：填写 Importer 的版本号，请填写`v4`。

!!! note
    建议使用相对路径。如果使用本地绝对路径，请检查路径映射到 Docker 中的路径。

例如：

```bash
$ docker pull vesoft/nebula-importer:v4
$ docker run --rm -ti \
      --network=host \
      -v /home/user/config.yaml:/home/user/config.yaml \
      -v /home/user/data:/home/user/data \
      vesoft/nebula-importer:v4 \
      --config /home/user/config.yaml
```

## 配置文件说明

NebulaGraph Importer 的 [Github](https://github.com/vesoft-inc/nebula-importer/tree/{{importer.branch}}/examples) 内提供多种示例配置文件。配置文件用来描述待导入文件信息、{{nebula.name}}服务器信息等。下文将分类介绍配置文件内的字段。

!!! note

    如果用户下载的是二进制包，请手动创建配置文件。

### Client 配置

Client 配置存储客户端连接{{nebula.name}}相关的配置。

示例配置如下：

```yaml
client:
  version: v3
  address: "192.168.1.100:9669,192.168.1.101:9669"
  user: root
  password: nebula
  concurrencyPerAddress: 10
  reconnectInitialInterval: 1s
  retry: 3
  retryInitialInterval: 1s
```

|参数|默认值|是否必须|说明|
|:---|:---|:---|:---|
|`client.version`|`v3`|是|指定连接的{{nebula.name}}的大版本。当前仅支持`v3`。|
|`client.address`|`"127.0.0.1:9669"`|是|指定连接的{{nebula.name}}地址。多个地址用英文逗号（,）分隔。|
|`client.user`|`root`|否|{{nebula.name}}的用户名。|
|`client.password`|`nebula`|否|{{nebula.name}}用户名对应的密码。|
|`client.concurrencyPerAddress`|`10`|否|单个 Graph 服务的客户端并发连接数。|
|`client.retryInitialInterval`|`1s`|否|重连间隔时间。|
|`client.retry`|`3`|否|nGQL 语句执行失败的重试次数。|
|`client.retryInitialInterval`|`1s`|否|重试间隔时间。|

### Manager 配置

Manager 配置是连接数据库后的人为控制配置。

示例配置如下：

```yaml
manager:
  spaceName: basic_string_examples
  batch: 128
  readerConcurrency: 50
  importerConcurrency: 512
  statsInterval: 10s
  hooks:
    before:
      - statements:
        - |
            DROP SPACE IF EXISTS basic_string_examples;
            CREATE SPACE IF NOT EXISTS basic_string_examples(partition_num=5, replica_factor=1, vid_type=int);
            USE basic_string_examples;
        wait: 10s
    after:
      - statements:
          - |
            SHOW SPACES;
```

|参数|默认值|是否必须|说明|
|:---|:---|:---|:---|
|`manager.spaceName`|-|是|指定数据要导入的图空间。不支持同时导入多个图空间。|
|`manager.batch`|`128`|否|执行语句的批处理量（全局配置）。</br>对某个数据源单独设置批处理量可以使用下文的`sources.batch`。|
|`manager.readerConcurrency`|`50`|否|读取器读取数据源的并发数。|
|`manager.importerConcurrency`|`512`|否|生成待执行的 nGQL 语句的并发数，然后会调用客户端执行这些语句。|
|`manager.statsInterval`|`10s`|否|打印统计信息的时间间隔。|
|`manager.hooks.before.[].statements`|-|否|导入前在图空间内执行的命令。|
|`manager.hooks.before.[].wait`|-|否|执行`statements`语句后的等待时间。|
|`manager.hooks.after.[].statements`|-|否|导入后在图空间内执行的命令。|
|`manager.hooks.after.[].wait`|-|否|执行`statements`语句后的等待时间。|

### Log 配置

Log 配置是设置日志相关配置。

示例配置如下：

```yaml
log:
  level: INFO
  console: true
  files:
   - logs/nebula-importer.log   
```

|参数|默认值|是否必须|说明|
|:---|:---|:---|:---|
|`log.level`|`INFO`|否|日志级别。可选值为`DEBUG`、`INFO`、`WARN`、`ERROR`、`PANIC`、`FATAL`。|
|`log.console`|`true`|否|存储日志时是否将日志同步打印到 Console。|
|`log.files`|-|否|日志文件路径。需手动创建日志文件目录。|

### Source 配置

Source 配置中需要配置数据源信息、数据处理方式和 Schema 映射。

示例配置如下：

```yaml
sources:
  - path: ./person.csv  # 指定存储数据文件的路径。如果使用相对路径，则路径和当前配置文件目录拼接。也支持通配符文件名，例如：./follower-*.csv，请确保所有匹配的文件具有相同的架构。
#  - s3: # AWS S3
#      endpoint: endpoint    # 可选。S3 服务端点，如果使用 AWS S3 可以省略。
#      region: us-east-1     # 必填。S3 服务的区域。
#      bucket: gdelt-open-data    # 必填。S3 服务中的 bucket。
#      key: events/20190918.export.csv     # 必填。S3 服务中文件的 key。
#      accessKeyID: ""    # 可选。S3 服务的访问密钥。如果是公共数据，则无需配置。
#      accessKeySecret: ""     # 可选。S3 服务的密钥。如果是公共数据，则无需配置。
#  - oss:
#      endpoint: https://oss-cn-hangzhou.aliyuncs.com    # 必填。OSS 服务端点。
#      bucket: bucketName    # 必填。OSS 服务中的 bucket。
#      key: objectKey    # 必填。OSS 服务中文件的 object key。
#      accessKeyID: accessKey    # 必填。OSS 服务的访问密钥。
#      accessKeySecret: secretKey    # 必填。OSS 服务的秘钥。
#  - ftp:
#      host: 192.168.0.10    # 必填。FTP 服务的主机。
#      port: 21    # 必填。FTP 服务的端口。
#      user: user    # 必填。FTP 服务的用户名。
#      password: password    # 必填。FTP 服务的密码。
#      path: "/events/20190918.export.csv"    # FTP 服务中文件的路径。
#  - sftp:
#      host: 192.168.0.10    # 必填。SFTP 服务的主机。
#      port: 22    # 必填。SFTP 服务的端口。
#      user: user    # 必填。SFTP 服务的用户名。
#      password: password    # 可选。SFTP 服务的密码。
#      keyFile: keyFile    # 可选。SFTP 服务的 SSH 密钥文件路径。
#      keyData: keyData    $ 可选。SFTP 服务的 SSH 密钥文件内容。
#      passphrase: passphrase    # 可选。SFTP 服务的 SSH 密钥密码。
#      path: "/events/20190918.export.csv"    # 必填。SFTP 服务中文件的路径。
#  - hdfs:
#      address: "127.0.0.1:8020"    # 必填。HDFS 服务的地址。
#      user: "hdfs"    # 可选。HDFS 服务的用户名。
#      path: "/events/20190918.export.csv"    # 必填。HDFS 服务中文件的路径。
    batch: 256
    csv:
      delimiter: "|"
      withHeader: false
      lazyQuotes: false
    tags:
    - name: Person
      id:
        type: "STRING"
        function: "hash"
#       index: 0        
        concatItems:
          - person_
          - 0
          - _id
      props:
        - name: "firstName"
          type: "STRING"
          index: 1
        - name: "lastName"
          type: "STRING"
          index: 2
        - name: "gender"
          type: "STRING"
          index: 3
          nullable: true
          defaultValue: female
        - name: "birthday"
          type: "DATE"
          index: 4
          nullable: true
          nullValue: _NULL_
        - name: "creationDate"
          type: "DATETIME"
          index: 5
        - name: "locationIP"
          type: "STRING"
          index: 6
        - name: "browserUsed"
          type: "STRING"
          index: 7
  - path: ./knows.csv
    batch: 256
    edges:
    - name: KNOWS # person_knows_person
      src:
        id:
          type: "STRING"
          concatItems:
            - person_
            - 0
            - _id
      dst:
        id:
          type: "STRING"
          concatItems:
            - person_
            - 1
            - _id
      props:
        - name: "creationDate"
          type: "DATETIME"
          index: 2
          nullable: true
          nullValue: _NULL_
          defaultValue: 0000-00-00T00:00:00
```

配置主要包括以下几个部分：

- 指定数据源信息。
- 指定执行语句的批处理量。
- 指定 CSV 文件格式信息。
- 指定 Tag 的模式映射。
- 指定 Edge type 的模式映射。

|参数|默认值|是否必须|说明|
|:---|:---|:---|:---|
|`sources.path`</br>`sources.s3`</br>`sources.oss`</br>`sources.ftp`</br>`sources.sftp`</br>`sources.hdfs`   |-| 否 | 指定数据源信息，例如本地文件、HDFS、S3 等。一个`source`只能配置一种数据源，配置多个数据源请在多个`source`内配置。</br>不同数据源的配置项说明请参见示例内的注释。         |  
|`sources.batch`   |`256`| 否 | 导入该数据源时执行语句的批处理量。优先级高于`manager.batch`。          |  
|`sources.csv.delimiter`   |`,`| 否 |  CSV 文件的分隔符。仅支持 1 个字符的字符串分隔符。使用特殊字符做分隔符时需要进行转义。例如当分隔符为十六进制`0x03`即`Ctrl+C`时，转义的写法为：`"\x03"`或`"\u0003"`。关于 yaml 格式特殊字符转义的细节请参见[Escaped Characters](https://yaml.org/spec/1.2.2/#escaped-characters)。|         |  
|`sources.csv.withHeader`   |`false`| 否 | 是否忽略 CSV 文件中的第一条记录。         |  
|`sources.csv.lazyQuotes`   |`false`| 否 | 是否允许惰性解析引号。如果值为`true`，引号可以出现在非引号字段中，非双引号可以出现在引号字段中，而不会引发解析错误。    |  
|`sources.tags.name`   |-| 是 | Tag 名称。         |  
|`sources.tags.id.type`   |`STRING`| 否 |  VID 的类型。        |  
|`sources.tags.id.function`   |-| 否 | 生成 VID 的函数。目前仅支持`hash`。         |  
|`sources.tags.id.index`   |-| 否 | VID 对应的数据文件中的列号。如果未配置`sources.tags.id.concatItems`，该参数必须配置。         |  
|`sources.tags.id.concatItems`   |-| 否 | 用于连接两个或多个数组，连接项可以是`string`、`int`或者混合。`string`代表常量，`int`表示索引列。如果设置了该参数，`sources.tags.id.index`参数将不生效。  |  
|`sources.tags.ignoreExistedIndex`   |`true`| 否 | 是否启用`IGNORE_EXISTED_INDEX`，即插入点后不更新索引。         |  
|`sources.tags.props.name`   |-| 是 | VID 上的属性名称，必须与数据库中的属性相同。         |  
|`sources.tags.props.type`   |`STRING`| 否 | VID 上属性的数据类型。目前支持`BOOL`、`INT`、`FLOAT`、`DOUBLE`、`STRING`、`TIME`、`TIMESTAMP`、`DATE`、`DATETIME`、`GEOGRAPHY`、`GEOGRAPHY(POINT)`、`GEOGRAPHY(LINESTRING)`、`GEOGRAPHY(POLYGON)`。    |  
|`sources.tags.props.index`   |-| 是 | 属性值对应的数据文件中的列号。         |  
|`sources.tags.props.nullable`   |`false`| 否 | 属性是否可以为`NULL`，可选`true`或者`false`。         |  
|`sources.tags.props.nullValue`   |-| 否 | `nullable`设置为`true`时，属性的值与`nullValue`相等则将该属性值设置为`NULL`。         |  
|`sources.tags.props.alternativeIndices`   |-| 否 | 当`nullable`为`false`时忽略。该属性根据索引顺序从文件中获取，直到不等于`nullValue`。         |  
|`sources.tags.props.defaultValue`   |-| 否 | 当`nullable`为`false`时忽略。根据`index`和`alternativeIndices`获取的所有值为`nullValue`时设置默认值。         |  
|`sources.edges.name`   |-| 是 | Edge type 名称。          |  
|`sources.edges.src.id.type`   |`STRING`| 否 |  边上起点 VID 的数据类型。        |  
|`sources.edges.src.id.index`   |-| 是 | 边上起点 VID 对应的数据文件中的列号。         |  
|`sources.edges.dst.id.type`   |`STRING`| 否 | 边上终点 VID 的数据类型。         |  
|`sources.edges.dst.id.index`   |-| 是 | 边上终点 VID 对应的数据文件中的列号。         |  
|`sources.edges.rank.index`   |-| 否 | 边上 RANK 对应的数据文件中的列号。         |  
|`sources.edges.ignoreExistedIndex`   |`true`| 否 | 是否启用`IGNORE_EXISTED_INDEX`，即插入点后不更新索引。         |  
|`sources.edges.props.name`   |-| 否 | 边上属性的名称，必须与数据库中的属性相同。         |  
|`sources.edges.props.type`   |`STRING`| 否 | 边上属性的数据类型。目前支持`BOOL`、`INT`、`FLOAT`、`DOUBLE`、`STRING`、`TIME`、`TIMESTAMP`、`DATE`、`DATETIME`、`GEOGRAPHY`、`GEOGRAPHY(POINT)`、`GEOGRAPHY(LINESTRING)`、`GEOGRAPHY(POLYGON)`。         |  
|`sources.edges.props.index`   |-| 否 | 属性值对应的数据文件中的列号。         |  
|`sources.edges.props.nullable`   |-| 否 | 属性是否可以为`NULL`，可选`true`或者`false`。         |  
|`sources.edges.props.nullValue`   |-| 否 | `nullable`设置为`true`时，属性的值与`nullValue`相等则将该属性值设置为`NULL`。         |  
|`sources.edges.props.defaultValue`   |-| 否 | 当`nullable`为`false`时忽略。根据`index`和`alternativeIndices`获取的所有值为`nullValue`时设置默认值。         |  

!!! note

    CSV 文件中列的序号从 0 开始，即第一列的序号为 0，第二列的序号为 1。
