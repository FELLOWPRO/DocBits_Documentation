# 管理通知

打开 **Settings → Email Notification** 查看您所在组织的规则。一条规则将文档状态与电子邮件模板及收件人关联起来。以下示例使用一条发票演示规则，该规则在 DocBits Sandbox 中保持**未激活**状态。

## 示例：发票已准备好进行验证

创建规则前，请先在 **Settings → Email Templates** 下为 **Invoice** 准备电子邮件模板。本例中的模板名为 **Docs Demo Invoice Notification**。该模板提供电子邮件主题和正文。

1. 在 **Email Notification** 页面上选择 **+ New**。
2. 输入 **Docs Demo Invoice Validation** 作为名称，选择 **Invoice** 作为文档类型，然后选择准备好的电子邮件模板。
3. 将状态设为 **Ready for validation**，优先级设为 **Medium**。将 **Time Unit** 设为 **MINUTES**，将 **Delay** 设为 **10**。分钟的最短延迟为五分钟。
4. 选择 **Send Email to Assigned User/Group**。如果只需发送一次消息，请开启 **Do not Repeat**。检查收件人和发送时间，然后选择 **Save**。

<figure><img src="../../../../.gitbook/assets/dbdc-164-example-form-en-20260930.png" alt="已填写的通知规则：文档类型为 Invoice，状态为 Ready for validation，延迟十分钟，收件人为指派的用户或群组"><figcaption><p>打开已保存的示例规则进行编辑。其值显示了通知的发送时间和收件人。</p></figcaption></figure>

该规则现在会显示在列表中。随后，文档示例被停用，因此其 **Actions** 菜单中显示 **Activate**。激活规则前，请在您自己的列表中检查名称、文档类型、状态、延迟时间和收件人。

<figure><img src="../../../../.gitbook/assets/dbdc-164-example-list-en-20260930.png" alt="Email Notification 列表中显示 Docs Demo Invoice Validation 示例规则，而不是空表"><figcaption><p>保存示例后，您可以在列表中找到并管理这条规则。</p></figcaption></figure>

## 编辑、激活或删除规则

打开该行的 **Actions** 菜单。选择 **Edit** 可打开规则并查看其当前值。选择 **Activate** 可启用此未激活的示例；规则处于激活状态时，则会显示 **Deactivate**。选择 **Logs** 可打开通知历史记录。选择 **Delete** 后，确认即可删除规则。激活或更改规则前，请检查收件人和发送时间。

<figure><img src="../../../../.gitbook/assets/dbdc-164-example-actions-en-20260930.png" alt="未激活的示例通知规则的 Actions 菜单，包含 Edit、Activate、Logs 和 Delete"><figcaption><p>可用操作取决于规则是否处于激活状态。</p></figcaption></figure>

如果列表显示 **No Record Found!**，请先创建规则。如果 **Document Type** 或电子邮件模板列表为空，请先配置已激活的文档类型和匹配的模板，然后再返回此表单。

有关初始设置的更多信息，请参阅[配置通知](configuring-notifications.md)。如果电子邮件未按预期送达，请参阅[故障排除](troubleshooting.md)。
