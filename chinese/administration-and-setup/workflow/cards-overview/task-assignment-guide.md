# 任务分配和创建卡

## 任务分配和创建卡 - 完整指南

**涵盖：** 12张任务相关卡片

***

此页面上的任务卡位于工作流生成器的 **则** 组中 — 一旦“何时/与”条件匹配，就会运行的操作：

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-zh.png" alt="包含“当”“且”和“则”卡片的未保存示例。执行前请配置所有占位字段。 此版本界面的部分标签尚未翻译或翻译不准确。本页说明使用正确术语；图片保留了实际界面。"><figcaption><p>包含“当”“且”和“则”卡片的未保存示例。执行前请配置所有占位字段。 此版本界面的部分标签尚未翻译或翻译不准确。本页说明使用正确术语；图片保留了实际界面。</p></figcaption></figure>

***

### 📌 版本信息

**进化最多的卡：**tasks\_create（4个版本，v4最新）**其他多版本卡：**ACTION\_TASK\_FOR\_GROUP（v4），ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP（v3），ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK（v3），ACTION\_DECISION\_TREE\_CREATE\_TASKS（v3）

**主要变化：**

* **v3 → v4 演变：** 删除了决策树方法，添加了通用工作项类型（任务、工单、问题）
* **v2 → v3 迁移：** 添加了决策树支持（现在大部分已弃用）

📖【完整版本历史](../release.md) | [卡牌版本和行为](card-versions-guide.md)

***

### 概述

任务卡为团队成员创建工作分配。当发票需要审批时，您可以自动创建任务并将其分配给合适的人员。

***

## 基本任务创建

### 卡：tasks\_create / 创建任务并分配给用户

#### 目的

创建任务并将其分配给特定人员

#### 何时使用

* 发票需要专人审核
* 需要指定个人的批准
* 移交给特定团队成员

#### 参数

**标题**任务名称/主题

```
Example: "Review Invoice #INV-2025-001 for approval"
```

**描述**有关任务的详细信息

```
Example: "Invoice from Supplier ABC needs review.
Amount: €5000
Deadline: 2025-10-30
Please verify pricing and quality."
```

**优先级**

* 🔴**High**：紧急，立即做
* 🟡 **中**：普通优先级
* 🟢 **低**：可以稍后完成

**分配的用户**谁获得任务

```
Example: John Smith (Finance Manager)
```

**电子邮件通知** 向指定人员发送电子邮件警报？

```
✅ Yes: Person gets email
❌ No: Task only in system
```

#### 示例

```
Condition: "Invoice amount > €10,000"
    ↓
Create Task:
- Title: "High-Value Invoice Review Required"
- Description: "Invoice #INV-2025-789 for €15,000 needs approval"
- Priority: High
- Assigned to: Sarah Johnson (Finance Approver)
- Send Email: Yes
    ↓
Sarah receives task and email notification
```

***

### 卡片：ACTION\_TASK\_FOR\_GROUP / 为小组创建任务

#### 目的

创建任务并将其分配给组（所有成员都可以看到）

#### 何时使用

* 多人可以完成任务
* 团队的任务，而不是个人的任务
* 第一个人应该处理

#### 与个人任务的区别

```
Individual Task:
- Only John sees it
- John must do it
- Others can't see it

Group Task:
- Everyone in group sees it
- Any group member can claim it
- Distributed workload
```

#### 示例工作流程

```
Document arrives
    ↓
Condition: "Is supplier new?"
    ↓
Create Task for Procurement Team:
- Title: "Verify New Supplier Details"
- Description: "Please validate supplier information"
- Priority: Medium
- Group: Procurement Team (10 members)
- Notify: Yes
    ↓
All 10 procurement team members see task
First person available takes it
```

***

### 卡牌：ACTION\_DECISION\_TREE\_CREATE\_TASKS

#### 目的

根据决策表逻辑创建任务

#### 它是如何运作的

```
Decision Table Returns:
  If invoice from Supplier A → Assign to Procurement
  If invoice from Supplier B → Assign to Quality Team
  If invoice from Supplier C → Assign to Finance

Task is automatically created and assigned
based on which condition is true
```

#### 何时使用

* 不同的供应商需要不同的批准
* 基于多种因素的复杂路由
* 根据文档类型不同的团队

#### 示例

```
Document: Invoice from ABC Corp (Supplier A)
    ↓
Decision Table checks: Which supplier?
    ↓
Result: Supplier A → Procurement Team
    ↓
Create and assign task to Procurement Team
```

***

### 卡牌：ACTION\_DECISION\_TREE\_TASKS\_SEQUENTIAL

#### 目的

根据决策表顺序创建任务 任务按优先级顺序一次分配一个

#### 何时使用

* 需要依次获得多个批准
* 工作流程审批链
* 每个人评论然后传递给下一个

#### 它是如何运作的

