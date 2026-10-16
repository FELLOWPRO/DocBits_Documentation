# 文档分配与用户卡片

## 文档分配与用户卡片 - 完整指南

**涵盖：**13 个分配和用户相关卡片

***

本页中的卡片位于 Workflow Builder 的 **Then** 组中——当 When/And 条件匹配时执行的操作：

<figure><img src="../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder 画布，包含 When、And 和 Then 卡片组"><figcaption><p>通过 <strong>Add Card</strong> 将分配和用户卡片添加到 <strong>Then</strong> 组。</p></figcaption></figure>

***

### 📌 版本信息

**多版本卡片：** DOC\_USER\_ASSIGN（最新版本 v2，v3 已弃用）、DOC\_GROUP\_ASSIGN（最新版本 v2，v3 已弃用）、OC\_ASSIGN\_DOC（v2）

**重要：**v3 版本增加了决策树支持，但现已弃用。**建议：**DOC\_USER\_ASSIGN 和 DOC\_GROUP\_ASSIGN 均使用 v2

📖 [完整版本历史](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/administration-and-setup/changelog/release.md#-assignment--routing-cards) | [卡片版本数据库](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/DocFlow/docs/card_version.md)

***

## 基本文档分配

### 卡片：DOC\_USER\_ASSIGN / 将文档分配给用户

#### 用途

将文档分配给特定人员，由其处理

#### 适用场景

* 需要由特定人员审核文档
* 将工作移交给某位团队成员
* 跟踪责任归属
* 将工作分配给指定人员

#### 工作方式

```
Document is "assigned to" = John Smith
Only John can see it as assigned to him
John is responsible for this document
```

#### 示例

```
Invoice arrives
    ↓
Assign Document to: John Smith (Finance Manager)
    ↓
Only John sees "Assigned to Me"
John must take action on it
```

#### 参数

```
User: [Select which person]
```

#### 注意

分配意味着：

* 对该人员而言，文档会显示为“分配给我”
* 该人员负责处理文档
* 其他人仍可查看文档（但文档不会显示为分配给他们）
* 每份文档同一时间只能有一个分配对象

***

### 卡片：DOC\_GROUP\_ASSIGN / 将文档分配给组

#### 用途

将文档分配给一个组（所有成员都会看到文档已分配给他们）

#### 适用场景

* 文档由团队处理，而非某个个人
* 多人都可以处理
* 共同承担责任
* 在团队之间分配工作量

#### 工作方式

```
Document is "assigned to" = Finance Team (10 people)
All 10 team members see "Assigned to My Group"
Any team member can take action
```

#### 示例

```
New vendor invoice
    ↓
Assign Document to: Procurement Team
    ↓
All procurement team members see it
First available person handles it
```

#### 参数

```
Group: [Select which group]
```

#### 区别

```
Individual Assignment:
- One person responsible
- That person sees "Assigned to Me"
- Others don't see assignment

Group Assignment:
- Team responsible
- All members see "Assigned to My Group"
- Anyone can claim/process
```

***

### 卡片：ACTION\_ASSIGN\_DOC\_BASED\_ON\_DECISION\_TABLE

#### 用途

根据决策表逻辑分配文档

#### 适用场景

* 不同供应商需要由不同人员处理
* 根据金额进行分配
* 复杂的路由逻辑
* 根据多个条件进行分配

#### 工作方式

```
Decision Table Logic:
  If Supplier = "ABC Corp" → Assign to: Procurement Team
  If Supplier = "XYZ Inc" → Assign to: Direct Manager
  If Amount > €10000 → Assign to: Finance Director

Document arrives
    ↓
Check: Which condition matches?
    ↓
Assign accordingly
```

#### 示例：按金额分配

```
Invoice: €2000 from ABC Corp

Decision Table checks:
  Is amount > €10000? NO
  Is amount > €5000? NO
  Is amount > €1000? YES

Result: Assign to: Finance Manager
```

#### 示例：按供应商分配

```
Invoice from: Preferred Supplier

Decision Table:
  If preferred supplier → Finance Team
  If new supplier → Procurement Manager
  If blacklisted → Director Review

Result: Assign to: Finance Team
```

#### 参数

```
Decision Table: [Select decision table]
(Decision table contains assignment logic)
```

***

### 卡片：ACTION\_ASSIGN\_DOC\_DECISION\_TABLE\_SEQUENTIAL

#### 用途

根据带有优先级的决策表按顺序分配文档

#### 适用场景

* 多个连续审批
* 不同级别由不同人员处理
* 根据金额设置审批链
* 设置升级路径

#### 工作方式

```
First Decision: Who approves first?
    ↓
Assign to: Person 1
    ↓
Person 1 approves
    ↓
Second Decision: Who approves next?
    ↓
Assign to: Person 2
    ↓
Person 2 approves (final)
    ↓
Document Complete
```

#### 优先级系统

```
Priority 1: First assignment
Priority 2: Second assignment
Priority 3: Third assignment
(etc.)

Each must complete before next begins
```

#### 示例：多级审批

```
Invoice: €50,000

Decision Table:
  €1k-€5k → Assign to: Finance Manager (Priority 1)
  €5k-€20k → Then: Assign to: Finance Director (Priority 2)
  €20k+ → Then: Assign to: CFO (Priority 3)

Invoice Flow:
1. Finance Manager reviews → approves
2. Finance Director reviews → approves
3. CFO reviews → approves final

Each step depends on previous completion
```

#### 参数

```
Decision Table: [Select]
Priority Order: [Determined by decision table]
```

***

### 卡片：ACTION\_ASSIGN\_DOC\_TO\_USER\_SEQUENTIAL

#### 用途

按顺序优先级将文档分配给用户

#### 适用场景

* 文档需要由特定人员处理
* 需要明确的顺序处理流程
* 按顺序进行单次分配

#### 工作方式

```
Assign Document to: User A (Priority 1)
    ↓
User A processes
    ↓
Then: Assign to User B (Priority 2)
    ↓
User B processes
```

#### 示例

```
Invoice processing:
1. Assign to: Accounts Payable Clerk
2. Then: Assign to: Finance Manager
3. Then: Assign to: Director

Each person has their turn
```

***

### 卡片：ACTION\_ASSIGN\_DOC\_TO\_GROUP\_SEQUENTIAL

#### 用途

按顺序将文档分配给多个组

#### 适用场景

* 需要多个组审批
* 每个阶段由不同部门处理
* 按顺序进行团队处理

#### 工作方式

```
Step 1: Assign to Group A (Quality Team)
        Quality verifies
    ↓
Step 2: Assign to Group B (Finance Team)
        Finance reviews
    ↓
Step 3: Assign to Group C (Procurement)
        Procurement approves
```

#### 示例

```
New Supplier Onboarding:

Step 1: Quality Team
  - Evaluate supplier capability
  - Check certifications

Step 2: Finance Team
  - Check payment terms
  - Verify pricing

Step 3: Procurement Team
  - Approve supplier
  - Set up in system

Document passes through all three
```

***

### 卡片：ACTION\_ASSIGN\_DOC\_TO\_FACILITY\_GROUP

#### 用途

将文档分配给特定设施组

#### 适用场景

* 文档对应特定仓库或设施
* 基于设施开展运营
* 按地点进行处理

#### 示例

```
Shipment notification

Assign to: Berlin Warehouse Team
    ↓
Berlin warehouse processes shipment
    ↓
Or

Assign to: Munich Warehouse Team
    ↓
Munich warehouse processes shipment
```

***

### 卡片：ACTION\_ASSIGN\_DOC\_TO\_FACILITY\_GROUP\_SEQUENTIAL

#### 用途

按顺序在多个设施之间进行分配

#### 适用场景

* 多地点处理
* 货物在多个设施之间流转
* 基于地点的工作流

#### 示例

```
Manufacturing Order:

Step 1: Factory A (Manufacturing) - Build product
Step 2: Quality Center (Testing) - Test product
Step 3: Distribution Center (Packing) - Package
Step 4: Warehouse (Storage) - Store

Document/shipment passes through each
```

***

### 卡片：ACTION\_ASSIGN\_DOC\_TO\_PROCUREMENT\_GROUP

#### 用途

将文档分配给采购部门

#### 适用场景

* 由采购团队处理
* 与供应商相关的工作
* 与采购订单相关的工作

#### 示例

```
Vendor evaluation document
    ↓
Assign to: Procurement Group
    ↓
Procurement team evaluates vendor
```

***

### 卡片：ACTION\_ASSIGN\_DOC\_TO\_PROCUREMENT\_GROUP\_SEQUENTIAL

#### 用途

在采购部门内按顺序分配

#### 适用场景

* 多步骤采购流程
* 采购部门的审批链

#### 示例

```
Purchase Requisition:

Step 1: Buyer (Creates PO)
Step 2: Approver (Reviews)
Step 3: Director (Final sign-off)

Each step in sequence
```

***

### 卡片：ACTION\_CHANGE\_DOC\_SUBORG / 更改文档子组织

#### 用途

将文档分配给其他子组织

#### 适用场景

* 选错组织
* 需要将文档转到正确的部门
* 组织架构调整

#### 工作方式

```
Current Sub-Org: Finance Department
    ↓
Change to: Accounting Department
    ↓
Document now belongs to Accounting
```

#### 示例

```
Document for: Berlin Office
    ↓
Realize should be: Munich Office
    ↓
Change Sub-Organization to: Munich Office
```

***

### 卡片：ACTION\_CHANGE\_DOC\_SUBORG\_BY\_FIELD\_TEXT

#### 用途

根据文档字段值更改子组织

#### 适用场景

* 字段中存储了子组织信息
* 根据字段将文档地点进行匹配
* 自动分配组织

#### 工作方式

```
Document Field: "Delivery_Location" = "Berlin"
    ↓
Decision Table:
  If location = "Berlin" → Assign to: Berlin Sub-Org
  If location = "Munich" → Assign to: Munich Sub-Org

    ↓
Document assigned to: Berlin Sub-Org
```

#### 示例

```
Invoice field: "Cost Center: CC-Berlin-001"
    ↓
System recognizes: Berlin location
    ↓
Change document to: Berlin Sub-Organization
```

***

### 卡片：ACTION\_ASSIGN\_USER\_FROM\_FIELD\_WITH\_FALLBACK

#### 用途

根据字段将文档分配给用户；如果找不到该用户，则使用备用用户

#### 适用场景

* 文档字段中存储了用户名
* 该用户可能不存在于系统中
* 用户不可用时需要备用人员

#### 工作方式

```
Document Field: "Approver: John Smith"
    ↓
Try to assign to: John Smith
    ↓
If John doesn't exist:
    ↓
Use Fallback: Sarah Johnson (Manager)
    ↓
Document assigned to: Sarah Johnson
```

#### 参数

```
Source Field: [Field containing user name]
Fallback User: [If source user not found]
```

#### 示例

```
Invoice has field: "Contact Person: Mike Johnson"

Try to assign to: Mike Johnson
    ↓
If Mike not in system:
    ↓
Fallback to: Finance Manager (Robert)
```

***

### 卡片：ACTION\_ASSIGN\_USER\_TO\_SUPPLIER

#### 用途

将文档分配给负责该供应商的用户

#### 适用场景

* 用户与供应商关联
* 供应商客户经理
* 供应商关系负责人

#### 工作方式

```
Document Supplier: ABC Corp
    ↓
System checks: Who manages ABC Corp?
    ↓
Assign to: John Smith (ABC Corp Account Manager)
```

***

## 分配决策树

### 决策表示例 1：按金额

```
Amount ≤ €1000
  → Assign to: Finance Team

Amount €1000-€5000
  → Assign to: Finance Manager

Amount €5000-€20000
  → Assign to: Finance Director

Amount > €20000
  → Assign to: CFO
```

### 决策表示例 2：按供应商

```
Supplier Type = "Preferred"
  → Assign to: Account Manager

Supplier Type = "New"
  → Assign to: Procurement Manager

Supplier Type = "Problem"
  → Assign to: Procurement Director
```

### 决策表示例 3：按文档类型

```
Document Type = "Invoice"
  → Assign to: Accounts Payable Team

Document Type = "Credit Memo"
  → Assign to: Finance Manager

Document Type = "PO"
  → Assign to: Procurement Team
```

***

## 分配工作流示例

### 示例 1：简单路由

```
Document Arrives
    ↓
Check: Supplier = "ABC Corp"? YES
    ↓
Assign to: John Smith
(John handles ABC Corp)
    ↓
John reviews and approves
```

### 示例 2：顺序审批

```
Document Arrives
    ↓
Assign to: Finance Manager (Step 1)
    ↓
Manager reviews
    ↓
Passes to: Finance Director (Step 2)
    ↓
Director reviews
    ↓
Passes to: CFO (Step 3)
    ↓
CFO approves final
```

### 示例 3：按金额路由

```
Invoice: €50,000
    ↓
Decision Table: Amount > €20k?
    ↓
YES → Assign to: CFO
    ↓
CFO approves directly
```

### 示例 4：按设施分配

```
Shipment for: Berlin Office
    ↓
Assign to: Berlin Warehouse Team
    ↓
Then assign to: Berlin Distribution Team
    ↓
Both teams process in sequence
```

***

## 分配最佳实践

✅ **建议：**

* 保持决策表简洁
* 使用样例测试路由逻辑
* 确保所有路径都有去向
* 为找不到用户的情况设置备用用户
* 记录路由决策

❌ **避免：**

* 创建循环分配（A→B→A）
* 分配给不存在的用户（未设置备用用户时）
* 让路由过于复杂
* 忘记测试路由
* 分配给不可用人员

***

## 分配故障排查

### “文档未分配”

**原因：**条件不满足或用户不存在

**解决方案：**

* 检查条件是否为真
* 确认用户存在于系统中
* 检查备用设置
* 查看决策表逻辑

### “分配给了错误的人员”

**原因：**决策表或路由逻辑不正确

**解决方案：**

* 测试决策表
* 检查条件
* 确认用户映射
* 查看字段值

### “分配似乎跳过了某个人”

**原因：**顺序不正确

**解决方案：**

* 检查优先级编号
* 确认顺序正确
* 使用样例进行测试
* 检查决策表的排序

***

## 分配卡片对比

| 卡片                                                    | 分配对象                 | 路由类型  | 使用场景                   |
| ------------------------------------------------------- | ------------------------ | ----------- | -------------------------- |
| DOC\_USER\_ASSIGN                                       | 个人                     | 直接      | 简单分配          |
| DOC\_GROUP\_ASSIGN                                      | 组                       | 直接      | 团队分配            |
| ACTION\_ASSIGN\_DOC\_BASED\_ON\_DECISION\_TABLE         | 决策结果                 | 条件式 | 复杂路由            |
| ACTION\_ASSIGN\_DOC\_DECISION\_TABLE\_SEQUENTIAL        | 多个对象（按顺序）    | 条件式 | 审批链             |
| ACTION\_ASSIGN\_DOC\_TO\_USER\_SEQUENTIAL               | 用户（按顺序）        | 有序     | 用户顺序处理步骤      |
| ACTION\_ASSIGN\_DOC\_TO\_GROUP\_SEQUENTIAL              | 多个组（按顺序）      | 有序     | 组顺序处理步骤     |
| ACTION\_ASSIGN\_DOC\_TO\_FACILITY\_GROUP                | 设施组           | 直接      | 特定设施处理          |
| ACTION\_ASSIGN\_DOC\_TO\_FACILITY\_GROUP\_SEQUENTIAL    | 多个设施（按顺序）  | 有序     | 多设施处理             |
| ACTION\_ASSIGN\_DOC\_TO\_PROCUREMENT\_GROUP             | 采购部门              | 直接      | 采购工作流       |
| ACTION\_ASSIGN\_DOC\_TO\_PROCUREMENT\_GROUP\_SEQUENTIAL | 采购部门（按顺序） | 有序     | 采购审批链 |
| ACTION\_CHANGE\_DOC\_SUBORG                             | 子组织         | 直接      | 部门变更          |
| ACTION\_CHANGE\_DOC\_SUBORG\_BY\_FIELD\_TEXT            | 按字段分配子组织         | 条件式 | 基于字段分配     |
| ACTION\_ASSIGN\_USER\_FROM\_FIELD\_WITH\_FALLBACK       | 字段/备用用户           | 条件式 | 动态用户分配    |

***

## 相关卡片

* **ACTION\_CREATE\_TASK\_FOR\_USER** - 将任务分配给同一人员
* **ACTION\_SEND\_EMAIL** - 通知已分配人员
* **CONDITION\_USER\_IS\_ISNOT** - 检查是否分配给了正确的人员
* **CONDITION\_GROUP\_IS\_ISNOT** - 检查是否分配给了正确的组
