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
  - 配置文件中弃用`OAuth.xxx`配置，请改用`SSO.xxx`。但是在 3.x 版本中继续保持兼容。
  - 配置文件中弃用`File.SqliteDbFilePath`配置，请改用`DB.SqliteDbFilePath`。
  - 配置文件中弃用`File.TaskIdPath`配置。
  - 内联框架弃用`NebulaGraphExploreLogin`消息类型，请改用`ExplorerLogin`。但是在 3.x 版本中继续保持兼容。