# NebulaGraph Studio 版本更新说明

<!--
## v3.8.0

- 增强
  - 兼容性
    由于数据库表结构变更，需要在配置文件内将`DB.AutoMigrate`设置为`true`，系统会自动对已有历史数据进行升级适配。

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
-->

## v3.7.0

- 增强

  - 支持导入 SFTP、Amazon S3 的数据文件。
  - 导入页面支持配置更多导入参数，如并发数、重试次数等。
  - 支持重跑任务。
  - 支持任务保存为草稿。
  - 支持 ARM 架构。

## v3.6.0

- 功能
  - 支持查看 Schema 的[创建语句](../../nebula-studio/manage-schema/st-ug-view-schema.md)。
  - 新增产品反馈页面。

- 优化
  - 优化慢查询，取消超时限制。
  - 浏览器兼容提示。
  - 优化登录页。
  - 控制台支持使用`#`添加注释。
  - 优化控制台界面。

- 缺陷修复
  - 修复上传文件后列表不刷新的问题。
  - 修复 Schema 草图中无效的错误提示。
  - 修复切换登录用户后，**查看 Schema** 数据未清除的问题。
  - 修复 Schema 草图的缩略图展示的问题。
