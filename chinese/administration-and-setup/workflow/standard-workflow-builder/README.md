# 标准工作流

**标准工作流**构建器是一个基于卡片的线性编辑器，用于自动处理文档。一个工作流由三组卡片组成：**When**（触发条件）、**And**（附加条件）和 **Then**（要执行的操作）。当文档符合 When/And 条件时，Then 操作会自动运行。

## 如何访问

打开 **Workflow Dashboard → Workflow List**，然后点击 **New Workflow** 创建新的标准工作流，或点击现有工作流进行编辑。

<figure><img src="../../../.gitbook/assets/workflow_list.png" alt="Workflow List，显示类型、执行顺序和触发条件"><figcaption><p>Workflow List — 每一行都是一个工作流，你可以打开、启用或停用，也可以进行编辑。</p></figcaption></figure>

## When / And / Then 模型

<figure><img src="../../../.gitbook/assets/workflow_designer_cards.png" alt="包含 When、And 和 Then 卡片的标准工作流画布"><figcaption><p>标准工作流画布。此示例会在子组织中的发票触发，并将其分配给一位用户。</p></figcaption></figure>

* **When** — 启动工作流的触发条件（例如，_Document type is Invoice_）。
* **And** — 还必须满足的其他条件（例如，_Document is part of sub-organization_）。留空时，只要符合 When 卡片的条件就会运行。
* **Then** — 要执行的操作（例如，将文档分配给用户、创建任务、调用 API 或发送电子邮件）。

## 添加卡片

在任意分组中点击 **Add Card**，打开卡片库。卡片按类别整理，方便你找到所需的构建模块：

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="按类别分组的 Add Card 卡片库"><figcaption><p><strong>Add Card</strong> 卡片库 — 按类别分组的条件卡片、比较卡片、操作卡片等。</p></figcaption></figure>

点击 **Save Workflow** 保存，或点击 **Save Template** 将布局保存为可重复使用的模板。

## 工作流模板 <a id="workflow-templates"></a>

工作流工具栏中的 **Templates** 按钮会打开 **Workflow Templates** 库，你可以在其中管理组织中保存的模板：

<figure><img src="../../../.gitbook/assets/workflow_templates_dialog.png" alt="Workflow Templates 对话框，列出模板及 Name、Updated By、Last Modified On 和 Actions 列，并启用了 Show default Templates 选项"><figcaption><p><strong>Workflow Templates</strong> 对话框 — 显示已保存的模板；启用 <strong>Show default Templates</strong> 后，还会显示内置默认模板。</p></figcaption></figure>

* 列表会显示每个模板的 **Name**、**Updated By** 和 **Last Modified On**。
* 启用 **Show default Templates**，即可在列表中显示内置默认模板。
* 使用所在行的 **Actions** 菜单 **Duplicate** 模板，或 **Delete** 已保存的模板 — 内置默认模板无法删除。
* 点击模板所在行，可在 **Template Designer** 中打开该模板。该设计器使用与标准工作流设计器相同的 When/And/Then 画布。点击 **Save Template** 保存更改。
* 要从模板新建工作流，请在设计器中打开模板，调整卡片，然后点击 **Save Workflow** 将其保存为工作流。

## 后续步骤

* 在 **Cards** 部分了解各卡片的功能。
* 通过 **Workflow Pattern Guides** 将卡片组合为经过验证的解决方案。
* 如需包含并行路径（Wait ALL / Wait ANY / OR）的分支流程，请使用 **Advanced Workflow** 构建器。
