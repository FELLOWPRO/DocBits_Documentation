---
description: "从入门到专家的学习路径"
---

# 从入门到专家的学习路径

七个层级带您从第一次查看工作流设计器，走到能对一个正在运行的工作流负责地做出变更。每个层级都给出目标、在您自己的测试组织中要执行的步骤，以及可以核对的结果。请按顺序完成，并亲手搭建每一个练习：每个层级都建立在前一层级的配置之上。

1. [认识产品与执行模型](#level-1)
2. [构建第一条规则](#level-2)
3. [字段、类型与边界](#level-3)
4. [业务规则与审批](#level-4)
5. [Advanced 控制流与子工作流](#level-5)
6. [计算、接口与导出](#level-6)
7. [变更与专家运维](#level-7)

## 开始之前

* 一个您自己的测试组织，里面有一张合成单据。绝不用客户单据练习。
* 执行第 1 层之前，先确认您的角色、工作流许可和 Advanced 权限。
* 导入的练习在您测试完成之前保持未启用状态。
* 完整的 JSON 数据放在 **Advanced Test → Custom Data** 中。
* 真实审批和集成需要各自的测试用户和测试目标；设计器里的测试不能替代它们。

## 1. 认识产品与执行模型 <a href="#level-1" id="level-1"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/zh.mp4" %}

[打开带中文字幕和文字稿的视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/zh.html)。

**目标:** 说清是什么启动工作流，以及测试结果对真实运行能说明什么、不能说明什么。

1. 检查组织、您的访问权限、工作流模块和 Advanced 权限。
2. 用自己的话说清 When–And–Then，然后说明线性规则到哪里为止，而 Advanced 图如何改为沿着已连接的出口推进。
3. 分清设计器里看起来相似的四个方面：单据类型过滤、执行事件、保存和启用。

**完成标准:** 您能说出规则何时才会被考虑，以及哪类依据能把模拟与真实单据运行区分开。

**延伸阅读:** [我的工作流什么时候运行？](workflow-execution-model.md) · [不重启工作流就改变状态](masterclass/status-and-reentry.md)

## 2. 构建第一条规则 <a href="#level-2" id="level-2"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/zh.mp4" %}

[打开带中文字幕和文字稿的视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/zh.html)。

**目标:** 把一条规则从设计器带到经过核对的结果，全程不碰真实单据。

1. 在 Advanced Builder 中搭建：When Invoice → And invoice\_id = WF-TRAINING-001 → And total\_amount > 1000 → Then wf\_training\_route = REVIEW。这种规模的线性规则不需要控制节点。
2. 保存后到规则列表里确认它仍处于未启用状态，因为保存一条新规则可能已经把它启用了。Advanced Test 是独立的执行层面：它评估构建器里的图，而不是已启用的规则。
3. 用 999、1000 和 1000.01 的完整数据运行 Advanced Test。逐个记录字段类型、运算符和选中的出口，再补一个金额完全缺失的用例。

**完成标准:** 只有 1000.01 会到达 REVIEW，缺失金额显示为错误而不是低于阈值的普通结果，并且结束时规则重新处于关闭状态。

**延伸阅读:** [Advanced 业务案例：发票路由](advanced-workflow-case-study.md) · [工作流练习包](workflow-training-kit.md)

## 3. 字段、类型与边界 <a href="#level-3" id="level-3"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/zh.mp4" %}

[打开带中文字幕和文字稿的视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/zh.html)。

**目标:** 在相信条件的结果之前，先弄清它到底比较了什么。

1. 用缺失字段、`null`、空文本、空格、`false`、`0`、`"0"` 和 `"false"` 测试空值检查，并记录哪些被视为空。
2. 把同一个 2 个百分点的容差算两次：一次以采购订单为参考（订单 100、单据 102.02），一次以单据为参考。
3. 在订单卡片上切换 Any 和 All，数一数实际比较了多少行。

**完成标准:** 您能从值、类型、参考侧和现有数据解释真、假和错误。在订单卡片的版本 5 中，单没有可比行属于数据错误，不是成功审批。

**延伸阅读:** [Field is、Docfield is 与两个字段比较](masterclass/field-conditions.md) · [让容差和订单参考侧没有歧义](masterclass/tolerances-and-po.md)

## 4. 业务规则与审批 <a href="#level-4" id="level-4"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/zh.mp4" %}

[打开带中文字幕和文字稿的视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/zh.html)。

**目标:** 通过决策表把发票送到正确的人，然后跑一条会等待第一位审核人的审批链。

**练习 1：带直接分配的决策表**

1. 建一张决策表，两条规则不可能同时命中：审核人 A 到 1000，审核人 B 高于 1000，使用 `cost_center=4711` 和 `total_amount`。
2. 在 **Decision Table has Returns** 版本 3 中设置 `store_data=wf_store_data`。用 **Assign document based on decision table** 和 `assignee_type=user` 分配单据，并使用您测试组织中的真实用户。
3. 测试命中一条、没有命中、命中多条和用户 ID 无效四种情况，并把未命中和分配错误导向明确的兜底路径。在单据本身上接受这次分配。

**练习 2：不使用直接分配的连续审批**

1. 用连续卡片另建一条独立规则：连续分配卡放在位置 10 给审核人 A，然后连续任务卡放在位置 20 给审核人 B。这次运行中不要加入直接分配，因为已核对的收尾逻辑在同一运行中已经直接分配过单据时，可能会跳过第一位连续接收人。
2. 以 A 身份批准，确认 B 只有在 A 的决定被处理后才收到单据；再以 B 身份批准。
3. 在一次新的运行中以 A 身份拒绝，确认没有发生导出，然后测试无法确定任何接收人时会发生什么。

**完成标准:** 您能区分责任人、任务、通知和真实批准；A → 批准 → B → 批准按这个顺序发生；A 的拒绝阻止了导出；接收人缺失没有算作已完成批准。

**延伸阅读:** [把决策表追踪到分配](masterclass/decision-table-routing.md) · [区分分配、任务和连续审批](masterclass/assignment-task-sequential.md)

## 5. Advanced 控制流与子工作流 <a href="#level-5" id="level-5"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/zh.mp4" %}

[打开带中文字幕和文字稿的视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/zh.html)。

**目标:** 正确汇合并行路径，并把工作交给另一个工作流。

1. 用两个真正会被执行到的检查比较 ALL、ANY 和 OR：ALL 需要每个来源都有匹配出口，ANY 和 OR 只需要一个，而同一来源的绿色加橙色仍然只算一个来源。
2. 看一个运行时没有走的分支，如 MERGE-04 案例：Advanced Test 仍会评估等待中的汇合，而正常运行一旦有前置永远不到达就跳过它。
3. 跑完 v2 案例的七个用例（高于、低于、边界、刚好高于、缺失、无效数字、另一张发票）。然后用 Run Workflow 调用您自己的一个未启用工作流，并打开目标中的路径本身。

**完成标准:** 您能解释 MERGE-04 案例中第 2 步的测试与运行差异、来源如何计数以及错误会往哪里走。Run Workflow 调用显示绿色仍需在目标侧核对。这里的 v2 指案例图的第二个版本：每条路径的状态卡直接进入共同的收尾卡，没有等待中的 OR 节点。

**延伸阅读:** [正确连接 Wait ALL、Wait ANY 和 OR](masterclass/control-nodes.md) · [理解 Run Workflow、目标条件和错误](masterclass/run-workflow.md) · [Advanced 业务案例：发票路由](advanced-workflow-case-study.md)

## 6. 计算、接口与导出 <a href="#level-6" id="level-6"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/zh.mp4" %}

[打开带中文字幕和文字稿的视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/zh.html)。

**目标:** 计算数值、从外部系统取回结果，并且只在真实批准之后导出。

1. 计算一列，并比较计算前后的整张表，其中包含正则不匹配的一行和除以零的一行。
2. 写下与外部系统的回写契约：哪个单据字段接收结果、哪张卡片或扩展把它写进去，以及您之后如何核对保存的值。单有 HTTP 200 不算结果。
3. 用您自己的导出配置规划批准后的导出，并记下您要在接收方核对什么。

**完成标准:** 字段里的后续值、接收方收到以及 ERP 处理各自需要独立依据。模拟或排队的导出不算送达。

**延伸阅读:** [计算表格并检查正则依赖](masterclass/table-calculations.md) · [检查 API 调用与响应的后续使用](masterclass/api-response-contract.md) · [导出变体、未完成任务和收尾状态](masterclass/export-lifecycle.md)

## 7. 变更与专家运维 <a href="#level-7" id="level-7"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/zh.mp4" %}

[打开带中文字幕和文字稿的视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/zh.html)。

**目标:** 变更一个不是您搭建的工作流，并且能把这次变更撤回。

1. 导出工作流并记下卡片版本，然后再动手。
2. 变更后重跑正例、反例、错误和边界用例，并额外重跑同一用例的第二次。
3. 把第一个失败追溯到某一个输入和某一处配置，并把保存的导出留作回退路径。

**完成标准:** 您能验收变更、恢复已保存的配置，并用依据比较一次新的单据运行。记录原因、修正以及仍然存在的限制。

**延伸阅读:** [系统地诊断工作流错误](workflow-troubleshooting.md) · [理解卡片并可靠地配置](card-reference-standard.md)

## 自测理解程度

| 问题 | 答案 |
| --- | --- |
| Field is v2 中 `false` 算空吗？ | 算。数字 0 和文本 "false" 都不算空。 |
| 绿色 OR 测试能保证单据运行吗？ | 不能。在已核对的 MERGE-04 案例中，测试会评估一个前置永远不到达时单据运行会跳过的汇合。 |
| Run Workflow 能调用未启用的目标吗？ | 能在已核对的显式调用中。仍要核对目标条件和结果。 |
| HTTP 200 会自动提供 api.response.cost\_center 吗？ | 不会。已核对的动作不提供这种自动 JSON 输出契约。 |
| 绿色测试能证明导出被接收吗？ | 不能。单据运行、接收方收到和 ERP 处理需要分别提供依据。 |

## 记录您验收过的内容

从[工作流练习包](workflow-training-kit.md)下载 `workflow-training-kit-v2.zip`，解压并打开 `acceptance-record-template.json`。这是一份空白记录，不是要导入的东西；同一个 ZIP 里还有各层级引用的数据、期望结果和已保存的测试响应。

记录您测试了什么以及凭什么知道：场景、配置（工作流导出的哈希、卡片版本）、您的预期、您观察到的现象，以及您手上是哪一类依据。把 Advanced Test 中的测试、孤立的来源核对、真实单据运行、接收方收到和 ERP 处理分开，未测试的步骤保持为未完成。
