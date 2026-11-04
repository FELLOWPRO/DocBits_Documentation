# 通过 MCP 解释和改善 Touchless

使用实际提供的 DocBits MCP 工具，区分读取与写入。核实组织、角色、类型、期间和日期，不编造证据。

<figure><img src="../../../.gitbook/assets/touchless-owned-po-price-zh.png" alt="真实中文 Dev 视图，虚构订单为 10 × 9 = 90。这是用于 MCP 诊断的源值比较，不是 MCP 客户端截图，也不证明提取或处理成功。"><figcaption><p>真实中文 Dev 视图，虚构订单为 10 × 9 = 90。这是用于 MCP 诊断的源值比较，不是 MCP 客户端截图，也不证明提取或处理成功。</p></figcaption></figure>

## 通过 MCP 解释 Touchless

> 解释最近 30 天发票的 Pure、仅审批和 AP 综合率。给出分子、分母、处理中、排除项、筛选和数据日期。区分提取质量与流程自动化。

使用 `touchless_get_summary`，参数 `period: "30d"`、`doc_type: "INVOICE"`。细分维度和值必须来自 `touchless_list_segments`。比较相同组织、类型、期间和细分；读取 `data_as_of`。

**真实 Dev 反例：** 三份新发票仍为 `IN_PROGRESS`：`population.total: 3`、`population.in_progress: 3`、`population.eligible: 0`、`official_touchless_rate.ap_pct: null`。暂时无法计算比例，不代表提取正确率 0 % 或 Touchless 100 %。这里摘要的 `eligible` 是已完成 KPI 范围；单份追踪可同时显示 `eligible: true`、`bucket_final: false`。

这些是实际提供并在 Dev 检查过的 MCP 工具；组织和权限仍适用。不能据此证明其他界面或额外工具白名单也已支持。

## 通过 MCP 检查差异

> 检查订单、导入和有效规则，区分提取、旧副本、源错误与配置缺失，暂不修改。

1. 比较原件、`get_extracted_fields`、`get_extracted_tables` 后才能确认提取正确。
2. `get_po_sync_status`：`po_number: "TL20261104X1-PO02"`、`language: "en"`。只支持 `de` 或 `en`，再用中文解释结果。导入已处理不证明业务正确或当前 Infor 状态。
3. 使用同一 `doc_id` 调用 `touchless_get_document_trace`、`touchless_explain_po_match`，核实实际引擎、版本、列及容差。把真实 `issue_signature` 传给 `touchless_get_po_match_evidence`。
4. 测试类型返回 `state: "none_published"`、`parse_error: "no published rule set"` 和空字段，未证明价格/数量阻塞或匹配成功。
5. 修复确认原因并核查新发票。人工更正/重启成功后仍保留；最终 ERP 错误优先。处理中文档不在分母。

完整案例需要原件、更正前提取、带日期的源值/导入、实际规则、AP 操作和最终结果。缺失证据仍需补充。

## 通过 MCP 读取证据

> 不修改这份发票。比较原件、当前字段与表格，解释已记录执行，并列出缺失的历史证据。

| 使用同一 `doc_id` 的工具 | 限制 |
| --- | --- |
| `get_extracted_fields` | 当前值与置信度，不是历史快照 |
| `get_extracted_tables` | 当前表格，不证明与原件一致 |
| `touchless_get_document_trace` | 已记录的结果、干预和执行 |
| `touchless_explain_pipeline` | 解释有证据的路径，不补造缺失证据 |

**真实负向测试：** `header_extraction: passed`，但 `extracted_field_count: 0`、八个必填字段为空、没有表格。验证报 `REQUIRED_FIELD_MISSING`。应检查提取/配置；绿色步骤不证明正确提取或价格阻塞。

### MCP 操作是否算人工干预？

阅读不会修改发票，其他工具则可能写入、验证或重启。API 密钥可能代表系统账户；“通过 MCP”不能证明人工干预或 Pure。不要用系统身份掩盖人工返工。检查 `human_touched`、`human_touch_source`、`human_restart_count`、`business_approval_touched`、最终状态和各次执行。仅审批不同于更正、手动验证和人工重启。

## 通过 MCP 排定供应商优先级并检查改善

> 按失去 Touchless 的文档数排列供应商，区分提取、源数据和配置。对已确认原因提出处理和验证方法，暂不修改。

1. `touchless_rank_supplier_opportunities`：`period: "30d"`、`doc_type: "INVOICE"`、`order_by_field: "lost_docs"`、`order_by_direction: "desc"`。`search` 搜索名称/编号，`limit`、`offset` 分页。
2. 把返回的 `supplier_key` 传给 `touchless_diagnose_supplier`；`window: 30` 查看当前情况，90 用于分析复发。
3. 把真实返回的 `issue_signature` 传给 `touchless_get_issue_cluster`，先检查文档和缺失证据。
4. `touchless_get_recommendations` 解释支持的措施。预期收益是估计，重叠簇不能相加。
5. 用可比的新发票和变更后测量验证。已人工处理的旧发票不会追溯变为 Pure。

提取正确但订单旧，应修复源数据/导入；原件与提取不同，应检查提取配置。空排名不证明没有问题：三份处理中测试发票还没有已完成的供应商结果。检查筛选、日期、供应商识别和完成量。

## 通过 MCP 预览、应用和测量

> 解释已确认原因，列出支持的提案，预览所选变更。只应用这项变更，再核实保存值、历史及效果。

| 步骤 | 工具 | 结果 |
| --- | --- | --- |
| 列表 | `touchless_list_change_proposals`，可选 `issue_signature`、`window: "30d"`、`lang: "zh"` | 现有提案，不写入设置 |
| 预览 | `touchless_preview_change`，使用返回的 `proposal_id`、`issue_signature` | 明确范围，以及获准时绑定的 `preview_token` |
| 应用 | `touchless_apply_change`，使用相同 ID、令牌、`overrides`、`window` | **写入**支持的设置；成功返回 `change_id` |
| 测量 | `touchless_verify_change`，使用该 `change_id` 和相同 `window` | 前后比较；每期至少 20 份已完成且符合条件的文档 |

不要编造 ID 或令牌。值不同需重新预览；过期或未获准的预览不证明已应用。演示案例未证明实际应用提案或测得提升。

52 % 到 61 % 是观察到的 9 个百分点，不证明单一原因。`touchless_apply_change` 不是任意写入 Infor 的工具；错误订单需业务更正和导入验证。不要放宽容差掩盖错误。

报告是估计，不是应用或撤销证明。要求成功响应和历史条目。只有支持撤销的提案才能撤销，并须核实恢复值。刷新历史不会应用变更，撤销也不会清除过去人工干预。

## 相关页面

* [Touchless Intelligence](./)
* [指标与计算](touchless-metrics.md)
* [使用仪表板](touchless-dashboard.md)
* [示例：价格与数量](touchless-examples.md)
* [供应商诊断与问题集群](touchless-supplier-diagnosis.md)
* [采购订单匹配诊断](touchless-po-matching-diagnosis.md)
* [文档追踪](touchless-document-trace.md)
* [变更提案和报告](touchless-change-proposals.md)

<!-- Alignment 2026-11-04: correct extraction is distinct from process Touchless; KPI numerator and denominator verified. -->
<!-- Completion 2026-11-04: localized MCP examples, AP actions, original-value evidence and owned synthetic PO cards. -->
