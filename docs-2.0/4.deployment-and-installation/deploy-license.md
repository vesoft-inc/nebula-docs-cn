# 设置企业版License

Nebula Graph企业版需要设置License才可以正常启动并使用企业版功能，本文介绍如何设置企业版的License文件。

!!! enterpriseonly

    License是为企业版用户提供的软件授权证书，企业版用户可以发送邮件至`inquiry@vesoft.com`申请License文件。

## 注意事项

- 没有设置License时，Nebula Graph企业版无法启动。

- 请勿修改文件，否则会导致License失效。

- License过期后，将无法执行任何操作。请及时发送邮件至`inquiry@vesoft.com`申请续期。

## License说明

用户可以用`cat`等命令查看License文件内容，示例文件如下：

```bash
----------License Content Start----------
{
  "vendor": "Vesoft_Inc",
  "organization": "doc",
  "issuedDate": "2021-11-07T16:00:00.000Z",
  "expirationDate": "2021-11-30T15:59:59.000Z",
  "product": "nebula_graph",
  "version": ">2.6.1",
  "licenseType": "enterprise"
}
----------License Content End----------

----------License Key Start----------
cofFcOxxxxxxxxxxxxxhnZgaxrQ==
----------License Key End----------
```

License文件包含生效时间、过期时间等信息。说明如下。

|参数|说明|
|:---|:---|
|`vendor`|发放渠道。|
|`organization`|用户名称。|
|`issuedDate`|License生效时间。|
|`expirationDate`|License过期时间。|
|`product`|产品类型。Nebula Graph的产品类型为`nebula_graph`。|
|`version`|版本支持的信息。|
|`licenseType`|License类型。包括`enterprise`、`samll_bussiness`、`pro`、`individual`。|

## 设置License

1. 安装Nebula Graph企业版。

2. 申请License文件。

3. 将License文件上传到所有包含Meta服务的机器上，路径为安装目录的`share/resources/`内。

  !!! note

        周边工具的License文件上传位置，请参见具体工具的说明文档。
