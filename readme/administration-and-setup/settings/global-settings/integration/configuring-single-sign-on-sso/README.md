# 配置单点登录（SSO）

在 DocBits 中配置单点登录（SSO）需要几个步骤。以下是分步指南：

**访问 SSO 设置：**

<figure><img src="../../../../../.gitbook/assets/image (198).png" alt=""><figcaption></figcaption></figure>

* 以管理员身份登录 DocBits 账户。
* 前往设置，找到 Single Sign-On 或 SSO。

**配置 SSO 参数：**

<figure><img src="../../../../../.gitbook/assets/image (195).png" alt=""><figcaption><p>SSO 服务提供商设置</p></figcaption></figure>

* 输入所需的 SSO 参数，例如实体 ID、单点注销（SLO）URL 和单点登录（SSO）URL。
* 实体 ID 是服务或应用程序的唯一标识符。
* SLO URL 是用于单点注销的 URL，可在需要时将用户从所有服务中注销。
* SSO URL 是将用户重定向到身份提供商以进行身份验证的 URL。

**下载证书和元数据：**

<figure><img src="../../../../../.gitbook/assets/image (196).png" alt=""><figcaption></figcaption></figure>

* 身份提供商（IdP）通常会提供证书，DocBits 使用该证书验证 SAML 身份验证响应。
* 下载证书并妥善保管。
* 元数据下载文件包含 SSO 集成所需的全部配置信息，包括实体 ID、SSO URL、证书信息等。
* 下载元数据并保存在本地，或提供给身份提供商。

**身份提供商（IdP）配置：**

<figure><img src="../../../../../.gitbook/assets/image (197).png" alt=""><figcaption><p>身份服务提供商设置</p></figcaption></figure>

* 登录身份提供商，并配置用于 SAML 集成的应用程序或服务。
* 使用已下载的元数据或手动输入的 SSO 参数，将 DocBits 添加为受信任的应用程序或服务。
* 确保 IdP 的配置与 DocBits 中指定的 SSO 参数一致。

**测试 SSO 集成：**

* 配置完成后，测试 SSO 集成，确保用户可以通过 SSO 成功登录 DocBits。
* 还要验证单点注销是否正常工作：从 DocBits 注销，并确认同时也已从其他已连接的服务中注销。

正确配置 SSO 后，用户即可使用现有凭据无缝登录 Docbits，从而改善用户体验并提高安全性。
