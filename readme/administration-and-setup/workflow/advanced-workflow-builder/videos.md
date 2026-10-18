---
description: "五个中文配音章节，讲解高级工作流与执行日志，附字幕和文字稿。"
---

# 高级工作流视频教程

学习如何构建、测试和诊断高级工作流。全部五个章节均使用中文配音。

前三个章节展示真实 DocBits 界面。两个日志章节使用明确标注的教学示意图。界面截图来自尚未保存的演示草稿。

每个视频均附 WebVTT 字幕和可展开的文字稿。

1. [构建器与画布](#builder-and-canvas) · 1:35
2. [节点与路径](#nodes-and-routes) · 1:46
3. [变量、测试与激活](#variables-tests-and-activation) · 1:48
4. [查找相关执行](#find-the-relevant-execution) · 1:48
5. [跟踪节点并诊断](#trace-nodes-and-diagnose) · 1:47

## 构建器与画布 {#builder-and-canvas}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/zh.mp4" %}

[字幕文件（WebVTT）](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/zh.vtt) · 1:35

<details>
<summary>文字稿</summary>

**一张发票，两条路径**

这是 DocBits 中真实的高级工作流界面。发票金额检查连接到两个操作。连接关系决定执行哪一个操作。本示例使用尚未保存的草稿和演示字段。

**配置金额检查**

打开添加菜单，选择 And，再选择文档字段条件。设置金额字段，选择大于，并输入一千。请使用文档配置中准确的字段键名。

**配置操作卡片**

添加两张 Then 卡片。两张卡片都设置演示字段 approval route。一张写入 Approval，另一张写入 Standard。这些值用于标记路径。生产工作流需要配置实际的业务操作。

**连接不同结果的输出**

将 Start 连接到条件的输入端。将蓝色成功输出连接到 Approval，将橙色条件不满足输出连接到 Standard。红色错误输出用于单独处理求值错误。仅移动卡片的位置不会建立执行路径。

**准备测试用例**

在工具栏中打开测试。选择测试文档，或以 JSON 格式输入完整的文档数据。分别检查大于、小于和等于一千的金额，以及缺失值。执行后，请检查各个节点的结果。

**验证、保存并检查启用状态**

验证连接和卡片设置。明确保存到服务器，然后单独检查工作流是否已启用。浏览器自动草稿不能代替保存。执行工作流和访问日志需要相应的模块及订阅。

</details>

## 节点与路径 {#nodes-and-routes}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/zh.mp4" %}

[字幕文件（WebVTT）](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/zh.vtt) · 1:46

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

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v2/zh.mp4" %}

[字幕文件（WebVTT）](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v2/zh.vtt) · 1:48

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

**检查测试结果**

检查节点消息和耗时。绿色表示成功，橙色表示条件不成立，红色表示错误，灰色表示跳过。修正后重新测试。使用测试管理器建立可重复场景，覆盖成功、替代路径、缺失数据和错误。

**保存后再激活**

自动保存会在更改后约每三十秒保留本地浏览器草稿。请明确保存到服务器。首次保存前无法激活。在预期自动执行之前，检查工作流列表中的启用状态。

</details>

## 查找相关执行 {#find-the-relevant-execution}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v2/zh.mp4" %}

[字幕文件（WebVTT）](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v2/zh.vtt) · 1:48

<details>
<summary>文字稿</summary>

**打开文档日志**

在文档仪表板的操作菜单中选择工作流日志。必须启用工作流访问权限。这些日志属于选定文档。设计器测试和组织的事件或活动日志是独立的记录。

**理解计数器**

蓝色统计当前结果中的执行次数，红色统计错误，黄色统计条件不成立，绿色统计成功。计数器描述的是执行次数，不是工作流定义数或节点数。筛选条件会影响这些数字。

**选择准确的执行**

每行显示工作流名称、创建时间、运行秒数和结果。同一工作流可以针对同一文档执行多次。请比较时间戳。非常短的运行可能四舍五入显示为零点零零秒。

**缩小结果范围**

使用搜索查找工作流。调整图标打开排序方向、排序依据、状态、开始日期和结束日期。按名称或创建时间排序。日期按年、月、日输入，然后点击应用。

**检查空结果和分页**

使用分页查看更早的结果。清除筛选会重新加载未设置筛选项的列表。搜索内容需要单独清除。没有结果时，请检查文档、日期和状态。列表为空不能证明执行失败。

**识别特殊状态**

提示横幅和阻止图标表示文档已达到执行上限。更改上限前，先调查重复触发。只有存在录制内容时，才会显示 DocOperator 视频下载。它是该次执行的录制，与教程视频不同。

</details>

## 跟踪节点并诊断 {#trace-nodes-and-diagnose}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/zh.mp4" %}

[字幕文件（WebVTT）](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/zh.vtt) · 1:47

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
