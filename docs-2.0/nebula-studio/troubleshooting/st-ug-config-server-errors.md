# 连接数据库错误

## 问题描述

按[连接 Studio](../deploy-connect/st-ug-connect.md) 文档操作，提示 **配置失败**。

## 可能的原因及解决方法

用户可以按以下步骤排查问题。

### 第 1 步。确认 **Host** 字段的格式是否正确

必须填写 Nebula Graph 图数据库 Graph 服务的 IP 地址（`graph_server_ip`）和端口。如果未做修改，端口默认为 `9669`。即使 Nebula Graph 与 Studio 都部署在当前机器上，用户也必须使用本机 IP 地址，而不能使用 `127.0.0.1`、`localhost` 或者 `0.0.0.0`。

### 第 2 步。确认 **用户名** 和 **密码** 是否正确

如果 Nebula Graph 没有开启身份认证，用户可以填写任意字符串登录。

如果已经开启身份认证，用户必须使用分配的账号登录。

### 第 3 步。确认 Nebula Graph 服务是否正常

检查 Nebula Graph 服务状态。关于查看服务的操作：

- 如果在 Linux 服务器上通过编译部署的 Nebula Graph，参考[查看 Nebula Graph 服务](../../4.deployment-and-installation/2.compile-and-install-nebula-graph/deploy-nebula-graph-cluster.md "点击查看 Nebula Graph 内核文档")。
- 如果使用 Docker Compose 部署和 RPM 部署的 Nebula Graph，参考[查看 Nebula Graph 服务状态和端口](../deploy-connect/st-ug-deploy.md "点击前往 GitHub 网站")。
  
如果 Nebula Graph 服务正常，进入第 4 步继续排查问题。否则，请重启 Nebula Graph 服务。

!!! Note

    如果之前使用 `docker-compose up -d` 启动 Nebula Graph，必须运行 `docker-compose down` 命令停止 Nebula Graph。

### 第 4 步。确认 Graph 服务的网络连接是否正常

在 Studio 机器上运行命令（例如 `telnet <graph_server_ip> 9669`）确认 Nebula Graph 的 Graph 服务网络连接是否正常。

如果连接失败，则按以下要求检查：

- 如果 Studio 与 Nebula Graph 在同一台机器上，检查端口是否已暴露。
- 如果两者不在同一台机器上，检查 Nebula Graph 服务器的网络配置，例如，防火墙、网关以及端口。

如果按上述步骤排查后仍无法连接 Nebula Graph 服务，请前往 [Nebula Graph 官方论坛](https://discuss.nebula-graph.com.cn/ "点击前往 Nebula Graph 官方论坛")咨询。
