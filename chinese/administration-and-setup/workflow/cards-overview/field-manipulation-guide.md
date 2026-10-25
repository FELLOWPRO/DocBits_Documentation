# 字段和表格操作卡

## 字段和表格操作卡 - 完整指南

**涵盖：** 9张用于修改文档字段和表格的卡片

***

此页面上的字段和表格卡位于工作流程生成器的 **则** 组中 — 一旦“何时/与”条件匹配，就会运行的操作：

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-zh.png" alt="包含“当”“且”和“则”卡片的未保存示例。执行前请配置所有占位字段。 此版本界面的部分标签尚未翻译或翻译不准确。本页说明使用正确术语；图片保留了实际界面。"><figcaption><p>包含“当”“且”和“则”卡片的未保存示例。执行前请配置所有占位字段。 此版本界面的部分标签尚未翻译或翻译不准确。本页说明使用正确术语；图片保留了实际界面。</p></figcaption></figure>

***

### 📌 版本信息

**多版本卡：** CALC\_COLUMNS (v2)、CALC\_COLUMNS\_REGEX (v2)、EDIT\_COLUMN (v2)、AI\_CALC\_MTZ\_ETZ (v2)

**版本提示：**请以实际卡片的版本徽章为准。本文的字段复制示例使用 v2；不同卡片的输入项和行为应分别核对。

📖 [完整版本历史](../release.md) | [卡牌版本和行为](card-versions-guide.md)

***

## 文档字段操作

### 卡：ACTION\_SET\_FIELD\_TO\_TEXT / 将字段设置为文本值

#### 目的

自动用特定文本填充文档字段

#### 何时使用

* 根据决策填充字段
* 设置默认值
* 填写标准化信息
* 根据条件更新字段

#### 它是如何运作的

```
IF Condition is true
    THEN Set Field "Category" to Value "Premium"
```

#### 示例场景

**场景一：设置审批类别**

```
Condition: Invoice amount > €10,000
    ↓
Action: Set "Approval_Category" field to "High Value"
    ↓
Result: Document now shows "Approval_Category: High Value"
```

**场景2：设置供应商类别**

```
Condition: Supplier name contains "ABC"
    ↓
Action: Set "Supplier_Type" field to "Preferred Supplier"
    ↓
Result: Document marked as "Preferred Supplier"
```

**场景3：设置加工备注**

```
Condition: Document has been rejected
    ↓
Action: Set "Processing_Notes" to "Requires supplier revision"
    ↓
Result: Note appears for next processor
```

#### 参数

**字段名称**要更新哪个字段

```
Examples: Category, Type, Status, Comment, Notes
```

**文本值**字段中应放置的内容

```
Examples: "Approved", "Pending Review", "High Priority"
```

#### 配置步骤

1. 选择要填写的字段
2. 输入文本值
3. 设置条件（何时填写）
4. 保存

***

### 卡：ACTION\_SET\_BOOLEAN\_FIELD / 设置复选框字段

#### 目的

自动选中或取消选中复选框字段

#### 何时使用

* 标记为已处理
* 设置批准标志
* 启用/禁用选项
* 导出标记

#### 它是如何运作的

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

**示例 2：手动审核标记**

```
Condition: Price variance > 10%
    ↓
Action: Check "Requires_Manual_Review" checkbox
    ↓
Result: ✅ Requires_Manual_Review (marked)
```

**示例3：取消勾选预填充框**

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

### 卡：ACTION\_INVERT\_BOOLEAN\_FIELD / 切换复选框

#### 目的

翻转复选框状态（选中 → 未选中，反之亦然）

#### 何时使用

* 切换批准状态
* 切换处理模式
* 反转之前的状态
* 更新布尔标志

#### 它是如何运作的

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

### 卡：ACTION\_COPY\_DOCFIELD\_TO\_DOCFIELD / 复制字段值

#### 用途与适用场景

当后续处理需要在另一个文本字段中使用同一个发票号码时，可用此卡片复制字段值。目标字段的原值会被覆盖；请先检查源字段、目标字段及其类型。复制操作本身不会规范化数据格式。

#### 在哪里配置

标准工作流设计器 → **然后…** → **文档字段** → 复制字段值卡片。本示例使用实际界面中的 **v2**。

#### 示例：把发票号码复制到附加字段

两个字段均为文本字段：

| 配置 | 本例中的值 |
| --- | --- |
| 源字段 | `invoice_id` — 发票号码 |
| 目标字段 | `custom_field_1` — 自定义字段 1 |
| 源值 | `WF-INV-1001` |
| 目标字段原值 | `ALT` |

在卡片中先选择“发票号码”，再选择“自定义字段 1”。请确认这两个标记的顺序；反向配置会覆盖另一个字段。

#### 预期结果与检查

| 情况 | 预期结果 |
| --- | --- |
| 源字段存在，文档服务接受修改 | 目标值变为 `WF-INV-1001`，结果为 `SUCCESS`。源字段保持原值。 |
| 文档中缺少源字段 | 返回 `NOT_FOUND_IN_DOCUMENT`；检查源字段名称和文档数据。 |
| 文档服务拒绝修改或请求超时 | 返回 `ERROR`；不要把这次复制视为成功。 |

运行后检查目标字段的实际值及工作流日志。下方影片中的结果图是同一示例的预期结果说明。

#### 管理员视频：复制字段值 <a href="#copy-field-admin-video" id="copy-field-admin-video"></a>

**34 秒 · 中文。** 陈伟说明何时使用此卡片，在真实中文界面中配置两个字段，并解释成功、缺少源字段和修改被拒绝时应检查什么。

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-copy-field-admin/v1/zh.mp4" %}

