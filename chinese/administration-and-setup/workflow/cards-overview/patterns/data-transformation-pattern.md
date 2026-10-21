# 数据转换模式

**模式类型：** 数据处理与操作 **复杂度：** 中等 **预计设置时间：** 30-45 分钟 **常见使用场景：** 字段计算、数据格式化、货币换算、单位换算、数据丰富

***

在 **工作流程生成器**（Workflow Dashboard → Workflow List → Add Workflow）中构建此模式。点击 **添加卡**，打开 **文档字段** 类别——此类别包含该模式串联使用的读取、写入、计算和格式化卡片：

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-category-9a74b1360332-zh.png" alt="所选类别中的可用卡片。使用前请填写所需字段。 此版本界面的部分标签尚未翻译或翻译不准确。本页说明使用正确术语；图片保留了实际界面。"><figcaption><p>所选类别中的可用卡片。使用前请填写所需字段。 此版本界面的部分标签尚未翻译或翻译不准确。本页说明使用正确术语；图片保留了实际界面。</p></figcaption></figure>

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
- 加法：Quantity + Bonus_Quantity = Total_Quantity
- 减法：Invoice_Total - Tax_Amount = Net_Amount
- 乘法：Quantity × Unit_Price = Line_Total
- 除法：Total_Amount / Quantity = Unit_Price
- 百分比：(Discount / Subtotal) × 100 = Discount_Percent
```

### 2. 字符串操作

**文本操作：**

```
- 拼接：First_Name + " " + Last_Name = Full_Name
- 转为大写："invoice" → "INVOICE"
- 转为小写："SUPPLIER" → "supplier"
- 子字符串："INV-2025-001" → "2025"（提取年份）
- 替换："01/23/2025" → "2025-01-23"
- 去除首尾空格："  ABC Corp  " → "ABC Corp"
```

### 3. 数据类型转换

**类型转换：**

```
- 字符串转数字："123.45" → 123.45
- 数字转字符串：123.45 → "123.45"
- 日期转字符串：2025-10-23 → "十月 23, 2025"
- 字符串转日期："23.10.2025" → 2025-10-23
- 布尔值转字符串：true → "Yes"
```

### 4. 单位换算

**度量单位换算：**

```
- 重量：kg → lbs，tons → kg
- 长度：cm → inches，m → ft
- 体积：liters → gallons
- 温度：Celsius → Fahrenheit
- 数量：pieces → dozens，units → pallets
```

### 5. 货币换算

**应用汇率：**

```
- USD → EUR：Amount_USD × Rate = Amount_EUR
- 多币种：全部转换为基准货币
- 历史汇率：使用发票日期对应的汇率
```

### 6. 日期转换

**日期操作：**

```
- 更改格式：10/23/2025 → 2025-10-23
- 增加天数：Invoice_Date + 30 = Due_Date
- 计算天数：Today - Invoice_Date = Age_Days
- 提取日期部分："2025-10-23" → 年：2025，月：10，日：23
```

***

## 完整工作流示例

### 场景：计算发票总额并丰富数据

**业务需求：**

* 从发票中提取行项目
* 计算行项目总额（数量 × 价格）
* 计算小计（行项目总额之和）
* 计算税额（小计 × `Tax_Rate`）
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
字段：Line_Total
公式：{{TABLE_FIELD:Quantity}} * {{TABLE_FIELD:Unit_Price}}
结果类型：Number
小数位数：2
```

**示例：**

```
行项目 1：
  数量：100
  单价：€50.00
  计算：100 × 50.00 = €5,000.00
  存储到：Line_Total

行项目 2：
  数量：50
  单价：€20.00
  计算：50 × 20.00 = €1,000.00
  存储到：Line_Total

行项目 3：
  数量：25
  单价：€15.50
  计算：25 × 15.50 = €387.50
  存储到：Line_Total
```

**指南参考：** [字段操作指南 - 计算](../field-manipulation-guide.md)

***

### 步骤 2：计算文档小计

**汇总所有行项目总额：**

**卡片：** ACTION\_CALCULATE\_FIELD

**配置：**

```
字段：Calculated_Subtotal
公式：SUM({{TABLE_COLUMN:Line_Total}})
结果类型：Number
小数位数：2
```

**示例：**

```
行项目 1 总额：€5,000.00
行项目 2 总额：€1,000.00
行项目 3 总额：€387.50

小计 = 5000 + 1000 + 387.50 = €6,387.50
存储到：Calculated_Subtotal
```

***

### 步骤 3：计算税额

**将税率应用于小计：**

