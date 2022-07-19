# 终止执行指定作业

本文介绍如何使用工作流的 API 终止执行指定作业。

## API 路径

`api-open/v1/jobs/<job_id>/cancel`

`<job_id>`：作业 ID。参见下文的请求参数。

## 请求参数

### 路径参数

|参数|类型|是否必填|默认值|示例|说明|
|:---|:---|:---|:---|:---|:---|
|`job_id`|number|必填|-|`1964`|作业 ID。可以通过 API [获取所有作业列表](api-get-jobs.md)查询，或者在作业列表页面查看。|

### Headers 参数

|参数|类型|是否必填|默认值|示例|说明|
|:---|:---|:---|:---|:---|:---|
|`Content-Type`|string|必填|-|`application/x-www-form-urlencoded`|内容类型。|
|`explorer_token`|string|必填|-|`eyJhbxxx`|授权 Token，用于验证账号信息。如何获取授权 Token 请参见[工作流 API 概览](workflow-api-overview.md)。|

### Body 参数

无。

### 请求示例

```bash
curl -i -X PUT -H "Content-Type: application/x-www-form-urlencoded" -H "Cookie: "explorer_token=eyJhbxxx"" http://192.168.8.145:7002/api-open/v1/jobs/30600/cancel
```

## 返回参数

|参数|类型|示例|说明|
|:---|:---|:---|:---|
|`code`                      | number | `0`       | 请求结果码。请求成功返回`0`，请求不成功返回对应的错误码。详情参见[工作流 API 概览](workflow-api-overview.md)。            |
|`message`                   | string | `Success` | 执行结果信息。 |
|`data`                       | object | -        | 返回的数据列表。 |
|&nbsp;&nbsp;&nbsp; - `success`         | bool   | `true` | 是否成功终止。|

### 返回示例

```http
{
  "cookie": [],
  "Content-Type": "application/json",
  "Traceparent": "00-8b4b47413a211d9b5e0839aadc712052-4a98bae37fe5948a-00",
  "Date": "Mon, 18 Jul 2022 01:45:08 GMT",
  "Content-Length": "54"
}
{
  "code": 0,
  "data": {
    "success": true
  },
  "message": "Success"
}
```