---
description: "五个中文配音章节，讲解高级工作流与执行日志，附字幕和文字稿。"
---

# 高级工作流视频教程

五个章节均提供中文讲解、字幕文件和文字稿。第一章逐步演示如何创建示例工作流，其余章节进一步讲解各个主题。

前三个章节使用演示草稿展示真实的 DocBits 设计器。执行查找预览展示真实的文档处理和日志控件，示例结果为空。诊断章节仍使用明确标注的教学示意图。

每个视频均附 WebVTT 字幕和可展开的文字稿。

1. [构建器与画布](#builder-and-canvas) · 4:53
2. [节点与路径](#nodes-and-routes) · 1:46
3. [变量、测试与激活](#variables-tests-and-activation) · 1:48
4. [查找相关执行](#find-the-relevant-execution) · 1:48
5. [跟踪节点并诊断](#trace-nodes-and-diagnose) · 1:47

## 构建器与画布 {#builder-and-canvas}

认识陈伟，并在真实的中文 DocBits 界面中跟随他的讲解。他先检查工作流仪表板、工作流列表和许可证，然后打开未保存的设计器草稿。接下来，他逐步命名工作流、配置发票金额条件和两个操作、排列卡片，并连接两条处理路径，最后演示如何使用文档或自定义数据准备测试。演示账号没有 Advanced Workflow 订阅，因此验证被阻止；草稿保持未保存、未激活状态。

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/zh.mp4" %}

[打开视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/zh.mp4) · [字幕（WebVTT）](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/zh.vtt) · [文字稿（文本）](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/zh.txt) · 4:53

| 本视频内容 | 开始时间 |
| --- | --- |
| 认识管理员 | [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/zh.mp4#t=0) |
| 检查工作流权限 | [0:05](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/zh.mp4#t=5) |
| 命名工作流 | [0:37](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/zh.mp4#t=37) |
| 配置金额条件 | [0:53](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/zh.mp4#t=53) |
| 添加 Approval 操作 | [1:28](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/zh.mp4#t=88) |
| 添加 Standard 操作 | [1:56](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/zh.mp4#t=116) |
| 排列卡片 | [2:23](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/zh.mp4#t=143) |
| 连接处理路径 | [2:57](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/zh.mp4#t=177) |
| 准备测试用例 | [3:44](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/zh.mp4#t=224) |
| 验证、保存与启用 | [4:20](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/zh.mp4#t=260) |

<details>
<summary>文字稿</summary>

**认识管理员**

我来演示如何在 DocBits 中检查发票。

**检查工作流权限**

我先打开工作流仪表板，再进入工作流列表，然后检查许可证。 Workflow 和 Advanced Workflow 都需要有效的使用权限。 启用这两项权限后，新建工作流中才会提供 Advanced Workflow。 这个文档演示账号没有有效的工作流许可证，因此我会继续使用设计器中未保存的预览。

**命名工作流**

这里是真实的 DocBits 设计器。首先给草稿起一个清楚的名称。我们将检查发票金额，再用两个简单操作展示不同的处理路径。这个演示草稿不会保存。

**配置金额条件**

我打开添加菜单，选择条件卡片。 在文档字段类别中，选择 Docfield 条件。 字段名称填写 total_amount。 然后选择大于这个比较条件。 并输入一千。 请使用你自己的文档字段标识。金额正好等于一千时，不满足这个比较条件。

**添加 Approval 操作**

接下来，从文档字段类别中添加一张操作卡片。 这个操作会设置文档字段的值。 这里使用演示字段 approval_route。 并输入 Approval 作为字段值。 这个值只是用来标记路径。实际的审批流程需要配置相应的业务操作。

**添加 Standard 操作**

我再添加一张卡片，使用同样的操作。 这一次，演示字段的值设为 Standard。 两张卡片都已配置，但还需要连接，才能确定执行哪个操作。

**排列卡片**

我拖动卡片，让布局更加清楚。 把两个操作放在右侧。 条件放在中间，Start 放在左侧。 移动卡片只会改变位置，不会创建连接。

**连接处理路径**

我从 Start 的输出端拖动到条件的输入端。 成功路径通过蓝色连接，通向 Approval。 条件不满足的橙色路径通向 Standard。 红色错误输出是独立的，用于处理条件计算出错的情况。 这里暂时没有连接这个输出。正式使用工作流时，需要明确这类错误的处理方式。

**准备测试用例**

点击工具栏中的测试按钮，打开测试文档选择窗口。 可以选择演示文档，也可以准备完整的自定义数据。 请测试大于、小于和正好等于一千的金额，也要测试金额缺失的情况。 这个账号没有 Advanced Workflow 许可证，所以这里展示的是测试准备，而不是已经执行的测试结果。

**验证、保存与启用**

验证功能用于检查连接和卡片设置。这个账号缺少许可证，因此验证被阻止。 在具备权限的账号中，我会明确地把工作流保存到服务器。 然后单独检查启用状态。第一次保存之前，启用开关不可用。 自动草稿提示指的是浏览器中的本地副本，并不表示工作流已经保存到服务器或已启用。

</details>

## 节点与路径 {#nodes-and-routes}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/zh.mp4" %}

[打开视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/zh.mp4) · [字幕文件（WebVTT）](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/zh.vtt) · 1:46

<details>
<summary>文字稿</summary>

**明确每个节点的作用**

Start 用于手动启动，When 定义事件触发器。两者都不接受传入连接。And 检查条件，Then 执行动作。标准和高级构建器共用卡片目录。备注用于说明设计，不参与执行。

**区分三种结果**

将输出拖到下一个输入。在设计器中，蓝色表示成功，橙色表示条件不成立，红色表示错误。And 有三种结果，Then 有成功和错误两种结果。执行视图用绿色表示成功。

**建立替代路径**

检查发票金额是否超过阈值。蓝色连接审批，橙色连接常规处理，红色连接错误处理。条件不成立时，可以沿已连接的路径继续，并不会停止所有分支。示例值只用于标记路径。

**使用 Wait ALL 合并**

Wait ALL 合并分支。每个源节点都必须选中一条连接到合并节点的路径。连接两个必要的检查和下一项动作。未选中的路径无法提供所需结果。

**使用 ANY 和 OR 合并**

Wait ANY 和 OR 在至少一个源节点选中已连接路径时合并分支。OR 需要两个不同的源节点。这些节点不会创建互斥选择，也不会取消其他动作。请测试完整流程图。

**确保流程图可以执行**

处理节点必须能从入口到达。避免环路，不要向 Start 或 When 添加传入连接。至少包含一个 Then 动作，并验证修改后的路径。导入的 Delay 节点需要正数时长；当前添加菜单不提供 Delay。

</details>

## 变量、测试与激活 {#variables-tests-and-activation}

在真实的 DocBits 设计器中查看已连接的发票工作流。打开变量，比较变量类型和文档引用，找到验证按钮，准备用文档或自定义数据进行测试，并查看保存和激活控件。测试画面展示示例输入的配置，不展示已执行的测试结果。

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/zh.mp4" %}

[打开视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/zh.mp4) · [字幕文件（WebVTT）](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/zh.vtt) · 1:50

<details>
<summary>文字稿</summary>

**选择变量类型**

点击花括号图标打开变量。选择文本、数字、是或否，或者文档，并按名称搜索。Document 变量存储由专用工作流动作设置的文档引用。此表单不接受文档值。

**变量属于整个组织**

设置唯一名称、类型和初始值。创建、修改或删除变量会立即保存到组织。其他工作流可以共用这些值。保存或放弃画布都无法撤销变量更改。

**先验证结构**

点击验证，查看画布上方的错误和警告。点击消息可以定位节点。检查动作、入口连接、输出、环路和合并节点。结构验证通过，并不代表运行时数据正确。

**选择测试上下文**

工具栏播放按钮打开测试文档选择器。选择文档、自定义数据，或对独立卡片选择无文档测试。Start 的播放按钮直接运行。测试使用当前画布，包括未保存的修改，并模拟破坏性动作。

**准备和检查测试场景**

分别准备用于大于、小于、等于一千以及缺少数据的测试。运行后，检查节点消息和耗时：绿色表示成功，橙色表示条件不成立，红色表示错误，灰色表示跳过。修正后重新测试。使用测试管理器重复运行测试场景。

**保存后再激活**

自动保存会在更改后约每三十秒保留本地浏览器草稿。请明确保存到服务器。首次保存前无法激活。在预期自动执行之前，检查工作流列表中的启用状态。

</details>

## 查找相关执行 {#find-the-relevant-execution}

{% hint style="info" %}
测试预览：使用真实 DocBits 画面展示文档操作、文档流、步骤耗时、空工作流日志以及状态和日期筛选。演示文档没有已保存的高级工作流执行。本预览尚未包含执行记录行、分页或节点诊断。
{% endhint %}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/zh.mp4" %}

[打开视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/zh.mp4) · [字幕文件（WebVTT）](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/zh.vtt) · 1:51

<details>
<summary>文字稿</summary>

**从文档开始**

在文档仪表板中，打开操作菜单并选择文档流。真实的处理历史显示导入和文字识别步骤。打开一个步骤，查看等待时间和处理时间。这些文档处理步骤与高级工作流节点是不同的。

**查看真实日志计数器**

这里是同一文档的工作流日志。蓝色表示总数，红色表示错误，黄色表示条件不满足，绿色表示成功。这个演示文档没有已记录的工作流执行，因此四个计数器都显示零。

**检查执行记录列**

表格包含工作流名称、创建时间、运行时长和结果。请根据时间戳区分重复执行。本预览版没有可打开的执行记录行。仅有空列表并不能证明执行发生错误。

**打开状态筛选器**

筛选图标会打开真实的筛选菜单。可以按名称或创建时间排序，并选择升序或降序。状态选项包括成功、条件不满足和错误。画面展示的是真实的 DocBits 界面。

**选择日期并清除筛选**

通过开始日期、结束日期或日历选择时间范围。日期格式为年、月、日。应用按钮会请求结果，清除筛选会重置选择。搜索内容需要单独清空。此版本的日历月份仍显示为英文。

**预览版：仍缺少已保存的执行**

这个预览版用于检查文档入口、处理详情和日志控件。还需要一条已保存的高级工作流执行，才能演示真实记录、分页、执行路径和节点消息。视频没有模拟这些执行结果。

</details>

## 跟踪节点并诊断 {#trace-nodes-and-diagnose}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/zh.mp4" %}

[打开视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/zh.mp4) · [字幕文件（WebVTT）](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/zh.vtt) · 1:47

<details>
<summary>文字稿</summary>

**展开一次执行**

展开工作流行。高级执行在左侧显示流程图，右侧显示消息。标准工作流显示卡片序列。可用数据描述的是当时的执行，可能与当前设计器中的配置不同。

**选择节点查看证据**

平移或缩放流程图，然后点击节点。卡片日志显示节点消息。Wait ALL 和 Wait ANY 等控制节点也可能显示节点级消息。阅读时同时核对所选节点和执行时间戳。

**区分不同结果**

绿色表示成功，橙色表示条件不成立，红色表示错误，灰色表示跳过。被跳过的节点没有执行。修改之前，先检查是否选择了其他分支，或合并节点是否缺少必要输入。

**从首次偏差开始跟踪**

从入口沿实际路径追踪。金额条件不成立时查看橙色路径；发生错误时阅读消息并查看红色路径。错误处理动作可能成功，但整次执行仍会报告原始错误。

**检查合并依据**

对于 Wait ALL，检查每个源节点及其连接的结果。对于 ANY 或 OR，找到匹配的源节点。同一源节点的两个输出并不是两次独立审批。橙色条件结果也可能符合设计。

**修正、测试并验证**

记录工作流名称、文档引用、时间戳、节点和完整消息。修正配置或数据，再测试可重复的场景。保存并检查激活状态。比较新旧执行。旧日志仍然描述当时的行为。

</details>
