# 运行 DocOperator 提示（自动化脚本）

***

将此卡添加到工作流程生成器的 **则** 组 — 一旦“何时/与”条件匹配就会运行的操作：

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-zh.png" alt="包含“当”“且”和“则”卡片的未保存示例。执行前请配置所有占位字段。 此版本界面的部分标签尚未翻译或翻译不准确。本页说明使用正确术语；图片保留了实际界面。"><figcaption><p>包含“当”“且”和“则”卡片的未保存示例。执行前请配置所有占位字段。 此版本界面的部分标签尚未翻译或翻译不准确。本页说明使用正确术语；图片保留了实际界面。</p></figcaption></figure>

***

## 📌 版本信息

**当前版本：** v3（最新和推荐）**状态：** ✅ 活跃

**版本历史：**

* v2 → 原始 DocOperator 实现
* **v3 → CURRENT**（新增执行控制参数）
* v4 → 已弃用（功能已恢复）

**更改内容：** v3 添加了可选的“执行提示”参数以进行更多控制。 v4 试图恢复此功能，但已被弃用。

📖 【版本历史及变更](../release.md) | 【完整卡牌数据库](export-cards-guide.md)

***

## 目的

该卡使用 DocOperator 运行自动浏览器操作或脚本。将其视为一个机器人，可以像人类一样与网站或系统交互 - 单击按钮、填写表格、提取数据等。

**真实示例：** 您的公司使用基于网络的采购系统。该卡可以自动登录、搜索产品、检查可用性并获取当前价格 - 所有这些都无需任何人手动执行。

***

## 何时使用此卡

当您需要时使用此卡：

* 在没有 API 的网站上自动执行任务
* 从网页中提取数据
* 自动填写表格
* 登录系统并检索信息
* 自动执行重复的手动任务
* 与未集成的遗留系统交互

**常见场景：**

* 登录供应商网站并获取实时库存
* 自动填写外部系统上的表格
* 从不提供 API 的网页中提取数据
* 在快递网站上查看递送状态
* 从没有 API 访问权限的系统获取定价

***

## 它是如何运作的

1. **卡触发**：工作流程到达此卡且满足条件
2. **脚本启动**：DocOperator 机器人开始运行您的自动化脚本
3. **机器人操作**：机器人执行单击、键入、滚动、提取等操作
4. **数据提取**：Bot从网页收集信息
5. **返回数据**：数据返回DocFlow以供下一张卡片使用
6. **超时处理**：如果脚本花费太长时间，它会停止并返回它所拥有的内容

***

## 参数解释

### DocOperator 提示/脚本

自动化脚本告诉 DocOperator 到底要做什么

**示例（简单英语）：**

```
1. Go to https://supplier.com/login
2. Enter username: myuser
3. Enter password: mypass
4. Click Login button
5. Search for product "ABC123"
6. Extract the price
7. Return the price
```

### 变量

您想要传递到脚本中的数据

**示例：**

```
product_id: "ABC123"
supplier_code: "SUPP-001"
```

这些变量可以在脚本中使用，例如：

```
Search for product "{product_id}"
Find supplier "{supplier_code}"
```

### 最大步数

允许机器人执行多少操作

**典型值：**

* 简单任务（例如获取一个价格）：10-20 个步骤
* 中等复杂度（填写表格+提取）：20-50 个步骤
* 复杂的工作流程（登录 + 搜索 + 验证）：50-100 个步骤

**为什么重要：** 防止无限循环和长时间运行的脚本

### 最大重试次数

如果机器人执行操作失败，它应该重试多少次？

**示例：**

* 1：尝试一次，如果失败则继续
* 3：尝试3次才放弃
* 5：非常坚持——尝试5次

***

## 分步示例

### 场景：从网站获取供应商定价

**脚本定义：**

```
Step 1: Open website https://prices.supplier-xyz.com
Step 2: Click on "Product Lookup"
Step 3: Enter product code: ABC-123
Step 4: Click "Search"
Step 5: Wait for results to load (3 seconds)
Step 6: Extract price from the page
Step 7: Extract available quantity
Step 8: Return both values
```

**传入的变量：**

```
product_code = "ABC-123"
supplier_name = "Supplier XYZ"
```

**使用变量的脚本：**

```
Open website https://prices.{supplier_name}.com
Enter product code: {product_code}
Extract price and quantity
```

**预期结果：**

```
price: 45.50
quantity_available: 500
```

***

## DocOperator 可以执行的操作类型

### 导航

* 转到网址
* 点击链接
* 按下按钮
* 滚动页面

### 填写表格

* 在字段中输入文本
* 选择下拉选项
* 选中/取消选中复选框
* 单击按钮

### 数据提取

* 从页面读取文本
* 提取数字
* 获取表数据
* 复制信息

### 等待

* 等待页面加载
* 等待元素出现
* 等待动态内容

### 条件逻辑

* 如果存在某些东西，请执行此操作
* 如果文本匹配，则...
* 计算结果并采取相应行动

***

## 常见用例

### 1. 获取实时定价

**场景：** 供应商没有API，但网站显示价格

**脚本：**

```
1. Go to supplier website
2. Search for product
3. Extract price from results
4. Return price to DocFlow
5. Use price to validate invoice
```

### 2. 检查库存情况

**场景：** 需要了解供应商是否有库存

**脚本：**

```
1. Log into supplier portal
2. Search for product
3. Extract availability status
4. Extract delivery time
5. Return both to DocFlow
```

### 3. 自动提交表格

**场景：**需要在外部网站填写表格

**脚本：**

