# 通知设置

通知设置页面可以设置通知邮箱和 Webhook。

## 入口

1. 在{{dashboard_ent.name}}顶部导航栏，单击**平台设置**。
2. 在左侧导航栏单击**通知设置**。

## 操作说明

### 邮箱

{{dashboard_ent.name}}支持通过邮箱发送和接收所有集群的告警消息。
  
- 用户需设置以下参数来发送告警消息。

  | 参数           | 说明      |
  | -------------- | --------- |
  | SMTP 服务器地址 | 用户邮箱对应的 SMTP 服务器地址。   |
  | 端口号         | 邮箱对应的 SMTP 服务器的端口号。  |
  | Use SSL        | 勾选后启用 SSL 进行数据的加密传输。  |
  | SMTP 用户名     | SMTP 服务器的用户名。   |
  | SMTP 密码       | SMTP 服务器的密码。     |
  | 发件人邮箱     | 发送告警消息的邮箱地址。  |

- 用户需设置**接收人**来接收告警消息。

  | 参数           | 说明                                                         |
  | -------------- | ------------------------------------------------------------ |
  | 接收人         | 接收告警消息的邮箱地址。该邮箱将接收{{dashboard_ent.name}}上所有集群的告警消息。 |

### Webhook

{{dashboard_ent.name}}支持用户配置 Webhook 将所有集群的告警消息接入第三方项目中。
  
在**平台设置**页面的左侧导航栏中，单击**通知设置**->**Webhook**，填入接收告警消息的 **Webhook URL** 和**Webhook请求体body**。用户也可在页面右上方开启和关闭 Webhook 功能。

支持的变量如下。

| 变量           | 说明      |
| -------------- | --------- |
|`${cluster.name}` | 集群名称。 |
|`${cluster.id}`  | 集群 ID。 | 
|`${cluster.version}` | 集群版本。|
|`${cluster.status}` | 集群当前状态。|
|`${cluster.owner}` | 拥有集群 Owner 角色权限的账号名称。|
|`${alert.labels.instance}` | 服务的 IP 地址和端口。  |
|`${alert.labels.instanceName}` |  服务名称。例如`192.168.10.100-graphd-9669`。 |
|`${alert.labels.alertname}` | 告警名称。|
|`${alert.labels.severity}` | 告警严重级别。|
|`${alert.labels.componentType}` |  告警服务类型。|
|`${alert.annotations.summary}` | 告警摘要。|
|`${alert.annotations.description}` |  告警消息描述。|

关于告警的更多信息，请参见[通知](../4.cluster-operator/9.notification.md)。