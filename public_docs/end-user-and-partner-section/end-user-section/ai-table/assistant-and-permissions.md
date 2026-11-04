# 助手与权限

[AI Table](README.md) · [表格的 Structured Output](structured-output.md)

## Assistant 与 AI 表格

在验证界面中，点击 **Assistant**（Save 旁边的灯泡图标），即可询问有关文档的问题。

<figure><img src="../../../.gitbook/assets/ai-table-assistant-panel-en.png" alt="包含问题卡片和建议问题的 Assistant 面板"><figcaption><p>Assistant 会列出尚未解决的问题，并提供可询问的问题。</p></figcaption></figure>

**Assistant 可以为表格执行的操作。** 它可以带你定位到某个表格单元格；如果你有权编辑文档，还可以设置单元格的值或添加表格行。这些操作适用于 AI Extracted table 和 Extracted table。你还可以询问 _What is still missing?_ 和 _What can I improve?_ 等问题。

<figure><img src="../../../.gitbook/assets/ai-table-assistant-improve-en.png" alt="Assistant 回答可以改进哪些内容"><figcaption><p>询问 <em>What can I improve?</em>，即可获取简短的待修正事项列表。</p></figcaption></figure>

**Assistant 不能执行的操作。** Assistant **不会**更改 AI 指令、额外列、列映射或训练。如需执行这些操作，请使用 **AI instructions** 卡片（**Suggest with Nexus**、**Test change**、**Apply**、**Save as training**）。管理员可以询问 _Is the AI set up correctly?_，以查看设置建议，例如如何将 AI 表格读取与已保存的表格规则结合使用。

### 向管理员提出规则建议

许多问题来自**字段**而非表格：始终必填但为空的电子邮件、格式错误的日期，或需要查找的供应商 ID。对于这些问题，任何可以打开文档的人都可以通过 Assistant 发送建议：

1. 询问 _What can I improve?_，或在 Assistant 中打开一张发现卡片。
2. 如果你是管理员，卡片会显示 **Apply**。如果你不是管理员，卡片会显示 _An administrator can review this proposal._，并提供 **Suggest improvement**。点击该按钮。
3. DocBits 会显示 _Your suggestion was sent to the administrators._。如果之前已有人发送相同建议，你的请求会计入该建议，而不会创建重复建议。
4. 随后，卡片会显示 **Requested**，之后状态会变为 **Implemented** 或 **Declined**（如果管理员填写了原因，也会显示原因）。

建议可以是**转换规则**、**验证规则**或**查找规则**。你可以从文档中发送建议；服务器会根据发现的问题自行生成规则草稿，因此你无需编写任何内容。每位用户每小时最多可发送 20 条建议。

{% hint style="warning" %}
你不能通过此方式建议**AI 表格指令、列映射或训练**。如果表格需要修正，请在文档中进行修改并告知管理员，或请管理员在该供应商的某份文档上点击 **Save as training**。管理员可以保存规则；参见[谁可以执行哪些操作](assistant-and-permissions.md#who-can-do-what)。
{% endhint %}

**管理员看到的内容。** 管理员会收到任务和电子邮件通知。他们可以打开 **Touchless Intelligence**，在 **Open improvements** 下找到建议（_Open_ 选项卡显示待处理建议，_History_ 选项卡显示历史记录）。点击建议后，会打开 _Improvement suggestion_ 侧边栏，其中包含示例文档和预览。管理员可以选择 **Approve** 或 **Reject**。批准时，**Switch on right away** 用于决定是否立即启用新规则；如果未启用该选项，规则会以未启用状态创建，管理员需要在规则列表中将其启用。拒绝时，管理员必须填写原因，也可以附上给请求者的备注。参见 [Touchless Intelligence](../../../administration-and-setup/analytics-dashboard/touchless-intelligence/)。

<figure><img src="../../../.gitbook/assets/ai-table-touchless-open-improvements-en.png" alt="Touchless Intelligence 中的 Open improvements 区域，当前为空"><figcaption><p>管理员可以在 **Open improvements** 下找到建议。</p></figcaption></figure>

## 谁可以执行哪些操作 <a id="who-can-do-what"></a>

| 操作 | 权限 |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 重新映射列、**Delete column**、**Amount Formatting**、**Extract From**、**Test change**、**Apply**、编辑行 | 所有可以编辑文档的用户 |
| **Save as training** | 所有可以编辑文档的用户均可使用，但组织设置 **Save extraction rules (Admin only)** 开启时除外。开启后，只有组织管理员可以保存规则；其他用户会收到错误消息。 |
| **Add new table column**（添加新的表格列） | 管理员 |
| 通过 Assistant 提出规则建议 | 所有可以打开文档的用户 |
| 批准或拒绝建议 | 管理员 |
| **Explain extraction**、**AI advice** | 其角色有权访问 Analytics Dashboard 模块的用户 |
