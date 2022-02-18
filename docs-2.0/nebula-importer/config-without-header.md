# 无表头配置说明

对于无表头（header）的 CSV 文件，需要在配置文件里设置`withHeader`为`false`，表示 CSV 文件中只含有数据（不含第一行表头），同时可能还需要设置数据类型、对应的列等。

## 示例文件

无表头的 CSV 文件示例如下：

- 点示例

  `student_without_header.csv`的示例数据：

  ```csv
  student100,Monica,16,female
  student101,Mike,18,male
  student102,Jane,17,female
  ```

  第一列为点 ID，后面三列为属性`name`、`age`和`gender`。

- 边示例

  `follow_without_header.csv`的示例数据：

  ```csv
  student100,student101,0,92.5
  student101,student100,1,85.6
  student101,student102,2,93.2
  student100,student102,1,96.2
  ```

  前两列的数据分别为起始点 ID 和目的点 ID，第三列为 rank，第四列为属性`degree`。

## 配置示例

```yaml
# 连接的 Nebula Graph 版本，连接 3.x 时设置为 v3。
version: v3

description: example

# 是否删除临时生成的日志和错误数据文件。
removeTempFiles: false

clientSettings:

  # nGQL 语句执行失败的重试次数。
  retry: 3

  # Nebula Graph 客户端并发数。
  concurrency: 10 

  # 每个 Nebula Graph 客户端的缓存队列大小。
  channelBufferSize: 128

  # 指定数据要导入的 Nebula Graph 图空间。
  space: student

  # 连接信息。
  connection:
    user: root
    password: nebula
    address: 192.168.11.13:9669

  postStart:
    # 配置连接 Nebula Graph 服务器之后，在插入数据之前执行的一些操作。
    commands: |
      DROP SPACE IF EXISTS student;
      CREATE SPACE IF NOT EXISTS student(partition_num=5, replica_factor=1, vid_type=FIXED_STRING(20));
      USE student;
      CREATE TAG student(name string, age int,gender string);
      CREATE EDGE follow(degree int);

    # 执行上述命令后到执行插入数据命令之间的间隔。
    afterPeriod: 15s
  
  preStop:
    # 配置断开 Nebula Graph 服务器连接之前执行的一些操作。
    commands: |

# 错误等日志信息输出的文件路径。    
logPath: ./err/test.log

# CSV 文件相关设置。
files:
  
    # 数据文件的存放路径，如果使用相对路径，则会将路径和当前配置文件的目录拼接。本示例第一个数据文件为点的数据。
  - path: ./student_without_header.csv

    # 插入失败的数据文件存放路径，以便后面补写数据。
    failDataPath: ./err/studenterr.csv

    # 单批次插入数据的语句数量。
    batchSize: 10

    # 读取数据的行数限制。
    limit: 10

    # 是否按顺序在文件中插入数据行。如果为 false，可以避免数据倾斜导致的导入速率降低。
    inOrder: true

    # 文件类型，当前仅支持 csv。
    type: csv

    csv:
      # 是否有表头。
      withHeader: false

      # 是否有 LABEL。
      withLabel: false

      # 指定 csv 文件的分隔符。只支持一个字符的字符串分隔符。
      delimiter: ","

    schema:
      # Schema 的类型，可选值为 vertex 和 edge。
      type: vertex

      vertex:
        
        # 点 ID 设置。
        vid:
           # 点 ID 对应 CSV 文件中列的序号。CSV 文件中列的序号从 0 开始。
           index: 0

           # 点 ID 的数据类型，可选值为 int 和 string，分别对应 Nebula Graph 中的 INT64 和 FIXED_STRING。
           type: string

        # Tag 设置。   
        tags:
            # Tag 名称。
          - name: student
           
            # Tag 内的属性设置。
            props:
                # 属性名称。
              - name: name
                
                # 属性数据类型。
                type: string

                # 属性对应 CSV 文件中列的序号。
                index: 1

              - name: age
                type: int
                index: 2
              - name: gender
                type: string
                index: 3

    # 本示例第二个数据文件为边的数据。
  - path: ./follow_without_header.csv
    failDataPath: ./err/followerr.csv
    batchSize: 10
    limit: 10
    inOrder: true
    type: csv
    csv:
      withHeader: false
      withLabel: false
    schema:
      # Schema 的类型为 edge。
      type: edge
      edge:
        # Edge type 名称。
        name: follow

        # 是否包含 rank。
        withRanking: true

        # 起始点 ID 设置。
        srcVID:
           # 数据类型。
           type: string

           # 起始点 ID 对应 CSV 文件中列的序号。
           index: 0

        # 目的点 ID 设置。
        dstVID:
           type: string
           index: 1

        # rank 设置。
        rank:
           # rank 值对应 CSV 文件中列的序号。如果没有设置 index，请务必在第三列设置 rank 的值。之后的列依次设置各属性。
           index: 2
        
        # Edge type 内的属性设置。
        props:
             # 属性名称。
           - name: degree
             
             # 属性数据类型。
             type: double

             # 属性对应 CSV 文件中列的序号。
             index: 3
```

!!! Note

    - CSV 文件中列的序号从 0 开始，即第一列的序号为 0，第二列的序号为 1。

    - 点 ID 的数据类型需要和`clientSettings.postStart.commands`中的创建图空间语句的数据类型一致。

    - 如果没有设置 index 字段指定列的序号，CSV 文件必须遵守如下规则：

      + 在点数据文件中，第一列必须为点 ID，后面的列为属性，且需要和配置文件内的顺序一一对应。

      + 在边数据文件中，第一列必须为起始点 ID，第二列必须为目的点 ID，如果`withRanking`为`true`，第三列必须为 rank 值，后面的列为属性，且需要和配置文件内的顺序一一对应。
