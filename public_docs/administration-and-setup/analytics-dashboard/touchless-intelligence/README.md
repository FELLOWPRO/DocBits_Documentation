# 无接触智能

Touchless Intelligence 回答两个彼此独立的问题：**DocBits 是否正确地提取了发票？**以及：**整个流程是否在没有处理干预的情况下完成？**即使提取正确，只要 Infor 数据不同，仍可能需要返工。AP 指人工应付账款团队。

## 视频：Touchless 报告功能

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/zh.mp4" %}

这段 4:49 的审核版视频展示了一份有数据的报告：筛选、KPI 与计算、趋势、首要阻塞点、已记录的证据、文档历史、运行比较、已学习规则、改进与历史、咨询报告，以及实际的 MCP 结果。

[打开带中文字幕和 16 个章节链接的视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/zh.html)。这一新版的人工试听评审仍在进行中。

这些教学案例用于说明报告功能。建议或预览既不能证明某项设置已应用，也不能证明改进已被测量。画面中的 MCP 变更提案仍需具体的目标配置；该提案暂不支持预览和应用。部分产品原生文本可能仍保留其原始语言。

<figure><img src="../../../.gitbook/assets/anatomy-touchless-zh.svg" alt="等距分拣线示意图：一条有 14 道闸门的传送带，一个推杆将一份文档推入审核托盘，一个装有成叠文档的导出箱，以及一个读数为 78.9 % 的表盘"><figcaption><p>把 Touchless 视为一条分拣线，数字取自示例计算：14 道闸门是 Pipeline Path 的各个阶段；仍在传送带上的纸张处于进行中状态，不计入统计；在闸门处停下的文档会被推入审核托盘，与 AP assisted（30）和流程异常（10）文档放在一起；导出箱中的 pure（120）和仅审批（30）文档使表盘显示 190 份中的 150 份，即 78.9 %，超过 70 % 的目标标记。</p></figcaption></figure>

## 找到正确的指南

| 指南 | 涵盖内容 |
| --- | --- |
| [指标与计算](touchless-metrics.md) | 结果类别、分子与分母、AP 操作与计算 |
| [使用仪表板](touchless-dashboard.md) | 筛选、KPI 卡、趋势、首要阻塞点与控件 |
| [完整示例：价格与数量](touchless-examples.md) | 虚构发票与真实 Dev PO 视图中的价格和数量差异 |
| [供应商诊断与问题集群](touchless-supplier-diagnosis.md) | 排定供应商和重复原因的优先级 |
| [PO 匹配诊断](touchless-po-matching-diagnosis.md) | 了解生效规则、容差与决策流程 |
| [文档追踪](touchless-document-trace.md) | 检查原始值、处理运行、阻塞点与人工干预 |
| [变更提案与报告](touchless-change-proposals.md) | 区分预览、应用、效果测量与回滚 |
| [通过 MCP 解释和改进 Touchless](touchless-mcp.md) | 通过 MCP 解释、诊断并执行受控改进 |

<figure><img src="../../../.gitbook/assets/touchless-overview.png" alt="Touchless Intelligence 选项卡，包含五项关键指标、改进建议和 touchless 率图表"><figcaption><p>Touchless Intelligence 选项卡：关键指标、改进项、随时间的比率以及首要流失图表。示例组织，使用演示数据；供应商名称为虚构。</p></figcaption></figure>

## 报告设置

报告读取管理员在 **Settings → Module → Dashboards & Analytics** 中维护的四项组织设置。它们决定目标值和成本视图；字段为空表示 DocBits 使用默认值。

| 设置 | 默认值 | 控制内容 |
| --- | --- | --- |
| Touchless target | 70 % | 应在没有处理干预的情况下通过的文档占比。报告将其用作比率图表中的目标标记。 |
| Minutes per AP intervention | 6 min | AP 员工更正并放行一份文档所需的时间。 |
| Hourly cost | 40 | 按下方货币计的一小时 AP 工作成本。 |
| Currency | EUR | 成本视图使用的货币，为三位字母的 ISO 4217 代码，例如 `EUR`、`CHF` 或 `USD`。DocBits 以大写形式存储该代码，并拒绝不是货币代码的值，因此拼写错误不会进入报告。 |

API 会再次检查存储的值，并对无法使用的值采用默认值。

## 访问权限

此区域属于 [Analytics Dashboard](../)。管理员可访问；其他用户需要相应的角色授权。AI 分析、受支持的变更和咨询报告可能需要管理员权限。

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->
<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
