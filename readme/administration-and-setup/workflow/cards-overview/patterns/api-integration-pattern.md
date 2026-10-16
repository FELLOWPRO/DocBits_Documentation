# API 集成模式

**模式类型：** 集成 **复杂度：** 中等 **预计设置时间：** 45-60 分钟 **常见使用场景：** 获取外部数据、价格验证、主数据查询

***

您可以在 **Workflow Builder**（工作流仪表板 → 工作流列表 → 添加工作流）中构建此模式。点击 **Add Card** 打开卡片库，并选择此模式使用的卡片 — `CALL_API`、`CONDITION_HTTPS_REQUEST_STATUS`、`ACTION_SET_FIELD_TO_TEXT` 和 `CONDITION_COMPARE_TWO_DOCFIELD_VALUES`：

<figure><img src="../../../../.gitbook/assets/workflow_add_card_picker.png" alt="Workflow Builder 中按类别分组的 Add Card 卡片库"><figcaption><p><strong>Add Card</strong> 卡片库 — 从这些类别中选择此模式使用的 API、条件和字段卡片。</p></figcaption></figure>

***

## 模式概述

此模式演示如何将 DocBits 与外部 API 集成，以从外部系统获取、验证和存储数据。这是将 DocBits 连接到定价系统、验证服务、ERP 系统及其他外部数据源时最常用的工作流模式之一。

**此模式的作用：**

1. 调用外部 API 获取数据
2. 验证 API 响应
3. 将响应数据存储到文档字段中
4. 根据获取的数据作出决策
5. 相应地路由文档

***

## 何时使用此模式

在以下情况下使用此模式：

* ✅ 从外部系统获取实时价格
* ✅ 根据主数据库验证供应商信息
* ✅ 从目录系统查询产品详情
* ✅ 从货币服务获取汇率
* ✅ 使用地理编码服务验证地址
* ✅ 从仓库系统检查库存水平
* ✅ 从税务服务验证税率

**以下情况不要使用此模式：**

* ❌ 数据已存在于 DocBits 主数据中（改用主数据查询）
* ❌ 外部系统没有 API（改用 DocOperator 脚本模式）
* ❌ 数据不常变化（可考虑手动导入）

***

## 完整工作流示例

### 场景：根据当前定价 API 验证发票价格

**业务需求：**

* 供应商发送发票
* 发票显示单价为 €52.00
* 我们需要确认该价格与当前供应商定价相符
* 如果价格偏差超过 5%，则升级处理以供审核

**使用的工作流卡片：**

1. CALL\_API - 从供应商 API 获取当前价格
2. CONDITION\_HTTPS\_REQUEST\_STATUS - 检查 API 调用是否成功
3. ACTION\_SET\_FIELD\_TO\_TEXT - 将 API 价格存储到文档字段
4. CONDITION\_COMPARE\_TWO\_DOCFIELD\_VALUES - 比较发票价格与 API 价格
5. ACTION\_ASSIGN\_TO\_USER - 根据比较结果进行路由
6. tasks\_create - 如有需要，创建审核任务

***

## 分步实施

### 步骤 1：调用外部 API

**卡片：** CALL\_API 或 ACTION\_CALL\_EXTERNAL\_API

**配置：**

```json
{
  "api_endpoint": "https://api.supplier-system.com/v1/pricing",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
  },
  "request_body": {
    "product_id": "{{DOCUMENT_FIELD:Product_Code}}",
    "supplier_id": "{{DOCUMENT_FIELD:Supplier_Code}}",
    "quantity": "{{DOCUMENT_FIELD:Quantity}}",
    "currency": "EUR"
  }
}
```

**预期响应：**

```json
{
  "success": true,
  "data": {
    "product_id": "ABC123",
    "unit_price": 50.00,
    "currency": "EUR",
    "valid_until": "2025-12-31",
    "discount_applicable": true
  }
}
```

**指南参考：** [调用 API 指南](../call-api-guide.md)

***

### 步骤 2：验证 API 响应

**卡片：** CONDITION\_HTTPS\_REQUEST\_STATUS

**配置：**

```
Operator: IS EQUAL TO
Status Code: 200
```

**逻辑：**

```
IF API returns 200 (success):
  → Continue to store data
ELSE:
  → Route to "API Error" handling workflow
  → Send email notification
  → Create manual review task
```

