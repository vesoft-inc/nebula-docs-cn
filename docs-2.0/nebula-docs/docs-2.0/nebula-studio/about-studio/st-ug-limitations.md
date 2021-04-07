# 限制

本文介绍Studio 2.0.0的限制。

## Nebula Graph版本

仅支持Nebula Graph 2.0.0，其他2.x版本可能会有未知问题。

<!--
如果您使用Nebula Graph 1.x，请使用Studio 1.x。详情请参见[Studio v1.x User Guide](https://docs.nebula-graph.io/1.1/nebula-studio/about-studio/st-ug-what-is-graph-studio/)。
-->

## 架构

目前Studio 2.0.0仅支持x86_64架构。

## 上传数据

只有以逗号分隔且没有列名的`.CSV`格式文件才能上传，对于单个文件的大小和存储周期没有限制。最大数据量取决于您机器的存储空间。

## 数据备份

您可以在控制台页面将查询结果导出为`.CSV`格式文件。

## nGQL语句

在Studio 2.0.0中，几乎支持所有nGQL语法，除了以下几点：

- `USE <space_name>`：不能在Studio中执行`USE`语句选择图空间。如果需要选择图空间，请在左上角的**当前图空间**下拉菜单中选择。

- 换行符（\\）：不能在Studio中使用换行符。如果需要换行，请使用`Enter`键换行。

## 浏览器

建议您使用最新版本的Chrome浏览器访问Studio 2.0.0。