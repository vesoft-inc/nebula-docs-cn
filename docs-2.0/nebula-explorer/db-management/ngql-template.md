# 查询语句模板

{{explorer.name}}支持将常用 nGQL 语句保存为模板，方便自己或他人使用。nGQL 语句中的文本还支持参数化，可根据需要填写参数值。

## 前提条件

{{nebula.name}}里已经创建 Schema。

## 入口

在顶部导航栏里，点击 ![Template](https://docs-cdn.nebula-graph.com.cn/figures/icon-navbar-queryTemplate.png) 图标。

## 新建模板

1. 单击 **+ 新模板**，设置如下参数。

  |参数|示例|说明|
  |:---|:---|:---|
  |模板名称|`test`|模板的名称。|
  |图空间|`basketballplayer`|模板适用的图空间。|
  |描述|`返回指定球员的邻居名称`|描述模板的作用。|
  |查询模板|`MATCH (v:player{name:"${name}"})--(v2:player) RETURN v2.player.name AS Name;`|nGQL 语句模板。可以选中需要参数化的文本，在右侧单击 **+ 文本参数化**，设置参数名称和描述。示例中`${name}`为参数化的文本，实际使用时可以填写`Tim Duncan`等名称。<br>可以在单行使用`//`添加注释。|
  |输入|-|显示参数化的文本内容。可以编辑或删除参数化的文本。|

  <img src="https://docs-cdn.nebula-graph.com.cn/figures/ec_expl_template_230913_cn.png" width="600" alt="图探索创建模板截屏">

  !!! note

        控制台页面左上角单击 **保存为模板**，会自动将已输入的查询语句作为模板语句。

2. 单击**保存为模板**。

## 其他操作

- 目标模板右侧单击 ![setup](https://docs-cdn.nebula-graph.com.cn/figures/setup-220916.png)可以修改模板内容。
- 目标模板右侧单击![console](https://docs-cdn.nebula-graph.com.cn/figures/nav-console2.png) 可以自动跳转至控制台并输入模板。
- 目标模板右侧单击 ![delete](https://docs-cdn.nebula-graph.com.cn/figures/alert-delete.png) 可以删除模板。
- 右上角筛选框可以筛选指定图空间的模板。
- 右上角搜索框可以搜索模板名称。

## 使用模板

- （推荐）在图探索页面使用模板。详情参见[开始探索](../graph-explorer/ex-ug-query-exploration.md)。

- 在模板列表页面单击 ![console](https://docs-cdn.nebula-graph.com.cn/figures/nav-console2.png) 自动跳转至控制台并输入模板语句，需要自行修改参数化的文本。
