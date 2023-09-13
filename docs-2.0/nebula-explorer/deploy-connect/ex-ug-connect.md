# 连接数据库

在成功启动{{explorer.name}}后，用户需要配置连接{{nebula.name}}。默认情况下可以直接连接数据库。为保证数据安全，还支持 OAuth2.0 认证，认证通过后才可以连接数据库。

## 前提条件

在连接{{nebula.name}}前，用户需要确认以下信息：

- 已经安装部署了{{explorer.name}}。详细信息，参见[部署{{explorer.name}}](../deploy-connect/ex-ug-deploy.md)。

- {{nebula.name}} 的 Graph 服务本机 IP 地址以及服务所用端口。默认端口为 `9669`。

-{{nebula.name}}登录账号信息，包括用户名和密码。

- 建议使用 Chrome 89 及以上的版本的 Chrome 浏览器，否则可能有兼容问题。

## OAuth2.0 认证设置

!!! caution

    当前 OAuth2.0 认证设置为 Beta 功能，后续可能会有一定优化调整。

!!! note

    如果想直接连接数据库，请参见后文**连接数据库**部分。

如果需要开启 OAuth2.0 认证，需要在{{explorer.name}}安装目录内修改配置文件。路径为`config/app-config.yaml`。

OAuth 部分的配置说明如下。

|参数|示例|说明|
|:--|:--|:--|
|`Enable`|`false`|是否开启 OAuth2.0 认证。|
|`ClientID` | `4953xxx-mmnoge13xx.apps.googleusercontent.com`| 应用的 ClientId。  |
|`ClientSecret` | `GOCxxx-xaytomFexxx` | 应用的 ClientSecret。 |
|`RedirectURL` | `http://dashboard.vesoft-inc.com/login` |重定向到{{dashboard_ent.name}}的 URL。   |
|`AuthURL` | `https://accounts.google.com/o/oauth2/auth` | 认证 URL。  |
|`TokenURL` | `https://oauth2.googleapis.com/token`| 获取 access_token 的 URL。 |
|`UserInfoURL` | `https://www.googleapis.com/oauth2/v1/userinfo`| 获取用户信息的 URL。 |
|`UsernameKey` | `email`| 用户名字段。 |
|`Organization` |  `vesoft company`       |  组织名称。             |
|`TokenName`|`oauth_token`|Cookie 里的 Token 名称。|
|`Scope`| `email`| OAuth 的权限范围。权限范围需要是厂商 OAuth2.0 平台配置的 scope 的子集，否则请求会失败。请求的 scope 需要能获取到`UsernameKey`的值。|
|`AvatarKey`|`picture`|用户信息里的 Avatar Key。|

配置完成后重启{{explorer.name}}服务，登录页面会先展示 OAuth 认证页面，通过后才能继续连接数据库。

## 连接数据库

按以下步骤连接{{nebula.name}}：

1. 在浏览器地址栏输入 `http://<ip_address>:7002`。

  在浏览器窗口中看到以下登录界面表示已经成功部署并启动了{{explorer.name}}。

  <img src="https://docs-cdn.nebula-graph.com.cn/figures/ec_expl_login_230912_cn.png" width="1200" alt="图探索登录界面截屏">

  !!! note

        首次登录{{explorer.name}}的时候，页面显示*最终用户许可协议*的内容，请仔细阅读并单击**同意**。

2. 在{{explorer.name}}的**配置数据库**页面上，输入以下信息：

  - **Graphd IP 地址**：填写{{nebula.name}}的 Graph 服务本机 IP 地址。例如`192.168.10.100`。

    !!! Note

        - 即使{{nebula.name}}与{{explorer.name}}部署在同一台机器上，用户也必须填写这台机器的本机 IP 地址，而不是 `127.0.0.1` 或者 `localhost`。
        - 在新的标签页连接另一个{{nebula.name}}时，会覆盖旧标签页的会话。如果需要同时登录多个{{nebula.name}}，可以用不同的浏览器或者无痕模式。

  - **Port**：Graphd 服务的端口。默认为`9669`。

  - **用户名**和**密码**：根据{{nebula.name}}的[身份验证](../../7.data-security/1.authentication/1.authentication.md)设置填写登录账号和密码。
    - 如果未启用身份验证，可以填写默认用户名 `root` 和任意密码。
    - 如果已启用身份验证，但是未创建账号信息，用户只能以 GOD 角色登录，必须填写用户名 `root` 和密码 `nebula`。
    - 如果已启用身份验证，同时又创建了不同的用户并分配了角色，不同角色的用户使用自己的账号和密码登录。

3. 完成设置后，点击**登录**按钮。

  !!! note

        一次连接会话持续 30 分钟。如果超过 30 分钟没有操作，会话即断开，用户需要重新登录数据库。

首次登录会显示欢迎页，根据使用流程展示相关功能，并且支持自动下载并导入测试数据集。

想要再次访问欢迎页，在 ![help](https://docs-cdn.nebula-graph.com.cn/figures/navbar-help.png) 下选择**新手引导**。

## 断开连接

在页面右上角，选择![icon](https://docs-cdn.nebula-graph.com.cn/figures/image-icon10.png)图标 > 清空连接。

如果浏览器上显示**配置数据库**页面，表示{{explorer.name}}已经成功断开了与{{nebula.name}}的连接。
