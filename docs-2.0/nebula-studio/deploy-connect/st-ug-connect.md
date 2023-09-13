# 连接数据库

在成功启动 Studio 后，用户需要配置连接{{nebula.name}}。本文主要描述 Studio 如何连接{{nebula.name}}。

## 前提条件

在连接{{nebula.name}}数据库前，用户需要确认以下信息：

- Studio 已经启动。详细信息参考[部署 Studio](st-ug-deploy.md)。

- {{nebula.name}}的 Graph 服务本机 IP 地址以及服务所用端口。默认端口为 `9669`。

- {{nebula.name}}登录账号信息，包括用户名和密码。

## 操作步骤

按以下步骤连接{{nebula.name}}：

1. 在浏览器地址栏输入 `http://<ip_address>:7001`。

  在浏览器窗口中看到以下登录界面表示已经成功部署并启动了 Studio。

  <img src="https://docs-cdn.nebula-graph.com.cn/figures/std_login_230912_cn.png" width="1200" alt="Studio 登录界面截屏">

2. 在 Studio 的 **配置数据库** 页面上，输入以下信息：

  - **Graphd IP 地址**：填写{{nebula.name}}的 Graph 服务本机 IP 地址。例如`192.168.10.100`。

    !!! Note

        - 即使{{nebula.name}}与 Studio 部署在同一台机器上，用户也必须填写这台机器的本机 IP 地址，而不是 `127.0.0.1` 或者 `localhost`。
        - 在新的标签页连接另一个{{nebula.name}}时，会覆盖旧标签页的会话。如果需要同时登录多个{{nebula.name}}，可以用不同的浏览器或者无痕模式。

  - **Port**：Graphd 服务的端口。默认为`9669`。

  - **用户名** 和 **密码**：根据{{nebula.name}}的身份验证设置填写登录账号和密码。
    - 如果未启用身份验证，可以填写默认用户名 `root` 和任意密码。
    - 如果已启用身份验证，但是未创建账号信息，用户只能以 GOD 角色登录，必须填写 `root` 及对应的密码 `nebula`。
    - 如果已启用身份验证，同时又创建了不同的用户并分配了角色，不同角色的用户使用自己的账号和密码登录。

3. 完成设置后，点击 **连接** 按钮。  

  !!! note

        一次连接会话持续 30 分钟。如果超过 30 分钟没有操作，会话即断开，用户需要重新登录数据库。

首次登录会显示欢迎页，根据使用流程展示相关功能，并且支持自动下载并导入测试数据集。

想要再次访问欢迎页，单击 ![help](https://docs-cdn.nebula-graph.com.cn/figures/navbar-help.png)。

## 后续操作

成功连接{{nebula.name}}后，用户可以执行以下操作：

- 使用[**控制台**](../quick-start/st-ug-create-schema.md)或者 [**Schema**](../manage-schema/st-ug-crud-space.md) 页面管理 Schema。
- [批量导入数据](../quick-start/st-ug-import-data.md)。
- 在 **控制台** 页面上执行 nGQL 语句查询数据。
- 在 **Schema 草图**页面图形化设计 Schema。


!!! note

    账号的权限决定了能执行哪些操作。详情参见[内置角色权限](../../7.data-security/1.authentication/3.role-list.md)。

### 登出

如果需要重新连接{{nebula.name}}，可以登出后重新配置数据库。

在页面右上角单击用户头像，单击 **登出**。
