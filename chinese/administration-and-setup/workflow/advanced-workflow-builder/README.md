# 高级工作流

**高级工作流**构建器是一种节点图编辑器，适用于需要分支、并行路径和流程控制的工作流，可实现标准构建器中线性的 When/And/Then 流程无法满足的需求。你可以在画布上排列节点并将它们连接起来，以定义执行流程。

{% embed url="https://youtu.be/EeNFVR6z7G8" %}
高级工作流设计器
{% endembed %}

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
