# 选择用于字段和表格提取的供应商专属 AI 模型

## 从组织标准到有效模式

<figure><img src="../../../.gitbook/assets/process-ai-model-zh-20261028.png" alt="当前提取模板使用哪个 AI 模型？: 组织默认设置与提取模板专用设置。"><figcaption><p>组织默认设置与提取模板专用设置。 该图是示意性的；您组织的活动设置决定了实际行为。</p></figcaption></figure>

验证屏幕中的条目称为供应商特定的 AI 模型。但是，**当前提取模板上下文**至关重要：覆盖按组织和模板保存。供应商可以拥有多个具有不同设置的模板。

1. **确定上下文：** 在修改模型之前检查组织、文档和当前提取模板。
2. **检查覆盖：** 如果为此模板存储了模型，则此选择在其范围内生效。如果缺少替代，则应用适用的组织设置。
3. **特意确认更改：** 仅选择您环境中可用的选项。更改可能需要确认并再次触发提取。单独打开菜单不会更改选择。
4. **比较结果：** 用固定样本检查字段值、表格、运行时间和成本。不同的模型级别并不能保证更好的提取、成功的验证或 PO 匹配。

**示例：** 供应商 A 使用模板“国内发票”和“国外发票”。 “国内发票”的覆盖不会更改该供应商的所有发票。对于其他文档，请再次检查其模板和有效设置。

该图显示了选择层次结构，而不是针对特定模型级别的建议。有关 [组织标准和覆盖](../../../administration-and-setup/settings/document-processing/classification-and-extraction/ai-model.md) 和 [使用了哪条提取路径？](../../../overview-and-basics/faq/document-processing/which-extraction-path-was-used.md) 诊断的信息有助于对实际结果进行分类。

在 **Validation screen（验证界面）** 的工具区域中，您可以选择用于 **Field Extraction（字段提取）** 和 **Table Extraction（表格提取）** 的 AI 模型。\
该入口设置当前提取模板上下文的覆盖值，按组织及模板标识 `tfidf_id` 保存。供应商标识可作为关联信息，但这不保证同一供应商的所有模板、所有历史文档都被更改。没有覆盖值时，按组织全局设置回退。

要更改模型，请点击屏幕右侧的 **More options（更多选项）**（三个点）按钮打开选项菜单，然后选择一个可用模型：<br>

当前菜单提供 **Full、Fast、Nexus、Nexus Flash、Auto、Auto Nexus** 六个选项。正式名称按界面原样保留；实际费用、可用性与自动选择方式以当前菜单信息及订阅约定为准，不承诺某级别在所有文档上准确率最高或速度最快。

选择新模型后，可能需要在确认对话框中确认并重新开始提取。先核对文档和作用范围；展开菜单本身不会更改设置。本文未执行选择或确认，也未测试切换后的结果。

<figure><img src="../../../.gitbook/assets/site-complete-supplier-model-menu-zh.png" alt="当前中文验证界面“更多选项”中的“供应商特定的 AI 模型”入口。示例为自有虚构中文发票，没有切换模型、重启提取或导出；测试文档在拍摄后已验证删除。"><figcaption><p>当前中文验证界面“更多选项”中的“供应商特定的 AI 模型”入口。示例为自有虚构中文发票，没有切换模型、重启提取或导出；测试文档在拍摄后已验证删除。</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/site-complete-supplier-model-options-zh.png" alt="当前实际模型菜单提供 Full、Fast、Nexus、Nexus Flash、Auto、Auto Nexus 六个选项。只展开菜单，未选择或确认；截图显示的文档语言值属于识别/文档设置，不是界面的语言，当前界面已验证为中文。"><figcaption><p>当前实际模型菜单提供 Full、Fast、Nexus、Nexus Flash、Auto、Auto Nexus 六个选项。只展开菜单，未选择或确认；截图显示的文档语言值属于识别/文档设置，不是界面的语言，当前界面已验证为中文。</p></figcaption></figure>

如果字段或表格提取结果不理想，可在获准测试文档中比较其他模型，并逐项检查提取值、处理时间和费用。切换模型可能重新处理文档，且不保证改善结果。

如需为**未设置自定义模型的供应商全局配置 AI 模型**，或**管理每个供应商启用的模型**，请参阅相应文档[**此处**](../../../administration-and-setup/settings/document-processing/classification-and-extraction/ai-model.md)。
