---
description: "从入门到专家的学习路径"
---

# 从入门到专家的学习路径

请按顺序完成各阶段。仅阅读并不足够：每个阶段都要形成自己的配置、可核对的预期与验证依据。P0 用于避免根本性的执行误判；P1 深入讲解数据、业务决策和集成。

1. [认识产品与执行模型](#level-1)
2. [构建第一条规则](#level-2)
3. [字段、类型与边界](#level-3)
4. [业务规则与审批](#level-4)
5. [Advanced 控制流与子工作流](#level-5)
6. [计算、接口与导出](#level-6)
7. [变更与专家运维](#level-7)

## 前提条件

使用自有测试组织及合成文档。检查组织、角色、工作流许可和 Advanced 授权。导入练习后保持未启用。完整 JSON 数据用于 Advanced Test → Custom Data。真实审批和集成验收需要专门的测试用户与目标。

## 1. 认识产品与执行模型 <a id="level-1"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/zh.mp4" %}

[打开带中文字幕和文字稿的视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/zh.html)。

**练习:** 说明组织、权限、When–And–Then，以及线性规则与 Advanced 图的区别。区分文档类型过滤、执行事件、保存和启用。

**完成标准:** 能够在搭建前说明何时会处理规则，以及哪些依据能区分模拟与实际文档运行。

阅读并搭建: [我的工作流何时运行？](workflow-execution-model.md) · [P0：更改状态并限制重复执行](masterclass/status-and-reentry.md).

## 2. 构建第一条规则 <a id="level-2"></a>

**练习:** 创建 When Invoice → And invoice_id = WF-TRAINING-001 → And total_amount > 1000 → Then wf_training_route = REVIEW，保持未启用。使用 999、1000 和 1000.01 的完整数据测试。这条线性规则暂不需要控制节点。

**完成标准:** 只有大于 1000 时到达 REVIEW；记录类型、运算符和出口，并另外处理输入缺失。

阅读并搭建: [高级案例：发票路由](advanced-workflow-case-study.md) · [工作流练习包](workflow-training-kit.md).

## 3. 字段、类型与边界 <a id="level-3"></a>

**练习:** 检查缺失、null、空文本、空格、false、0 和文本数字。分别以订单及文档为参考计算容差，比较一个和全部实际匹配行。

**完成标准:** 根据值、类型、参考侧和现有数据解释真、假与错误；没有可比较行不能当作成功批准。

阅读并搭建: [P1：选择 Field is、Docfield is 或 Compare two Fields](masterclass/field-conditions.md) · [P1：明确容差参考侧与采购订单比较方向](masterclass/tolerances-and-po.md).

## 4. 业务规则与审批 <a id="level-4"></a>

**练习:** 配置两条不重叠的金额规则，追踪已保存的用户返回值直到分配。安排 A 的顺序值为 10、B 为 20，并设计拒绝与后备路径。

**完成标准:** 能区分责任人、任务、通知与真实批准。转交给 B 的验收必须依据已处理的 A 决定。

阅读并搭建: [P1：从决策表追踪到文档分配](masterclass/decision-table-routing.md) · [P1：区分文档分配、任务与顺序审批](masterclass/assignment-task-sequential.md).

## 5. Advanced 控制流与子工作流 <a id="level-5"></a>

**练习:** 用两项实际执行的检查比较 ALL、ANY 和 OR，并检查未选择的分支。运行全部七个 v2 用例，使用自有未启用目标测试 Run Workflow。

**完成标准:** 能解释测试与调度器差异、源节点计数和错误传递。v2 不依赖停滞的 OR 即可完成；绿色子调用仍要核对目标。

阅读并搭建: [P0：正确连接 Wait ALL、Wait ANY 和 OR](masterclass/control-nodes.md) · [P0：理解 Run Workflow、目标条件和错误](masterclass/run-workflow.md) · [高级案例：发票路由](advanced-workflow-case-study.md).

## 6. 计算、接口与导出 <a id="level-6"></a>

**练习:** 比较完整表格的计算前后结果，包含正则未命中和除零。明确接口真实回写契约，并使用自有测试配置设计审批后的导出。

**完成标准:** 分别证明后续字段值、接收方收到和 ERP 已处理；不把模拟或导出请求记录为送达。

阅读并搭建: [P1：计算表格列并检查正则依赖](masterclass/table-calculations.md) · [P1：验证 API 调用与后续响应使用](masterclass/api-response-contract.md) · [P1：选择导出方式、待办检查与最终状态](masterclass/export-lifecycle.md).

## 7. 变更与专家运维 <a id="level-7"></a>

**练习:** 修改前保存工作流导出并记录卡片版本。复测正例、反例、错误、边界和第二次运行，将第一个错误关联到具体输入与配置。

**完成标准:** 能验收变更、恢复配置，并比较新文档运行及其效果；记录原因、修正和剩余限制。

阅读并搭建: [系统诊断工作流问题](workflow-troubleshooting.md) · [理解并配置工作流卡片](card-reference-standard.md).

## 自测理解程度

| 问题 | 答案 |
| --- | --- |
| 在 Field is v2 中，false 为空吗？ | 是；数字 0 和字符串 "false" 不为空。 |
| 绿色 OR 测试能保证实际文档运行吗？ | 不能。测试与经检查的调度器对未到达前驱的处理不同。 |
| Run Workflow 能调用未启用目标吗？ | 能，经检查的显式调用可以；仍须核对目标条件和结果。 |
| HTTP 200 会自动提供 api.response.cost_center 吗？ | 不会。经检查的动作没有这种自动 JSON 输出契约。 |
| 绿色测试能证明导出已经收到吗？ | 不能。文档运行、接收方收到和 ERP 处理需要分别证明。 |

## 五篇配套指南

练习过程中依次使用：执行模型 → 可复现案例 → 练习包 → 诊断 → 卡片参考。这些是各阶段的工作材料，不是另外五项未经验证的任务。

1. [我的工作流何时运行？](workflow-execution-model.md)
2. [高级案例：发票路由](advanced-workflow-case-study.md)
3. [工作流练习包](workflow-training-kit.md)
4. [系统诊断工作流问题](workflow-troubleshooting.md)
5. [理解并配置工作流卡片](card-reference-standard.md)

## 完成记录

使用练习包中的 acceptance-record-template.json，记录场景、配置修订、预期、观察与依据类型。区分 Dev 测试、隔离源码检查、实际文档运行、接收和 ERP 处理。未验证步骤必须明确保留为待验收。
