# 条件卡片 - 完整指南

## 条件卡片 - 完整指南

**涵盖：**剩余的 31 个条件卡片

***

本页中的条件卡片位于工作流构建器的 **When** 和 **And** 组中，用于决定是否运行 Then 操作：

<figure><img src="../../../.gitbook/assets/workflow_designer_cards.png" alt="工作流构建器画布，包含 When、And 和 Then 卡片组"><figcaption><p>通过 <strong>Add Card</strong> 将条件卡片添加到 <strong>When</strong> 和 <strong>And</strong> 组。</p></figcaption></figure>

***

### 📌 版本信息

**状态：**大多数条件卡片都很稳定，采用单版本或双版本结构。**版本模式：**大多数卡片遵循 v1 → v2 模式（添加 i18n 支持）。**多版本示例：**CONDITION\_DECISION\_TREE\_DATA（v2-v3）

**注意：**某些采购订单比较条件卡片有多个版本。请参考本指南了解当前行为，并参考下方发行说明了解已发布的变更。

📖 [产品发行说明](../../../overview-and-basics/release-notes/) | [采购订单匹配指南](po-matching-complete-guide.md)

***

## 文档状态与状态条件

### 卡片：CONDITION\_DOC\_STATUS\_IS\_ISNOT / 文档状态检查

#### 用途

检查文档是否处于特定状态

#### 使用场景

* 审批前
* 工作流的特定阶段
* 基于状态进行路由

#### 文档状态类型

```
- Upload：正在上传
- OCR：正在扫描
- Classification：类型检测
- Ready for Validation：等待验证
- Workflow：处理中
- Pending Approval：需要审批
- Pending Second Approval：需要二次审批
- Auto Accounting：自动记账
- Export：正在导出
- Error：发生问题
```

#### 工作方式

```
Current Status: "Pending Approval"
    ↓
Check: Is status = "Pending Approval"?
    ↓
YES → Continue with action
NO → Stop or do alternative action
```

#### 示例

```
Condition: "Document status IS Pending Approval?"
    ↓
If YES: Create approval task
If NO: Do something else
```

#### 参数

```
Operator: IS / IS NOT
Status: [Select status]
```

***

### 卡片：CONDITION\_DOC\_STATUS\_IS\_ISNOT\_IN\_LIST

#### 用途

检查状态是否与列表中的任一状态匹配

#### 使用场景

* 有多个有效状态时
* 对状态使用 OR 逻辑

#### 示例

```
Condition: "Status is one of: [Pending Approval, Pending Second Approval, Workflow]?"
    ↓
If status matches any: Continue
If doesn't match: Stop
```

***

### 卡片：CONDITION\_DOC\_TYPE\_IS\_ISNOT / 文档类型检查 <a id="condition-doc-type-is-isnot"></a>

#### 用途

检查文档是否为特定类型

#### 文档类型

```
- Invoice
- Credit Note
- Purchase Order
- Delivery Note
- ASN (Advanced Ship Notice)
- Receipt
- Return
- Custom Types
```

#### 工作方式

```
Document type: "Invoice"
    ↓
Check: Is type = "Invoice"?
    ↓
YES → Process as invoice
NO → Process differently
```

#### 示例

```
Condition: "Document type IS Invoice?"
    ↓
If YES: Check PO match
If NO: Skip PO validation
```

***

### 卡片：CONDITION\_DOC\_TYPE\_IS\_ISNOT\_LIST

#### 用途

检查类型是否与列表中的任一类型匹配

#### 示例

```
Condition: "Type is one of: [Invoice, Credit Note]?"
    ↓
YES: Process financial document
NO: Skip financial checks
```

***

### 卡片：CONDITION\_SUB\_ORG\_IS\_ISNOT / 子组织检查

#### 用途

检查哪个组织或部门拥有该文档

#### 组织

```
- Finance Department
- Procurement
- Warehouse
- Manufacturing
- Quality Control
- Distribution
- Regional Offices
```

#### 示例

```
Document belongs to: "Berlin Office"
    ↓
Check: Sub-Org = "Berlin Office"?
    ↓
YES: Assign to Berlin team
NO: Check other offices
```

***

