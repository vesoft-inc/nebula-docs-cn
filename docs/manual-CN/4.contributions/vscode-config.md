# Nebula Graph 文档工程师 Visual Studio Code 推荐配置

图数据库 Nebula Graph 的所有文档均使用 Markdown 格式并已在 [GitHub](https://github.com/vesoft-inc/nebula-docs-cn) 开源。很多跨平台开发工具都支持 Markdown 格式，比如 Visual Studio Code、Atom、Sublime Text 等。本文档将介绍一些在写文档时比较常用的 Visual Studio Code 插件，以帮助提高写文档的效率。

Visual Studio Code（简称 VS Code）是一个由微软开发的免费代码编辑器，它内置了 Git 版本控制功能和丰富扩展程序。利用这些插件，可以有效提升写文档的速率。接下来介绍几种写文档时常见的插件。

## 插件安装方法

点击左侧的扩展按钮，输入插件名称即可下载。打开扩展的快捷方式为： `Ctrl+Shift+X`。

## 中文汉化包

如果更习惯使用中文语言环境，使用中文汉化包 Chinese (Simplified) Language Pack for Visual Studio Code 即可将 VS Code 默认的语言切换成简体中文。使用快捷键 `Ctrl+Shift+P` 调出命令面板，输入 Configure Display Language，选择 zh-ch，然后重启 VS Code 即可。

![image](https://user-images.githubusercontent.com/42762957/93572162-0459f080-f9c8-11ea-8809-7fb4db3ffdf4.png)

## Markdown All in One

使用 Markdown 写文档当然少不了这个插件。借助这个插件使用各种快捷键。此外，它还会自动处理列表以及表格的格式。

![image](https://user-images.githubusercontent.com/42762957/93577643-dd52ed00-f9ce-11ea-962f-82969b3cadf1.png)

## Markdown lint

markdownlint 插件可以规范 Markdown 文档的格式。这样多人协作也不用担心文档格式不一致了。

![image](https://user-images.githubusercontent.com/42762957/93583977-3a52a100-f9d7-11ea-8ca1-2d524bca05e4.png)

## 英语自动补全

插件 VSCode Dictionary Completion 可以自动补全英文单词，提高文档开发效率。

![image](https://user-images.githubusercontent.com/42762957/93575420-31100700-f9cc-11ea-9c14-1558cf86e56b.png)

## 拼写检查

拼写检查插件 Code Spell Checker 在写英文文档时十分有用。这个插件会自动识别单词拼写错误并且给出修改建议，能够帮我们减少文档中的拼写错误。

![image](https://user-images.githubusercontent.com/42762957/93572110-f4421100-f9c7-11ea-9f5c-e2b669a5b666.png)

## Markdown Preview Enhanced

Markdown Preview Enhanced 插件可以实时预览 Markdown 文档。效果如下图，左侧书写 Markdown 文本，右侧预览实时渲染效果。

![image](https://user-images.githubusercontent.com/42762957/93582374-f65e9c80-f9d4-11ea-9833-163f9f0ad4e2.png)

## 将 VS Code 配置同步到 Gist

Settings Sync 插件可以将您的 VS Code 设置同步到 Gist，下次在您更换电脑需要重新配置开发环境时，您就可以通过 Gist 下载您的配置了。

## 大小写转换

打开命令面板，输入 transform，就可以修改英语的大小写了。

![image](https://user-images.githubusercontent.com/42762957/93580204-0923a200-f9d2-11ea-8baf-9954c8c3f810.png)

## 自动保存

点击 Code> 首选项 > 设置，将文件设置为自动保存。这样就不用一直 `control+s` 手动保存了，也不用担心电脑突然关机的意外情况了。

![image](https://user-images.githubusercontent.com/42762957/93580547-86e7ad80-f9d2-11ea-8af9-494dfbf94d3b.png)
