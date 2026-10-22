# 文件分配和用户卡

## 文件分配和用户卡 - 完整指南

**涵盖：** 13张分配和用户相关卡

***

此页面上的卡片位于工作流程生成器的 **则** 组中 — 一旦“何时/与”条件匹配，就会运行的操作：

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-zh.png" alt="包含“当”“且”和“则”卡片的未保存示例。执行前请配置所有占位字段。 此版本界面的部分标签尚未翻译或翻译不准确。本页说明使用正确术语；图片保留了实际界面。"><figcaption><p>包含“当”“且”和“则”卡片的未保存示例。执行前请配置所有占位字段。 此版本界面的部分标签尚未翻译或翻译不准确。本页说明使用正确术语；图片保留了实际界面。</p></figcaption></figure>

***

### 📌 版本信息

**多版本卡：**DOC\_USER\_ASSIGN（v2最新，v3已弃用），DOC\_GROUP\_ASSIGN（v2最新，v3已弃用），OC\_ASSIGN\_DOC（v2）

**重要：** v3 版本添加了决策树支持，但现已弃用 **建议：** DOC\_USER\_ASSIGN 和 DOC\_GROUP\_ASSIGN 使用 v2

📖【完整版本历史](../release.md) | [卡牌版本和行为](card-versions-guide.md)

***

## 基本文档分配

### 卡：DOC\_USER\_ASSIGN / 将文档分配给用户

#### 目的

将文档分配给特定人员以执行其操作

#### 何时使用

* 文件需要专人审核
* 移交给个别团队成员
* 问责追踪
* 将工作分配给指定人员

#### 它是如何运作的

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

#### 注意事项

赋值的意思是：

* 该人的文档显示为“已分配给我”
* 那个人有责任
* 其他人仍然可以查看文档（但不是分配给他们的）
* 每个文档一次分配一项作业

***

### 卡：DOC\_GROUP\_ASSIGN / 将文档分配给组

#### 目的

将文档分配给一个组（所有成员都将其视为已分配给他们）

#### 何时使用

* 团队而非个人的文档
* 多人即可处理
* 共同责任
* 团队工作量分配

#### 它是如何运作的

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

#### 差异

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

### 卡牌：ACTION\_ASSIGN\_DOC\_BASED\_ON\_DECISION\_TABLE

#### 目的

根据决策表逻辑分配文档

#### 何时使用

* 不同的供应商需要不同的处理程序
* 根据金额分配
* 复杂的路由逻辑
* 多种分配条件

#### 它是如何运作的

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

#### 示例：基于金额的分配

```
Invoice: €2000 from ABC Corp

Decision Table checks:
  Is amount > €10000? NO
  Is amount > €5000? NO
  Is amount > €1000? YES

Result: Assign to: Finance Manager
```

#### 示例：基于供应商的分配

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

### 卡牌：ACTION\_ASSIGN\_DOC\_DECISION\_TABLE\_SEQUENTIAL

#### 目的

根据具有优先级的决策表按顺序分配文档

#### 何时使用

* 多次连续批准
* 不同层次的人不同
* 基于金额的审批链
* 升级路径

#### 它是如何运作的

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

#### 优先权制度

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

### 卡牌：ACTION\_ASSIGN\_DOC\_TO\_USER\_SEQUENTIAL

#### 目的

将文档分配给具有顺序优先级的用户

#### 何时使用

* 文件需要特定人员
* 清晰的顺序处理
* 带顺序的单一作业

#### 它是如何运作的

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

### 卡牌：ACTION\_ASSIGN\_DOC\_TO\_GROUP\_SEQUENTIAL

#### 目的

将文档按顺序分配给组

#### 何时使用

* 多个团体批准
* 每个阶段不同部门
* 基于团队的顺序处理

#### 它是如何运作的

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

### 卡牌：ACTION\_ASSIGN\_DOC\_TO\_FACILITY\_GROUP

<!-- workflow-facility-example-direct-20261022 -->

此工作流操作根据文档所匹配采购订单的地点，将文档分配给相应组。在版本 2 中，`group_name` 是用于搜索组名的文本片段。

示例：合成文档匹配采购订单 `DEMO-PO-100`，该订单的 `location_id=BERLIN`。已配置的组为 `Receiving BERLIN` 和 `Receiving MUNICH`。将 `group_name` 设置为 `Receiving`。组名必须同时包含该文本片段和采购订单的地点标识；匹配不区分大小写。

预期结果：如果文档状态允许分配，文档会直接分配给 `Receiving BERLIN`。没有匹配的采购订单或组时，不会成功完成分配；请检查工作流日志。避免使用含义不明确的组名：如果有多个组匹配，此卡不保证固定的选择顺序。

这只是示例配置，未执行工作流。

***

