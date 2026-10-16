# 工作流模式指南

**版本：** 1.0 **上次更新：** 2025 年 10 月 23 日

***

## 概览

此目录包含全面的工作流模式指南，展示如何组合多个工作流卡片来解决常见业务场景。每种模式都提供分步实施说明、完整示例和最佳实践。

**什么是工作流模式？**

工作流模式是针对常见文档处理挑战、经过验证且可重复使用的解决方案。您无需从头开始，可以将这些模式用作模板，并根据具体需求进行调整。

***

## 工作流构建器一览

本页中的每种模式都在 **Workflow Builder** 中组装。您可以通过 **Workflow Dashboard → Workflow List → Add Workflow** 进入，也可以打开现有工作流。仪表板会显示所有工作流的运行历史记录以及成功率和失败率：

<figure><img src="../../../../.gitbook/assets/workflow_dashboard.png" alt="Workflow Dashboard，显示运行总数、成功率和失败率、工作流运行图表以及最近活动"><figcaption><p>Workflow Dashboard — 显示每个工作流的运行总数、成功率和失败率以及最近活动。</p></figcaption></figure>

**Workflow List** 选项卡会列出每个工作流及其类型、执行顺序和触发器。使用 **Add Workflow** 创建新工作流，或点击某个工作流，在构建器中打开它：

<figure><img src="../../../../.gitbook/assets/workflow_list.png" alt="Workflow List 选项卡，列出工作流及其类型、执行顺序和触发器"><figcaption><p>Workflow List — 每一行代表一个工作流，您可以打开它、切换启用或停用状态，也可以对其进行编辑。</p></figcaption></figure>

工作流由三组卡片构成：**When**（触发器）、**And**（附加条件）和 **Then**（要执行的操作）。下方示例会在发票属于某个子组织时触发，并将其分配给某位用户：

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder 画布，包含 When、And 和 Then 卡片"><figcaption><p>Workflow Builder 画布。下方每种模式都只是 When / And / Then 卡片的不同组合。</p></figcaption></figure>

点击任意分组中的 **Add Card**，即可打开卡片库。卡片按类别整理（Compare with Purchase Order、Partner Cards、Document Field、Date & Time、Document、Logic、Status、Table、Assignee 等），方便您找到每种模式所需的构建模块：

<figure><img src="../../../../.gitbook/assets/workflow_add_card_picker.png" alt="Add Card 对话框，显示卡片类别和可用卡片"><figcaption><p><strong>Add Card</strong> 卡片库 — 下方模式中引用的所有卡片都可以从这里选取。</p></figcaption></figure>

***

## 可用模式

### 1. [API 集成模式](api-integration-pattern.md)

**复杂度：** 中等 | **设置时间：** 45-60 分钟

了解如何将 DocBits 与外部 API 集成，以从外部系统获取、验证和存储数据。

**使用场景：**

* 从外部系统获取实时价格
* 根据主数据库验证供应商信息
* 从目录系统查询产品详情
* 从货币服务获取汇率
* 使用地理编码服务验证地址

**使用的卡片：** CALL\_API、CONDITION\_HTTPS\_REQUEST\_STATUS、ACTION\_SET\_FIELD\_TO\_TEXT、CONDITION\_COMPARE\_TWO\_DOCFIELD\_VALUES

[**查看完整模式 →**](api-integration-pattern.md)

***

### 2. [任务管理模式](task-management-pattern.md)

**复杂度：** 低至中等 | **设置时间：** 30-45 分钟

掌握如何在 DocBits 工作流中创建、分配、跟踪和管理任务，以支持审批和审核流程。

**使用场景：**

* 创建审批工作流
* 将审核任务分配给用户
* 处理需要人工干预的异常
* 将问题升级给经理
* 创建多级审批链
* 跟踪任务完成情况和截止日期

**使用的卡片：** tasks\_create、ACTION\_ASSIGN\_TO\_USER、ACTION\_SEND\_EMAIL\_TO\_GROUPS、CONDITION\_TASK\_STATUS

[**查看完整模式 →**](task-management-pattern.md)

***

### 3. [采购订单匹配模式](po-matching-pattern.md)

**复杂度：** 中等偏高 | **设置时间：** 60-90 分钟

实施全面的采购订单匹配工作流，根据容差将发票与采购订单进行验证并路由处理。

**使用场景：**

* 根据采购订单验证发票
* 在付款前检测价格错误
* 识别数量差异
* 执行采购控制
* 防止重复付款
* 自动执行三方匹配

**使用的卡片：** PURCHASE\_ORDER\_FULL\_MATCH、CONDITION\_DOC\_TO\_PO\_UNIT\_PRICE、CONDITION\_DOC\_TO\_PO\_QUANTITY、CONDITION\_DOC\_TO\_PO\_TAX\_LINES