**卡片：** ACTION\_CALCULATE\_FIELD

**配置：**

```
字段：Calculated_Tax_Amount
公式：{{Calculated_Subtotal}} * ({{Tax_Rate}} / 100)
结果类型：Number
小数位数：2
```

**示例：**

```
Calculated_Subtotal：€6,387.50
Tax_Rate：19% (VAT)

税额 = 6387.50 × (19 / 100)
          = 6387.50 × 0.19
          = €1,213.63

存储到：Calculated_Tax_Amount
```

***

### 步骤 4：计算总计

**将小计和税额相加：**

**卡片：** ACTION\_CALCULATE\_FIELD

**配置：**

```
字段：Calculated_Grand_Total
公式：{{Calculated_Subtotal}} + {{Calculated_Tax_Amount}}
结果类型：Number
小数位数：2
```

**示例：**

```
Calculated_Subtotal：€6,387.50
Calculated_Tax_Amount：€1,213.63

总计 = 6387.50 + 1213.63 = €7,601.13

存储到：Calculated_Grand_Total
```

***

### 步骤 5：货币换算（如有需要）

**检查是否需要换算：**

**卡片：** CONDITION\_DOC\_FIELD\_IS

**配置：**

```
字段：Invoice_Currency
运算符：IS NOT EQUAL TO
值：EUR
```

**如果需要换算：**

**步骤 5a：获取汇率**

**卡片：** CALL\_API

**配置：**

```
端点：https://api.exchangerate-api.com/v4/latest/{{Invoice_Currency}}
方法：GET
响应路径：rates.EUR
存储到：Exchange_Rate_To_EUR
```

**示例：**

```
发票货币：USD
API 响应：{
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
字段：Grand_Total_EUR
公式：{{Calculated_Grand_Total}} * {{Exchange_Rate_To_EUR}}
结果类型：Number
小数位数：2
```

**示例：**

```
总计（USD）：$7,601.13
汇率：0.92

总计（EUR） = 7601.13 × 0.92 = €6,993.04

存储到：Grand_Total_EUR
```

**指南参考：** [API 集成模式 - 货币换算](api-integration-pattern.md)

***

### 步骤 6：数据丰富 - 添加 GL 科目

**根据产品类别查找 GL 科目：**

**卡片：** ACTION\_SET\_FIELD\_FROM\_MASTER\_DATA

**配置：**

```
查找表：GL_Account_Mapping
查找键：{{TABLE_FIELD:Product_Category}}
返回字段：GL_Account_Number
存储到：GL_Account
```

**示例：**

```
行项目 1：
  产品类别: "Office Supplies"
  查询 → GL_Account_Mapping 表
  结果: 总账科目 "4200-100" (办公费用)

行项目 2：
  产品类别: "IT Equipment"
  查询 → GL_Account_Mapping 表
  结果: 总账科目 "6100-200" (IT 资产)

行项目 3：
  产品类别: "Services"
  查询 → GL_Account_Mapping 表
  结果: 总账科目 "5000-300" (服务费用)
```

**指南参考：** [字段操作指南 - 主数据](../field-manipulation-guide.md)

***

### 步骤 7：验证计算结果

**将计算出的总计与发票总额进行比较：**

**卡片：** CONDITION\_COMPARE\_TWO\_DOCFIELD\_VALUES

**配置：**

```
字段 1：Calculated_Grand_Total
字段 2：Invoice_Total（来自 OCR）
运算符：计算差异百分比
容差：1%
```

**计算方式：**

```
差异 % = |Calculated - Invoice| / Invoice × 100

示例：
  计算总额：€7,601.13
  发票总额：€7,600.00

  差异 = |7601.13 - 7600.00| / 7600.00 × 100
          = 1.13 / 7600.00 × 100
          = 0.015%

  0.015% ≤ 1% 容差吗？是 ✅
  结果：PASS（计算结果与发票相符）
```

**逻辑：**

```
IF Variance ≤ 1%:
  设置 Validation_Status = "PASS"
  继续处理
ELSE:
  设置 Validation_Status = "FAIL"
  创建审核任务
  标记为需要人工验证
```

**指南参考：** [条件卡片指南 - 字段比较](../condition-cards-complete-guide.md)

***

### 步骤 8：格式化导出数据

**统一格式：**

**卡片：** ACTION\_SET\_FIELD\_TO\_TEXT

**日期格式化：**

```
字段：Invoice_Date_Formatted
值：FORMATDATE({{Invoice_Date}}, "YYYY-MM-DD")
示例：10/23/2025 → 2025-10-23
```

