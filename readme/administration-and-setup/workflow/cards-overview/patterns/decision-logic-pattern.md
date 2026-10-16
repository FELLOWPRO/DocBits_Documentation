# 决策逻辑模式

**模式类型：**条件路由与逻辑 **复杂度：**中等 **预计设置时间：**30-45 分钟 **常见用例：**多路径路由、条件处理、决策树、业务规则实施

***

您可以在 **Workflow Builder**（Workflow Dashboard → Workflow List → Add Workflow）中构建此模式。点击 **Add Card** 并打开 **Logic** 类别——其中包含用于驱动决策树的条件卡片和分支卡片，您可以将它们与 **And** 组结合起来评估多个条件：

<figure><img src="../../../../.gitbook/assets/workflow_add_card_picker.png" alt="Workflow Builder 中按类别分组的 Add Card 卡片库"><figcaption><p><strong>Add Card</strong> 卡片库——条件卡片和分支卡片位于 <strong>Logic</strong> 类别下。</p></figcaption></figure>

***

## 模式概述

此模式演示如何在 DocBits 工作流中使用条件卡片实现复杂的决策逻辑，根据文档属性、字段值和业务规则将文档路由到不同的处理路径。

**此模式的功能：**

1. 按顺序或并行评估多个条件
2. 根据条件将文档路由到不同路径
3. 实施业务规则和政策
4. 处理复杂的决策树
5. 组合多个标准来决定路由

***

## 何时使用此模式

在需要以下功能时使用此模式：

* ✅ 按金额阈值路由文档
* ✅ 为不同文档类型应用不同规则
* ✅ 实施多级审批逻辑
* ✅ 处理复杂的业务政策
* ✅ 根据多个标准创建动态路由
* ✅ 实施异常处理逻辑
* ✅ 创建审批矩阵

**以下情况不要使用此模式：**

* ❌ 简单的线性工作流已足够
* ❌ 所有文档都遵循相同路径
* ❌ 不需要条件处理

***

## 决策逻辑类型

### 1. 简单的 IF-THEN 逻辑

```
IF condition:
  → Action A
ELSE:
  → Action B
```

**示例：**

```
IF Amount > €10,000:
  → Assign to Director
ELSE:
  → Assign to Manager
```

### 2. 多个条件（AND 逻辑）

```
IF condition1 AND condition2 AND condition3:
  → Action A
ELSE:
  → Action B
```

**示例：**

```
IF Amount > €10,000 AND Supplier = "New" AND Department = "IT":
  → Assign to IT Director + CFO (dual approval)
ELSE:
  → Standard approval workflow
```

### 3. 替代条件（OR 逻辑）

```
IF condition1 OR condition2 OR condition3:
  → Action A
ELSE:
  → Action B
```

**示例：**

```
IF Amount > €50,000 OR Supplier is "Blocked" OR Document has "Urgent" flag:
  → Escalate immediately
ELSE:
  → Standard processing
```

### 4. 嵌套决策树

```
IF condition1:
  IF condition2:
    → Action A
  ELSE:
    → Action B
ELSE:
  IF condition3:
    → Action C
  ELSE:
    → Action D
```

**示例：**

```
IF Document_Type = "Invoice":
  IF Amount > €10,000:
    → High-value invoice workflow
  ELSE:
    → Standard invoice workflow
ELSE IF Document_Type = "Credit Note":
  IF Amount > €5,000:
    → High-value credit workflow
  ELSE:
    → Standard credit workflow
```

***

## 完整工作流示例

### 场景：发票审批矩阵

**业务规则：**

1. 金额 < €1,000：自动审批
2. 金额 €1,000-€10,000：经理审批
3. 金额 > €10,000 且为新供应商：总监 + CFO 审批
4. 金额 > €10,000 且为现有供应商：仅需总监审批
5. 任意金额但采购订单不匹配：先由采购部门审批
6. 紧急发票（已标记）：使用加急工作流

**实施：**

