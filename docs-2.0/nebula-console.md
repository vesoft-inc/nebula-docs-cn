# Nebula Console

Nebula Console 是 Nebula Graph 的原生命令行客户端，用于连接 Nebula Graph 集群并执行查询，同时支持管理参数、导出命令的执行结果、导入测试数据集等。

使用 Nebula Console 连接 Nebula Graph 请参见[步骤 3：连接 Nebula Graph](2.quick-start/3.connect-to-nebula-graph.md)。

!!! note

    命令不区分大小写。

## 管理参数

可以保存参数，用于参数化查询。

!!! note

    - VID 不支持参数化查询。

    - `SAMPLE`子句中不支持参数化查询。

    - 会话释放后，参数不会保留。

- 保存参数命令如下：

  ```ngql
  nebula> :param <param_name> => <param_value>;
  ```

  示例：

  ```ngql
  nebula> :param p1 => "Tim Duncan";
  nebula> MATCH (v:player{name:$p1})-[:follow]->(n)  RETURN v,n;
  +----------------------------------------------------+-------------------------------------------------------+
  | v                                                  | n                                                     |
  +----------------------------------------------------+-------------------------------------------------------+
  | ("player100" :player{age: 42, name: "Tim Duncan"}) | ("player125" :player{age: 41, name: "Manu Ginobili"}) |
  | ("player100" :player{age: 42, name: "Tim Duncan"}) | ("player101" :player{age: 36, name: "Tony Parker"})   |
  +----------------------------------------------------+-------------------------------------------------------+

  nebula> :param p2 => {"a":3,"b":false,"c":"Tim Duncan"};
  nebula> RETURN $p2.b AS b;
  +-------+
  | b     |
  +-------+
  | false |
  +-------+
  ```

- 查看当前保存的所有参数，命令如下：

  ```ngql
  nebula> :params;
  ```

- 查看指定参数，命令如下：

  ```ngql
  nebula> :params <param_name>;
  ```

- 删除指定参数，命令如下：

  ```ngql
  nebula> :param <param_name> =>;
  ```

## 导出执行结果

导出命令执行的返回结果，可以保存为 CSV 文件或 DOT 文件。

!!! note

    - 文件保存在当前工作目录中，即 Linux 命令`pwd`显示的目录。

    - 命令只对下一条查询语句生效。

    - DOT 文件的内容可以复制后在 [GraphvizOnline](https://dreampuf.github.io/GraphvizOnline/) 网页中粘贴，生成可视化的执行计划图。

- 导出 CSV 文件命令如下：

  ```ngql
  nebula> :CSV <file_name.csv>;
  ```

- 导出 DOT 文件命令如下：

  ```ngql
  nebula> :dot <file_name.dot>;
  ```

  示例：

  ```ngql
  nebula> :dot a.dot;
  nebula> PROFILE FORMAT="dot" GO FROM "player100" OVER follow;
  ```

## 加载测试数据集

测试数据集名称为 basketballplayer，详细 Schema 信息和数据信息请使用相关`SHOW`命令查看。

加载测试数据集命令如下：

```ngql
nebula> :play basketballplayer;
```

## 重复执行

重复执行下一个命令 N 次，然后打印平均执行时间。命令如下：

```ngql
nebula> :repeat N;
```

示例：

```ngql
nebula> :repeat 3;
nebula> GO FROM "player100" OVER follow YIELD dst(edge);
+-------------+
| dst(EDGE)   |
+-------------+
| "player101" |
| "player125" |
+-------------+
Got 2 rows (time spent 2602/3214 us)

Fri, 20 Aug 2021 06:36:05 UTC

+-------------+
| dst(EDGE)   |
+-------------+
| "player101" |
| "player125" |
+-------------+
Got 2 rows (time spent 583/849 us)

Fri, 20 Aug 2021 06:36:05 UTC

+-------------+
| dst(EDGE)   |
+-------------+
| "player101" |
| "player125" |
+-------------+
Got 2 rows (time spent 496/671 us)

Fri, 20 Aug 2021 06:36:05 UTC

Executed 3 times, (total time spent 3681/4734 us), (average time spent 1227/1578 us)
```

## 睡眠

睡眠 N 秒。常用于修改 Schema 的操作中，因为修改 Schema 是异步实现的，需要在下一个心跳周期才同步数据。命令如下：

```ngql
nebula> :sleep N;
```

## 断开连接

用户可以使用`:EXIT`或者`:QUIT`从 Nebula Graph 断开连接。为方便使用，Nebula Console 支持使用不带冒号（:）的小写命令，例如`quit`。

示例：

```ngql
nebula> :QUIT;

Bye root!
```

## 常见问题

### 如何通过源码安装 Nebula Console？

下载和编译 Nebula Console 的最新源码，请参见 [GitHub nebula console](https://github.com/vesoft-inc/nebula-console#build-nebula-graph-console) 页面的说明。
