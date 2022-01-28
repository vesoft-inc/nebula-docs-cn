# 管理 Storage 主机

从 3.0.0 版本开始，在配置文件中添加的 Storage 节点无法直接读写，配置文件的作用仅仅是将 Storage 节点注册至 Meta 服务中。必须使用`ADD HOSTS`命令后，才能正常读写 Storage 节点。

## 增加 Storage 主机

向集群中增加 Storage 主机。

```ngql
ADD HOSTS <ip>:<port> [,<ip>:<port> ...];
```

## 删除 Storage 主机

从集群中删除 Storage 主机。

!!! note

    无法直接删除正在使用的 Storage 主机，需要先删除关联的图空间，才能删除 Storage 主机。

```ngql
DROP HOSTS <ip>:<port> [,<ip>:<port> ...];
```