```
STEP 1: Check for PO Mismatch
  IF PO_Match_Status = "FAIL":
    → Route to Procurement for PO resolution
    → After resolution, continue below

STEP 2: Check Urgent Flag
  IF Urgent_Flag = TRUE:
    → Skip amount checks
    → Direct to highest approver
    → Set priority = HIGH
    → 1-day deadline

STEP 3: Amount-Based Routing (if not urgent)
  IF Amount < €1,000:
    → Auto-approve
    → Export immediately

  ELSE IF Amount < €10,000:
    → Create task for Manager
    → Priority: Medium
    → Deadline: 3 days

  ELSE IF Amount ≥ €10,000:
    CHECK Supplier Status:
      IF Supplier_Age < 180 days (New):
        → Create task for Director (Task 1)
        → After approval, create task for CFO (Task 2)
        → Priority: High
        → Deadline: 2 days each

      ELSE (Existing Supplier):
        → Create task for Director only
        → Priority: High
        → Deadline: 2 days
```

***

## 分步实施

### 第 1 步：定义条件卡片

**条件 1：金额阈值**

```
Card: CONDITION_DOC_FIELD_AMOUNT
Field: Total_Amount
Operator: IS LESS THAN
Value: 1000
Currency: EUR
```

**条件 2：文档类型检查**

```
Card: CONDITION_DOC_TYPE_IS_ISNOT
Document Type: IS
Type: Invoice
```

**条件 3：供应商状态**

```
Card: CONDITION_SUPPLIER_STATUS_IS_ISNOT
Supplier Status: IS
Status: ACTIVE
```

**条件 4：新供应商检查**

```
Card: CONDITION_DOC_FIELD_DATE
Field: Supplier_First_Transaction_Date
Operator: IS AFTER
Value: {{TODAY_MINUS_180_DAYS}}
```

**指南参考：**[条件卡片完整指南](../condition-cards-complete-guide.md)

***

### 第 2 步：构建决策树

**第 1 级：文档类型**

```
Workflow: "Invoice Processing"

IF Document_Type = "Invoice":
  → Continue to Level 2

ELSE IF Document_Type = "Credit Note":
  → Branch to "Credit Note Processing"

ELSE IF Document_Type = "Receipt":
  → Branch to "Receipt Processing"

ELSE:
  → Route to "Unknown Document Type" handling
```

**第 2 级：金额阈值（适用于发票）**

```
IF Amount < €1,000:
  → Branch to "Auto-Approve Path"

ELSE IF Amount < €10,000:
  → Branch to "Manager Approval Path"

ELSE IF Amount < €50,000:
  → Branch to "Director Approval Path"
  → Check Level 3 conditions

ELSE (Amount ≥ €50,000):
  → Branch to "Executive Approval Path"
  → Dual or triple approval required
```

**第 3 级：供应商分析（适用于高金额发票）**

```
IF Supplier_Status = "BLOCKED":
  → STOP processing
  → Create urgent escalation task
  → Notify procurement and finance

ELSE IF Supplier_Age < 180 days (New):
  → Additional approval required
  → Add CFO to approval chain
  → Enhanced verification

ELSE IF Supplier_Risk_Rating = "HIGH":
  → Additional checks required
  → Fraud detection review
  → Manager pre-approval

ELSE:
  → Standard high-value workflow
```

***

### 第 3 步：创建路由操作

**路径 A：自动审批（金额 < €1,000）**

```
Actions:
1. Set field "Approval_Type" = "AUTO"
2. Set field "Approval_Level" = "0"
3. ACTION_APPROVE_DOCUMENT
4. Export to ERP
5. Send confirmation email (optional)
```

**路径 B：经理审批（€1,000-€10,000）**

```
Actions:
1. Set field "Approval_Type" = "MANUAL"
2. Set field "Approval_Level" = "1"
3. tasks_create:
   - Title: "Approve Invoice {{DOCUMENT_NUMBER}}"
   - Assign to: Department_Manager
   - Priority: Medium
   - Deadline: 3 days
4. Send email notification to manager
5. Wait for task completion
6. If approved: Export to ERP
7. If rejected: Return to supplier
```

**路径 C：总监审批（€10,000-€50,000）**

```
Actions:
1. Set field "Approval_Type" = "MANUAL"
2. Set field "Approval_Level" = "2"
3. Check Supplier_Age:
   IF New (< 180 days):
     - Create Task 1: Director approval
     - After Task 1: Create Task 2: CFO approval
     - Dual approval required
   ELSE:
     - Create Task: Director approval only
4. Priority: High
5. Deadline: 2 days
6. Send email notifications
7. Wait for completion
8. If all approved: Export
9. If any rejected: Return to supplier
```

