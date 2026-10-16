# 卡片

卡片是每个工作流的构建模块。你可以将它们组合到 **When / And / Then** 组中，描述工作流何时运行以及执行什么操作。本节介绍可用的卡片及其功能。

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="按类别分组的 Add Card 卡片库"><figcaption><p><strong>Add Card</strong> 卡片库 — 卡片按类别分组。</p></figcaption></figure>

## 卡片组

* **When** — 启动工作流的触发卡片（例如文档类型、多个文档类型中的任意一种）。
* **And** — 在执行操作之前必须同时满足的条件卡片。这些卡片包括 _Compare with Purchase Order_（采购订单匹配）、_Document Field_ 比较、_Date & Time_、_Logic_、_Status_、_Table_ 和 _Assignee_ 条件。
* **Then** — 执行具体操作的卡片：设置字段、批准或拒绝、更改状态、导出、创建任务、分配文档、操作表格，以及运行操作（Call API、Send HTTPS request、Run Workflow、AI calculations）。

## 卡片参考指南

如需查看每种卡片及其选项的完整参考，请参阅本节中的_完整指南_页面（条件卡片、采购订单匹配卡片、分配与用户卡片、任务卡片、字段与表格卡片以及操作卡片）。

## 组合卡片

如需了解经过验证、可解决常见业务场景的卡片组合，请参阅 **Workflow Pattern Guides**。
