# 案例 14：费用行 - 单位费用超出容差（已批准）

以下场景用于说明一种已配置的映射，并不代表已核实部署的默认模板。实际输出、金额、正负号和文档类型取决于当前生效的 `conflict_resolution` 规则与表达式、导出映射及审批决定。下文提到的借项通知单或贷项通知单均以这些配置为前提；示例不保证自动开具，也不保证符合法律要求。

## 场景：

单位费用超出容差，但已获批准。

## 操作：

系统接受该单位费用并应用已批准的费用，据此处理交易。

## 示例：

* **Purchase Order (PO):**
  * Charge Per Unit: $4.50
  * Quantity: 1,000 units
  * Total Charge Amount: $4,500.00
* **Invoice Received:**
  * Charge Per Unit: $5.00 — 11.11% above the PO value, outside the configured ±5% tolerance; approved.
  * Quantity: 1,000 units
  * Total Charge Amount: $5,000.00
* **Tolerance Levels:**
  * Charge Per Unit Tolerance: ±5%

由于单位费用（$5.00）超出 5% 的可接受容差范围，但已获批准，系统将：

1. **Accept the Approved Charge Per Unit:**尽管超出容差限制，系统仍接受已批准的发票单位费用 $5.00。
2. **Process the Transaction:**系统使用已批准的单位费用和数量处理发票：
   * **Total Charge Amount = Quantity × Approved Charge Per Unit**
   * **Total Charge Amount = 1,000 units × $5.00 = $5,000.00**
3. **Finalize the Invoice:**系统使用已批准的费用处理交易，反映 $5,000.00 的总金额。

这种做法确保系统能够处理已批准的费用差异，在保持财务记录准确的同时提供灵活性。