**路径 D：高管审批（≥ €50,000）**

```
Actions:
1. Set field "Approval_Type" = "EXECUTIVE"
2. Set field "Approval_Level" = "3"
3. Sequential approvals:
   - Task 1: Finance Director
   - Task 2: CFO
   - Task 3: CEO (if > €100,000)
4. Priority: Urgent
5. Deadline: 1 day each
6. Send urgent notifications
7. Executive dashboard update
8. Wait for all approvals
9. If all approved: Export
10. If any rejected: Executive review meeting
```

***

## 高级决策逻辑模式

### 模式 1：基于评分的路由

**计算风险评分并据此路由：**

```
Risk Score Calculation:
  Score = 0

  IF Amount > €50,000: Score += 30
  IF Supplier_Age < 180 days: Score += 25
  IF PO_Variance > 10%: Score += 20
  IF Supplier_Country = "High Risk Country": Score += 15
  IF Payment_Terms < 30 days: Score += 10

  Total Score Range: 0-100

Routing:
  IF Score < 20: Auto-approve
  IF Score 20-50: Manager approval
  IF Score 51-75: Director approval
  IF Score > 75: Executive approval + fraud check
```

**实施：**

```
1. ACTION_CALCULATE_FIELD: Calculate risk score
2. ACTION_SET_FIELD_TO_NUMBER: Store score
3. CONDITION_DOC_FIELD_NUMBER: Check score thresholds
4. Route based on score
```

***

### 模式 2：基于部门的矩阵

**按部门应用不同的审批规则：**

```
Department Matrix:

  IT Department:
    Amount < €5,000: IT Manager
    Amount ≥ €5,000: IT Director + CIO

  Finance Department:
    Amount < €10,000: Finance Manager
    Amount ≥ €10,000: CFO

  Operations Department:
    Amount < €3,000: Operations Manager
    Amount ≥ €3,000: COO

  General:
    Amount < €2,000: Department Manager
    Amount ≥ €2,000: Department Director
```

**实施：**

```
1. Check Department field
2. Based on department, check amount threshold
3. Route to appropriate approver
4. Different thresholds per department
```

***

### 模式 3：基于时间的逻辑

**根据时间采用不同规则：**

```
Month-End Processing (Last 3 days of month):
  IF Today in last 3 days of month:
    - Priority: URGENT
    - Deadline: 1 day
    - Approver: On-duty finance manager
    - Expedited workflow
  ELSE:
    - Standard priority
    - Standard deadline
    - Standard workflow

Business Hours vs After Hours:
  IF Time between 9 AM - 5 PM:
    - Assign to current shift
  ELSE:
    - Queue for next business day
    - OR route to on-call approver

Fiscal Period:
  IF Document_Date in Current_Fiscal_Period:
    - Standard processing
  ELSE:
    - Flag as "Prior Period"
    - Require accounting approval
    - Additional checks
```

***

### 模式 4：基于异常的路由

**单独路由异常：**

```
Exception Detection:

  No Exception:
    → Standard workflow

  Minor Exception (Auto-fixable):
    → Auto-correct
    → Log correction
    → Continue standard workflow

  Medium Exception (Needs review):
    → Create review task
    → Flag document
    → After fix: Continue workflow

  Major Exception (Requires escalation):
    → Stop processing
    → Create urgent task
    → Notify multiple levels
    → Manual intervention required

Exception Types:
  - Missing required field
  - Invalid field value
  - PO mismatch
  - Duplicate invoice
  - Supplier mismatch
  - Amount discrepancy
```

***

## 完整决策逻辑图