[**查看完整模式 →**](po-matching-pattern.md)

***

### 4. [决策逻辑模式](decision-logic-pattern.md)

**复杂度：** 中等 | **设置时间：** 30-45 分钟

实施复杂的决策树和条件路由逻辑，根据业务规则沿不同路径处理文档。

**使用场景：**

* 按金额阈值路由文档
* 对不同类型的文档应用不同规则
* 实施多级审批逻辑
* 处理复杂业务策略
* 根据多个条件动态路由
* 实施审批矩阵

**使用的卡片：** CONDITION\_DOC\_FIELD\_AMOUNT、CONDITION\_DOC\_TYPE\_IS\_ISNOT、CONDITION\_SUPPLIER\_STATUS\_IS\_ISNOT、ACTION\_ASSIGN\_TO\_USER

[**查看完整模式 →**](decision-logic-pattern.md)

***

### 5. [数据转换模式](data-transformation-pattern.md)

**复杂度：** 中等 | **设置时间：** 30-45 分钟

转换、计算、格式化和丰富文档数据，为导出做准备、执行计算并统一格式。

**使用场景：**

* 计算总额、小计和税额
* 转换货币或计量单位
* 格式化日期、数字和文本
* 根据现有字段推导数值
* 从外部来源丰富数据
* 统一数据格式
* 验证计算结果

**使用的卡片：** ACTION\_CALCULATE\_FIELD、ACTION\_SET\_FIELD\_TO\_TEXT、ACTION\_COPY\_FIELD\_VALUE、CALL\_API、CONDITION\_COMPARE\_TWO\_DOCFIELD\_VALUES

[**查看完整模式 →**](data-transformation-pattern.md)

***

## 模式选择指南

### 按复杂度选择

| 复杂度          | 模式                                                                                                                                                                                      | 最适合                              |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **低至中等**    | [任务管理](task-management-pattern.md)                                                                                                                                                    | 初学者、简单工作流                  |
| **中等**        | <p><a href="api-integration-pattern.md">API 集成</a><br><a href="decision-logic-pattern.md">决策逻辑</a><br><a href="data-transformation-pattern.md">数据转换</a></p>                   | 中级用户、标准工作流                |
| **中等偏高**    | [采购订单匹配](po-matching-pattern.md)                                                                                                                                                    | 高级用户、复杂验证                  |

***

### 按使用场景选择

| 我需要……                  | 使用此模式                                                    |
| ------------------------- | ------------------------------------------------------------- |
| 与外部系统集成            | [API 集成模式](api-integration-pattern.md)                     |
| 创建审批工作流            | [任务管理模式](task-management-pattern.md)                     |
| 根据采购订单进行验证      | [采购订单匹配模式](po-matching-pattern.md)                     |
| 根据条件进行路由          | [决策逻辑模式](decision-logic-pattern.md)                       |
| 计算和转换数据            | [数据转换模式](data-transformation-pattern.md)                 |

***

### 按行业/部门选择

| 行业/部门           | 推荐模式                                                                                                                                    |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **财务/会计**       | [采购订单匹配](po-matching-pattern.md)、[任务管理](task-management-pattern.md)、[数据转换](data-transformation-pattern.md)                  |
| **采购**            | [采购订单匹配](po-matching-pattern.md)、[决策逻辑](decision-logic-pattern.md)、[API 集成](api-integration-pattern.md)                       |
| **运营**            | [任务管理](task-management-pattern.md)、[决策逻辑](decision-logic-pattern.md)                                                               |
| **IT/集成**         | [API 集成](api-integration-pattern.md)、[数据转换](data-transformation-pattern.md)                                                         |
| **所有部门**        | [决策逻辑](decision-logic-pattern.md)、[任务管理](task-management-pattern.md)                                                               |

***

## 如何使用这些模式

### 步骤 1：选择模式

1. 查看上方的模式说明
2. 找出与您的使用场景相符的模式
3. 查看复杂度和预计设置时间
4. 阅读模式指南中的“适用场景”部分

### 步骤 2：查看前提条件

每份模式指南都列出以下内容：

* 所需知识
* 建议先阅读的相关指南
* 将使用的卡片
* 配置要求

### 步骤 3：按照分步说明操作

每种模式都提供：

* 完整的工作流示例
* 分步实施指南
* 配置模板
* 实际案例
* 故障排查提示

### 步骤 4：根据需求进行自定义

* 根据您的业务规则调整示例
* 调整阈值和容差
* 修改路由逻辑
* 根据需要添加或删除步骤
* 在投入生产前进行全面测试

### 步骤 5：监控并优化

* 跟踪工作流性能
* 监控成功率
* 收集用户反馈
* 改进配置
* 记录自定义内容

