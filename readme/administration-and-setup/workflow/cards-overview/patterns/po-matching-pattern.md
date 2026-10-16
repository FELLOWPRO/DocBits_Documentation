# 采购订单匹配模式

**模式类型：** 验证与比较 **复杂度：** 中高 **预计设置时间：** 60-90 分钟 **常见用例：** 三方匹配、发票验证、差异检查、容差管理

***

您可以在 **Workflow Builder**（工作流仪表板 → 工作流列表 → 添加工作流）中构建此模式。点击 **Add Card**，然后打开 **Compare with Purchase Order** 类别——此类别包含此模式使用的所有匹配卡片（价格、数量、容差和行项目比较卡片）：

<figure><img src="../../../../.gitbook/assets/workflow_add_card_picker.png" alt="Add Card 卡片库，显示 Compare with Purchase Order 卡片"><figcaption><p><strong>Compare with Purchase Order</strong> 类别——此模式中使用的价格、数量、容差和行项目匹配卡片。</p></figcaption></figure>

***

## 模式概览

此模式演示如何在 DocBits 中实现全面的采购订单（PO）匹配工作流。PO 匹配是一项关键控制流程，用于将发票数据与采购订单数据进行比较，以便在审批付款前发现差异。

**此模式的功能：**

1. 根据发票中的 PO 编号检索 PO 数据
2. 比较发票行项目与 PO 行项目
3. 计算差异（价格、数量、总额）
4. 应用容差规则
5. 根据匹配结果转交审批或升级处理
6. 跟踪匹配历史和例外情况

***

## 何时使用此模式

在需要以下功能时使用此模式：

* ✅ 根据采购订单验证发票
* ✅ 在付款前发现定价错误
* ✅ 识别数量差异
* ✅ 执行采购控制
* ✅ 防止重复付款
* ✅ 自动执行三方匹配
* ✅ 减少人工审核发票的工作量

**以下情况不要使用此模式：**

* ❌ 发票没有对应的 PO（非 PO 发票）
* ❌ DocBits 中没有可用的 PO 数据
* ❌ 更倾向于人工审核，而非自动化
* ❌ 业务政策不要求进行 PO 匹配

***

## 了解 PO 匹配

### 三方匹配

**传统采购控制：**

```
Purchase Order (PO)  →  Created when ordering
        ↓
Goods Receipt (GR)   →  Created when receiving
        ↓
Invoice              →  Created by supplier

THREE-WAY MATCH = PO + GR + Invoice all match
```

**DocBits 实施方式（两方匹配）：**

```
Purchase Order (PO)  →  Imported to DocBits
        ↓
Invoice              →  Scanned by DocBits
        ↓
COMPARISON           →  Invoice vs PO validation
```

***

## 差异计算公式

### 单价差异

**公式：**

```
Variance % = |(Invoice Unit Price - PO Unit Price)| / PO Unit Price × 100
```

**示例：**

```
PO Unit Price:       €100.00
Invoice Unit Price:  €103.00

Variance = |103 - 100| / 100 × 100
        = 3 / 100 × 100
        = 3%

Tolerance: 5%
Result: 3% ≤ 5% → PASS ✅
```

***

### 数量差异

**公式：**

```
Variance % = |(Invoice Quantity - PO Quantity)| / PO Quantity × 100
```

**示例：**

```
PO Quantity:        100 units
Invoice Quantity:   98 units

Variance = |98 - 100| / 100 × 100
        = 2 / 100 × 100
        = 2%

Tolerance: 10%
Result: 2% ≤ 10% → PASS ✅
```

***

### 总金额差异

**公式：**

```
Variance % = |(Invoice Total - PO Total)| / PO Total × 100
```

**示例：**

```
PO Total:       €10,000.00
Invoice Total:  €10,450.00

Variance = |10450 - 10000| / 10000 × 100
        = 450 / 10000 × 100
        = 4.5%

Tolerance: 5%
Result: 4.5% ≤ 5% → PASS ✅
```

***

## 完整工作流示例

### 场景：基于容差路由的发票验证

**业务需求：**

* 必须验证所有带有 PO 参考信息的发票
* 价格差异容差：5%
* 数量差异容差：10%
* 总金额差异容差：3%
* 在容差范围内：自动审批
* 超出容差范围：创建审核任务
* 缺少 PO：升级至采购部门处理

