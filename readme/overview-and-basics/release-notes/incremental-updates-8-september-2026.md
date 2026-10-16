# 2026年9月8日热修复

> 采购订单匹配：了解 2026 年 9 月 8 日部署的热修复带来了哪些变化。以下行为已在开发环境生效，并将在下一轮升级中发布到 stage、sandbox 和生产环境。

## 采购订单匹配

- **保存后仍会保留匹配。** 过去，转换规则每次保存时都会静默丢弃采购订单匹配（即重建行项目的规则）。现在，只要规则生成的行项目相同，就会保留匹配。如果规则确实替换了已匹配的行项目，文档会记录该规则，屏幕也会显示规则名称。
- **保存时会再次执行匹配。** 如果文档中的采购订单号发生变化，或者主数据在处理后填入了采购订单号、但系统尚未查找该号码，保存时会立即匹配文档。保存操作绝不会覆盖现有匹配。
- **屏幕会说明未匹配的原因。** Purchase Order Matching 屏幕会在采购订单区域上方显示一句说明：没有采购订单号、在 ERP 中未找到采购订单、尚未查找、已加载但未关联、没有行项目匹配、没有表格、表格列未映射，或没有剩余未结行项目。被排除的候选项会连同原因一起列出（例如，读入采购订单列的发票号码）。
- **已丢弃的匹配绝不会被报告为已保存。** 如果服务器未保留某个匹配，屏幕会恢复该匹配，将文档标记为未保存，并说明拒绝原因，而不是显示“已保存”。
- **匹配历史会显示转换规则。** 文档的匹配历史现在会在第一个匹配阶段之前增加一个 _Transformation rules_ 步骤，列出已运行的规则，以及其中是否有规则丢弃了匹配。管理员还会看到指向规则的链接。
- **根据净金额计算采购订单单价。** 开启 _Calculate PO unit price_ 后，系统现在会优先根据采购订单行项目的**净金额**计算单价；只有没有净金额时，才使用总金额。来自 Infor 的采购订单会将税额计入行项目总额；对于按净价计价的发票，过去显示的“unit price under-matched”差额恰好等于税率。每次匹配时都会刷新计算出的单价，因此现有文档无需重新加载采购订单也能受益。
- **发票号码不再被误认为采购订单号。** 如果行项目列或先前查找得到的候选号码与文档自身的发票号码相同，该候选项将被排除。

## 文档

- 新增页面 [转换规则](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md)。
- [采购订单匹配规则](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) 现已介绍规则类型、启用条件、回退规则、默认规则集、容差类型和生效列。
- [计算采购订单单价](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/calculate-po-unit-price.md) 介绍净金额计算方式。
- [采购订单匹配屏幕](../../end-user-and-partner-section/end-user-section/purchase-order-matching/README.md) 说明“为何没有匹配”消息和匹配历史。