### 卡牌：ACTION\_ASSIGN\_DOC\_TO\_FACILITY\_GROUP\_SEQUENTIAL

<!-- workflow-facility-example-sequential-20261022 -->

此工作流操作将匹配的地点组按配置的优先级加入顺序分配队列。它并不表示货物在工厂或仓库之间流转。

示例：使用上文中的同一合成采购订单、地点和组。设置 `group_name=Receiving` 和优先级 `value=10`。版本 2 从匹配的采购订单读取地点，并找到 `Receiving BERLIN`。

预期结果：该组的分配请求以优先级 `10` 加入队列。如果有多个组匹配，它们会获得相同的优先级；组名并不决定处理顺序。请分别检查队列和后续审批。没有匹配项时，不会创建成功的分配。

这只是示例配置，未执行工作流。

***

### 卡牌：ACTION\_ASSIGN\_DOC\_TO\_PROCUREMENT\_GROUP

#### 目的

将文件分配给采购部门

#### 何时使用

* 采购团队处理
* 供应商相关工作
* 采购订单相关

#### 示例

```
Vendor evaluation document
    ↓
Assign to: Procurement Group
    ↓
Procurement team evaluates vendor
```

***

### 卡牌：ACTION\_ASSIGN\_DOC\_TO\_PROCUREMENT\_GROUP\_SEQUENTIAL

#### 目的

采购中的顺序分配

#### 何时使用

* 多步骤采购流程
* 采购审批链

#### 示例

```
Purchase Requisition:

Step 1: Buyer (Creates PO)
Step 2: Approver (Reviews)
Step 3: Director (Final sign-off)

Each step in sequence
```

***

### 卡：ACTION\_CHANGE\_DOC\_SUBORG / 更改文档子组织

#### 目的

将文档分配给不同的子组织

#### 何时使用

* 选择了错误的组织
* 需要调到正确的部门
* 组织架构调整

#### 它是如何运作的

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

### 卡牌：ACTION\_CHANGE\_DOC\_SUBORG\_BY\_FIELD\_TEXT

#### 目的

根据文档字段值更改子组织

#### 何时使用

* 子组织存储在字段中
* 将文档位置与字段匹配
* 自动组织分配

#### 它是如何运作的

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

### 卡牌：ACTION\_ASSIGN\_USER\_FROM\_FIELD\_WITH\_FALLBACK

#### 目的

从字段将文档分配给用户，如果未找到用户则进行回退

#### 何时使用

* 存储在文档字段中的用户名
* 系统中可能不存在
* 如果用户不可用则需要备份

#### 它是如何运作的

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

### 卡牌：ACTION\_ASSIGN\_USER\_TO\_SUPPLIER

#### 目的

将文档分配给管理该供应商的用户

#### 何时使用

* 用户链接到供应商
* 供应商客户经理
* 供应商关系所有者

#### 它是如何运作的

```
Document Supplier: ABC Corp
    ↓
System checks: Who manages ABC Corp?
    ↓
Assign to: John Smith (ABC Corp Account Manager)
```

***

## 分配决策树

### 决策表示例 1：基于金额

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

### 决策表示例 2：基于供应商

```
Supplier Type = "Preferred"
  → Assign to: Account Manager

Supplier Type = "New"
  → Assign to: Procurement Manager

Supplier Type = "Problem"
  → Assign to: Procurement Director
```

### 决策表示例 3：基于文档类型

```
Document Type = "Invoice"
  → Assign to: Accounts Payable Team

Document Type = "Credit Memo"
  → Assign to: Finance Manager

Document Type = "PO"
  → Assign to: Procurement Team
```

***

## 分配工作流程示例

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

### 示例 2：顺序批准

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

### 示例 3：基于金额的路由

```
Invoice: €50,000
    ↓
Decision Table: Amount > €20k?
    ↓
YES → Assign to: CFO
    ↓
CFO approves directly
```

### 示例 4：基于设施

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

## 作业最佳实践

✅ **做：**

* 保持决策表简单
* 使用示例测试路由逻辑
* 确保所有路径都通向某个地方
* 为丢失的用户提供后备方案
* 记录路由决策

❌**不要：**

* 创建循环分配 (A→B→A)
* 分配给不存在的用户（无回退）
* 使路由过于复杂
* 忘记测试路由
* 分配给无法联系的人

***

## 故障排除分配

### “文档未分配”

**原因：**条件不满足或用户不存在

**解：**

* 检查条件是否为真
* 验证系统中是否存在用户
* 检查后备设置
* 检查决策表逻辑

### “分配了错误的人”

**原因：**决策表或路由逻辑不正确

**解：**

* 测试决策表
* 检查条件
* 验证用户映射
* 查看字段值

### “作业似乎跳过了某人”

**原因：**顺序错误

