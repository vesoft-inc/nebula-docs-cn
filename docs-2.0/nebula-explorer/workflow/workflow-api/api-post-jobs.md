# 新增作业

本文介绍如何使用工作流的 API 新增作业。

## 请求参数

### 路径参数

- `workflow_id`：必填。数据类型为 string。表示工作流 ID。需要指定工作流将其实例化为作业。

### Headers 参数

- `Content-Type`：必填。表示内容类型。取值为`application/json`。

- `explorer_token`：必填。用于验证登录状态。需要登录 Explorer 在 xx 页面查看。

### Body 参数

- `input`：可选。数据类型为 object。表示包含的传入参数。

  - `task_id_param`：必选。数据类型为 object。表示任务 ID。一个任务可以设置多个由键值对表示的任务参数。

    - `param_name: param_value`：必选。`param_name`为参数的键，即参数名。数据类型为 string。`value`为参数的值。数据类型为 string 或 number。

### 请求示例

```http
https://192.168.10.100:7002/api-analytics/jobs?filter={"workflow_id":"3992429968"}
```

## 返回参数

- `code`：可选。数据类型为 number。请求成功时为`200`，错误时返回对应的通用错误码。详情参见[工作流 API 概览](workflow-api-overview.md)。

- `data`：可选。数据类型为 object。表示返回的数据。

  - `id`：可选。数据类型为 string。表示新增作业的 ID。

### 返回示例

```http

```