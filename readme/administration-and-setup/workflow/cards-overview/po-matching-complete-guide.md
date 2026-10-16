# 采购订单匹配卡片 - 完整指南

## 采购订单（PO）匹配卡片 - 完整指南

**状态：**涵盖 15 张 PO 比较卡片及其详细计算

***

本页介绍的 PO 比较卡片应添加到工作流构建器的 **And** 组中——它们会在 Then 操作运行之前，将发票数据与匹配的采购订单进行比较：

<figure><img src="../../../.gitbook/assets/workflow_designer_cards.png" alt="工作流构建器画布，包含 When、And 和 Then 卡片组"><figcaption><p>通过 <strong>Add Card</strong> 将 PO 比较卡片添加到 <strong>And</strong> 组。</p></figcaption></figure>

***

### 📌 版本信息

**演进最充分的卡片：** CONDITION\_DOC\_TO\_PO\_UNIT\_PRICE（5 个版本，最新为 v5） **其他复杂卡片：** CONDITION\_OC\_TO\_PO\_ITEMS（v4）、CONDITION\_LESS\_THAN\_TOLERANCE\_AS\_VALUE\_OF\_ORDERED\_QUANTITY（v4）

**主要模式：**

* **v2 → v3+：**增加容差参数，实现灵活匹配
* **v3 → v4：**增加比较模式参数
* **v4 → v5：**增强容差设置，支持多种单位（%、EUR、$ 等）

