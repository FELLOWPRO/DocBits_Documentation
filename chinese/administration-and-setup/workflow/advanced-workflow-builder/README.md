# 高级工作流

**高级工作流**构建器是一种节点图编辑器，适用于需要分支、并行路径和流程控制的工作流，可实现标准构建器中线性的 When/And/Then 流程无法满足的需求。你可以在画布上排列节点并将它们连接起来，以定义执行流程。

## 视频：在 DocBits 中配置发票处理路径

认识陈伟，并在真实的中文 DocBits 界面中跟随他的讲解。他先检查工作流仪表板、工作流列表和许可证，然后打开未保存的设计器草稿。接下来，他逐步命名工作流、配置发票金额条件和两个操作、排列卡片，并连接两条处理路径，最后演示如何使用文档或自定义数据准备测试。演示账号没有 Advanced Workflow 订阅，因此验证被阻止；草稿保持未保存、未激活状态。

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/zh.mp4" %}

[打开视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/zh.mp4) · [字幕（WebVTT）](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/zh.vtt) · [文字稿（文本）](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/zh.txt) · 3:15

| 本视频内容 | 开始时间 |
| --- | --- |
| 认识管理员 | [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/zh.mp4#t=0) |
| 检查工作流权限 | [0:04](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/zh.mp4#t=4) |
| 命名工作流 | [0:29](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/zh.mp4#t=29) |
| 配置金额条件 | [0:42](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/zh.mp4#t=42) |
| 添加 Approval 操作 | [1:04](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/zh.mp4#t=64) |
| 添加 Standard 操作 | [1:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/zh.mp4#t=85) |
| 排列卡片 | [1:45](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/zh.mp4#t=105) |
| 连接处理路径 | [1:57](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/zh.mp4#t=117) |
| 准备测试用例 | [2:24](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/zh.mp4#t=144) |
| 验证、保存与启用 | [2:48](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/zh.mp4#t=168) |

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

我再添加一张卡片，使用同样的操作。 这个操作会设置文档字段的值。 这里使用演示字段 approval_route。 这一次，演示字段的值设为 Standard。 两张卡片都已配置，但还需要连接，才能确定执行哪个操作。

**排列卡片**

我拖动卡片，让布局更加清楚。 把两个操作放在右侧。 条件放在中间，Start 放在左侧。 移动卡片只会改变位置，不会创建连接。

**连接处理路径**

我从 Start 的输出端拖动到条件的输入端。 成功路径通过蓝色连接，通向 Approval。 条件不满足的橙色路径通向 Standard。 红色错误输出是独立的，用于处理条件计算出错的情况。 这里暂时没有连接这个输出。正式使用工作流时，需要明确这类错误的处理方式。

**准备测试用例**

点击工具栏中的测试按钮，打开测试文档选择窗口。 可以选择演示文档，也可以准备完整的自定义数据。 请测试大于、小于和正好等于一千的金额，也要测试金额缺失的情况。 这个账号没有 Advanced Workflow 许可证，所以这里展示的是测试准备，而不是已经执行的测试结果。

**验证、保存与启用**

验证功能用于检查连接和卡片设置。这个账号缺少许可证，因此验证被阻止。 在具备权限的账号中，我会明确地把工作流保存到服务器。 然后单独检查启用状态。第一次保存之前，启用开关不可用。 自动草稿提示指的是浏览器中的本地副本，并不表示工作流已经保存到服务器或已启用。

</details>

## 如何访问

从工作流区域（高级构建器画布）打开高级工作流设计器。你可以从 **Start** 节点开始，通过添加节点逐步构建流程。

<figure><img src="../../../.gitbook/assets/workflow_advanced_canvas.png" alt="包含工具栏的高级工作流节点图画布"><figcaption><p>高级工作流画布——包含缩放、运行、网格和保存控件的节点图。请在工具栏中为工作流命名。</p></figcaption></figure>

## 添加节点

点击 **+ Add** 打开节点菜单。除了熟悉的 **When**、**And** 和 **Then** 卡片，高级构建器还提供流程控制节点：

<figure><img src="../../../.gitbook/assets/workflow_advanced_add_menu.png" alt="包含节点类型的高级工作流 Add 菜单"><figcaption><p><strong>+ Add</strong> 节点菜单：When / And / Then，以及 Wait ALL、Wait ANY、OR 和 Note。</p></figcaption></figure>

* **When / And / Then** — 与标准构建器中的条件卡片和操作卡片相同。
* **Wait ALL** — 等待所有传入分支完成后再继续。
* **Wait ANY** — 任意一个传入分支完成后立即继续。
* **OR** — 将流程分支到不同的替代路径。
* **Note** — 在画布上添加自由文本注释（不影响执行）。

使用播放控件运行流程，验证流程，并点击工具栏中的保存按钮保存。

## 后续步骤

* 在 **Cards** 部分了解每种卡片的功能。
* 对于简单的线性自动化，使用 **Standard Workflow** 构建器可以更快完成设置。

[查看全部五个章节](videos.md)
