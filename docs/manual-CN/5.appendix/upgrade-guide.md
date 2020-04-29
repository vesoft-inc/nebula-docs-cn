# Nebula Graph 升级指南

本文档介绍如何升级 Nebula Graph。对应版本升级指南见下文。

## 从 Nebula Graph RC3 升级至 RC4

- 首先停止所有机器的 Nebula Graph 服务
  - 在每一台机器执行 `scripts/nebula.service stop all` 命令
  - 然后执行 `scripts/nebula.service status all` 命令确认进程已经退出
- 在每一台机器(根据系统环境)安装新的 `rpm` 包
  - 下载安装包：`https://github.com/vesoft-inc/nebula/releases/tag/v1.0.0-rc4`
  - 安装 Nebula Graph：`rpm -Uvh nebula-1.0.0-rc4.el7-5.x86_64.rpm`
- 如果下载速度过慢，国内用户可在 OSS 下载对应安装包。
  - [CentOS 6.5](https://nebula-graph.oss-cn-hangzhou.aliyuncs.com/package/1.0.0-rc4/nebula-1.0.0-rc4.el6-5.x86_64.rpm)
  - [CentOS 7.5](https://nebula-graph.oss-cn-hangzhou.aliyuncs.com/package/1.0.0-rc4/nebula-1.0.0-rc4.el7-5.x86_64.rpm)
  - [Ubuntu 16.04](https://nebula-graph.oss-cn-hangzhou.aliyuncs.com/package/1.0.0-rc4/nebula-1.0.0-rc4.ubuntu1604.amd64.deb)
  - [Ubuntu 18.04](https://nebula-graph.oss-cn-hangzhou.aliyuncs.com/package/1.0.0-rc4/nebula-1.0.0-rc4.ubuntu1804.amd64.deb)
- 启动 Nebula Graph 服务
  - 在所有机器执行 `scripts/nebula.service start all` 命令
  - 然后执行 `scripts/nebula.service status all` 确认进程正常启动
  - 或者 Nebula 终端运行 `nebula> SHOW HOSTS` 查看服务状态
- **重新导入数据**
