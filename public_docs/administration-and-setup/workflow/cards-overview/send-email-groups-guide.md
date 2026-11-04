# 向群组发送电子邮件

***

将此卡添加到工作流程生成器的 **则** 组 — 一旦“何时/与”条件匹配就会运行的操作：

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-zh.png" alt="包含“当”“且”和“则”卡片的未保存示例。执行前请配置所有占位字段。 此版本界面的部分标签尚未翻译或翻译不准确。本页说明使用正确术语；图片保留了实际界面。"><figcaption><p>包含“当”“且”和“则”卡片的未保存示例。执行前请配置所有占位字段。 此版本界面的部分标签尚未翻译或翻译不准确。本页说明使用正确术语；图片保留了实际界面。</p></figcaption></figure>

***

## 📌 版本信息

**状态：**✅单一版本（无重大更改）**最新版本：**v1（活动）**注意：**此卡使用单一版本模型，通过翻译键支持多语言。

📖【完整卡牌数据库](export-cards-guide.md)

***

## 目的

该卡会自动向用户组发送电子邮件通知。您无需将工作分配给个人，而是将消息发送给一个组，然后该组的所有成员都会收到该消息。

**真实示例：** 当高额发票到达时，自动向“财务团队”组中的每个人发送电子邮件通知，以便他们知道需要审核。

***

## 何时使用此卡

当您需要时使用此卡：

* 一次通知多人
* 向团队组发送警报
* 向各部门广播更新情况
* 通知群组有关文档状态更改的信息
* 向群组成员发送提醒

**常见场景：**

* 通知采购团队有关新供应商的信息
* 提醒财务团队有关高额发票的信息
* 通知仓库团队有关发货的信息
* 广播文档状态变化

***

## 它是如何运作的

1. **条件检查**：工作流程检查“Where”和“And”条件
2. **准备电子邮件**：系统使用模板准备电子邮件
3. **获取群组成员**：系统查找指定群组的所有成员
4. **发送**：电子邮件发送给每个群组成员
5. **Log**：邮件发送记录

***

## 参数解释

### 电子邮件模板

要发送的电子邮件消息

**选项：**

* 从现有模板中选择
* 每个模板都有预定义的主题、正文和格式
* 模板可以包含占位符，例如 {document\_number}、{supplier\_name}

**示例模板：**

```
Subject: Document {document_number} requires review

Body:
Dear Team,

A new invoice has arrived and requires review:
- Document: {document_number}
- Supplier: {supplier_name}
- Amount: {amount} {currency}
- Date: {date}

Please login to DocBits to review.

Best regards,
DocBits Automation
```

### 集团

向其发送电子邮件的用户组

**示例组：**

* 财务团队
* 采购团队
* 仓储团队
* 审批委员会
* 管理组

***

## 配置步骤

### 第 1 步：选择电子邮件模板

1. 点击“选择电子邮件模板”
2. 从列表中选择模板
3. 验证主题和内容

### 第 2 步：选择组

1. 点击“选择组”
2. 选择您要通知的群组
3. 验证组成员（通常显示计数）

### 第 3 步：设置条件

1. 添加条件：“当\[条件]为真时”
2. 示例：“当发票金额大于 5000 欧元时”

### 第四步：测试

1. 使用示例文档进行测试
2. 验证电子邮件是否发送至群组
3. 检查模板渲染

***

## 电子邮件模板示例

### 模板 1：高额发票提醒

```
Subject: High-Value Invoice Alert - {document_number}

Body:
Team,

An invoice exceeding €10,000 has been received:

Document Number: {document_number}
Supplier: {supplier_name}
Amount: {amount} EUR
Received Date: {date}
Status: {status}

This requires immediate review and approval.

---
Sent automatically by DocBits
```

### 模板 2：供应商状态变更

```
Subject: Supplier Status Update - {supplier_name}

Body:
Procurement Team,

The following supplier's status has been updated:

Supplier: {supplier_name}
Supplier Code: {supplier_code}
New Status: {status}
Effective Date: {date}

Please update your systems accordingly.

---
Sent automatically by DocBits
```

### 模板 3：准备导出的文档

```
Subject: Document Approved for Export - {document_number}

Body:
Export Team,

The following document has been approved and is ready for export:

Document Number: {document_number}
Invoice Number: {invoice_number}
Supplier: {supplier_name}

Please proceed with export to {destination_system}.

---
Sent automatically by DocBits
```

***

## 常见用例

### 使用案例 1：质量控制警报

**触发：**当发现发票与采购订单不符时

**邮件组：**质量团队

**内容：**

```
Invoice {number} has quality issues:
- Unit Price variance: 12% (exceeds 5% tolerance)
- Please review and take action
```

### 用例 2：批准通知

