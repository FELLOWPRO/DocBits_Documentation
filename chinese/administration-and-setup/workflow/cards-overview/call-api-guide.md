# 调用外部 API

***

将此卡片添加到工作流构建器的 **Then** 分组中。该分组包含在 When/And 条件匹配后运行的操作：

<figure><img src="../../../.gitbook/assets/workflow_designer_cards.png" alt="包含 When、And 和 Then 卡片分组的工作流构建器画布"><figcaption><p>通过 <strong>Add Card</strong> 将 <strong>Call External API</strong> 卡片添加到 <strong>Then</strong> 分组。</p></figcaption></figure>

***

## 📌 版本信息

**当前版本：** v2（最新且推荐） **状态：** ✅ 已启用

**版本历史：**

* v1 → 基本 API 调用（不再推荐）
* **v2 → 当前版本**（新增多语言支持）

**变更内容：** v2 新增了国际化（i18n）支持和翻译键。功能保持不变。

📖 [版本历史与变更](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/administration-and-setup/changelog/release.md#1-call_api) | [完整卡片数据库](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/DocFlow/docs/card_version.md#call_api)

***

## 用途

此卡片可让你向外部网站或服务发送数据，并接收返回的信息。可以把它想象成向外部服务提问，并获得一个可在工作流中使用的答案。

**实际示例：** 你的公司在另一个网站上使用定价系统。此卡片可以自动向该定价系统查询某个商品的当前价格，并将价格带入文档。

***

## 何时使用此卡片

在以下情况下使用此卡片：

* 从外部服务获取信息（例如定价、验证或查询数据）
* 将文档信息发送到其他系统进行处理
* 与第三方服务集成
* 自动获取数据，无需手动查询
* 连接多个业务系统

**常见场景：**

* 从数据库查询供应商信息
* 从定价服务获取实时价格
* 根据外部系统验证数据
* 从物流服务商获取运输信息

***

## 工作原理

1. **条件检查**：工作流首先检查“Where”和“And”部分中的条件是否满足
2. **准备数据**：卡片收集你配置的参数
3. **发送请求**：将数据发送到外部 API/服务
4. **接收响应**：外部服务返回数据
5. **继续执行**：工作流在后续卡片中使用这些数据

***

## 参数说明

### API 端点 URL

**含义：** 你要与之通信的外部服务地址

**示例：** `https://api.supplier-system.com/product/pricing`

**如何获取：** 向 IT 团队或服务提供商索取其 API 端点

***

### HTTP 方法

**含义：** 要发送的请求类型

**选项：**

* **GET**：请求信息（例如提出查询）
* **POST**：发送新数据
* **PUT**：更新现有数据
* **DELETE**：删除数据

**最常用：** GET（用于获取信息）

***

### 请求头

**含义：** 发给所调用服务的附加指令

**示例：**

```
Authorization: Bearer your-api-key
Content-Type: application/json
```

**用途：** 服务通常需要身份验证信息或特定的格式说明

***

### 参数（查询参数）

**含义：** 在 URL 中传递的额外信息

**示例：**

```
?supplier_id=12345&currency=USD
```

**实际示例：** 如果要查询价格，参数可能包括供应商 ID 和货币

***

### 请求数据（正文）

**含义：** 发送给服务的信息

**示例：**

```json
{
  "product_id": "ABC123",
  "quantity": 100,
  "currency": "EUR"
}
```

**适用情况：** 使用 POST 或 PUT 方法时

***

## 分步示例

### 场景：获取供应商实时价格

**设置：**

1. **卡片类型：** Call API
2. **API 端点：** `https://api.suppliers.com/v1/prices`
3. **方法：** POST
4. **请求头：** `Authorization: Bearer YOUR-API-KEY`
5.  **请求数据：**

    ```json
    {
      "product_id": "ABC123",
      "quantity": 100
    }
    ```

**执行过程：**

1. 收到文档，其中包含产品 ID：ABC123、数量：100
2. 卡片向供应商 API 发送请求
3. 供应商 API 返回：`{"unit_price": 25.50, "total_price": 2550}`
4. 工作流使用此价格信息继续执行
5. 下一个卡片可以使用这些数据验证发票价格

***

## 配置步骤

### 1. 获取 API 信息

联系外部服务提供商并索取：

* [ ] API 端点 URL
* [ ] 身份验证方法（API 密钥、用户名/密码、OAuth）
* [ ] 必需参数
* [ ] 预期的响应格式
* [ ] 速率限制或配额

### 2. 配置卡片

1. 输入 API 端点 URL
2. 选择 HTTP 方法（通常为 GET 或 POST）
3. 如有需要，添加身份验证请求头
4. 添加必需的参数
5. 如有需要，将请求数据设置为 JSON 格式

### 3. 测试卡片

1. 使用测试文档
2. 运行工作流
3. 检查是否正确收到响应
4. 验证数据格式是否符合预期

***

## 常见响应场景 <a id="response-scenarios"></a>

### 成功响应（状态码 200）

```json
{
  "success": true,
  "data": {
    "price": 150,
    "currency": "EUR",
    "delivery_days": 5
  }
}
```

✅ 数据可供后续卡片使用

### 错误响应（状态码 404）

```json
{
  "error": "Product not found"
}
```

⚠️ API 未能找到你要查询的内容

### 超时

外部服务未在时限内响应 ⚠️ 检查服务是否可用，或端点 URL 是否正确

***

## 工作流示例

### 示例 1：自动验证价格

**场景：** 根据供应商当前定价验证发票价格

**流程：**

1. 收到包含发票行项目的文档（产品：A123，价格：€50）
2. **Call API 卡片** → 向供应商 API 查询：“A123 的当前价格是多少？”
3. 供应商返回：“€48”
4. **Condition 卡片** → 检查发票价格（€50）是否在当前价格（€48）的 5% 范围内
5. **Approval 卡片** → 如果在容差范围内，则批准

### 示例 2：自动查询供应商

**场景：** 从中央数据库获取供应商主数据

**流程：**

1. 收到包含供应商代码 SUPP-789 的发票
2. **Call API 卡片** → 向系统查询：“提供供应商 SUPP-789 的详细信息”
3. 系统返回：名称、联系人、条款等
4. **Set Field 卡片** → 使用这些数据填充文档字段
5. **Export 卡片** → 导出包含完整信息的文档

### 示例 3：实时运输费用

**场景：** 根据目的地自动获取运输费用

**流程：**

1. 文档中包含交货地址
2. **Call API 卡片** → 向运输服务商查询：“运送到 \[address] 的费用是多少？”
3. 服务商返回运输费用
4. **Calculate 卡片** → 将运输费用计入发票总金额
5. **Export 卡片** → 发送更新后的总金额

***

## 故障排除 <a id="troubleshooting"></a>

### “Connection Timeout”错误

**原因：** API 服务没有响应

**解决方案：**

* [ ] 检查服务是否可用（访问其网站）
* [ ] 确认端点 URL 正确（没有拼写错误）
* [ ] 检查互联网连接
* [ ] 联系服务提供商
* [ ] 检查服务是否设有速率限制（请求发送过多）

### “Unauthorized”或“403 Forbidden”错误

**原因：** 身份验证失败

**解决方案：**

* [ ] 确认 API 密钥正确
* [ ] 检查 API 密钥是否已过期
* [ ] 确保身份验证请求头的格式正确
* [ ] 确认你拥有访问此端点的权限

### “Bad Request”或“400 Error”

**原因：** 请求数据格式不正确

**解决方案：**

* [ ] 检查 JSON 语法（是否缺少逗号、引号等）
* [ ] 确认包含所有必需字段
* [ ] 检查参数名称是否与服务要求一致
* [ ] 查阅 API 文档

### “Response not working as expected”

**解决方案：**

* [ ] 使用 Postman 等工具测试 API
* [ ] 比较实际响应格式与预期格式
* [ ] 检查 API 文档是否有变更
* [ ] 确认发送的数据正确

***

## 使用响应数据

从 API 获取数据后，后续卡片可以使用这些数据：

```
API Response:
{
  "unit_price": 45.00,
  "currency": "USD",
  "available": true
}

Next Card (Set Field):
- Set "Unit_Price" field to 45.00
- Set "Currency" field to USD
- Set "In_Stock" checkbox to true
```

***

## 安全说明

⚠️ **重要：** 切勿在其他用户可能看到的卡片配置中填写敏感信息

* 不要将密码硬编码
* 安全地使用 API 密钥
* 不要在日志中包含个人数据
* 使用 HTTPS 端点（不要使用 HTTP）

***

## 提示与最佳实践

✅ **建议：**

* 先用少量文档进行测试
* 保持 API 调用简单且目标明确
* 使用 Condition 卡片添加错误处理
* 监控 API 用量/费用
* 为团队记录 API 要求

❌ **避免：**

* 如果可以缓存数据，就不要对每个请求都调用 API
* 不要忽略响应错误代码
* 不要在生产环境中使用测试 API
* 不要忘记添加身份验证请求头
* 不要假设 API 始终可用

***

## 相关卡片

* **ACTION\_HTTPS\_REQUEST** - 类似但更简单的 HTTPS 请求
* **CONDITION\_HTTPS\_REQUEST\_STATUS** - 检查 API 调用是否成功
* **ACTION\_SEND\_EMAIL** - 通过电子邮件而不是 API 发送数据
* **CALL\_API**（不同版本）- 另一种 API 调用方法

***

## 需要帮助？

* 向 IT/集成团队索取 API 文档
* 先使用 Postman 工具测试 API 端点
* 查看服务提供商的支持门户
* 查阅 API 文档，了解所需格式
