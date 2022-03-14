# Nebula Graph {{ nebula.release }} release notes

## Bug fix

- 修复`ADD HOSTS`后 Storage 服务可能需要等待较长时间才能在线（`ONLINE`）的缺陷。 [#3950](https://github.com/vesoft-inc/nebula/pull/3950)

- 修复了早于 v2.6 版本的客户端连接 Nebula Graph 时，Graph 服务会崩溃的缺陷。 [#3942](https://github.com/vesoft-inc/nebula/pull/3942)

- 修复了如果图空间中没有 Tag 会导致升级时升级工具崩溃的缺陷。 [#3920](https://github.com/vesoft-inc/nebula/pull/3920)

- 修复了`MATCH <node>, <node>, <path>`时，Graph 服务会崩溃的缺陷。 [#3915](https://github.com/vesoft-inc/nebula/pull/3915)

## 历史版本

[历史版本](https://nebula-graph.com.cn/tags/release-note/)
