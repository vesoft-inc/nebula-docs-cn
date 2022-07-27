# 新增作业

本文介绍如何使用工作流的 API 新增作业。

## API 路径

`api-open/v1/workflows/<workflow_id>/jobs`

`<workflow_id>`：工作流 ID。参见下文的请求参数。

## 请求参数

### 路径参数

|参数|类型|是否必填|默认值|示例|说明|
|:---|:---|:---|:---|:---|:---|
|`workflow_id`|number|必填|-|`4216617528`|工作流 ID。需要指定工作流将其实例化为作业。可以在指定的工作流页面左上角查看 ID。|

### Headers 参数

|参数|类型|是否必填|默认值|示例|说明|
|:---|:---|:---|:---|:---|:---|
|`Content-Type`|string|必填|-|`application/json`|内容类型。|
|`explorer_token`|string|必填|-|`eyJhbxxx`|授权 Token，用于验证账号信息。如何获取授权 Token 请参见[工作流 API 概览](workflow-api-overview.md)。|

### Body 参数

!!! note

    自定义的传入参数需要用户自行保证参数的合理性和正确性，否则作业会执行失败。

|参数|类型|是否必填|默认值|示例|说明|
|:---|:---|:---|:---|:---|:---|
|`input`|object|可选|-|-| 自定义的传入参数。|
|&nbsp;&nbsp;&nbsp;- `task_id`|object|可选|-|`query_1`|任务 ID。可以在组件设置页面右上角查看。一个任务可以设置多个由键值对表示的参数。|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- `param_name: param_value`|string: {string 或 number}|可选|-|`param0: player100`|`param_name`为参数的键，即参数名。`param_value`为参数的值。|

### 请求示例

以下图为例，在 nGQL 语句使用自定义参数`name`。在创建作业时传入参数值`Tim Duncan`。

![api-postjob](https://docs-cdn.nebula-graph.com.cn/figures/api-postjob-220715-cn.png)

```bash
curl -i -X POST -H "Content-Type: application/json" -H "Cookie: "explorer_token=eyJhbxxx"" -d '{"input":{"query_1":{"name":"Tim Duncan"}}}' http://192.168.8.145:7002/api-open/v1/workflows/4216617528/jobs
```

## 返回参数

|参数|类型|示例|说明|
|:---|:---|:---|:---|
|`code`    | number | `0`       |  请求结果码。请求成功返回`0`，请求不成功返回对应的错误码。详情参见[工作流 API 概览](workflow-api-overview.md)。            |
|`message`   | string | `Success` | 执行结果信息。 |
|`data`    | object | -        | 返回的数据列表。 |
|&nbsp;&nbsp;&nbsp;- `id`|string|`107`|新增作业的 ID。|

### 返回示例

```http
{
  "cookie": [],
  "Content-Type": "application/json",
  "Traceparent": "00-1ba128615cdc2226c921973a689e9f1b-7630b12963494672-00",
  "Date": "Fri, 15 Jul 2022 07:19:25 GMT",
  "Content-Length": "48"
}

{
  "code": 0,
  "data": {
    "id": 107
  },
  "message": "Success"
}
```