**数字格式化：**

```
字段：Amount_Formatted
值：FORMATNUMBER({{Grand_Total_EUR}}, 2, ",", ".")
示例：7601.13 → 7.601,13（德国格式）
```

**文本格式化：**

```
字段：Supplier_Name_Upper
值：UPPERCASE({{Supplier_Name}})
示例："ABC Corporation" → "ABC CORPORATION"
```

***

## 高级转换

### 转换 1：多级税额计算

**场景：** 每个行项目适用不同税率

```
行项目 1：Product A（税率 19%）
行项目 2：Product B（税率 7% - 减免税率）
行项目 3：Product C（税率 0% - 免税）

计算：
  行项目 1 税额 = €5,000.00 × 0.19 = €950.00
  行项目 2 税额 = €1,000.00 × 0.07 = €70.00
  行项目 3 税额 = €387.50 × 0.00 = €0.00

  总税额 = €950.00 + €70.00 + €0.00 = €1,020.00
```

**实施方式：**

```
对每个行项目：
  1. 获取产品税务类别
  2. 查找适用的税率
  3. 计算：Line_Net × Tax_Rate = Line_Tax
  4. 汇总所有 Line_Tax 值 = Total_Tax
```

***

### 转换 2：折扣计算

**场景：** 应用批量折扣和提前付款折扣

```
原始小计: €10,000.00

步骤 1：批量折扣（订单金额 > €5,000 时折扣 10%）
  折扣 = €10,000.00 × 0.10 = €1,000.00
  扣除批量折扣后 = €10,000.00 - €1,000.00 = €9,000.00

步骤 2：提前付款折扣（10 天内付款时折扣 2%）
  折扣 = €9,000.00 × 0.02 = €180.00
  扣除付款折扣后 = €9,000.00 - €180.00 = €8,820.00

步骤 3：计算税额（按折扣后金额计算）
  税额 = €8,820.00 × 0.19 = €1,675.80

最终总额 = €8,820.00 + €1,675.80 = €10,495.80
```

**实施方式：**

```
1. 检查订单金额是否符合批量折扣条件
2. 计算批量折扣
3. 将批量折扣应用于小计
4. 检查付款条款是否适用提前付款折扣
5. 计算提前付款折扣
6. 应用提前付款折扣
7. 按最终折扣后金额计算税额
8. 计算总计
```

***

### 转换 3：计量单位换算

**场景：** 将发票计量单位换算为标准计量单位

```
发票显示：
  产品: Steel Rods
  数量: 50
  单位: Meters
  单价: €10.00/meter
  行项目总额: €500.00

公司标准计量单位 (UOM): Feet

换算：
  1 meter = 3.28084 feet

  数量 (feet) = 50 meters × 3.28084 = 164.042 feet
  单价 (feet) = €10.00/meter ÷ 3.28084 = €3.05/foot

  验证: 164.042 feet × €3.05/foot ≈ €500.00 ✅
```

**实施方式：**

```
1. 确定发票计量单位（UOM）
2. 获取转换为标准 UOM 的换算系数
3. 转换数量
4. 转换单价
5. 验证行项目总额保持不变
6. 存储原始值和转换后的值
```

***

### 转换 4：日期计算

**场景：** 计算付款条件和到期日

```
发票日期: 2025-10-23
付款条款: NET30

计算：
  到期日期 = 发票日期 + 30 天 = 2025-11-22

  提前付款折扣适用条件：
    付款日期 ≤ 发票日期 + 10 天
    折扣截止日期 = 2025-11-02

  距到期天数 = 到期日期 - 今天
    如果今天 = 2025-10-23：天数 = 30
    如果今天 = 2025-11-15：天数 = 7
    如果今天 = 2025-11-23：天数 = -1 (逾期)
```

**实施方式：**

```
1. 提取 Invoice_Date
2. 提取 Payment_Terms（例如，"NET30"、"NET60"、"2/10 NET30"）
3. 解析付款条款
4. 计算 Due_Date
5. 计算 Discount_End_Date（如适用）
6. 计算 Days_Until_Due
7. 设置状态: "Current"（当前）、"Due Soon"（即将到期）、"Overdue"（逾期）
```

***

### 转换 5：文本解析与提取

**场景：** 从非结构化文本中提取结构化数据