```
INVOICE ARRIVES
│
├─ LEVEL 1: EXCEPTION CHECK
│  │
│  ├─ Has Critical Exception? (Missing PO, Duplicate, etc.)
│  │  │
│  │  ├─ YES → Stop & Escalate
│  │  │        Create urgent task
│  │  │        Notify admin
│  │  │        → END (Exception Handling)
│  │  │
│  │  └─ NO → Continue to Level 2
│
├─ LEVEL 2: DOCUMENT TYPE
│  │
│  ├─ Type = Invoice?
│  │  └─ YES → Continue to Level 3
│  │
│  ├─ Type = Credit Note?
│  │  └─ YES → Branch to Credit Note workflow
│  │           → END (Credit Note Path)
│  │
│  └─ Other Type?
│     └─ YES → Branch to appropriate workflow
│              → END (Other Type Path)
│
├─ LEVEL 3: URGENCY CHECK (for Invoices)
│  │
│  ├─ Urgent Flag = TRUE?
│  │  │
│  │  ├─ YES → Expedited Workflow
│  │  │        Priority: URGENT
│  │  │        Deadline: 1 day
│  │  │        Assign to: Senior Approver
│  │  │        → END (Expedited Path)
│  │  │
│  │  └─ NO → Continue to Level 4
│
├─ LEVEL 4: AMOUNT THRESHOLDS
│  │
│  ├─ Amount < €1,000?
│  │  │
│  │  ├─ YES → AUTO-APPROVE PATH
│  │  │        Set Approval_Type = "AUTO"
│  │  │        Approve immediately
│  │  │        Export to ERP
│  │  │        → END (Auto-Approved)
│  │  │
│  │  └─ NO → Continue
│  │
│  ├─ Amount < €10,000?
│  │  │
│  │  ├─ YES → MANAGER APPROVAL PATH
│  │  │        Create task for Manager
│  │  │        Priority: Medium
│  │  │        Deadline: 3 days
│  │  │        → WAIT for approval
│  │  │           → END (Manager Path)
│  │  │
│  │  └─ NO → Continue
│  │
│  ├─ Amount < €50,000?
│  │  │
│  │  ├─ YES → DIRECTOR APPROVAL PATH
│  │  │        Continue to Level 5 (Supplier Check)
│  │  │
│  │  └─ NO → Continue
│  │
│  └─ Amount ≥ €50,000?
│     │
│     └─ YES → EXECUTIVE APPROVAL PATH
│              Create sequential tasks:
│              - Finance Director
│              - CFO
│              - CEO (if > €100,000)
│              Priority: URGENT
│              Deadline: 1 day each
│              → WAIT for all approvals
│                 → END (Executive Path)
│
├─ LEVEL 5: SUPPLIER ANALYSIS (for €10k-€50k range)
│  │
│  ├─ Supplier Status = "BLOCKED"?
│  │  │
│  │  ├─ YES → BLOCK & ESCALATE
│  │  │        Stop processing
│  │  │        Create urgent task
│  │  │        Notify procurement & finance
│  │  │        → END (Blocked Supplier)
│  │  │
│  │  └─ NO → Continue
│  │
│  ├─ Supplier Age < 180 days (New)?
│  │  │
│  │  ├─ YES → DUAL APPROVAL REQUIRED
│  │  │        Task 1: Director (2 days)
│  │  │        → WAIT for Task 1
│  │  │           IF Task 1 Approved:
│  │  │             Task 2: CFO (2 days)
│  │  │             → WAIT for Task 2
│  │  │                → END (Dual Approved)
│  │  │           IF Task 1 Rejected:
│  │  │             → END (Rejected at Level 1)
│  │  │
│  │  └─ NO → Continue
│  │
│  ├─ Supplier Risk Rating = "HIGH"?
│  │  │
│  │  ├─ YES → ENHANCED APPROVAL
│  │  │        Additional fraud checks
│  │  │        Director approval required
│  │  │        Extended deadline
│  │  │        → END (Enhanced Path)
│  │  │
│  │  └─ NO → STANDARD DIRECTOR APPROVAL
│  │           Create task for Director
│  │           Priority: High
│  │           Deadline: 2 days
│  │           → WAIT for approval
│  │              → END (Standard High-Value)
│  │
│  └─ [Supplier analysis complete]
│
└─ [All decision levels processed]
```

***

## 配置最佳实践

### 1. 保持逻辑清晰且易于维护

✅ **良好示例：**

```
IF Amount > 10000:
  → High value path
ELSE:
  → Standard path
```

❌ **不良示例（过于复杂）：**

```
IF (Amount > 10000 AND (Supplier = "A" OR Supplier = "B") AND NOT (Status = "X" OR Status = "Y") AND Department IN [1,2,3]):
  → Complex path
```

