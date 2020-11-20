# 身份验证

当客户端连接到 **Nebula Graph** 时，**Nebula Graph** 就会创建一个会话。会话用来存储有关连接的各种信息。每条会话只关联一个用户。身份验证即为将会话映射到特定用户的过程。一旦将会话映射到用户，便可以使用授权将一组权限与之关联。

**Nebula Graph** 支持两种身份验证方式，即本地和 LDAP。详细说明见下文。

## 本地身份验证

本地数据库存储用户名、加密密码，本地用户设置和远程 LDAP 用户设置。当用户尝试访问数据库时，将接受安全验证。

按照以下步骤启用本地认证：

1. 将配置文件 `nebula-graphd.conf`（默认目录 `/usr/local/nebula/etc/`）中的 `--enable_authorize` 属性设置为 `true`。
2. 保存第一步的设置并关闭配置文件 `nebula-graphd.conf`。
3. 重启 Nebula Graph 服务。

## LDAP

轻型目录访问协议（LDAP）是用于访问目录服务的轻型客户端-服务器协议。 LDAP 中存储的用户优先级高于本地数据库用户。例如，如果两个本地和 LDAP 都有一个名为 “Amber” 的用户，则优先从 LDAP 读取该用户的设置和角色信息。

与本地身份验证不同，除需设置 `--enable_authorize` 参数之外， LDAP 还需要在 `nebula-graphd.conf` 文件中（默认目录 `/usr/local/nebula/etc/`）配置相关参数方可启用。详细信息，请参见[集成 LDAP 文档](LDAP.md)。

### LDAP 参数

| 参数名               | 参数类型 | 默认值                                        | 说明                                           |
| -------------------- | -------- | --------------------------------------------- | ---------------------------------------------- |
| ldap_server          | string   | ""                                            | 一系列 ldap 服务器地址。多个地址使用逗号隔开。 |
| ldap_port            | INT32    | LDAP 服务器端口号。如未指定，则使用默认端口。 |
| ldap_scheme          | string   | "ldap"                                        | 仅支持 ldap。                                  |
| ldap_tls             | bool     | false                                         | 开启/禁用 graphd 和 ldap 之间的 TLS 加密方式。 |
| ldap_suffix          | string   | ""                                            | 指定用于所有 ldap 操作的根后缀。               |
| ldap_basedn          | string   | ""                                            | LDAP 的专有名称。                              |
| ldap_binddn          | string   | ""                                            | 允许搜索基本 DN 的 LDAP 用户。                 |
|                      |
| ldap_bindpasswd      | string   | ""                                            | 绑定到 DN 的用户密码。                         |
| ldap_searchattribute | string   | ""                                            | 一系列必填属性。                               |
|                      |
| ldap_searchfilter    | string   | ""                                            | 定义搜索过滤规则。较 searchattribut 更为灵活。 |

## FAQ

### 报错信息：Authentication fails, Invalid data length

身份验证失败，请按照上述步骤开启身份验证。

<!-- ### ObjectClass

| objectClass        | 含义                                               |
| ------------------ | -------------------------------------------------- |
| olcGlobal          | 全局配置文件类型，主要是 `cn=config.ldif` 的配置项 |
| top                | 顶层对象                                           |
| organization       | 组织，比如公司名称，顶层对象                       |
| organizationalUnit | 一个目录节点，通常是 group，或者部门               |
| inetOrgPerson      | 真正的用户节点类型，person 类型，叶子节点          |
| groupOfNames       | 分组的类型，标记一个 group 节点                    |
| olcModuleList      | 配置模块的对象                                     |

### LDAP 关键字

| 关键字 | 英文全称           | 含义                                                                                                                                               |
| ------ | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| dc     | Domain Component   | 域名，其格式是将完整的域名分成几部分，如域名为 example.com 变成 dc=example,dc=com                                                                  |
| uid    | User Id            | 用户 ID，如“tom”                                                                                                                                   |
| ou     | Organization Unit  | 组织单位，类似于 Linux 文件系统中的子目录，它是一个容器对象，组织单位可以包含其他各种对象（包括其他组织单元），如 “market”                         |
| cn     | Common Name        | 公共名称，如 “Thomas Johnson”                                                                                                                      |
| sn     | Surname            | 姓，如 “Johnson”                                                                                                                                   |
| dn     | Distinguished Name | 惟一辨别名，类似于 Linux 文件系统中的绝对路径，每个对象都有一个惟一的名称，如 “uid= tom,ou=market,dc=example,dc=com”，在一个目录树中 DN 总是惟一的 |
| rdn    | Relative dn        | 相对辨别名，类似于文件系统中的相对路径，它是与目录树结构无关的部分，如 “uid=tom” 或 “cn= Thomas Johnson”                                           |
| c      | Country            | 国家，如 “CN” 或 “US” 等。                                                                                                                         |
| o      | Organization       | 组织名，如 “Example, Inc.”                                                                                                                         | -->
