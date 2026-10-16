# 使用了哪种提取路径？

“为什么这个表格看起来是这样的？”要回答这个问题，需要查明 DocBits 对此文档执行了什么操作：保存的规则、AI 表格、使用的 AI 层级，以及出错的位置。本页是支持人员和合作伙伴在更改任何配置前使用的检查清单。

## 1. 查看验证界面上的选项卡

打开文档，查看行项目表格上方的选项卡：

| 看到的内容 | 路径 |
|---|---|
| **Extracted table** 选项卡中的行 | 基于规则的路径。该供应商已有经过训练的表格；这些行来自已保存的坐标规则，未使用 AI（标记为 *Use AI* 的列除外）。 |
| **AI Extracted table** 选项卡中的行，以及下方的 *Tags* 字段 | AI 路径。没有匹配的已保存规则；AI 表格提取生成了这些行，使用的是组织的 AI 层级，或在 *More settings* → *Supplier-Based AI Model* 中为该供应商设置的层级。 |
| AI 选项卡上的 *AI table not found* 提示 | AI 路径已运行，但没有为此文档返回内容。 |
| 没有任何表格选项卡 | 组织已关闭两项表格设置，因此没有任何内容提取表格。 |
| *No line items yet* | 路径已运行，但未找到行（没有可读取的文本、页面上没有表格，或规则与此版式不匹配）。 |

表头字段会在值旁显示各自的来源标记：*Extracted using AI*、*Learned from validated AI extraction*、*Extracted using saved rules (FELLOW_KV2)*、*Extracted from electronic document*、*Calculated from vendor master data*。这些标记描述的是表头字段，而不是表格。

## 2. 检查供应商的配置

* **Settings → Document Processing → Classification and Extraction → AI Model**：选择器下方的表格会列出所有已保存模型或训练数据的供应商。列表中带有 *training data* 的供应商已有已保存的规则；*reset the training data* 会移除这些规则。
* **Settings → Document Processing → OCR Settings**：*Use E-Text if available* 和 *Use AI data for tables* 会改变提取过程所读取的文本。供应商可以在验证界面的 *More settings* 中覆盖 E-Text 设置。
* **Settings → Global Settings → Document Types → Table Columns**：此处设有隐藏、必填和 *Use AI* 标记。隐藏列永远不会填充；即使供应商已有规则，标记为 *Use AI* 的列也会由 AI 填充。

## 3. 不使用界面进行复现（API / MCP）

通过 API 或 MCP 访问权限，可以用编程方式查询相同的信息：

| 问题 | 工具 |
|---|---|
| 这个表格是由 AI 生成的吗？ | `get_extracted_tables(doc_id)`：每个表格都带有 `is_ai_table: true/false`。 |
| 规则会提取什么，AI 会提取什么？ | 调用 `get_table_extraction_report(doc_id, mode="nonai")`，再调用 `mode="ai"`；报告会显示每种路径的已配置结构、提取的行和页面预览。对比两份报告。 |
| 配置了哪些列，各自带有什么标记？ | `get_table_config(doc_type)` |
| AI 层级是否有影响？ | `compare_table_extraction_models(doc_id)` 会对同一文档运行两个层级（需要文档中有供应商编号）。 |
| 重新提取此文档 | `extract_table_ai(doc_id)`（AI）或 `restart_document(doc_id)`（整个工作流）。 |
| 工作流记录了此文档的哪些日志？ | `get_document_logs(doc_id)` |

DocBits MCP 工具的说明见 [DocBits MCP](../../../advanced-functions-and-tools/docbits-mcp/README.md)。

## 4. 查看日志

**Settings → Log Settings**（Activity Logging）显示所有服务的事件。排查表格问题时：

* 在 *Search logs* 中按文档文件名或 ID 筛选。
* 使用 *Service* 筛选器：提取本身运行于提取服务和 Celery 工作进程中，而不是 `api` 服务。如果只看到 `api` 日志行，请扩大筛选范围。
* 正常运行会按顺序记录：收到文档 → OCR / E-Text → 分类 → 字段提取 → 表格提取（查询规则，然后在无规则匹配时使用 AI）→ 验证 → 状态更改。缺失或报告错误的步骤就是需要检查的步骤。

## 5. 判断问题出在配置、数据还是程序错误

| 症状 | 最可能的原因 | 下一步 |
|---|---|---|
| 同一文档类型中，供应商 A 的表格正确，供应商 B 的表格错误 | 供应商级别的问题：B 没有规则，或旧规则已不再匹配 B 的版式 | 为 B 训练一次表格（或删除 B 的规则，让 AI 接管）。 |
| 从某个日期起，所有供应商的表格都出错 | 组织设置已更改（AI 层级、结构化提取、视觉识别、表格列） | 将设置与更改日期进行对比；重启一个文档以确认。 |
| 同一文档：规则路径为空，AI 路径正确 | 规则与此版式变体不匹配 | 使用此文档重新训练，或删除这些规则。 |
| 同一文档：两种路径都为空 | 没有可读取的文本（扫描件没有 OCR 文本，或 PDF 仅包含图像） | 查看验证界面上的 OCR 视图；如果 PDF 有文本层，则启用 E-Text；尝试其他 OCR 版本。 |
| 每一行都只有一个列出错，其余列正常 | 列映射或 *Use AI* 标记 | 检查 Table Columns 设置；在表格训练中重新映射。 |
| 在分页处或小计行之后缺少行 | AI 或规则未能正确处理该版式 | 使用多页文档训练表格；添加类似 *"table continues on page 2"* 的标签。 |
| 日志中缺少提取步骤，文档停留在 *running* 状态 | 基础设施问题（工作进程积压），而非配置问题 | 检查待处理任务（通过 MCP 调用 `get_pending_tasks_detail`），并向支持人员提供文档 ID。 |

## 需要发送给支持人员的信息

* 文档 ID 和组织
* 哪个选项卡中有这些行（Extracted table / AI Extracted table / 无），以及正在使用的 AI 层级
* 供应商是否有已保存的规则，以及这些规则上次保存的时间
* 如果有，请提供一个正常工作的文档示例和一个无法正常工作的文档示例

## 相关页面

* [Table Extraction Troubleshoot](table-extraction-troubleshoot.md)：提取质量、OCR、E-Text、表格消息
* [训练行字段／表格训练](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md)
* [AI Table](../../../end-user-and-partner-section/end-user-section/ai-table/README.md)
* [Log Settings](../../../administration-and-setup/settings/log-settings/README.md)
