# O365 租户

## 在 Azure AD 中注册应用

<mark style="color:red;">**注意**</mark>：这些权限可能需要管理员授权。

1. 使用您的凭据登录 [Azure 门户](https://portal.azure.com/)。
2. 在 Azure 服务中找到并打开 Azure Active Directory（也称为 Azure AD）。

<figure><img src="../../../../.gitbook/assets/o365_tenant_1.png" alt="Azure 门户搜索和服务列表中的 Azure Active Directory 条目"><figcaption></figcaption></figure>

3. 在 **Manage** 部分中，选择 **App registrations**。

<figure><img src="../../../../.gitbook/assets/o365_tenant_2.png" alt="Azure Active Directory 概述页，左侧菜单显示 Manage 区域和 App registrations 条目"><figcaption></figcaption></figure>

4. 在 App registrations 页面中，点击 **+ New registration**。

<figure><img src="../../../../.gitbook/assets/o365_tenant_3.png" alt="App registrations 页面，工具栏中显示 + New registration 按钮"><figcaption></figcaption></figure>

5. 此时会显示 **Register an application** 页面。在 **Name** 中输入应用面向用户显示的名称。

<figure><img src="../../../../.gitbook/assets/o365_tenant_4.png" alt="Register an application 表单，显示 Name 字段及其显示名称的帮助文本"><figcaption></figcaption></figure>

6. 根据需要选择以下帐户类型之一：

* **Accounts in any organizational directory (Any Azure AD directory Multitenant) and personal Microsoft accounts (e.g. Skype, Xbox)**（任何组织目录中的账户〔任何 Azure AD 目录，多租户〕及个人 Microsoft 账户，例如 Skype、Xbox）
* **Accounts in any organizational directory (Any Azure AD directory Multitenant)**（任何组织目录中的帐户，即任何 Azure AD 目录中的多租户帐户）

<figure><img src="../../../../.gitbook/assets/o365_tenant_5.png" alt="Supported account types 列表，显示单租户、多租户和个人 Microsoft 账户选项"><figcaption></figcaption></figure>

7. 保持 **Redirect URI (optional)** 选项不变。

<figure><img src="../../../../.gitbook/assets/o365_tenant_6.png" alt="Register an application 表单，显示支持的账户类型并已选中多租户选项"><figcaption></figcaption></figure>

8. 点击 **Register** 完成应用注册。随后会返回新应用的页面。
9. 在应用页面中找到 **Application (client) ID**。复制此 ID，以便在为 **DocBits** 配置电子邮件导入时使用。

<figure><img src="../../../../.gitbook/assets/o365_tenant_7.png" alt="注册表单的 Redirect URI (optional) 区域及其下方的 Register 按钮"><figcaption></figcaption></figure>

10. 在左侧面板中选择 **Certificates & secrets**：

<figure><img src="../../../../.gitbook/assets/o365_tenant_8.png" alt="已注册应用程序的概述页，显示 Display name、Application (client) ID 以及 Delete 和 Endpoints 按钮"><figcaption></figcaption></figure>

11. 在 **Certificates & secrets** 页面中，点击 **Client secrets** 部分下的 **+ New client secret** 按钮：

<figure><img src="../../../../.gitbook/assets/o365_tenant_9.png" alt="已注册应用程序左侧菜单中的 Certificates & secrets 条目"><figcaption></figcaption></figure>

12. 在 **Add a client secret** 对话框中，点击 **Add** 按钮：

<figure><img src="../../../../.gitbook/assets/o365_tenant_10.png" alt="Client secrets 区域及其说明，并提示尚未创建任何客户端密码"><figcaption></figcaption></figure>

建议填写描述，以便在多个密钥中识别此密钥（目前每个应用最多可创建 2 个密钥）。

<figure><img src="../../../../.gitbook/assets/o365_tenant_11.png" alt="Add a client secret 对话框，显示 Description 字段以及 1 年、2 年和永不过期的选项"><figcaption></figcaption></figure>

<mark style="color:red;">**注意**</mark>：请根据公司的策略选择过期日期。密钥过期后，需要创建新的客户端密钥，并在之前使用该密钥的每项电子邮件配置中指定新密钥。

13. 新生成的客户端密钥将会显示。复制此客户端密钥，以便在配置 DocBits 电子邮件导入时使用。

<figure><img src="../../../../.gitbook/assets/o365_tenant_12.png" alt="Client secrets 表格，显示已创建的密码、到期日期以及值旁的复制图标"><figcaption></figcaption></figure>

**重要提示：**请确保已复制客户端密钥。关闭后将无法再次查看该密钥。

14. 在左侧面板中选择 **Authentication**。右侧将显示 **Authentication** 页面。

<figure><img src="../../../../.gitbook/assets/o365_tenant_13.png" alt="已注册应用程序左侧菜单中的 Authentication 条目"><figcaption></figcaption></figure>

15. 在 **Advanced settings** 部分中，将 **Default client type** 设置为 **Yes**。

<figure><img src="../../../../.gitbook/assets/o365_tenant_14.png" alt="Authentication 页面的 Advanced settings 区域，Default client type 设为 Yes 以作为公共客户端"><figcaption></figcaption></figure>

16. 点击 **Save** 以确认更改。

<figure><img src="../../../../.gitbook/assets/o365_tenant_15.png" alt="Authentication 页面，工具栏中显示 Save 和 Discard 按钮"><figcaption></figcaption></figure>

17. 在左侧面板中选择 **API permissions**。随后会显示 API permissions 页面。

<figure><img src="../../../../.gitbook/assets/o365_tenant_16.png" alt="已注册应用程序左侧菜单中的 API permissions 条目"><figcaption></figcaption></figure>

18. 默认情况下，**Microsoft Graph** 的 **User.Read** 权限已存在，请保持不变。

<figure><img src="../../../../.gitbook/assets/o365_tenant_17.png" alt="API permissions 表格，显示 Microsoft Graph 的委托权限 User.Read"><figcaption></figcaption></figure>

<mark style="color:red;">**注意**</mark>：此权限为必需权限。如果没有此权限，请按照下方添加 **Mail.ReadWrite** 权限的步骤添加该权限。

19. 点击 **+ Add a permission**。这将打开 **Request API permissions** 面板。

<figure><img src="../../../../.gitbook/assets/o365_tenant_18.png" alt="Configured permissions 面板，显示 + Add a permission 按钮和空的权限列表"><figcaption></figcaption></figure>

20. 点击 **Microsoft Graph**。

<figure><img src="../../../../.gitbook/assets/o365_tenant_19.png" alt="Request API permissions 面板，在常用 Microsoft API 中显示 Microsoft Graph 条目"><figcaption></figcaption></figure>

21. 从两个子类别中选择 **App Permissions**。

<figure><img src="../../../../.gitbook/assets/o365_tenant_20.png" alt="Microsoft Graph 权限面板，可在 Delegated permissions 和 Application permissions 之间选择"><figcaption></figcaption></figure>

22. 在搜索框中输入 **Mail.ReadWrite**。勾选该权限对应的 **Mail.ReadWrite** 复选框。

<figure><img src="../../../../.gitbook/assets/o365_tenant_21.png" alt="Request API permissions 面板，权限搜索中已输入 Mail.ReadWrite 并显示匹配的 Mail 权限"><figcaption></figcaption></figure>

23. 面板底部将启用 **Add permissions** 按钮。点击 **Add permissions**。

<figure><img src="../../../../.gitbook/assets/o365_tenant_22.png" alt="Request API permissions 面板，Mail.ReadWrite 复选框已选中，Add permissions 按钮可用"><figcaption></figcaption></figure>

24. 这会将 **Mail.ReadWrite** 权限添加到应用的 **Configured permissions** 列表中。

<mark style="color:red;">**注意**</mark>：可能需要管理员权限。管理员必须授权应用使用这些权限。授权后，授予状态将如下所示：

<figure><img src="../../../../.gitbook/assets/o365_tenant_23.png" alt="Configured permissions 面板，显示 Mail.ReadWrite 权限和用于该租户的 Grant admin consent 按钮"><figcaption></figcaption></figure>
