# 操作 Edge type

在 Nebula Graph 数据库中创建图空间后，用户可能需要创建 Edge type（边类型）。用户可以选择使用 **控制台** 或者 **Schema** 操作 Edge type。本文仅说明如何使用 **Schema** 操作 Edge type。

## 前提条件

在 Studio 上操作 Edge type 之前，用户必须确认以下信息：

- Studio 已经连接到 Nebula Graph 数据库。

- 图空间已经创建。

- 当前登录的账号拥有 GOD、ADMIN 或者 DBA 的权限。

## 创建边类型

1. 在顶部导航栏中，点击 **Schema** 页签。

2. 在 **图空间列表** 中，找到图空间，点击图空间名称或者在 **操作** 列中点击 **Schema**。

3. 在 **当前图空间** 里确认图空间名称。用户也可以通过选择图空间名称切换图空间。

4. 点击 **边类型** 页签，并点击 **+ 创建** 按钮。

5. 在 **创建边类型** 页面上，完成以下设置：

  1. **名称**：输入 Edge type 名称。本示例中，输入 `serve`。
  
  2. **描述**（可选）：输入 Edge type 的备注。
  
  3. **定义属性**（可选）：如果 Edge type 需要属性，点击 **+ 添加属性**，添加一个或多个属性：

    - 输入属性名称。
    - 选择数据类型。
    - 选择是否允许空值。 
    - （可选）输入默认值。
    - （可选）输入属性备注。

  4. **设置TTL（存活时间）**（可选）：Edge type 未设置索引时，用户可以设置 TTL。勾选**设置TTL（存活时间）**，设置`TTL_COL`和`TTL_DURATION`（单位：秒）。详情参考 [TTL 配置](../../3.ngql-guide/8.clauses-and-options/ttl-options.md "点击前往 Nebula Graph 网站")。

6. 完成设置后，在 **对应的 nGQL 语句** 面板上，用户能看到与上述配置等价的 nGQL 语句。  

   ![定义 Edge type action 的属性](https://docs-cdn.nebula-graph.com.cn/figures/st-ug-004-cn.png "定义 Edge type")

7. 确认无误后，点击 **创建** 按钮。

如果 Edge Type 创建成功，**边类型** 面板会显示这个 Edge type 的属性列表。

## 修改 Edge type

按以下步骤使用 **Schema** 修改 Edge type：

1. 在顶部导航栏中，点击 **Schema** 页签。

2. 在 **图空间列表** 中，找到图空间，点击图空间名称或者在 **操作** 列中点击 **Schema**。

3. 在 **当前图空间** 里确认图空间名称。用户也可以通过选择图空间名称完成图空间切换。

4. 点击 **边类型** 页签，找到需要修改的 Edge Type，并在 **操作** 列中，点击 ![表示修改的图标](https://docs-cdn.nebula-graph.com.cn/figures/Setup.png "修改") 图标。

5. 在 **编辑** 页面，用户可以选择以下操作：

   - 如果要修改描述：在 **描述** 右侧点击 **编辑**，修改后点击 **确认**。
   - 如果要修改属性：在 **定义属性** 区域，找到需要修改的属性，在右侧点击 **编辑**，修改后点击 **确认**。
   - 如果要删除属性：在 **定义属性** 区域，找到需要删除的属性，在右侧点击 **删除**，然后点击 **确认**。
   - 如果要添加属性：在 **定义属性** 区域，点击 **+ 添加属性**，设置属性信息，点击 **确认**。详细说明参考[创建边类型](#_2) 。
   - 如果要修改 TTL 信息：在 **设置 TTL** 区域，点击 **编辑**，修改后点击 **确认**。详情参考 [TTL 配置](../../3.ngql-guide/8.clauses-and-options/ttl-options.md "点击前往 Nebula Graph 网站")。
   - 如果要删除已经配置的 TTL 信息：在 **设置 TTL** 区域，取消勾选 **设置TTL（存活时间）**，然后点击 **确定**。
   - 如果要配置 TTL 信息：在 **设置 TTL** 区域，勾选 **设置TTL（存活时间）**，设置`TTL_COL`和`TTL_DURATION`（单位：秒），点击 **确认**。详情参考 [TTL 配置](../../3.ngql-guide/8.clauses-and-options/ttl-options.md "点击前往 Nebula Graph 网站")。

    !!! note

        TTL 与索引的共存问题，详情请见 [TTL](../../3.ngql-guide/8.clauses-and-options/ttl-options.md)。

## 删除 Edge type

!!! danger
    删除 Edge type 前先确认[影响](../../3.ngql-guide/11.edge-type-statements/2.drop-edge.md)，已删除的数据如未[备份](../../backup-and-restore/3.manage-snapshot.md)无法恢复。

1. 在顶部导航栏中，点击 **Schema** 页签。

2. 在 **图空间列表** 中，找到图空间，点击图空间名称或者在 **操作** 列中点击 **Schema**。

3. 在 **当前图空间** 里确认图空间名称。用户也可以通过选择图空间名称切换图空间。

4. 点击 **边类型** 页签，找到需要修改的 Edge type，并在 **操作** 列中，点击 ![表示删除的图标](https://docs-cdn.nebula-graph.com.cn/figures/alert-delete.png) 图标。

5. 在弹出的对话框中点击 **确认**。

## 后续操作

Edge type 创建成功后，用户可以在 **控制台** 上逐条插入边数据，或者使用 **导入** 功能批量插入边数据。
