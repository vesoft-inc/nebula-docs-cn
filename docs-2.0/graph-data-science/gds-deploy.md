# 部署及使用 GDS

## 前提条件

- 准备单机的 Linux 或 MacOS 环境。
- 确保相关组件的端口未被占用。如被占用，请根据报错提示进行关闭。
- 硬盘剩余存储空间需要 xx GB以上。

## 步骤

1. 执行如下命令安装所有组件。首次安装请耐心等待。

  ```bash
  curl -fsSL nebula-up.siwei.io/all-in-one.sh | bash
  ```

  你也可以选择性安装组件，例如：

  ```bash
  # Install Core with Backup and Restore with MinIO
  curl -fsSL nebula-up.siwei.io/all-in-one.sh | bash -s -- v3 br
  # Install Core with Spark Connector, Nebula Algorithm, Nebula Exchange
  curl -fsSL nebula-up.siwei.io/all-in-one.sh | bash -s -- v3 spark
  # Install Core with Dashboard
  curl -fsSL nebula-up.siwei.io/all-in-one.sh | bash -s -- v3 dashboard
  ```

  - `-s`：从标准输入读取命令。
  - `--`：传递参数给脚本。例如`-- v3 spark`表示选择性安装最新的 3.x 版本 NebulaGraph 和 Spark 系列组件。

2. 在浏览器中输入`<Host_ip>:8888`访问 Jupyter Notebook 界面。

3. 在页面下方填写 Token `nebula`，然后设置登录密码并登录。

4. 在页面右上方选择 **New**->**Python 3(ipykernel)** 新建`.ipynb`文件，即可开始交互式开发。

  ![jupyter](https://docs-cdn.nebula-graph.com.cn/figures/gds_230214.png)

默认有`pagerank_example.ipynb`可供参考，这是 PageRank 算法的示例笔记。

## 内置脚本

`~/.nebula-up`目录内置了部分脚本方便用户导入数据、备份恢复、执行 nGQL 等，详情参见 [Nebula-Up Readme](https://github.com/wey-gu/nebula-up)。