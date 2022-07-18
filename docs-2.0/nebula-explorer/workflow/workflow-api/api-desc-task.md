# 获取指定任务的运行结果

本文介绍如何使用工作流的 API 获取指定任务的运行结果。

## API 路径

`api-open/v1/jobs/<job_id>/tasks/<task_id>/sample_result`

- `<job_id>`：作业 ID。参见下文的请求参数。

- `<task_id>`：任务 ID。参见下文的请求参数。

## 请求参数

### 路径参数

|参数|类型|是否必填|默认值|示例|说明|
|:---|:---|:---|:---|:---|:---|
|`job_id`|number|必填|-|`29987`|作业 ID。可以通过 API [获取所有作业列表](api-get-jobs.md)查询，或者在作业列表页面查看。|
|`task_id`|number|必填|-|`8c171f70fb6f11ecac7e6da0662c195b`|任务 ID。可以通过 API [查询指定作业详情](api-desc-job.md)查询，或者在指定作业页面单击组件，在右上角查看。|

### Headers 参数

|参数|类型|是否必填|默认值|示例|说明|
|:---|:---|:---|:---|:---|:---|
|`Content-Type`|string|必填|-|`application/x-www-form-urlencoded`|内容类型。|
|`explorer_token`|string|必填|-|`eyJhbxxx`|授权 Token，用于验证账号信息。如何获取授权 Token 请参见[工作流 API 概览](workflow-api-overview.md)。|

### Body 参数

|参数|类型|是否必填|默认值|示例|说明|
|:---|:---|:---|:---|:---|:---|
|`limit`|number|必填|`10`|-|返回结果行数限制。|

### 请求示例

```bash
curl -i -X GET -H "Content-Type: application/x-www-form-urlencoded" -H "Cookie: "explorer_token=eyJhbxxx"" http://192.168.8.145:7002/api-open/v1/jobs/29987/tasks/8c171f70fb6f11ecac7e6da0662c195b/sample_result?limit=1000
```

## 返回参数

|参数|类型|示例|说明|
|:---|:---|:---|:---|
|`code`                      | number | `0`       | 请求结果码。请求成功返回`0`，请求不成功返回对应的错误码。详情参见[工作流 API 概览](workflow-api-overview.md)。             |
|`message`                   | string | `Success` | 执行结果信息。 |
|`data`                       | object | -        | 返回的数据列表。 |
|&nbsp;&nbsp;&nbsp; - `items`|list|-|详细结果列表。|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - `result`         | string   | `"player110","0.150000"` | 根据算法不同，结果可能是 2 列或 3 列。|

### 返回示例

```http
{
  "cookie": [],
  "Content-Type": "application/json",
  "Traceparent": "00-14047b04b6810be06be22e010f500506-4c310a844b824a7f-00",
  "Date": "Fri, 15 Jul 2022 09:36:56 GMT",
  "Content-Length": "2014"
}
{
  "code": 0,
  "data": {
    "items": [
      [
        "player110",
        "0.150000"
      ],
      [
        "team219",
        "0.452126"
      ],
      ......
      [
        "player121",
        "0.262148"
      ]
    ]
  },
  "message": "Success"
}
```
