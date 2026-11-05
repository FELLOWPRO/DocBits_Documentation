# 无接触智能

Touchless Intelligence 区分两个问题： **DocBits 是否正确提取发票？** 以及 **整个流程是否无人工处理干预地完成？** 提取正确也可能需要处理不同的 Infor 数据。AP 指人工应付账款团队。

## 视频：Touchless 报告功能

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/zh.mp4" %}

这份 4:49 的审核版展示有实际数据的报告：筛选、指标与计算、趋势、首次阻塞点、已记录证据、文档历史、执行对比、学习规则、改进与历史记录、咨询报告，以及实际 MCP 查询结果。

[打开含中文字幕和 16 个章节的视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/zh.html). 本次新版的人工试听评估尚未完成。

这些教学案例用于解释报告功能。建议或预览不能证明修改已生效，也不能证明已取得实际改善。 画面中的 MCP 修改建议还需要明确具体目标配置，暂不支持预览和应用。部分产品原生文本可能仍保留原始语言。 已学习规则中的“21份中20份”表示规则匹配的案例数。反例显示规则会替换某个已被接受的值；部分原生界面标签的翻译不准确。

<figure><img src="../../../.gitbook/assets/anatomy-touchless-zh.svg" alt="等距分拣线示意图：传送带上有 14 道闸门，一个推杆将一份文档推入审核托盘，导出箱中有一叠文档，表盘显示 78.9 %"><figcaption><p>将 Touchless 比作分拣线，数字取自示例计算：14 道闸门是 Pipeline Path 的各个阶段，仍在传送带上的纸张处于处理中，不计入统计；在闸门处停下的文档会被推入审核托盘，与 AP 辅助（30）和流程异常（10）文档放在一起；导出箱中的纯无接触（120）和仅需审批（30）文档合计 190 份中的 150 份，即表盘上的 78.9 %，高于 70 % 的目标标记。</p></figcaption></figure>

## 选择合适的指南

| 指南 | 内容 |
| --- | --- |
| [指标与计算](touchless-metrics.md) | 类别、分子分母、操作和计算示例 |
| [使用仪表板](touchless-dashboard.md) | 筛选、指标、趋势和首次阻塞 |
| [示例：价格与数量](touchless-examples.md) | 虚构发票及真实 Dev 价格/数量差异画面 |
| [供应商诊断与问题集群](touchless-supplier-diagnosis.md) | 供应商和重复原因的优先级 |
| [采购订单匹配诊断](touchless-po-matching-diagnosis.md) | 有效规则、容差和决策 |
| [文档追踪](touchless-document-trace.md) | 原件、执行、阻塞和人工操作 |
| [变更提案和报告](touchless-change-proposals.md) | 区分预览、应用、测量和撤销 |
| [通过 MCP 解释和改善 Touchless](touchless-mcp.md) | 通过 MCP 解释、诊断和受控改善 |

<figure><img src="../../../.gitbook/assets/site-complete-touchless-overview-zh.png" alt="当前中文 Touchless Intelligence 总览。指标和图表是测试环境实际数据；“美联社协助”指应付账款辅助处理，“非接触式费率”指免人工处理率，“学术规则提案”指已学习规则提案。Compare suppliers 按钮仍为英文。未运行诊断或应用提案。"><figcaption><p>当前中文 Touchless Intelligence 总览。指标和图表是测试环境实际数据；“美联社协助”指应付账款辅助处理，“非接触式费率”指免人工处理率，“学术规则提案”指已学习规则提案。Compare suppliers 按钮仍为英文。未运行诊断或应用提案。</p></figcaption></figure>

## 访问权限

属于[分析仪表板](../)。管理员可访问，其他用户需要相应角色权限。AI 分析、支持的变更和报告可能需要管理员。

<!-- Alignment 2026-11-04: correct extraction is distinct from process Touchless; KPI numerator and denominator verified. -->
<!-- Completion 2026-11-04: localized MCP examples, AP actions, original-value evidence and owned synthetic PO cards. -->
