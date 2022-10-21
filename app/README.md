# 简易说明
`app/` 这个目录下的源代码主要用来临时支持文档站点可以使用 algolia 搜索的功能。所谓临时支持是因为未来基于 mkdocs 框架的文档计划即将迁移至 docusaurus 来维护。基于此背景采用了外部引用js的方式来实现，而这里的源码就是用来处理并最终导出可供外部引用js。

## 编译

```shell
$ cd app/
$ npm install
$ npm run build
```

## 上传构建产物至cdn
构建产物目录: `src/dist/nebula-docs.[hash].js`
根据不同的环境，上传至不同的oss bucket中：

- 中文站点:
  - bucket: oss://nebula-website-cn/nebula-docs/nebula-docs.[hash].js
  - cdn地址: https://www-cdn.nebula-graph.com.cn/nebula-docs/nebula-docs.[hash].js
英文站点: 
  - bucket: oss://nebula-website-global/nebula-docs/nebula-docs.[hash].js
  - cdn地址: https://www-cdn.nebula-graph.io/nebula-docs/nebula-docs.[has].js


## 开发配置
配置根目录下的 `mkdocs.yml` 文件，添加引入的js文件:

```yaml
  extra_javascript:
    ....
    - https://www-cdn.nebula-graph.com.cn/nebula-docs/nebula-docs.576081464dcc6d4426ce.js # 添加文档的脚本
```

## 文档同学配置，选择搜索
由于algolia目前仅支持最新版本的文档搜索，一旦开启algolia搜索，只会搜索最新版本的内容，所以文档同学需要依据要发布的版本来决定是否使用algolia搜索，配置方式：

通过修改: `mkdocs.yml`

``` yaml
  plugins:
    ## 如果要使用 algolia 搜索就注释掉原有的搜索插件
    # - search 

    ## 如果要使用原有的插件，那就保留这个插件配置
    - search

```

