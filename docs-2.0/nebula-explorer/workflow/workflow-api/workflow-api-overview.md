# 工作流 API 概览

Nebula Explorer 提供 API 接口使用工作流的部分功能。

当前支持的 API 接口如下：

- [新增作业](api-post-jobs.md)
- [获取所有作业列表](api-get-jobs.md)
- [获取指定工作流的作业列表](api-get-workflow-jobs.md)
- [查询指定作业详情](api-desc-job.md)
- [取消作业运行](api-cancel-job.md)
- [获取指定任务的运行结果数据](api-desc-task.md)

## 请求方式

支持使用 curl 调用 API 接口实现对应的功能。

格式如下：

```bash
curl <options> http://<explorer_address>:<explorer_port>/<api_path>?{<body>}
```

- `<options>`：curl 支持大量选项，工作流使用较多的是`-X`、`-H`、`-d`。关于选项的详细说明，参见 [curl 官方文档](https://curl.se/docs/manpage.html)。

- `<explorer_address>`：Nebula Explorer 访问地址。

- `<explorer_port>`：Nebula Explorer 访问端口。

- `<api_path>`：API 的调用路径。例如`api-open/v1/jobs`。

- `<body>`：调用 API 时传入的 Body 参数。

## 获取授权 Token

使用 API 时，需要做 Token 信息校验。请使用如下命令获取 Token 信息。

```bash
curl -i -X POST -H "Content-Type: application/json" -H "Authorization: Bearer <account_base64_encode>" -d '{"address":"<nebula_address>","port":<nebula_port>}' http://<explorer_address>:<explorer_port>/api-open/v1/connect
```

- `<account_base64_encode>`：Base64 编码后的 Nebula Graph 账号和密码。编码前格式为`账号:密码`，下文示例为`root:123`，编码后为`cm9vdDoxMjM=`。
- `<nebula_address>`：Nebula Graph 访问地址。
- `<nebula_port>`：Nebula Graph 访问端口。
- `<explorer_address>`：Nebula Explorer 访问地址。
- `<explorer_port>`：Nebula Explorer 访问端口。

示例：

```bash
curl -i -X POST -H "Content-Type: application/json" -H "Authorization: Bearer cm9vdDoxMjM=" -d '{"address":"192.168.8.111","port":9669}' http://192.168.8.145:7002/api-open/v1/connect
```

返回结果：

```http
HTTP/1.1 200 OK
Content-Type: application/json
Set-Cookie: explorer_token=eyJhbxxx; Path=/; # Max-Age=259200; HttpOnly
Traceparent: 00-1c3f55cdbf81e13a2331ed88155ce0bf-2b97474943563f20-# 00
Date: Thu, 14 Jul 2022 06:47:01 GMT
Content-Length: 54

{
  "code": 0,
  "data": {
    "success": true
  },
  "message": "Success"
}
```

需要关注的参数如下：

- `explorer_token`：Token 信息。

- `Max-Age`：Token 有效时间。单位：秒。默认为 259200 秒，即 3 天。可以在安装目录内的`config/app-config.yaml`文件内修改默认有效时间。

## 请求结果

- API 如果调用成功，会返回如下信息：

  ```http
  {
    code: 0,
    message: 'Success',
    data: <ResponseData> //根据接口返回相应结果。
  }
  ```

- API如果调用失败，会返回对应的通用错误码，例如：

  ```http
  {
    code: 40004000,
    message: '<ErrBadRequest>',  //返回具体报错信息。
  }
  ```

  通用错误码的说明参见下文。

### 通用错误码

|错误码|信息|说明|
|:---|:---|:---|
|40004000 | `ErrBadRequest`  |  请求异常 |
|40004001 | `ErrParam`  | 请求参数异常  |
|40104000 | `ErrUnauthorized`  | 请求未授权  |
|40104001 | `ErrSession`  | 登录会话异常  |
|40304000 | `ErrForbidden`  | 请求被拒绝  |
|40404000 | `ErrNotFound`  | 请求资源不存在  |
|50004000 | `ErrInternalServer`  | 内部服务异常  |
|50004001 | `ErrInternalDatabase`  | 数据库异常  |
|50004002 | `ErrInternalController`  | 控制器异常  |
|50004003 | `ErrInternalLicense`  | 证书校验异常  |
|90004000 | `ErrUnknown`  | 未知错误  |

### 作业/任务状态码

|状态码|说明|
|:---|:---|
|0  | 准备中|
|1  | 执行中|
|2  | 执行成功|
|3  | 执行失败|
|4  | 已中断|
|5  | 暂停中|
