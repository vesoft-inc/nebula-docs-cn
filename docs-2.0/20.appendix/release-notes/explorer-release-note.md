# NebulaGraph Explorer 版本更新说明

## v3.2.0

- 功能
  - 支持[边聚合](../..//nebula-explorer/canvas-operations/visualization-mode.md)。对画布上起点、终点、边类型相同的边进行聚合，使得哪些点之间存在大量关系一目了然。并支持对聚合边的属性进行计算。
  - 支持 [Schema 草图](../../nebula-explorer/db-management/draft.md)。直接在画板上通过拖拽方式设计 Schema，点边关系更加直观，并支持一键应用至图空间。
  - 支持 [iFrame 模式](../../nebula-explorer/iframe.md)。支持使用内联框架将画布嵌入至第三方页面中使用。
  - 支持 [OAuth 2.0 认证](../../nebula-explorer/deploy-connect/ex-ug-connect.md)。用户通过 OAuth2.0 认证登录 Explorer，保证数据安全。
  - 支持[自定义图标库及点边样式](../../nebula-explorer/canvas-operations/canvas-overview.md)。Explorer 内置十种行业分类图标，并支持上传图片作为图标。
  - 支持[查询语句模板](../../nebula-explorer/db-management/ngql-template.md)。直接设计查询语句模板或在控制台将 nGQL 语句制作为模版，后续可直接调用模版，填入参数即可查询。
  - 支持[数据库用户管理](../../nebula-explorer/db-management/dbuser_management.md)。可视化管理数据库用户，包括创建用户、授权用户等操作。
  - 工作流添加 [node2vec 算法](../../graph-computing/algorithm-description.md)。

- 优化
  - 安装包[内置 Dag Controller](../../nebula-explorer/deploy-connect/ex-ug-deploy.md)。
  - 欢迎页改版，内置 demo 数据集。
  - 增加节点拖动动效。
  - 控制台支持使用`//`添加注释。
  - 收藏夹内容支持在服务端保存。
  - 图空间列表支持搜索图空间名。
  - 工作流对于缺失的入参，会提示手动输入。
  - 帮助页整合，提供介绍视频。
  - 工作流支持页面配置资源。
  - 新增白屏崩溃兜底页。

- 缺陷修复
  - 修复右键菜单点击后无法自动收起问题。
  - 修复添加筛选条件时，画布自动缩放问题。
  - 修复大数据量下切换至 3D 模式时展示结果抖动问题。
  - 修复无法导入 Int8/16/32 和 fixed_string 类型数据的问题。
