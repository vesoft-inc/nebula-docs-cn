# 单点登录

NebulaGraph Dashboard 企业版支持普通账户、LDAP 账户和 OAuth2.0 账户。本文介绍如何在 Dashboard 上配置 LDAP 和 OAuth2.0 协议。

!!! note

    - 配置完成后，请参见[权限管理](../5.account-management.md)创建账户和邀请激活。
    - 可以在左侧导航栏里通过开关快速开启或关闭 LDAP 或 OAuth2.0 登录方式。

## LDAP 设置

### 入口

1. 在 Dashboard 企业版顶部导航栏，单击**平台设置**。
2. 在左侧导航栏单击**单点登录**->**LDAP**。

### 设置说明

|参数|示例|说明|
|:--|:--|:--|
|`LDAP Server Address` | `ldap://192.168.10.100` | LDAP 服务器地址。 |  
|`Bind DN` | `cn=admin,dc=vesoft,dc=com`| LDAP 服务器登录用户名。  |
|`Password` |`123456` | LDAP 服务器登录密码。 |
|`Base DN` | `dc=vesoft,dc=com`| 查询用户数据的路径。 |
|`User Filter` | `&(objectClass=*)` | 查询条件。 |
|`Email Key` | `mail`| LDAP 数据库存放邮箱信息的字段名。 |

## OAuth2.0 设置

### 入口

1. 在 Dashboard 企业版顶部导航栏，单击**平台设置**。
2. 在左侧导航栏单击**单点登录**->**OAuth2.0**。

### 设置说明

|参数|示例|说明|
|:--|:--|:--|
|`ClientID` | `4953xxx-mmnoge13xx.apps.googleusercontent.com`| 应用的 ClientId。  |
|`ClientSecret` | `GOCxxx-xaytomFexxx` | 应用的 ClientSecret。 |
|`RedirectURL` | `http://dashboard.vesoft-inc.com/login` |重定向到 Dashboard 的 URL。   |
|`AuthURL` | `https://accounts.google.com/o/oauth2/auth` | 认证 URL。  |
|`TokenURL` | `https://oauth2.googleapis.com/token`| 获取 access_token 的URL。 |
|`UserInfoURL` | `https://www.googleapis.com/oauth2/v1/userinfo`| 获取用户信息的 URL。 |
|`Name` | `vesoft`| Oauth 的名称。 |
