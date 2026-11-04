# 设置与覆盖

[AI Table](README.md) · [表格的 Structured Output](structured-output.md)

## 管理员设置 <a id="settings-for-admins"></a>

打开 **设置 → 文档处理 → 文档类型 → 分类和提取**，选择 **General** 选项卡中的 **Extraction** 部分。

<figure><img src="../../../.gitbook/assets/structured-output-settings-zh-20261104.png" alt="当前提取设置。此现有配置关闭了 Structured Output，因此不显示架构预览。未更改任何提取设置。"><figcaption><p>当前提取设置。此现有配置关闭了 Structured Output，因此不显示架构预览。未更改任何提取设置。</p></figcaption></figure>

* **Table Extraction** 用于启用传统表格。
* **AI Table extraction** 用于为组织启用或关闭 AI 表格。
* **使用结构化提取（人工智能）**: 此开关设置组织的结构化输出默认值。实际请求的列取决于 Use AI 的默认/是/否选择、模板覆盖及供应商训练。完整指南说明配置、预览及示例。 [表格的 Structured Output](structured-output.md).
* **Save extraction rules (Admin only)**：开启后，只有组织管理员可以保存和导出提取规则。

<figure><img src="../../../.gitbook/assets/ai-table-settings-extraction-admin-only-en.png" alt="Save extraction rules (Admin only) 开关"><figcaption><p><strong>Save extraction rules (Admin only)</strong> 用于控制谁可以使用 <strong>Save as training</strong>。</p></figcaption></figure>

### 按列使用 AI <a id="use-ai-per-column"></a>

三态 AI 选择：默认继承文档类型的 AI 选择，是明确请求该列，否将其排除出基础架构。此设置独立于必填、只读和隐藏。 [表格的 Structured Output](structured-output.md).


Structured Output 有独立的组织/提取模板设置，与 AI 模型档位不同。在文档的更多选项中更改；确认后保存覆盖并重新启动该文档。设置列表中的状态仅供查看。删除条目可能同时移除多个覆盖值。 [表格的 Structured Output](structured-output.md).
