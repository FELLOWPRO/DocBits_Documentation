# 超出容差的单位费用（已拒绝）

以下场景用于说明一种已配置的映射，并不代表已核实部署的默认模板。实际输出、金额、正负号和文档类型取决于当前生效的 `conflict_resolution` 规则与表达式、导出映射及审批决定。下文提到的借项通知单或贷项通知单均以这些配置为前提；示例不保证自动开具，也不保证符合法律要求。

## 场景：

单位费用超出容差，且尚未获得审批。

## 操作：

系统会调整单位费用，使其与采购订单或已批准的金额一致，并按需生成借项通知单或贷项通知单。

## 示例：

* **Purchase Order (PO):**
  * Charge Per Unit:$6.00
  * Quantity:800 件
  * Total Charge Amount:$4,800.00
* **Invoice Received:**
  * Charge Per Unit:$7.00（偏差 16.67%，超出 ±5% 的容差，已拒绝）
  * Quantity:800 件
  * Total Charge Amount:$5,600.00
* **Tolerance Levels:**
  * Charge Per Unit Tolerance:±5%

由于单位费用（$7.00）超出 5% 的可接受容差范围，且尚未获得审批，系统将执行以下操作：

1. **Reject the Invoiced Charge Per Unit:**由于差异超出容差限值，系统不接受发票中的单位费用 $7.00。
2. **Adjust the Charge Per Unit:**系统会将单位费用调整为与采购订单或已批准的单位费用一致：
   * Adjusted Charge Per Unit = $6.00（来自 PO）
3. **Recalculate the Total Charge Amount:**系统会根据调整后的单位费用重新计算费用总额：
   * **Corrected Total Charge Amount = Quantity × Adjusted Charge Per Unit**
   * **Corrected Total Charge Amount = 800 units × $6.00 = $4,800.00**
4. **Generate a Debit Note:**由于原发票总额高于更正后的总额，系统会针对多收的金额生成借项通知单：
   * **Debit Note Amount = Original Invoice Total - Corrected Total Charge Amount**
   * **Debit Note Amount = $5,600.00 - $4,800.00 = $800.00**
5. **Process the Invoice:**系统会按更正后的费用总额 $4,800.00 处理发票，并开具 $800.00 的借项通知单，以处理多收的金额。

此方法可确保财务交易符合采购订单条款，拒绝未经审批的差异，并保持计费准确。