**触发：**当文档达到某种状态时

**邮件群：**审批委员会

**内容：**

```
Document {number} is awaiting approval:
- Amount: {amount}
- Supplier: {supplier_name}
- Please login to approve/reject
```

### 用例 3：异常通知

**触发：**条件不满足时

**邮件组：**经理

**内容：**

```
Exception alert for document {number}:
- Supplier code missing
- Delivery date invalid
- Manual review required
```

### 用例 4：状态更新

**触发：**文档状态发生变化时

**邮件组：**下一步负责团队

**内容：**

```
Document {number} status changed to: {status}
Assigned to: {assigned_user}
Next steps: {next_steps}
```

***

## 故障排除

### “未收到电子邮件”

**可能原因：**

* [ ] 群组中的用户没有电子邮件地址
* [ ] 电子邮件被垃圾邮件过滤器阻止
* [ ] 群组中的电子邮件地址不正确
* [ ] 群组没有成员

**解决方案：**

1. 验证所有群组成员都有电子邮件地址
2. 检查垃圾邮件/垃圾文件夹
3. 验证组成员身份是否正确
4. 如果缺少用户，请将其添加到组中
5. 与 IT 部门核实电子邮件服务是否正常运行

### “模板未正确呈现”

**原因：**未找到占位符变量

**解：**

* [ ] 验证字段名称完全匹配
* [ ] 检查字段在文档中是否有值
* [ ] 使用正确的占位符格式：{field\_name}
* [ ] 使用包含所有字段的示例文档进行测试

### “有些人收到电子邮件，有些人则没有”

**原因：** 群组成员身份不完整或电子邮件无效

**解决方案：**

* [ ] 验证所有成员都有有效的电子邮件
* [ ] 检查是否有部分用户选择退出
* [ ] 验证组成员身份是否为最新
* [ ] 联系 IT 部门以验证电子邮件地址

### “想要在群组中添加/删除人员”

**解：**

* 联系您的管理员
* 群组在系统设置中管理
* 此卡无法更改
* 请求 IT 中的组成员变更

***

## 电子邮件模板定制

### 可用占位符

```
{document_number} - Document ID
{invoice_number} - Invoice ID
{supplier_name} - Supplier name
{supplier_code} - Supplier code
{amount} - Invoice amount
{currency} - Currency (EUR, USD, etc.)
{date} - Document date
{status} - Current status
{assigned_user} - Assigned person
{assigned_group} - Assigned group
{next_steps} - What needs to happen next
{reason} - Reason for exception/alert
{comment} - Comments or notes
```

### 创建自定义占位符

如果您需要电子邮件中的其他数据：

1. 联系您的管理员
2. 请求新的占位符
3. 向文档添加必要的字段
4. 更新电子邮件模板

***

## 最佳实践

✅ **做：**

* 保持电子邮件内容简洁明了
* 包括行动项目（收件人应该做什么？）
* 包含访问文档的链接或说明
* 使用示例数据测试模板
* 发送到正确的组（不要过度通知）
* 使用模板以保持一致性

❌**不要：**

* 发送太多电子邮件（通知疲劳）
* 在电子邮件中包含敏感数据
* 发送给不需要信息的群组
* 使用不明确的主题行
* 忘记包括如何采取行动
* 向个人发送电子邮件（改为使用群组）

***

## 性能说明

* 每封电子邮件发送需要约 1 秒
* 大型团体可能需要时间（100 人 = \~100 秒）
* 不要创建发送数千封电子邮件的循环
* 监控电子邮件服务容量
* 如果文档很多，请考虑批处理

***

## 相关卡牌

* **ACTION\_SEND\_EMAIL** - 发送给个人
* **ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP** - 分配任务而不仅仅是通知
* **ACTION\_CREATE\_TASK\_FOR\_GROUP\_SEQUENTIAL** - 创建任务并通知
* **STAUS\_CHANGE** - 更改状态并通知

***

## 典型工作流程示例

```
Document Arrives
    ↓
Check Condition: "Is amount > €10,000?"
    ↓
YES: Send Email to Finance Team
     "High value invoice alert"
    ↓
Send Email to Procurement Team
     "New invoice from supplier"
    ↓
Workflow Continues
```

***

## 常见问题解答

**Q: 我可以发送给多个群组吗？** A: 为每个群组创建单独的卡片

**Q：如果某人的电子邮件被退回怎么办？**A：电子邮件被记录为失败，IT 可以排除故障

**Q：我可以更改邮件模板吗？** A：联系管理员修改模板

**Q: 可以根据条件发送吗？** A: 可以！使用“Where”和“And”条件来控制电子邮件的发送时间

**Q：我如何知道是否收到电子邮件？** A：在 DocBits 中检查电子邮件日志以了解发送状态
