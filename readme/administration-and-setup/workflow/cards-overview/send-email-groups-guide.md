# 向群组发送电子邮件

***

将此卡片添加到 Workflow Builder 的 **Then** 组中——当 When/And 条件匹配后执行的操作：

<figure><img src="../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder 画布，包含 When、And 和 Then 卡片组"><figcaption><p>通过 <strong>Add Card</strong>，将 <strong>Send Email to Groups</strong> 卡片添加到 <strong>Then</strong> 组。</p></figcaption></figure>

***

## 📌 版本信息

**状态：** ✅ 单一版本（无重大变更） **最新版本：** v1（有效） **说明：** 此卡片采用单一版本模式，并通过翻译键支持多语言。

📖 [完整卡片数据库](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/DocFlow/docs/card_version.md)

***

## 用途

此卡片会自动向用户群组发送电子邮件通知。您无需将工作分配给个人，而是将消息发送给一个群组，由该群组的所有成员接收。

**实际示例：** 收到一张高金额发票时，自动向“Finance Team”群组中的所有人发送电子邮件通知，让他们知晓该发票需要审核。

***

## 何时使用此卡片

在需要以下操作时使用此卡片：

* 同时通知多位人员
* 向团队群组发送提醒
* 向部门广播更新
* 通知群组文档状态变更
* 向群组成员发送提醒

**常见场景：**

* 通知采购团队有新供应商
* 提醒财务团队有高金额发票
* 通知仓库团队有货运到达
* 广播文档状态变更

***

## 工作原理

1. **检查条件：** 工作流检查“Where”和“And”条件
2. **准备电子邮件：** 系统使用模板准备电子邮件
3. **获取群组成员：** 系统查找指定群组的所有成员
4. **发送：** 电子邮件发送给每位群组成员
5. **记录：** 记录电子邮件发送情况

***

## 参数说明

### 电子邮件模板

要发送的电子邮件内容

**选项：**

* 从现有模板中选择
* 每个模板都预先定义了主题、正文和格式
* 模板可以包含占位符，例如 {document\_number}、{supplier\_name}

**模板示例：**

```
主题：文档 {document_number} 需要审核

正文：
团队您好：

收到一张新发票，需要审核：
- 文档：{document_number}
- 供应商：{supplier_name}
- 金额：{amount} {currency}
- 日期：{date}

请登录 DocBits 进行审核。

此致，
DocBits 自动化
```

### 群组

要向其发送电子邮件的用户群组

**群组示例：**

* Finance Team
* Procurement Team
* Warehouse Team
* Approval Committee
* Management Group

***

## 配置步骤

### 第 1 步：选择电子邮件模板

1. 点击“Select Email Template”
2. 从列表中选择模板
3. 检查主题和内容

### 第 2 步：选择群组

1. 点击“Select Group”
2. 选择要通知的群组
3. 确认群组成员（通常会显示成员数量）

### 第 3 步：设置条件

1. 添加条件：“When \[condition] is true”
2. 示例：“When invoice amount is greater than €5000”

### 第 4 步：测试

1. 使用示例文档进行测试
2. 确认电子邮件已发送给群组
3. 检查模板的呈现效果

***

## 电子邮件模板示例

### 模板 1：高金额发票提醒

```
主题：高金额发票提醒 - {document_number}

正文：
团队您好：

收到一张金额超过 €10,000 的发票：

文档编号：{document_number}
供应商：{supplier_name}
金额：{amount} EUR
接收日期：{date}
状态：{status}

此事项需要立即审核并批准。

---
由 DocBits 自动发送
```

### 模板 2：供应商状态变更

```
主题：供应商状态更新 - {supplier_name}

正文：
采购团队您好：

以下供应商的状态已更新：

供应商：{supplier_name}
供应商代码：{supplier_code}
新状态：{status}
生效日期：{date}

请相应地更新您的系统。

---
由 DocBits 自动发送
```

### 模板 3：文档已准备好导出

```
主题：文档已批准，可供导出 - {document_number}

正文：
导出团队您好：

以下文档已获批准，可以导出：

文档编号：{document_number}
发票编号：{invoice_number}
供应商：{supplier_name}

请继续将其导出到 {destination_system}。

---
由 DocBits 自动发送
```

***

## 常见用例

### 用例 1：质量控制提醒

**触发条件：** 发票与 PO 之间发现差异时

**电子邮件群组：** Quality Team

**内容：**

