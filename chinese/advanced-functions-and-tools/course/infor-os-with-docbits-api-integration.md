# Infor OS 与 DocBits API 集成



{% embed url="https://youtu.be/0aeSDWi9cV8" %}



## 将 DocBits API 导入 Infor OS — 使用 Swagger 2.0 规范

将 Infor OS 连接到 DocBits API 时（例如创建自定义应用程序或 Infor OS 中的 API 流程），Infor 会导入 DocBits 的 API 规范。**对于 Infor OS，请使用 Swagger 2.0 规范，而不是 OpenAPI 3.0 规范。**

DocBits 以两种方言发布其 API 规范：

| 规范 | 路径 | 用途 |
| --- | --- | --- |
| OpenAPI 3.0 / 3.1 | `/openapi.json` | 标准 API 客户端、SDK 生成和常规 API 文档 |
| **Swagger 2.0** | `/openapi-swagger2.json` | **Infor OS**（以及任何使用旧版 swagger-ui 的工具） |

{% hint style="warning" %}
**为什么 Infor 要使用 Swagger 2.0？** Infor OS 使用的旧版 swagger-ui 无法根据现代 OpenAPI 3.0 表示法（包含 `format: binary` 的 `requestBody`）构建文件上传请求。它发送的上传请求**不带 multipart 边界**，因此 API 会拒绝该请求并返回：

`400 — Missing boundary in multipart`

Swagger 2.0 规范将文件上传声明为 `in: formData, type: file`，Infor 的 swagger-ui 可以正确构建此请求（包含边界）。端点和数据均相同，只有规范方言不同。
{% endhint %}

### 如何获取 Swagger 2.0 URL

1. 在浏览器中打开 DocBits API 文档（例如 `https://api.docbits.com/docs`）。
2. 在页面顶部打开**规范下拉菜单**，然后选择 **Swagger 2.0 (Infor OS)**。
3. 复制该规范显示的 URL — 它是 DocBits API 基础 URL 后接 `/openapi-swagger2.json`。

在 Infor OS 要求提供 API / Swagger 规范的任何位置使用此 URL。从下拉菜单中复制 URL，可确保使用适合你所在区域和环境的主机。

{% hint style="info" %}
集成的其他所有内容 — 身份验证（API 密钥 / 令牌）、端点和有效负载 — 均保持不变。只有导入 Infor 的规范方言不同。
{% endhint %}