**解：**

* 检查优先级号码
* 验证序列是否正确
* 样品测试
* 查看决策表排序

***

## 作业卡比较

| 卡                                                    | 分配给               | 航线类型  | 使用案例                   |
| ------------------------------------------------------- | ------------------------ | ----------- | -------------------------- |
| DOC\_USER\_ASSIGN                                       | 个人               | 直接      | 简单的分配          |
| DOC\_GROUP\_ASSIGN                                      | 集团                    | 直接      | 团队分配            |
| ACTION\_ASSIGN\_DOC\_BASED\_ON\_DECISION\_TABLE         | 决策结果          | 有条件的 | 复杂的路由            |
| ACTION\_ASSIGN\_DOC\_DECISION\_TABLE\_SEQUENTIAL        | 多个（顺序）    | 有条件的 | 审批链             |
| ACTION\_ASSIGN\_DOC\_TO\_USER\_SEQUENTIAL               | 用户（顺序）        | 已订购     | 连续的用户步骤      |
| ACTION\_ASSIGN\_DOC\_TO\_GROUP\_SEQUENTIAL              | 组（顺序）      | 已订购     | 连续的组步骤     |
| ACTION\_ASSIGN\_DOC\_TO\_FACILITY\_GROUP                | 设施组           | 直接      | 特定设施          |
| ACTION\_ASSIGN\_DOC\_TO\_FACILITY\_GROUP\_SEQUENTIAL    | 设施（顺序）  | 已订购     | 多功能设施             |
| ACTION\_ASSIGN\_DOC\_TO\_PROCUREMENT\_GROUP             | 采购              | 直接      | 采购工作流程       |
| ACTION\_ASSIGN\_DOC\_TO\_PROCUREMENT\_GROUP\_SEQUENTIAL | 采购（顺序） | 已订购     | 采购审批链 |
| ACTION\_CHANGE\_DOC\_SUBORG                             | 下属组织         | 直接      | 部门变动          |
| ACTION\_CHANGE\_DOC\_SUBORG\_BY\_FIELD\_TEXT            | 按领域划分的子组织         | 有条件的 | 实地作业     |
| ACTION\_ASSIGN\_USER\_FROM\_FIELD\_WITH\_FALLBACK       | 现场/后备           | 有条件的 | 动态用户分配    |

***

## 相关卡牌

* **ACTION\_CREATE\_TASK\_FOR\_USER** - 将任务分配给同一个人
* **ACTION\_SEND\_EMAIL** - 通知指定人员
* **CONDITION\_USER\_IS\_ISNOT** - 检查是否分配了正确的人员
* **CONDITION\_GROUP\_IS\_ISNOT** - 检查是否分配了正确的组

<!-- workflow-card-example-action_assign_doc_to_first_user_and_tasks-20261021 -->

### 将文档分配给第一个返回的用户并创建任务

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-card-extra-ae5af7c6bdc2-zh.png" alt="所示版本的卡片字段。占位字段尚未配置。 此版本界面的部分标签尚未翻译或翻译不准确。本页说明使用正确术语；图片保留了实际界面。" width="563"><figcaption><p>所示版本的卡片字段。占位字段尚未配置。 此版本界面的部分标签尚未翻译或翻译不准确。本页说明使用正确术语；图片保留了实际界面。</p></figcaption></figure>

`ACTION_ASSIGN_DOC_TO_FIRST_USER_AND_TASKS`·版本2

使用演示决策表规则按顺序返回配置的用户 `Demo Reviewer A` 和 `Demo Reviewer B`。选择任务/通知选项、标题`Review invoice`、描述、优先级和电子邮件首选项。第一个返回的用户是文档分配目标，配置的任务/通知以返回的用户为目标。检查两个输出；空返回不能被视为赋值。

<!-- workflow-card-example-action_assign_supplier_user_first_return_of_dt-20261021 -->

### 将第一个返回的用户分配给供应商

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-card-extra-0c3d87c8a5e7-zh.png" alt="所示版本的卡片字段。占位字段尚未配置。 此版本界面的部分标签尚未翻译或翻译不准确。本页说明使用正确术语；图片保留了实际界面。" width="563"><figcaption><p>所示版本的卡片字段。占位字段尚未配置。 此版本界面的部分标签尚未翻译或翻译不准确。本页说明使用正确术语；图片保留了实际界面。</p></figcaption></figure>

`ACTION_ASSIGN_SUPPLIER_USER_FIRST_RETURN_OF_DT`·版本2

使用注册的演示供应商和第一个用户结果为`Demo Supplier Owner`的决策表规则。选择决策表，并根据需要选择电子邮件模板。供应商-用户关联使用第一个返回的用户；它与分配文档的操作不同。单独验证供应商结果并测试空规则返回。