### 卡片：CONDITION\_PURCHASE\_ORDER\_IMPORT / 采购订单导入检查

#### 用途

检查采购订单是新导入的还是已存在的

#### 工作方式

```
PO Status: "Newly Imported" (First time seeing this PO)
    ↓
Check: Is new import?
    ↓
YES: Do initial validation
NO: Use cached PO data
```

#### 使用场景

* 对新采购订单进行不同处理
* 跳过已知采购订单的验证
* 跟踪首次出现的供应商

***

## 受派人条件

### 卡片：CONDITION\_USER\_IS\_ISNOT / 用户检查

#### 用途

检查文档是否分配给特定用户

#### 工作方式

```
Assigned to: "John Smith"
    ↓
Check: Is assigned to "John Smith"?
    ↓
YES: Continue
NO: Stop
```

#### 示例

```
Condition: "Assigned to IS 'Finance Manager'"?
    ↓
If YES: Create approval task
If NO: Skip approval
```

***

### 卡片：CONDITION\_USER\_IS\_ISNOT\_IN\_LIST

#### 用途

检查文档是否分配给列表中的任一用户

#### 示例

```
Condition: "Assigned to one of: [John, Sarah, Mike]?"
    ↓
YES: Continue
NO: Stop
```

***

### 卡片：CONDITION\_GROUP\_IS\_ISNOT / 用户组检查

#### 用途

检查文档是否分配给特定用户组

#### 示例

```
Assigned to: "Finance Team" (10 members)
    ↓
Check: Is assigned to Finance Team?
    ↓
YES: Process for group
NO: Check other groups
```

***

### 卡片：CONDITION\_GROUP\_IS\_ISNOT\_IN\_LIST

#### 用途

检查文档是否分配给列表中的任一用户组

#### 示例

```
Condition: "Assigned to one of: [Finance, Procurement, Quality]?"
    ↓
YES: Continue
NO: Stop
```

***

## 日期与时间条件

### 卡片：CONDITION\_TIME\_IS\_ISNOT\_BETWEEN / 日期范围检查

#### 用途

检查日期是否介于两个日期之间

#### 工作方式

```
Document Date: 2025-10-23
    ↓
Check: Is date between 2025-10-01 and 2025-10-31?
    ↓
YES (October) → Continue
NO (Other month) → Stop
```

#### 计算

```
Formula:
  Start Date ≤ Document Date ≤ End Date?

Example:
  2025-01-01 ≤ 2025-10-23 ≤ 2025-10-31?
  YES ✅ Within range
```

#### 使用场景

* 检查日期是否处于财务期间
* 检查是否在截止日期范围内
* 检查是否在促销期内

#### 示例

```
Condition: "Document date between Oct 1 and Oct 31?"
    ↓
If YES: Oct invoices (monthly processing)
If NO: Other month invoices
```

#### 参数

```
Start Date: [Select or enter]
End Date: [Select or enter]
Date Field: [Which field to check]
```

***

### 卡片：CONDITION\_TODAY\_IS\_ISNOT / 今日检查

#### 用途

检查今天的日期是否符合条件

#### 工作方式

```
Today: 2025-10-23
    ↓
Check: Is today > 2025-10-31?
    ↓
NO → Deadline not passed
YES → Deadline passed (overdue)
```

#### 使用场景

```
Is today past deadline? → Invoice is overdue
Is today past promotion date? → Promotion ended
Is today in quarter? → For quarterly reporting
```

#### 示例

```
Condition: "Is today AFTER invoice due date?"
    ↓
If YES: Invoice is overdue, escalate
If NO: Invoice still within deadline
```

***

### 卡片：CONDITION\_CONFIRMED\_DELIVERY\_ACCEPTED\_DATE\_IN\_CALENDAR\_MASTER\_DATA

#### 用途

检查交付日期是否与日历中已批准的交付日期匹配

#### 工作方式

```
Delivery Date from Invoice: 2025-10-25
    ↓
Check Master Calendar: Is 2025-10-25 acceptable?
    ↓
(Master calendar has list of acceptable dates)
    ↓
YES: Date is acceptable
NO: Date not in approved list
```

#### 使用场景

* 验证交付日期是否符合约定
* 对照节假日日历进行检查
* 对照合同约定日期进行验证

