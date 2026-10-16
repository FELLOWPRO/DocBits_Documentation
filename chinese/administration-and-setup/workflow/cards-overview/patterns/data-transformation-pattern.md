# 数据转换模式

**模式类型：** 数据处理与操作 **复杂度：** 中等 **预计设置时间：** 30-45 分钟 **常见使用场景：** 字段计算、数据格式化、货币换算、单位换算、数据丰富

***

在 **Workflow Builder**（Workflow Dashboard → Workflow List → Add Workflow）中构建此模式。点击 **Add Card**，打开 **Document Field** 类别——此类别包含该模式串联使用的读取、写入、计算和格式化卡片：

<figure><img src="../../../../.gitbook/assets/workflow_add_card_picker.png" alt="Workflow Builder 中按类别分组的 Add Card 卡片库"><figcaption><p><strong>Add Card</strong> 卡片库——字段读取/写入、计算和格式化卡片位于 <strong>Document Field</strong> 类别下。</p></figcaption></figure>

***

## 模式概述

此模式演示如何在 DocBits 工作流中转换、计算、格式化和丰富文档数据。数据转换对于准备导出数据、执行计算、统一格式以及使用其他信息丰富文档至关重要。

**此模式的作用：**

1. 从文档字段中提取数据
2. 执行计算和转换
3. 将数据格式化为所需标准
4. 在单位、货币和日期之间进行转换
5. 使用派生数据或查找数据丰富文档
6. 验证并清理数据

***

## 何时使用此模式

在需要以下操作时使用此模式：

* ✅ 计算总额、小计和税额
* ✅ 换算货币或单位
* ✅ 格式化日期、数字和文本
* ✅ 根据现有字段派生值
* ✅ 从外部来源丰富数据
* ✅ 统一数据格式
* ✅ 清理并验证数据
* ✅ 准备导出数据

**以下情况不要使用此模式：**

* ❌ 不需要转换
* ❌ 数据格式已经正确
* ❌ 简单复制字段即可满足需求

***

## 数据转换类型

### 1. 计算

**数学运算：**

```
- Addition: Quantity + Bonus_Quantity = Total_Quantity
- Subtraction: Invoice_Total - Tax_Amount = Net_Amount
- Multiplication: Quantity × Unit_Price = Line_Total
- Division: Total_Amount / Quantity = Unit_Price
- Percentage: (Discount / Subtotal) × 100 = Discount_Percent
```

### 2. 字符串操作

**文本操作：**

```
- Concatenation: First_Name + " " + Last_Name = Full_Name
- Uppercase: "invoice" → "INVOICE"
- Lowercase: "SUPPLIER" → "supplier"
- Substring: "INV-2025-001" → "2025" (extract year)
- Replace: "01/23/2025" → "2025-01-23"
- Trim: "  ABC Corp  " → "ABC Corp"
```

### 3. 数据类型转换

**类型转换：**

```
- String to Number: "123.45" → 123.45
- Number to String: 123.45 → "123.45"
- Date to String: 2025-10-23 → "October 23, 2025"
- String to Date: "23.10.2025" → 2025-10-23
- Boolean to String: true → "Yes"
```

### 4. 单位换算

**度量单位换算：**

```
- Weight: kg → lbs, tons → kg
- Length: cm → inches, m → ft
- Volume: liters → gallons
- Temperature: Celsius → Fahrenheit
- Quantity: pieces → dozens, units → pallets
```

### 5. 货币换算

**应用汇率：**

```
- USD → EUR: Amount_USD × Rate = Amount_EUR
- Multi-currency: Convert all to base currency
- Historical rates: Use rate from invoice date
```

### 6. 日期转换

**日期操作：**

```
- Format change: 10/23/2025 → 2025-10-23
- Add days: Invoice_Date + 30 = Due_Date
- Calculate age: Today - Invoice_Date = Age_Days
- Extract parts: "2025-10-23" → Year: 2025, Month: 10, Day: 23
```

