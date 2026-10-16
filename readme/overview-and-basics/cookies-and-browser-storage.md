# Cookie 与浏览器存储

针对问卷 **4.15**，于 **2026 年 10 月 16 日**核查。公共网站、DocBits 应用和本文档使用的 Cookie 与服务有所不同。

## 政策与用途

[DocBits 隐私政策](https://docbits.com/en/privacy-policy/)包含 **Cookies** 和 **Consent with Borlabs Cookie** 部分，介绍同意记录、必要功能、机器人防护、Google Analytics、广告及 Leadfeeder。分析可生成访问、页面、交互和性能报告，但收集范围不限于匿名汇总数据。网站政策本身不能确定应用的 Cookie 清单。

## Cookie 清单

**观察到**指未登录、未选择可选同意项的全新访问。**源代码**指已检查的应用代码或基础设施设置，不代表已确认每个生产响应的属性。

| Cookie / 范围 | 用途与保留期限 | 证据与安全属性 |
| --- | --- | --- |
| `__cf_bm` / 网站及应用 | Cloudflare 机器人防护；连续闲置 30 分钟 | 观察到：`Secure`、`HttpOnly`、`SameSite=None`。[Cloudflare](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cloudflare-cookies/)对时间信息以外的机器人信息加密。 |
| `pll_language` / 网站 | 语言偏好；约一年 | 观察到：`Secure`、JavaScript 可读、`SameSite=Lax`。 |
| `_lfa` / 网站 | Leadfeeder 访客及企业分析；约一年 | 观察到：JavaScript 可读、`SameSite=Lax`，此次访问中**没有 `Secure` 属性**。 |
| Borlabs 同意 Cookie / 网站 | 保存同意及撤回选择 | 隐私政策中声明；此次访问未验证名称、实际属性及期限。 |
| `session` / 身份验证服务 | 身份验证流程的会话状态 | 源代码默认：`Secure`、`HttpOnly`、`SameSite=None`；Flask 会话数据经签名，未加密。部署配置可以覆盖默认值。 |
| `dbx_td` / 身份验证服务 | MFA 成功后按用户选择记住可信设备；30 天 | 源代码：`Secure`、`HttpOnly`、`SameSite=None`；随机令牌，服务端存储其哈希值。 |
| `prod-sticky` / 生产负载均衡 | 将请求路由到相同后端；配置期限 300 秒 | 已验证基础设施设置；未验证浏览器属性。 |
| `dontAsk` / 应用 | 记住提示偏好；已检查调用未指定到期时间 | 源代码：JavaScript 可读；该调用未显式设置 `Secure` 或 `SameSite`。 |

全新访问文档时未观察到 Cookie。这是一份注明日期的观察记录，不是登录流程、可选功能或第三方嵌入内容的完整清单。政策还列出其他分析及广告服务，此次访问未确认其 Cookie。完整清单及同意机制是否生效，需要分别检查这些流程。

## 安全与分析

`Secure` 限制仅通过 HTTPS 发送；`HttpOnly` 阻止 JavaScript 读取；`SameSite` 控制跨站发送。这些属性不会加密内容。因此，笼统声称所有 Cookie 均已加密或具有相同保护并不准确。公共应用端点支持 TLS 1.2 和 1.3，详见[凭据的安全存储](secure-storage-of-credentials.md)。

浏览器存储也独立于 Cookie 使用。应用的 Grafana Faro 配置支持持久会话跟踪、错误、性能测量和跟踪信息，并可附带可用的用户与组织标识。收集是否启用取决于已部署的收集器配置，不应描述为仅匿名汇总的 Cookie 分析。语言偏好也使用本地存储。

您可以在浏览器中删除 Cookie 和存储数据，但这可能清除偏好及可信设备记录。获取最新清单或咨询隐私问题，请联系 **compliance@fellowpro.com**。