#### 示例

```
Supplier promised: 2025-10-25
Invoice shows delivery: 2025-10-25
Check Master Calendar: Is 2025-10-25 valid delivery date?
    ↓
YES: Delivery date acceptable ✅
```

***

## 逻辑条件

### 卡片：CONDITION\_DECISION\_TREE\_DATA / 决策表返回值

#### 用途

检查决策表是否返回值

#### 工作方式

```
Run Decision Table
    ↓
Does it return values?
    ↓
YES: Data is available for next cards
NO: No matching results
```

#### 使用场景

* 使用决策表结果前
* 作为门控条件
* 检查是否有可用的路由

#### 示例

```
Decision Table: "Route by supplier"
    ↓
Condition: "Decision table returns data?"
    ↓
If YES: Use returned values for routing
If NO: Use default routing
```

***

### 卡片：CONDITION\_CONTINUE\_CHANCE / 随机概率

#### 用途

按指定概率继续

#### 工作方式

```
Probability: 50%
    ↓
Roll dice
    ↓
Random chance: 50% YES, 50% NO
```

#### 使用场景

* A/B 测试工作流
* 抽样处理文档
* 随机质量检查

#### 示例

```
Condition: "Continue with 10% chance?"
    ↓
90% of documents: Stop here
10% of documents: Continue for detailed review
```

#### 计算

```
If probability = 50%:
  - 50% of documents continue
  - 50% of documents stop

If probability = 10%:
  - 10% continue (1 in 10 documents)
  - 90% stop
```

***

### 卡片：CONDITION\_MODULE\_IS\_ISNOT\_ACTIVE / 功能检查

#### 用途

检查特定模块或功能是否已启用

#### 模块

```
- PO Matching
- Auto Accounting
- OCR
- Document Classification
- Supplier Management
- Custom Modules
```

#### 工作方式

```
Module: "PO Matching"
    ↓
Is PO Matching enabled?
    ↓
YES: Do PO match validation
NO: Skip PO checks
```

#### 使用场景

* 依赖特定功能的工作流
* 可选处理
* 检查已授权的功能是否处于启用状态

***

### 卡片：CONDITION\_HTTPS\_REQUEST\_STATUS / 请求结果检查 <a id="condition-https-request-status"></a>

#### 用途

检查 HTTPS 请求是否成功

#### 状态码

```
200-299: ✅ Success
300-399: ↪️ Redirect
400-499: ❌ Client Error
500-599: ❌ Server Error
```

#### 工作方式

```
Send HTTPS request
    ↓
Receive response code
    ↓
Check: Was request successful (200)?
    ↓
YES: Continue with response data
NO: Error handling
```

#### 示例

```
Send pricing request to API
    ↓
Condition: "Did request return 200 (success)?"
    ↓
If YES: Use returned price
If NO: Use fallback price
```

***

### 卡片：CONDITION\_SUPPLIER\_STATUS\_IS\_ISNOT / 供应商状态检查 <a id="condition-supplier-status-is-isnot"></a>

#### 用途

检查系统中的供应商状态

#### 供应商状态

```
✅ ACTIVE: Can do business
⚠️ ON HOLD: Temporarily blocked
❌ INACTIVE: No longer doing business
⚠️ CONDITIONAL: Only for specific items
```

#### 工作方式

```
Supplier: ABC Corp
Status in Database: ACTIVE
    ↓
Check: Is status ACTIVE?
    ↓
YES: Process normally
NO: Flag for review
```

#### 示例

```
Invoice from ABC Corp
    ↓
Condition: "Is supplier status ACTIVE?"
    ↓
If YES: Process normally
If NO: Block or escalate
```

***

### 卡片：CONDITION\_SPECIFY\_SUPPLIER\_TYPE

#### 用途

指定或检查供应商类型

#### 供应商类型

```
- Preferred Supplier
- Standard Supplier
- Spot Purchase
- Framework Agreement
- Strategic Partner
```

#### 工作方式

```
Supplier Type: "Preferred"
    ↓
Check: Is preferred supplier?
    ↓
YES: Apply preferred supplier discounts
NO: Standard pricing
```

***

## 决策流示例

### 流程 1：基于状态的处理

