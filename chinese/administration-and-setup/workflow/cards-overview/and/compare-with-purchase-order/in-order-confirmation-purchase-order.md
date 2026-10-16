---
hidden: true
---

# 订单确认采购订单

当需要根据采购订单检查订单确认时，请在工作流生成器中使用 **Compare with Purchase Order**。将此卡片添加到 **And...** 下方，然后选择订单数据、运算符以及结果的处理方式。以下截图展示了英文界面中的两个可用卡片版本。其字段仍为占位内容；保存前请根据自己的工作流进行设置。

## 将结果写入字段

<figure><img src="../../../../../.gitbook/assets/dbdc-133-workflow-card-write-text.png" alt="工作流生成器中的 Compare with Purchase Order 卡片，包含 Order Data、Operator、Text、Field Name 和 Result of condition 占位内容。" width="563"><figcaption><p>版本 2：根据条件结果将文本写入字段。</p></figcaption></figure>

从订单确认中选择 **Order Data**，并选择用于与采购订单进行比较的 **Operator**。输入要写入的 **Text**，选择 **Field Name**，然后选择触发写入的 **Result of condition**。

## 比较数据

<figure><img src="../../../../../.gitbook/assets/dbdc-133-workflow-card-compare-as.png" alt="工作流生成器中的 Compare with Purchase Order 卡片，包含 Any/All、Order Data、Operator 和 Comparison Data 占位内容。" width="563"><figcaption><p>版本 4：将选定的订单确认数据与采购订单数据进行比较。</p></figcaption></figure>

选择 **Any/All**，以决定是否必须有一个或所有选定条件匹配。然后选择用于采购订单比较的 **Order Data**、**Operator** 和 **Comparison Data**。

有关周边步骤，请参阅 [工作流](../../../) 和 [Compare with Purchase Order](./)。