[打开带中文字幕的视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-copy-field-admin/v1/zh.html) · [阅读文字稿](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-copy-field-admin/v1/zh.txt)

***

## 表操作

### 卡：EDIT\_COLUMN / 编辑表格列

#### 目的

根据条件更改表列中的值

#### 何时使用

* 修复订单项中的定价错误
* 更新数量
* 正确的物品描述
* 标准化字段值

#### 它是如何运作的

```
Table Column: "Unit_Price"
Original Values: [100, 105, 103]
    ↓
FIND: Values matching condition
REPLACE: With new value
    ↓
Updated Column: [100, 110, 110] (example)
```

#### 示例：固定定价

**场景：货币价格错误**

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

* 固定单价
* 标准化描述
* 正确的数量
* 更新 SKU 编号

***

### 卡：CALC\_COLUMNS / 计算列值

#### 目的

对表列执行计算并存储结果

#### 何时使用

* 计算行总计（数量 × 单价）
* 总和列
* 计算折扣
* 计算百分比

#### 它是如何运作的

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

**类型3：百分比计算**

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

#### 现实世界的例子

**发票行项目计算：**

```
Table: Invoice_Lines

Row 1:
  Quantity: 100
  Unit Price: €25.00
  Calculate: 100 × €25.00 = €2500.00 (Line Total)

Row 2:
  Quantity: 50
  Unit Price: €40.00
  Calculate: 50 × €40.00 = €2000.00 (Line Total)

Row 3:
  Quantity: 200
  Unit Price: €10.00
  Calculate: 200 × €10.00 = €2000.00 (Line Total)

Subtotal: €6500.00 (sum of line totals)
Tax (19%): €1235.00
Shipping: €100.00
TOTAL: €7835.00
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

### 卡：CALC\_COLUMNS\_REGEX / 使用正则表达式模式计算

#### 目的

根据模式匹配计算列值

#### 何时使用

* 使用模式从文本中提取值
* 根据规则格式化数据
* 根据模式转换值
* 解析结构化文本

#### 它是如何运作的

**正则表达式模式匹配：**

```
Original Value: "ABC-12345-XYZ"
Pattern: Extract numbers only
Calculation: Convert to "12345"
Result: "12345"
```

#### 示例：提取供应商代码

**场景：商品编号包含供应商信息**

```
Table Column: "Article_Code"
Values: ["SUPP001-2025-A", "SUPP002-2025-B"]

Pattern: Extract supplier code (first 7 characters)
    ↓
Calculate: SUPP001, SUPP002
    ↓
Store in: "Supplier_Code" column

Result:
Article_Code: SUPP001-2025-A  →  Supplier_Code: SUPP001
Article_Code: SUPP002-2025-B  →  Supplier_Code: SUPP002
```

#### 示例：设置电话号码格式

**场景：未格式化的电话号码**

```
Original: "491234567890"
Pattern: Format as: +49 123 4567 890
Result: "+49 123 4567 890"
```

#### 示例：从文本中提取价格

**场景：文本格式价格**

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

#### 常见的正则表达式模式

```
Numbers only: [0-9]+
Letters only: [a-zA-Z]+
First word: ^\w+
Extract €: €(\d+\.\d{2})
Date format: \d{4}-\d{2}-\d{2}
```

***

## 计算示例

### 示例1：发票总计计算

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

### 示例2：方差计算

```
PO Price: €100
Invoice Price: €103

Variance = |(Invoice - PO)| / PO × 100
Variance = |3| / 100 × 100 = 3%

Store in "Price_Variance%" column
```

### 示例3：折扣申请

```
Original Price: €100
Discount %: 10%
Discount Amount: €100 × 0.10 = €10
Final Price: €100 - €10 = €90
```

***

## 现场操作工作流程示例

```
Document arrives
    ↓
Check condition: "Amount > €5000?"
    ↓
YES → Set field "Category" = "High Value"
    ↓
Check condition: "Supplier is preferred?"
    ↓
YES → Check "FastTrack" checkbox
    ↓
Copy "Delivery_Address" to "Invoice_Address"
    ↓
In table: Calculate line totals (Qty × Price)
    ↓
In table: Calculate total with tax
    ↓
Document now has all calculated and populated fields
```

***

## 最佳实践

✅ **做：**

* 保持公式简单
* 使用样本数据测试计算
* 验证结果是否有意义
* 记录您更改字段的原因
* 当数据相同时使用复制字段

❌**不要：**

* 创建循环引用（A=B、B=A）
* 无故覆盖重要数据
* 创建过于复杂的正则表达式模式
* 忘记验证计算结果
* 计算错误的表/列

***

## 故障排除

### “字段未更新”

**原因：**条件不满足或卡未触发

**解：**

* 检查条件是否为真
* 验证卡是否在工作流程中
* 使用样本数据进行测试
* 检查字段名称是否有拼写错误

### “计算结果错误”

**原因：**选择了错误的列或公式不正确

**解：**

* 验证源列
* 检查公式是否正确
* 手动测试
* 检查小数位/四舍五入

### “表显示错误”

**原因：**引用的列不存在

**解：**

* 验证列名称拼写
* 检查列是否有数据
* 确保列数据类型与计算匹配
* 如果需要，添加缺失的列

***

## 相关卡牌

* **ACTION\_COPY\_DOCFIELD\_TO\_DOCFIELD** - 复制值
* **EDIT\_COLUMN** - 更改表值
* **CALC\_COLUMNS** - 计算公式
* **ACTION\_SET\_FIELD\_TO\_TEXT** - 设置文本值
* **ACTION\_SET\_BOOLEAN\_FIELD** - 复选框
