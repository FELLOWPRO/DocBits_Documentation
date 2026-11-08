# 通过 MCP 解释和改进 Touchless

<!-- touchless-admin-video-v2-20261104:start -->
**视频章节（审核版）：** [通过 MCP 查询指标](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/zh.html#chapter=12)。
<!-- touchless-admin-video-v2-20261104:end -->

以下工作流程使用 DocBits MCP 实际提供的工具。请区分读取和解释与写入。核实组织、角色、文档类型、期间和数据时间戳；不要编造缺失的证据。

<figure><img src="../../../.gitbook/assets/touchless-owned-po-price-zh.png" alt="自建虚构 PO 的实际英文 Dev 视图：10 × 9 = 90。这是用于 MCP 诊断的源值比较，不是 MCP 客户端的截图，也不证明提取或处理成功。"><figcaption><p>自建虚构 PO 的实际英文 Dev 视图：10 × 9 = 90。这是用于 MCP 诊断的源值比较，不是 MCP 客户端的截图，也不证明提取或处理成功。</p></figcaption></figure>

## 通过 MCP 解释 Touchless

> 解释最近 30 天发票的 Pure Touchless、仅审批结果和合并的 AP 比率。说明分子、分母、进行中和被排除的文档、范围和数据的时点。将提取正确性单独区分开。

使用 `touchless_get_summary`，参数为 `period: "30d"` 和 `doc_type: "INVOICE"`。对于子流程，只能使用 `touchless_list_segments` 实际返回的细分字段和值。用相同的组织、文档类型、细分和期间比较仪表板与 MCP；读取 `data_as_of`。

**已验证的 Dev 反例：**三份新上传的测试发票仍为 `IN_PROGRESS`。摘要返回 `population.total: 3`、`population.in_progress: 3`、`population.eligible: 0` 和 `official_touchless_rate.ap_pct: null`。此时还无法计量任何比率。这既不是 0% 的提取准确率，也不是 100% 的 Touchless。此处的摘要合格性指已完成的 KPI 总体；单次追踪可以同时显示 `eligible: true` 和 `bucket_final: false`。

这五页中的 MCP 示例使用在 Dev 上核对过的 DocBits MCP 直连工具。您所连接账户的组织和角色仍然适用；该测试并不能证明在其他界面或额外工具白名单中同样可用。

## 常见问题

**DocBits 提取完全正确，为什么发票还是 AP assisted？**
Touchless 衡量的是整个流程。即使提取正确，错误或过时的 Infor 数据也可能需要已记录的更正或人工重启。请分别检查原始发票、DocBits 提取的值和导入的源数据。

**AP assisted 能告诉我工作是 DocBits 还是 Infor 造成的吗？**
不能。它记录的是干预，而不是责任。请使用文档追踪以及底层的文档和源数据来确认原因。

**比率显示破折号（—）。** 该期间内没有文档达到最终结果，或被计量的文档少于最低数量。仍在进行中的文档不计入。

**选项卡缺失。** 请让管理员启用该模块，并为您的角色授予 **Analytics dashboard** 选项卡权限。

**某份文档被计为已处理，但这次它无人干预就跑完了。** 它在更早的一次运行中被处理过（一次更正或一次重启）。比率统计的是已经发生的工作。

**为什么几个小时后数字会变化？** ERP 可能在导出发出数小时后才确认。结果每 15 分钟重新计算一次。

**AI 会自行更改任何内容吗？** 不会。AI 只写解释。只有在管理员预览并应用之后，设置才会改变。

## 通过 MCP 调查差异

> 检查此发票的 PO 号、导入状态和实际生效的匹配规则。区分提取、导入过时、源数据错误和配置缺失。暂时不要更改任何内容。

1. 在断言提取正确之前，比较原件、`get_extracted_fields` 和 `get_extracted_tables`。
2. 使用 `get_po_sync_status`，参数为 `po_number: "TL20261104X1-PO02"` 和 `language: "en"`。Dev 测试确认了一次已处理的导入和一个已存在的 PO。这证明订单已经到达，而不能证明业务上正确或当前的 Infor 记录。
3. 使用相同的 `doc_id` 调用 `touchless_get_document_trace` 和 `touchless_explain_po_match`。读取实际引擎、生效规则版本、列和当前生效的容差。对于实际返回的集群，将其 `issue_signature` 用于 `touchless_get_po_match_evidence`。
4. 保留缺失的证据：我们的新测试类型返回了 `state: "none_published"` 和 `parse_error: "no published rule set"`，以及空的提取字段。未证明存在价格/数量阻塞，也未证明匹配成功。通用决策流程不能替代这些缺失的检查。
5. 修复已确认的原因并检查新的发票。人工更正或重启在成功之后仍然相关；最终的 ERP 失败会优先作为异常处理，而未完成的文档不在比率分母之内。

对于完整案例，请保留原件、更正前的提取、导入的/当前的源值和导入时间、实际规则、AP 操作以及最终结果。缺失的证据应保持未定。

## 通过 MCP 读取证据

> 在不做任何更改的情况下检查此发票。比较原件、当前字段和表格。解释已记录的阶段和运行，并指出缺失的历史提取证据。

| 使用同一 `doc_id` 的工具 | 证据与局限 |
| --- | --- |
| `get_extracted_fields` | 当前表头值和置信度；不是历史快照 |
| `get_extracted_tables` | 实际的表格和行；不能证明它们与原件一致 |
| `touchless_get_document_trace` | 已记录的结果、干预、阶段和运行 |
| `touchless_explain_pipeline` | 对有证据的处理路径的解释；不会补齐缺失的证据 |

**观察到的负向检查：**我们新生成的测试发票有一个 `passed` 的表头提取阶段，但 `extracted_field_count: 0`、八个必填字段为空且没有表格。字段校验以 `REQUIRED_FIELD_MISSING` 阻塞。助手应调查提取/配置缺失，而不是仅凭一个绿色阶段就声称提取正确，也不能仅凭源值不同就声称存在已证实的 PO 价格阻塞。

### MCP 操作算作人工处理吗？

只读检查不会改变发票。其他 MCP 工具可能写入字段、执行校验或重启。分类取决于已记录的事件以及其操作者是人工还是系统账户。API 密钥可以代表系统账户；仅“通过 MCP 执行”既不能证明存在人工处理，也不能证明 Pure Touchless。绝不要用系统凭据掩盖人工返工。

在执行文档操作后，检查 `human_touched`、`human_touch_source`、`human_restart_count`、`business_approval_touched`、最终状态和运行。仅有业务审批与已保存的更正、手动校验或人工重启不同。

## 通过 MCP 排定供应商优先级并核实持久的改进

> 排出流失 Touchless 发票最多的供应商。区分提取错误、导入源差异和流程设置。为每个已确认的原因提出一项措施和可验证的成功检查；暂时不要更改任何内容。

1. 使用 `touchless_rank_supplier_opportunities`，参数为 `period: "30d"`、`doc_type: "INVOICE"`、`order_by_field: "lost_docs"`、`order_by_direction: "desc"`。用 `search` 查找供应商编号或名称；用 `limit` 和 `offset` 分页。
2. 将返回的 `supplier_key` 原样传给 `touchless_diagnose_supplier`。当前问题使用 `window: 30`，调查反复出现的问题使用 90。
3. 将实际返回的 `issue_signature` 传给 `touchless_get_issue_cluster`。在确认原因之前，先查看示例文档和缺失的证据。不要编造标识符。
4. 使用 `touchless_get_recommendations` 说明受支持的措施。预期提升是估算值；相互重叠的集群不能简单相加。
5. 修复后检查新的可比发票，并查看[变更测量](touchless-change-proposals.md)。此前被处理过的发票不会追溯地变为 Pure Touchless。

对于提取正确但 PO 过时的情况，应修复源数据/导入数据。对于原件与提取不一致的情况，应调查提取配置。策略要求的审批属于另一种成功的 AP Touchless 结果。排名为空并不能证明没有问题：我们的三份进行中测试发票尚未产生任何已排名的供应商结果。请检查范围、数据时间戳、供应商识别和已完成的文档量。

## 通过 MCP 预览、应用和测量

> 解释已确认的原因并列出受支持的提案。预览所选变更、其范围和风险。只应用所选的那项变更，然后核实已保存的设置、变更历史和可计量的效果。

| 步骤 | 工具与实际返回的标识符 | 证明了什么 |
| --- | --- | --- |
| 列表 | `touchless_list_change_proposals`，可选 `issue_signature`、`window: "30d"`、`lang: "en"` | 可用的提案；未保存任何设置 |
| 预览 | `touchless_preview_change`，使用返回的 `proposal_id` 和匹配的 `issue_signature` | 获准时给出具体范围和绑定的 `preview_token` |
| 应用所选变更 | `touchless_apply_change`，使用相同的 ID、`preview_token`、`overrides` 和 `window` | **写入**受支持的设置；成功响应返回 `change_id` |
| 读取效果 | `touchless_verify_change`，使用该 `change_id` 和相同的 `window` | 前后测量；每个期间仍需至少 20 份符合条件的已完成文档 |

请从真实响应中复制 ID 和令牌。为某个值生成的预览令牌不能用于应用另一个值。过期、被禁止或不完整的预览不能作为已应用变更的证据。只读工具与应用不可混为一谈。本表说明的是工具顺序；它并不声称演示执行过提案或测得增益。

**配置示例：**在确认某项配置修复后，检查实际保存的数值和新的发票。52% 到 61% 是观察到的 9 个百分点差异，不能证明是该变更单独造成的。**源数据示例：**错误的 Infor PO 需要业务更正和经过核实的导入。`touchless_apply_change` 不是通用的 Infor 写入工具。不要为了掩盖错误的源数据而放宽容差。

报告截图显示的是建议和预计影响，而不是应用或回滚。成功应用需要成功响应和历史条目。只有在所选提案支持时才能撤销；请核实实际恢复的设置。重新加载历史不会应用设置，回滚也不会删除过去对文档的干预。

## 相关页面

* [Touchless Intelligence](./)
* [指标与计算](touchless-metrics.md)
* [使用仪表板](touchless-dashboard.md)
* [完整示例：价格与数量](touchless-examples.md)
* [供应商诊断与问题集群](touchless-supplier-diagnosis.md)
* [PO 匹配诊断](touchless-po-matching-diagnosis.md)
* [文档追踪](touchless-document-trace.md)
* [变更提案与报告](touchless-change-proposals.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->
<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
