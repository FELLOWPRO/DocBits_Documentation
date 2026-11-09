# 容差范围内的单位费用

以下场景用于说明一种已配置的映射，并不代表已核实部署的默认模板。实际输出、金额、正负号和文档类型取决于当前生效的 `conflict_resolution` 规则与表达式、导出映射及审批决定。下文提到的借项通知单或贷项通知单均以这些配置为前提；示例不保证自动开具，也不保证符合法律要求。

## 场景：

发票上的 Charge Per Unit 与采购订单相比，处于可接受的容差范围内。

## 操作：

系统接受发票上的 Charge Per Unit，并且不做调整，直接处理该交易。

## 示例：

* **Purchase Order (PO):**
  * Charge Per Unit: $5.00
  * Quantity: 500 units
  * Total Charge Amount: $2,500.00
* **Invoice Received:**
  * Charge Per Unit: $5.10 (variance 2%, within the ±3% tolerance)
  * Quantity: 500 units
  * Total Charge Amount: $2,550.00
* **Tolerance Levels:**
  * Charge Per Unit Tolerance: ±3%

由于 Charge Per Unit（$5.10）与采购订单相比处于 3% 的可接受容差范围内，系统将：

1. **Accept the Charge Per Unit:**系统接受发票上的 Charge Per Unit $5.10，因为它处于定义的容差限值内。
2. **Process the Transaction:**系统根据发票上的 Charge Per Unit 和 Quantity，按 Total Charge Amount 处理发票：
   * **Total Charge Amount = Quantity × Charge Per Unit**
   * **Total Charge Amount = 500 units × $5.10 = $2,550.00**
3. **Finalize the Invoice:**系统不做任何调整，直接处理该交易并接受发票内容。

这种方式使系统能够处理费用中的小幅可接受差异，确保交易处理顺畅高效，避免不必要的拒绝或延迟。
