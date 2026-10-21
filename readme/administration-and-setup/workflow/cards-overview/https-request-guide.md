# 发送 HTTPS 请求

***

将此卡添加到工作流程生成器的 **则** 组 — 一旦“何时/与”条件匹配就会运行的操作：

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-zh.png" alt="包含“当”“且”和“则”卡片的未保存示例。执行前请配置所有占位字段。 此版本界面的部分标签尚未翻译或翻译不准确。本页说明使用正确术语；图片保留了实际界面。"><figcaption><p>包含“当”“且”和“则”卡片的未保存示例。执行前请配置所有占位字段。 此版本界面的部分标签尚未翻译或翻译不准确。本页说明使用正确术语；图片保留了实际界面。</p></figcaption></figure>

***

## 📌 版本信息

**当前版本：** v2（最新和推荐）**状态：**✅活跃

**版本历史：**

* v1 → 简单的 HTTP 请求（不再推荐）
* **v2 → CURRENT**（添加多语言支持）

**更改内容：** v2 添加了国际化 (i18n) 支持。核心 webhook/请求功能保持不变。

📖 【版本历史及变更](../release.md) | 【完整卡牌数据库](export-cards-guide.md)

***

## 目的

该卡向网站或服务发送安全消息，并可以接收回复。它比“调用 API”卡更简单，并且对于快速集成很有用。

**真实示例：** 将发票数据发送到您的会计系统，或询问外部系统是否批准员工处理此采购。

***

## 何时使用此卡

当您需要时使用此卡：

* 向外部服务发送 webhook 通知
* 触发其他系统中的操作
* 查询一个简单的Web服务
* 将状态更新发送到其他应用程序
* 执行简单的集成，无需复杂的 API 要求

***

## 它是如何运作的

1. **触发检查**：系统检查“Where”和“And”条件是否满足
2. **构建请求**：系统使用您的参数准备HTTPS请求
3. **安全发送**：使用安全 HTTPS 连接发送数据
4. **接收响应**：外部服务响应
5. **Continue**：工作流程继续处理响应数据

***

## 参数

### 网址

发送请求的网站地址

**示例：** `https://webhook.company.com/process`

### 标头

给收件人的特别说明

**示例：**

```
Content-Type: application/json
Authorization: Bearer token123
```

### 方法

* **GET**：请求信息
* **POST**：发送数据
* **PUT**：更新数据

### 参数（查询字符串）

添加到 URL 的数据

**示例：** `?action=approve&user_id=123`

### 请求数据

实际发送的信息（JSON 格式）

**示例：**

```json
{
  "invoice_number": "INV-2025-001",
  "amount": 5000,
  "currency": "EUR"
}
```

***

## 分步示例

### 场景：将发票发送到会计系统

**卡片配置：**

* **网址:**`https://accounting.company.com/invoices/create`
* **方法：** POST
* **标题：**`Authorization: Bearer YOUR-TOKEN`
* **请求数据：**

```json
{
  "supplier_id": "SUPP001",
  "invoice_number": "12345",
  "amount": 1500.00,
  "currency": "EUR",
  "date": "2025-10-23"
}
```

**预期响应：**

```json
{
  "status": "success",
  "accounting_id": "ACC-98765",
  "message": "Invoice recorded in accounting system"
}
```

***

## 常见用例

### 1.Webhook通知

当 DocFlow 中发生任何情况时，向其他系统发送实时通知

**示例：**

* 文件批准 → 发送通知至履行系统
* 供应商变更 → 通过 Slack/Teams webhook 通知采购团队

### 2. 外部系统集成

将DocFlow与其他业务系统连接，实现数据自动交换

**示例：**

* 文件处理后→同步至ERP系统
* 添加新供应商 → 在主数据系统中创建供应商记录

### 3. 审批流程

将文件发送到外部审批系统并接收决定

**示例：**

* 大额发票 → 送财务审批
* 将文档返回给外部系统并做出决定

***

## 配置指南

### 第1步：获取端点信息

向接收系统询问：

* [ ] HTTPS 网址
* [ ] 必需的标头
* [ ] 认证方式
* [ ] 预期的请求格式
* [ ] 预期响应格式

### 第 2 步：配置卡