```
Step 1: Create Task for Procurement Manager
        (Priority 1)
    ↓
Step 2: Procurement Manager approves
    ↓
Step 3: Create Task for Finance Manager
        (Priority 2)
    ↓
Step 4: Finance Manager approves
    ↓
Step 5: Export
```

#### 优先权制度

```
Priority 1 → Assign to: Person A
Priority 2 → Assign to: Person B
Priority 3 → Assign to: Person C

They must complete in order (1→2→3)
```

#### 配置示例

```
Decision Table Returns:
  Level 1: Sarah Johnson (Finance)
  Level 2: Mike Smith (Manager)
  Level 3: Director (for approval)

Task Flow:
1. Sarah reviews → Comments
2. Passes to Mike → He reviews
3. Passes to Director → Final approval
4. All complete → Export
```

***

### 卡牌：ACTION\_CREATE\_TASK\_FOR\_USER\_SEQUENTIAL

#### 目的

将文档分配给一个用户并创建顺序任务

#### 何时使用

* 分配文档并同时创建任务
* 文件需要由特定人员审核
* 跟踪分配和任务创建

#### 它是如何运作的

```
Two things happen:
1. Document is assigned to: Person A
2. Task is created for: Person A

Both in one action
```

#### 示例

```
High-value invoice arrives
    ↓
ACTION_CREATE_TASK_FOR_USER_SEQUENTIAL:
- Assign Document to: Finance Manager
- Create Task: "Review & Approve High Value Invoice"
- Priority: High
    ↓
Document AND task both go to Finance Manager
```

***

### 卡牌：ACTION\_CREATE\_TASK\_FOR\_GROUP\_SEQUENTIAL

#### 目的

将文档分配给组并创建任务

#### 何时使用

* 文件需要群体关注
* 想要跟踪任务创建
* 创建初始任务然后记录分配

#### 示例

```
New supplier evaluation
    ↓
ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL:
- Document assigned to: Supplier Management Group
- Create Task: "Evaluate New Supplier Credentials"
- Assign Task to: Same group
- Priority: Medium
    ↓
Group members see document and task
```

***

## 高级任务创建

### 卡牌：ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP

#### 目的

为特定设施组创建任务

#### 何时使用

* 仓库/设施团队的任务
* 设施特定操作
* 物理位置很重要

#### 示例

```
Document: Shipment notification
    ↓
Create Task for Facility Group:
- Group: Berlin Warehouse Team
- Task: "Prepare items for shipment"
- Items: From document
    ↓
Berlin warehouse team gets task
```

***

### 卡牌：ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP\_SEQUENTIAL

#### 目的

跨设施的顺序任务分配

#### 何时使用

* 多设施运营
* 任务从一个设施传递到另一个设施
* 顺序设施处理

#### 它是如何运作的

```
Factory A (Step 1): Production
    ↓
Quality Check (Step 2): Verification
    ↓
Warehouse (Step 3): Packaging
    ↓
Shipping (Step 4): Dispatch
```

#### 示例

```
Manufacturing Document
    ↓
Create Sequential Tasks:
- Task 1: Factory A (Manufacturing) - Priority 1
- Task 2: Quality Team (Testing) - Priority 2
- Task 3: Warehouse (Packing) - Priority 3
- Task 4: Shipping (Dispatch) - Priority 4
    ↓
Each team completes → Passes to next
```

***

### 卡牌：ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP

#### 目的

为采购部门创建任务

#### 何时使用

* 采购团队的任务
* 供应商管理任务
* 采购相关工作

#### 示例

```
Supplier status change notification
    ↓
Create Task for Procurement Group:
- Task: "Update supplier records"
- Supplier: ABC Corp
- Action: Change status to 'On Hold'
- Priority: High
    ↓
Procurement team is notified
```

***

### 卡牌：ACTION\_ASSIGN\_TASK\_PROCUREMENT\_GROUP\_SEQUENTIAL

#### 目的

采购中的顺序任务路由

#### 何时使用

* 多步骤采购流程
* 采购审批链
* 升级路径

#### 示例

```
Purchase Requisition received
    ↓
Step 1: Buyer verifies (Priority 1)
    ↓
Step 2: Approver approves (Priority 2)
    ↓
Step 3: Director signs off (Priority 3)
    ↓
All sign-offs complete → Release to supplier
```

***

### 卡牌：ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK

#### 目的

从文档字段获取用户，分配任务如果找不到用户，则使用后备用户

#### 何时使用

* 用户存储在文档字段中
* 文件规定了谁应该审查
* 如果指定用户不可用，请有备份人员

#### 它是如何运作的

```
Document has field: "Approver Name: John Smith"

Card checks: Is John in system?
    If YES → Assign task to John
    If NO → Assign to Fallback User (Sarah)
```

#### 示例

```
Invoice field: "Contact: Mike Johnson"

Try to assign task to Mike Johnson
    ↓
If Mike doesn't exist in system:
    ↓
Use Fallback: Team Lead (Robert Brown)
```

#### 参数

```
- Field to Read: "Approver Name"
- Fallback User: Robert Brown
- Task Details: Title, Description, Priority
```

