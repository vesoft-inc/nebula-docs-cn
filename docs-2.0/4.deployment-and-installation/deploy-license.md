# 设置 NebulaGraph 企业版 License

NebulaGraph 企业版需要用户设置 License 才可以正常启动并使用企业版功能，本文介绍如何设置企业版的 License 文件。

!!! enterpriseonly

    License 是为企业版用户提供的软件授权证书，企业版用户可以[联系我们](https://www.nebula-graph.com.cn/contact)申请 License 文件。

## 注意事项

- 没有设置 License 时，NebulaGraph 企业版无法启动。

- 请勿修改 License 文件，否则会导致 License 失效。

- License 快过期时，请[联系我们](https://www.nebula-graph.com.cn/contact)申请续期。

- License 的过期缓冲为 14 天：

  - 过期前 30 天和过期当天，服务启动时会打印日志进行提醒。

  - 过期后仍可继续使用 14 天。

  - 过期 14 天后，服务无法启动，并会打印日志进行提醒。

## NebulaGraph 企业版 License 说明

License 文件（`nebula.license`）内容示例如下：

```bash
----------License Content Start----------
{
  "vendor": "vesoft",
  "organization": "doc",
  "issuedDate": "2022-04-06T16:00:00.000Z",
  "expirationDate": "2022-05-31T15:59:59.000Z",
  "product": "nebula_graph",
  "version": ">3.0.0",
  "licenseType": "enterprise",
  "gracePeriod": 14,
  "graphdSpec": {
    "nodes": 3
  },
  "storagedSpec": {
    "nodes": 3
  },
  "clusterCode": "BAIAEAiAQAAG"
}
----------License Content End----------

----------License Key Start----------
cofFcOxxxxxxxxxxxxxhnZgaxrQ==
----------License Key End----------
```

License 文件包含生效时间、过期时间等信息。说明如下。

|参数|说明|
|:---|:---|
|`vendor`| 发放渠道。|
|`organization`| 用户名称。|
|`issuedDate`| License 生效时间。|
|`expirationDate`| License 过期时间。|
|`product`| 产品类型。NebulaGraph 的产品类型为`nebula_graph`。|
|`version`| 版本支持的信息。|
|`licenseType`| License 类型。包括`enterprise`、`samll_bussiness`、`pro`、`individual`。预留参数。|
|`gracePeriod`| 证书过期后可继续使用服务的缓冲时间（单位天），超过缓冲期后停止服务。试用版的 License 过期后无缓冲期，默认值为 0。 |
|`graphdSpec`| 集群中 Graph 服务的数量限制。NebulaGraph 会实时监测当前活动的 Graph 服务数量，超过限制的 Graph 服务无法连接集群。|
|`storagedSpec`| 集群中 Storage 服务的数量限制。NebulaGraph 会实时监测当前活动的 Storage 服务数量，超过限制的 Storage 服务无法连接集群。|
|`clusterCode`| 用户的硬件信息，也是集群的唯一标识码。试用版的 License 中无此参数。 |

## 设置 NebulaGraph 企业版 License

1. [联系我们](https://www.nebula-graph.com.cn/contact)申请 NebulaGraph 企业版安装包。

2. 安装 NebulaGraph 企业版。安装方式与社区版相同，请参见[使用 RPM 或 DEB 包安装 NebulaGraph](2.compile-and-install-nebula-graph/2.install-nebula-graph-by-rpm-or-deb.md)。

3. [联系我们](https://www.nebula-graph.com.cn/contact)申请 License 文件`nebula.license`。

4. 将 License 文件上传到所有包含 Meta 服务的机器上，路径为每个 Meta 服务安装目录的`share/resources/`内。

  !!! note

        周边工具的 License 文件上传位置，请参见[具体周边工具](../20.appendix/6.eco-tool-version.md)的说明文档。

## 续期 NebulaGraph 企业版 License

1. 发送邮件至`inqury@vesoft.com`申请新的 NebulaGraph 企业版 License。
2. 在所有包含 Meta 服务的机器上，路径为每个 Meta 服务安装目录的`share/resources/`内，使用新的 License 文件`nebula.license`替换旧的 License 文件。
3. 重启 Storage 和 Graph 服务。关于重启操作，参见[启动服务](manage-service.md)。如果用户的 License 的过期时间在到期后的缓冲期内（默认 14 天），则无需重启 Storage 和 Graph 服务。

  !!! note

        当用户的 License 过期时间超过到期后的缓冲期，Graph 和 Storage 服务会自动停止。为了确保服务正常运行，请及时更新 License。

## 查看 NebulaGraph 企业版 License

- 直接查看 License 文件

  可以使用 cat 等命令直接查看 License 文件，例如`cat share/resources/nebula.license`。

- 通过 HTTP 接口查看 License 文件

  当 NebulaGraph 正常运行时，可以请求 Meta 服务的 HTTP 接口（默认为19559）获取 License 文件内容。例如`curl -G "http://192.168.10.101:19559/license"`。

## 下一步

[启动 NebulaGraph](manage-service.md)