***

## 组合模式

许多实际场景需要组合多种模式：

### 示例 1：完整发票处理

```
1. API 集成模式 → 获取当前定价
2. 数据转换模式 → 计算总额
3. 采购订单匹配模式 → 根据采购订单进行验证
4. 决策逻辑模式 → 根据差异进行路由
5. 任务管理模式 → 创建审批任务
```

### 示例 2：高金额发票审批

```
1. 数据转换模式 → 计算金额
2. 决策逻辑模式 → 检查阈值
3. 任务管理模式 → 多级审批
4. API 集成模式 → 通知外部系统
```

### 示例 3：异常处理

```
1. 采购订单匹配模式 → 检测差异
2. 决策逻辑模式 → 对异常严重程度进行分类
3. 任务管理模式 → 创建审核任务
4. 数据转换模式 → 计算影响
```

***

## 模式模板

每种模式都包含以下标准章节：

1. **概览** - 模式的功能
2. **适用场景** - 适用的使用场景
3. **完整示例** - 实际场景
4. **分步说明** - 实施说明
5. **配置** - 卡片设置模板
6. **工作流图** - 可视化表示
7. **高级变体** - 其他实施方式
8. **错误处理** - 常见问题及解决方案
9. **测试清单** - 验证步骤
10. **相关模式** - 可互补的模式
11. **相关指南** - 参考文档

***

## 获取帮助

### 模式支持资源

**文档：**

* [完整工作流指南索引](../../)
* [单张卡片指南](../then/action/)
* [条件卡片参考](../condition-cards-complete-guide.md)
* [工作流链接映射](https://github.com/Fellow-Consulting-AG/docbits/tree/main/WORKFLOW_LINKING_MAP.md)

**其他资源：**

* [快速参考指南](https://github.com/Fellow-Consulting-AG/docbits/tree/main/WORKFLOW_LINKING_QUICK_REFERENCE.md)
* [2025 年 10 月发行说明](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/administration-and-setup/workflow/changelog/2025-10-october.md)
* [卡片版本参考](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/docs/card_version.md)

**联系方式：**

* 模式反馈：docs@docbits.com
* 技术支持：support@docbits.com
* 实施帮助：consulting@docbits.com

***

## 模式统计

| 指标                    | 数值                |
| ----------------------- | ------------------- |
| **模式总数**            | 5                   |
| **涵盖的卡片总数**      | 30+                 |
| **合并文档篇幅**        | \~1,200 行          |
| **示例场景**            | 25+                 |
| **配置模板**            | 15+                 |
| **工作流图**            | 5 个完整图示        |
| **交叉引用**            | 87+ 个内部链接      |

***

## 参与贡献模式

您是否有能帮助其他人的工作流模式？

**模式贡献指南：**

1. **记录您的工作流**
   * 清晰的业务场景
   * 分步实施说明
   * 可用的配置示例
   * 实际测试结果
2. **遵循模式模板**
   * 使用标准章节结构
   * 包含所有必需内容
   * 提供图示/示例
   * 添加故障排查指南
3. **提交审核**
   * 发送邮件至：docs@docbits.com
   * 包含：模式说明、使用场景和实施指南
   * 我们会进行审核，并可能将其添加到官方文档中

**贡献收益：**

* 帮助其他 DocBits 用户
* 在文档中获得认可
* 改进整体产品知识库
* 获得关于您实施方案的反馈

***

## 更新日志

### 版本 1.0（2025 年 10 月 23 日）

* 首次发布 5 种全面的工作流模式
* 添加 API 集成模式
* 添加任务管理模式
* 添加采购订单匹配模式
* 添加决策逻辑模式
* 添加数据转换模式
* 实施交叉引用链接（87 个链接）
* 创建模式选择指南

***

## 后续步骤

**初次使用工作流模式？**

1. 从[任务管理模式](task-management-pattern.md)开始——最容易理解
2. 查看[决策逻辑模式](decision-logic-pattern.md)——适用于所有工作流的基础模式
3. 了解[API 集成模式](api-integration-pattern.md)——常见的集成需求

**准备好实施？**

1. 从上方列表中选择一种模式
2. 阅读完整的模式指南
3. 查看前提条件和相关指南
4. 按照分步说明操作
5. 使用示例文档进行测试
6. 部署到生产环境
7. 监控并优化

**需要更多帮助？**

* 查看[工作流文档概览](../../)
* 查看[快速参考指南](https://github.com/Fellow-Consulting-AG/docbits/tree/main/WORKFLOW_LINKING_QUICK_REFERENCE.md)
* 联系支持团队

***

**上次更新：** 2025 年 10 月 23 日 **维护方：** 文档团队 **版本：** 1.0
