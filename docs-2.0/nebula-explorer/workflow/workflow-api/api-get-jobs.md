# 获取所有作业列表

本文介绍如何使用工作流的 API 获取所有作业列表。

## API 路径

`api-open/v1/jobs`

## 请求参数

### 路径参数

无。

### Headers 参数

|参数|类型|是否必填|默认值|示例|说明|
|:---|:---|:---|:---|:---|:---|
|`Content-Type`|string|必填|-|`application/json`|内容类型。|
|`explorer_token`|string|必填|-|`eyJhbxxx`|授权 Token，用于验证账号信息。如何获取授权 Token 请参见[工作流 API 概览](workflow-api-overview.md)。|

### Body 参数

|参数|类型|是否必填|默认值|示例|说明|
|:---|:---|:---|:---|:---|:---|
|`filter` | object| 可选|-|-| 过滤器的设置。|
|&nbsp;&nbsp;&nbsp;- `name` |string |可选 |-|`workflow_q745a_20220715092236`| 作业名称。 |
|&nbsp;&nbsp;&nbsp;- `status` |number |可选 |-|`2`| 作业状态码。详情参见[工作流 API 概览](workflow-api-overview.md)。|
|&nbsp;&nbsp;&nbsp;- `fromCreateTime` | number| 可选|-|`1657848036000`| 起始时间戳。基于作业的创建时间进行过滤。|
|&nbsp;&nbsp;&nbsp;- `toCreateTime` |number |可选 |-|`1657848157000`|结束时间戳。基于作业的创建时间进行过滤。|
|&nbsp;&nbsp;&nbsp;- `orderByCreateTime` | string| 可选|`desc`|-| 排序方式。支持`desc`和`asc`。 |
|`pageSize` |number |可选| `10`| -| 每页记录数。|
|`page` |number |可选| `1`| -| 页码。|

### 请求示例

!!! note

    `jobs?`后的内容为 Body 参数，`filter`的内容是进过 URL 编码的结果。原始内容为：`{ "status": 2,  "orderByCreateTime": "asc"}`。

```bash
curl -i -X GET -H "Content-Type: application/json" -H "Cookie: "explorer_token=eyJhbxxx"" http://192.168.8.145:7002/api-open/v1/jobs?filter=%7B%20%22status%22%3A%202%2C%20%20%22orderByCreateTime%22%3A%20%22asc%22%7D&pageSize=10&page=1
```

## 返回参数

|参数|类型|示例|说明|
|:---|:---|:---|:---|
|`code`                      | number | `0`       | 请求结果码。请求成功返回`0`，请求不成功返回对应的错误码。详情参见[工作流 API 概览](workflow-api-overview.md)。             |
|`message`                   | string | `Success` | 执行结果信息。 |
|`data`                       | object | -        | 返回的数据列表。 |
|&nbsp;&nbsp;&nbsp;- `total`  | number | `2`      |记录总数。 |
|&nbsp;&nbsp;&nbsp;- `Page`   | number | `1`      | 页码。 |
|&nbsp;&nbsp;&nbsp;- `PageSize`  | number | `10`  | 每页记录数。 |
|&nbsp;&nbsp;&nbsp;- `items`     | object | -     | 记录详情列表。  |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - `id`         | number   | `105` | 作业 ID。|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - `name`       | string   | `workflow_q745a_20220715090915` | 作业名称。 |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - `workflowId` | string   | `4216617528` | 工作流 ID。 |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - `workflowName` | string | `workflow_q745a` | 工作流名称。 |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - `status`      | number  | `2`  | 作业状态码。详情参见[工作流 API 概览](workflow-api-overview.md)。 |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - `runBeginTime` | number | `1657847358000` | 作业开始执行时间。 |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - `runEndTime` | number | `1657847364000` | 作业执行结束时间。 |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - `createTime` | number  | `1657847355906`  | 作业创建时间。 |

### 返回示例

```http
{
  "cookie": [],
  "Content-Type": "application/json",
  "Traceparent": "00-d3a1943f5baf46771e9afc629e0b5d40-920db2f06142f5ff-00",
  "Date": "Fri, 15 Jul 2022 06:17:21 GMT",
  "Content-Length": "512"
}

{
  "code": 0,
  "data": {
    "items": [
      {
        "id": 105,
        "name": "workflow_q745a_20220715090915",
        "workflowId": "4216617528",
        "workflowName": "workflow_q745a",
        "status": 2,
        "runBeginTime": 1657847358000,
        "runEndTime": 1657847364000,
        "createTime": 1657847355906
      },
      {
        "id": 106,
        "name": "workflow_q745a_20220715092236",
        "workflowId": "4216617528",
        "workflowName": "workflow_q745a",
        "status": 2,
        "runBeginTime": 1657848157000,
        "runEndTime": 1657848163000,
        "createTime": 1657848156290
      }
    ],
    "total": 2,
    "Page": 1,
    "PageSize": 10
  },
  "message": "Success"
}
```