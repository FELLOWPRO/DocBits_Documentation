# OAuth Office365



{% embed url="https://youtu.be/Vvy38N_5g3Y" %}

在这里，只需输入所需的子组织，然后按“Authenticate”

<figure><img src="../../../../.gitbook/assets/a-email-oauth-office365-authenticate-en-20261006.png" alt="电子邮件服务器设置对话框，协议为 OAuth Office365，包含文档路由选项和 Authenticate 按钮。"><figcaption><p>选择路由，然后按 Authenticate。</p></figcaption></figure>

系统会带您前往 Microsoft 页面，您需要在该页面输入一段代码。

![](https://lh7-us.googleusercontent.com/Q76mIMXr5bWCrcu_6TOKDrh6yQIMESIrFvEcfvqg7mJp-K_4ES2e5ekPY4Ghhwxym-uRKz_QVCHyqk2u5onyoCCmg7fMbt3mnIUyCrc8XT4jBGn9ueEYij3DRg1-oODWHd-vDfM9FfbU3omF6RJJKsE)

返回 DocBits 即可找到这段代码，代码会像下图所示显示在那里。只需复制代码并将其输入 Microsoft 页面。之后，您需要输入自己的 Microsoft 凭据。

<figure><img src="../../../../.gitbook/assets/a-email-oauth-office365-code-en-20261006.png" alt="电子邮件服务器设置对话框，显示 Microsoft 身份验证代码、Copy 按钮和 Finish authentication 按钮。"><figcaption><p>Microsoft 代码会显示在 DocBits 中。</p></figcaption></figure>

按 FINISH AUTHENTICATION 按钮，系统会带您前往此菜单

<figure><img src="../../../../.gitbook/assets/a-email-oauth-office365-options-en-20261006.png" alt="身份验证完成后的电子邮件服务器设置对话框，包含 Use Folder、Use Shared Mailbox 和 Move Emails To Other Folder 开关。"><figcaption><p>身份验证完成后的选项。</p></figcaption></figure>

**Use Folder**

如果您使用的文件夹不是收件箱，请启用滑块，然后输入文件夹名称。

**Use Shared Mailbox**

如果您希望电子邮件导入功能访问共享邮箱中的收件箱或文件夹，请启用滑块，然后在此输入电子邮件地址。

**Move imported emails to trash**

如果您希望导入所有电子邮件（而不只是未读邮件），并将其移至垃圾箱，请启用此选项。否则，系统只会检查未读邮件，导入文档，将邮件标记为已读，并将其保留在当前位置。

如果收到错误消息，提示您没有权限建立此类连接，则需要由拥有 Azure 管理员权限的人员授权此连接。有关更多信息，请访问以下页面：https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal#grant-tenant-wide-admin-consent-in-enterprise-apps
