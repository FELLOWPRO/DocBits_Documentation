---
description: 使用 Microsoft 登录 DocBits，无需单独设置密码
---

# Azure SSO

### 在 Azure AD 中创建 SAML SSO

按照以下步骤在 Azure AD 中添加 SAML SSO：

*   在 Azure 中，前往 \`Azure Active Directory\` 控制台

    ![Azure门户导航窗格，包含Resource groups、All resources和Azure Active Directory等收藏夹](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_1.png)
* 在左侧面板中，点击 \`Enterprise applications\`

![Azure Active Directory左侧面板，包含Manage下的Users、Groups、Roles and administrators和Enterprise applications条目](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_2.png)

* 点击 \`+ New application

<figure><img src="../../../../../../.gitbook/assets/image (311).png" alt="Azure的Add Assignment对话框，显示2 users selected、2 groups selected，且Select Role设置为User"><figcaption></figcaption></figure>

* 点击 \`+ Create your own application\`

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (312).png" alt="Azure中的企业应用程序概览菜单，Manage条目包括Properties、Owners、Users and groups、Single sign-on和Provisioning"><figcaption></figcaption></figure></div>

* 输入应用名称。其余选项保留默认设置。

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_5.png" alt="Azure中Create your own application对话框，应用名称为MyApplication并显示应用程序集成选项"><figcaption></figcaption></figure>

* 点击 \`Create\`

### 将用户分配到 SSO 配置

接下来，将用户或组分配到 SSO 配置。

**重要提示**：你应已在 Azure AD 中创建用户和组。如果还没有用户或组，请先创建，然后再继续。

* 在 \`Getting Started\` 下，点击 \`Assign Users and Groups\`。
* 点击 \`+ Add user\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_6.png" alt="Azure中MyApplication的Users and groups页面，包含Add user、Edit和Remove按钮以及空的Display Name列表" width="563"><figcaption></figcaption></figure>

* 选择要分配到此 SSO 配置的用户和组。这些用户将能够通过 SSO 在 DocBits 中进行身份验证。

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_7.png" alt="Azure中的用户和组选择面板，包含Daniel用户列表和Selected items面板"><figcaption></figcaption></figure>

* 点击 \`Select\`
* 确认选择无误后，点击 \`Assign\`

![Azure的Add Assignment对话框，显示2 users selected、2 groups selected，且Select Role设置为User](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_8.png)

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (313).png" alt="Azure中Create your own application对话框，应用名称为MyApplication并显示应用程序集成选项"><figcaption></figcaption></figure></div>

* 前往 \`Groups\` 视图列表，找到已分配的组。

### 在 Azure 中设置 SSO

接下来，需要在 Azure 中完成单点登录设置。\\

* 在左侧面板中，点击 \`Single sign-on\`

![Azure中的企业应用程序概览菜单，Manage条目包括Properties、Owners、Users and groups、Single sign-on和Provisioning](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_10.png)

* 点击 \`SAML\`

![Azure中的SAML选项卡片，描述使用Security Assertion Markup Language协议实现丰富而安全的身份验证](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_11.png)

* 点击 \`Upload metadata file\`

![Azure中的SAML-based Sign-on面板，包含Upload metadata file和Set up Single Sign-On](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_12.png)

* 上传 DocBits **metadata.xml**。你可以在 DocBits 账户的“设置”菜单中，前往 **Integration** 下的 **SSO Service Provider Settings** 找到该文件。

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_Metadata-1024x216.png" alt="SSO Service Provider Settings页面，包含Tenant ID、Entity ID以及SSO Url、SLO Url和Metadata Url字段"><figcaption></figcaption></figure>

* 编辑 \`Basic SAML Configuration\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.png" alt="设置基于SAML的单一登录的屏幕，其中显示Basic SAML Configuration以及Identifier、Reply URL、Sign on URL和Logout Url"><figcaption></figcaption></figure>

* 检查 \`Entity ID\`、\`ACS URL\`、\`Sign on URL\` 和 \`Logout URL\` 是否已正确填入。

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.1.png" alt="Azure中的Basic SAML Configuration编辑器，包含Identifier、Reply URL、Sign on URL、Relay State和Logout Url字段以及Save按钮"><figcaption></figcaption></figure>

* 下载新生成的 **Federation Metadata XML**。

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_14.png" alt="Azure中的SAML Signing Certificate部分，包含指纹、到期日期以及Certificate (Raw)和Federation Metadata XML的下载链接"><figcaption></figcaption></figure>

* 将 FederationMetadata.xml 上传到 DocBits 账户的 **Identity Service Provider Settings**。你可以在“设置”菜单的 **Integration** 下找到该设置。

\\

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_15-1024x204.png" alt="DocBits中的Identity Service Provider Settings对话框，其中包含Tenant ID FELLOWPRO_PRD和Upload file按钮"><figcaption></figcaption></figure>