**指南参考：** [条件卡片指南 - HTTP 状态](../condition-cards-complete-guide.md#condition-https-request-status)

***

### 步骤 3：将 API 响应存储到文档字段

**卡片：** ACTION\_SET\_FIELD\_TO\_TEXT（或等效字段设置卡片）

**配置：**

**字段 1：Current\_API\_Price**

```
Field Name: Current_API_Price
Field Value: {{API_RESPONSE:data.unit_price}}
Field Type: Number
```

**字段 2：API\_Price\_Valid\_Until**

```
Field Name: API_Price_Valid_Until
Field Value: {{API_RESPONSE:data.valid_until}}
Field Type: Date
```

**字段 3：API\_Discount\_Available**

```
Field Name: API_Discount_Available
Field Value: {{API_RESPONSE:data.discount_applicable}}
Field Type: Boolean
```

**结果：** API 中的数据现在已存储在文档字段中，供后续使用

**指南参考：** [字段操作指南 - API 数据存储](../field-manipulation-guide.md#storing-api-data)

***

### 步骤 4：比较发票价格与 API 价格

**卡片：** CONDITION\_COMPARE\_TWO\_DOCFIELD\_VALUES

**配置：**

```
Field 1: Invoice_Unit_Price (from OCR extraction)
Field 2: Current_API_Price (from API response)
Operator: Calculate variance percentage
Tolerance: 5%
```

**计算：**

```
Variance % = |(Invoice_Price - API_Price)| / API_Price × 100

Example:
  Invoice Price: €52.00
  API Price: €50.00
  Variance = |52 - 50| / 50 × 100 = 4%

  Is 4% ≤ 5% tolerance? YES ✅
  Result: PASS
```

**指南参考：** [条件卡片指南 - 字段比较](../condition-cards-complete-guide.md)

***

### 步骤 5：根据验证结果进行路由

**场景 A：价格在容差范围内（通过）**

**卡片：**

* ACTION\_SET\_FIELD\_TO\_TEXT
  * 将字段 "Price\_Validation\_Status" 设置为 "PASS"
  * 将字段 "Price\_Variance\_Percent" 设置为 "4%"
* ACTION\_APPROVE\_DOCUMENT
  * 自动审批文档

**场景 B：价格超出容差范围（失败）**

**卡片：**

* ACTION\_SET\_FIELD\_TO\_TEXT
  * 将字段 "Price\_Validation\_Status" 设置为 "FAIL"
  * 将字段 "Price\_Variance\_Percent" 设置为 "12%"（示例）
* tasks\_create
  * 任务标题："Review Price Variance - \{{DOCUMENT\_NUMBER\}}"
  * 任务描述："发票价格 (€\{{Invoice\_Unit\_Price\}}) 比 API 价格 (€\{{Current\_API\_Price\}}) 高出 \{{Price\_Variance\_Percent\}}"
  * 优先级：高
* ACTION\_ASSIGN\_TO\_USER
  * 分配给：采购经理
* ACTION\_SEND\_EMAIL\_TO\_GROUPS
  * 向采购团队发送通知

**指南参考：**

* [分配指南](../assignment-user-guide.md)
* [任务分配指南](../task-assignment-guide.md)
* [发送邮件指南](../send-email-groups-guide.md)

***

## 完整工作流图

```
文档到达（发票，包含产品 ABC123，价格 €52）
│
├─ 步骤 1：调用定价 API
│  卡片：CALL_API
│  请求：获取 ABC123 的当前价格
│  │
│  ├─ 成功 (200) ✅
│  │  响应：{"unit_price": 50.00}
│  │  │
│  │  ├─ 步骤 2：检查 API 状态
│  │  │  卡片：CONDITION_HTTPS_REQUEST_STATUS
│  │  │  结果：200 = 成功
│  │  │  │
│  │  │  ├─ 步骤 3：存储 API 数据
│  │  │  │  卡片：ACTION_SET_FIELD_TO_TEXT
│  │  │  │  操作：将 €50 存入 "Current_API_Price" 字段
│  │  │  │  │
│  │  │  │  ├─ 步骤 4：比较价格
│  │  │  │  │  卡片：CONDITION_COMPARE_TWO_DOCFIELD_VALUES
│  │  │  │  │  计算：偏差 = |52-50|/50 = 4%
│  │  │  │  │  │
│  │  │  │  │  ├─ IF 偏差 ≤ 5%（通过）✅
│  │  │  │  │  │  │
│  │  │  │  │  │  ├─ 设置状态字段："PASS"
│  │  │  │  │  │  └─ 自动批准文档
│  │  │  │  │  │     → 结束（文档已批准）
│  │  │  │  │  │
│  │  │  │  │  └─ IF 偏差 > 5%（失败）❌
│  │  │  │  │     │
│  │  │  │  │     ├─ 设置状态字段："FAIL"
│  │  │  │  │     ├─ 创建审核任务
│  │  │  │  │     ├─ 分配给采购经理
│  │  │  │  │     └─ 发送电子邮件通知
│  │  │  │  │        → 结束（等待审核）
│  │  │  │  │
│  │  │  │  └─ [字段存储完成]
│  │  │  │
│  │  │  └─ [状态检查完成]
│  │  │
│  │  └─ [API 数据已获取]
│  │
│  └─ 错误（非 200）❌
│     │
│     ├─ 设置错误状态
│     ├─ 创建 "API Error"（API 错误）任务
│     ├─ 分配给 IT 支持人员
│     └─ 向管理员发送电子邮件
│        → 结束（API 错误 - 人工审核）
```

***

## 配置模板

### 模板 1：简单 GET 请求（查询）

```json
{
  "card": "CALL_API",
  "endpoint": "https://api.example.com/lookup",
  "method": "GET",
  "headers": {
    "Authorization": "Bearer {{API_KEY}}"
  },
  "parameters": {
    "id": "{{DOCUMENT_FIELD:Lookup_ID}}"
  }
}
```

**用途：** 按 ID 简单查询数据

***

### 模板 2：带请求正文的 POST 请求（验证）

```json
{
  "card": "CALL_API",
  "endpoint": "https://api.example.com/validate",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer {{API_KEY}}",
    "Content-Type": "application/json"
  },
  "body": {
    "document_number": "{{DOCUMENT_NUMBER}}",
    "supplier_id": "{{DOCUMENT_FIELD:Supplier_Code}}",
    "total_amount": "{{DOCUMENT_FIELD:Total_Amount}}",
    "currency": "{{DOCUMENT_FIELD:Currency}}"
  }
}
```

**用途：** 发送文档数据以进行验证

***

### 模板 3：包含嵌套数据的复杂请求

```json
{
  "card": "CALL_API",
  "endpoint": "https://api.example.com/process",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer {{API_KEY}}",
    "Content-Type": "application/json"
  },
  "body": {
    "document": {
      "type": "{{DOCUMENT_TYPE}}",
      "number": "{{DOCUMENT_NUMBER}}",
      "date": "{{DOCUMENT_FIELD:Invoice_Date}}"
    },
    "vendor": {
      "code": "{{DOCUMENT_FIELD:Supplier_Code}}",
      "name": "{{DOCUMENT_FIELD:Supplier_Name}}"
    },
    "items": [
      {
        "product": "{{TABLE_FIELD:Product_Code}}",
        "quantity": "{{TABLE_FIELD:Quantity}}",
        "unit_price": "{{TABLE_FIELD:Unit_Price}}"
      }
    ]
  }
}
```

**用途：** 使用表格数据处理复杂文档

***

## 错误处理 <a id="error-handling"></a>

### 常见错误及解决方案

#### 错误 1：连接超时

**症状：**

* API 没有响应
* 工作流一直处于等待状态

**解决方案：**

```
1. 检查 API 端点 URL（是否有拼写错误？）
2. 验证网络连接
3. 检查 API 服务状态
4. 实施超时处理：

   IF CONDITION_HTTPS_REQUEST_STATUS = TIMEOUT:
     → 创建 "API Timeout"（API 超时）任务
     → 分配给 IT 支持人员
     → 发送电子邮件通知
     → 使用备用值（如果有）
```

#### 错误 2：401 未授权

**症状：**

* API 返回 401 状态
* 身份验证失败

**解决方案：**

```
1. 验证 API 密钥是否正确
2. 检查 API 密钥是否已过期
3. 确保 Authorization 标头格式正确
4. 实施身份验证错误处理：

   IF CONDITION_HTTPS_REQUEST_STATUS = 401:
     → 创建 "API Auth Failed"（API 身份验证失败）任务
     → 分配给管理员
     → 记录错误详情
     → 停止工作流执行
```

#### 错误 3：响应格式无效

**症状：**

* 已收到响应，但无法解析
* 缺少预期字段

**解决方案：**

```
1. 查阅 API 文档
2. 检查响应结构是否符合预期
3. 实施响应验证：

   IF API_RESPONSE:data.unit_price IS NULL:
     → 设置默认值
     → 创建 "Invalid Response"（无效响应）任务
     → 记录响应以便调试
```

**指南参考：** [调用 API 故障排除](../call-api-guide.md#troubleshooting)

***

## 高级变体

### 变体 1：多 API 链式调用

**场景：** 需要从多个 API 获取数据

```
步骤 1：调用供应商 API → 获取供应商详情
步骤 2：调用产品 API → 获取产品信息（使用步骤 1 中的供应商 ID）
步骤 3：调用定价 API → 获取价格（使用步骤 2 中的产品 ID）
步骤 4：验证并存储所有数据
```

***

### 变体 2：条件式 API 调用

**场景：** 仅在满足特定条件时调用 API

```
IF DOCUMENT_TYPE = "Invoice" AND AMOUNT > 10000:
  → Call Pricing Validation API
  → Verify prices
ELSE:
  → Skip API call (not needed for small amounts)
```

***

### 变体 3：API 响应缓存

**场景：** 通过缓存响应减少 API 调用

```
1. 检查 "API_Last_Called" 日期是否为今天
2. IF 是：
     → 使用 "Cached_API_Price" 字段中的缓存值
3. IF 否：
     → 调用 API
     → 将响应存储在 "Cached_API_Price" 中
     → 将 "API_Last_Called" 设为今天
```

***

## 性能注意事项

### 最佳实践

✅ **建议：**

* 尽可能缓存 API 响应
* 使用超时设置（30-60 秒）
* 为临时故障实现重试逻辑
* 记录 API 调用以便调试
* 监控 API 使用量/费用
* 先使用示例文档进行测试

❌ **避免：**

* 对每个文档都同步调用 API（可考虑批量处理）
* 忽略响应错误
* 在工作流中硬编码凭据
* 进行不必要的 API 调用
* 忘记处理超时

***

## 测试清单

部署此模式之前：

* [ ] 使用有效数据测试 API 调用
* [ ] 使用无效数据测试 API 调用
* [ ] 测试超时场景（API 响应缓慢时会发生什么？）
* [ ] 测试身份验证失败
* [ ] 测试无效的响应格式
* [ ] 测试字段存储（数据是否正确存储？）
* [ ] 测试比较逻辑（计算是否正确？）
* [ ] 测试路由（文档是否被发送到正确位置？）
* [ ] 测试错误处理（是否能妥善处理错误？）
* [ ] 使用高流量进行测试（性能是否可接受？）

***

## 实际示例

### 示例 1：查询货币汇率 <a id="currency-conversion-example"></a>

**API：** https://api.exchangerate-api.com/v4/latest/USD

**工作流：**

1. 提取发票币种："GBP"
2. 调用汇率 API
3. 获取 GBP→EUR 汇率
4. 计算 EUR 等值金额
5. 存储到 "Amount\_EUR" 字段
6. 使用 EUR 金额继续处理

***

### 示例 2：供应商信用检查

**API：** 内部信用检查服务

**工作流：**

1. 提取供应商代码
2. 调用信用检查 API
3. 获取信用状态："APPROVED" 或 "BLOCKED"
4. 如果状态为 BLOCKED：
   * 停止处理
   * 创建紧急任务
   * 通知财务团队
5. 如果状态为 APPROVED：
   * 继续正常工作流

***

### 示例 3：产品主数据补充

**API：** 产品目录服务

**工作流：**

1. 从发票中提取产品代码
2. 调用产品 API
3. 获取：产品名称、类别、GL 科目
4. 存储到文档字段
5. 用于自动记账

***

## 相关模式

### 此模式适合搭配：

* [**数据转换模式**](data-transformation-pattern.md) - 转换 API 响应数据
* [**决策逻辑模式**](decision-logic-pattern.md) - 根据 API 数据进行路由
* [**任务管理模式**](task-management-pattern.md) - 为 API 错误创建任务
* [**采购订单匹配模式**](po-matching-pattern.md) - 将 API 定价与采购订单验证相结合

***

## 相关指南

### 前置指南

* [调用 API 指南](../call-api-guide.md) - API 卡片文档
* [条件卡片指南](../condition-cards-complete-guide.md) - 条件逻辑
* [字段操作指南](../field-manipulation-guide.md) - 字段操作

### 相关卡片

* **CALL\_API** - [调用 API 指南](../call-api-guide.md)
* **ACTION\_HTTPS\_REQUEST** - [HTTPS 请求指南](../https-request-guide.md)
* **CONDITION\_HTTPS\_REQUEST\_STATUS** - [条件卡片指南](../condition-cards-complete-guide.md#condition-https-request-status)
* **ACTION\_SET\_FIELD\_TO\_TEXT** - [字段操作指南](../field-manipulation-guide.md#set-field)
* **CONDITION\_COMPARE\_TWO\_DOCFIELD\_VALUES** - [条件卡片指南](../condition-cards-complete-guide.md)

### 后续步骤

* 解决 API 错误：[错误处理](api-integration-pattern.md#error-handling)（见上文）
* 添加任务创建：[任务管理模式](task-management-pattern.md)
* 转换数据：[数据转换模式](data-transformation-pattern.md)

***

## 支持与资源

**需要帮助？**

* 查看[调用 API 故障排除](../call-api-guide.md#troubleshooting)
* 查看 [API 响应代码](../call-api-guide.md#response-scenarios)
* 先使用 Postman 测试 API
* 联系 API 提供商支持

**反馈：**

* 将模式问题报告至：docs@docbits.com
* 提出改进建议
* 分享您的使用场景

***

**模式版本：** 1.0 **最后更新：** 2025 年 10 月 23 日 **难度：** 中等 **预计时间：** 45-60 分钟 **成功率：** 高（API 稳定时）
