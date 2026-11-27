# 案例 15：抬头费用——单位费用超出容差范围（已拒绝）

以下场景用于说明一种已配置的映射，并不代表已核实部署的默认模板。实际输出、金额、正负号和文档类型取决于当前生效的 `conflict_resolution` 规则与表达式、导出映射及审批决定。下文提到的借项通知单或贷项通知单均以这些配置为前提；示例不保证自动开具，也不保证符合法律要求。

## 场景：

抬头单位费用超出容差范围，且尚未获得批准。

## 操作：

系统将抬头费用调整为与采购订单一致，并据此处理交易，同时生成任何必要的备注。

## 示例：

* **Purchase Order (PO):**
  * Header Charge Per Unit: $4.00
  * Quantity: 1,500 units
  * Total Header Charge Amount: $6,000.00
* **Invoice Received:**
  * Header Charge Per Unit: $5.00 — 25% above the PO value, outside the configured ±5% tolerance; rejected.
  * Quantity: 1,500 units
  * Total Header Charge Amount: $7,500.00
* **Tolerance Levels:**
  * Header Charge Per Unit Tolerance: ±5%

由于抬头单位费用（$5.00）超出 5% 的可接受容差范围，且尚未获得批准，系统将：

1. **Reject the Invoiced Header Charge Per Unit:**由于差异超出容差限值，系统不接受发票中的 $5.00 抬头单位费用。
2. **Adjust the Header Charge Per Unit:**系统将单位费用调整为与原始采购订单或已批准的单位费用一致：
   * Adjusted Header Charge Per Unit = $4.00 (from PO)
3. **Recalculate the Total Header Charge Amount:**系统根据调整后的单位费用重新计算费用总额：
   * **Corrected Total Header Charge Amount = Quantity × Adjusted Header Charge Per Unit**
   * **Corrected Total Header Charge Amount = 1,500 units × $4.00 = $6,000.00**
4. **Generate a Credit Note:**由于原始发票总额高于更正后的总额，系统会针对多收的金额生成贷项通知单：
   * **Credit Note Amount = Original Invoice Total - Corrected Total Header Charge Amount**
   * **Credit Note Amount = $7,500.00 - $6,000.00 = $1,500.00**
5. **Process the Invoice:**系统按更正后的费用总额 $6,000.00 处理发票，并开具金额为 $1,500.00 的贷项通知单，以抵扣多收的金额。

此方法可确保交易符合采购订单的原始条款，在更正多收费用的同时，保持财务处理准确。
