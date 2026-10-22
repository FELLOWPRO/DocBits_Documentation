---
description: 使用 Microsoft 登录 DocBits，无需单独设置密码
---

# Azure SSO

### 在 Azure AD 中创建 SAML SSO

按照以下步骤在 Azure AD 中添加 SAML SSO：

*   在 Azure 中，前往 \`Azure Active Directory\` 控制台

    ![Azure 门户主页，左侧导航的收藏夹中包含 Azure Active Directory](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_1.png)
* 在左侧面板中，点击 \`Enterprise applications\`

![Azure Active Directory 的左侧导航，包含管理分组和企业应用程序条目](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_2.png)

* 点击 \`+ New application

<figure><img src="../../../../../../.gitbook/assets/image (311).png" alt="Azure Active Directory 的企业应用程序页面，包含所有应用程序列表和新建应用程序按钮"><figcaption></figcaption></figure>

* 点击 \`+ Create your own application\`

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (312).png" alt="浏览 Azure AD 库对话框，包含创建你自己的应用程序和请求新的库应用程序按钮以及搜索应用程序字段"><figcaption></figcaption></figure></div>

* 输入应用名称。其余选项保留默认设置。

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_5.png" alt="创建你自己的应用程序对话框，名称为 MyApplication，选中选项为集成你在库中找不到的任何其他应用程序"><figcaption></figcaption></figure>

* 点击 \`Create\`

### 将用户分配到 SSO 配置

接下来，将用户或组分配到 SSO 配置。

**重要提示**：你应已在 Azure AD 中创建用户和组。如果还没有用户或组，请先创建，然后再继续。

* 在 \`Getting Started\` 下，点击 \`Assign Users and Groups\`。
* 点击 \`+ Add user\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_6.png" alt="应用程序 MyApplication 的用户和组页面，包含添加用户、编辑、删除和更新按钮以及未找到任何应用程序分配的消息" width="563"><figcaption></figcaption></figure>

* 选择要分配到此 SSO 配置的用户和组。这些用户将能够通过 SSO 在 DocBits 中进行身份验证。

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_7.png" alt="用户选择面板，列出多个用户，并显示已选择部分"><figcaption></figcaption></figure>

* 点击 \`Select\`
* 确认选择无误后，点击 \`Assign\`

![租户 chimdustries 的添加分配对话框，显示已选择 2 个用户和 2 个组](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_8.png)

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (313).png" alt="Azure Active Directory 分配对话框中带有绿色边框的分配按钮"><figcaption></figcaption></figure></div>

* 前往 \`Groups\` 视图列表，找到已分配的组。

### 在 Azure 中设置 SSO

接下来，需要在 Azure 中完成单点登录设置。\\

* 在左侧面板中，点击 \`Single sign-on\`

![企业应用程序 MyApplication 的左侧导航，包含单一登录条目](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_10.png)

* 点击 \`SAML\`

![单一登录页面，显示 SAML 图块以及通过 SAML 协议为应用程序提供安全可靠身份验证的说明文字](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_11.png)

* 点击 \`Upload metadata file\`

![基于 SAML 的登录页面，包含上传元数据文件和设置单一登录链接](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_12.png)

* 上传 DocBits **metadata.xml**。你可以在 DocBits 账户的“设置”菜单中，前往 **Integration** 下的 **SSO Service Provider Settings** 找到该文件。

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_Metadata-1024x216.png" alt="DocBits 中的 SSO 服务提供商设置，包含实体 ID、SLO URI 和 SSO URI 以及证书下载和下载元数据按钮"><figcaption></figcaption></figure>

* 编辑 \`Basic SAML Configuration\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.png" alt="使用 SAML 设置单一登录页面，包含基本 SAML 配置部分以及标识符实体 ID、回复 URL、登录 URL、中继状态和注销 URL 字段"><figcaption></figcaption></figure>

* 检查 \`Entity ID\`、\`ACS URL\`、\`Sign on URL\` 和 \`Logout URL\` 是否已正确填入。

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.1.png" alt="Azure 中的基本 SAML 配置，包含说明文字、设为租户 SAML 元数据 URL 的标识符实体 ID 以及作为断言消费者服务 URL 的回复 URL"><figcaption></figcaption></figure>

* 下载新生成的 **Federation Metadata XML**。

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_14.png" alt="SAML 签名证书部分，包含状态为活动、指纹、到期日期、通知电子邮件以及原始证书和联合身份验证元数据 XML 下载链接"><figcaption></figcaption></figure>

* 将 FederationMetadata.xml 上传到 DocBits 账户的 **Identity Service Provider Settings**。你可以在“设置”菜单的 **Integration** 下找到该设置。

\\

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_15-1024x204.png" alt="DocBits 中的身份服务提供商设置，包含租户 ID、上传文件和导入按钮以及现有文件的条目"><figcaption></figcaption></figure>
