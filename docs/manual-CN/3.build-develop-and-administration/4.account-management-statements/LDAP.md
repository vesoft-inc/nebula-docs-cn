# 集成 LDAP

本文档介绍如何将 **Nebula Graph** 连接到 LDAP 服务器以进行身份​​验证（仅企业版可用）。

## LDAP 介绍

集成 LDAP 后， **Nebula Graph** 即可共享在 LDAP 中定义的用户身份信息和密码。

## 安装 LDAP 插件

1. 构建 LDAP 服务器并插入相应的记录。

    例如，插入用户名 `test2`，密码 `passwdtest2`。然后使用以下命令查看用户：

    ```bash
    ldapsearch -x -b 'uid=test2,ou=it,dc=sys,dc=com'
    ```

2. 将 `auth_ldap.so` 文件放在安装路径的共享目录中。
3. 创建影子账户安装 `auth_ldap` 插件。

    以 root 身份登录 **Nebula Graph**， 密码为 `nebula`，身份验证 `auth_type` 类型为 `password`：

    ```bash
    ./bin/nebula -u root  -p nebula   --port 3699 --addr="127.0.0.1"
    ```

    创建影子账户：

    ```ngql
    # 此处需要为影子账户 test2 赋权
    nebula> CREATE USER test2 WITH PASSWORD "";
    ```

    安装 `auth_ldap` 插件：

    ```ngql
    nebula> INSTALL PLUGIN auth_ldap SONMAE "auth_ldap.so";
    ```

    查看插件是否成功安装：

    ```ngql
    nebula> SHOW PLUGINS;
    ```

## 卸载 LDAP 插件

1. 以 root 身份登录 **Nebula Graph**， 密码为 `nebula`，身份验证 `auth_type` 类型为 `password`：

    ```bash
    ./bin/nebula -u root  -p nebula   --port 3699 --addr="127.0.0.1"
    ```

2. 执行以下命令卸载 `auth_ldap` 插件：

    ```ngql
    nebula> UNINSTALL PLUGIN auth_ldap;
    ```

## 启用 LDAP 身份验证

**Nebula Graph** 默认禁用 LDAP 身份验证。执行以下操作启用 LDAP 身份验证：

### 开启身份验证开关

首先，开启身份验证开关。打开 `nebula-graphd.conf` 文件（默认目录为 `/usr/local/nebula/etc/`），然后找到 `--enable_authorize`，将其更改为 `true`：

```conf
########## Authorization ##########
# Enable authorization
--enable_authorize=true
```

### 配置 Nebula Graph

然后配置 **Nebula Graph** 以使用 LDAP。您可以使用两种 LDAP 方法来为 **Nebula Graph** 开启身份验证。

- **简单绑定**。打开 `nebula-graphd.conf` 文件（默认目录为 `/usr/local/nebula/etc/`），找到 `Authentication` 部分，将 `auth_type` 更改为 `ldap` 并添加以下属性：

    ```conf
    ########## Authentication ##########
    # User login authentication type, password for nebula authentication, ldap for ldap authentication, cloud for cloud authentication
    --auth_type=ldap
    --ldap_server=127.0.0.1
    --ldap_port=389
    --ldap_scheme=ldap
    --ldap_prefix=uid=
    --ldap_suffix=,ou=it,dc=sys,dc=com
    ```

- **搜索和绑定**. 打开 `nebula-graphd.conf` 文件（默认目录为 `/usr/local/nebula/etc/`），找到 `Authentication` 部分，将 `auth_type` 更改为 `ldap` 并添加以下属性：

    ```conf
    ########## Authentication ##########
    # User login authentication type, password for nebula authentication, ldap for ldap authentication, cloud for cloud authentication
    --auth_type=ldap
    --ldap_server=127.0.0.1
    --ldap_port=389
    --ldap_scheme=ldap
    --ldap_prefix=uid=
    --ldap_suffix=,ou=it,dc=sys,dc=com
    ```

### 重启服务

保存并关闭配置文件，然后重启服务：

```bash
/usr/local/nebula/scripts/nebula.service restart all
```

## 禁用 LDAP

将 `nebula-graphd.conf` 中的 `--enable_authorize` 参数设置为 `false` 然后重启服务即可在 **Nebula Graph** 中禁用 LDAP 身份验证。

## 使用 LDAP 连接 Nebula Graph

配置完成后，您可以使用 LDAP 身份验证连接到 **Nebula Graph**，运行以下命令：

```bash
./bin/nebula -u test2 -p passwdtest2 --port 3699 --addr="127.0.0.1"
```
