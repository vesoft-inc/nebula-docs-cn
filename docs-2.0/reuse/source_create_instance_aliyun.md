
在使用 NebulaGraph Cloud 阿里云版服务前，要先在阿里云控制台创建服务实例。

!!! caution

    通过 NebulaGraph Cloud 阿里云版创建的 NebulaGraph、NebulaGraph Dashboard 和 NebulaGraph Explorer 服务都是企业版，试用期 3 天。如需长期使用，发送邮件[申请正式许可证](mailto:inquiry@vesoft.com)，之后[续期许可证](https://docs.nebula-graph.com.cn/{{nebula.release}}/4.deployment-and-installation/deploy-license/#nebulagraph_license_3)。

## 前提条件

- 准备[阿里云账号](https://help.aliyun.com/document_detail/324606.html)。

- 如果使用 RAM 用户创建实例，需为其添加以下权限：

  - AliyunECSFullAccess
  - AliyunVPCFullAccess
  - AliyunROSFullAccess
  - AliyunCloudMonitorFullAccess
  - AliyunComputeNestUserFullAccess

## 操作步骤

1. 登录[创建服务实例](https://computenest.console.aliyun.com/user/cn-hangzhou/serviceInstanceCreate?ServiceId=service-39f4f251e9484369a778)页面。

2. 选中**同意授权并创建关联角色**。

  ![选中同意授权并创建关联角色](https://docs-cdn.nebula-graph.com.cn/figures/authorize-compute-nest_cn_2022.05.30.png)

3. 选择要创建实例的**地域**。

4. 进行**基本信息配置**。
  
  1. 选择 **NebulaGraph版本**。默认为 **3.1.0**。
  当前仅能选择 **3.1.0**。
  
  2. 设置 **NebulaGraph集群名**。默认为`nebula`。
  
  3. 设置实例密码。
  
    - 密码长度为 8-30 个字符。
    - 密码中必须包含大写字母、小写字母、数字、特殊符号中的三种。
    - 特殊符号包括：()`~!@#$%^&*_-+=|{}[]:;'<>,.?/

5. 进行**付费模式设置**，指定 ECS 服务器的付费方式。默认为**按量付费**。

  - **按量付费**：按照计费周期计费，在每个结算周期生成账单并从账户中扣除相应费用。详情参见[按量付费](https://help.aliyun.com/document_detail/40653.html)。

  - **预付费，包年包月**：先付费后使用。详情参见[包年包月](https://help.aliyun.com/document_detail/56220.html)。
  
    选择包年包月模式需要指定**购买时长周期**和**购买时长**。**购买时长周期**当前仅支持 **Month**，即按月购买，**购买时间**选择范围为 1-60 月。
  
6. 进行**基础设施配置**。

  1. 选择**专有网络VPC实例ID**。
  
    如果下拉列表为空，先单击其右侧的**新建专有网络**，完成专有网络创建。

  2. 选择**交换机可用区**。

  3. 选择**业务网络交换机的实例ID**。
  
    如果下拉列表为空，先单击其右侧的**新建交换机**，完成交换机创建。

7. 进行**集群节点配置**，根据业务需求配置 NebulaGraph 内核服务的节点。

  NebulaGraph 内核包含 Graph、Meta、Storage 服务，因此需要为这些服务分别选择**节点数量**、**节点实例类型**、**数据盘类型**和**数据盘空间**。

  !!! caution
        建议按照页面推荐信息配置集群节点以提升服务的可用性，例如配置 3 个 Meta 节点和至少 3 个 Storage 节点。

8. 进行**可视化产品配置**，选择要部署的可视化产品。
  
  可选用的产品包括 [Dashboard](https://docs.nebula-graph.com.cn/{{nebula.release}}/nebula-dashboard-ent/1.what-is-dashboard-ent/) 和 [Explorer](https://docs.nebula-graph.com.cn/{{nebula.release}}/nebula-explorer/about-explorer/ex-ug-what-is-explorer/)，默认都处于**开启**状态，此时需要为其选择**实例类型**。选中**关闭**表示不部署相应产品。

9. 根据需要配置**标签和资源组**。详情参见[什么是资源管理](https://help.aliyun.com/document_detail/94475.html)。

10. 完成**权限确认**，并选中**我同意授权服务商（杭州悦数科技有限公司）获取上述权限以提供代运维服务**。

11. 在页面底部，选中**我已阅读并同意《计算巢服务协议》**，并单击**创建**。

12. 在**创建**对话框，完成**信息确认**并**支付费用**。

13. 在**提交成功**页面，单击去列表查看。

14. 在实例列表中查看目标实例的**状态**，确保状态为**部署中**。

  部署的平均耗时为 10 分钟。完成后实例的状态变为**已部署**。

## 常见问题

Q：服务实例的状态显示为**部署失败**怎么处理？

1. 如果使用 RAM 账号创建的实例，确认为该账号授予了本文前提条件中指定的权限。
2. 如果权限符合要求，[删除](https://help.aliyun.com/document_detail/290837.html)创建失败的实例，尝试重新创建。
3. 如果仍然创建失败，到 [NebulaGraph 论坛](https://discuss.nebula-graph.com.cn/)寻求帮助。
