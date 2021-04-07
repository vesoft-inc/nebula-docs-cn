# 检查更新

Studio 2.x持续开发中，您可以访问GitHub查看[Changelog](https://github.com/vesoft-inc/nebula-web-docker/blob/master/docs/CHANGELOG-en.md)，了解开发进度。

当您登录Studio 2.0.0，可以在右上角查看当前版本。也可以在版本的下拉菜单中，单击**新发布**查看Changelog。

如果新版本发布，请在目录`nebula-web-docker`内按如下步骤执行命令更新镜像并启动服务。

```bash
$ git pull origin master
$ cd v2
$ docker-compose pull && docker-compose up -d
```