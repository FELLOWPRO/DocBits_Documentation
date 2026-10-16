# 任务分配与创建卡片

## 任务分配与创建卡片 — 完整指南

**涵盖内容：**12 个任务相关卡片

***

本页介绍的任务卡片位于工作流构建器的 **Then** 组中，也就是 **When/And** 条件匹配后执行的操作：

<figure><img src="../../../.gitbook/assets/workflow_designer_cards.png" alt="包含 When、And 和 Then 卡片组的工作流构建器画布"><figcaption><p>通过 <strong>Add Card</strong> 将任务和创建卡片添加到 <strong>Then</strong> 组。</p></figcaption></figure>

***

### 📌 版本信息

**演进最多的卡片：**tasks\_create（共 4 个版本，最新为 v4） **其他多版本卡片：**ACTION\_TASK\_FOR\_GROUP（v4）、ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP（v3）、ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK（v3）、ACTION\_DECISION\_TREE\_CREATE\_TASKS（v3）

**主要变更：**

* **v3 → v4 演进：**移除了决策树方案，新增通用工作项类型（Task、Ticket、Issue）
* **v2 → v3 迁移：**增加了决策树支持（目前已基本弃用）

📖 [完整版本历史](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/administration-and-setup/changelog/release.md#-task-management-cards) | [卡片版本数据库](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/DocFlow/docs/card_version.md)

***

### 概述

任务卡片用于为团队成员创建工作分配。当发票需要审批时，您可以自动创建任务并将其分配给合适的人员。

***

## 创建基本任务

### 卡片：tasks\_create / 创建任务并分配给用户

#### 用途

创建任务并将其分配给指定人员

#### 适用场景

* 发票需要由特定人员审核
* 需要指定个人审批
* 需要将工作交接给特定团队成员

#### 参数

**标题** 任务名称或主题

```
Example: "Review Invoice #INV-2025-001 for approval"
```

**描述** 任务详情

```
Example: "Invoice from Supplier ABC needs review.
Amount: €5000
Deadline: 2025-10-30
Please verify pricing and quality."
```

**优先级**

* 🔴 **高：**紧急，立即处理
* 🟡 **中：**普通优先级
* 🟢 **低：**可以稍后处理

**分配用户** 接收任务的人员

```
Example: John Smith (Finance Manager)
```

**电子邮件通知** 是否向被分配人员发送电子邮件提醒？

```
✅ Yes: Person gets email
❌ No: Task only in system
```

#### 示例

```
Condition（条件）: "Invoice amount > €10,000"
    ↓
Create Task（创建任务）:
- Title（标题）: "High-Value Invoice Review Required"
- Description（描述）: "Invoice #INV-2025-789 for €15,000 needs approval"
- Priority（优先级）: High
- Assigned to（分配给）: Sarah Johnson (Finance Approver)
- Send Email（发送电子邮件）: Yes
    ↓
Sarah 收到任务和电子邮件通知
```

***

### 卡片：ACTION\_TASK\_FOR\_GROUP / 为组创建任务

#### 用途

创建任务并分配给一个组（所有成员都可以看到）

#### 适用场景

* 多人都可以执行此任务
* 任务面向团队，而非个人
* 由最先有空的人员处理

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

#### 工作流示例

```
文档到达
    ↓
Condition（条件）: "Is supplier new?"
    ↓
为采购团队创建任务:
- Title（标题）: "Verify New Supplier Details"
- Description（描述）: "Please validate supplier information"
- Priority（优先级）: Medium
- Group（组）: Procurement Team (10 members)
- Notify（通知）: Yes
    ↓
采购团队的全部 10 名成员都能看到该任务
由第一位有空的成员接手
```

***

### 卡片：ACTION\_DECISION\_TREE\_CREATE\_TASKS

#### 用途

根据决策表逻辑创建任务

#### 工作方式

```
Decision Table Returns（决策表返回）:
  如果发票来自 Supplier A → 分配给采购部门
  如果发票来自 Supplier B → 分配给质量团队
  如果发票来自 Supplier C → 分配给财务部门

系统会根据满足的条件
自动创建并分配任务
```

#### 适用场景

* 不同供应商需要不同的审批流程
* 根据多个因素进行复杂路由
* 根据文档类型分配给不同团队

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

### 卡片：ACTION\_DECISION\_TREE\_TASKS\_SEQUENTIAL

#### 用途

根据决策表依次创建任务。任务按优先级顺序逐个分配

#### 适用场景

* 需要按顺序进行多次审批
* 工作流审批链
* 每个人审核后再交给下一位

#### 工作方式

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

#### 优先级系统

```
Priority 1 → Assign to: Person A
Priority 2 → Assign to: Person B
Priority 3 → Assign to: Person C

They must complete in order (1→2→3)
```

#### 配置示例

```
Decision Table Returns（决策表返回）:
  Level 1: Sarah Johnson (Finance)
  Level 2: Mike Smith (Manager)
  Level 3: Director (for approval)

Task Flow（任务流程）:
1. Sarah 审核 → 添加评论
2. 转交给 Mike → 他进行审核
3. 转交给 Director → 最终审批
4. 全部完成 → 导出
```

***

### 卡片：ACTION\_CREATE\_TASK\_FOR\_USER\_SEQUENTIAL

#### 用途

将文档分配给一位用户，并创建顺序任务

#### 适用场景

* 同时分配文档并创建任务
* 文档需要由特定人员审核
* 同时跟踪文档分配和任务创建

#### 工作方式

```
Two things happen:
1. Document is assigned to: Person A
2. Task is created for: Person A

Both in one action
```

#### 示例

```
高金额发票到达
    ↓
ACTION_CREATE_TASK_FOR_USER_SEQUENTIAL:
- 将文档分配给: Finance Manager
- 创建任务: "Review & Approve High Value Invoice"
- Priority（优先级）: High
    ↓
文档和任务都会转交给 Finance Manager
```

***

### 卡片：ACTION\_CREATE\_TASK\_FOR\_GROUP\_SEQUENTIAL

#### 用途

将文档分配给一个组并创建任务

#### 适用场景

* 文档需要由一个组处理
* 需要跟踪任务创建
* 先创建初始任务，再分配文档

#### 示例

```
新供应商评估
    ↓
ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL:
- 将文档分配给: Supplier Management Group
- 创建任务: "Evaluate New Supplier Credentials"
- 将任务分配给: 同一组
- Priority（优先级）: Medium
    ↓
组内成员都能看到文档和任务
```

***

## 创建高级任务

### 卡片：ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP

#### 用途

为特定设施组创建任务

#### 适用场景

* 面向仓库或设施团队的任务
* 特定设施的运营工作
* 需要考虑实际地点

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

### 卡片：ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP\_SEQUENTIAL

#### 用途

在多个设施之间依次分配任务

#### 适用场景

* 涉及多个设施的运营
* 任务在不同设施之间流转
* 按顺序处理设施相关工作

#### 工作方式

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
制造业文档
    ↓
创建顺序任务:
- 任务 1: Factory A（制造）- 优先级 1
- 任务 2: Quality Team（测试）- 优先级 2
- 任务 3: Warehouse（打包）- 优先级 3
- 任务 4: Shipping（发运）- 优先级 4
    ↓
每个团队完成后 → 转交给下一个团队
```

***

### 卡片：ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP

#### 用途

为采购部门创建任务

#### 适用场景

* 面向采购团队的任务
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

### 卡片：ACTION\_ASSIGN\_TASK\_PROCUREMENT\_GROUP\_SEQUENTIAL

#### 用途

在采购部门内部依次路由任务

#### 适用场景

* 多步骤采购流程
* 采购审批链
* 升级处理路径

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

### 卡片：ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK

#### 用途

从文档字段中获取用户并分配任务。如果找不到该用户，则使用备用用户

#### 适用场景

* 用户信息存储在文档字段中
* 文档指定了审核人员
* 指定用户不可用时有备用人员

#### 工作方式

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

所有任务卡片都使用以下参数：

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
🔴 HIGH（高）
   - 需在数小时内处理
   - 会阻塞其他流程
   - 示例：缺少供应物资、紧急审批

🟡 MEDIUM（中）
   - 常规处理
   - 正常时限
   - 示例：常规发票审核

🟢 LOW（低）
   - 可以等待数天/数周
   - 非紧急
   - 示例：归档旧文档
```

#### 截止日期（如有）

```
When should task be completed by?
Example: 2025-10-30 (5 days from now)
```

***

## 任务工作流场景

### 场景 1：简单审批

```
Invoice Arrives (€2000)
    ↓
Condition: Amount between €1000-€5000?
    ↓
YES: Create Task for Finance Manager
    ↓
Finance Manager reviews and approves
```

### 场景 2：多级审批

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
发票到达（来自新供应商）
    ↓
创建任务 1: 质量团队（验证供应商）
创建任务 2: 财务团队（检查价格）
创建任务 3: 采购部门（检查合同）
    ↓
所有团队同时开展工作
继续下一步前，所有任务都必须完成
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

✅ **建议：**

* 在任务标题中加入具体信息
* 设置合适的优先级
* 设置切实可行的截止日期
* 通知被分配人员
* 添加文档链接
* 使用清晰且可执行的描述

❌ **避免：**

* 创建含糊的任务标题（“审核一下”）
* 将所有任务都设为高优先级
* 忘记通知被分配人员
* 为同一项工作创建多个任务
* 将任务分配给无法处理的人员

***

## 任务故障排除

### “任务未分配给任何人”

**原因：**用户不存在或组为空

**解决方法：**

* 核对用户名拼写
* 检查用户在系统中是否处于启用状态
* 确认组内有成员
* 必要时使用备用用户

### “对方说没有收到通知”

**原因：**电子邮件通知已禁用，或电子邮件地址错误

**解决方法：**

* 检查是否已启用“Send Email”复选框
* 核实收件人电子邮件地址
* 检查垃圾邮件文件夹
* 手动重新发送通知

### “任务分配给了错误的人”

**原因：**路由逻辑不正确

**解决方法：**

* 检查决策表条件
* 核实备用设置
* 使用示例文档进行测试
* 检查用户名是否有拼写错误

### “创建了太多任务”

**原因：**卡片被多次触发

**解决方法：**

* 检查条件是否足够具体
* 确认每份文档只运行一次该卡片
* 检查“And”条件
* 添加其他筛选条件

***

## 任务卡片对比表

| 卡片                                                        | 创建任务 | 分配对象         | 适用时机   |
| ----------------------------------------------------------- | -------- | ---------------- | ---------- |
| tasks\_create                                               | 是       | 个人             | 始终       |
| ACTION\_TASK\_FOR\_GROUP                                    | 是       | 组               | 始终       |
| ACTION\_DECISION\_TREE\_CREATE\_TASKS                       | 是       | 决策表结果       | 有条件     |
| ACTION\_DECISION\_TREE\_TASKS\_SEQUENTIAL                   | 是       | 多人（依次）     | 有条件     |
| ACTION\_CREATE\_TASK\_FOR\_USER\_SEQUENTIAL                 | 是       | 用户与文档       | 有条件     |
| ACTION\_CREATE\_TASK\_FOR\_GROUP\_SEQUENTIAL                | 是       | 组与文档         | 有条件     |
| ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP                   | 是       | 设施组           | 有条件     |
| ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP\_SEQUENTIAL       | 是       | 多个设施         | 有条件     |
| ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP                | 是       | 采购团队         | 有条件     |
| ACTION\_ASSIGN\_TASK\_PROCUREMENT\_GROUP\_SEQUENTIAL        | 是       | 多人（依次）     | 有条件     |
| ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK | 是       | 字段/备用用户    | 有条件     |

***

## 相关卡片

* **ACTION\_ASSIGN\_DOCUMENT\_TO\_USER** - 分配文档但不创建任务
* **ACTION\_SEND\_EMAIL** - 直接通知相关人员
* **STAUS\_CHANGE** - 更改状态，而不是创建任务
* **RUN\_WORKFLOW** - 触发其他工作流
