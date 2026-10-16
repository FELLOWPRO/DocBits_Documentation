# 采购订单匹配模式

**模式类型：** 验证与比较 **复杂度：** 中高 **预计设置时间：** 60-90 分钟 **常见用例：** 三方匹配、发票验证、差异检查、容差管理

***

您可以在 **Workflow Builder**（工作流仪表板 → 工作流列表 → 添加工作流）中构建此模式。点击 **Add Card**，然后打开 **Compare with Purchase Order** 类别——此类别包含此模式使用的所有匹配卡片（价格、数量、容差和行项目比较卡片）：

<figure><img src="../../../../.gitbook/assets/workflow_add_card_picker.png" alt="Add Card 卡片库，显示 Compare with Purchase Order 卡片"><figcaption><p><strong>Compare with Purchase Order</strong> 类别——此模式中使用的价格、数量、容差和行项目匹配卡片。</p></figcaption></figure>

***

## 模式概览

此模式演示如何在 DocBits 中实现全面的采购订单（PO）匹配工作流。PO 匹配是一项关键控制流程，用于将发票数据与采购订单数据进行比较，以便在审批付款前发现差异。

**此模式的功能：**

1. 根据发票中的 PO 编号检索 PO 数据
2. 比较发票行项目与 PO 行项目
3. 计算差异（价格、数量、总额）
4. 应用容差规则
5. 根据匹配结果转交审批或升级处理
6. 跟踪匹配历史和例外情况

***

## 何时使用此模式

在需要以下功能时使用此模式：

* ✅ 根据采购订单验证发票
* ✅ 在付款前发现定价错误
* ✅ 识别数量差异
* ✅ 执行采购控制
* ✅ 防止重复付款
* ✅ 自动执行三方匹配
* ✅ 减少人工审核发票的工作量

**以下情况不要使用此模式：**

* ❌ 发票没有对应的 PO（非 PO 发票）
* ❌ DocBits 中没有可用的 PO 数据
* ❌ 更倾向于人工审核，而非自动化
* ❌ 业务政策不要求进行 PO 匹配

***

## 了解 PO 匹配

### 三方匹配

**传统采购控制：**

```
采购订单 (PO)  →  下单时创建
        ↓
收货单 (GR)     →  收货时创建
        ↓
发票            →  由供应商创建

三方匹配 = 采购订单 + 收货单 + 发票全部匹配
```

**DocBits 实施方式（两方匹配）：**

```
采购订单 (PO)  →  导入 DocBits
        ↓
发票            →  由 DocBits 扫描
        ↓
比较            →  验证发票与采购订单
```

***

## 差异计算公式

### 单价差异

**公式：**

```
差异百分比 = |(发票单价 - 采购订单单价)| / 采购订单单价 × 100
```

**示例：**

```
采购订单单价：       €100.00
发票单价：           €103.00

差异 = |103 - 100| / 100 × 100
     = 3 / 100 × 100
     = 3%

容差：5%
结果：3% ≤ 5% → 通过 ✅
```

***

### 数量差异

**公式：**

```
差异百分比 = |(发票数量 - 采购订单数量)| / 采购订单数量 × 100
```

**示例：**

```
采购订单数量：       100 units
发票数量：           98 units

差异 = |98 - 100| / 100 × 100
     = 2 / 100 × 100
     = 2%

容差：10%
结果：2% ≤ 10% → 通过 ✅
```

***

### 总金额差异

**公式：**

```
差异百分比 = |(发票总额 - 采购订单总额)| / 采购订单总额 × 100
```

**示例：**

```
采购订单总额：       €10,000.00
发票总额：           €10,450.00

差异 = |10450 - 10000| / 10000 × 100
     = 450 / 10000 × 100
     = 4.5%

容差：5%
结果：4.5% ≤ 5% → 通过 ✅
```

***

## 完整工作流示例

### 场景：基于容差路由的发票验证

**业务需求：**

* 必须验证所有带有 PO 参考信息的发票
* 价格差异容差：5%
* 数量差异容差：10%
* 总金额差异容差：3%
* 在容差范围内：自动审批
* 超出容差范围：创建审核任务
* 缺少 PO：升级至采购部门处理

**使用的工作流卡片：**

