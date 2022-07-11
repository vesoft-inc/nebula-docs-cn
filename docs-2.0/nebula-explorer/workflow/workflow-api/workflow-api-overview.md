# 工作流 API 概览

Nebula Explorer 提供 API 接口使用工作流的部分功能。API 接口说明如下。

|接口|说明|
|:--|:--|
|get_workflow_jobs|查看指定 workflow 的作业列表。|
|post_jobs|创建作业。|
|get_jobs|获取所有作业列表。|
|get_job_id|获取指定作业详情。|
|post_job_cancel|取消作业运行。|
|get_task_id|获取指定任务的运行结果数据。|

## 请求结果

- API 如果调用成功，会返回如下信息：

  ```http
  {
    code: 200,
    message: 'success',
    data: ResponseData
  }
  ```

- API如果调用失败，会返回对应的通用错误码，例如：

  ```http
  {
    code: 40004000,
    message: 'ErrBadRequest',
  }
  ```

  通用错误码的说明参见下文。

### 通用错误码

|错误码|信息|说明|
|:---|:---|:---|
|40004000 | `ErrBadRequest`  |  请求错误。 |
|40004001 | `ErrParam`  | 参数错误。  |
|40104000 | `ErrUnauthorized`  | 认证失败。  |
|40104001 | `ErrSession`  |   |
|40304000 | `ErrForbidden`  |   |
|40404000 | `ErrNotFound`  |   |
|50004000 | `ErrInternalServer`  |   |
|50004001 | `ErrInternalDatabase`  |   |
|50004002 | `ErrInternalController`  |   |
|50004003 | `ErrInternalLicense`  |   |
|50104000 | `ErrNotImplemented`  |   |
|90004000 | `ErrUnknown`  | 未知错误  |

## 公共请求参数

|参数 |类型 |是否必须 |说明 |
|:---|:--- |:---   |:---|
| explorer_token |  | 是 | 登录状态校验。登录 Explorer 在xxx页面获取。  |
| version |  |  | Explorer 版本。 |
|  |  |  |  |

## API 示例

- 请求示例

```http
https://192.168.10.100:7002/api-analytics/jobs?page=1&pageSize=10&filter={}
```

- 返回示例