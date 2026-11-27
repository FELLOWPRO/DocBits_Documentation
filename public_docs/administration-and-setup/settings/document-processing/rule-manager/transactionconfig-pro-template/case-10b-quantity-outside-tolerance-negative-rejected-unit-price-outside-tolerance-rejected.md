# 案例 10b：数量超出容差（拒绝），单价超出容差（拒绝）

以下场景用于说明一种已配置的映射，并不代表已核实部署的默认模板。实际输出、金额、正负号和文档类型取决于当前生效的 `conflict_resolution` 规则与表达式、导出映射及审批决定。下文提到的借项通知单或贷项通知单均以这些配置为前提；示例不保证自动开具，也不保证符合法律要求。

## 场景：

数量和单价均超出容差，且两者都未获审批。

## 操作：

系统拒绝发票数据，将数值调整为与采购订单一致，并生成所需的借项或贷项通知单。

## 示例：

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Unit Price: $30.00 per unit
  * Total Amount: $4,500.00
* **Invoice Received:**
  * Quantity: 140 units — 6.67% below the PO value, outside the configured ±5% tolerance; rejected.
  * Unit Price: $33.00 per unit — 10% above the PO value, outside the configured ±2% tolerance; rejected.
  * Total Amount: $4,620.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

由于数量（140 件）和单价（$33.00）均超出可接受的容差范围，且两者都未获审批，系统将：

1. **拒绝发票数据：**由于开票数量和单价偏离容差范围，系统不予接受。
2. **调整数量：**系统将数量调整为与原采购订单数量一致。
   * Adjusted Quantity = 150 units (from PO)
3. **调整单价：**系统将单价调整为与原采购订单单价一致。
   * Adjusted Unit Price = $30.00 per unit (from PO)
4. **重新计算总金额：**系统使用调整后的数量和单价重新计算总金额：
   * **Corrected Total Amount = Adjusted Quantity × Adjusted Unit Price**
   * **Corrected Total Amount = 150 units × $30.00 per unit = $4,500.00**
5. **生成借项通知单：**由于原发票总金额高于更正后的总金额，系统会针对多收金额生成借项通知单。
   * **Debit Note Amount = Original Invoice Total - Corrected Total Amount**
   * **Debit Note Amount = $4,620.00 - $4,500.00 = $120.00**
6. **处理发票：**系统以更正后的总金额 $4,500.00 处理发票，并开具金额为 $120.00 的借项通知单，以抵消多收金额。

这种处理方式可确保财务交易符合采购订单条款，从而保持开票准确、公平。