```
Document Arrives
    ↓
Check: Status = "Ready for Validation"?
    ↓
YES: Validate document
    ↓
Check: Status = "Pending Approval"?
    ↓
YES: Create approval task
    ↓
Check: Status = "Error"?
    ↓
YES: Escalate to manager
```

### 流程 2：基于供应商的处理

```
Invoice Arrives
    ↓
Check: Supplier status ACTIVE?
    ↓
NO: Block and escalate
    ↓
YES: Check: Supplier is preferred?
    ↓
YES: Fast track approval
NO: Standard approval
```

### 流程 3：基于金额并检查日期

```
Invoice Arrives
    ↓
Check: Amount > €10,000?
    ↓
YES: Check: Date within Oct (fiscal period)?
    ↓
YES: Assign to Finance Director
NO: Assign to Finance Manager
```

***

## 条件卡片对比

| 卡片                                        | 检查内容       | 运算符        | 用途           |
| ------------------------------------------- | -------------- | ------------- | -------------- |
| CONDITION\_DOC\_STATUS\_IS\_ISNOT           | 文档状态       | IS / IS NOT   | 阶段检查       |
| CONDITION\_DOC\_STATUS\_IS\_ISNOT\_IN\_LIST | 列表中的状态   | IN / NOT IN   | 多个状态       |
| CONDITION\_DOC\_TYPE\_IS\_ISNOT             | 文档类型       | IS / IS NOT   | 类型筛选       |
| CONDITION\_DOC\_TYPE\_IS\_ISNOT\_LIST       | 列表中的类型   | IN / NOT IN   | 多种类型       |
| CONDITION\_SUB\_ORG\_IS\_ISNOT              | 组织           | IS / IS NOT   | 部门检查       |
| CONDITION\_USER\_IS\_ISNOT                  | 受派用户       | IS / IS NOT   | 用户检查       |
| CONDITION\_USER\_IS\_ISNOT\_IN\_LIST        | 列表中的用户   | IN / NOT IN   | 多个用户       |
| CONDITION\_GROUP\_IS\_ISNOT                 | 受派用户组     | IS / IS NOT   | 用户组检查     |
| CONDITION\_GROUP\_IS\_ISNOT\_IN\_LIST       | 列表中的用户组 | IN / NOT IN   | 多个用户组     |
| CONDITION\_TIME\_IS\_ISNOT\_BETWEEN         | 日期范围       | BETWEEN       | 日期区间       |
| CONDITION\_TODAY\_IS\_ISNOT                 | 今天的日期     | IS / IS NOT   | 今日检查       |
| CONDITION\_DECISION\_TREE\_DATA             | 决策表返回值   | HAS / HAS NOT | 决策表结果检查 |
| CONDITION\_CONTINUE\_CHANCE                 | 概率           | CHANCE        | 随机门控       |
| CONDITION\_MODULE\_IS\_ISNOT\_ACTIVE        | 功能是否启用   | IS / IS NOT   | 功能检查       |
| CONDITION\_HTTPS\_REQUEST\_STATUS           | 请求结果       | STATUS        | 响应检查       |
| CONDITION\_SUPPLIER\_STATUS\_IS\_ISNOT      | 供应商状态     | IS / IS NOT   | 供应商检查     |

***

## 条件最佳实践

✅ **建议：**

* 使用具体的条件
* 使用样例测试逻辑
* 按逻辑顺序排列条件
* 为所有路径设置后备处理
* 记录复杂逻辑

❌ **避免：**

* 创建循环条件（A 依赖 B，B 又依赖 A）
* 让条件过于复杂
* 忽略边缘情况
* 假定字段始终有值
* 创建不可能成立的条件

***

## 组合多个条件

```
Condition 1: Type = Invoice?
    AND
Condition 2: Amount > €5000?
    AND
Condition 3: Supplier status = Active?
    ↓
ALL TRUE → Process
SOME FALSE → Stop
```

***

## 相关卡片

* **CONDITION\_DOC\_FIELD\_CONTAINS** - 字段内容检查
* **CONDITION\_COMPARE\_TWO\_DOCFIELD\_VALUES** - 字段比较
* **CONDITION\_CHECKBOX\_IS** - 复选框检查
