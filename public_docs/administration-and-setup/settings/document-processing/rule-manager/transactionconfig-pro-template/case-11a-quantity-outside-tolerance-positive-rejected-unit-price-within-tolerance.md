# 案例 11a：数量超出容差（正向超差被拒绝），单价在容差范围内

以下场景用于说明一种已配置的映射，并不代表已核实部署的默认模板。实际输出、金额、正负号和文档类型取决于当前生效的 `conflict_resolution` 规则与表达式、导出映射及审批决定。下文提到的借项通知单或贷项通知单均以这些配置为前提；示例不保证自动开具，也不保证符合法律要求。

## 场景：

发票上的数量超出可接受范围（正向超差）并被拒绝，但单价在容差范围内。

## 操作：

系统将数量调整为已批准的水平，同时保持单价不变，并处理该交易。超出的数量将被拒绝且不会开票。

## 示例：

* **Purchase Order (PO):**
  * Quantity: 100 units
  * Unit Price: $8.00 per unit
  * Total Amount: $800.00
* **Invoice Received:**
  * Quantity: 110 units — 10% above the PO value, outside the configured ±5% tolerance; rejected.
  * Unit Price: $8.00 per unit (within tolerance)
  * Total Amount: $880.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

由于数量（110 件）超出可接受的容差限值（正向偏差 10%）且未获批准，而单价（$8.00）在容差范围内，系统将：

1. **拒绝超出部分：**系统拒绝超出已批准容差级别的数量。
2. **调整数量：**系统将数量调整为采购订单中指定的已批准数量。
   * Approved Quantity = 100 units (from PO)
3. **保持单价不变：**每件 $8.00 的单价在容差范围内，因此保持不变。
4. **重新计算总金额：**系统使用已批准的数量和接受的单价计算总金额：
   * **Total Amount = Approved Quantity × Unit Price**
   * **Total Amount = 100 units × $8.00 per unit = $800.00**
5. **处理发票：**系统按调整后的总金额 $800.00 处理发票，仅反映已批准的数量和单价。超出的 10 件数量将被拒绝且不会开票。

即使供应商尝试对超出部分开票，这种方式也能确保发票金额符合采购订单中约定的条款。
