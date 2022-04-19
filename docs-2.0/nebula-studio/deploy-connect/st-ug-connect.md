# 连接数据库
<!--
在 Nebula Graph Cloud Service 上，创建 Nebula Graph 实例后，用户可以一键直连云服务版 Studio。详细信息参考 [Nebula Graph Cloud Service 用户手册](https://cloud-docs.nebula-graph.com.cn/cn/posts/manage-instances/dbaas-ug-connect-nebulastudio/ "点击进入 Nebula Graph Cloud Service 用户手册")。
-->

在成功启动 Studio 后，用户需要配置连接 Nebula Graph。本文主要描述 Studio 如何连接 Nebula Graph 数据库。

## 前提条件

在连接 Nebula Graph 数据库前，用户需要确认以下信息：

- Studio 已经启动。详细信息参考[部署 Studio](st-ug-deploy.md)。

- Nebula Graph 的 Graph 服务本机 IP 地址以及服务所用端口。默认端口为 `9669`。

- Nebula Graph 数据库登录账号信息，包括用户名和密码。

  !!! Note
  
        如果 Nebula Graph 已经启用了身份验证，并且已经创建了不同角色的用户，用户只能使用被分配到的账号和密码登录数据库。如果未启用身份验证，用户可以使用 `root` 用户名和任意密码登录数据库。关于启用身份验证，参考 [Nebula Graph 用户手册](../../README.md "点击进入 Nebula Graph 用户手册")。

## 操作步骤

按以下步骤连接 Nebula Graph 数据库：

1. 在 Studio 的 **配置数据库** 页面上，输入以下信息：

   - **Host**：填写 Nebula Graph 的 Graph 服务本机 IP 地址及端口。格式为`ip:port`。默认端口为`9669`。

    !!! Note

        即使 Nebula Graph 数据库与 Studio 部署在同一台机器上，用户也必须在 **Host** 字段填写这台机器的本机 IP 地址，而不是 `127.0.0.1` 或者 `localhost`。

   - **用户名** 和 **密码**：根据 Nebula Graph 的身份验证设置填写登录账号和密码。
     - 如果未启用身份验证，可以填写默认用户名 `root` 和任意密码。
     - 如果已启用身份验证，但是未创建账号信息，用户只能以 GOD 角色登录，必须填写 `root` 及对应的密码 `nebula`。
     - 如果已启用身份验证，同时又创建了不同的用户并分配了角色，不同角色的用户使用自己的账号和密码登录。

      ![Nebula Graph Studio 的登录页面](https://docs-cdn.nebula-graph.com.cn/figures/st-ug-000-cn.png "配置数据库")

2. 完成设置后，点击 **连接** 按钮。  

  如果能看到如下图所示的界面，表示已经成功连接到 Nebula Graph 数据库。

  ![Studio 进入控制台页面，表示成功连接到 Nebula Graph](https://docs-cdn.nebula-graph.com.cn/figures/st-ug-003-cn.png)

一次连接会话持续 30 分钟。如果超过 30 分钟没有操作，会话即断开，用户需要重新登录数据库。

## 后续操作

成功连接 Nebula Graph 数据库后，根据账号的权限，用户可以选择执行以下操作：

- 拥有 GOD 或者 ADMIN 权限的账号，可以使用[**控制台**](../quick-start/st-ug-create-schema.md)或者 [**Schema**](../manage-schema/st-ug-crud-space.md) 页面管理 Schema、[批量导入数据](../quick-start/st-ug-import-data.md)、在**控制台**页面上执行 nGQL 语句。
- 拥有 DBA 或者 USER 权限的账号，可以[批量导入数据](../quick-start/st-ug-import-data.md)、在**控制台**页面上执行 nGQL 语句。
- 拥有 GUEST 权限的账号，仅可以在 **控制台** 页面上执行 nGQL 语句查询数据。

!!! note

    账号权限参见 [内置角色权限](../../7.data-security/1.authentication/3.role-list.md)。

### 登出
<!--
使用云服务版 Studio 时，用户不能清除连接。
-->

如果需要重新连接 Nebula Graph 数据库，可以登出后重新配置数据库。

在页面右上角单击用户头像，单击 **登出**，如果浏览器上显示 **配置数据库** 页面，表示 Studio 已经成功断开了与 Nebula Graph 数据库的连接。

![reset](https://docs-cdn.nebula-graph.com.cn/figures/st-ug-000-cn.png)