```
1. Navigate to form page
2. Fill Company Name field
3. Fill Contact Email field
4. Select Country from dropdown
5. Upload file attachment
6. Click Submit button
7. Capture confirmation message
```

### 4. 数据录入验证

**场景：**验证两个不同系统上的数据匹配

**脚本：**

```
1. Go to System A
2. Search for Order #123
3. Extract order amount
4. Go to System B
5. Search for Order #123
6. Extract order amount
7. Compare amounts
8. Return true/false if they match
```

***

## 配置步骤

### 第 1 步：创建脚本

1. 定义你想要实现的目标
2. 把它分成小步骤
3. 把每一步都写清楚
4. 先手动测试一下（打开网站，自己做）
5. 准确记录您点击的内容、输入的位置以及提取的内容

### 第 2 步：识别变量

1. 文档之间哪些数据会发生变化？
2. 应该将什么传递到脚本中？
3. 定义变量名
4. 指定脚本中使用变量的位置

### 第三步：设置参数

* **最大步数**：基于脚本复杂性
* **最大重试次数**：机器人应该有多持久？
* **超时**：页面应该等待多长时间？

### 第四步：测试

1. 使用样本数据进行测试
2. 验证机器人可以访问该网站
3. 验证提取是否正确
4. 检查变量是否正常工作

***

## 剧本写作技巧

### 清晰的语言

✅ **做：**

```
1. Click the "Login" button
2. Type the username in the login field
3. Wait 2 seconds for form to process
```

❌**不要：**

```
1. Do the login thing
2. Enter stuff
3. Wait for it
```

### 特定选择器

✅ **做：**

```
Click the button labeled "Submit Order"
Type in the field with placeholder "Enter Email"
```

❌**不要：**

```
Click somewhere
Type in a field
```

### 错误处理

✅ **做：**

```
1. Try to click "Next" button
2. If button not found, extract data from current page
3. Return what we have
```

❌**不要：**

```
Click "Next" (assumes it's always there)
```

***

## 故障排除

### “脚本超时”

**原因：**脚本完成时间过长

**解决方案：**

* [ ] 减少动作数量
* [ ] 增加“最大步数”值
* [ ] 优化脚本以加快执行速度
* [ ] 简化您要提取的内容

### “未找到元素”

**原因：** DocOperator 找不到您指定的按钮/字段

**解决方案：**

* [ ] 验证按钮/字段名称是否完全正确
* [ ] 检查网站布局是否改变
* [ ] 添加点击前的等待时间
* [ ] 检查按钮是否仅在特定条件下出现

### “登录失败”

**原因：**认证失败

**解决方案：**

* [ ] 验证用户名/密码是否正确
* [ ] 检查密码是否有特殊字符
* [ ] 验证帐户未被锁定
* [ ] 检查登录流程是否发生变化

### “数据未正确提取”

**原因：**脚本运行但提取了错误的信息

**解决方案：**

* [ ] 验证选择了正确的字段
* [ ] 检查数据是否在预期位置
* [ ] 手动测试提取逻辑
* [ ] 添加调试步骤以验证页面上的内容

### “脚本运行缓慢”

**原因：**步骤太多或网站速度慢

**解决方案：**

* [ ] 删除不必要的步骤
* [ ] 优化等待时间
* [ ] 检查互联网连接
* [ ] 考虑是否存在 API 替代方案

***

## 最佳实践

✅ **做：**

* 在部署之前彻底测试脚本
* 保持脚本简单且重点突出
* 添加解释每个步骤的注释
* 使用有意义的变量名
* 监控脚本性能
* 当脚本失败时有后备措施

❌**不要：**

* 创建极长的脚本（>100 个步骤）
* 将敏感密码放入日志中
* 依赖精确坐标（网站更改）
* 创建没有退出条件的循环
* 忽略错误消息

***

## 性能技巧

* **删除未使用的步骤** - 每一步都需要时间
* **组合相似的操作** - 对相关点击进行分组
* **优化等待** - 仅使用必要的延迟
* **缓存数据** - 不要提取相同的数据两次
* **并行处理** - 如果可能，运行多个脚本

***

## 安全考虑

⚠️**重要：**

* 不要在 DocFlow 中存储密码
* 使用安全方法传递凭据
* 不要记录敏感数据
* 监控正在提取的内容
* 确保机器人活动已记录且可审核

***

## 变量示例

### 您可以使用的可用变量：

```
{invoice_number} - From document field
{supplier_code} - From document field
{product_id} - From document field
{quantity} - From document field
{currency} - From document field
```

### 使用变量的脚本：

```
1. Go to https://supplier.com/api/lookup
2. Enter supplier code: {supplier_code}
3. Search for product: {product_id}
4. Enter quantity: {quantity}
5. Extract price in currency: {currency}
6. Return extracted price
```

***

## 比较：何时使用 DocOperator 与 API

| 情况              | 使用文档操作符 | 使用API     |
| ---------------------- | --------------- | ----------- |
| 网站有API        | ❌ 没有            | ✅ 是的       |
| 网站是互动的 | ✅ 是的           | ❌ 没有        |
| 需要登录         | ✅ 是的           | 视情况而定     |
| 需要非常快       | ❌ 没有            | ✅ 是的       |
| 复杂的工作流程       | ✅ 是的           | ❌也许不是 |
| 数据每日变化     | ✅ 是的           | ✅ 是的       |

***

## 相关卡牌

* **CALL\_API** - 当 API 可用时使用
* **ACTION\_HTTPS\_REQUEST** - 更简单的请求
* **ACTION\_SET\_FIELD\_TO\_TEXT** - 使用提取的数据
* **CONDITION\_HTTPS\_REQUEST\_STATUS** - 检查请求状态
