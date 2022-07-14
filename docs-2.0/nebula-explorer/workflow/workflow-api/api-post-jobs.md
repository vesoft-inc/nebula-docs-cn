# 新增作业

本文介绍如何使用工作流的 API 新增作业。

## 请求参数

### 路径参数

|参数|类型|是否必填|说明|
|:---|:---|:---|:---|
|`workflow_id`|string|必填|工作流 ID。需要指定工作流将其实例化为作业。|

### Headers 参数

|参数|类型|是否必填|说明|
|:---|:---|:---|:---|
|`Content-Type`|-|必填|内容类型。取值为`application/json`。|
|`explorer_token`|-|必填|授权 Token，用于验证账号信息。如何获取授权 Token 请参见[工作流 API 概览](workflow-api-overview.md)。|

### Body 参数

|参数|类型|是否必填|说明|
|:---|:---|:---|:---|
|`input`|object|可选|传入参数。|
|&nbsp;&nbsp;&nbsp;- `task_id_param`|object|必选|任务 ID。一个任务可以设置多个由键值对表示的任务参数。|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- `param_name: param_value`|string: {string 或 number}|必选|`param_name`为参数的键，即参数名。`param_value`为参数的值。|

### 请求示例

```http
curl -i -X POST -H "Content-Type: application/json" -H "Cookie: "explorer_token=eyJhbxxx"" -d '{"address":"192.168.8.111","port":9669}' http://192.168.8.145:7002/api-open/v1/workflows/3533497370/jobs?{}
```

## 返回参数

- `code`：可选。数据类型为 number。请求成功时为`200`，错误时返回对应的通用错误码。详情参见[工作流 API 概览](workflow-api-overview.md)。

- `data`：可选。数据类型为 object。表示返回的数据。

  - `id`：可选。数据类型为 string。表示新增作业的 ID。

### 返回示例

```http
HTTP/1.1 200 OK
Content-Type: application/json
Traceparent: 00-95b90aa422f0c31da371d428b55b1872-a2230a276d6a6814-00
Date: Thu, 14 Jul 2022 08:41:27 GMT
Content-Length: 48

{"code":0,
"data":{
  "id":103},
"message":"Success"}
```
