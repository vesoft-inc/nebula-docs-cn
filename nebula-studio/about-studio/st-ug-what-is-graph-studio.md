# 什么是 Nebula Graph Studio

Nebula Graph Studio（简称 Studio）是一款可以通过 Web 访问的图数据库可视化工具，搭配 Nebula Graph DBMS 使用，为您提供构图、数据导入、编写 nGQL 查询、图探索等一站式服务。即使没有图数据库操作经验，您也可以快速成为图专家。

## 发行版本

Studio 目前有两个发行版本：

- Docker 版本：您可以使用 Docker 服务手动部署 Studio，并连接到 Nebula Graph 数据库。详细信息，参考 [部署 Studio](../install-configure/st-ug-install.md)。
- 云服务版本：您可以在 Nebula Graph Cloud Service 上创建 Nebula Graph 数据库实例，并一键直连云服务版 Studio。详细信息，参考 [Nebula Graph Cloud Service 用户手册](https://cloud-docs.nebula-graph.com.cn/cn/posts/manage-instances/dbaas-ug-connect-nebulastudio/ "点击前往 Nebula Graph Cloud Service 用户手册")。

两个发行版本功能基本相同。但是，因为部署方式不同，会有不同的使用限制。详细信息，参考 [使用限制](st-ug-limitations.md)。

## 产品功能

Studio 提供以下功能：

- 灵活的部署方式，满足您的不同需求。
- GUI 设计，方便您管理 Nebula Graph 图数据：
  - 借助 **Schema** 管理功能，您可以使用图形界面完成 Schema（模式）创建，快速上手 Nebula Graph 数据库。
  - 借助 **控制台** 功能，您可以使用 nGQL 语句创建 Schema，并对数据执行增删改查操作。
  - 借助 **导入** 功能，通过简单的配置，您即能批量导入点和边数据，并能实时查看数据导入日志。
- 图探索，支持可视化展示图数据，使您更容易发现数据之间的关联性，提高数据分析和解读的效率。

## 适用场景

如果您有以下任一需求，都可以使用 Studio：

- 您有一份数据集，想进行可视化图探索或者数据分析。您可以使用 Docker Compose 或者 Nebula Graph Cloud Service 部署 Nebula Graph，再使用 Studio 完成可视化操作。
- 您已经安装部署了 Nebula Graph 数据库，并且已经导入数据集，想使用 GUI 工具执行 nGQL 语句查询、可视化图探索或者数据分析。
- 您刚开始学习 nGQL（Nebula Graph Query Language），但是不习惯用命令行工具，更希望使用 GUI 工具查看语句输出的结果。

## 身份验证

对于云服务版 Studio，只有 Nebula Graph 实例的创建者以及被授予操作权限的 Nebula Graph Cloud Service 用户可以登录 Studio。详细信息参考 [Nebula Graph Cloud Service 用户手册](https://cloud-docs.nebula-graph.com.cn/cn/posts/manage-instances/dbaas-ug-connect-nebulastudio/ "点击前往 Nebula Graph Cloud Service 用户手册")。

对于 Docker 版 Studio，因为 Nebula Graph 默认不启用身份验证，所以，一般情况下您可以使用默认账号和密码（`user` 和 `password`）登录 Studio。当 Nebula Graph 启用了身份验证后，您只能使用指定的账号和密码登录 Studio。关于 Nebula Graph 的身份验证功能，参考 [Nebula Graph 用户手册](https://docs.nebula-graph.com.cn/manual-CN/3.build-develop-and-administration/4.account-management-statements/authentication/ "点击前往 Nebula Graph 官网")。
