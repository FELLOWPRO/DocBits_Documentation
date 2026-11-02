# DocBits MCP

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/docbits-mcp-admin/v1/zh.mp4" %}

DocBits 提供了一个 **Model Context Protocol (MCP)** 服务器，让 AI 助手可以直接在聊天或编码会话中处理您的文档、提取、搜索、分析和配置。任何兼容 MCP 的客户端都可以连接：**Claude Code**、**Claude Desktop**、**Google Gemini CLI**、**OpenAI Codex**，或任何自定义集成。

该服务器挂载在 DocBits API 的 `/v3/mcp` 路径下，并限定于您的组织范围 — 每次调用都使用连接用户（或 API 密钥）的权限运行。

{% hint style="info" %}
**端点 — 请使用您所在的区域（EU 或 US）：**

* 生产环境（EU）— `https://eu.api.docbits.com/v3/mcp`
* 生产环境（US）— `https://us.api.docbits.com/v3/mcp`

有关完整的主机列表以及如何使用 OAuth 登录，请参阅[设置与配置](setup-and-configuration.md)。
{% endhint %}

## 可以做什么？

借助 DocBits MCP，助手可以代表您：

* **查找和读取文档** — 列出、搜索（全文和字段搜索）、打开文档、读取其状态、日志、页面图像和导出预览
* **处理提取的数据** — 读取提取的字段和表格、更正字段值、使用 AI 提取表格、验证、审批并导出到您的 ERP
* **查询仪表板** — 使用自然语言运行仪表板查询、比较搜索模式并检查搜索功能
* **获取分析数据** — 执行摘要、成功率、处理量趋势、热门文档类型和待处理任务详情
* **处理电子发票（eDocs）** — 列出电子文档类型、测试和验证电子文档、管理自定义提取属性
* **管理主数据** — 新建或更新供应商主数据、触发供应商查询、导入供应商发票 BOD、维护付款条件和折扣映射
* **读取和更改配置** — 组织首选项、文档类型、字段设置、用户和缓存
* **检查运行状况** — API 和 Celery 运行状况、当前用户和 API 信息

## 工具概览

DocBits MCP 将一百多个工具分为以下类别（具体数量会随着每次发布而增加；您的助手会列出当前工具集）。大多数工具对应现有的 DocBits REST 端点，请参阅 [API 参考](../../)了解请求和响应详情。助手会根据您的请求自动选择合适的工具；下表列出了可用工具。

### 文档与处理

| 工具                                    | 描述                                      |
| --------------------------------------- | ---------------------------------------- |
| `list_documents`                        | 列出组织的文档（可筛选） |
| `get_document` / `get_document_by_name` | 按 ID 或文件名打开文档                |
| `upload_document`                       | 上传新文档以进行处理             |
| `get_document_status`                   | 查看文档当前的处理流水线状态            |
| `get_document_logs`                     | 查看文档的处理日志条目            |
| `query_org_logs`                        | 分页查看组织的服务日志     |
| `restart_document`                      | 重新运行处理流水线                   |
| `delete_document`                       | 删除文档                                |
| `get_pending_documents_count`           | 查看等待验证的文档数量              |

### 提取与验证

| 工具                                                | 描述                                                                         |
| --------------------------------------------------- | --------------------------------------------------------------------------- |
| `get_extracted_fields` / `get_document_fields`      | 读取提取的抬头字段                                                        |
| `get_extracted_tables`                              | 读取提取的行项目表格                                                     |
| `get_document_for_validation` / `get_next_document` | 按验证屏幕的方式打开文档；获取队列中的下一份文档 |
| `get_page_image`                                    | 获取页面图像以进行目视检查                                                        |
| `update_document_fields`                            | 更正或设置字段值                                                         |
| `validate_document`                                 | 运行字段验证规则                                                          |
| `approve_document`                                  | 审批已验证的文档                                                        |
| `validate_and_export`                               | 验证文档，然后导出到 ERP                                                     |
| `get_export_preview`                                | 发送前预览导出载荷                                           |

