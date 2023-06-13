# NebulaGraph Console

NebulaGraph Console 是{{nebula.name}}的原生命令行客户端，用于连接{{nebula.name}}集群并执行查询，同时支持管理参数、导出命令的执行结果、导入测试数据集等功能。

## 版本对照表

参见[Github](https://github.com/vesoft-inc/nebula-console/tree/{{console.branch}})。

## 获取 NebulaGraph Console

NebulaGraph Console 的获取方式如下：

<!-- - 直接从{{nebula.name}}安装路径的 `bin` 目录中获取二进制文件 `nebula-console`。-->

- 从 [GitHub 发布页](https://github.com/vesoft-inc/nebula-console/releases "the nebula-console Releases page")下载二进制文件。

- 编译源码获取二进制文件。编译方法参见 [Install from source code](https://github.com/vesoft-inc/nebula-console#from-source-code)。

## 功能说明

### 连接{{nebula.name}}

运行二进制文件 `nebula-console` 连接{{nebula.name}}的命令语法如下：

```bash
<path_of_console> -addr <ip> -port <port> -u <username> -p <password>
```

`path_of_console`是 NebulaGraph Console 二进制文件的存储路径。

常用参数的说明如下。

| 参数 | 说明 |
| - | - |
| `-h/-help` | 显示帮助菜单。 |
| `-addr/-address` | 设置要连接的 Graph 服务的 IP 地址。默认地址为 127.0.0.1。<!--如果 {{nebula.name}} 部署在 [Nebula Cloud](https://docs.nebula-graph.com.cn/{{cloud.azureLatestRelease}}/nebula-cloud/1.what-is-cloud/) 上，需要创建 [Private Link](https://docs.nebula-graph.com.cn/{{cloud.azureLatestRelease}}/nebula-cloud/nebula-cloud-on-azure/5.solution/5.2.connection-configuration-and-use)，并设置该参数的值为专用终结点的 IP 地址。--> |
| `-P/-port` | 设置要连接的 Graph 服务的端口。默认端口为 9669。|
| `-u/-user` | 设置{{nebula.name}}账号的用户名。未启用身份认证时，可以使用任意已存在的用户名（默认为`root`）。 |
| `-p/-password` | 设置用户名对应的密码。未启用身份认证时，密码可以填写任意字符。 |
| `-t/-timeout`  | 设置整数类型的连接超时时间。单位为毫秒，默认值为 120。 |
| `-e/-eval` | 设置字符串类型的 nGQL 语句。连接成功后会执行一次该语句并返回结果，然后自动断开连接。 |
| `-f/-file` | 设置存储 nGQL 语句的文件的路径。连接成功后会执行该文件内的 nGQL 语句并返回结果，执行完毕后自动断开连接。 |
| `-enable_ssl` | 连接{{nebula.name}}时使用 SSL 加密。 |
| `-ssl_root_ca_path` | 指定 CA 证书的存储路径。 |
| `-ssl_cert_path` | 指定 CRT 证书的存储路径。 |
| `-ssl_private_key_path` | 指定私钥文件的存储路径。 |

更多参数参见[项目仓库](https://github.com/vesoft-inc/nebula-console/tree/{{console.branch}})。

例如，要连接到部署在 192.168.10.8 上的 Graph 服务，运行以下命令。

```bash
./nebula-console -addr 192.168.10.8 -port 9669 -u Joe -p Joespassword
```

### 管理参数

NebulaGraph Console 可以保存参数，用于参数化查询。

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

### 导出执行结果

导出命令执行的返回结果，可以保存为 CSV 文件、 DOT 文件或者 Profile/Explain 结果。

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

- 导出 PROFILE/EXPLAIN 结果到文件命令如下：

  ```ngql
  nebula> :profile <file_name>;
  ```
  或者

  ```ngql
  nebula> :explain <file_name>;
  ```

!!! note

    相比于 Studio 中的截图、CSV 文件，因为保有更多信息量和拥有更好的可读性，经由此命令输出的文本文件内容是首推的在 GitHub issue、论坛中报告执行计划、图查询调优的方式。

  示例：

  ```ngql
  nebula> :profile profile.log
  nebula> PROFILE GO FROM "player102" OVER serve YIELD dst(edge);
  nebula> :profile profile.dot
  nebula> PROFILE FORMAT="dot" GO FROM "player102" OVER serve YIELD dst(edge);
  nebula> :explain explain.log
  nebula> EXPLAIN GO FROM "player102" OVER serve YIELD dst(edge);
  ```

### 加载测试数据集

测试数据集名称为 basketballplayer，详细 Schema 信息和数据信息请使用相关`SHOW`命令查看。

加载测试数据集命令如下：

```ngql
nebula> :play basketballplayer;
```

### 重复执行语句

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

### 睡眠

睡眠 N 秒。常用于修改 Schema 的操作中，因为修改 Schema 是异步实现的，需要在下一个心跳周期才同步数据。命令如下：

```ngql
nebula> :sleep N;
```

### 断开连接

用户可以使用`:EXIT`或者`:QUIT`从{{nebula.name}}断开连接。为方便使用，NebulaGraph Console 支持使用不带冒号（:）的小写命令，例如`quit`。

示例：

```ngql
nebula> :QUIT;

Bye root!
```
