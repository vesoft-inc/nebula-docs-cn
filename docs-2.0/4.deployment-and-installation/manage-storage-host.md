# 管理 Storage 主机

从 3.0.0 版本开始，在配置文件中添加的 Storage 主机无法直接读写，配置文件的作用仅仅是将 Storage 主机注册至 Meta 服务中。必须使用`ADD HOSTS`命令后，才能正常读写 Storage 主机。

## 增加 Storage 主机

向集群中增加 Storage 主机。

```ngql
ADD HOSTS <ip>:<port> [,<ip>:<port> ...];
```

!!! note

    - 增加 Storage 主机在**下一个**心跳周期之后才能生效，为确保数据同步，请等待 2 个心跳周期（20 秒），然后执行`SHOW HOSTS`查看是否在线。
    
    - IP地址和端口请和配置文件中的设置保持一致，例如单机部署的默认为`127.0.0.1:9779`。

## 删除 Storage 主机

从集群中删除 Storage 主机。

!!! note

    无法直接删除正在使用的 Storage 主机，需要先删除关联的图空间，才能删除 Storage 主机。

```ngql
DROP HOSTS <ip>:<port> [,<ip>:<port> ...];
```
