# 连接数据库错误

## 问题描述

按 [连接 Studio](../deploy-connect/st-ug-connect.md) 文档操作，连接数据库失败。

## 可能的原因及解决方法

- Nebula Graph 版本是否正确？

  目前 Studio 仅支持 Nebula Graph v1.1.0 及以前版本，不支持 Nebula Graph v2.0.0。

- Nebula Graph 是否正常启动？
  
  您可以使用 [nebula-console 连接 Nebula Graph](https://github.com/vesoft-inc/nebula-docker-compose/blob/master/README_zh-CN.md#%E9%83%A8%E7%BD%B2%E6%B5%81%E7%A8%8B "点击前往 GitHub 网站")。如果 nebula-console 能正常连接 Nebula Graph，则继续按以下步骤排查问题。

- 已经部署的 Nebula Graph 是否能被访问？
  
  在命令行工具里，运行命令 `curl <部署 Nebula Graph 的机器 IP 地址>:3699`。如果 <!--返回什么结果是正常的？--> 表示 Nebula Graph 服务能被正常访问。如果不能，

- 部署 Studio 的机器是否已经关闭防火墙？

  必须关闭防火墙。<!--有推荐的操作步骤吗？-->

- 