***

## 完整工作流示例

### 场景：计算发票总额并丰富数据

**业务需求：**

* 从发票中提取行项目
* 计算行项目总额（数量 × 价格）
* 计算小计（行项目总额之和）
* 计算税额（小计 × 税率）
* 计算总计（小计 + 税额）
* 如果发票使用其他货币，则换算为 EUR
* 将金额格式化为 2 位小数
* 根据产品类别添加公司 GL 科目
* 根据发票总额验证计算结果
* 如果差异 > 1%，则标记

**使用的工作流卡片：**

1. ACTION\_CALCULATE\_FIELD - 执行计算
2. ACTION\_SET\_FIELD\_TO\_TEXT - 存储结果
3. ACTION\_COPY\_FIELD\_VALUE - 复制值
4. CALL\_API - 获取汇率（如有需要）
5. CONDITION\_COMPARE\_TWO\_DOCFIELD\_VALUES - 验证计算结果
6. ACTION\_SET\_FIELD\_FROM\_MASTER\_DATA - 使用 GL 科目丰富数据

***

## 分步实施

### 步骤 1：行项目计算

**计算行项目总额：**

**卡片：** ACTION\_CALCULATE\_FIELD

**针对每个行项目：**

```
Field: Line_Total
Formula: {{TABLE_FIELD:Quantity}} * {{TABLE_FIELD:Unit_Price}}
Result Type: Number
Decimal Places: 2
```

**示例：**

```
Line 1:
  Quantity: 100
  Unit Price: €50.00
  Calculation: 100 × 50.00 = €5,000.00
  Store in: Line_Total

Line 2:
  Quantity: 50
  Unit Price: €20.00
  Calculation: 50 × 20.00 = €1,000.00
  Store in: Line_Total

Line 3:
  Quantity: 25
  Unit Price: €15.50
  Calculation: 25 × 15.50 = €387.50
  Store in: Line_Total
```

**指南参考：** [字段操作指南 - 计算](../field-manipulation-guide.md)

***

### 步骤 2：计算文档小计

**汇总所有行项目总额：**

**卡片：** ACTION\_CALCULATE\_FIELD

**配置：**

```
Field: Calculated_Subtotal
Formula: SUM({{TABLE_COLUMN:Line_Total}})
Result Type: Number
Decimal Places: 2
```

**示例：**

```
Line 1 Total: €5,000.00
Line 2 Total: €1,000.00
Line 3 Total: €387.50

Subtotal = 5000 + 1000 + 387.50 = €6,387.50
Store in: Calculated_Subtotal
```

***

### 步骤 3：计算税额

**将税率应用于小计：**

**卡片：** ACTION\_CALCULATE\_FIELD

**配置：**

```
Field: Calculated_Tax_Amount
Formula: {{Calculated_Subtotal}} * ({{Tax_Rate}} / 100)
Result Type: Number
Decimal Places: 2
```

**示例：**

```
Calculated_Subtotal: €6,387.50
Tax_Rate: 19% (VAT)

Tax Amount = 6387.50 × (19 / 100)
          = 6387.50 × 0.19
          = €1,213.63

Store in: Calculated_Tax_Amount
```

***

### 步骤 4：计算总计

**将小计和税额相加：**

**卡片：** ACTION\_CALCULATE\_FIELD

**配置：**

```
Field: Calculated_Grand_Total
Formula: {{Calculated_Subtotal}} + {{Calculated_Tax_Amount}}
Result Type: Number
Decimal Places: 2
```

**示例：**

```
Calculated_Subtotal: €6,387.50
Calculated_Tax_Amount: €1,213.63

Grand Total = 6387.50 + 1213.63 = €7,601.13

Store in: Calculated_Grand_Total
```

***

### 步骤 5：货币换算（如有需要）

**检查是否需要换算：**

**卡片：** CONDITION\_DOC\_FIELD\_IS

**配置：**

