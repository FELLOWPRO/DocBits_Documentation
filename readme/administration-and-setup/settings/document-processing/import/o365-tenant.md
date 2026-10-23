# O365 租户

## 在 Azure AD 中注册应用

<mark style="color:red;">**注意**</mark>：这些权限可能需要管理员授权。

1. 使用您的凭据登录 [Azure 门户](https://portal.azure.com/)。
2. 在 Azure 服务中找到并打开 Azure Active Directory（也称为 Azure AD）。

<figure><img src="../../../../.gitbook/assets/o365_tenant_1.png" alt="Azure门户页面，包含Azure Active Directory条目和服务搜索栏"><figcaption></figcaption></figure>

3. 在 **Manage** 部分中，选择 **App registrations**。

<figure><img src="../../../../.gitbook/assets/o365_tenant_2.png" alt="Azure Active Directory概述页面，左侧Manage菜单已打开且App registrations被高亮显示"><figcaption></figcaption></figure>

4. 在 App registrations 页面中，点击 **+ New registration**。

<figure><img src="../../../../.gitbook/assets/o365_tenant_3.png" alt="Azure中的App registrations屏幕，工具栏中有New registration按钮以及已注册应用的列表"><figcaption></figcaption></figure>

5. 此时会显示 **Register an application** 页面。在 **Name** 中输入应用面向用户显示的名称。

<figure><img src="../../../../.gitbook/assets/o365_tenant_4.png" alt="Azure门户中的Register an application屏幕，其中新应用的Name字段为空"><figcaption></figcaption></figure>

6. 根据需要选择以下帐户类型之一：

* **Accounts in any organizational directory (Any Azure AD directory Multitenant) and personal Microsoft accounts (e.g. Skype, Xbox)**（任何组织目录中的账户〔任何 Azure AD 目录，多租户〕及个人 Microsoft 账户，例如 Skype、Xbox）
* **Accounts in any organizational directory (Any Azure AD directory Multitenant)**

<figure><img src="../../../../.gitbook/assets/o365_tenant_5.png" alt="Register an application屏幕，包含针对组织目录和个人Microsoft账户的受支持账户类型单选选项"><figcaption></figcaption></figure>

7. 保持 **Redirect URI (optional)** 选项不变。

<figure><img src="../../../../.gitbook/assets/o365_tenant_6.png" alt="Register an application屏幕，底部的Redirect URI (optional)部分保持不变"><figcaption></figcaption></figure>

8. 点击 **Register** 完成应用注册。随后会返回新应用的页面。
9. 在应用页面中找到 **Application (client) ID**。复制此 ID，以便在为 **DocBits** 配置电子邮件导入时使用。

<figure><img src="../../../../.gitbook/assets/o365_tenant_7.png" alt="已注册应用概览页面，显示Display name Ephesoft OAuth2 App和Application client ID"><figcaption></figcaption></figure>

10. 在左侧面板中选择 **Certificates & secrets**：

<figure><img src="../../../../.gitbook/assets/o365_tenant_8.png" alt="已注册应用概览页面，在左侧面板的Manage部分中选中了Certificates and secrets"><figcaption></figcaption></figure>

11. 在 **Certificates & secrets** 页面中，点击 **Client secrets** 部分下的 **+ New client secret** 按钮：

<figure><img src="../../../../.gitbook/assets/o365_tenant_9.png" alt="Certificates &amp; secrets屏幕，其中包含Client secrets部分和+ New client secret按钮"><figcaption></figcaption></figure>

12. 在 **Add a client secret** 对话框中，点击 **Add** 按钮：

<figure><img src="../../../../.gitbook/assets/o365_tenant_10.png" alt="Add a client secret对话框，包含Description和Expires字段以及Add按钮"><figcaption></figcaption></figure>

建议填写描述，以便在多个密钥中识别此密钥（目前每个应用最多可创建 2 个密钥）。

<figure><img src="../../../../.gitbook/assets/o365_tenant_11.png" alt="客户端密钥列表，显示新密钥及其描述、Value和Expires列"><figcaption></figcaption></figure>

<mark style="color:red;">**注意**</mark>：请根据公司的策略选择过期日期。密钥过期后，需要创建新的客户端密钥，并在之前使用该密钥的每项电子邮件配置中指定新密钥。

13. 新生成的客户端密钥将会显示。复制此客户端密钥，以便在配置 DocBits 电子邮件导入时使用。

<figure><img src="../../../../.gitbook/assets/o365_tenant_12.png" alt="Certificates &amp; secrets中的Client secrets部分，生成的密钥Value可随时复制"><figcaption></figcaption></figure>

**重要提示：**请确保已复制客户端密钥。关闭后将无法再次查看该密钥。

14. 在左侧面板中选择 **Authentication**。右侧将显示 **Authentication** 页面。

<figure><img src="../../../../.gitbook/assets/o365_tenant_13.png" alt="从左侧面板打开的应用注册Authentication屏幕，右侧显示平台设置"><figcaption></figcaption></figure>

15. 在 **Advanced settings** 部分中，将 **Default client type** 设置为 **Yes**。

<figure><img src="../../../../.gitbook/assets/o365_tenant_14.png" alt="Authentication屏幕的Advanced settings部分，Default client type选项设置为Yes"><figcaption></figcaption></figure>

16. 点击 **Save** 以确认更改。

<figure><img src="../../../../.gitbook/assets/o365_tenant_15.png" alt="应用注册顶栏，在启用默认客户端类型后Save按钮高亮显示"><figcaption></figcaption></figure>

17. 在左侧面板中选择 **API permissions**。随后会显示 API permissions 页面。

<figure><img src="../../../../.gitbook/assets/o365_tenant_16.png" alt="从左侧面板打开的API permissions屏幕，其中显示该应用的已配置权限"><figcaption></figcaption></figure>

18. 默认情况下，**Microsoft Graph** 的 **User.Read** 权限已存在，请保持不变。

<figure><img src="../../../../.gitbook/assets/o365_tenant_17.png" alt="已配置权限列表，显示Microsoft Graph的默认委托权限User.Read"><figcaption></figcaption></figure>

<mark style="color:red;">**注意**</mark>：此权限为必需权限。如果没有此权限，请按照下方添加 **Mail.ReadWrite** 权限的步骤添加该权限。

19. 点击 **+ Add a permission**。这将打开 **Request API permissions** 面板。

<figure><img src="../../../../.gitbook/assets/o365_tenant_18.png" alt="Request API permissions面板，包含Microsoft APIs、APIs my organization uses以及+ Add a permission操作流程"><figcaption></figcaption></figure>

20. 点击 **Microsoft Graph**。

<figure><img src="../../../../.gitbook/assets/o365_tenant_19.png" alt="Request API permissions面板，Microsoft Graph在常用Microsoft API中被高亮显示"><figcaption></figcaption></figure>

21. 从两个子类别中选择 **App Permissions**。

<figure><img src="../../../../.gitbook/assets/o365_tenant_20.png" alt="Microsoft Graph的Request API permissions面板，包含Delegated permissions和Application permissions选项"><figcaption></figcaption></figure>

22. 在搜索框中输入 **Mail.ReadWrite**。勾选该权限对应的 **Mail.ReadWrite** 复选框。

<figure><img src="../../../../.gitbook/assets/o365_tenant_21.png" alt="应用程序权限搜索框，已输入Mail.ReadWrite并勾选了Mail.ReadWrite权限复选框"><figcaption></figcaption></figure>

23. 面板底部将启用 **Add permissions** 按钮。点击 **Add permissions**。

<figure><img src="../../../../.gitbook/assets/o365_tenant_22.png" alt="Request API permissions面板，选中Mail.ReadWrite权限，底部为Add permissions按钮"><figcaption></figcaption></figure>

24. 这会将 **Mail.ReadWrite** 权限添加到应用的 **Configured permissions** 列表中。

<mark style="color:red;">**注意**</mark>：可能需要管理员权限。管理员必须授权应用使用这些权限。授权后，授予状态将如下所示：

<figure><img src="../../../../.gitbook/assets/o365_tenant_23.png" alt="已配置权限列表，显示已添加的Mail.ReadWrite应用程序权限及其已授予状态"><figcaption></figcaption></figure>
