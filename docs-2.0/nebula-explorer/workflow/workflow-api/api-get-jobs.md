# 获取所有作业列表

本文介绍如何使用工作流的 API 获取所有作业列表。

## 请求参数

### 路径参数

无。

### Headers 参数

- `Content-Type`：必填。表示内容类型。取值为`application/json`。

- `explorer_token`：必填。用于验证登录状态。需要登录 Explorer 在 xx 页面查看。

### Body 参数

- `filter`：可选。数据类型为 object。表示过滤器的设置。

  - `name`：可选。数据类型为 string。

  - `status`：可选。数据类型为 number。表示任务状态码。详情参见[工作流 API 概览](workflow-api-overview.md)。

  - `fromCreateTime`：可选。数据类型为 number。

  - `toCreateTime`：可选。数据类型为 number。

  - `orderByCreateTime`：可选。数据类型为 string。

- `pageSize`：

- `page`：




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

  - total

  - page

  - pageSize

  - items

    - id
    - name
    - workflowName
    - workflowId
    - status
    - runBeginTime
    - runEndTime
    - createTime


- `code`：可选。数据类型为 number。请求成功时为`200`，错误时返回对应的通用错误码。详情参见[工作流 API 概览](workflow-api-overview.md)。

- `data`：可选。数据类型为 object。表示返回的数据。

  - `id`：可选。数据类型为 string。表示新增作业的 ID。

### 返回示例

```http
{"code":0,
"data":{
  "items":[{
    "id":782,
    "name":"workflow_tg4s9_20220705150339",
    "flowId":"3821817867",
    "flowHistoryId":274,
    "flowVersion":1,
    "flowName":"workflow_tg4s9",
    "schema":"",
    "status":2,
    "ctlJobId":28451,
    "tasks":[{
      "id":"8f1c2960fc3011ecac7e6da0662c195b",
      "name":"KCore",
      "runBeginTime":"2022-07-05T15:03:42+08:00",
      "runEndTime":"2022-07-05T15:03:44+08:00",
      "status":2}],
    "runBeginTime":1657004622000,
    "runEndTime":0,
    "createTime":1657004619499,
    "updateTime":1657004625700}],
    "total":1,
    "page":1,
    "pageSize":10},
"message":"Success"}
```