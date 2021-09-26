RPM和DEB是Linux系统下常见的两种安装包格式，本文介绍如何使用RPM或DEB文件在一台机器上快速安装Nebula Graph。

!!! note

    部署Nebula Graph集群的方式参见[使用RPM/DEB包部署集群](https://docs.nebula-graph.com.cn/{{nebula.release}}/4.deployment-and-installation/deploy-nebula-graph-cluster/)。<!--这里用外链。-->

!!! enterpriseonly

    企业版请发送邮件至 inquiry@vesoft.com。

## 前提条件

安装wget

## 下载安装包

### 阿里云OSS下载

- 下载release版本

    URL格式如下：

    ```bash
    //Centos 7
    https://oss-cdn.nebula-graph.com.cn/package/<release_version>/nebula-graph-<release_version>.el7.x86_64.rpm

    //Centos 8
    https://oss-cdn.nebula-graph.com.cn/package/<release_version>/nebula-graph-<release_version>.el8.x86_64.rpm

    //Ubuntu 1604
    https://oss-cdn.nebula-graph.com.cn/package/<release_version>/nebula-graph-<release_version>.ubuntu1604.amd64.deb

    //Ubuntu 1804
    https://oss-cdn.nebula-graph.com.cn/package/<release_version>/nebula-graph-<release_version>.ubuntu1804.amd64.deb

    //Ubuntu 2004
    https://oss-cdn.nebula-graph.com.cn/package/<release_version>/nebula-graph-<release_version>.ubuntu2004.amd64.deb
    ```

    例如要下载适用于`Centos 7.5`的`{{ nebula.release }}`安装包：

    ```bash
    wget https://oss-cdn.nebula-graph.com.cn/package/{{ nebula.release }}/nebula-graph-{{ nebula.release }}.el7.x86_64.rpm
    wget https://oss-cdn.nebula-graph.com.cn/package/{{ nebula.release }}/nebula-graph-{{ nebula.release }}.el7.x86_64.rpm.sha256sum.txt
    ```

    下载适用于`ubuntu 1804`的`{{ nebula.release }}`安装包：
    ```bash
    wget https://oss-cdn.nebula-graph.com.cn/package/{{ nebula.release }}/nebula-graph-{{ nebula.release }}.ubuntu1804.amd64.deb
    wget https://oss-cdn.nebula-graph.com.cn/package/{{ nebula.release }}/nebula-graph-{{ nebula.release }}.ubuntu1804.amd64.deb.sha256sum.txt
    ```

- 下载日常开发版本(nightly)

  !!! danger
  
      - nightly 版本通常用于测试新功能、新特性，请**不要**在生产环境中使用 nightly 版本。
      - nightly 版本不保证每日都能完整发布，也不保证是否会更改文件名。

    URL格式如下：

    ```bash
    //Centos 7
    https://oss-cdn.nebula-graph.com.cn/package/v2-nightly/<yyyy.mm.dd>/nebula-graph-<yyyy.mm.dd>-nightly.el7.x86_64.rpm

    //Centos 8
    https://oss-cdn.nebula-graph.com.cn/package/v2-nightly/<yyyy.mm.dd>/nebula-graph-<yyyy.mm.dd>-nightly.el8.x86_64.rpm

    //Ubuntu 1604
    https://oss-cdn.nebula-graph.com.cn/package/v2-nightly/<yyyy.mm.dd>/nebula-graph-<yyyy.mm.dd>-nightly.ubuntu1604.amd64.deb

    //Ubuntu 1804
    https://oss-cdn.nebula-graph.com.cn/package/v2-nightly/<yyyy.mm.dd>/nebula-graph-<yyyy.mm.dd>-nightly.ubuntu1804.amd64.deb

    //Ubuntu 2004
    https://oss-cdn.nebula-graph.com.cn/package/v2-nightly/<yyyy.mm.dd>/nebula-graph-<yyyy.mm.dd>-nightly.ubuntu2004.amd64.deb
    ```

    例如要下载`2021.03.28`适用于`Centos 7.5`的`2.x`安装包：

    ```bash
    wget https://oss-cdn.nebula-graph.com.cn/package/v2-nightly/2021.03.28/nebula-graph-2021.03.28-nightly.el7.x86_64.rpm
    wget https://oss-cdn.nebula-graph.com.cn/package/v2-nightly/2021.03.28/nebula-graph-2021.03.28-nightly.el7.x86_64.rpm.sha256sum.txt
    ```

    要下载`2021.03.28`适用于`Ubuntu 1804`的`2.x`安装包：
    ```bash
    wget https://oss-cdn.nebula-graph.com.cn/package/v2-nightly/2021.03.28/nebula-graph-2021.03.28-nightly.ubuntu1804.amd64.deb
    wget https://oss-cdn.nebula-graph.com.cn/package/v2-nightly/2021.03.28/nebula-graph-2021.03.28-nightly.ubuntu1804.amd64.deb.sha256sum.txt
    ```

<!--
### GitHub下载

- 下载release版本

   + 登录[Nebula Graph Releases](https://github.com/vesoft-inc/nebula/releases)页面，确认需要的版本，单击**Assets**。

   ![Select a Nebula Graph release version](https://github.com/vesoft-inc/nebula-docs/raw/master/docs-2.0/figs/4.deployment-and-installation/2.complie-and-install-nebula-graph/2.install-nebula-graph-by-rpm-or-deb/releases-page.png?raw=true)

   + 在**Assets**区域找到机器运行所需的安装包，下载文件到机器上。

- 下载nightly版本

    >**禁止**：nightly版本通常用于测试新功能、新特性，请**不要**在生产环境中使用nightly版本。

   + 登录[Nebula Graph package](https://github.com/vesoft-inc/nebula/actions/workflows/package.yaml)页面，单击顶部最新的**package**。

   ![Select a Nebula Graph nightly version](https://github.com/vesoft-inc/nebula-docs/raw/master/docs-2.0/figs/4.deployment-and-installation/2.complie-and-install-nebula-graph/2.install-nebula-graph-by-rpm-or-deb/nightly-page.png?raw=true)

   + 在**Artifacts**区域找到机器运行所需的安装包，下载文件到机器上。
-->

## 安装Nebula Graph

- 安装RPM包

    ```bash
    $ sudo rpm -ivh --prefix=<installation_path> <package_name>
    ```

- 安装DEB包

    ```bash
    $ sudo dpkg -i --instdir==<installation_path> <package_name>
    ```

!!! Note

    如果不设置安装路径，默认安装路径为`/usr/local/nebula/`。

## 后续操作

- [启动Nebula Graph](https://docs.nebula-graph.com.cn/{{nebula.release}}/2.quick-start/5.start-stop-service/)<!--这里用外链。-->
- [连接Nebula Graph](https://docs.nebula-graph.com.cn/{{nebula.release}}/2.quick-start/3.connect-to-nebula-graph/)<!--这里用外链。-->
