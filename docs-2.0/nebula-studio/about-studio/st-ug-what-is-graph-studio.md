# 什么是 NebulaGraph Studio

NebulaGraph Studio（简称 Studio）是一款可以通过 Web 访问的开源图数据库可视化工具，搭配 [{{nebula.name}}](../../README.md) 内核使用，提供构图、数据导入、编写 nGQL 查询等一站式服务。用户可以在{{nebula.name}} GitHub 仓库中查看最新源码，详情参见 [nebula-studio](https://github.com/vesoft-inc/nebula-studio)。

!!! Note

    用户可以[在线试用 Studio](https://playground.nebula-graph.com.cn/explore) 部分功能。企业版 NebulaGraph 提供功能更强大的可视化工具，点击[免费试用](https://computenest.console.aliyun.com/user/cn-hangzhou/serviceInstanceCreate?ServiceId=service-39f4f251e9484369a778&ServiceVersion=20&isTrial=true)即可在阿里云上体验。

## 发行版本

用户可以使用 RPM 包、DEB 包、tar 包和 Docker 服务安装部署 Studio，在 Kubernetes 集群里还支持使用 Helm 安装部署 Studio。详细信息参考 [部署 Studio](../deploy-connect/st-ug-deploy.md)。

几种部署方式功能基本相同，在使用 Studio 时可能会受到限制。详细信息，参考[使用限制](st-ug-limitations.md)。

## 产品功能

Studio 可以方便管理{{nebula.name}}数据，具备以下功能：

- 使用 **Schema** 管理功能，用户可以使用图形界面完成图空间、Tag（标签）、Edge Type（边类型）、索引的创建，查看图空间的统计数据，快速上手{{nebula.name}}。
  
- 使用**导入**功能，通过简单的配置，用户即能批量导入点和边数据，并能实时查看数据导入日志。

- 使用**控制台**功能，用户可以使用 nGQL 语句创建 Schema，并对数据执行增删改查操作。

## 适用场景

如果有以下任一需求，都可以使用 Studio：

- 已经安装部署了{{nebula.name}}，想使用 GUI 工具创建 Schema、导入数据、执行 nGQL 语句查询。
- 刚开始学习 nGQL（NebulaGraph Query Language），但是不习惯用命令行工具，更希望使用 GUI 工具查看语句输出的结果。

## 身份验证

因为{{nebula.name}}默认不启用身份验证，所以用户可以使用 `root` 账号和任意密码登录 Studio。

当{{nebula.name}}启用了身份验证后，用户只能使用指定的账号和密码登录 Studio。关于{{nebula.name}}的身份验证功能，参考 [身份验证](../../7.data-security/1.authentication/1.authentication.md "点击前往{{nebula.name}}官网")。


## 版本兼容性

!!! Note

    Studio 版本发布节奏独立于{{nebula.name}}内核，其命名方式也不参照内核命名规则，两者兼容对应关系如下表。

|{{nebula.name}}版本 | Studio 版本 |
| --- | --- |
| 3.5.0  | 3.7.0 |
| 3.4.0 ~ 3.4.1| 3.7.0、3.6.0、3.5.1、3.5.0 |
| 3.3.0 | 3.5.1、3.5.0 |
| 3.0.0 ～ 3.2.x| 3.4.1、3.4.0|
| 3.1.0 | 3.3.2 |
| 3.0.0 | 3.2.x |
| 2.6.x | 3.1.x |
| 2.6.x | 3.1.x |
| 2.0 & 2.0.1 | 2.x |
| 1.x | 1.x|

## 版本更新

Studio 处于持续开发状态中。用户可以通过 [Studio 版本更新说明](../../20.appendix/release-notes/studio-release-note.md)查看最新发布的功能。

成功连接 Studio 后，用户可以在页面右上角点击用户头像，再点击 **更新日志**，查看 Studio 的版本更新说明。

![在页面右上角点击头像，并在弹出菜单里点击“新发布”](https://docs-cdn.nebula-graph.com.cn/figures/st-ug-001-cn.png)