```
Field: Invoice_Currency
Operator: IS NOT EQUAL TO
Value: EUR
```

**如果需要换算：**

**步骤 5a：获取汇率**

**卡片：** CALL\_API

**配置：**

```
Endpoint: https://api.exchangerate-api.com/v4/latest/{{Invoice_Currency}}
Method: GET
Response Path: rates.EUR
Store in: Exchange_Rate_To_EUR
```

**示例：**

```
Invoice Currency: USD
API Response: {
  "base": "USD",
  "rates": {
    "EUR": 0.92
  }
}

Exchange_Rate_To_EUR = 0.92
```

**步骤 5b：换算金额**

**卡片：** ACTION\_CALCULATE\_FIELD

**配置：**

```
Field: Grand_Total_EUR
Formula: {{Calculated_Grand_Total}} * {{Exchange_Rate_To_EUR}}
Result Type: Number
Decimal Places: 2
```

**示例：**

```
Grand Total (USD): $7,601.13
Exchange Rate: 0.92

Grand Total (EUR) = 7601.13 × 0.92 = €6,993.04

Store in: Grand_Total_EUR
```

**指南参考：** [API 集成模式 - 货币换算](api-integration-pattern.md#currency-conversion-example)

***

### 步骤 6：数据丰富 - 添加 GL 科目

**根据产品类别查找 GL 科目：**

**卡片：** ACTION\_SET\_FIELD\_FROM\_MASTER\_DATA

**配置：**

```
Lookup Table: GL_Account_Mapping
Lookup Key: {{TABLE_FIELD:Product_Category}}
Return Field: GL_Account_Number
Store in: GL_Account
```

**示例：**

```
Line 1:
  Product Category: "Office Supplies"
  Lookup → GL_Account_Mapping table
  Result: GL Account "4200-100" (Office Expense)

Line 2:
  Product Category: "IT Equipment"
  Lookup → GL_Account_Mapping table
  Result: GL Account "6100-200" (IT Assets)

Line 3:
  Product Category: "Services"
  Lookup → GL_Account_Mapping table
  Result: GL Account "5000-300" (Services Expense)
```

**指南参考：** [字段操作指南 - 主数据](../field-manipulation-guide.md)

***

### 步骤 7：验证计算结果

**将计算出的总计与发票总额进行比较：**

**卡片：** CONDITION\_COMPARE\_TWO\_DOCFIELD\_VALUES

**配置：**

```
Field 1: Calculated_Grand_Total
Field 2: Invoice_Total (from OCR)
Operator: Calculate Variance Percentage
Tolerance: 1%
```

**计算方式：**

```
Variance % = |Calculated - Invoice| / Invoice × 100

Example:
  Calculated Total: €7,601.13
  Invoice Total: €7,600.00

  Variance = |7601.13 - 7600.00| / 7600.00 × 100
          = 1.13 / 7600.00 × 100
          = 0.015%

  Is 0.015% ≤ 1% tolerance? YES ✅
  Result: PASS (calculations match invoice)
```

**逻辑：**

```
IF Variance ≤ 1%:
  Set Validation_Status = "PASS"
  Continue processing
ELSE:
  Set Validation_Status = "FAIL"
  Create review task
  Flag for manual verification
```

**指南参考：** [条件卡片指南 - 字段比较](../condition-cards-complete-guide.md)

***

### 步骤 8：格式化导出数据

**统一格式：**

**卡片：** ACTION\_SET\_FIELD\_TO\_TEXT

**日期格式化：**

```
Field: Invoice_Date_Formatted
Value: FORMATDATE({{Invoice_Date}}, "YYYY-MM-DD")
Example: 10/23/2025 → 2025-10-23
```

**数字格式化：**

```
Field: Amount_Formatted
Value: FORMATNUMBER({{Grand_Total_EUR}}, 2, ",", ".")
Example: 7601.13 → 7.601,13 (German format)
```

**文本格式化：**

```
Field: Supplier_Name_Upper
Value: UPPERCASE({{Supplier_Name}})
Example: "ABC Corporation" → "ABC CORPORATION"
```

***

## 高级转换

### 转换 1：多级税额计算

**场景：** 每个行项目适用不同税率

```
Line 1: Product A (Tax Rate 19%)
Line 2: Product B (Tax Rate 7% - reduced)
Line 3: Product C (Tax Rate 0% - exempt)

Calculation:
  Line 1 Tax = €5,000.00 × 0.19 = €950.00
  Line 2 Tax = €1,000.00 × 0.07 = €70.00
  Line 3 Tax = €387.50 × 0.00 = €0.00

  Total Tax = €950.00 + €70.00 + €0.00 = €1,020.00
```

**实施方式：**

```
For each line:
  1. Get product tax category
  2. Lookup applicable tax rate
  3. Calculate: Line_Net × Tax_Rate = Line_Tax
  4. Sum all Line_Tax values = Total_Tax
```

***

### 转换 2：折扣计算

**场景：** 应用批量折扣和提前付款折扣

```
Original Subtotal: €10,000.00

Step 1: Volume Discount (10% for orders > €5,000)
  Discount = €10,000.00 × 0.10 = €1,000.00
  After Volume Discount = €10,000.00 - €1,000.00 = €9,000.00

Step 2: Early Payment Discount (2% if paid within 10 days)
  Discount = €9,000.00 × 0.02 = €180.00
  After Payment Discount = €9,000.00 - €180.00 = €8,820.00

Step 3: Calculate Tax (on discounted amount)
  Tax = €8,820.00 × 0.19 = €1,675.80

Final Total = €8,820.00 + €1,675.80 = €10,495.80
```

**实施方式：**

```
1. Check order value for volume discount eligibility
2. Calculate volume discount
3. Apply volume discount to subtotal
4. Check payment terms for early payment discount
5. Calculate early payment discount
6. Apply early payment discount
7. Calculate tax on final discounted amount
8. Calculate grand total
```

***

### 转换 3：计量单位换算

**场景：** 将发票计量单位换算为标准计量单位

```
Invoice shows:
  Product: Steel Rods
  Quantity: 50
  Unit: Meters
  Unit Price: €10.00/meter
  Line Total: €500.00

Company standard UOM: Feet

Conversion:
  1 meter = 3.28084 feet

  Quantity (feet) = 50 meters × 3.28084 = 164.042 feet
  Unit Price (feet) = €10.00/meter ÷ 3.28084 = €3.05/foot

  Verification: 164.042 feet × €3.05/foot ≈ €500.00 ✅
```

**实施方式：**

```
1. Identify invoice UOM
2. Get conversion factor to standard UOM
3. Convert quantity
4. Convert unit price
5. Verify line total remains same
6. Store both original and converted values
```

***

### 转换 4：日期计算

**场景：** 计算付款条件和到期日

```
Invoice Date: 2025-10-23
Payment Terms: NET30

Calculations:
  Due Date = Invoice Date + 30 days = 2025-11-22

  Early Payment Discount Available If:
    Payment Date ≤ Invoice Date + 10 days
    Discount End Date = 2025-11-02

  Days Until Due = Due Date - Today
    If Today = 2025-10-23: Days = 30
    If Today = 2025-11-15: Days = 7
    If Today = 2025-11-23: Days = -1 (overdue)
```

**实施方式：**

```
1. Extract Invoice_Date
2. Extract Payment_Terms (e.g., "NET30", "NET60", "2/10 NET30")
3. Parse payment terms
4. Calculate Due_Date
5. Calculate Discount_End_Date (if applicable)
6. Calculate Days_Until_Due
7. Set Status: "Current", "Due Soon", "Overdue"
```

***

### 转换 5：文本解析与提取

**场景：** 从非结构化文本中提取结构化数据

```
Original Field: "PO-2025-ABC-12345-REV2"

Extract:
  Year: "2025"
  Department: "ABC"
  PO Number: "12345"
  Revision: "2"

Method:
  Split by delimiter "-"
  Array: ["PO", "2025", "ABC", "12345", "REV2"]

  Extract:
    Year = Array[1] = "2025"
    Department = Array[2] = "ABC"
    PO_Number = Array[3] = "12345"
    Revision = Extract digits from Array[4] = "2"
```

***

## 完整转换工作流图

```
INVOICE DATA EXTRACTED
│
├─ STEP 1: LINE ITEM CALCULATIONS
│  For each line:
│    Quantity × Unit_Price = Line_Total
│  Result: Line totals calculated
│
├─ STEP 2: SUBTOTAL CALCULATION
│  SUM(All Line_Totals) = Subtotal
│  Result: €6,387.50
│
├─ STEP 3: TAX CALCULATION
│  Subtotal × Tax_Rate = Tax_Amount
│  €6,387.50 × 19% = €1,213.63
│
├─ STEP 4: GRAND TOTAL CALCULATION
│  Subtotal + Tax_Amount = Grand_Total
│  €6,387.50 + €1,213.63 = €7,601.13
│
├─ STEP 5: CURRENCY CHECK
│  │
│  ├─ Currency = EUR? YES
│  │  → Skip conversion
│  │  → Use Grand_Total as is
│  │
│  └─ Currency ≠ EUR? NO (e.g., USD)
│     │
│     ├─ Call Exchange Rate API
│     │  Get: USD → EUR rate (0.92)
│     │
│     ├─ Convert Amount
│     │  $7,601.13 × 0.92 = €6,993.04
│     │
│     └─ Store converted amount
│        Grand_Total_EUR = €6,993.04
│
├─ STEP 6: DATA ENRICHMENT
│  For each line:
│    Lookup Product_Category → GL_Account
│    Store GL_Account in line item
│  Result: All lines have GL accounts
│
├─ STEP 7: VALIDATION
│  │
│  ├─ Compare Calculated vs Invoice Total
│  │  Variance = |Calculated - Invoice| / Invoice × 100
│  │
│  ├─ Variance ≤ 1%? ✅
│  │  Set Validation_Status = "PASS"
│  │  Continue processing
│  │
│  └─ Variance > 1%? ❌
│     Set Validation_Status = "FAIL"
│     Create review task
│     Flag for manual check
│
├─ STEP 8: FORMATTING
│  │
│  ├─ Format Dates
│  │  10/23/2025 → 2025-10-23
│  │
│  ├─ Format Numbers
│  │  7601.13 → 7.601,13 (locale-specific)
│  │
│  ├─ Format Text
│  │  "abc corp" → "ABC CORP"
│  │
│  └─ Format for Export
│     All fields in ERP-compatible format
│
└─ TRANSFORMATION COMPLETE
   Document ready for next workflow step
```

***

## 配置模板

### 模板 1：标准发票计算

```json
{
  "transformations": [
    {
      "step": 1,
      "name": "Calculate Line Totals",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "{{Quantity}} * {{Unit_Price}}",
      "result_field": "Line_Total"
    },
    {
      "step": 2,
      "name": "Calculate Subtotal",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "SUM({{Line_Total}})",
      "result_field": "Calculated_Subtotal"
    },
    {
      "step": 3,
      "name": "Calculate Tax",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "{{Calculated_Subtotal}} * {{Tax_Rate}} / 100",
      "result_field": "Calculated_Tax"
    },
    {
      "step": 4,
      "name": "Calculate Total",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "{{Calculated_Subtotal}} + {{Calculated_Tax}}",
      "result_field": "Calculated_Total"
    }
  ]
}
```

***

### 模板 2：货币换算工作流

```json
{
  "currency_conversion": {
    "check_needed": {
      "card": "CONDITION_DOC_FIELD_IS",
      "field": "Invoice_Currency",
      "operator": "NOT EQUAL TO",
      "value": "EUR"
    },
    "get_rate": {
      "card": "CALL_API",
      "endpoint": "https://api.exchangerate.com/v1/rates/{{Invoice_Currency}}",
      "method": "GET",
      "response_path": "rates.EUR"
    },
    "convert": {
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "{{Amount}} * {{Exchange_Rate}}",
      "result_field": "Amount_EUR"
    },
    "store_details": {
      "original_currency": "{{Invoice_Currency}}",
      "original_amount": "{{Amount}}",
      "exchange_rate": "{{Exchange_Rate}}",
      "converted_amount": "{{Amount_EUR}}",
      "conversion_date": "{{Today}}"
    }
  }
}
```

***

## 错误处理

### 常见转换错误

**错误 1：除以零**

```
Problem: Unit_Price = Total / Quantity, but Quantity = 0

Solution:
  IF Quantity = 0 OR Quantity IS NULL:
    Set Unit_Price = 0
    Flag for review
  ELSE:
    Calculate normally
```

**错误 2：数字格式无效**

```
Problem: Field contains "€1,234.56" but need number 1234.56

Solution:
  1. Remove currency symbols
  2. Remove thousand separators
  3. Convert decimal separator if needed
  4. Parse to number
  5. Validate result
```

**错误 3：日期解析失败**

```
Problem: Date in unexpected format

Solution:
  1. Try multiple date formats
  2. If all fail: Set to null
  3. Flag for manual review
  4. Log original value
```

**错误 4：缺少换算系数**

```
Problem: Unknown UOM conversion

Solution:
  1. Check conversion table
  2. If not found: Skip conversion
  3. Flag for admin to add conversion
  4. Use original values
```

***

## 测试清单

* [ ] 所有计算都能得出正确结果
* [ ] 保持小数精度
* [ ] 货币换算准确
* [ ] 日期计算正确
* [ ] 文本转换正常
* [ ] 正确处理空值/空字段
* [ ] 避免除以零
* [ ] 验证数字格式
* [ ] 正确应用舍入规则
* [ ] 所有转换后的字段均已填充
* [ ] 验证能够发现错误
* [ ] 导出格式正确

***

## 相关模式

### 适合配合使用的模式：

* [**API 集成模式**](api-integration-pattern.md) - 获取汇率和丰富数据
* [**PO 匹配模式**](po-matching-pattern.md) - 差异计算
* [**决策逻辑模式**](decision-logic-pattern.md) - 根据计算值进行路由
* [**任务管理模式**](task-management-pattern.md) - 为验证失败创建任务

***

## 相关指南

### 前置条件

* [字段操作指南](../field-manipulation-guide.md) - 所有字段操作
* [条件卡片指南](../condition-cards-complete-guide.md) - 验证条件
* [Call API 指南](../call-api-guide.md) - 获取外部数据

### 相关卡片

* **ACTION\_CALCULATE\_FIELD** - [字段操作指南](../field-manipulation-guide.md)
* **ACTION\_SET\_FIELD\_TO\_TEXT** - [字段操作指南](../field-manipulation-guide.md#set-field)
* **ACTION\_COPY\_FIELD\_VALUE** - [字段操作指南](../field-manipulation-guide.md#copy-field)
* **CALL\_API** - [Call API 指南](../call-api-guide.md)
* **CONDITION\_COMPARE\_TWO\_DOCFIELD\_VALUES** - [条件卡片指南](../condition-cards-complete-guide.md)

### 后续步骤

* 验证结果：[决策逻辑模式](decision-logic-pattern.md)
* 为错误创建任务：[任务管理模式](task-management-pattern.md)
* 用于 PO 匹配：[PO 匹配模式](po-matching-pattern.md)

***

**模式版本：** 1.0 **最后更新：** October 23, 2025 **难度：** 中等 **预计时间：** 30-45 分钟 **成功率：** 高
