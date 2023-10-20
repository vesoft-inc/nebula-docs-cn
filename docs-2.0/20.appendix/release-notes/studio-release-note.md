# NebulaGraph Studio 版本更新说明


## v3.8.0

- 功能
  - 支持使用 MySQL 数据库作为后端存储。

- 增强
  - 支持自定义 WebSocket 的读写参数。
  - 易用性
    - 支持在导入任务列表根据图空间名称筛选任务。
  - 兼容性
    - 由于数据库表结构变更，需要在配置文件内将`DB.AutoMigrate`设置为`true`，系统会自动对已有历史数据进行升级适配。

      如果是自己手动创建的库表，请手动修改这些表：`task_infos`、`task_effects`、`sketches`、`schema_snapshots`、`favorites`、`files`、`datasources`。

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

## v3.7.0

- 增强

  - 支持导入 SFTP、Amazon S3 的数据文件。
  - 导入页面支持配置更多导入参数，如并发数、重试次数等。
  - 支持重跑任务。
  - 支持任务保存为草稿。
  - 支持 ARM 架构。