### 表格提取

验证屏幕和表格列设置中针对行项目表格的所有功能。配置工具会更改组织的文档类型；提取和更正工具针对单份文档操作；规则工具则保存 DocBits 为某个供应商学习到的内容。

| 工具                                                          | 描述                                                                                                        |
| ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `list_tables` / `get_table_config`                            | 文档类型的表格和列，以及 Required / Read Only / Hidden / Use AI 标记                       |
| `create_table`                                                | 为文档类型添加第二个行项目表格                                                                    |
| `add_table_column` / `delete_table_column`                    | 添加或软删除表格列                                                                                  |
| `set_ai_table_config`                                         | 为组织切换 AI 表格提取、视觉和结构化模式                                        |
| `extract_table_ai`                                            | 对文档运行 AI 表格提取（文本或视觉模式）                                                         |
| `extract_table_only`                                          | 仅提取表格，不处理抬头字段（使用规则或 AI）                                                 |
| `extract_table_nonai`                                         | 根据您传入的坐标进行基于规则的提取，这是通过 API 训练表格的第一步                |
| `apply_ai_table_formatting` / `apply_table_feedback`          | 重新格式化 AI 表格：隐藏列、重新映射、应用用户反馈                                                     |
| `remap_table_columns`                                         | 更改提取列与配置列之间的对应关系                                                        |
| `save_table_rules` / `save_table_training_rules`              | 为供应商保存坐标规则或 AI 格式化规则，使下一份文档以相同方式提取 |
| `delete_table_training_rules`                                 | 删除供应商已保存的规则；下一份文档将回退到 AI                                            |
| `get_table_extraction_report` / `list_table_report_suppliers` | 按供应商报告表格的提取方式（规则、AI、模型），并提供预览                                 |
| `compare_table_extraction_models`                             | 使用两个 AI 层级提取同一份文档并比较表格                                                 |

### 搜索与仪表板

| 工具                                              | 描述                                                                                       |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `search_documents` / `search_documents_by_name`   | 全文和文件名搜索                                                                     |
| `query_document_dashboard`                        | 使用自然语言查询仪表板                                                                  |
| `explain_document_dashboard_query`                | 显示查询的解释方式                                                                  |
| `get_search_capabilities`                         | 查看组织已启用的搜索功能                                                         |
| `compare_search_modes`                            | 比较关键词搜索与向量搜索结果                                                                |
| `diagnose_document_search`                        | 并排检查某份文档为何会或不会出现在特定搜索结果中，以及经典搜索与全文搜索的差异 |
| `inspect_document_search_index`                   | 检查文档是否存在于文档、文本和向量索引中，以及各索引的写入时间 |
| `get_dashboard_columns` / `set_dashboard_columns` | 读取或更改文档仪表板上显示的列                                        |

### 无人干预智能

了解文档为何需要人工介入，以及如何减少这种情况。此处的工具均为只读，只有 `touchless_apply_change` 除外；该工具只会写入一项已预览的设置更改。

| 工具                                                             | 描述                                                                                                |
| ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `touchless_get_summary`                                          | 组织的无人干预评分卡：按期间和细分统计未经人工干预处理的文档数量 |
| `touchless_list_segments`                                        | 可用于细分数据的值（供应商、文档类型等）                                         |
| `touchless_rank_supplier_opportunities`                          | 按供应商导致的人工工作量进行排名                                                        |
| `touchless_diagnose_supplier`                                    | 诊断某个供应商的文档为何会停止处理并等待人工介入                                                              |
| `touchless_get_issue_cluster`                                    | 查看一个重复出现的问题及其影响的文档                                                          |
| `touchless_get_document_trace`                                   | 查看一份文档的完整无人干预处理历史                                                                     |
| `touchless_explain_pipeline`                                     | 查看文档或问题集群在处理流水线的哪个环节停止                                                      |
| `touchless_explain_po_match` / `touchless_get_po_match_evidence` | 查看采购订单匹配成功或失败的原因，以及规则集和容差计算                                 |
| `touchless_get_recommendations`                                  | 查看建议的更改内容，而不只是已发现的问题                                                                   |
| `touchless_list_change_proposals`                                | 查看能够提高无人干预率的设置更改及其预期提升幅度                                |
| `touchless_preview_change`                                       | 对一项建议进行试运行：不会写入任何内容                                                                   |
| `touchless_apply_change`                                         | 将一项已预览的建议应用到组织                                                                   |
| `touchless_verify_change`                                        | 查看已应用的更改实际带来的收益                                                              |

