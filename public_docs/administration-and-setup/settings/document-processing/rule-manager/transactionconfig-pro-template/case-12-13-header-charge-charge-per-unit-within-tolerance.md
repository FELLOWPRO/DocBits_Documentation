# 单位抬头费用在容差范围内

以下场景用于说明一种已配置的映射，并不代表已核实部署的默认模板。实际输出、金额、正负号和文档类型取决于当前生效的 `conflict_resolution` 规则与表达式、导出映射及审批决定。下文提到的借项通知单或贷项通知单均以这些配置为前提；示例不保证自动开具，也不保证符合法律要求。

## 场景：

与采购订单相比，单位抬头费用在可接受的容差范围内。

## 操作：

系统按发票所列金额处理抬头费用，不作调整。

## 示例：

* **Purchase Order (PO):**
  * Header Charge Per Unit: $3.50
  * Quantity: 1,200 units
  * Total Header Charge Amount: $4,200.00
* **Invoice Received:**
  * Header Charge Per Unit: $3.55 — 1.43% above the PO value, within the configured ±2% tolerance.
  * Quantity: 1,200 units
  * Total Header Charge Amount: $4,260.00
* **Tolerance Levels:**
  * Header Charge Per Unit Tolerance: ±2%

由于单位抬头费用（$3.55）与采购订单相比处于 2% 的可接受容差范围内，系统将：

1. **接受单位抬头费用：**系统接受发票所列的单位抬头费用 $3.55，因为该金额在规定的容差限值内。
2. **处理抬头费用：**系统根据发票所列的单位费用和数量，按抬头费用总额处理发票：
   * **Total Header Charge Amount = Quantity × Header Charge Per Unit**
   * **Total Header Charge Amount = 1,200 units × $3.55 = $4,260.00**
3. **完成发票处理：**系统无需进行任何调整即可处理该交易，并按原样接受发票。

这种方法可确保在抬头费用处于可接受的容差范围内时，交易得到顺畅、高效的处理，避免不必要的拒收或延误。
