# 欢迎阅读{{nebula.name}} {{ nebula.release }} 文档

!!! Note
    
    本文档更新时间{{ now().year }}-{{ now().month }}-{{ now().day }}，GitHub commit [{{ git.short_commit }}](https://github.com/vesoft-inc/nebula-docs/commits/v{{nebula.release}})。该版本主色系为"胶蓝"，色号为 #66CCFF。

<!--
!!! caution

    该版本文档仅包括 {{nebula.name}} {{ nebula.release }} 社区版内容和对应版本的周边工具内容。{{nebula.name}} {{ nebula.release }} 未发布企业版（[企业版发布周期通常为 6 个月](20.appendix/6.eco-tool-version.md)）。详情查看[版本发布说明](20.appendix/release-notes/nebula-comm-release-note.md)。


!!! Compatibility

    在 NebulaGraph 3.2 的版本中，允许存在无 Tag 的点，但从 NebulaGraph 3.3.0 开始默认不支持无 Tag 的点。
    
NebulaGraph 是一款开源的、分布式的、易扩展的原生图数据库，能够承载数千亿个点和数万亿条边的超大规模数据集，并且提供毫秒级查询。


<a href="https://www.bilibili.com/video/BV12R4y1e7U7"><img src="https://docs-cdn.nebula-graph.com.cn/figures/picture1.png" alt="3.4.0发布"></a>
-->

## 快速开始

* [快速开始](2.quick-start/1.quick-start-overview.md)
* [部署要求](4.deployment-and-installation/1.resource-preparations.md)
* [nGQL 命令汇总](2.quick-start/6.cheatsheet-for-ngql-command.md)
* [FAQ](20.appendix/0.FAQ.md)
* [生态工具](20.appendix/6.eco-tool-version.md)
* [Academy 课程](https://academic.nebula-graph.io/intro/)

## 最新发布

{{comm.comm_begin}}
- [{{nebula.name}} {{nebula.release}}](20.appendix/release-notes/nebula-comm-release-note.md)
- [Studio](20.appendix/release-notes/studio-release-note.md)
- [Dashboard](20.appendix/release-notes/dashboard-comm-release-note.md)
{{comm.comm_end}}

{{ent.ent_begin}}
- [{{nebula.name}} {{nebula.release}}](20.appendix/release-notes/nebula-ent-release-note.md)
- [Dashboard](20.appendix/release-notes/dashboard-ent-release-note.md)
- [Explorer](20.appendix/release-notes/explorer-release-note.md)
{{ent.ent_end}}


## 其他资料

- [学习路径](https://academic.nebula-graph.io/?lang=ZH_CN)
   {{ comm.comm_begin }}
- [引用 NebulaGraph](https://arxiv.org/abs/2206.07278)
- [论坛](https://discuss.nebula-graph.com.cn/)
- [主页](https://nebula-graph.com.cn/)
- [系列视频](https://space.bilibili.com/472621355)
- [英文文档](https://docs.nebula-graph.io/)
   {{ comm.comm_end }}
   {{ ent.ent_begin }}
- [主页](https://yueshu.com.cn/)
   {{ ent.ent_end }}


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
 
{{nebula.name}}文档以 Markdown 语言编写。单击文档标题右上侧的铅笔图标即可提交修改建议。