**更好的做法：拆分为多个步骤：**

```
Step 1: IF Amount > 10000: Continue, ELSE: Standard path
Step 2: IF Supplier in allowed list: Continue, ELSE: Review
Step 3: IF Status valid: Continue, ELSE: Reject
Step 4: IF Department authorized: Approve, ELSE: Escalate
```

***

### 2. 记录决策逻辑

**务必包含：**

* 每个决策点的用途
* 所实施的业务规则
* 预期结果
* 异常处理

**文档示例：**

```
Decision Point: Amount Threshold Check
Business Rule: BR-INV-001 (Invoice Approval Matrix)
Purpose: Route invoices based on amount thresholds per company policy
Thresholds:
  < €1,000: Auto-approve (CFO approved threshold)
  €1,000-€10,000: Manager approval (Delegation matrix)
  > €10,000: Director approval (Signature authority)
Exceptions: Urgent invoices skip to highest level
Updated: 2025-10-23
Owner: Finance Department
```

***

### 3. 测试所有路径

**测试矩阵：**

| 测试用例 | 金额   | 类型        | 供应商 | 预期路径         | 状态 |
| -------- | ------ | ----------- | ------ | ---------------- | ---- |
| TC1      | €500   | 发票        | 现有   | 自动审批         | ✅    |
| TC2      | €5,000 | 发票        | 现有   | 经理             | ✅    |
| TC3      | €15,000 | 发票       | 新供应商 | 总监+CFO         | ✅    |
| TC4      | €60,000 | 发票       | 现有   | 高管             | ✅    |
| TC5      | €2,000 | 贷项通知单  | 现有   | 贷项工作流       | ✅    |
| TC6      | €100,000 | 发票     | 已阻止 | 停止并升级       | ✅    |

***

### 4. 监控决策指标

**跟踪：**

* 各决策路径的分布情况
* 自动审批率
* 人工审核率
* 各路径的平均处理时间
* 异常率
* 路径使用率

**指标示例：**

```
Month: October 2025
Total Invoices: 1,250

Decision Path Distribution:
- Auto-approved (< €1k): 680 (54%)
- Manager path (€1k-€10k): 420 (34%)
- Director path (€10k-€50k): 120 (10%)
- Executive path (> €50k): 30 (2%)

Processing Time:
- Auto-approve: < 1 minute
- Manager path: 2.5 days average
- Director path: 1.8 days average
- Executive path: 3.2 days average

Exceptions: 15 (1.2%)
```

***

## 相关模式

### 可配合使用的模式：

* [**任务管理模式**](task-management-pattern.md) - 根据决策创建任务
* [**API 集成模式**](api-integration-pattern.md) - 获取决策所需的数据
* [**采购订单匹配模式**](po-matching-pattern.md) - 在决策中使用采购订单匹配结果
* [**数据转换模式**](data-transformation-pattern.md) - 在决策前转换数据

***

## 相关指南

### 前置条件

* [条件卡片完整指南](../condition-cards-complete-guide.md) - 所有条件卡片
* [字段操作指南](../field-manipulation-guide.md) - 字段操作
* [分配用户指南](../assignment-user-guide.md) - 路由逻辑

### 相关卡片

* **CONDITION\_DOC\_FIELD\_AMOUNT** - [条件卡片指南](../condition-cards-complete-guide.md)
* **CONDITION\_DOC\_TYPE\_IS\_ISNOT** - [条件卡片指南](../condition-cards-complete-guide.md#condition-doc-type-is-isnot)
* **CONDITION\_SUPPLIER\_STATUS\_IS\_ISNOT** - [条件卡片指南](../condition-cards-complete-guide.md#condition-supplier-status-is-isnot)
* **ACTION\_ASSIGN\_TO\_USER** - [分配指南](../assignment-user-guide.md)
* **tasks\_create** - [任务分配指南](../task-assignment-guide.md)

### 后续步骤

* 创建任务：[任务管理模式](task-management-pattern.md)
* 添加复杂匹配：[采购订单匹配模式](po-matching-pattern.md)
* 集成 API：[API 集成模式](api-integration-pattern.md)

***

**模式版本：**1.0 **最后更新：**2025 年 10 月 23 日 **难度：**中等 **预计时间：**30-45 分钟 **成功率：**高
