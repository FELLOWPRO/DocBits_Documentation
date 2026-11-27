# 案例 14：抬头费用 - 单位费用超出容差（已审批）

以下场景用于说明一种已配置的映射，并不代表已核实部署的默认模板。实际输出、金额、正负号和文档类型取决于当前生效的 `conflict_resolution` 规则与表达式、导出映射及审批决定。下文提到的借项通知单或贷项通知单均以这些配置为前提；示例不保证自动开具，也不保证符合法律要求。

## 场景：

抬头单位费用超出容差，但已获得审批。

## 操作：

系统处理已审批的单位费用，并将其应用于交易。

## 示例：

* **Purchase Order (PO):**
  * Header Charge Per Unit: $2.50
  * Quantity: 2,000 units
  * Total Header Charge Amount: $5,000.00
* **Invoice Received:**
  * Header Charge Per Unit: $3.00 — 20% above the PO value, outside the configured ±5% tolerance; approved.
  * Quantity: 2,000 units
  * Total Header Charge Amount: $6,000.00
* **Tolerance Levels:**
  * Header Charge Per Unit Tolerance: ±5%

由于抬头单位费用（$3.00）超出 5% 的可接受容差范围，但已获得审批，系统将：

1. **接受已审批的抬头单位费用：** 尽管超出容差限值，系统仍接受已审批的发票抬头单位费用 $3.00。
2. **处理抬头费用：** 系统使用已审批的单位费用和数量处理发票：
   * **Total Header Charge Amount = Quantity × Approved Header Charge Per Unit**
   * **Total Header Charge Amount = 2,000 units × $3.00 = $6,000.00**
3. **完成发票处理：** 系统使用已审批的费用处理交易，反映 $6,000.00 的总金额。

这种处理方式使系统能够接受已审批的抬头费用差异，确保交易按照审批结果处理，同时保持财务记录准确。
