---
description: 使用 Microsoft 登录 DocBits，无需单独设置密码
---

# Azure 单点登录

### 在 Azure AD 中创建 SAML SSO

按照以下步骤在 Azure AD 中添加 SAML SSO：

*   在 Azure 中，前往 \`Azure Active Directory\` 控制台

    ![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_1.png)
* 在左侧面板中，点击 \`Enterprise applications\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_2.png)

* 点击 \`+ New application

<figure><img src="../../../../../../.gitbook/assets/image (311).png" alt=""><figcaption></figcaption></figure>

* 点击 \`+ Create your own application\`

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (312).png" alt=""><figcaption></figcaption></figure></div>

* 输入应用名称。其余选项保留默认设置。

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_5.png" alt=""><figcaption></figcaption></figure>

* 点击 \`Create\`

### 将用户分配到 SSO 配置

接下来，将用户或组分配到 SSO 配置。

**重要提示**：你应已在 Azure AD 中创建用户和组。如果还没有用户或组，请先创建，然后再继续。

* 在 \`Getting Started\` 下，点击 \`Assign Users and Groups\`。
* 点击 \`+ Add user\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_6.png" alt="" width="563"><figcaption></figcaption></figure>

* 选择要分配到此 SSO 配置的用户和组。这些用户将能够通过 SSO 在 DocBits 中进行身份验证。

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_7.png" alt=""><figcaption></figcaption></figure>

* 点击 \`Select\`
* 确认选择无误后，点击 \`Assign\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_8.png)

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (313).png" alt=""><figcaption></figcaption></figure></div>

* 前往 \`Groups\` 视图列表，找到已分配的组。

### 在 Azure 中设置 SSO

接下来，需要在 Azure 中完成单点登录设置。\\

* 在左侧面板中，点击 \`Single sign-on\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_10.png)

* 点击 \`SAML\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_11.png)

* 点击 \`Upload metadata file\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_12.png)

* 上传 DocBits **metadata.xml**。你可以在 DocBits 账户的“设置”菜单中，前往 **Integration** 下的 **SSO Service Provider Settings** 找到该文件。

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_Metadata-1024x216.png" alt=""><figcaption></figcaption></figure>

* 编辑 \`Basic SAML Configuration\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.png" alt=""><figcaption></figcaption></figure>

* 检查 \`Entity ID\`、\`ACS URL\`、\`Sign on URL\` 和 \`Logout URL\` 是否已正确填入。

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.1.png" alt=""><figcaption></figcaption></figure>

* 下载新生成的 **Federation Metadata XML**。

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_14.png" alt=""><figcaption></figcaption></figure>

* 将 FederationMetadata.xml 上传到 DocBits 账户的 **Identity Service Provider Settings**。你可以在“设置”菜单的 **Integration** 下找到该设置。

\\

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_15-1024x204.png" alt=""><figcaption></figcaption></figure>