```
Invoice {number} has quality issues:
- Unit Price variance: 12% (exceeds 5% tolerance)
- Please review and take action
```

### 用例 2：审批通知

**触发条件：** 文档达到特定状态时

**电子邮件群组：** Approval Committee

**内容：**

```
Document {number} is awaiting approval:
- Amount: {amount}
- Supplier: {supplier_name}
- Please login to approve/reject
```

### 用例 3：异常通知

**触发条件：** 条件未满足时

**电子邮件群组：** Managers

**内容：**

```
Exception alert for document {number}:
- Supplier code missing
- Delivery date invalid
- Manual review required
```

### 用例 4：状态更新

**触发条件：** 文档状态变更时

**电子邮件群组：** 负责下一步的团队

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
* [ ] 电子邮件被垃圾邮件过滤器拦截
* [ ] 群组中的电子邮件地址不正确
* [ ] 群组没有成员

**解决方案：**

1. 确认所有群组成员都有电子邮件地址
2. 检查垃圾邮件文件夹
3. 确认群组成员设置正确
4. 如果缺少用户，将其添加到群组
5. 联系 IT，确认电子邮件服务正常运行

### “模板呈现不正确”

**原因：** 未找到占位符变量

**解决方案：**

* [ ] 确认字段名称完全匹配
* [ ] 检查文档中的字段是否有值
* [ ] 使用正确的占位符格式：{field\_name}
* [ ] 使用包含所有字段的示例文档进行测试

### “有些人收到了电子邮件，其他人没有”

**原因：** 群组成员不完整或电子邮件地址无效

**解决方案：**

* [ ] 确认所有成员都有有效的电子邮件地址
* [ ] 检查是否有用户选择了退订
* [ ] 确认群组成员名单是最新的
* [ ] 联系 IT 验证电子邮件地址

### “想要在群组中添加或移除人员”

**解决方案：**

* 联系您的管理员
* 群组在系统设置中管理
* 无法通过此卡片进行更改
* 通过 IT 申请变更群组成员

***

## 自定义电子邮件模板

### 可用占位符

```
{document_number} - 文档 ID
{invoice_number} - 发票 ID
{supplier_name} - 供应商名称
{supplier_code} - 供应商代码
{amount} - 发票金额
{currency} - 货币（EUR、USD 等）
{date} - 文档日期
{status} - 当前状态
{assigned_user} - 指派人员
{assigned_group} - 指派组
{next_steps} - 接下来需要执行的操作
{reason} - 异常/提醒原因
{comment} - 评论或备注
```

### 创建自定义占位符

如果您需要在电子邮件中加入其他数据：

1. 联系您的管理员
2. 申请新的占位符
3. 在文档中添加所需字段
4. 更新电子邮件模板

***

## 最佳实践

✅ **建议：**

* 电子邮件内容应简短清晰
* 包含待办事项（收件人应采取什么行动？）
* 包含访问文档的链接或说明
* 使用示例数据测试模板
* 发送给合适的群组（避免过度通知）
* 使用模板以保持一致性

❌ **避免：**

* 发送过多电子邮件（造成通知疲劳）
* 在电子邮件中包含敏感数据
* 发送给不需要这些信息的群组
* 使用含义不清的主题行
* 忘记说明如何采取行动
* 向个人发送电子邮件（改为发送给群组）

***

## 性能说明

* 每封电子邮件大约需要 \~1 秒发送
* 大型群组可能需要较长时间（100 人 = \~100 秒）
* 不要创建会发送数千封电子邮件的循环
* 监控电子邮件服务容量
* 如果涉及许多文档，请考虑分批处理

***

## 相关卡片

* **ACTION\_SEND\_EMAIL** - 发送给个人
* **ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP** - 分配任务，而不只是发送通知
* **ACTION\_CREATE\_TASK\_FOR\_GROUP\_SEQUENTIAL** - 创建任务并发送通知
* **STAUS\_CHANGE** - 更改状态并发送通知

***

## 典型工作流示例

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

## 常见问题

**问：可以发送给多个群组吗？** 答：为每个群组创建单独的卡片

**问：如果某人的电子邮件被退回怎么办？** 答：电子邮件会被记录为发送失败，IT 可以进行故障排查

**问：可以更改电子邮件模板吗？** 答：联系您的管理员修改模板

**问：可以根据条件发送吗？** 答：可以！使用“Where”和“And”条件控制电子邮件的发送时机

**问：如何知道电子邮件是否已收到？** 答：在 DocBits 中查看电子邮件日志，确认发送状态