**使用的工作流卡片：**

1. CONDITION\_DOC\_FIELD\_EXISTS - 检查是否存在 PO 编号
2. PURCHASE\_ORDER\_FULL\_MATCH - 尝试完整匹配
3. CONDITION\_DOC\_TO\_PO\_UNIT\_PRICE - 检查价格差异
4. CONDITION\_DOC\_TO\_PO\_QUANTITY - 检查数量差异
5. CONDITION\_DOC\_TO\_PO\_TAX\_LINES - 检查税项是否一致
6. ACTION\_SET\_FIELD\_TO\_TEXT - 存储匹配结果
7. tasks\_create - 创建审核任务
8. ACTION\_SEND\_EMAIL\_TO\_GROUPS - 发送通知

***

## 分步实施

### 步骤 1：检查 PO 参考信息

**卡片：** CONDITION\_DOC\_FIELD\_EXISTS 或 CONDITION\_DOC\_FIELD\_CONTAINS

**配置：**

```
Field: PO_Number
Operator: IS NOT EMPTY
```

**逻辑：**

```
IF PO_Number exists:
  → Continue to PO matching
ELSE:
  → Route to "Non-PO Invoice" workflow
  → Create manual review task
  → Skip PO matching
```

**指南参考：** [条件卡片指南](../condition-cards-complete-guide.md)

***

### 步骤 2：检索 PO 数据

**在 DocBits 中自动完成：**

* 系统通过 PO\_Number 字段查找 PO
* 检索 PO 行项目
* 提供数据以供比较

**手动配置（如有需要）：**

```
PO Source: DocBits Master Data
PO Lookup Field: PO_Number
Match Type: Exact Match
Include Closed POs: No (or Yes if policy allows)
```

***

### 步骤 3：检查 PO 完整匹配

**卡片：** PURCHASE\_ORDER\_FULL\_MATCH

**用途：** 快速检查所有内容是否完全匹配

**配置：**

```
Match Level: Full Match
Include: All line items, prices, quantities, totals
Tolerance: None (exact match)
```

**逻辑：**

```
IF Full Match = TRUE:
  → Set "PO_Match_Status" = "FULL MATCH"
  → Auto-approve document
  → Skip detailed checks
  → END ✅

IF Full Match = FALSE:
  → Continue to detailed variance checks
  → Identify specific variances
```

**结果：**

* **TRUE**：完全匹配，自动审批
* **FALSE**：继续执行详细检查

***

### 步骤 4：检查单价差异

**卡片：** CONDITION\_DOC\_TO\_PO\_UNIT\_PRICE（推荐 v5）

**配置：**

```
Comparison Mode: Percentage Variance
Tolerance: 5%
Operator: Variance is Less Than or Equal To
Apply To: All line items
```

**分步说明：**

```
For each line item:
  1. Get Invoice Unit Price
  2. Get PO Unit Price (matched by product code)
  3. Calculate: Variance % = |Invoice - PO| / PO × 100
  4. Check: Variance % ≤ 5%?
  5. Store result
```

**计算示例：**

```
Line Item 1:
  Product: ABC123
  Invoice Price: €52.00
  PO Price: €50.00
  Variance = |52-50|/50 × 100 = 4%
  Tolerance: 5%
  Result: PASS ✅

Line Item 2:
  Product: XYZ789
  Invoice Price: €120.00
  PO Price: €100.00
  Variance = |120-100|/100 × 100 = 20%
  Tolerance: 5%
  Result: FAIL ❌

Overall Result: FAIL (one or more items failed)
```

