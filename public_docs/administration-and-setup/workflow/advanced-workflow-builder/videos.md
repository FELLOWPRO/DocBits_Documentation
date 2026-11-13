---
description: "观看五个带解说的章节，内容涉及 Advanced Workflows 和 Workflow Logs，含字幕文件和转录文本。"
---

# 高级工作流视频教程

了解如何构建、测试和诊断一个 Advanced Workflow。每一章均为英语解说；时长列于下方。

第一章介绍 Mike，然后展示他在真实 DocBits 设计器中的操作。接下来的两章同样使用真实的 DocBits 演示草稿。执行记录搜索预览展示了真实的文档处理和日志控件，结果为空。诊断章节仍使用带标注的教学示意图。完整的控件说明请参阅 [Advanced Workflows 指南](README.md)、[工具栏与画布](toolbar-and-canvas.md)、[节点](nodes.md)、[变量](variables.md) 和 [验证与测试](validation-and-testing.md)。

每个视频下方均提供 WebVTT 格式的字幕文件。展开可折叠的转录文本，无需播放视频即可阅读讲解。

| 章节 | 时长 |
| --- | --- |
| [1. 构建器与画布](#builder-and-canvas) | 3:42 |
| [2. 节点与路由](#nodes-and-routes) | 1:42 |
| [3. 变量、测试与激活](#variables-tests-and-activation) | 1:53 |
| [4. 找到相关的执行记录](#find-the-relevant-execution) | 1:50 |
| [5. 追踪节点并诊断](#trace-nodes-and-diagnose) | 1:43 |

## 构建器与画布

认识 Mike，然后直接在真实的英文 DocBits 界面中跟随他的讲解。在他打开未保存的设计器预览之前，先跟随 Workflow Dashboard、Workflow List 和 License。观看他为草稿命名、配置发票金额检查与两个操作、排列卡片、连接两条路由，并查看文档和 Custom Data 测试选项。该演示账户因没有 Advanced Workflow 订阅而阻止验证；Workflow 保持未保存且未激活状态。

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/en.mp4" %}

[打开视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/en.mp4) · [字幕（WebVTT）](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/en.vtt) · [转录文本（text）](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/en.txt) · 3:42

| 本视频内容 | 开始 |
| --- | --- |
| 认识管理员 | [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/en.mp4#t=0) |
| 检查 Workflow 访问权限 | [0:09](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/en.mp4#t=9) |
| 为 Workflow 命名 | [0:37](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/en.mp4#t=37) |
| 配置金额检查 | [0:52](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/en.mp4#t=52) |
| 添加 Approval 操作 | [1:16](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/en.mp4#t=76) |
| 添加 Standard 操作 | [1:37](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/en.mp4#t=97) |
| 排列画布 | [2:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/en.mp4#t=120) |
| 连接路由 | [2:17](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/en.mp4#t=137) |
| 准备测试用例 | [2:44](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/en.mp4#t=164) |
| 验证、保存并激活 | [3:10](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/en.mp4#t=190) |

<details>
<summary>转录文本</summary>

**认识管理员**

我在这里负责 DocBits。让我演示我如何构建一个发票检查，并连接它的两条路由。

**检查 Workflow 访问权限**

我从 Workflow Dashboard 开始，打开 Workflow List。然后检查 License。Workflow 和 Advanced Workflow 都需要有效的访问权限。启用这些之后，New Workflow 会提供 Advanced Workflow。这个文档账户没有有效的 Workflow 订阅，因此本视频继续使用未保存的设计器预览。

**为 Workflow 命名**

我在真实的 DocBits 设计器中操作。首先，我为这个草稿取一个清晰的名称。我们要检查发票金额，然后用两个简单的操作来展示可能的路由。此演示保持未保存状态。

**配置金额检查**

我打开 Add 并选择 And。在 Document Field 下，我选择 Docfield 条件。我将该字段设置为 total amount。然后我选择 Greater Than。And 输入一千。请使用你自己的文档字段键。正好等于一千不会通过此比较。

**添加 Approval 操作**

现在我添加一个来自 Document Field 的 Then 卡片。该操作设置一个文档字段。我使用演示键 approval route，并输入 Approval。这样便为该路由加上了标签。真实的审批流程需要它自己的业务操作。

**添加 Standard 操作**

我使用同一个操作添加第二个 Then 卡片。该操作设置一个文档字段。我使用演示键 approval route，这一次，该演示字段获得值 Standard。两个卡片都已配置完成。它们仍然需要连接，以定义执行哪个操作。

**排列画布**

我将卡片拖动成易于阅读的布局。两个操作放在右侧。条件位于中间，Start 在左侧。移动卡片只会改变它们的位置。它不会创建连接。

**连接路由**

我从 Start 的输出拖到条件的输入。Success 路由通向 Approval，为蓝色连接。橙色的 Failed Condition 路由通向 Standard。Red Error 是用于评估失败的独立输出。在这里它保持未连接。在生产 Workflow 中，请决定你将如何处理这些失败。

**准备测试用例**

工具栏的 Test 按钮会打开 Select Test Document。我可以选择一个演示文档，或者准备完整的 Custom Data。测试高于、低于以及正好等于一千的金额。也要检查缺失的金额。这个账户没有 Advanced Workflow 订阅。我展示的是测试准备，而不是执行结果。

**验证、保存并激活**

我找到 Validate 来检查连接和卡片设置。此账户因订阅不可用而阻止验证。在已启用的账户中，我会显式保存到服务器。然后单独检查激活状态。该开关在首次保存之前处于禁用状态。自动草稿指示器指的是浏览器本地的副本。它并不意味着此 Workflow 已保存或已启用。

</details>

## 节点与路由

在真实的 DocBits 设计器中跟随一个已连接的演示草稿。查看成功、条件为假和错误路由，然后将两个源节点连接到 Wait ALL、Wait ANY 和 OR。示例操作会写入演示值，以便识别这些路由。

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/en.mp4" %}

[打开视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/en.mp4) · [字幕（WebVTT）](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/en.vtt) · 1:42

<details>
<summary>转录文本（英文）</summary>

Start 是手动入口。When 定义一个事件触发器。两者都不接受传入连接。And 检查一个条件。Then 执行一个操作。两个构建器共用同一个卡片目录。Notes 在不执行的情况下解释设计。

将一个输出拖到下一个输入。设计器中的蓝色表示成功，橙色表示条件为假，红色表示错误。And 有三个结果。Then 有成功和错误。执行视图以绿色显示成功。

检查一张发票是否超过某个阈值。将蓝色连接到审批，橙色连接到常规处理，红色连接到错误处理。条件为假时可以继续沿其已连接的路由执行。它并不会停止所有分支。

Wait ALL 汇合分支。每个源都必须经过一条连接到该网关的路由。连接两个必需的检查以及下一个操作。未被选中的路由无法提供必需的结果。

当至少一个源经过已连接的路由时，Wait ANY 和 OR 汇合分支。OR 需要两个不同的源节点。这些网关既不创建互斥选择，也不取消其他操作。请测试完整的图。

保持处理节点可从入口到达。避免循环以及指向入口节点的传入连接。包含一个 Then 操作。验证已更改的路由。导入的 Delay 节点需要正数时长。当前的 Add 菜单不提供 Delay。

</details>

## 变量、测试与激活

在真实的 DocBits 设计器中跟随已连接的发票 Workflow。打开 Variables，比较各类型与文档引用表单，找到 Validate，准备文档或 Custom Data 测试，并识别 Save 与激活。测试场景展示的是示例输入配置；它们不展示执行结果。

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/en.mp4" %}

[打开视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/en.mp4) · [字幕（WebVTT）](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/en.vtt) · 1:53

<details>
<summary>转录文本（英文）</summary>

使用大括号图标打开 Variables。选择 Text、Number、Yes or No 或 Document。Search 会查找变量名称。Document 变量存储由专用 Workflow 操作设置的引用。此表单不接受文档值。

选择一个唯一的名称、类型和初始值。创建、编辑和删除变量会立即对组织持久生效。其他 Workflow 可以共享这些值。保存或丢弃画布都无法撤销变量更改。

选择 Validate。在画布上方查看错误和警告。点击一条消息以聚焦其节点。检查操作、入口连接、句柄、循环和汇合。结构验证并不能证明运行时数据是正确的。

工具栏的播放按钮会打开 Select Test Document。选择一个文档、Custom Data，或对独立卡片使用 Test Without Document。Start 处的播放会直接运行。测试使用当前画布，包括未保存的编辑，并模拟破坏性操作。

准备高于、低于和正好等于一千的单独测试，以及缺失数据的情况。运行后，检查节点消息和时长：绿色为成功，橙色为假，红色为错误，灰色为跳过。修复后重新测试；对于可重复的场景，使用 Test Manager。

自动保存在更改后大约每三十秒保留一份浏览器本地草稿。请显式保存到服务器。首次保存之前，激活开关不可用。在期望自动执行之前，请在 Workflow List 中检查启用状态。

</details>

## 找到相关的执行记录

{% hint style="info" %}
测试预览：真实的 DocBits 文档操作、Document Flow、步骤计时、空的 Workflow Logs 以及状态/日期筛选。该演示文档没有已保存的 Advanced Workflow 执行记录。本预览不包含执行行、分页和节点诊断。
{% endhint %}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/en.mp4" %}

[打开视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/en.mp4) · [字幕（WebVTT）](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/en.vtt) · 1:50

<details>
<summary>转录文本（英文）</summary>

**从文档开始**

在文档 Dashboard 中，打开 Actions 菜单并选择 Document flow。真实的处理历史会显示导入和 OCR。打开一个步骤以查看等待时间和处理时间。这些处理步骤与 Advanced Workflow 节点是分开的。

**读取真实的日志计数器**

这里是同一文档的 Workflow Logs。蓝色为总数，红色为错误，黄色为失败的条件，绿色为成功。此演示文档没有记录任何 Workflow 执行。因此四个计数器都显示零。

**查看执行列**

该表格包含 workflow name、creation time、runtime 和 result 列。使用时间戳来区分重复的运行。本预览没有可打开的执行行。仅凭列表为空并不能证明存在执行错误。

**打开状态筛选**

调节图标会打开实际的筛选菜单。选择按 name 或 creation time 排序，并选择升序或降序。Status 提供 success、failed condition 和 error。此处展示的界面是真实的 DocBits 屏幕。

**选择日期并重置筛选**

使用开始和结束字段或日历来选择时间段。日期使用年、月和日。Apply 请求结果。Clear filters 重置所选项。搜索需单独清除。此版本中日历保留英文月份名称。

**预览：仍缺少已保存的执行记录**

本预览可让你检查文档导航、处理详情和日志控件。仍需一条已保存的 Advanced Workflow 执行记录，才能展示实际的行、分页、路由和节点消息。本视频未模拟这些结果。

</details>

## 追踪节点并诊断

展开一条高级执行记录，选择节点，区分条件为假、错误和被跳过的节点，查看汇合结果，然后修正、测试并验证该 Workflow。

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v1/en.mp4" %}

[打开视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v1/en.mp4) · [字幕（WebVTT）](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v1/en.vtt) · 1:43

<details>
<summary>转录文本（英文）</summary>

展开 Workflow 行。高级执行记录在左侧显示其图，在右侧显示消息。标准 Workflow 显示卡片序列。可用的执行数据描述的是该次运行，它可能与今天的设计器不同。

平移或缩放，然后点击一个节点。Card Logs 显示其消息。控制节点（包括 Wait ALL 和 Wait ANY）可以显示节点级消息。结合所选节点和执行时间戳来阅读该消息。

绿色表示成功，橙色表示条件为假，红色表示错误，灰色表示跳过。被跳过的节点未被执行。在更改该节点之前，请检查是否选择了其他分支，或者是否缺少必需的汇合输入。

从入口开始沿实际路由查看。对于金额检查为假的情况，查看橙色。对于错误，阅读消息并查看红色。错误处理器可能成功执行，而整体执行仍报告原始错误。

对于 Wait ALL，检查每个源以及已连接的结果。对于 ANY 或 OR，找到匹配的源。来自同一个源的两个句柄并不是独立的审批。橙色的条件结果可能是有意为之。

记录 Workflow 名称、文档引用、时间戳、节点和确切消息。修正配置或数据，然后测试一个可重复的场景。保存并检查激活状态。将新的执行与旧的运行进行比较。较早的日志仍然描述较早的行为。

</details>

继续阅读 [Advanced Workflows 指南](README.md) 或 [Workflow Logs](../workflow-logs.md)。
