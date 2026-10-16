# 示例

连接 DocBits MCP 后（请参阅[设置与配置](setup-and-configuration.md)），你可以用自然语言与助手交流，它会为你选择合适的 DocBits 工具。以下是客户常见的实际操作示例，包括你可以输入的提示，以及助手在后台使用的工具。

{% hint style="info" %}
这些操作在 Claude Code、Gemini CLI 和 Codex 中方式相同——提示使用自然语言，而不是命令。
{% endhint %}

## 处理工作队列

> *“有多少份文档正在等待验证？它们分别是什么类型？”*

使用 `get_pending_documents_count`、`get_pending_tasks_detail`、`get_top_document_types`。助手会汇总积压情况，并可进一步查看任意文档。

> *“显示今天出错的发票，并告诉我出错原因。”*

使用 `search_documents` / `query_document_dashboard` + `get_document_logs` 查找出错的文档，并根据日志说明失败原因。

## 查找并检查文档

> *“打开发票 INV-2026-00231，显示提取的字段和行项目。”*

使用 `get_document_by_name`、`get_extracted_fields`、`get_extracted_tables`。助手会返回抬头数据和表格；如果你想查看来源，还可以使用 `get_page_image` 获取页面图像。

> *“搜索上个月所有来自供应商‘ACME GmbH’且金额超过 €10,000 的文档。”*

使用 `search_documents` / `query_document_dashboard` 并设置字段筛选条件。

## 更正并审批

> *“在文档 84213 中，将采购订单编号设为 4500098123，到期日期设为 2026-07-15，然后验证该文档。”*

先使用 `update_document_fields`，再使用 `validate_document`。助手会报告验证错误，方便你修正。

> *“验证文档 84213 并将其导出到 ERP，但先向我显示导出预览。”*

使用 `get_export_preview`，待你确认后再使用 `validate_and_export`。

## 修复表格提取

> *“这张交货单的行项目表格缺少两行，请用 AI 重新提取，隐藏 *费用* 列，并为该供应商保留此设置。”*

使用 `extract_table_ai` 重新运行文档的 AI 表格提取，使用 `apply_ai_table_formatting` 隐藏该列，并使用 `save_table_training_rules` 为该供应商保存结果；下次提取该供应商的交货单时也会采用相同方式。对于基于规则的提取漏掉行的文档，此功能很有用。使用 `get_extracted_tables` 查看最终表格。

## 分析与报告

> *“为我提供本月的高管摘要：数量趋势、免人工处理率和排名前 5 的文档类型。”*

使用 `get_executive_summary`、`get_volume_trends`、`get_success_rates`、`get_top_document_types`。无需打开仪表板，即可快速了解管理层所需的信息。

## 电子发票（eDocs）

> *“我们启用了哪些电子发票格式？这个 ZUGFeRD 文件能否正确提取？”*

使用 `list_electronic_document_types` + `test_electronic_document`，然后使用 `verify_electronic_documents` 确认提取的字段。

## 主数据与供应商信息补充

> *“将新的供应商（名称、VAT、IBAN）添加到主数据，然后重新运行文档 84500 的供应商查询。”*

使用 `upsert_vendor_master_data` + `trigger_supplier_lookup`。

## 配置更改

> *“为我们的组织启用二维码提取，并确认偏好设置已生效。”*

使用 `set_preference`（该操作会自动清除缓存）+ `get_preference` 进行确认。

> *“列出我们的文档类型，并显示‘Invoice’的字段设置。”*

使用 `list_document_types` + `get_field_settings`。

## 健康状态与诊断

> *“DocBits API 和处理工作器当前运行正常吗？我当前以哪个身份连接？”*

使用 `check_api_health`、`check_celery_health`、`get_current_user`。

---

## 提示

- **明确指定文档**——提供 ID 或准确的文件名最快；否则助手会先进行搜索。
- **导出前先请求预览**——`get_export_preview` 可让你在 `validate_and_export` 发送 ERP 数据前确认载荷。
- **权限仍然适用**——助手只能执行你的 DocBits 用户或 API 密钥获准执行的操作。审批和导出会遵循你的角色和 ACL。
- **注意生产环境操作**——MCP 会操作真实数据。在客户或生产环境中，优先使用读取和预览操作，并在审批、导出或删除前进行确认。
