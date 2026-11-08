# 完整示例：价格与数量

<!-- touchless-admin-video-v2-20261104:start -->
**视频章节（审核版）：** [跟踪一份文档](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/zh.html#chapter=07)。
<!-- touchless-admin-video-v2-20261104:end -->

## 完整示例：提取正确，Infor 数据不同

这是一个说明性案例，与截图无关。发票显示 **10 件，每件 €10.00**，合计 **€100.00**。DocBits 正确提取了这三个值。导入的 Infor 订单显示 **10 件，每件 €9.00**，合计 **€90.00**。假设已配置的匹配检查会阻塞这一价格差异。

1. **检查提取：** 将原始发票与提取的数量、单价和行金额比较。它们一致，因此这些值并不存在已证实的提取错误。
2. **检查来源：** 将导入的订单与当前的 Infor 订单比较，包括价格单位和导入时间。过时的导入与错误的 Infor 订单需要不同的修复方式。
3. **澄清业务价值：** 在此示例中，采购确认约定价格为 €10.00，并更正了 Infor 订单。如果约定价格是 €9.00，则需改为与供应商澄清发票。
4. **核实更正后的导入：** 重试之前，检查正确的订单值确实已经到达 DocBits。
5. **记录 AP 操作：** AP 在 DocBits 中手动重启该发票；成功完成后，它属于 **AP assisted**。提取正确与流程非 touchless 可以同时成立。
6. **检查后续发票：** 核实匹配和导出现在能完成，无需再次更正或重启。此前被处理过的发票仍是被处理过的；后续发票才是改进的证据。

{% hint style="warning" %}
不要为了让一份错误的订单匹配，就把正确提取的 €10.00 改为 €9.00，也不要仅仅为了掩盖差异而放宽容差。请确认约定值，并更正相应的数据或配置。匹配阻塞点说明流程在哪里停下，而不是说明是谁造成的。
{% endhint %}

关于另一个提取质量示例和 AP touchless 计算，参见 [Touchless Intelligence](./)；需要对比证据时，参见 [Document Trace](touchless-document-trace.md)。

## 三张自建演示 PO：值一致、价格和数量

这些 PO 是专门在 **Dev** 中创建的。供应商、物料和发票均为虚构。每张发票都包含 **10 件 × €10 = €100 净额**。说明卡包含真实的英文界面截图和放大的数字细节。它们并未展示真实的客户 Infor 连接、经过验证的提取，或成功完成的自动发票流程。

| 案例 | 发票 | 导入的 PO | 比较所确立的内容 |
| --- | --- | --- | --- |
| PO01 / RE01：值一致 | 10 × €10 = €100 | 10 × €10 = €100 | 源值一致；Pure Touchless 仍需要正确提取，以及无需干预或审批的已确认完成 |
| PO02 / RE02：价格差异 | 10 × €10 = €100 | 10 × €9 = €90 | 行差额 €10；单价相对 PO 价格相差约 11.11%。是否阻塞由实际生效的规则决定 |
| PO03 / RE03：数量差异 | 10 × €10 = €100 | 8 × €10 = €80 | 多出 2 件，相当于订购数量的 25%。请检查未结/已收数量以及已配置的比较数量 |

<figure><img src="../../../.gitbook/assets/touchless-owned-po-match-zh.png" alt="FELLOW 说明卡，显示实际的英文 Dev 采购订单 PO01，数量十、单价十、金额一百"><figcaption><p>虚构 PO01 中值一致。放大的原生行显示数量、单价和金额。仅凭一致既不能证明提取正确，也不能证明 Pure Touchless。</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/touchless-owned-po-price-zh.png" alt="FELLOW 说明卡，显示实际的英文 Dev 采购订单 PO02，十件单价九、金额九十，对应发票金额一百"><figcaption><p>价格示例 PO02：导入的订单实际显示 10 × 9 = 90，而虚构发票为 10 × 10 = 100。请检查约定价格、价格单位和导入情况。已记录的人工干预随后成功完成，属于 AP Assisted。</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/touchless-owned-po-quantity-zh.png" alt="FELLOW 说明卡，显示实际的英文 Dev 采购订单 PO03，八件单价十、金额八十，对应开票十件"><figcaption><p>数量示例 PO03：导入的 PO 包含 8 件，发票为 10 件。此测试中已收数量为空，因此不能证明已收货。这些说明卡只解释比较过程；它们并不证明匹配成功。</p></figcaption></figure>

## 相关页面

* [Touchless Intelligence](./)
* [指标与计算](touchless-metrics.md)
* [使用仪表板](touchless-dashboard.md)
* [供应商诊断与问题集群](touchless-supplier-diagnosis.md)
* [PO 匹配诊断](touchless-po-matching-diagnosis.md)
* [文档追踪](touchless-document-trace.md)
* [变更提案与报告](touchless-change-proposals.md)
* [通过 MCP 解释和改进 Touchless](touchless-mcp.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->
<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
