# 设置企业版 License

Nebula Graph 企业版需要用户设置 License 才可以正常启动并使用企业版功能，本文介绍如何设置企业版的 License 文件。

!!! enterpriseonly

    License 是为企业版用户提供的软件授权证书，企业版用户可以发送邮件至`inquiry@vesoft.com`申请 License 文件。

## 注意事项

- 没有设置 License 时，Nebula Graph 企业版无法启动。

- 请勿修改 License 文件，否则会导致 License 失效。

- License 快过期时，请及时发送邮件至`inquiry@vesoft.com`申请续期。

- License 的过期缓冲为 3 天：

  - 过期 7 天前和过期当天，服务启动时会打印日志进行提醒。

  - 过期后仍可继续使用 3 天。

  - 过期 3 天后，服务无法启动，并会打印日志进行提醒。

## License 说明

用户可以用`cat`等命令查看 License 文件（`nebula.license`）内容，示例文件内容如下：

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

License 文件包含生效时间、过期时间等信息。说明如下。

|参数|说明|
|:---|:---|
|`vendor`|发放渠道。|
|`organization`|用户名称。|
|`issuedDate`|License 生效时间。|
|`expirationDate`|License 过期时间。|
|`product`|产品类型。Nebula Graph 的产品类型为`nebula_graph`。|
|`version`|版本支持的信息。|
|`licenseType`|License 类型。包括`enterprise`、`samll_bussiness`、`pro`、`individual`。预留参数。|

## 设置 License

1. 发送邮件至`inquiry@vesoft.com`申请 Nebula Graph 企业版安装包。

2. 安装 Nebula Graph 企业版。安装方式与社区版相同，请参见[使用 RPM 或 DEB 包安装 Nebula Graph](2.compile-and-install-nebula-graph/2.install-nebula-graph-by-rpm-or-deb.md)。

3. 发送邮件至`inquiry@vesoft.com`申请 License 文件`nebula.license`。

4. 将 License 文件上传到所有包含 Meta 服务的机器上，路径为每个 Meta 服务安装目录的`share/resources/`内。

  !!! note

        周边工具的 License 文件上传位置，请参见[具体周边工具](../20.appendix/6.eco-tool-version.md)的说明文档。
