# 使用限制

本文描述了在使用 Studio 时可能会受到的限制。

## Nebula Graph 版本支持

目前 Studio v1.x 仅支持 Nebula Graph v1.x，Studio v2.x 仅支持 Nebula Graph v2.x。

## 系统架构

Docker 版和 RPM 版 Studio 目前仅支持 x86_64 架构。

## 数据上传

<!--
使用云服务版 Studio 上传数据有以下限制：

- 目前仅支持上传没有表头行的 CSV 文件，而且仅支持英文逗号（,）作为分隔符。
- 单个文件不得超过 100 MB。
- 单个实例上传文件总量不得超过 1 GB。
- 单个文件仅能保存 1 天。

-->

使用 Docker 版和 RPM 版 Studio 上传数据也仅支持上传无表头的 CSV 文件，但是，单个文件大小及保存时间不受限制，而且，数据总量以本地存储容量为准。

## 数据备份

目前仅支持在 **控制台** 上以 CSV 格式导出查询结果，不支持其他数据备份方式。

## nGQL 支持

使用 Docker 版 Studio 时，除以下内容外，用户可以在 **控制台** 上执行所有 nGQL 语句：

- `USE <space_name>`：只能在 **Space** 下拉列表中选择图空间，不能运行这个语句选择图空间。
- **控制台** 上使用 nGQL 语句时，用户可以直接回车换行，不能使用换行符。

使用云服务版 Studio 时，除以上限制外，用户也不能在 **控制台** 上执行用户管理和角色管理相关的语句，包括：

- `CREATE USER`
- `ALTER USER`
- `CHANGE PASSWORD`
- `DROP USER`
- `GRANT ROLE`
- `REVOKE ROLE`  

关于语句的详细信息，参考 [Nebula Graph 用户手册](../../7.data-security/1.authentication/2.management-user.md "点击前往 Nebula Graph 用户手册")。

## 浏览器支持

建议使用最新版本的 Chrome 访问 Studio。
