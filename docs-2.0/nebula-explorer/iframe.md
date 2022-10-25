# 内联框架

NebulaGraph Explorer 支持内联框架（iFrame），可以将画布嵌入至第三方页面中使用。本文介绍如何嵌入画布。

## 前提条件

已安装 Explorer。

## 注意事项

- 嵌入的 Explorer 页面默认直接访问目标图空间，因此会屏蔽部分页面及功能。例如上方导航栏、左侧导航栏中的模板查询和切换图空间等。如果需要访问多个图空间，可以在多个页面中分别嵌入。
- 暂不支持切换语言，默认为中文页面。

## 步骤

1. 在 Explorer 安装目录内修改配置文件`config/app-config.yaml`。需要修改的内容如下。

  ```bash
  # 取消 CertFile 和 KeyFile 参数的注释。
  CertFile: "./config/NebulaGraphExplorer.crt"
  KeyFile: "./config/NebulaGraphExplorer.key"

  # 修改 IframeMode.Enable为 true。
  IframeMode:
  Enable: true 
  ```

2. 在`config`文件夹内使用`openssl`命令生成自签名证书。示例如下。

  ```bash
  openssl req -newkey rsa:4096 -x509 -sha512 -days 365 -nodes -subj "/CN=NebulaGraphExplorer.com" -out NebulaGraphExplorer.crt -keyout NebulaGraphExplorer.key
  ```

  - `-newkey`：生成证书请求或者自签名证书的时候自动生成密钥。
  - `-x509`：生成自签名证书。
  - `-sha512`：指定消息摘要算法。
  - `-days`：`-x509`生成的证书的有效天数。
  - `-nodes`：不加密输出密钥。
  - `-subj`：设置请求的主题。
  - `-out`：指定生成的证书请求或者自签名证书名称。
  - `-keyout`：指定自动生成的密钥名称。

3. 在第三方页面中嵌入 Explorer。这部分内容由用户自行开发，本文仅提供示例核心代码介绍必须传递的参数。

  ```html
  function Iframe1() {
    const iframeRef = useRef();
    const onIframeLoad = useCallback(() => {
      setTimeout(() => {
        iframeRef.current?.contentWindow.postMessage({
          type: 'NebulaGraphExploreLogin',
          data: { authorization: 'cm9vdDoxMjM=', host: '192.168.10.100:9669', space: 'basketballplayer' }
        }, '*');
      }, 500);
    }, []);

  function Iframe2() {
    const iframeRef = useRef();
    const onIframeLoad = useCallback(() => {
      setTimeout(() => {
        iframeRef.current?.contentWindow.postMessage({
          type: 'NebulaGraphExploreLogin',
          data: { authorization: 'cm9vdDoxMjM=', host: '192.168.10.100:9669', space: 'test1' }
        }, '*');
      }, 500);
    }, []);
  ```

  - `authorization`：Base64 编码后的 NebulaGraph 账号和密码。编码前格式为`账号:密码`，示例为`root:123`，编码后为`cm9vdDoxMjM=`。
  - `host`：NebulaGraph 的 Graph 服务地址。
  - `space`：目标图空间名称。

4. 启动 Explorer 服务。

  !!! note

        如果是 RPM/DEB 安装的 Explorer，请执行命令`sudo ./nebula-explorer-server &`。

  ```bash
  ./scripts/start.sh
  ```

5. 访问第三方页面，检查是否可以查看到嵌入的 Explorer 页面。示例页面中第一个页面展示`basketballplayer`图空间，第二个页面展示`test1`图空间。

  ![iFrame_example](https://docs-cdn.nebula-graph.com.cn/figures/explorer_iframe_example_221025.png)