***

## 常用任务参数

所有任务卡都使用以下参数：

#### 标题

```
Good: "Review Invoice #INV-12345 - €5000 - Supplier ABC"
Bad: "Approve something"
```

#### 描述

```
Should include:
✅ What to do
✅ Deadline
✅ Any special requirements
✅ Who to contact
✅ Link to document
```

#### 优先级

```
🔴 HIGH
   - Action needed within hours
   - Blocks other processes
   - Example: Supply missing, urgent approval

🟡 MEDIUM
   - Standard processing
   - Normal timeline
   - Example: Regular invoice review

🟢 LOW
   - Can wait days/weeks
   - Non-urgent
   - Example: Archive old documents
```

#### 截止日期（如果有）

```
When should task be completed by?
Example: 2025-10-30 (5 days from now)
```

***

## 任务工作流程场景

### 场景一：简单审批

```
Invoice Arrives (€2000)
    ↓
Condition: Amount between €1000-€5000?
    ↓
YES: Create Task for Finance Manager
    ↓
Finance Manager reviews and approves
```

### 场景二：多级审批

```
Invoice Arrives (€50,000 - High Value)
    ↓
Create Sequential Tasks:
1. Finance Team (Initial review)
2. Finance Manager (Approval)
3. Director (Final sign-off)
    ↓
Each level completes → Next begins
```

### 场景 3：并行任务

```
Invoice Arrives (From New Supplier)
    ↓
Create Task 1: Quality Team (verify supplier)
Create Task 2: Finance Team (check prices)
Create Task 3: Procurement (check contract)
    ↓
All teams work simultaneously
All must complete before proceeding
```

### 场景 4：条件路由

```
Invoice Arrives
    ↓
Decision Table:
  If amount > €10k → Assign to Director
  If amount €1k-€10k → Assign to Manager
  If amount < €1k → Assign to Team Lead
    ↓
Task created for correct person
```

***

## 任务分配最佳实践

✅ **做：**

* 在任务标题中包含具体详细信息
* 设置适当的优先级
* 设定切合实际的截止日期
* 通知分配对象
* 包含文档链接
* 使用清晰、可操作的描述

❌**不要：**

* 创建模糊的任务标题（“查看此”）
* 将所有内容设置为高优先级
* 忘记通知指定人员
* 为同一工作创建多个任务
* 分配给无法联系的人

***

## 故障排除任务

### “任务未分配给任何人”

**原因：** 用户不存在或组为空

**解：**

* 验证用户名拼写
* 检查用户在系统中是否处于活动状态
* 验证组有成员
* 如果需要，使用后备

### “有人说他们没有收到通知”

**原因：** 邮件通知被禁用或邮件错误

**解：**

* 检查“发送电子邮件”复选框已启用
* 验证收件人电子邮件地址
* 检查垃圾邮件文件夹
* 手动重新发送通知

### “错误的人得到了任务”

**原因：**路由逻辑不正确

**解：**

* 检查决策表条件
* 验证后备设置
* 使用示例文档进行测试
* 检查用户名中是否有拼写错误

### “创建的任务太多”

**原因：**卡多次触发

**解：**

* 检查条件是否足够具体
* 验证卡每个文档仅运行一次
* 查看“与”条件
* 添加额外的过滤

***

## 任务卡对照表

| 卡                                                        | 创建任务 | 分配给            | When        |
| ----------------------------------------------------------- | ------------ | --------------------- | ----------- |
| tasks\_create                                               | 是          | 个人            | 总是      |
| ACTION\_TASK\_FOR\_GROUP                                    | 是          | 集团                 | 总是      |
| ACTION\_DECISION\_TREE\_CREATE\_TASKS                       | 是          | 决策表结果 | 有条件的 |
| ACTION\_DECISION\_TREE\_TASKS\_SEQUENTIAL                   | 是          | 多个（顺序） | 有条件的 |
| ACTION\_CREATE\_TASK\_FOR\_USER\_SEQUENTIAL                 | 是          | 用户+文档       | 有条件的 |
| ACTION\_CREATE\_TASK\_FOR\_GROUP\_SEQUENTIAL                | 是          | 小组+文件      | 有条件的 |
| ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP                   | 是          | 设施组        | 有条件的 |
| ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP\_SEQUENTIAL       | 是          | 多种设施   | 有条件的 |
| ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP                | 是          | 采购团队      | 有条件的 |
| ACTION\_ASSIGN\_TASK\_PROCUREMENT\_GROUP\_SEQUENTIAL        | 是          | 多个（顺序） | 有条件的 |
| ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK | 是          | 现场/后备        | 有条件的 |

***

## 相关卡牌

* **ACTION\_ASSIGN\_DOCUMENT\_TO\_USER** - 分配文档而不创建任务
* **ACTION\_SEND\_EMAIL** - 直接通知人们
* **STAUS\_CHANGE** - 更改状态而不是创建任务
* **RUN\_WORKFLOW** - 触发不同的工作流程