```
原始字段: "PO-2025-ABC-12345-REV2"

提取：
  年份: "2025"
  部门: "ABC"
  采购订单编号: "12345"
  修订版本: "2"

方法：
  使用分隔符 "-" 拆分
  数组: ["PO", "2025", "ABC", "12345", "REV2"]

  提取：
    Year = Array[1] = "2025"
    Department = Array[2] = "ABC"
    PO_Number = Array[3] = "12345"
    Revision = 从 Array[4] 提取数字 = "2"
```

***

## 完整转换工作流图

```
已提取发票数据
│
├─ 步骤 1：行项目计算
│  对每个行项目：
│    Quantity × Unit_Price = Line_Total
│  结果：已计算各行项目总额
│
├─ 步骤 2：小计计算
│  SUM(All Line_Totals) = Subtotal
│  结果: €6,387.50
│
├─ 步骤 3：税额计算
│  Subtotal × Tax_Rate = Tax_Amount
│  €6,387.50 × 19% = €1,213.63
│
├─ 步骤 4：总计计算
│  Subtotal + Tax_Amount = Grand_Total
│  €6,387.50 + €1,213.63 = €7,601.13
│
├─ 步骤 5：货币检查
│  │
│  ├─ Currency = EUR? 是
│  │  → 跳过换算
│  │  → 直接使用 Grand_Total
│  │
│  └─ Currency ≠ EUR? 否（例如，USD）
│     │
│     ├─ 调用汇率 API
│     │  获取：USD → EUR 汇率 (0.92)
│     │
│     ├─ 换算金额
│     │  $7,601.13 × 0.92 = €6,993.04
│     │
│     └─ 存储换算后的金额
│        Grand_Total_EUR = €6,993.04
│
├─ 步骤 6：数据丰富
│  对每个行项目：
│    查询 Product_Category → GL_Account
│    将 GL_Account 存储在行项目中
│  结果：所有行项目都已关联总账科目
│
├─ 步骤 7：验证
│  │
│  ├─ 比较计算总额与发票总额
│  │  差异率 = |计算金额 - 发票金额| / 发票金额 × 100
│  │
│  ├─ 差异率 ≤ 1%? ✅
│  │  设置 Validation_Status = "PASS"
│  │  继续处理
│  │
│  └─ 差异率 > 1%? ❌
│     设置 Validation_Status = "FAIL"
│     创建审核任务
│     标记以供人工检查
│
├─ 步骤 8：格式化
│  │
│  ├─ 格式化日期
│  │  10/23/2025 → 2025-10-23
│  │
│  ├─ 格式化数字
│  │  7601.13 → 7.601,13 (因区域设置而异)
│  │
│  ├─ 格式化文本
│  │  "abc corp" → "ABC CORP"
│  │
│  └─ 格式化以供导出
│     所有字段均采用与 ERP 兼容的格式
│
└─ 转换完成
   文档已准备好进入工作流的下一步
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
问题：Unit_Price = Total / Quantity，但 Quantity = 0

解决方案：
  IF Quantity = 0 OR Quantity IS NULL:
    设置 Unit_Price = 0
    标记为需要审核
  ELSE:
    正常计算
```

**错误 2：数字格式无效**

```
问题：字段包含 "€1,234.56"，但需要数字 1234.56

解决方案：
  1. 移除货币符号
  2. 移除千位分隔符
  3. 如有需要，转换小数分隔符
  4. 解析为数字
  5. 验证结果
```

**错误 3：日期解析失败**

```
问题：日期格式不符合预期

解决方案：
  1. 尝试多种日期格式
  2. 如果都失败：设为 null
  3. 标记为需要人工审核
  4. 记录原始值
```

**错误 4：缺少换算系数**

```
问题：未知的 UOM 换算

解决方案：
  1. 检查换算表
  2. 如果未找到：跳过换算
  3. 标记管理员添加换算项
  4. 使用原始值
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
* **ACTION\_SET\_FIELD\_TO\_TEXT** - [字段操作指南](../field-manipulation-guide.md)
* **ACTION\_COPY\_FIELD\_VALUE** - [字段操作指南](../field-manipulation-guide.md)
* **CALL\_API** - [Call API 指南](../call-api-guide.md)
* **CONDITION\_COMPARE\_TWO\_DOCFIELD\_VALUES** - [条件卡片指南](../condition-cards-complete-guide.md)

### 后续步骤

* 验证结果：[决策逻辑模式](decision-logic-pattern.md)
* 为错误创建任务：[任务管理模式](task-management-pattern.md)
* 用于 PO 匹配：[PO 匹配模式](po-matching-pattern.md)

***

**模式版本：** 1.0 **最后更新：** October 23, 2025 **难度：** 中等 **预计时间：** 30-45 分钟 **成功率：** 高
