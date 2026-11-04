# AI 指令

[AI Table](README.md) · [表格的 Structured Output](structured-output.md)

## 向 AI 提供指令 <a id="give-the-ai-instructions"></a>

表格下方的 **AI instructions** 卡片用于告诉 AI 应如何调整处理方式。卡片包含两个输入框和四个常用按钮。

<figure><img src="../../../.gitbook/assets/ai-table-instructions-en.png" alt="包含提示、额外列和按钮的 AI instructions 卡片"><figcaption><p>AI instructions 卡片。</p></figcaption></figure>

* **Prompt for the AI.** 用通俗语言逐行写入指令。输入 **@** 可插入列名称，让 AI 明确你指的是哪一列。
* **Extra columns for the AI.** 选择 AI 除常规列外还必须返回的列。
* **训练状态。** 如果最近一次运行使用了已保存的训练，状态标签会显示 **Training applied**；否则显示 **No training applied**。

<figure><img src="../../../.gitbook/assets/ai-table-prompt-mention-en.png" alt="输入 @ 时会打开表格列列表"><figcaption><p>在提示中输入 <strong>@</strong> 可选择列。只要内容发生更改，<strong>Test change</strong> 就会显示在 <strong>Apply</strong> 旁边。</p></figcaption></figure>

{% hint style="warning" %}
更改提示会让 AI 重新读取表格，并且可能影响所有列，而不只是你想修改的那一列。之后请检查整个表格。
{% endhint %}

### 使用 Nexus 提供建议

不确定该写什么？点击 **Suggest with Nexus**。DocBits 会分析当前文档的提取结果，并提出指令或额外列建议。只有点击 **Insert**（将内容添加到提示中）或 **Add column** 后，更改才会应用。

<figure><img src="../../../.gitbook/assets/ai-table-nexus-suggest-en.png" alt="带有 Insert 按钮的 Nexus 建议"><figcaption><p>Nexus 提供的建议。<strong>Insert</strong> 会将建议复制到提示中。</p></figcaption></figure>

如果你的组织已关闭 AI 顾问功能，DocBits 会告知你，而不是提供建议。

### 测试、应用和保存：各按钮的功能

| 按钮 | 会发生什么 | 是否保存供后续文档使用？ |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **Test change**                             | 运行你的更改并显示对比结果。**不会写入任何内容**，既不会写入文档，也不会保存为规则。 | 否 |
| **Apply**                                   | 根据你的更改重新读取表格，并将结果放入编辑器中的当前文档。只有保存文档后，更改才会生效。 | 否 |
| **Save as training**（保存为训练样本；工具提示 _Save Rules_） | 保存当前供应商版式的提示、额外列、列映射、隐藏列、金额格式和 **Extract From** 设置。之后，该版式的新文档会采用相同方式读取。 | 是 |
| **Delete**（工具提示 _Delete Rules_）         | 删除当前供应商版式已保存的表格规则，无需额外确认，然后在不使用这些规则的情况下重新运行 AI。它也会删除为同一版式保存的传统表格训练。 | 删除这些规则 |
| **Export**                                  | 将表格下载为 CSV 文件。 | 否 |

{% hint style="info" %}
标题重新映射、**Delete column**、**Amount Formatting**、**Extract From** 和 **Restore Table Column** 的行为与 **Apply** 相同：它们会立即为当前文档重新生成表格，并随文档一起保存，而不会保存为规则。只有 **Save as training** 才会训练 DocBits 以处理后续文档。
{% endhint %}

如果文档中的行已与采购订单匹配，点击 Apply 和 Save 时会收到警告：**你可能会丢失 PO 关联**。选择 **Done** 继续，然后重新进行匹配。

<figure><img src="../../../.gitbook/assets/ai-table-test-change-en.png" alt="对比当前表格和新结果的 Test change 对话框"><figcaption><p><strong>Test change</strong> 对话框会将新结果与当前显示的表格进行对比。</p></figcaption></figure>

**Test change** 对话框会统计可能发生的更改：已更改单元格、新增列、缺失列和重新分配的列。每个单元格都会标记为 **Added**、**Changed**、**Missing**、**Reassigned** 或 **Unchanged**。对话框底部会列出此次运行的依据：_Effective hints_、_Selected training_、_Column policy_ 和 _Request overrides used_。选择 **Apply result to this document** 以应用结果（然后保存文档），或选择 **Discard** 放弃结果。如果测试后更改了提示，测试结果会标记为过期，你必须重新测试。

点击 **Save as training** 后，DocBits 会告知你该训练将在下次重新处理时使用；当前这次运行尚未使用该训练。请在该供应商的下一个文档中检查状态标签是否显示 **Training applied**。
