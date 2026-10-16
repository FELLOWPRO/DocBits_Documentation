# 字段和表格操作卡片

## 字段和表格操作卡片 - 完整指南

**涵盖：** 用于修改文档字段和表格的 9 张卡片

***

本页中的字段和表格卡片位于工作流构建器的 **Then** 组中 — 当 When/And 条件匹配后运行的操作：

<figure><img src="../../../.gitbook/assets/workflow_designer_cards.png" alt="工作流构建器画布，包含 When、And 和 Then 卡片组"><figcaption><p>通过 <strong>Add Card</strong> 将字段和表格操作卡片添加到 <strong>Then</strong> 组。</p></figcaption></figure>

***

### 📌 版本信息

**多版本卡片：** CALC\_COLUMNS (v2)、CALC\_COLUMNS\_REGEX (v2)、EDIT\_COLUMN (v2)、AI\_CALC\_MTZ\_ETZ (v2)

**版本模式：** 所有字段操作卡片都遵循 v1 → v2 模式 **关键更改：** v2 增加了国际化 (i18n) 支持和翻译键

📖 [完整版本历史](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/administration-and-setup/changelog/release.md#-data-manipulation-cards) | [卡片版本数据库](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/DocFlow/docs/card_version.md)

***

## 文档字段操作 <a id="storing-api-data"></a>

### 卡片：ACTION\_SET\_FIELD\_TO\_TEXT / 将字段设为文本值 <a id="set-field"></a>

#### 用途

自动将指定文本填入文档字段

#### 使用场景

* 根据决策填写字段
* 设置默认值
* 填写标准化信息
* 根据条件更新字段

#### 工作原理

```
IF Condition is true
    THEN Set Field "Category" to Value "Premium"
```

#### 示例场景

**场景 1：设置审批类别**

```
Condition: Invoice amount > €10,000
    ↓
Action: Set "Approval_Category" field to "High Value"
    ↓
Result: Document now shows "Approval_Category: High Value"
```

**场景 2：设置供应商类别**

```
Condition: Supplier name contains "ABC"
    ↓
Action: Set "Supplier_Type" field to "Preferred Supplier"
    ↓
Result: Document marked as "Preferred Supplier"
```

**场景 3：设置处理备注**

```
Condition: Document has been rejected
    ↓
Action: Set "Processing_Notes" to "Requires supplier revision"
    ↓
Result: Note appears for next processor
```

#### 参数

**字段名称** 要更新的字段

```
Examples: Category, Type, Status, Comment, Notes
```

**文本值** 要填入字段的内容

```
Examples: "Approved", "Pending Review", "High Priority"
```

#### 配置步骤

1. 选择要填写的字段
2. 输入文本值
3. 设置条件（何时填写）
4. 保存

***

### 卡片：ACTION\_SET\_BOOLEAN\_FIELD / 设置复选框字段

#### 用途

自动选中或取消选中复选框字段

#### 使用场景

* 标记为已处理
* 设置审批标记
* 启用/禁用选项
* 标记为待导出

#### 工作原理

```
IF Condition is true
    THEN Check/Uncheck the "Approved" box
```

#### True = 已选中，False = 未选中

**示例：**

**示例 1：标记为已验证**

```
Condition: PO matches perfectly
    ↓
Action: Check "Verified" checkbox
    ↓
Result: ✅ Verified (checked)
```

**示例 2：标记为需人工审核**

```
Condition: Price variance > 10%
    ↓
Action: Check "Requires_Manual_Review" checkbox
    ↓
Result: ✅ Requires_Manual_Review (marked)
```

**示例 3：取消预填复选框的选中状态**

```
Condition: Supplier is blacklisted
    ↓
Action: Uncheck "Approved_for_Payment" checkbox
    ↓
Result: ☐ Approved_for_Payment (unchecked - blocked)
```

#### 参数

```
Checkbox Field: [Choose field]
Set To: ☑ Checked (✅ True)
   or: ☐ Unchecked (❌ False)
```

***

### 卡片：ACTION\_INVERT\_BOOLEAN\_FIELD / 切换复选框

#### 用途

切换复选框状态（已选中 → 未选中，反之亦然）

#### 使用场景

* 切换审批状态
* 切换处理模式
* 反转先前状态
* 更新布尔标记

#### 工作原理

```
Current state: ✅ (Checked)
    ↓
ACTION_INVERT: Toggle the box
    ↓
New state: ☐ (Unchecked)

OR

Current state: ☐ (Unchecked)
    ↓
ACTION_INVERT: Toggle the box
    ↓
New state: ✅ (Checked)
```

#### 示例

```
Invoice received with "Priority" checked
    ↓
After processing, invert "Priority" checkbox
    ↓
Checkbox now unchecked (no longer priority)
```

***

### 卡片：ACTION\_COPY\_DOCFIELD\_TO\_DOCFIELD / 复制字段值 <a id="copy-field"></a>

#### 用途

将一个字段的值复制到另一个字段

#### 使用场景

* 将供应商信息复制到账单信息
* 在多个字段间复制数据
* 统一数据格式
* 创建值的备份

#### 工作原理

```
Source Field: "Invoice_Supplier"  Value: "ABC Corp"
    ↓
COPY TO
    ↓
Target Field: "Billing_Partner"  Value: "ABC Corp"

Both fields now have same value
```

#### 实际示例

**示例 1：复制交货地址**

```
Source: "Delivery_Address" = "123 Main St, Berlin"
    ↓
Copy to: "Billing_Address"
    ↓
Result: Both fields show "123 Main St, Berlin"
```

**示例 2：复制供应商代码**

```
Source: "Supplier_Code_External" = "SUPP-789"
    ↓
Copy to: "Supplier_Code_Internal"
    ↓
Result: Both codes match, system recognizes supplier
```

**示例 3：复制金额以供验证**

```
Source: "Invoice_Total" = "€5000"
    ↓
Copy to: "Amount_to_Validate"
    ↓
Result: Validation field has correct amount
```

#### 参数

```
Source Field: [Choose field to copy FROM]
Target Field: [Choose field to copy TO]
```

#### 备注

* 原字段保持不变
* 目标字段会被源字段的值覆盖
* 适用于统一数据

***

## 表格操作

### 卡片：EDIT\_COLUMN / 编辑表格列

#### 用途

根据条件更改表格列中的值

#### 使用场景

* 修正行项目中的定价错误
* 更新数量
* 更正商品描述
* 统一值

#### 工作原理

```
Table Column: "Unit_Price"
Original Values: [100, 105, 103]
    ↓
FIND: Values matching condition
REPLACE: With new value
    ↓
Updated Column: [100, 110, 110] (example)
```

#### 示例：修正定价

**场景：价格使用了错误的货币**

```
Table "Line_Items" with column "Price"

Current prices: [100, 100, 100] (in wrong currency)
    ↓
Condition: "If Price column equals 100"
    ↓
Action: Replace with 95 (corrected price)
    ↓
Result: [95, 95, 95] (prices corrected)
```

#### 参数

```
Table: [Choose table]
Column: [Choose column to edit]
Find: [Value to find]
Replace with: [New value]
Condition: [When to apply]
```

#### 常见用途

* 修正单价
* 统一描述
* 更正数量
* 更新 SKU 编号

***

### 卡片：CALC\_COLUMNS / 计算列值

#### 用途

对表格列执行计算并保存结果

#### 使用场景

* 计算行项目总额（数量 × 单价）
* 汇总列
* 计算折扣
* 计算百分比

#### 工作原理

```
Column A (Quantity): 100
Column B (Unit Price): €50
    ↓
CALCULATE: A × B
    ↓
Column C (Line Total): €5000
```

#### 计算类型

**类型 1：简单乘法**

```
Formula: Qty × Unit Price = Line Total

Example:
100 units × €50/unit = €5000

Config:
  Column 1: Quantity
  Operator: ×
  Column 2: Unit Price
  Result Column: Line Total
```

**类型 2：加法**

```
Formula: Base Price + Shipping + Tax = Total

Example:
€5000 + €100 + €950 = €6050

Config:
  Column 1: Base Price
  Operator: +
  Column 2: Shipping
  Operator: +
  Column 3: Tax
  Result Column: Total
```

**类型 3：百分比计算**

```
Formula: Amount × (1 + Tax%) = Total with Tax

Example:
€5000 × 1.19 = €5950

Config:
  Column: Amount
  Operator: × (1 + Tax%)
  Result Column: Amount_with_Tax
```

**类型 4：减法**

```
Formula: Original Price - Discount = Final Price

Example:
€100 - €10 = €90

Config:
  Column 1: Original Price
  Operator: -
  Column 2: Discount
  Result Column: Final Price
```

#### 实际示例

**发票行项目计算：**

```
表：Invoice_Lines

行 1：
  数量：100
  单价：€25.00
  计算：100 × €25.00 = €2500.00（行项目总额）

行 2：
  数量：50
  单价：€40.00
  计算：50 × €40.00 = €2000.00（行项目总额）

行 3：
  数量：200
  单价：€10.00
  计算：200 × €10.00 = €2000.00（行项目总额）

小计：€6500.00（行项目总额之和）
税费（19%）：€1235.00
运费：€100.00
总计：€7835.00
```

#### 参数

```
Table: [Select table]
Column 1: [First column]
Operator: [×, +, -, ÷, %]
Column 2: [Second column] (if needed)
Result Column: [Where to put answer]
```

***

### 卡片：CALC\_COLUMNS\_REGEX / 使用正则表达式模式计算

#### 用途

根据模式匹配计算列值

#### 使用场景

* 使用模式从文本中提取值
* 根据规则设置数据格式
* 根据模式转换值
* 解析结构化文本

#### 工作原理

**正则表达式模式匹配：**

```
Original Value: "ABC-12345-XYZ"
Pattern: Extract numbers only
Calculation: Convert to "12345"
Result: "12345"
```

#### 示例：提取供应商代码

**场景：商品编号中包含供应商信息**

```
表字段：“Article_Code”
值：["SUPP001-2025-A", "SUPP002-2025-B"]

模式：提取供应商代码（前 7 个字符）
    ↓
计算：SUPP001、SUPP002
    ↓
存入：“Supplier_Code”字段

结果：
Article_Code: SUPP001-2025-A  →  Supplier_Code: SUPP001
Article_Code: SUPP002-2025-B  →  Supplier_Code: SUPP002
```

#### 示例：设置电话号码格式

**场景：电话号码未格式化**

```
Original: "491234567890"
Pattern: Format as: +49 123 4567 890
Result: "+49 123 4567 890"
```

#### 示例：从文本中提取价格

**场景：价格采用文本格式**

```
Original: "Price is 99.99 EUR"
Pattern: Extract number only
Result: "99.99"
```

#### 参数

```
Table: [Select table]
Column: [Column to analyze]
Regex Pattern: [Pattern to find]
Replacement: [What to replace with]
Result Column: [Where to store result]
```

#### 常见正则表达式模式

```
Numbers only: [0-9]+
Letters only: [a-zA-Z]+
First word: ^\w+
Extract €: €(\d+\.\d{2})
Date format: \d{4}-\d{2}-\d{2}
```

***

## 计算示例

### 示例 1：发票总额计算

```
Step 1: Calculate line totals
  Each row: Qty × Unit Price

Step 2: Sum all line totals
  Sum: €2500 + €2000 + €2000 = €6500

Step 3: Calculate tax
  Tax: €6500 × 0.19 = €1235

Step 4: Add shipping
  Final: €6500 + €1235 + €100 = €7835
```

### 示例 2：差异计算

```
PO Price: €100
Invoice Price: €103

Variance = |(Invoice - PO)| / PO × 100
Variance = |3| / 100 × 100 = 3%

Store in "Price_Variance%" column
```

### 示例 3：应用折扣

```
Original Price: €100
Discount %: 10%
Discount Amount: €100 × 0.10 = €10
Final Price: €100 - €10 = €90
```

***

## 字段操作工作流示例

```
文档到达
    ↓
检查条件：“Amount > €5000?”
    ↓
是 → 将字段“Category”设为“High Value”（高价值）
    ↓
检查条件：“Supplier is preferred?”（供应商是否为首选？）
    ↓
是 → 勾选“FastTrack”复选框
    ↓
将“Delivery_Address”复制到“Invoice_Address”
    ↓
在表中：计算行项目总额（Qty × Price）
    ↓
在表中：计算含税总额
    ↓
文档现在已填充所有计算所得字段和其他字段
```

***

## 最佳实践

✅ **建议：**

* 保持公式简单
* 使用示例数据测试计算
* 确认结果合理
* 记录更改字段的原因
* 数据相同时使用复制字段卡片

❌ **避免：**

* 创建循环引用（A=B，B=A）
* 无故覆盖重要数据
* 编写过于复杂的正则表达式模式
* 忘记核实计算结果
* 在错误的表格或列上执行计算

***

## 故障排除

### “字段未更新”

**原因：** 条件未满足或卡片未触发

**解决方案：**

* 检查条件是否为真
* 确认卡片已添加到工作流
* 使用示例数据进行测试
* 检查字段名称是否有拼写错误

### “计算结果错误”

**原因：** 选择了错误的列或公式不正确

**解决方案：**

* 核实源列
* 检查公式是否正确
* 手动测试
* 检查小数位数和舍入方式

### “表格显示错误”

**原因：** 引用的列不存在

**解决方案：**

* 核实列名拼写
* 检查列中是否有数据
* 确保列数据类型与计算匹配
* 如有需要，添加缺失的列

***

## 相关卡片

* **ACTION\_COPY\_DOCFIELD\_TO\_DOCFIELD** - 复制值
* **EDIT\_COLUMN** - 更改表格值
* **CALC\_COLUMNS** - 计算公式
* **ACTION\_SET\_FIELD\_TO\_TEXT** - 设置文本值
* **ACTION\_SET\_BOOLEAN\_FIELD** - 选中复选框