**指南参考：** [PO 匹配完整指南 - 单价](../po-matching-complete-guide.md#unit-price-comparison)

***

### 步骤 5：检查数量差异

**卡片：** CONDITION\_DOC\_TO\_PO\_QUANTITY

**配置：**

```
Comparison Mode: Percentage Variance
Tolerance: 10%
Operator: Variance is Less Than or Equal To
Apply To: All line items
Allow Under-Delivery: Yes (within tolerance)
Allow Over-Delivery: No (strict)
```

**逻辑：**

```
For each line item:
  1. Get Invoice Quantity
  2. Get PO Quantity
  3. Calculate: Variance % = |Invoice - PO| / PO × 100
  4. Check: Variance % ≤ 10%?
  5. Special rules:
     - Under-delivery: Allow within tolerance
     - Over-delivery: Reject (or apply stricter tolerance)
```

**示例：**

```
Line Item 1:
  Product: ABC123
  Invoice Qty: 98 units
  PO Qty: 100 units
  Variance = |98-100|/100 × 100 = 2%
  Under-delivery: 2% (within 10% tolerance)
  Result: PASS ✅

Line Item 2:
  Product: XYZ789
  Invoice Qty: 115 units
  PO Qty: 100 units
  Variance = |115-100|/100 × 100 = 15%
  Over-delivery: 15% (exceeds 10% tolerance)
  Result: FAIL ❌ (Escalate)
```

**指南参考：** [PO 匹配完整指南 - 数量](../po-matching-complete-guide.md#quantity-comparison)

***

### 步骤 6：检查税项是否一致

**卡片：** CONDITION\_DOC\_TO\_PO\_TAX\_LINES

**配置：**

```
Match Tax Codes: Yes
Match Tax Rates: Yes
Match Tax Amounts: With 1% tolerance
Tax Calculation: Verify recalculation
```

**验证：**

```
1. Check tax codes match (e.g., "VAT19" on both)
2. Check tax rates match (19% on both)
3. Verify tax amount calculation:
   Tax Amount = Net Amount × Tax Rate
4. Allow small rounding differences
```

**示例：**

```
Invoice:
  Net Amount: €100.00
  Tax Rate: 19%
  Tax Amount: €19.00
  Total: €119.00

PO:
  Net Amount: €100.00
  Tax Rate: 19%
  Tax Amount: €19.00
  Total: €119.00

Result: Tax alignment PASS ✅
```

***

### 步骤 7：存储匹配结果

**卡片：** ACTION\_SET\_FIELD\_TO\_TEXT（多个实例）

**配置：**

**字段 1：PO\_Match\_Status**

```
Field: PO_Match_Status
Value: {{CALCULATED}}
Options: "FULL MATCH" | "WITHIN TOLERANCE" | "OUT OF TOLERANCE" | "NO MATCH"
```

**字段 2：Price\_Variance\_Percent**

```
Field: Price_Variance_Percent
Value: {{CALCULATED_PRICE_VARIANCE}}
Format: "4.5%" (example)
```

**字段 3：Quantity\_Variance\_Percent**

```
Field: Quantity_Variance_Percent
Value: {{CALCULATED_QUANTITY_VARIANCE}}
Format: "2.0%" (example)
```

**字段 4：Match\_Details**

```
Field: Match_Details
Value: "Price Variance: 4.5% (within 5% tolerance)\nQuantity Variance: 2.0% (within 10% tolerance)\nTotal: PASS"
```

**指南参考：** [字段操作指南](../field-manipulation-guide.md)

***

### 步骤 8：根据匹配结果路由

**场景 A：完全匹配（完整匹配）**

```
IF PO_Match_Status = "FULL MATCH":
  1. Set Approval_Status = "AUTO APPROVED"
  2. Set Match_Type = "FULL"
  3. ACTION_APPROVE_DOCUMENT
  4. Export to ERP
  5. Send confirmation email
  → END ✅
```

**场景 B：在容差范围内**

```
IF PO_Match_Status = "WITHIN TOLERANCE":
  1. Set Approval_Status = "AUTO APPROVED"
  2. Set Match_Type = "TOLERANCE"
  3. Log variance details
  4. ACTION_APPROVE_DOCUMENT
  5. Export to ERP
  → END ✅
```

**场景 C：超出容差范围（轻微）**

```
IF Variance < 15% (minor exceptions):
  1. Set Match_Status = "REVIEW REQUIRED"
  2. Create Task: "Review PO Variance"
     - Assign to: Accounts Payable Officer
     - Priority: Medium
     - Deadline: 3 days
  3. Send email with variance details
  4. Wait for task completion
  5. IF Approved: Continue processing
     IF Rejected: Return to supplier
```

**场景 D：超出容差范围（严重）**

```
IF Variance ≥ 15% (major exceptions):
  1. Set Match_Status = "ESCALATION REQUIRED"
  2. Create Task: "URGENT: Major PO Variance"
     - Assign to: Procurement Manager
     - Priority: High
     - Deadline: 1 day
  3. Send urgent email to:
     - Procurement Manager
     - Finance Manager
     - Supplier contact
  4. Block document from processing
  5. Wait for resolution
```

**场景 E：缺少 PO 或未匹配**

```
IF PO not found OR no items match:
  1. Set Match_Status = "NO MATCH"
  2. Create Task: "PO Not Found"
     - Assign to: Procurement Team
     - Priority: High
  3. Send email to procurement
  4. Block document
  5. Request PO creation or correction
```

***

## 完整工作流图

```
INVOICE ARRIVES
│
├─ CHECK: Does invoice have PO number?
│  │
│  ├─ NO PO NUMBER ❌
│  │  │
│  │  ├─ Set Match_Status = "NO PO"
│  │  ├─ Route to Non-PO workflow
│  │  └─ Create manual review task
│  │     → END (Non-PO Invoice)
│  │
│  └─ PO NUMBER EXISTS ✅
│     │
│     ├─ RETRIEVE PO DATA
│     │  - Lookup PO by PO_Number
│     │  - Get PO line items
│     │  - Get PO totals
│     │  │
│     │  ├─ PO FOUND ✅
│     │  │  │
│     │  │  ├─ STEP 1: Check Full Match
│     │  │  │  Card: PURCHASE_ORDER_FULL_MATCH
│     │  │  │  │
│     │  │  │  ├─ FULL MATCH ✅✅✅
│     │  │  │  │  │
│     │  │  │  │  ├─ Set Match_Status = "FULL MATCH"
│     │  │  │  │  ├─ Auto-Approve
│     │  │  │  │  └─ Export to ERP
│     │  │  │  │     → END (Perfect Match)
│     │  │  │  │
│     │  │  │  └─ NO FULL MATCH ⚠️
│     │  │  │     │
│     │  │  │     ├─ STEP 2: Check Unit Price Variance
│     │  │  │     │  Card: CONDITION_DOC_TO_PO_UNIT_PRICE
│     │  │  │     │  Tolerance: 5%
│     │  │  │     │  │
│     │  │  │     │  ├─ Calculate for each line:
│     │  │  │     │  │  Variance % = |Invoice-PO|/PO × 100
│     │  │  │     │  │
│     │  │  │     │  ├─ PRICE VARIANCE ≤ 5% ✅
│     │  │  │     │  │  Store variance: 3.2% (example)
│     │  │  │     │  │  Price Check: PASS
│     │  │  │     │  │
│     │  │  │     │  └─ PRICE VARIANCE > 5% ❌
│     │  │  │     │     Store variance: 12.5% (example)
│     │  │  │     │     Price Check: FAIL
│     │  │  │     │     → Flag for review
│     │  │  │     │
│     │  │  │     ├─ STEP 3: Check Quantity Variance
│     │  │  │     │  Card: CONDITION_DOC_TO_PO_QUANTITY
│     │  │  │     │  Tolerance: 10%
│     │  │  │     │  │
│     │  │  │     │  ├─ Calculate for each line:
│     │  │  │     │  │  Variance % = |Inv Qty-PO Qty|/PO Qty × 100
│     │  │  │     │  │
│     │  │  │     │  ├─ QUANTITY VARIANCE ≤ 10% ✅
│     │  │  │     │  │  Store variance: 2.0% (example)
│     │  │  │     │  │  Quantity Check: PASS
│     │  │  │     │  │
│     │  │  │     │  └─ QUANTITY VARIANCE > 10% ❌
│     │  │  │     │     Store variance: 15.0% (example)
│     │  │  │     │     Quantity Check: FAIL
│     │  │  │     │     → Flag for review
│     │  │  │     │
│     │  │  │     ├─ STEP 4: Check Tax Lines
│     │  │  │     │  Card: CONDITION_DOC_TO_PO_TAX_LINES
│     │  │  │     │  │
│     │  │  │     │  ├─ TAX ALIGNED ✅
│     │  │  │     │  │  Tax Check: PASS
│     │  │  │     │  │
│     │  │  │     │  └─ TAX MISMATCH ❌
│     │  │  │     │     Tax Check: FAIL
│     │  │  │     │     → Flag for review
│     │  │  │     │
│     │  │  │     ├─ EVALUATE RESULTS
│     │  │  │     │  │
│     │  │  │     │  ├─ ALL CHECKS PASS ✅
│     │  │  │     │  │  (Within tolerance)
│     │  │  │     │  │  │
│     │  │  │     │  │  ├─ Set Match_Status = "WITHIN TOLERANCE"
│     │  │  │     │  │  ├─ Log variance details
│     │  │  │     │  │  ├─ Auto-Approve
│     │  │  │     │  │  └─ Export to ERP
│     │  │  │     │  │     → END (Approved with Variance)
│     │  │  │     │  │
│     │  │  │     │  ├─ MINOR FAILURES (Variance < 15%) ⚠️
│     │  │  │     │  │  │
│     │  │  │     │  │  ├─ Set Match_Status = "REVIEW REQUIRED"
│     │  │  │     │  │  ├─ Create Review Task
│     │  │  │     │  │  │  - Assign to: AP Officer
│     │  │  │     │  │  │  - Priority: Medium
│     │  │  │     │  │  │  - Deadline: 3 days
│     │  │  │     │  │  ├─ Send email with details
│     │  │  │     │  │  │
│     │  │  │     │  │  └─ WAIT FOR TASK COMPLETION
│     │  │  │     │  │     │
│     │  │  │     │  │     ├─ TASK APPROVED ✅
│     │  │  │     │  │     │  Approve & Export
│     │  │  │     │  │     │  → END (Manual Approval)
│     │  │  │     │  │     │
│     │  │  │     │  │     └─ TASK REJECTED ❌
│     │  │  │     │  │        Reject & Return to Supplier
│     │  │  │     │  │        → END (Rejected)
│     │  │  │     │  │
│     │  │  │     │  └─ MAJOR FAILURES (Variance ≥ 15%) 🚨
│     │  │  │     │     │
│     │  │  │     │     ├─ Set Match_Status = "ESCALATION"
│     │  │  │     │     ├─ Create Urgent Task
│     │  │  │     │     │  - Assign to: Procurement Manager
│     │  │  │     │     │  - Priority: High
│     │  │  │     │     │  - Deadline: 1 day
│     │  │  │     │     ├─ Send urgent emails to:
│     │  │  │     │     │  * Procurement Manager
│     │  │  │     │     │  * Finance Manager
│     │  │  │     │     │  * Supplier
│     │  │  │     │     ├─ Block document processing
│     │  │  │     │     │
│     │  │  │     │     └─ WAIT FOR RESOLUTION
│     │  │  │     │        → END (Pending Escalation)
│     │  │  │     │
│     │  │  │     └─ [Variance checks complete]
│     │  │  │
│     │  │  └─ [Full match check complete]
│     │  │
│     │  └─ PO NOT FOUND ❌
│     │     │
│     │     ├─ Set Match_Status = "PO NOT FOUND"
│     │     ├─ Create Task: "Missing PO"
│     │     │  - Assign to: Procurement Team
│     │     │  - Priority: High
│     │     ├─ Send email to procurement
│     │     └─ Block document
│     │        → END (Missing PO)
│     │
│     └─ [PO retrieval complete]
│
└─ [PO check complete]
```

***

## 配置模板

### 模板 1：标准 PO 匹配（保守）

```json
{
  "full_match_check": true,
  "price_variance": {
    "enabled": true,
    "tolerance_percent": 3,
    "tolerance_type": "percentage"
  },
  "quantity_variance": {
    "enabled": true,
    "tolerance_percent": 5,
    "tolerance_type": "percentage",
    "allow_under_delivery": true,
    "allow_over_delivery": false
  },
  "tax_validation": {
    "enabled": true,
    "match_tax_codes": true,
    "match_tax_rates": true,
    "tax_amount_tolerance": 0.5
  },
  "auto_approve": {
    "full_match": true,
    "within_tolerance": true
  },
  "escalation": {
    "threshold_percent": 10,
    "assign_to": "procurement_manager"
  }
}
```

**适用场景：** 控制严格、对差异容忍度低的环境

***

### 模板 2：灵活 PO 匹配（宽松）

```json
{
  "full_match_check": true,
  "price_variance": {
    "enabled": true,
    "tolerance_percent": 10,
    "tolerance_type": "percentage"
  },
  "quantity_variance": {
    "enabled": true,
    "tolerance_percent": 15,
    "tolerance_type": "percentage",
    "allow_under_delivery": true,
    "allow_over_delivery": true
  },
  "tax_validation": {
    "enabled": true,
    "match_tax_codes": false,
    "match_tax_rates": true,
    "tax_amount_tolerance": 2
  },
  "auto_approve": {
    "full_match": true,
    "within_tolerance": true
  },
  "escalation": {
    "threshold_percent": 20,
    "assign_to": "accounts_payable"
  }
}
```

**适用场景：** 灵活的环境、值得信赖的供应商、较高的容差

***

### 模板 3：仅匹配价格

```json
{
  "full_match_check": false,
  "price_variance": {
    "enabled": true,
    "tolerance_percent": 5,
    "tolerance_type": "percentage"
  },
  "quantity_variance": {
    "enabled": false
  },
  "tax_validation": {
    "enabled": false
  },
  "auto_approve": {
    "full_match": false,
    "within_tolerance": true
  }
}
```

**适用场景：** 仅关注价格且预期会有数量变化时

***

## 高级场景

### 场景 1：处理部分交付

**挑战：** 发票对应 PO 的部分交付

**解决方案：**

```
1. Allow quantity under-delivery within tolerance
2. Track cumulative invoiced quantity vs PO quantity
3. Update PO remaining quantity
4. Create field: "PO_Percentage_Invoiced"
5. When 100% invoiced: Close PO automatically
```

**实施方式：**

```
IF Cumulative_Invoiced_Quantity ≤ PO_Quantity:
  Calculate: Percentage = (Cumulative/PO) × 100
  Store in: PO_Percentage_Invoiced
  IF Percentage ≥ 100:
    Set PO_Status = "FULLY INVOICED"
    Close PO
```

***

### 场景 2：多币种 PO 匹配

**挑战：** 发票币种与 PO 币种不同

**解决方案：**

```
1. Detect currency mismatch
2. Get exchange rate (from API or master data)
3. Convert invoice amount to PO currency
4. Compare converted amounts
5. Store both original and converted amounts
```

**实施方式：**

```
IF Invoice_Currency ≠ PO_Currency:
  1. Get exchange rate for Invoice_Currency → PO_Currency
  2. Convert: Invoice_Amount_Converted = Invoice_Amount × Rate
  3. Compare: Invoice_Amount_Converted vs PO_Amount
  4. Store: Original_Currency_Amount and Converted_Amount
  5. Flag: "Currency_Conversion_Applied"
```

***

### 场景 3：总括 PO / 框架协议

**挑战：** 多张发票对应同一 PO

**解决方案：**

```
1. Identify PO type = "Blanket"
2. Track cumulative invoiced value
3. Check: Cumulative ≤ Blanket PO Total
4. Update remaining PO value after each invoice
5. Alert when approaching PO limit
```

**实施方式：**

```
IF PO_Type = "Blanket":
  Calculate: Total_Invoiced_To_Date
  Check: Total_Invoiced_To_Date + Current_Invoice ≤ PO_Total_Value
  IF Within limit:
    Approve invoice
    Update: Remaining_PO_Value
  ELSE:
    Escalate: "Blanket PO limit exceeded"
```

***

## 错误处理和边缘情况

### 边缘情况 1：发票缺少行项目

**问题：** 发票上有 PO 中不存在的项目

**解决方案：**

```
1. Identify unmatched line items
2. Calculate: Unmatched_Amount
3. IF Unmatched_Amount < €100 (threshold):
     Create review task (minor issue)
   ELSE:
     Escalate immediately (major issue)
4. Store unmatched item details
5. Flag: "Additional_Items_Present"
```

***

### 边缘情况 2：PO 已关闭，但收到发票

**问题：** PO 已关闭，之后才收到发票

**解决方案：**

```
1. Check: PO_Status = "CLOSED"
2. Check: Invoice_Date vs PO_Close_Date
3. IF Invoice within 30 days of close:
     Reopen PO temporarily
     Process invoice
     Close PO again
   ELSE:
     Create task: "Late Invoice for Closed PO"
     Assign to procurement
     Manual decision required
```

***

### 边缘情况 3：单张发票对应多个 PO

**问题：** 发票引用了多个 PO

**解决方案：**

```
1. Parse invoice for multiple PO numbers
2. For each PO:
     Retrieve PO data
     Match respective line items
3. Aggregate match results
4. Overall match = ALL individual POs must match
5. Report on each PO separately
```

***

## 性能提示

✅ **最佳实践：**

* 缓存 PO 数据，以减少查询次数
* 设置合适的容差（既不要太严格，也不要太宽松）
* 优先使用完整匹配检查（速度更快）
* 记录所有差异计算
* 每季度检查容差设置
* 监控自动审批率
* 跟踪常见差异原因

❌ **应避免：**

* 容差为零（过于严格，导致过多人工审核）
* 容差极高（失去控制目的）
* 忽略系统性差异
* 不跟踪差异趋势
* 在必须有 PO 的情况下无 PO 处理

***

## 监控和报告

### 要跟踪的关键指标

1. **匹配率：**
   * 完整匹配：X%
   * 在容差范围内：Y%
   * 超出容差范围：Z%
2. **差异分析：**
   * 平均价格差异
   * 平均数量差异
   * 常见差异原因
3. **处理效率：**
   * 自动审批率
   * 人工审核率
   * 平均审核时间
4. **供应商表现：**
   * 按供应商统计的差异
   * 按供应商统计的匹配率
   * 问题供应商

***

## 测试清单

* [ ] 完全匹配场景（完整匹配）
* [ ] 在容差范围内的场景（轻微差异）
* [ ] 超出容差范围的场景（严重差异）
* [ ] 缺少 PO 的场景
* [ ] PO 编号错误的场景
* [ ] 部分交付场景
* [ ] 超量交付场景
* [ ] 币种不匹配场景
* [ ] 多个 PO 场景
* [ ] PO 已关闭的场景
* [ ] 税项差异场景
* [ ] 升级处理工作流
* [ ] 创建任务
* [ ] 电子邮件通知
* [ ] 字段更新
* [ ] 审批后导出

***

## 相关模式

### 可配合使用的模式：

* [**任务管理模式**](task-management-pattern.md) - 为差异创建审核任务
* [**决策逻辑模式**](decision-logic-pattern.md) - 根据差异级别进行复杂路由
* [**API 集成模式**](api-integration-pattern.md) - 获取当前价格以供比较
* [**数据转换模式**](data-transformation-pattern.md) - 币种转换、单位转换

***

## 相关指南

### 前置条件

* [PO 匹配完整指南](../po-matching-complete-guide.md) - 所有 PO 匹配卡片
* [条件卡片指南](../condition-cards-complete-guide.md) - 条件逻辑
* [字段操作指南](../field-manipulation-guide.md) - 字段操作

### 相关卡片

* **PURCHASE\_ORDER\_FULL\_MATCH** - [PO 匹配指南](../po-matching-complete-guide.md#full-match)
* **CONDITION\_DOC\_TO\_PO\_UNIT\_PRICE** - [PO 匹配指南](../po-matching-complete-guide.md#unit-price)
* **CONDITION\_DOC\_TO\_PO\_QUANTITY** - [PO 匹配指南](../po-matching-complete-guide.md#quantity)
* **CONDITION\_DOC\_TO\_PO\_TAX\_LINES** - [PO 匹配指南](../po-matching-complete-guide.md#tax-lines)
* **tasks\_create** - [任务分配指南](../task-assignment-guide.md)

### 后续步骤

* 创建审核任务：[任务管理模式](task-management-pattern.md)
* 添加电子邮件通知：[发送电子邮件指南](../send-email-groups-guide.md)
* 实施复杂路由：[决策逻辑模式](decision-logic-pattern.md)

***

**模式版本：** 1.0 **最后更新：** 2025 年 10 月 23 日 **难度：** 中高 **预计时间：** 60-90 分钟 **成功率：** 高（正确配置时）
