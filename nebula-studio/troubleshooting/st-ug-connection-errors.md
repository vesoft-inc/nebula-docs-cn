# 无法访问 Studio  

## 问题描述

我按照文档描述启动 Studio 后访问 `127.0.0.1:7001` 或者 `0.0.0.0:7001`，但是打不开页面，为什么？

## 可能的原因及解决方法

您可以按以下顺序排查问题。

### 第 1 步. 检查 Studio 服务是否正常启动
  
运行 `docker-compose ps` 查看服务是否已经正常启动。  

如果服务正常，返回结果如下。其中，`State` 列应全部显示为 `Up`。

```bash
     Name                          Command               State               Ports
------------------------------------------------------------------------------------------------------
nebula-web-docker_client_1     ./nebula-go-api                  Up      0.0.0.0:32782->8080/tcp
nebula-web-docker_importer_1   nebula-importer --port=569 ...   Up      0.0.0.0:32783->5699/tcp
nebula-web-docker_nginx_1      /docker-entrypoint.sh ngin ...   Up      0.0.0.0:7001->7001/tcp, 80/tcp
nebula-web-docker_web_1        docker-entrypoint.sh npm r ...   Up      0.0.0.0:32784->7001/tcp
```

如果没有返回以上结果，则重新启动 Studio。详细信息，参考 [部署 Studio](../deploy-connect/st-ug-deploy.md)。

### 第 2 步. 确认系统架构

需要确认部署 Studio 服务的机器是否为 x86_64 架构。目前 Studio 仅支持 x86_64 系统架构。

### 第 3 步. 确认访问地址

如果 Studio 与浏览器在同一台机器上，您可以在浏览器里使用 `localhost:7001`、`127.0.0.1:7001` 或者 `0.0.0.0:7001` 访问 Studio。
  
如果两者不在同一台机器上，必须在浏览器里输入 `<Studio 服务的 IP:7001>`。

### 第 4 步. 确认 Studio 服务连接是否正常

运行 `curl <Studio 服务的 IP:7001>` 确认连接是否正常。如果连接失败，则按以下要求检查：

- 如果浏览器与 Studio 在同一台机器上，检查端口是否已暴露。
- 如果两者不在同一台机器上，检查 Studio 服务器的网络配置，例如，防火墙、网关以及端口。

如果按上述步骤排查后仍无法访问 Studio，您可以前往 [Nebula Graph 官方论坛](https://discuss.nebula-graph.com.cn/ "点击前往 Nebula Graph 官方论坛") 咨询。
