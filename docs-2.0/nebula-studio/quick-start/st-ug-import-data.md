# 导入数据

<<<<<<< HEAD
Studio 支持界面化地将 CSV 格式数据导入至{{nebula.name}}中。
=======
准备好 CSV 文件，创建了 Schema 后，用户可以使用 **导入** 功能将所有点和边数据上传到 Studio，用于数据查询和数据分析。
>>>>>>> a7074d38d (increment-changes-on-ent-docs (#2789))

## 前提条件

导入数据之前，需要确认以下信息：

<<<<<<< HEAD
- {{nebula.name}}里已经创建 Schema。

- CSV 文件符合 Schema 要求。

- 账号拥有 GOD、ADMIN 或 DBA 权限。详情参见 [{{nebula.name}}内置角色](../../7.data-security/1.authentication/3.role-list.md)。

## 入口

在顶部导航栏里，单击 ![download](https://docs-cdn.nebula-graph.com.cn/figures/studio-btn-download.png) 图标。

导入数据主要分为 2 个部分，新建数据源和创建导入任务，接下来将详细介绍。

### 新建数据源

在页面右上角单击**新建数据源**，设置数据来源及其相关设置。当前支持 3 种类型的数据源。

| 数据源类型 | 说明 |
| :--- | :--- |
| 云存储 | 添加云存储作为 CSV 文件来源，只支持兼容 Amazon S3接口的云服务。 |
| SFTP | 添加 SFTP 作为 CSV 文件来源。 |
| 本地文件 | 上传本地 CSV 文件。文件大小不能超过 200 MB，超过限制的文件请放入其他方式的数据源中。 |

!!! Note

    - 上传本地 CSV 文件时，一次可以选择多个 CSV 文件。
    - 数据源添加后，可以在页面上方单击**数据源管理**，切换页签即可查看不同类型的数据源详情，也可以编辑或删除数据源。

### 创建导入任务

1. 在页面左上角单击**创建导入任务**，完成如下设置：
  
  !!! caution

        用户也可以单击**导入模版**，下载示例配置文件`example.yaml`，配置后再上传配置文件。配置方式与 [NebulaGraph Importer](../../nebula-importer/use-importer.md)大致相同。

  - **图空间**：需要导入数据的图空间名称。
  - **任务名称**：默认自动生成，可以修改。
  - **更多配置**（可选）：可以自定义设置并发数、批处理量、重试次数、读取并发数和导入并发数。
  - **关联标签**：

    1. 单击**添加 Tag**，然后在下方新增的标签内选择 Tag。
    2. 单击**添加导入文件**，在**文件源**里选择**数据源类型**和**文件路径**，找到需要导入的文件，然后单击**添加**。
    3. 在预览页面设置文件的分隔符和是否携带表头，然后单击**确认**。
    4. 在**VID 列**为 VID 选择对应的列。支持选择多个列合并为 VID，也可以为 VID 添加前缀或后缀。
    5. 在**属性**框内为属性选择对应的列。对于可以为`NULL`或设置了`DEFAULT`的属性，可以不指定对应的列。
    6. 重复 2 ~ 5 步骤将步骤 1 所选 Tag 的数据文件全部导入。
    7. 重复 1 ~ 6 步骤将所有需要导入的 Tag 数据全部导入。
  
  - **关联边**：与关联标签的操作相同。

  ![导入任务](https://docs-cdn.nebula-graph.com.cn/figures/explorer_import_230522_cn.png)

2. 完成设置后，单击**导入**,输入{{nebula.name}}账号的密码并确认。

导入任务创建后，可以在**导入数据**页签内查看导入任务的进度，支持编辑任务、查看日志、下载日志、重新导入、下载配置文件、删除任务等操作。
=======
- Studio 已经连接到{{nebula.name}}。

-{{nebula.name}}里已经创建 Schema。

- CSV 文件符合 Schema 要求。

- 账号拥有 GOD、ADMIN、DBA 或者 USER 的权限，能往图空间中写入数据。

## 操作步骤

在导入数据之前，用户需要先上传文件后再创建导入任务。

### 上传文件

1. 在顶部导航栏里，点击 **导入** 页签。
2. 在 **上传文件** 页面，点击 **上传文件** 按钮，并选择需要的 CSV 文件。本示例中，选择 `edge_serve.csv`、`edge_follow.csv`、`vertex_player.csv` 和 `vertex_team.csv` 文件。

  !!! Note

        一次可以选择多个 CSV 文件，本文使用的 CSV 文件可以在[规划 Schema](st-ug-plan-schema.md) 中下载。

3. 上传结束后，可以在文件列表的 **操作** 列，点击 ![detail](https://docs-cdn.nebula-graph.com.cn/figures/detail.png) 图标预览文件内容，或点击 ![delete](https://docs-cdn.nebula-graph.com.cn/figures/alert-delete.png) 图标删除上传的文件。

![上传文件](https://docs-cdn.nebula-graph.com.cn/figures/st-ug-010-cn.png)

### 导入数据

按照以下步骤导入数据：

1. 在顶部导航栏里，点击 **导入** 页签。
2. 在标签页内点击 **导入数据** 按钮。
3. 在 **导入数据** 页面，点击 **+ 创建导入任务** 按钮，完成以下任务：
  
  !!! caution

        用户也可以点击 **导入模版** ，下载示例配置文件`example.yaml`，配置后再上传配置文件。配置方式与 [NebulaGraph Importer](../../nebula-importer/use-importer.md) 大致相同，但是所有文件路径仅保留文件名。并且请确保在导入配置文件之前已上传所有 CSV 数据文件。

  - 选择图空间。
  - 填写任务名称。
  - （可选）填写批处理量。
  - 在 **关联点** 页签里，点击 **+ 绑定数据源** 按钮，在对话框中选择绑定文件，并点击 **确认** 按钮。如本示例中的 `vertex_player.csv`文件。

    - 在 **vertices 1** 页签下的 `verteID` 项中，点击 **Select CSV Index**，在弹出的对话框内选择 vertexID 所在的列。
    - 点击 **+ 添加Tag** 按钮，点击右方的![down](https://docs-cdn.nebula-graph.com.cn/figures/down.png)图标，在显示的属性列表中，为 Tag 属性绑定源数据。在本示例中，`player` 标签的 `name` 属性对应文件中的 **Column 2** 列，类型为 `string`，`age` 属性对应文件中的 **Column 1** 列，类型 为 `int`。
  
  - 在 **关联边** 页签里，点击 **+ 绑定数据源** 按钮，在对话框中选择绑定文件，并点击 **确认** 按钮。如本示例中的 `edge_follow.csv`文件。
    - 在 **edge 1** 页签下，点击右方的![down](https://docs-cdn.nebula-graph.com.cn/figures/down.png)图标，在显示的属性列表中，选择 Edge Type。
    - 根据 Edge type 的属性，从 `edge_follow.csv` 文件中选择相应的数据列。其中，**srcId** 和 **dstId** 分别表示边的起点与终点，所选择的数据类型必须与 Schema 中的 VID 类型保持一致。本示例中，**srcId** 对应的是表示起点球员的 VID，**dstId** 对应的是表示终点球员的 VID。rank 为选填项，可以忽略。
    ![导入任务](https://docs-cdn.nebula-graph.com.cn/figures/st-ug-011-cn.png)

4. 完成设置后，点击 **导入** 按钮。

5. 用户输入{{nebula.name}}账号的密码后方可导入数据。
  ![输入密码](https://docs-cdn.nebula-graph.com.cn/figures/st-ug-014-cn.png)

6. 导入数据后可以在 **导入数据** 页签内查看日志、下载日志、下载配置文件、删除任务等操作。
  ![导入成功](https://docs-cdn.nebula-graph.com.cn/figures/st-ug-012-cn.png)
>>>>>>> a7074d38d (increment-changes-on-ent-docs (#2789))

## 后续操作

完成数据导入后，用户可以进入[控制台](st-ug-console.md)页面。
