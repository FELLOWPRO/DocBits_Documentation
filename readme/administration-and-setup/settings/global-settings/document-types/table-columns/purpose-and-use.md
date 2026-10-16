# 目的和用途

表格列是行项目表格中的一个字段。DocBits 对表格执行的所有操作（提取、验证、采购订单匹配、导出）都会使用此处配置的列。

## 列的显示位置

| 位置 | 列在该处的作用 |
|---|---|
| **验证界面** | 行项目表格中的一列。*Title* 是表头，*Column Type* 决定编辑器类型（金额、日期、文本、是/否）。隐藏列不会显示。 |
| **表格训练** | 训练某个供应商的表格时，需要将检测到的每个表格列映射到这些已配置的列之一。只有已配置的列才能进行映射。 |
| **AI 表格提取** | AI 会填充已配置的列。标记为 *Use AI* 的列即使对于已训练规则的供应商，也会由 AI 填充。 |
| **验证规则** | 行项目检查（例如 *数量 × 单价 = 行总额*）会针对默认列 `QUANTITY`、`UNIT_PRICE`、`TOTAL_AMOUNT`、`CHARGES`、`DISCOUNT` 运行。 |
| **采购订单匹配** | 需要默认列 item number、unit price、quantity 和 total amount。缺少这些列时，文档会显示 *Line Item Table is missing Mandatory column for PO*。 |
| **导出** | 每个非隐藏列都会作为行项目数据的一部分发送到 ERP。导出映射会引用 *Column name*。 |
| **脚本** | 脚本通过 *Column name* 读取和写入列，例如 `row["TOTAL_AMOUNT"]`。 |

## 适用范围

* 表格列按**表格**配置，而表格属于某个**文档类型**。发票列不会影响交货单。
* 配置按**组织**设置。子组织会继承此配置。
* 某个供应商需要填充哪些列，由该供应商的训练结果或 AI 决定；列配置仅用于指定有哪些列。

## 更改配置的常见原因

* 需要按行捕获客户特定的值（成本中心、项目编号、内部货号）→ 添加一列。
* 某个默认列从未使用，却让验证界面显得杂乱 → 将其隐藏。
* 导出前必须始终填写某一列 → 将其标记为 *Required*。
* 某个值来自 ERP 查询，用户不得编辑 → 将其标记为 *Read Only*。
* AI 对某列的提取效果优于训练规则（例如自由文本描述）→ 将其标记为 *Use AI*。

## 相关页面

* [添加新列](adding-a-new-column.md)
* [编辑和删除列](editing-and-deleting-columns.md)
* [表格提取故障排除](../../../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md)