1. CONDITION\_DOC\_FIELD\_EXISTS - 检查是否存在 PO 编号
2. PURCHASE\_ORDER\_FULL\_MATCH - 尝试完整匹配
3. CONDITION\_DOC\_TO\_PO\_UNIT\_PRICE - 检查价格差异
4. CONDITION\_DOC\_TO\_PO\_QUANTITY - 检查数量差异
5. CONDITION\_DOC\_TO\_PO\_TAX\_LINES - 检查税项是否一致
6. ACTION\_SET\_FIELD\_TO\_TEXT - 存储匹配结果
7. tasks\_create - 创建审核任务
8. ACTION\_SEND\_EMAIL\_TO\_GROUPS - 发送通知

***

## 分步实施

### 步骤 1：检查 PO 参考信息

**卡片：** CONDITION\_DOC\_FIELD\_EXISTS 或 CONDITION\_DOC\_FIELD\_CONTAINS

**配置：**

```
字段：PO_Number
运算符：IS NOT EMPTY
```

**逻辑：**

```
IF PO_Number 存在：
  → 继续进行采购订单匹配
ELSE：
  → 路由至“非采购订单发票”工作流
  → 创建人工审核任务
  → 跳过采购订单匹配
```

**指南参考：** [条件卡片指南](../condition-cards-complete-guide.md)

***

### 步骤 2：检索 PO 数据

**在 DocBits 中自动完成：**

* 系统通过 PO\_Number 字段查找 PO
* 检索 PO 行项目
* 提供数据以供比较

**手动配置（如有需要）：**

```
采购订单来源：DocBits 主数据
采购订单查询字段：PO_Number
匹配类型：精确匹配
包含已关闭的采购订单：否（或在策略允许时为是）
```

***

### 步骤 3：检查 PO 完整匹配

**卡片：** PURCHASE\_ORDER\_FULL\_MATCH

**用途：** 快速检查所有内容是否完全匹配

**配置：**

```
匹配级别：完全匹配
包含：所有行项目、价格、数量、总额
容差：无（精确匹配）
```

**逻辑：**

```
IF 完全匹配 = TRUE：
  → 将 "PO_Match_Status" 设为 "FULL MATCH"
  → 自动批准文档
  → 跳过详细检查
  → END ✅

IF 完全匹配 = FALSE：
  → 继续进行详细差异检查
  → 确定具体差异
```

**结果：**

* **TRUE**：完全匹配，自动审批
* **FALSE**：继续执行详细检查

***

### 步骤 4：检查单价差异

**卡片：** CONDITION\_DOC\_TO\_PO\_UNIT\_PRICE（推荐 v5）

**配置：**

```
比较模式：百分比差异
容差：5%
运算符：差异小于或等于
应用范围：所有行项目
```

**分步说明：**

```
对于每个行项目：
  1. 获取发票单价
  2. 获取采购订单单价（按产品代码匹配）
  3. 计算：差异百分比 = |发票 - 采购订单| / 采购订单 × 100
  4. 检查：差异百分比 ≤ 5%？
  5. 存储结果
```

**计算示例：**

```
行项目 1：
  产品：ABC123
  发票价格：€52.00
  采购订单价格：€50.00
  差异 = |52-50|/50 × 100 = 4%
  容差：5%
  结果：通过 ✅

行项目 2：
  产品：XYZ789
  发票价格：€120.00
  采购订单价格：€100.00
  差异 = |120-100|/100 × 100 = 20%
  容差：5%
  结果：未通过 ❌

总体结果：未通过（一个或多个行项目未通过）
```