### 分析与 BI

| 工具                       | 描述                          |
| -------------------------- | ---------------------------- |
| `get_executive_summary`    | 组织的高级 KPI |
| `get_success_rates`        | 无人干预处理率 / 直通率   |
| `get_volume_trends`        | 随时间变化的文档处理量            |
| `get_top_document_types`   | 最常见的文档类型   |
| `get_pending_tasks_detail` | 未完成工作的详情           |

### 电子文档（电子发票）

| 工具                                                           | 描述                                                        |
| -------------------------------------------------------------- | ---------------------------------------------------------- |
| `list_electronic_document_types`                               | 支持的电子发票格式（ZUGFeRD、XRechnung、Factur-X、UBL 等） |
| `test_electronic_document`                                     | 对电子文档样本进行分类和提取                           |
| `verify_electronic_documents` / `validate_all_edocs`           | 验证电子文档提取                                       |
| `list_edoc_custom_attributes` / `create_edoc_custom_attribute` | 管理自定义提取属性                                |

### 主数据

| 工具                                                      | 描述                                                                     |
| --------------------------------------------------------- | ----------------------------------------------------------------------- |
| `upsert_vendor_master_data`                               | 创建或更新供应商主数据                                             |
| `trigger_supplier_lookup`                                 | 使用供应商主数据丰富文档                                     |
| `import_supplier_invoice_bod`                             | 导入供应商发票 BOD                                                   |
| `get_supplier_invoice`                                    | 按发票、供应商或文档读取已持久化的供应商发票（BOD）数据 |
| `upsert_payment_term_mapping` / `upsert_discount_mapping` | 维护计算映射                                                   |

### 配置、管理与运行状况

| 工具                                                    | 描述                               |
| ------------------------------------------------------- | --------------------------------- |
| `get_preferences` / `get_preference` / `set_preference` | 读取和更改组织首选项           |
| `list_document_types` / `get_field_settings`            | 检查文档类型和字段设置 |
| `list_users`                                            | 列出组织用户                   |
| `clear_org_cache`                                       | 清除缓存的配置                |
| `check_api_health` / `check_celery_health`              | 服务运行状况                            |
| `get_current_user` / `get_api_info`                     | 身份和 API 元数据                 |

## 后续步骤

* [**设置与配置**](setup-and-configuration.md) — 连接 Claude Code、Gemini CLI 或 Codex（使用登录或 API 密钥）
* [**示例**](examples.md) — 客户让助手执行的实际任务
* [**电子文档（eDocs）**](edocs-mcp/) — 深入了解 eDoc 工具：检查/测试电子发票处理，并管理自定义提取/预览规则（相同端点，相同登录）
* [**工作流与卡片（DocFlow）**](docflow-mcp/) — 管理高级工作流和合作伙伴卡片

{% hint style="info" %}
**一个 MCP，满足所有需求。** eDoc 工具和 **工作流与卡片（DocFlow）** 工具运行在**同一个** `api.docbits.com/v3/mcp` 端点上，并使用相同的 DocBits 登录凭据。DocFlow 工具在该端点中的前缀为 `docflow_`（例如 `docflow_list_workflows`）；DocFlow 页面则使用它们不带前缀的名称进行说明。仍然可以直接连接到 DocFlow 主机，但现在已无此必要。
{% endhint %}

[使用 Claude 或 Codex 配置 DocBits](configuration-with-claude-or-codex.md)：连接、提示词、预览、版本化更改、验证与回退。
