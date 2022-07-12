# 工作流 API 概览

Nebula Explorer 提供 API 接口使用工作流的部分功能。

当前支持的 API 接口如下：

- 新增作业。
- 获取所有作业列表。
- 查询指定作业详情。
- 取消作业运行。
- 获取指定任务的运行结果数据。

## 请求方式

在 URL 中指定 API 和请求参数，从而实现对应的功能。请求参数包含路径参数、Headers 参数和 Body 参数。

示例如下：

```http

```

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

### 任务状态码

|状态码|说明|
|:---|:---|
|0  | 准备中|
|1  | 执行中|
|2  | 执行成功|
|3  | 执行失败|
|4  | 已中断|
|5  | 暂停中|
