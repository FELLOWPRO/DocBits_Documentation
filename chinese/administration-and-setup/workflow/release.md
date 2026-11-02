---
hidden: true
---

# 发布

## 版本控制原则

<figure><img src="../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 13.41.53.png" alt=""><figcaption><p>工作流版本控制系统</p></figcaption></figure>

### 版本 8.5.2024 - 核心版本控制功能

DocBits 工作流引擎为所有工作流卡片实现了稳健的版本控制：

1. **版本控制**：每张卡片可以有多个版本，每个版本代表一组不同的条件或操作。这样，您可以试验或调整规则，而不影响当前启用的工作流。
2. **无缝升级**：当文档处理要求发生变化，需要更新规则或条件时，您可以创建卡片的新版本。这样可以确保所有修改都经过有意制定和测试，然后再替换当前版本。这可以最大限度地减少文档处理中的错误和潜在中断。
3. **保持一致性**：在您决定升级之前保持原始卡片版本不变，可确保正在进行的流程不受影响。您可以在新版本上运行测试和验证，而不会影响线上数据或工作流。
4. **灵活性和测试**：多个版本支持在受控环境中测试不同场景。您可以查看新规则或变更对文档处理工作流的影响，而无需进行永久性修改。对结果满意后，您可以选择应用新版本。

***

## 卡片版本概览

### 统计数据

| 指标 | 数值 |
| -------------------------------- | --------------------------------------- |
| **具有多个版本的卡片** | 30+ |
| **版本记录总数** | 90+ |
| **当前启用的版本** | 81+ |
| **已弃用的版本** | 9 |
| **已完全禁用的卡片** | 2 |
| **最新版本（最高）** | 5 (CONDITION\_DOC\_TO\_PO\_UNIT\_PRICE) |

### 版本范围

* **最小值：** v1
* **最大值：** v5
* **每张卡片的平均版本数：** 3

***

## 卡片版本变更详情

### 🔧 操作卡片 - 外部集成与执行

#### 1. CALL\_API

**版本：** v1、v2（当前：v2）

📖 **指南：** [调用外部 API 指南](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/administration-and-setup/then/action/call-api-guide.md)

| 版本 | 翻译 | 状态 | 主要变更 |
| ------- | ----------- | --------- | -------------------------------------------------- |
| v1 | 否 | 启用 | 不含翻译键的基本 API 调用 |
| v2 | 是 | ✅ 当前 | 添加了用于多语言支持的 `trnsl_%call_api` |

**变更内容：**添加了带翻译键的国际化（i18n）支持。功能保持不变。

**变更前（v1）：**

```
Call Api: [endpoint] with method: [method], params: [params], data: [data]
```

**变更后（v2）：**

```
trnsl_%call_api trnsl_be_% Call Api: [endpoint] with method: [method], params: [params], data: [data]
```

**建议：**所有新工作流均使用 v2（包含语言支持） **向后兼容性：**✅ v1 仍可使用

***

#### 2. HTTPS 请求 (HTTPS\_REQUEST)

**版本：** v1、v2（当前：v2）

| 版本 | 翻译 | 状态 | 主要变更 |
| ------- | ----------- | --------- | -------------------------------------------------- |
| v1 | 否 | 启用 | 简单 HTTP 请求 |
| v2 | 是 | ✅ 当前 | 添加了 `trnsl_%send_https_request` 翻译键 |

**变更内容：**添加了翻译支持。核心 webhook/请求功能保持不变。 **建议：**使用 v2（支持多语言）

***

#### 3. ACTION\_RUN\_DOCOPERATOR\_SCRIPT ⚠️

**版本：** v2（当前）、v3、v4（已弃用并禁用）

| 版本 | 翻译 | 状态 | 主要变更 |
| ------- | ----------- | ----------------------- | ----------------------------------------------------------- |
| v2 | 是 | 启用 | 原始 DocOperator 实现 |
| v3 | 是 | 启用 | 添加了“执行提示”参数，以提供更多控制 |
| v4 | 是 | ❌ 已弃用并禁用 | 移除了“执行”参数（回退） |

**演进路径：**v2 → v3（添加参数）→ v4（回退 - 不建议使用）

**变更内容：**

* v2 → v3：添加了可选的执行控制参数，以提高灵活性
* v3 → v4：经过进一步分析后移除了该参数（已弃用）

**建议：**新工作流使用 v3（功能最全的最新启用版本） **迁移：**如果正在使用 v4，请切换到 v3 ⚠️