**指南参考：** [PO 匹配完整指南 - 单价](../po-matching-complete-guide.md#unit-price-comparison)

***

### 步骤 5：检查数量差异

**卡片：** CONDITION\_DOC\_TO\_PO\_QUANTITY

**配置：**

```
比较模式：百分比差异
容差：10%
运算符：差异小于或等于
应用范围：所有行项目
允许交付不足：是（在容差范围内）
允许超额交付：否（严格限制）
```

**逻辑：**

```
对于每个行项目：
  1. 获取发票数量
  2. 获取采购订单数量
  3. 计算：差异 % = |Invoice - PO| / PO × 100
  4. 检查：差异 % ≤ 10%？
  5. 特殊规则：
     - 少交货：允许在容差范围内
     - 超交货：拒绝（或采用更严格的容差）
```

**示例：**

```
行项目 1：
  产品：ABC123
  发票数量：98 units
  采购订单数量：100 units
  差异 = |98-100|/100 × 100 = 2%
  少交货：2%（在 10% 容差范围内）
  结果：通过 ✅

行项目 2：
  产品：XYZ789
  发票数量：115 units
  采购订单数量：100 units
  差异 = |115-100|/100 × 100 = 15%
  超交货：15%（超出 10% 容差）
  结果：未通过 ❌（升级处理）
```

**指南参考：** [PO 匹配完整指南 - 数量](../po-matching-complete-guide.md#quantity-comparison)

***

### 步骤 6：检查税项是否一致

**卡片：** CONDITION\_DOC\_TO\_PO\_TAX\_LINES

**配置：**

```
匹配税码：是
匹配税率：是
匹配税额：容差为 1%
税额计算：验证重新计算结果
```

**验证：**

```
1. 检查税码是否匹配（例如，双方均为 "VAT19"）
2. 检查税率是否匹配（双方均为 19%）
3. 验证税额计算：
   税额 = 净额 × 税率
4. 允许小幅舍入差异
```

**示例：**

```
发票：
  净额：€100.00
  税率：19%
  税额：€19.00
  总额：€119.00

采购订单：
  净额：€100.00
  税率：19%
  税额：€19.00
  总额：€119.00

结果：税务信息一致，通过 ✅
```

***

### 步骤 7：存储匹配结果

**卡片：** ACTION\_SET\_FIELD\_TO\_TEXT（多个实例）

**配置：**

**字段 1：PO\_Match\_Status**

```
字段：PO_Match_Status
值：{{CALCULATED}}
选项："FULL MATCH" | "WITHIN TOLERANCE" | "OUT OF TOLERANCE" | "NO MATCH"
```

**字段 2：Price\_Variance\_Percent**

```
字段：Price_Variance_Percent
值：{{CALCULATED_PRICE_VARIANCE}}
格式："4.5%"（示例）
```

**字段 3：Quantity\_Variance\_Percent**

```
字段：Quantity_Variance_Percent
值：{{CALCULATED_QUANTITY_VARIANCE}}
格式："2.0%"（示例）
```

**字段 4：Match\_Details**

```
字段：Match_Details
值："价格差异：4.5%（在 5% 容差范围内）\n数量差异：2.0%（在 10% 容差范围内）\n总计：通过"
```

**指南参考：** [字段操作指南](../field-manipulation-guide.md)

***

### 步骤 8：根据匹配结果路由

**场景 A：完全匹配（完整匹配）**

```
IF PO_Match_Status = "FULL MATCH":
  1. 将 Approval_Status 设为 "AUTO APPROVED"
  2. 将 Match_Type 设为 "FULL"
  3. ACTION_APPROVE_DOCUMENT
  4. 导出到 ERP
  5. 发送确认邮件
  → END ✅
```

**场景 B：在容差范围内**

```
IF PO_Match_Status = "WITHIN TOLERANCE":
  1. 将 Approval_Status 设为 "AUTO APPROVED"
  2. 将 Match_Type 设为 "TOLERANCE"
  3. 记录差异详情
  4. ACTION_APPROVE_DOCUMENT
  5. 导出到 ERP
  → END ✅
```

**场景 C：超出容差范围（轻微）**

```
IF 差异 < 15%（轻微异常）：
  1. 设置 Match_Status = "REVIEW REQUIRED"（需要审核）
  2. 创建任务："Review PO Variance"（审核采购订单差异）
     - 分配给：应付账款专员
     - 优先级：Medium（中）
     - 截止时间：3 days
  3. 发送包含差异详情的电子邮件
  4. 等待任务完成
  5. IF 已批准：继续处理
     IF 已拒绝：退回给供应商
```

**场景 D：超出容差范围（严重）**

```
IF 差异 ≥ 15%（重大异常）：
  1. 设置 Match_Status = "ESCALATION REQUIRED"（需要升级处理）
  2. 创建任务："URGENT: Major PO Variance"（紧急：重大采购订单差异）
     - 分配给：采购经理
     - 优先级：High（高）
     - 截止时间：1 day
  3. 向以下对象发送紧急电子邮件：
     - 采购经理
     - 财务经理
     - 供应商联系人
  4. 阻止文档继续处理
  5. 等待问题解决
```

**场景 E：缺少 PO 或未匹配**

```
IF 未找到采购订单 OR 没有匹配的行项目：
  1. 将 Match_Status 设为 "NO MATCH"
  2. 创建任务：“PO Not Found”
     - 分配给：采购团队
     - 优先级：高
  3. 向采购部门发送邮件
  4. 阻止文档处理
  5. 请求创建或更正采购订单
```

***

## 完整工作流图

```
发票到达
│
├─ 检查：发票是否包含采购订单编号？
│  │
│  ├─ 没有采购订单编号 ❌
│  │  │
│  │  ├─ 设置 Match_Status = "NO PO"（无采购订单）
│  │  ├─ 路由至非采购订单工作流
│  │  └─ 创建人工审核任务
│  │     → 结束（非采购订单发票）
│  │
│  └─ 存在采购订单编号 ✅
│     │
│     ├─ 检索采购订单数据
│     │  - 按 PO_Number 查找采购订单
│     │  - 获取采购订单行项目
│     │  - 获取采购订单总额
│     │  │
│     │  ├─ 找到采购订单 ✅
│     │  │  │
│     │  │  ├─ 步骤 1：检查是否完全匹配
│     │  │  │  卡片：PURCHASE_ORDER_FULL_MATCH
│     │  │  │  │
│     │  │  │  ├─ 完全匹配 ✅✅✅
│     │  │  │  │  │
│     │  │  │  │  ├─ 设置 Match_Status = "FULL MATCH"（完全匹配）
│     │  │  │  │  ├─ 自动批准
│     │  │  │  │  └─ 导出至 ERP
│     │  │  │  │     → 结束（完美匹配）
│     │  │  │  │
│     │  │  │  └─ 不完全匹配 ⚠️
│     │  │  │     │
│     │  │  │     ├─ 步骤 2：检查单价差异
│     │  │  │     │  卡片：CONDITION_DOC_TO_PO_UNIT_PRICE
│     │  │  │     │  容差：5%
│     │  │  │     │  │
│     │  │  │     │  ├─ 计算每个行项目的差异：
│     │  │  │     │  │  差异 % = |Invoice-PO|/PO × 100
│     │  │  │     │  │
│     │  │  │     │  ├─ 价格差异 ≤ 5% ✅
│     │  │  │     │  │  保存差异：3.2%（示例）
│     │  │  │     │  │  价格检查：通过
│     │  │  │     │  │
│     │  │  │     │  └─ 价格差异 > 5% ❌
│     │  │  │     │     保存差异：12.5%（示例）
│     │  │  │     │     价格检查：未通过
│     │  │  │     │     → 标记以供审核
│     │  │  │     │
│     │  │  │     ├─ 步骤 3：检查数量差异
│     │  │  │     │  卡片：CONDITION_DOC_TO_PO_QUANTITY
│     │  │  │     │  容差：10%
│     │  │  │     │  │
│     │  │  │     │  ├─ 计算每个行项目的差异：
│     │  │  │     │  │  差异 % = |Inv Qty-PO Qty|/PO Qty × 100
│     │  │  │     │  │
│     │  │  │     │  ├─ 数量差异 ≤ 10% ✅
│     │  │  │     │  │  保存差异：2.0%（示例）
│     │  │  │     │  │  数量检查：通过
│     │  │  │     │  │
│     │  │  │     │  └─ 数量差异 > 10% ❌
│     │  │  │     │     保存差异：15.0%（示例）
│     │  │  │     │     数量检查：未通过
│     │  │  │     │     → 标记以供审核
│     │  │  │     │
│     │  │  │     ├─ 步骤 4：检查税费行
│     │  │  │     │  卡片：CONDITION_DOC_TO_PO_TAX_LINES
│     │  │  │     │  │
│     │  │  │     │  ├─ 税费一致 ✅
│     │  │  │     │  │  税费检查：通过
│     │  │  │     │  │
│     │  │  │     │  └─ 税费不匹配 ❌
│     │  │  │     │     税费检查：未通过
│     │  │  │     │     → 标记以供审核
│     │  │  │     │
│     │  │  │     ├─ 评估结果
│     │  │  │     │  │
│     │  │  │     │  ├─ 所有检查均通过 ✅
│     │  │  │     │  │  （在容差范围内）
│     │  │  │     │  │  │
│     │  │  │     │  │  ├─ 设置 Match_Status = "WITHIN TOLERANCE"（在容差范围内）
│     │  │  │     │  │  ├─ 记录差异详情
│     │  │  │     │  │  ├─ 自动批准
│     │  │  │     │  │  └─ 导出至 ERP
│     │  │  │     │  │     → 结束（有差异但已批准）
│     │  │  │     │  │
│     │  │  │     │  ├─ 轻微未通过（差异 < 15%）⚠️
│     │  │  │     │  │  │
│     │  │  │     │  │  ├─ 设置 Match_Status = "REVIEW REQUIRED"（需要审核）
│     │  │  │     │  │  ├─ 创建审核任务
│     │  │  │     │  │  │  - 分配给：应付账款专员
│     │  │  │     │  │  │  - 优先级：Medium（中）
│     │  │  │     │  │  │  - 截止时间：3 days
│     │  │  │     │  │  ├─ 发送包含详情的电子邮件
│     │  │  │     │  │  │
│     │  │  │     │  │  └─ 等待任务完成
│     │  │  │     │  │     │
│     │  │  │     │  │     ├─ 任务已批准 ✅
│     │  │  │     │  │     │  批准并导出
│     │  │  │     │  │     │  → 结束（人工批准）
│     │  │  │     │  │     │
│     │  │  │     │  │     └─ 任务已拒绝 ❌
│     │  │  │     │  │        拒绝并退回给供应商
│     │  │  │     │  │        → 结束（已拒绝）
│     │  │  │     │  │
│     │  │  │     │  └─ 重大未通过（差异 ≥ 15%）🚨
│     │  │  │     │     │
│     │  │  │     │     ├─ 设置 Match_Status = "ESCALATION"（升级处理）
│     │  │  │     │     ├─ 创建紧急任务
│     │  │  │     │     │  - 分配给：采购经理
│     │  │  │     │     │  - 优先级：High（高）
│     │  │  │     │     │  - 截止时间：1 day
│     │  │  │     │     ├─ 向以下对象发送紧急电子邮件：
│     │  │  │     │     │  * 采购经理
│     │  │  │     │     │  * 财务经理
│     │  │  │     │     │  * 供应商
│     │  │  │     │     ├─ 阻止文档处理
│     │  │  │     │     │
│     │  │  │     │     └─ 等待问题解决
│     │  │  │     │        → 结束（等待升级处理）
│     │  │  │     │
│     │  │  │     └─ [差异检查已完成]
│     │  │  │
│     │  │  └─ [完全匹配检查已完成]
│     │  │
│     │  └─ 未找到采购订单 ❌
│     │     │
│     │     ├─ 设置 Match_Status = "PO NOT FOUND"（未找到采购订单）
│     │     ├─ 创建任务："Missing PO"（缺少采购订单）
│     │     │  - 分配给：采购团队
│     │     │  - 优先级：High（高）
│     │     ├─ 向采购团队发送电子邮件
│     │     └─ 阻止文档处理
│     │        → 结束（缺少采购订单）
│     │
│     └─ [采购订单检索已完成]
│
└─ [采购订单检查已完成]
```

***

## 配置模板

### 模板 1：标准 PO 匹配（保守）

```json
{
  "full_match_check": true,
  "price_variance": {
    "enabled": true,
    "tolerance_percent": 3,
    "tolerance_type": "percentage"
  },
  "quantity_variance": {
    "enabled": true,
    "tolerance_percent": 5,
    "tolerance_type": "percentage",
    "allow_under_delivery": true,
    "allow_over_delivery": false
  },
  "tax_validation": {
    "enabled": true,
    "match_tax_codes": true,
    "match_tax_rates": true,
    "tax_amount_tolerance": 0.5
  },
  "auto_approve": {
    "full_match": true,
    "within_tolerance": true
  },
  "escalation": {
    "threshold_percent": 10,
    "assign_to": "procurement_manager"
  }
}
```

**适用场景：** 控制严格、对差异容忍度低的环境

***

### 模板 2：灵活 PO 匹配（宽松）

```json
{
  "full_match_check": true,
  "price_variance": {
    "enabled": true,
    "tolerance_percent": 10,
    "tolerance_type": "percentage"
  },
  "quantity_variance": {
    "enabled": true,
    "tolerance_percent": 15,
    "tolerance_type": "percentage",
    "allow_under_delivery": true,
    "allow_over_delivery": true
  },
  "tax_validation": {
    "enabled": true,
    "match_tax_codes": false,
    "match_tax_rates": true,
    "tax_amount_tolerance": 2
  },
  "auto_approve": {
    "full_match": true,
    "within_tolerance": true
  },
  "escalation": {
    "threshold_percent": 20,
    "assign_to": "accounts_payable"
  }
}
```

**适用场景：** 灵活的环境、值得信赖的供应商、较高的容差

***

### 模板 3：仅匹配价格

```json
{
  "full_match_check": false,
  "price_variance": {
    "enabled": true,
    "tolerance_percent": 5,
    "tolerance_type": "percentage"
  },
  "quantity_variance": {
    "enabled": false
  },
  "tax_validation": {
    "enabled": false
  },
  "auto_approve": {
    "full_match": false,
    "within_tolerance": true
  }
}
```

**适用场景：** 仅关注价格且预期会有数量变化时

***

## 高级场景

### 场景 1：处理部分交付

**挑战：** 发票对应 PO 的部分交付

**解决方案：**

```
1. 允许在容差范围内交付不足
2. 跟踪累计开票数量与采购订单数量的对比
3. 更新采购订单剩余数量
4. 创建字段："PO_Percentage_Invoiced"
5. 开票达到 100% 时：自动关闭采购订单
```

**实施方式：**

```
IF Cumulative_Invoiced_Quantity ≤ PO_Quantity：
  计算：百分比 = (累计数量/采购订单数量) × 100
  存储于：PO_Percentage_Invoiced
  IF 百分比 ≥ 100：
    将 PO_Status 设为 "FULLY INVOICED"
    关闭采购订单
```

***

### 场景 2：多币种 PO 匹配

**挑战：** 发票币种与 PO 币种不同

**解决方案：**

```
1. 检测币种不匹配
2. 获取汇率（来自 API 或主数据）
3. 将发票金额转换为采购订单币种
4. 比较转换后的金额
5. 同时存储原始金额和转换后的金额
```

**实施方式：**

```
IF Invoice_Currency ≠ PO_Currency:
  1. 获取 Invoice_Currency → PO_Currency 的汇率
  2. 换算：Invoice_Amount_Converted = Invoice_Amount × Rate
  3. 比较：Invoice_Amount_Converted 与 PO_Amount
  4. 保存：Original_Currency_Amount 和 Converted_Amount
  5. 标记："Currency_Conversion_Applied"
```

***

### 场景 3：总括 PO / 框架协议

**挑战：** 多张发票对应同一 PO

**解决方案：**

```
1. 确定采购订单类型 = "Blanket"
2. 跟踪累计开票金额
3. 检查：累计金额 ≤ 总框架采购订单金额
4. 每张发票处理后更新采购订单剩余金额
5. 接近采购订单限额时发出提醒
```

**实施方式：**

```
IF PO_Type = "Blanket":
  计算：Total_Invoiced_To_Date
  检查：Total_Invoiced_To_Date + Current_Invoice ≤ PO_Total_Value
  IF 在限额内：
    批准发票
    更新：Remaining_PO_Value
  ELSE:
    升级处理："Blanket PO limit exceeded"（总括采购订单额度已超出）
```

***

## 错误处理和边缘情况

### 边缘情况 1：发票缺少行项目

**问题：** 发票上有 PO 中不存在的项目

**解决方案：**

```
1. 识别未匹配的行项目
2. 计算：Unmatched_Amount
3. IF Unmatched_Amount < €100（阈值）：
     创建审核任务（轻微问题）
   ELSE:
     立即升级处理（重大问题）
4. 保存未匹配项目的详情
5. 标记："Additional_Items_Present"
```

***

### 边缘情况 2：PO 已关闭，但收到发票

**问题：** PO 已关闭，之后才收到发票

**解决方案：**

```
1. 检查：PO_Status = "CLOSED"
2. 检查：Invoice_Date 与 PO_Close_Date
3. IF 发票日期在关闭日期后的 30 天内：
     暂时重新打开采购订单
     处理发票
     再次关闭采购订单
   ELSE:
     创建任务："Late Invoice for Closed PO"（已关闭采购订单的逾期发票）
     分配给采购部门
     需要人工决定
```

***

### 边缘情况 3：单张发票对应多个 PO

**问题：** 发票引用了多个 PO

**解决方案：**

```
1. 解析发票中的多个采购订单编号
2. 对每个采购订单：
     检索采购订单数据
     匹配对应的行项目
3. 汇总匹配结果
4. 总体匹配 = 所有单个采购订单都必须匹配
5. 分别报告每个采购订单的结果
```

***

## 性能提示

✅ **最佳实践：**

* 缓存 PO 数据，以减少查询次数
* 设置合适的容差（既不要太严格，也不要太宽松）
* 优先使用完整匹配检查（速度更快）
* 记录所有差异计算
* 每季度检查容差设置
* 监控自动审批率
* 跟踪常见差异原因

❌ **应避免：**

* 容差为零（过于严格，导致过多人工审核）
* 容差极高（失去控制目的）
* 忽略系统性差异
* 不跟踪差异趋势
* 在必须有 PO 的情况下无 PO 处理

***

## 监控和报告

### 要跟踪的关键指标

1. **匹配率：**
   * 完整匹配：X%
   * 在容差范围内：Y%
   * 超出容差范围：Z%
2. **差异分析：**
   * 平均价格差异
   * 平均数量差异
   * 常见差异原因
3. **处理效率：**
   * 自动审批率
   * 人工审核率
   * 平均审核时间
4. **供应商表现：**
   * 按供应商统计的差异
   * 按供应商统计的匹配率
   * 问题供应商

***

## 测试清单

* [ ] 完全匹配场景（完整匹配）
* [ ] 在容差范围内的场景（轻微差异）
* [ ] 超出容差范围的场景（严重差异）
* [ ] 缺少 PO 的场景
* [ ] PO 编号错误的场景
* [ ] 部分交付场景
* [ ] 超量交付场景
* [ ] 币种不匹配场景
* [ ] 多个 PO 场景
* [ ] PO 已关闭的场景
* [ ] 税项差异场景
* [ ] 升级处理工作流
* [ ] 创建任务
* [ ] 电子邮件通知
* [ ] 字段更新
* [ ] 审批后导出

***

## 相关模式

### 可配合使用的模式：

* [**任务管理模式**](task-management-pattern.md) - 为差异创建审核任务
* [**决策逻辑模式**](decision-logic-pattern.md) - 根据差异级别进行复杂路由
* [**API 集成模式**](api-integration-pattern.md) - 获取当前价格以供比较
* [**数据转换模式**](data-transformation-pattern.md) - 币种转换、单位转换

***

## 相关指南

### 前置条件

* [PO 匹配完整指南](../po-matching-complete-guide.md) - 所有 PO 匹配卡片
* [条件卡片指南](../condition-cards-complete-guide.md) - 条件逻辑
* [字段操作指南](../field-manipulation-guide.md) - 字段操作

### 相关卡片

* **PURCHASE\_ORDER\_FULL\_MATCH** - [PO 匹配指南](../po-matching-complete-guide.md#full-match)
* **CONDITION\_DOC\_TO\_PO\_UNIT\_PRICE** - [PO 匹配指南](../po-matching-complete-guide.md#unit-price)
* **CONDITION\_DOC\_TO\_PO\_QUANTITY** - [PO 匹配指南](../po-matching-complete-guide.md#quantity)
* **CONDITION\_DOC\_TO\_PO\_TAX\_LINES** - [PO 匹配指南](../po-matching-complete-guide.md#tax-lines)
* **tasks\_create** - [任务分配指南](../task-assignment-guide.md)

### 后续步骤

* 创建审核任务：[任务管理模式](task-management-pattern.md)
* 添加电子邮件通知：[发送电子邮件指南](../send-email-groups-guide.md)
* 实施复杂路由：[决策逻辑模式](decision-logic-pattern.md)

***

**模式版本：** 1.0 **最后更新：** 2025 年 10 月 23 日 **难度：** 中高 **预计时间：** 60-90 分钟 **成功率：** 高（正确配置时）
