# 使用限制

本文描述使用 Studio 的限制。

## 系统架构

Studio 目前仅支持 x86_64 架构。

## 数据上传

Studio 上传数据仅支持上传无表头的 CSV 文件，但是，单个文件大小及保存时间不受限制，而且数据总量以本地存储容量为准。

## 数据备份

目前仅支持在 **控制台** 上以 CSV 格式导出查询结果，不支持其他数据备份方式。

## nGQL 支持

除以下内容外，用户可以在 **控制台** 上执行所有 nGQL 语句：

- `USE <space_name>`：只能在 **Space** 下拉列表中选择图空间，不能运行这个语句选择图空间。
- **控制台** 上使用 nGQL 语句时，用户可以直接回车换行，不能使用换行符。

<!-- 
使用云服务版 Studio 时，除以上限制外，用户也不能在 **控制台** 上执行用户管理和角色管理相关的语句，包括：

- `CREATE USER`
- `ALTER USER`
- `CHANGE PASSWORD`
- `DROP USER`
- `GRANT ROLE`
- `REVOKE ROLE`  

-->

关于语句的详细信息，参考[用户管理](../../7.data-security/1.authentication/2.management-user.md "点击前往用户管理")。

## 浏览器支持

建议使用最新版本的 Chrome 访问 Studio。