***

#### 4. ACTION\_TASK\_FOR\_GROUP

**版本：** v2、v3（已弃用）、v4（当前）

📖 **指南：**[任务分配指南](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/administration-and-setup/then/task/task-assignment-guide.md)

| 版本 | 变更 | 状态 | 类型参数 |
| ------- | ------------------------------- | ------------ | ----------------------- |
| v2 | 原始实现 | 启用 | "Task"（固定） |
| v3 | + 决策树支持 | ❌ 已弃用 | "Task"（固定） |
| v4 | - 决策树，+ 通用类型 | ✅ 当前 | 通用类型（灵活） |

**演进：**v2 → v3（决策树实验）→ v4（通用类型，移除决策树）

**v2 → v3 变更（决策树实验）：**

```
Before: "Create a new Task with the title: [param] ... and assign to group [param]"
After:  "Create a new Task with the title: [param] ... and assign to group [param].
         Use decision tree, if available: [param]"
```

**v3 → v4 变更（通用类型 + 移除决策树）：**

```
Before (v3): "Create a new Task with the title: [param] ... "
After (v4):  "Create a new [param] with the title: [param] ... "
```

**变更内容：**

* v2 → v3：添加了 `decision tree, if available: [param]` 参数
* v3 → v4：
  * ❌ 移除了决策树参数
  * ✅ 将“Task”改为通用的 `[param]`（支持 Task、Ticket、Issue 等）
  * 添加了翻译键 `trnsl_%task_for_group_v4`

**原因：**v3 的决策树方案属于实验性质。v4 提供了更好的灵活性，支持通用工作项类型。 **建议：**使用 v4（当前版本，灵活性最高）

***

#### 5. ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP

**版本：**v2、v3（当前）

| 版本 | 任务类型 | 状态 | 主要差异 |
| ------- | -------------- | --------- | ----------------------------- |
| v2 | "task"（固定） | 启用 | 原始版本 |
| v3 | 通用类型 | ✅ 当前 | 改为灵活的 `[param]` |

**变更内容：**v2 → v3：“Create a new task” → “Create a new \[param]”（支持任意工作项类型） **建议：**使用 v3

***

#### 6. RUN\_WORKFLOW

**版本：**v1、v2（当前）

**变更内容：**v1 → v2：添加了 `trnsl_%run_workflow` 翻译键 **建议：**使用 v2

***

### 📊 采购订单比较与验证卡片

#### 1. CONDITION\_DOC\_TO\_PO\_UNIT\_PRICE ⭐（演进最多 - 5 个版本）

**版本：**v2、v3、v4、v5（当前）

