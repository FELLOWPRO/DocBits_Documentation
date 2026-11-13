# 节点

## 视频: 节点与路径

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

[查看全部五个章节](videos.md)

高级工作流是由边连接的**节点**构成的图。你可以从 **+ Add** 菜单中添加节点（也可以右键单击画布），并将它们连接起来以定义执行流程。

<figure><img src="../../../.gitbook/assets/workflow_advanced_add_menu.png" alt="显示可用节点类型的添加节点菜单"><figcaption><p><strong>+ Add</strong> 节点菜单 — 可用的节点类型。</p></figcaption></figure>

## 节点类型

* **Start** — 工作流的入口点。自动添加；每个流程都从这里开始。
* **When** — 触发器卡片，与标准构建器中的相同。
* **And** — 条件卡片。其结果为 true 或 false，并可据此分支流程。
* **Then** — 执行动作的卡片（设置字段、创建任务、调用 API，……）。
* **Wait ALL** — 等待所有传入分支完成后再继续。
* **Wait ANY** — 任意一个传入分支完成后立即继续。
* **OR** — 将流程分支到不同的替代路径。
* **Note** — 画布上的自由文本注释；不会影响执行。

**When / And / Then** 节点使用的卡片与 [卡片](../cards-overview/) 部分所述的完全相同。

## 连接节点

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/zh.mp4" %}

**视频:** Workflow 运行中的成功、条件失败和错误 · 1:14 · [字幕 (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/zh.vtt)

<details>

<summary>文字稿</summary>

**运行时的“当”、“和”、“然后”** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/zh.mp4#t=0.25)

Workflow 运行时，由“当”卡启动。和卡检查条件，然后卡执行操作。接下来发生什么取决于每张卡片的结果。

**成功、失败条件或错误** · [0:11](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/zh.mp4#t=11.016)

每张和卡以三种结果之一结束。成功走蓝色的成功路径，失败条件走橙色路径，错误走红色的错误路径。

**缺少数据是错误** · [0:21](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/zh.mp4#t=21.75)

缺少数据不是失败条件。如果卡片需要的字段不在文档中、缺少变量或没有文档，卡片会报告错误并走红色的错误路径。

**没有橙色路径：运行停止** · [0:33](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/zh.mp4#t=33.716)

如果条件不满足且其橙色路径没有连接，Workflow 会在这张卡片处停止。这次运行以失败条件结束。

**已连接：只是另一个分支** · [0:43](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/zh.mp4#t=43.35)

如果橙色路径已连接，失败条件只是另一个分支。Workflow 在那里继续，仍然可能以成功结束。

**红色错误路径：捕获错误** · [0:51](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/zh.mp4#t=51.65)

把红色错误路径连接到一个备用方案，例如给某人的任务，这样错误就不会被忽视。备用方案会运行，但这次运行仍标记为错误。

**运行如何结束** · [1:03](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/zh.mp4#t=63.45)

简而言之：任何错误都会使运行成为错误。没有连接橙色路径的失败条件会使其成为失败条件。其他情况都以成功结束。

</details>

节点通过**彩色边**连接。从节点**右侧**的连接手柄拖动到另一个节点**左侧**的输入手柄，即可创建连接。每种颜色表示不同的执行结果：

* **Success**（蓝色）— 节点成功完成时采用的默认路径。所有节点类型均可使用。
* **Failed Condition**（橙色）— 条件结果为 false 时采用的路径。**And**（条件）节点可使用。
* **Error**（红色）— 节点执行过程中发生错误时采用的路径。**And** 和 **Then**（动作）节点可使用。

## 执行路径高亮显示

单击任意节点即可查看其执行路径。所有通向该节点的节点以及从该节点继续延伸的节点都会高亮显示，其余内容则会变暗。对于 **Wait ALL** 节点，所有传入分支都会显示出来，让你准确查看该节点在继续之前会等待哪些分支。

## 后续步骤

* 使用 [变量](variables.md) 在节点之间传递数据。
* 使用 [验证与测试](validation-and-testing.md) 检查并运行工作流。