1. 输入 HTTPS 网址
2. 设置HTTP方法（通常是POST）
3. 如果需要，添加身份验证
4. 将请求数据格式化为 JSON
5. 添加任何自定义标头

### 第三步：测试

发送测试请求并验证响应

***

## 响应处理

您的 HTTPS 请求将得到响应。常见回应：

### 成功 (200, 201)

```json
{
  "success": true,
  "id": "REC-12345",
  "status": "processed"
}
```

### 错误请求 (400)

```json
{
  "error": "Missing required field: invoice_number"
}
```

### 未经授权 (401)

```json
{
  "error": "Invalid authentication token"
}
```

### 服务器错误 (500)

接收系统有内部问题

***

## 故障排除

### “证书错误”

**原因：** HTTPS安全证书问题

**解：**

* 验证 URL 是否正确
* 检查网站证书是否有效
* 确保您使用的是 HTTPS（不是 HTTP）

### “连接被拒绝”

**原因：**无法连接服务器

**解：**

* 验证 URL/IP 地址是否正确
* 检查服务是否正在运行
* 检查防火墙规则
* 验证互联网连接

### “无响应/超时”

**原因：** 服务器未在限定时间内响应

**解：**

* 检查服务是否可用
* 验证端点 URL
* 检查是否有速率限制
* 联系系统管理员

### “无效的 JSON”

**原因：**请求数据格式错误

**解：**

* 检查 JSON 中是否缺少逗号
* 验证所有报价是否正确
* 验证 JSON 格式（使用在线 JSON 验证器）
* 检查特殊字符

***

## 示例

### 示例 1：发送到 Webhook 服务

```
URL: https://webhook.site/your-unique-id
Method: POST
Data:
{
  "document_id": "DOC-123",
  "status": "approved",
  "amount": 5000
}
```

### 示例 2：更新外部系统

```
URL: https://api.company.com/update
Method: PUT
Data:
{
  "record_id": "REC-456",
  "status": "completed",
  "timestamp": "2025-10-23T10:30:00"
}
```

### 示例3：查询外部服务

```
URL: https://lookup.company.com/validate?id=SUP-789
Method: GET
Headers: Authorization: Bearer token
```

***

## 与“调用API”卡的区别

| 特点        | HTTPS 请求      | 调用API          |
| -------------- | ------------------ | ----------------- |
| 简单性     | 简单             | 更复杂      |
| 参数     | 基础              | 高级          |
| 错误处理 | 基础              | 详细          |
| 用于        | 快速集成 | 复杂的API      |
| 最适合       | 网络钩子           | 专业API |

***

## 安全考虑

✅ **始终使用HTTPS**（安全连接）

⚠️**从不：**

* 将密码放入 URL 中
* 在日志中公开 API 密钥
* 在参数中包含个人数据
* 对敏感数据使用 HTTP

***

## 最佳实践

✅ **做：**

* 首先用少量数据进行测试
* 包括错误处理
* 记录重要请求
* 记录集成
* 监控故障

❌**不要：**

* 如果不需要，重复调用同一端点
* 忽略响应错误
* 以纯文本形式包含敏感数据
* 超出服务速率限制

***

## 相关卡牌

* **CALL\_API** - 更高级的 API 集成
* **CONDITION\_HTTPS\_REQUEST\_STATUS** - 检查请求是否成功
* **ACTION\_SEND\_EMAIL** - 通过电子邮件发送
* **ACTION\_RUN\_DOCOPERATOR\_SCRIPT** - 自动化脚本

<!-- workflow-card-complete-example-20261021 action_https_request -->

### HTTPS 操作示例

**配置：** 选择方法`POST`，将`DEMO_WEBHOOK_URL`替换为您授权的测试端点，添加标头`Content-Type: application/json`和正文`{"document_number":"DEMO-001"}`。仅根据该端点的需要配置身份验证；永远不要将真正的秘密复制到文档中。

**预期结果和反例：**操作在其工作流路由执行时发送配置的请求。检查 HTTP 响应和接收测试服务。超时并不能证明服务没有执行任何操作，并且此“Then”操作与检查 HTTP 状态的“And”卡是分开的。该说明性请求尚未发送。

这是一个说明性的测试配置和预期结果；它没有被执行。使用测试组织中配置的数据和收件人。