📖 [完整版本历史](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/administration-and-setup/changelog/release.md#-po-comparison--validation-cards) | [卡片版本数据库](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/DocFlow/docs/card_version.md)

***

### 了解 PO 匹配

收到发票后，应将其与之前下达的采购订单（PO）进行匹配。PO 匹配卡片会自动检查发票数据是否与 PO 数据相符。

**整体流程：**

```
PO Placed     Invoice Arrives     PO Matching     Decision
(€100)    →   (€103)          →   (Check if       → Approve/Reject
Qty: 100      Qty: 100            within tolerance)
```

***

## 1. 采购订单完整匹配 <a id="full-match"></a>

### 用途

检查整张发票是否与 PO 完全匹配，或是否在容差范围内

### 适用场景

* 批准发票之前
* 作为初步质量检查
* 尽早发现问题

### 工作原理

系统会比较：

* 发票数量与 PO 数量
* 发票价格与 PO 价格
* 发票行项目与 PO 行项目
* 发票总额与 PO 总额

### 结果

* **TRUE**（完整匹配）：所有内容均匹配，可以继续
* **FALSE**（不匹配）：存在不匹配项，需要审核

### 示例

```
采购订单：
- Item ABC：数量 100，单价 €50 = €5000
- Item XYZ：数量 50，单价 €20 = €1000
- 总计：€6000

发票：
- Item ABC：数量 100，单价 €50 = €5000
- Item XYZ：数量 50，单价 €20 = €1000
- 总计：€6000

结果：✅ 完全匹配
```

***

## 2. 单价比较（文档与 PO） <a id="unit-price"></a> <a id="unit-price-comparison"></a>

### 用途

比较发票上的单价与 PO 上的单价

### 参数

* **单价容差**：允许的差异上限
* **容差类型**：百分比（%）或绝对金额（€/$）
* **运算符**：等于、大于、小于等

### 工作原理（百分比容差）

**公式：**

```
Variance % = |(Invoice Price - PO Price)| / PO Price × 100

Check: Is Variance % ≤ Tolerance %?
```

**分步示例：**

```
Step 1: Get prices
  PO Unit Price: €100.00
  Invoice Unit Price: €103.00

Step 2: Calculate difference
  Difference = |€103.00 - €100.00| = €3.00

Step 3: Calculate percentage
  Percentage = (€3.00 / €100.00) × 100 = 3%

Step 4: Check tolerance (5% allowed)
  Is 3% ≤ 5%? YES ✅

Result: PASS - Within tolerance
```

### 实际示例

#### 示例 1：小幅涨价（接受）

```
PO Price: €50.00
Invoice Price: €51.50
Tolerance: ±3%

Calculation:
  Variance = |(€51.50 - €50.00)| / €50.00 × 100
  Variance = €1.50 / €50.00 × 100 = 3%

Is 3% ≤ 3%? YES ✅ ACCEPT
```

#### 示例 2：大幅涨价（拒绝）

```
PO Price: €50.00
Invoice Price: €55.00
Tolerance: ±3%

Calculation:
  Variance = |(€55.00 - €50.00)| / €50.00 × 100
  Variance = €5.00 / €50.00 × 100 = 10%

Is 10% ≤ 3%? NO ❌ REJECT - NEEDS REVIEW
```

#### 示例 3：折扣（同样会检查）

```
PO Price: €100.00
Invoice Price: €97.00
Tolerance: ±5%

Calculation:
  Variance = |(€97.00 - €100.00)| / €100.00 × 100
  Variance = €3.00 / €100.00 × 100 = 3%

Is 3% ≤ 5%? YES ✅ ACCEPT (Discount is within tolerance)
```

#### 示例 4：绝对金额容差

```
PO Price: €10.00
Invoice Price: €10.50
Tolerance: ±€1.00 (absolute, not %)

Calculation:
  Variance = |€10.50 - €10.00| = €0.50

Is €0.50 ≤ €1.00? YES ✅ ACCEPT
```

### 如何处理结果

**如果通过 ✅：**

* 继续进行下一项检查
* 或批准发票
* 或继续导出

**如果未通过 ❌：**

* 标记为需要人工审核
* 向供应商询问原因
* 联系采购团队
* 如果可以接受，则附注后批准

***

## 3. 数量比较 <a id="quantity"></a> <a id="quantity-comparison"></a>

### 用途

检查订购数量是否与发票数量相符

### 参数

* **容差**：允许的数量或百分比差异
* **运算符**：等于、大于、小于
* **数量类型**：已订购、已收货、未完成

### 计算示例

**百分比容差：**

```
Formula:
  Quantity Variance % = |(Invoice Qty - PO Qty)| / PO Qty × 100

Example:
  PO Quantity: 100 units
  Invoice Quantity: 103 units
  Tolerance: ±5%

  Variance = |(103 - 100)| / 100 × 100
  Variance = 3 / 100 × 100 = 3%

  Is 3% ≤ 5%? YES ✅ ACCEPT
```

**绝对容差：**

```
Formula:
  Quantity Variance = |Invoice Qty - PO Qty|

Example:
  PO Quantity: 100 units
  Invoice Quantity: 102 units
  Tolerance: ±5 units

  Variance = |102 - 100| = 2 units

  Is 2 units ≤ 5 units? YES ✅ ACCEPT
```

### 实际场景

#### 超量交付（交付量超过订购量）

```
Ordered: 100 units
Invoiced: 110 units
Tolerance: ±5%

Variance = |(110-100)|/100 × 100 = 10%

Is 10% ≤ 5%? NO ❌

Decision: Contact supplier - more delivered than ordered
Possible reason: Error by supplier, partial shipment already received
```

#### 未足量交付（交付量少于订购量）

```
Ordered: 100 units
Invoiced: 95 units
Tolerance: ±5%

Variance = |(95-100)|/100 × 100 = 5%

Is 5% ≤ 5%? YES ✅

Decision: Accept - within tolerance
Possible reason: Partial shipment, rest to follow
```

***

## 4. 数量差异对应的合并价格

### 用途

数量存在差异时，计算总价差异是否可以接受

### 重要原因

```
Scenario: You ordered 100 units but received 110
- Quantity is 10% over (bad)
- BUT: You're only charged for 10% extra
- Combined effect might be acceptable
```

### 计算

**公式：**

```
Combined Variance = Quantity Variance × Price Variance

If both are within tolerance, combined is usually acceptable
```

**示例：**

```
PO:
- Unit Price: €100
- Quantity: 100
- Total: €10,000

Invoice:
- Unit Price: €102 (2% higher)
- Quantity: 105 (5% higher)
- Total: €10,710

Analysis:
- Price variance: 2% ✅
- Quantity variance: 5% ✅
- Combined effect: 1.02 × 1.05 = 1.071 = 7.1% total increase

Is combined variance acceptable? Usually YES ✅
```

***

## 5. 行项目 ID / 供应商行项目编号比较

### 用途

检查发票中的行项目是否与 PO 中的行项目相符

### 工作原理

**精确匹配（最简单）：**

```
PO Item ID: ABC-123
Invoice Item ID: ABC-123
Result: ✅ MATCH
```

**供应商行项目编号（更常见）：**

```
PO Item: ABC-123 (Our internal code)
Supplier Item: SUPP-456 (Their code for same item)
System matches these as same item
Result: ✅ MATCH
```

### 场景：如果不匹配怎么办？

```
采购订单行项目：ABC-123 (Copper Wire, 2mm)
发票行项目：ABC-124 (Steel Wire, 2mm)

结果：❌ 不匹配

处理措施：
1. 这是替代品吗？请与采购部门确认
2. 这是错误吗？请联系供应商
3. 描述是否相似？请手动验证
```

***

## 6. 订单类型验证

### 用途

验证采购订单类型是否正确

### 订单类型

* **标准订单**：常规采购
* **加急订单**：紧急订单，可能包含溢价
* **框架协议**：长期合同
* **总括订单**：开放式合同
* **寄售**：使用后才付款

### 检查示例

```
PO Order Type: Standard Order
Invoice Order Type: Standard Order
Result: ✅ MATCH

If mismatch: Could affect terms, payment, pricing
```

***

## 7. 交付日期验证

### 用途

检查交付日期是否与 PO 中承诺的日期相符

### 计算

**延迟交付：**

```
Formula:
  Days Late = Invoice Delivery Date - PO Promised Date

Example:
  PO Promised: 2025-10-15
  Actual Delivery: 2025-10-22
  Days Late = 7 days

If tolerance is ±3 days:
  Is 7 ≤ 3? NO ❌ LATE
```

**提前交付：**

```
Formula:
  Days Early = PO Promised Date - Invoice Delivery Date

Example:
  PO Promised: 2025-10-15
  Actual Delivery: 2025-10-10
  Days Early = 5 days

Early delivery is usually OK ✅
Unless you need it at specific time
```

### 容差设置

```
±3 days: Allow 3 days late or early
±5 days: Allow up to 5 days variance
0 days: Must match exactly
```

***

## 8. 费用验证（税费、运费等）

### 用途

检查附加费用（税费、运费、手续费）是否与 PO 相符

### 常见费用

```
- Shipping: €50
- Handling: €10
- Packaging: €5
- Insurance: €15
- Taxes: €300
```

### 计算

**示例：运费检查**

```
PO Shipping: €50.00
Invoice Shipping: €51.00
Tolerance: ±3%

Variance = |€51.00 - €50.00| / €50.00 × 100 = 2%

Is 2% ≤ 3%? YES ✅ ACCEPT
```

**示例：多项费用**

```
PO Total Charges:
  - Shipping: €50
  - Taxes: €300
  - Handling: €10
  Total: €360

Invoice Total Charges:
  - Shipping: €50
  - Taxes: €312 (11% tax)
  - Handling: €10
  Total: €372

Difference: €12
Check if within tolerance ✅ or ❌
```

***

## 9. 税费验证 <a id="tax-lines"></a>

### 用途

验证税额计算是否正确

### 计算

**公式：**

```
Tax Amount = Subtotal × Tax Rate

Example:
  Subtotal: €1000
  Tax Rate: 19%
  Expected Tax: €1000 × 0.19 = €190

Invoice Tax: €190
Match? YES ✅
```

**常见问题：**

```
1. Tax rate changed (region-based)
2. Tax applied to wrong amount (before/after discounts)
3. Multiple tax rates (some items 7%, others 19%)
4. Tax exempt items (0% tax)
```

**示例：多税率计税**

```
Item A: €100 @ 19% tax = €119
Item B: €100 @ 7% tax = €107
Item C: €100 @ 0% tax = €100
Total: €326

Invoice shows €325 (€1 error)

Check: Within tolerance or needs attention?
```

***

## 10. 设施/成本中心匹配

### 用途

确保发票对应正确的设施/成本中心

### 示例

```
PO is for:
- Facility: Berlin Plant
- Cost Center: CC-2025

Invoice should have:
- Facility: Berlin Plant ✅
- Cost Center: CC-2025 ✅

If different facility: May need different approval
```

***

## 11. 供应商状态验证

### 用途

检查供应商是否仍处于已批准/有效状态

### 状态类型

```
✅ ACTIVE: Approved, can do business
⚠️ ON HOLD: Temporarily blocked
❌ INACTIVE: No longer doing business
⚠️ CONDITIONAL: Only for specific items
```

### 检查示例

```
Supplier: ABC Corp
Status in Database: ACTIVE
Status when creating PO: ACTIVE
Status when invoice arrives: INACTIVE

Alert: Supplier status changed! Investigate why.
```

***

## 应使用哪种容差？

### 严格容差（风险较低，人工工作较多）

```
Use for:
- High-value items
- Items where exactness matters
- Regulated industries

Settings:
- Unit Price: ±1%
- Quantity: ±1%
- Delivery Date: ±1 day
- Charges: ±1%
```

### 中等容差（平衡）

```
Use for:
- Most business transactions
- Standard items
- Normal purchasing

Settings:
- Unit Price: ±3-5%
- Quantity: ±3-5%
- Delivery Date: ±3 days
- Charges: ±5%
```

### 宽松容差（风险较高，人工工作较少）

```
Use for:
- Low-value items
- Bulk purchases
- Supplier agreements with flexibility

Settings:
- Unit Price: ±10%
- Quantity: ±10%
- Delivery Date: ±7 days
- Charges: ±10%
```

***

## PO 匹配工作流示例

```
发票到达
    ↓
条件："Is amount > €5000?"（金额是否 > €5000？）→ YES（是）
    ↓
检查：是否完全匹配？→ NO（否）（价格相差 10%）
    ↓
检查：单价是否在 5% 范围内？→ NO（否）（相差 12%）
    ↓
检查：数量是否在 5% 范围内？→ YES（是）（相差 2%）
    ↓
决定：FAIL（失败）- 价格差异过大
    ↓
标记为：手动审核 / 采购员审批
    ↓
等待：采购员评论
    ↓
如果已批准：继续导出
如果已拒绝：退回供应商
```

***

## PO 匹配故障排除

### “未找到 PO”

```
Cause: Invoice PO number doesn't exist in system
Fix:
1. Verify PO number spelling
2. Check if PO was created
3. Verify PO is in correct organization
4. Ask supplier for PO reference
```

### “行项目不匹配”

```
Cause: Invoice items are different from PO items
Possible Reasons:
1. Substitution approved by procurement
2. Different item numbers for same item
3. Error by supplier
Fix: Contact procurement or supplier
```

### “价格高于 PO”

```
Cause: Invoice price > PO price
Possible Reasons:
1. Price increase approved
2. Supplier error
3. Currency difference
4. Additional services included
Fix: Verify with procurement
```

### “交付日期错误”

```
Cause: Invoice dated after promised delivery
Possible Reasons:
1. Shipment was delayed
2. Receiving date different from invoice date
3. Partial shipment
Fix: Check shipping documents or contact supplier
```

***

## 汇总表

| 卡片 | 检查内容 | 主要计算 | 常见容差 |
| -------------- | --------------------- | -------------------- | ---------------- |
| 完整匹配 | 所有内容 | 所有检查 | 不定 |
| 单价 | 单位价格 | % 或 € 差异 | ±3-5% |
| 数量 | 订购数量 | % 或数量差异 | ±3-5% |
| 合并价格 | 数量变化后的总价 | 数量 × 价格 | ±5-10% |
| 行项目 ID | 行项目是否正确 | 字符串匹配 | 精确 |
| 订单类型 | 采购类型 | 字符串匹配 | 精确 |
| 交付日期 | 到货时间 | 天数差异 | ±3 天 |
| 费用 | 额外费用 | % 或 € 差异 | ±5% |
| 税费 | 税额 | 税率计算 | ±1% |
| 设施 | 成本中心 | 字符串匹配 | 精确 |
| 供应商 | 是否已批准？ | 状态检查 | 仅限有效 |

***

## 相关文档

* 有关完整工作流，请参阅“发票验证”指南
* 有关按行业推荐的数值，请参阅“容差设置”
* 有关失败时的处理方式，请参阅“异常处理”
* 有关具体容差政策，请联系采购团队
