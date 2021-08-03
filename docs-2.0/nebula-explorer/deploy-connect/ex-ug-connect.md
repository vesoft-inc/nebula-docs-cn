# 连接数据库

对于 RPM 安装的 Explorer，在成功启动 Explorer 后，用户需要配置连接 Nebula Graph。本文主要描述 RPM 安装的 Explorer 如何连接 Nebula Graph 数据库。

## 前提条件

在连接 Nebula Graph 数据库前，用户需要确认以下信息：

- 已经安装部署了 Explorer。详细信息参考 [部署 Explorer](../deploy-connect/ex-ug-connect.md)。

- Nebula Graph 的 Graph 服务本机 IP 地址以及服务所用端口。默认端口为 `9669`。

- Nebula Graph 数据库登录账号信息，包括用户名和密码。

  !!! Note
  
        如果 Nebula Graph 已经启用了身份验证，并且已经创建了不同角色的用户，用户只能使用被分配到的账号和密码登录数据库。如果未启用身份验证，用户可以使用 `root` 用户名和任意密码登录数据库。关于启用身份验证，参考 [Nebula Graph 用户手册](../../README.md "点击进入 Nebula Graph 用户手册")。

## 操作步骤

按以下步骤连接 Nebula Graph 数据库：

1. 在 Explorer 的 **配置数据库** 页面上，输入以下信息：

   - **Host**：填写 Nebula Graph 的 Graph 服务本机 IP 地址及端口。格式为 `ip:port`。如果端口未修改，则使用默认端口 `9669`。

    !!! Note

        即使 Nebula Graph 数据库与 Explorer 部署在同一台机器上，用户也必须在 **Host** 字段填写这台机器的本机 IP 地址，而不是 `127.0.0.1` 或者 `localhost`。

   - **用户名** 和 **密码**：根据 Nebula Graph 的身份验证设置填写登录账号和密码。
     - 如果未启用身份验证，可以填写默认用户名 `root` 和任意密码。
     - 如果已启用身份验证，但是未创建账号信息，用户只能以 GOD 角色登录，必须填写 `root` 及对应的密码 `nebula`。
     - 如果已启用身份验证，同时又创建了不同的用户并分配了角色，不同角色的用户使用自己的账号和密码登录。

      ![Nebula Graph Explorer 的登录页面](../figs/ex-ug-002-1.png "配置数据库")

2. 完成设置后，点击 **连接** 按钮。  
   如果能看到如下图所示的界面，表示已经成功连接到 Nebula Graph 数据库。

    ![Explorer 进入控制台页面，表示成功连接到 Nebula Graph](../figs/ex-ug-003-1.png "Nebula Graph 连接成功")

一次连接会话持续 30 分钟。如果超过 30 分钟没有操作，会话即断开，用户需要重新登录数据库。
