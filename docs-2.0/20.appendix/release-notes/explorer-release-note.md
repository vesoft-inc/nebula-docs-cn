# {{explorer.name}}版本更新说明

## v3.6.0

- 功能
  - 登录认证新增支持 [CAS](../../nebula-explorer/deploy-connect/ex-ug-deploy.md)。
  - 内联框架新增支持三种消息类型：`ExplorerLogin`（替代`NebulaGraphExploreLogin`）、`ExplorerAddCanvasElements`和`ExplorerClearCanvas`。

- 增强
  - 兼容性

    - 由于数据库表结构变更，需要在配置文件内将`DB.AutoMigrate`设置为`true`，系统会自动对已有历史数据进行升级适配。

      如果是咨询售后工作人员手动创建的库表，请手动修改这些表：`task_infos`、`task_effects`、`sketches`、`schema_snapshots`、`favorites`、`files`、`datasources`、`snapshots`、`templates`、`icon_groups`、`icon_items`。

      示例如下：

      ```mysql
      ALTER TABLE `task_infos` ADD COLUMN `b_id` CHAR(32) NOT NULL DEFAULT '';
      UPDATE TABLE `task_infos` SET `b_id` = `id`;
      CREATE UNIQUE INDEX `idx_task_infos_id` ON `task_infos`(`b_id`);

      ALTER TABLE `task_effects` ADD COLUMN `b_id` CHAR(32) NOT NULL DEFAULT '';
      UPDATE TABLE `task_effects` SET `b_id` = `id`;
      CREATE UNIQUE INDEX `idx_task_effects_id` ON `task_effects`(`b_id`);
      ...
      ```

    - 由于 nGQL 语法兼容问题，连接 3.5.x 及以下版本的图数据库时禁用修改 IP 白名单功能。您可以执行对应数据库版本的 nGQL 语句修改 IP 白名单。

  - 高可用
    - 支持[高可用架构](../../nebula-explorer/faq.md)。

- 弃用
  - 配置文件中弃用`OAuth.xxx`配置，但是在 3.x 版本中继续保持兼容。请改用`SSO.xxx`。
  - 配置文件中弃用`File.SqliteDbFilePath`配置，请改用`DB.SqliteDbFilePath`。
  - 配置文件中弃用`File.TaskIdPath`配置。
  - 内联框架弃用`NebulaGraphExploreLogin`消息类型，但是在 3.x 版本中继续保持兼容。请改用`ExplorerLogin`。

## v3.5.1

- 缺陷修复

  - 修复错误链接。
  - 修复错误文案。
  - 移除弃用的工具组件。

## v3.5.0

- 功能

  - 支持通过[配置 NFS](../../nebula-explorer/workflow/1.prepare-resources.md) 使用工作流。
  - 允许用户对产品进行个性化自定义，包括页面 Logo 和产品名称。
  - [数据导入](../../nebula-explorer/db-management/11.import-data.md)支持历史任务重新导入，数据源类型新增支持云存储和 SFTP。
  - 支持新版 [License](../../9.about-license/1.license-overview.md)。

## v3.4.0

- 功能

  - 支持查看 Schema 的[创建语句](../../nebula-explorer/db-management/10.create-schema.md)。
  - 全局设置页面增加 Beta 功能开关。
  - 新增产品反馈页面。

- 优化

  - 优化慢查询，取消超时限制。
  - 切换页面后控制台保留历史记录。
  - 控制台支持使用`#`添加注释。
  - 创建模版时支持使用`#`或`//`添加注释。
  - 更新全局设置页面。
  - 支持可视化修改 IP 白名单。
  - 画布中默认展示 VID。
  - 浏览器兼容提示。
  - 连接信息展示内核版本。
  - 内置数据集增加索引。
  - 优化登录页。
  - 优化 Workflow：
    - 增加算法说明。
    - 优化图算法的参数配置。
    - 优化结果的展示。
  - 优化交互：
    - 节点筛选
    - Tag 查询
    - 路径查询
  - 优化展示：
    - 优化 Schema 统计信息展示。
    - 优化力导向图布局。
    - 优化可视化查询结果导入画布后的布局。
    - 优化悬挂边上的点的展示。
    - 优化控制台界面。
  - 优化提示：
    - 优化引导提示。
    - 优化报错提示。

- 缺陷修复
  - 修复无法查看导入任务日志的问题。
  - 修复`demo_basketballplayer`数据集中缺失部分边数据的问题。
  - 修复页面崩溃的问题。
  - 修复 Workflow 中图计算结果导入画布后无法展示点的详细信息的问题。