📖 **指南：**[采购订单匹配完整指南](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/administration-and-setup/and/compare-with-purchase-order/po-matching-complete-guide.md#2-unit-price-comparison-document-vs-po)

| 版本 | 变更 | 状态 | 容差 | 比较 |
| ------- | ------------------------ | --------- | --------------------- | ---------- |
| v2 | 基本价格比较 | 启用 | ❌ 无 | 基本 |
| v3 | 与 v2 相同 | 启用 | ❌ 无 | 基本 |
| v4 | + 比较模式参数 | 启用 | ❌ 无 | ✅ 是 |
| v5 | + 容差参数 | ✅ 当前 | ✅ 是（金额 + 单位） | ✅ 是 |

**演进路径：**v2 → v3（无变化）→ v4（比较模式）→ v5（容差阈值）

**v2 → v3：**无功能变化（使用相同翻译键）

**v3 → v4 变更（添加比较模式）：**

```
Before: "[document] unit price is [operator] to purchase order"
After:  "[document] unit price is [operator] to purchase order. Compare as [mode]"
```

**v4 → v5 变更（添加容差参数）：**

```
Before: "[document] unit price is [operator] to purchase order. Compare as [mode]"
After:  "[document] unit price is [operator] to purchase order, with tolerance of [amount] [unit].
         Compare as [mode]"
```

**变更内容：**

* **v2 → v3：**无功能变化
* **v3 → v4：**添加了 `Compare as [param]`，支持不同的比较运算符
* **v4 → v5：**添加了容差参数：
  * `with tolerance of [amount] [unit]`
  * 示例：“with tolerance of 2 %”或“with tolerance of 100 EUR”
  * 支持：%、EUR、$ 及其他货币

**使用场景：**

* v2/v3：严格匹配（仅接受完全相同的价格）
* v4：不同的比较方法
* v5：灵活接受偏差（例如，接受 2% 的价格差异）✅ 推荐

**建议：**现代采购订单匹配工作流使用 v5

***

#### 2. CONDITION\_OC\_TO\_PO\_ITEMS

**版本：**v1（已弃用）、v2、v3、v4（当前）

| 版本 | 变更 | 状态 | 比较功能 |
| ------- | ---------------------------- | ------------ | --------------- |
| v1 | 无翻译、无方法 | ❌ 已弃用 | 基本 |
| v2 | + 翻译键、+ 方法 | 启用 | 基本方法 |
| v3 | 与 v2 相同 | 启用 | 基本方法 |
| v4 | + 比较模式参数 | ✅ 当前 | ✅ 灵活 |

**变更内容：**

* **v1 → v2：**添加了 `trnsl_%in_order_confirmations_matches_purchase_order` 和比较方法参数
* **v2 → v3：**无变化
* **v3 → v4：**添加了 `Compare as [param1] [param2]`，支持灵活的比较模式

**建议：**使用 v4（避免使用已弃用的 v1）

***

#### 3. CONDITION\_DATES\_OPERATOR\_OC\_LINE\_ITEMS

**版本：**v2、v3（当前）

| 版本 | 容差天数 | 可接受的容差天数 | 状态 |
| ------- | -------------- | ----------------------- | --------- |
| v2 | ❌ 无 | ❌ 无 | 启用 |
| v3 | ✅ 有 | ✅ 有 | ✅ 当前 |

**变更内容：**v2 → v3：添加了容差参数：

* `with [param] days as tolerance`
* `and [param] as accepted tolerance days`

**示例：**接受承诺交货日期前后 5 天内的交货日期 **建议：**使用 v3

***

#### 4. CONDITION\_LESS\_THAN\_TOLERANCE\_AS\_VALUE\_OF\_ORDERED\_QUANTITY

**版本：**v2、v3、v4（当前）

| 版本 | 比较模式 | 状态 |
| ------- | ------------------------- | --------- |
| v2 | 基本 | 启用 |
| v3 | 基本（无变化） | 启用 |
| v4 | ✅ 灵活模式选择 | ✅ 当前 |

**变更内容：**v3 → v4：添加了 `compare [param]`，支持不同的比较方式 **建议：**使用 v4

***

#### 5. COMBINED\_PRICE\_OF\_QUANTITY\_DIFFERENCE\_OPERATOR\_VALUE

**版本：**v2、v3、v4（当前）

| 版本 | 比较模式 | 状态 |
| ------- | -------------------- | --------- |
| v2 | 标准 | 启用 |
| v3 | 标准（无变化） | 启用 |
| v4 | ✅ 灵活 | ✅ 当前 |

**变更内容：**v3 → v4：添加了 `compare [param]` 参数 **建议：**使用 v4

***

#### 6. CONDITION\_CONFIRMED\_DELIVERY\_ACCEPTED\_DATE\_IN\_CALENDAR\_MASTER\_DATA

**版本：**v2、v3（当前）

| 版本 | 交货类型 | 主数据表 | 状态 |
| ------- | --------------------- | ----------------- | --------- |
| v2 | "Confirmed"（固定） | 固定引用 | 启用 |
| v3 | \[可配置参数] | 动态 \[param] | ✅ 当前 |

**变更内容：**v2 → v3：

* 将“Confirmed delivery”改为 `[param] delivery`（灵活的交货类型）
* 将固定表引用改为 `stored in [param]`（动态选择数据表）

**灵活性：**v3 支持不同的交货日期类型和供应商表 **建议：**使用 v3

***

#### 7. CONDIITON\_UNIT\_OF\_MEASURE\_EQUAL

**版本：**v2、v3（当前）

| 版本 | 供应商表引用 | 状态 |
| ------- | ----------------------------------- | --------- |
| v2 | "supplier item price table"（固定） | 启用 |
| v3 | \[动态参数] | ✅ 当前 |

**变更内容：**v2 → v3：将固定表引用改为 `stored in [param]`（支持动态选择数据表） **建议：**使用 v3

***

### 👥 分配与路由卡片

#### 1. DOC\_USER\_ASSIGN

**版本：**v1、v2、v3（已弃用）

| 版本 | 翻译 | 决策树 | 状态 |
| ------- | ----------- | ------------- | ------------ |
| v1 | 否 | ❌ 否 | 启用 |
| v2 | 是 | ❌ 否 | ✅ 当前 |
| v3 | 是 | ✅ 是 | ❌ 已弃用 |

**演进：**v1（无 i18n）→ v2（支持 i18n）→ v3（+ 决策树实验，现已弃用）

**变更内容：**

* v1 → v2：添加了翻译键
* v2 → v3：添加了决策树支持（实验性质，已弃用）

**建议：**使用 v2（稳定并支持 i18n）

***

#### 2. DOC\_GROUP\_ASSIGN

**版本：**v2、v3（已弃用）

| 版本 | 决策树 | 状态 |
| ------- | ------------- | ------------ |
| v2 | ❌ 否 | ✅ 当前 |
| v3 | ✅ 是 | ❌ 已弃用 |

**变更内容：**v2 → v3：添加了 `Use decision tree, if available [param]`（后来已弃用） **建议：**使用 v2

***

#### 3. OC\_ASSIGN\_DOC

**版本：**v1、v2（当前）

**变更内容：**v1 → v2：添加了 `trnsl_%oc_assign_doc` 翻译键 **建议：**使用 v2

***

### 📋 任务管理卡片

#### 1. tasks\_create ⭐（演进最多的任务卡片 - 4 个版本）

**版本：**v1（已弃用）、v2（已弃用）、v3（已弃用）、v4（当前）

📖 **指南：**[任务分配指南](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/administration-and-setup/then/task/task-assignment-guide.md#card-tasks_create--create-task-and-assign-to-user)

| 版本 | 翻译 | 决策树 | 工作项类型 | 状态 |
| ------- | ----------- | ------------- | ---------------- | ------------ |
| v1 | 否 | 否 | "Task"（固定） | ❌ 已弃用 |
| v2 | 是 | 否 | "Task"（固定） | ❌ 已弃用 |
| v3 | 是 | 是 | "Task"（固定） | ❌ 已弃用 |
| v4 | 是 | 否 | \[通用参数] | ✅ 当前 |

**演进时间线：**

```
v1 (original)
  ↓ (add translation)
v2 (with i18n)
  ↓ (experiment with decision tree)
v3 (+ decision tree, BUT deprecated after this)
  ↓ (remove decision tree, add generic types)
v4 (CURRENT - flexible work items)
```

**v1 → v2 变更（添加翻译键）：**

```
Before: "Create a new Task with the title: [param] ... and assign to user [param]"
After:  "trnsl_%tasks_create trnsl_be_% Create a new Task with the title: [param] ... and assign to user [param]"
```

**v2 → v3 变更（决策树实验）：**

```
Before: "Create a new Task with the title: [param] ... and assign to user [param]"
After:  "Create a new Task with the title: [param] ... and assign it to the user [param].
         Use decision tree, if available: [param]"
```

**v3 → v4 变更（通用类型 + 移除决策树）：**

```
Before: "Create a new Task with the title: [param] ... "
After:  "Create a new [param] with the title: [param] ... "
```

**变更内容：**

* **v1 → v2：**添加了 `trnsl_%tasks_create` 翻译键
* **v2 → v3：**
  * 添加了决策树支持：`Use decision tree, if available: [param]`
  * 将“assign to user”改为“assign it to the user”
* **v3 → v4：**
  * ❌ 移除了决策树参数
  * ✅ 将“Task”改为通用的 `[param]`（支持 Task、Ticket、Issue 等）
  * 将翻译键更新为 `trnsl_%tasks_create_v4`

**决策树说明：**v3 使用决策树动态分配任务。此方案属于实验性质，在 v4 中已弃用，改用基于直接参数的工作项类型选择。

**建议：**新工作流仅使用 v4 **迁移：**如果正在使用 v1、v2 或 v3，请升级到 v4 ✅

***

#### 2. OC\_TASK

**版本：**v1、v2（当前）

**变更内容：**v1 → v2：添加了 `trnsl_%oc_task` 翻译键 **建议：**使用 v2

***

#### 3. ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK

**版本：**v1、v3（当前 - 跳过 v2）

| 版本 | 工作项类型 | 状态 |
| ------- | ---------------- | --------- |
| v1 | "Task"（固定） | 启用 |
| v3 | \[通用参数] | ✅ 当前 |

**变更内容：**v1 → v3：演进为通用类型（生产环境跳过了 v2） **建议：**使用 v3

***

#### 4. ACTION\_DECISION\_TREE\_CREATE\_TASKS

**版本：**v2、v3（当前）

| 版本 | 分配文本 | 状态 |
| ------- | ------------------------------ | --------- |
| v2 | "Assign task with title" | 启用 |
| v3 | "Assign \[generic] with title" | ✅ 当前 |

**变更内容：**v2 → v3：

* 将“Assign task”改为“Assign \[generic param]”
* 将“return of decision”改为“return of decision table”（术语更清晰）

**建议：**使用 v3

***

### 🔄 文档控制卡片

#### APPROVE

**版本：**v1、v2（当前） **变更：**添加了 `trnsl_%approve_doc` 翻译键 **建议：**使用 v2

***

#### REJECT

**版本：**v1、v2（当前） **变更：**添加了 `trnsl_%reject_doc` 翻译键 **建议：**使用 v2

***

#### STAUS\_CHANGE（状态变更）

**版本：**v1、v2、v3（当前）

| 版本 | 工作流触发 | 状态 |
| ------- | ---------------- | --------- |
| v1 | ❌ 否 | 启用 |
| v2 | ❌ 否 | 启用 |
| v3 | ✅ 是 | ✅ 当前 |

**变更内容：**v2 → v3：添加了 `trigger Workflows [param]`，在状态变更时自动触发工作流 **建议：**使用 v3

***

#### EXPORT

**版本：**v1、v2、v3（当前）

| 版本 | 验证 | 状态 |
| ------- | ---------- | --------- |
| v1 | ❌ 否 | 启用 |
| v2 | ❌ 否 | 启用 |
| v3 | ✅ 是 | ✅ 当前 |

**变更内容：**v2 → v3：添加了 `Start Export with Validation: [param]` **建议：**使用 v3

***

### 🧮 数据处理卡片

#### CALC\_COLUMNS、CALC\_COLUMNS\_REGEX、EDIT\_COLUMN、AI\_CALC\_MTZ\_ETZ

**模式：**v1 → v2（添加翻译键） **建议：**全部使用 v2

***

#### CONDITION\_DECISION\_TREE\_DATA

**版本：**v2、v3（当前）

| 版本 | 数据使用方式 | 状态 |
| ------- | ------------------------------------------------------------- | --------- |
| v2 | “在后续卡片中使用返回数据” | 启用 |
| v3 | "\[明确参数] 返回的数据可供后续卡片使用" | ✅ 当前 |

**变更内容：**v2 → v3：更明确地控制决策树数据提取 **建议：**使用 v3

***

### ❌ 已禁用的卡片（请勿使用）

#### DOC\_SUBORG\_CHANGE

**版本：**v1、v2（均已禁用） **状态：**不再支持 **替代方案：**使用文档分配功能

***

#### RUN\_SCRIPT

**版本：**v2、v3（均已禁用） **状态：**已由 ACTION\_RUN\_DOCOPERATOR\_SCRIPT 替代 **替代方案：**使用 ACTION\_RUN\_DOCOPERATOR\_SCRIPT v3

***

## 🎯 常见版本模式

### 模式 1：采用翻译键（v1 → v2）

**受影响：**15+ 张卡片

**变更：**添加了 `trnsl_%[card_name]` 翻译键

```
v1: Plain text (no i18n)
v2: trnsl_%[key] trnsl_be_% Plain text (with i18n)
```

**卡片：**CALL\_API、RUN\_WORKFLOW、APPROVE、REJECT、CALC\_COLUMNS 等 **影响：**支持多语言

***

### 模式 2：集成决策树（v2 → v3）- 已弃用

**受影响：**5 张卡片 (ACTION\_TASK\_FOR\_GROUP, tasks\_create, DOC\_USER\_ASSIGN, DOC\_GROUP\_ASSIGN, ACTION\_DECISION\_TREE\_CREATE\_TASKS)

**变更：**添加了可选的决策树参数

```
v2: Standard task/assignment logic
v3: + "Use decision tree, if available: [param]"
```

**状态：**❌ 大多已弃用（ACTION\_DECISION\_TREE\_CREATE\_TASKS 除外） **原因：**更倾向于采用更简单的直接参数方案

***

### 模式 3：通用类型演进（v3 → v4）

**受影响：**4 张卡片 (tasks\_create, ACTION\_TASK\_FOR\_GROUP, ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP, ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK)

**变更：**“Task” → 通用类型参数

```
v3: Create a new Task with title: [param]
v4: Create a new [param] with title: [param]
```

**影响：**支持 Task、Ticket、Issue 和其他工作项类型 **优势：**灵活性和可复用性更高

***

### 模式 4：容差参数（采购订单卡片）

**受影响：**6 张卡片 (CONDITION\_DOC\_TO\_PO\_UNIT\_PRICE, CONDITION\_DATES\_OPERATOR\_OC\_LINE\_ITEMS, CONDITION\_LESS\_THAN\_TOLERANCE\_AS\_VALUE\_OF\_ORDERED\_QUANTITY 等)

**变更：**添加了容差/偏差支持

```
v2: Value [operator] Reference Value
v3+: Value [operator] Reference with tolerance [amount] [unit]
```

**示例：**

* “with tolerance of 2 %”
* “with tolerance of 100 EUR”
* “with 5 days as tolerance”

**影响：**匹配条件更贴合实际（不必要求所有值完全一致）

***

### 模式 5：比较模式参数

**受影响：**3 张卡片 (COMBINED\_PRICE\_OF\_QUANTITY\_DIFFERENCE\_OPERATOR\_VALUE, CONDITION\_OC\_TO\_PO\_ITEMS, CONDITION\_LESS\_THAN\_TOLERANCE\_AS\_VALUE\_OF\_ORDERED\_QUANTITY)

**变更：**添加了灵活的比较方法选择

```
v3: Standard comparison
v4: + "Compare as [param1] [param2]"
```

**影响：**支持不同的比较算法

***

## ✅ 版本建议

### 用于新工作流

**规则：**始终使用编号最高且已启用的版本

* 提供最新功能
* 支持最佳
* 经过最多测试
* 推荐的方案

### 用于现有工作流

**稳妥做法：**

* 如果当前版本运行正常，请继续使用
* 规划逐步迁移到较新版本
* 先在沙盒环境中测试升级

### 迁移优先级

| 优先级 | 卡片 | 操作 |
| ---------- | ------------------------------------------------------------------------------------------------- | -------------------------- |
| **高** | tasks\_create v1/v2/v3、ACTION\_TASK\_FOR\_GROUP v3、CONDITION\_DOC\_TO\_PO\_UNIT\_PRICE v2/v3/v4 | 升级到当前版本 |
| **中** | 其他 v1/v2 翻译升级、采购订单卡片 v2/v3 | 考虑升级 |
| **低** | 没有功能变更的卡片 | 可选 |

***

## ⚠️ 已弃用的版本 - 请勿使用

| 卡片 | 版本 | 原因 | 替代版本 |
| -------------------------------- | ---------- | ------------------------------------- | ----------- |
| tasks\_create | v1、v2、v3 | 版本很旧，或决策树已弃用 | v4 |
| ACTION\_TASK\_FOR\_GROUP | v3 | 决策树方案已弃用 | v4 |
| DOC\_USER\_ASSIGN | v3 | 决策树方案已弃用 | v2 |
| DOC\_GROUP\_ASSIGN | v3 | 决策树方案已弃用 | v2 |
| CONDITION\_DOC\_TYPE\_IS\_ISNOT | v1 | 版本很旧 | v2 |
| CONDITION\_OC\_TO\_PO\_ITEMS | v1 | 版本很旧 | v4 |
| ACTION\_RUN\_DOCOPERATOR\_SCRIPT | v4 | 功能已回退 | v3 |

***

## 🔄 已完全禁用的卡片 - 无法使用

| 卡片 | 版本 | 原因 | 替代方案 |
| ------------------- | -------- | ----------------------- | ----------------------------------- |
| DOC\_SUBORG\_CHANGE | v1、v2 | 不再支持 | 文档分配卡片 |
| RUN\_SCRIPT | v2、v3 | 已由 DocOperator 替代 | ACTION\_RUN\_DOCOPERATOR\_SCRIPT v3 |

***

## 相关文档

* 📖 [卡片版本参考](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/administration-and-setup/changelog/card-versioning.md) - 版本信息详情
* 📚 [工作流指南](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/administration-and-setup/README.md) - 卡片使用分步指南
* 🔄 [卡片版本数据库](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/administration-and-setup/docs/card_version.md) - 完整版本历史
* 📋 [工作流日志](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/administration-and-setup/workflow-logs/README.md) - 执行与调试

***

**最后更新：**2025 年 10 月 23 日 **状态：**版本历史完整 **数据库来源：**postgres-dev-docflow
