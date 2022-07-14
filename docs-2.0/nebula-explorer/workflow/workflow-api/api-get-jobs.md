# 获取所有作业列表

本文介绍如何使用工作流的 API 获取所有作业列表。

## 请求参数

### 路径参数

无。

### Headers 参数

|参数|类型|是否必填|说明|
|:---|:---|:---|:---|
|`Content-Type`|-|必填|内容类型。取值为`application/json`。|
|`explorer_token`|-|必填|授权 Token，用于验证账号信息。如何获取授权 Token 请参见[工作流 API 概览](workflow-api-overview.md)。|

### Body 参数

|参数|类型|是否必填|说明|
|:---|:---|:---|:---|
|`filter` | object| 可选| 过滤器的设置。|
|&nbsp;&nbsp;&nbsp;- `name` |string |可选 | |
|&nbsp;&nbsp;&nbsp;- `status` |number |可选 | 任务状态码。详情参见[工作流 API 概览](workflow-api-overview.md)。|
|&nbsp;&nbsp;&nbsp;- `fromCreateTime` | number| 可选| |
|&nbsp;&nbsp;&nbsp;- `toCreateTime` |number |可选 | |
|&nbsp;&nbsp;&nbsp;- `orderByCreateTime` | string| 可选| |
|`pageSize` | | | |
|`page` | | | |


### 请求示例

```http
curl -i -X GET -H "Content-Type: application/json" -H "Cookie: "explorer_token=eyJhbxxx"" http://192.168.8.145:7002/api-open/v1/jobs?{}
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
HTTP/1.1 200 OK
Content-Type: application/json
Traceparent: 00-e3d4c3f9f35c2c0a63d600a5194cda5b-5ee2fe62ec604dfe-00
Date: Thu, 14 Jul 2022 09:29:59 GMT
Content-Length: 621

{"code":0,
"data":{
  "items":[
    {"id":102,
    "name":"workflow_qoutm_20220714163750",
    "workflowId":"3533497370",
    "workflowName":"workflow_qoutm",
    "status":2,
    "tasks":null,
    "runBeginTime":1657787872000,
    "runEndTime":1657787875000,
    "createTime":1657787870010},
    {"id":101,
    "name":"workflow_qoutm_20220714162311",
    "workflowId":"3533497370",
    "workflowName":"workflow_qoutm",
    "status":2,
    "tasks":null,
    "runBeginTime":1657786993000,
    "runEndTime":1657786996000,
    "createTime":1657786991455}
    ],
  "total":4,
  "Page":1,
  "PageSize":10},
"message":"Success"}
```