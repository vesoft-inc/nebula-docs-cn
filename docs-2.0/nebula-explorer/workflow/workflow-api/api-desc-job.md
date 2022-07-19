# 查询指定作业详情

本文介绍如何使用工作流的 API 查询指定作业详情。

## API 路径

`api-open/v1/jobs/<job_id>`

`<job_id>`：作业 ID。参见下文的请求参数。

## 请求参数

### 路径参数

|参数|类型|是否必填|默认值|示例|说明|
|:---|:---|:---|:---|:---|:---|
|`job_id`|number|必填|-|`1964`|作业 ID。可以通过 API [获取所有作业列表](api-get-jobs.md)查询，或者在作业列表页面查看。|

### Headers 参数

|参数|类型|是否必填|默认值|示例|说明|
|:---|:---|:---|:---|:---|:---|
|`Content-Type`|string|必填|-|`application/json`|内容类型。|
|`explorer_token`|string|必填|-|`eyJhbxxx`|授权 Token，用于验证账号信息。如何获取授权 Token 请参见[工作流 API 概览](workflow-api-overview.md)。|

### Body 参数

无。

### 请求示例

```bash
curl -i -X GET -H "Content-Type: application/json" -H "Cookie: "explorer_token=eyJhbxxx"" http://192.168.8.145:7002/api-open/v1/jobs/1964
```

## 返回参数

|参数|类型|示例|说明|
|:---|:---|:---|:---|
|`code`                      | number | `0`       | 请求结果码。请求成功返回`0`，请求不成功返回对应的错误码。详情参见[工作流 API 概览](workflow-api-overview.md)。             |
|`message`                   | string | `Success` | 执行结果信息。 |
|`data`                       | object | -        | 返回的数据列表。 |
|&nbsp;&nbsp;&nbsp; - `id`         | number   | `1964` | 作业 ID。|
|&nbsp;&nbsp;&nbsp; - `name`       | string   | `workflow_xkkjf_20220712103332` | 作业名称。 |
|&nbsp;&nbsp;&nbsp; - `workflowId` | string   | `3992429968` | 工作流 ID。 |
|&nbsp;&nbsp;&nbsp; - `workflowName` | string | `workflow_xkkjf` | 工作流名称。 |
|&nbsp;&nbsp;&nbsp; - `status`      | number  | `2`  | 作业状态码。详情参见[工作流 API 概览](workflow-api-overview.md)。 |
|&nbsp;&nbsp;&nbsp; - `tasks`      | object | -| 任务详情。 |  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - `id`      | string | `f93dea90fc3a11ecac7e6da0662c195b`| 任务 ID。 |  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - `name`      | string | `BFS`| 任务名称。 |  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - `runBeginTime` | datetime | `2022-07-12T10:33:35+08:00` | 任务开始执行时间。 |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - `runEndTime` | datetime | `2022-07-12T10:33:38+08:00` | 任务执行结束时间。 |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - `status` | number  | `2`  | 任务状态码。详情参见[工作流 API 概览](workflow-api-overview.md)。 |

### 返回示例

```http
{
  "cookie": [],
  "Content-Type": "application/json",
  "Traceparent": "00-3db17c9fd9e0a4c3824973471523d214-4384705e523dce83-00",
  "Date": "Fri, 15 Jul 2022 09:08:20 GMT",
  "Content-Length": "400"
}
{
  "code": 0,
  "data": {
    "id": 1964,
    "name": "workflow_xkkjf_20220712103332",
    "workflowId": "3992429968",
    "workflowName": "workflow_xkkjf",
    "status": 2,
    "tasks": [
      {
        "id": "f93dea90fc3a11ecac7e6da0662c195b",
        "name": "BFS",
        "runBeginTime": "2022-07-12T10:33:35+08:00",
        "runEndTime": "2022-07-12T10:33:38+08:00",
        "status": 2
      }
    ],
    "runBeginTime": 1657593215000,
    "runEndTime": 1657593218000,
    "createTime": 1657593212505
  },
  "message": "Success"
}
```