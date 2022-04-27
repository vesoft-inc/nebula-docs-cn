# 欢迎阅读 Nebula Graph {{ nebula.release }} 文档

!!! Note "[查看版本发布说明](20.appendix/release-notes.md)"

    本文档更新时间{{ now().year }}-{{ now().month }}-{{ now().day }}，GitHub commit [{{ git.short_commit }}](https://github.com/vesoft-inc/nebula-docs/commits/v{{nebula.release}})。

Nebula Graph 是一款开源的、分布式的、易扩展的原生图数据库，能够承载数千亿个点和数万亿条边的超大规模数据集，并且提供毫秒级查询。

## 快速开始
* [学习路径](20.appendix/learning-path.md)
* [什么是 Nebula Graph](1.introduction/1.what-is-nebula-graph.md)
* [快速开始](2.quick-start/1.quick-start-workflow.md)
* [部署要求](4.deployment-and-installation/1.resource-preparations.md)
* [nGQL 命令汇总](2.quick-start/6.cheatsheet-for-ngql-command.md)
* [FAQ](20.appendix/0.FAQ.md)
* [生态工具](20.appendix/6.eco-tool-version.md)

## 其他资料

- [《开源分布式图数据库 Nebula
Graph 完全指南》](https://docs.nebula-graph.com.cn/site/pdf/NebulaGraph-book.pdf)
- [发布说明](20.appendix/release-notes.md)
- [论坛](https://discuss.nebula-graph.com.cn/)
- [项目主页](https://nebula-graph.com.cn/)
- [系列视频](https://space.bilibili.com/472621355)
- [英文文档](https://docs.nebula-graph.io/)

## 图例说明

<!-- 
本文有 40+ 个 caution。
本文有 30+ 个 danger。
本文有 80+ 个 compatibility 和兼容性提示。
-->

!!! note

    额外的信息或者操作相关的提醒等。

!!! caution

    需要严格遵守的注意事项。不遵守 caution 可能导致系统故障、数据丢失、安全问题等。

!!! danger

    会引发危险的事项。不遵守 danger 必定会导致系统故障、数据丢失、安全问题等。

!!! performance

    性能调优时需要注意的事项。

!!! faq

    常见问题。

!!! compatibility

    nGQL 与 openCypher 的兼容性或 nGQL 当前版本与历史版本的兼容性。

!!! enterpriseonly

    描述社区版和企业版的差异。
    
## 修改文档中的错误
 
Nebula Graph 文档以 Markdown 语言编写。单击文档标题右上侧的铅笔图标即可提交修改建议。
