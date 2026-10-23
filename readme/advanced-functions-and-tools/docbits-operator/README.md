# DocBits Operator

## 概述

**DocBits Operator** 是一款由 AI 驱动的自动化助手，旨在简化工作流中的重复性任务。用户可以创建 _提示词_，即加入变量的分步说明，引导 AI 自动浏览界面、输入数据并点击操作，从而减少手动工作，加快日常操作。

## 启用 DocBits Operator

按照以下步骤启用 DocBits Operator：

1. **前往设置**：
   * 在仪表板中，前往 **Settings**。
   *   选择 **Document Processing**，然后选择 **Module**。

       <figure><img src="../../.gitbook/assets/docbits_operator_module_selection.png" alt="DocBits Operator 模块选择"><figcaption></figcaption></figure>
2. **启用此功能**：
   * 向下滚动，找到 **DocBits Operator** 选项。
   *   切换滑块以启用 **DocBits Operator**。

       <div align="left"><figure><img src="../../.gitbook/assets/docbits_operator_enable_toggle.png" alt="启用 DocBits Operator 的开关" width="563"><figcaption></figcaption></figure></div>

## 访问界面

* 启用此功能后，从主导航菜单打开 **DocBits Operator**。

### **1. 提示词输入**

屏幕底部有一个标记为 _“Enter your prompt here…”_ 的输入框，用户可以在此编写要让 Operator 执行的说明。

输入框旁有几个控制按钮：

* **提示词变量** – 打开一个弹出窗口，可在其中输入提示词使用的键值对。变量使用花括号书写，例如 `{invoice_number}` 或 `{url}`。这些值仅适用于输入框中的当前提示词。
* **保存提示词** – 保存当前提示词。可选择将其保存为：
  * **组织提示词** – 可在组织内编辑；包含提示词和已定义的变量值。
  * **全局提示词** – 在所有租户之间共享；仅包含提示词和变量占位符（不保存变量值）。
* **清除聊天** – 清除与 Operator 的当前对话，但保留输入框中的提示词不变。适用于重复使用或完善提示词。

有关如何编写有效提示词的详细指南，包括语法、变量和示例，请参阅[**提示词编写指南**](prompt-writing-guide.md)。

### **2. 侧边栏导航**

使用左上角的图标打开或关闭侧边栏。侧边栏显示已保存的提示词，并分为以下两类：

* **组织提示词**：可在组织内编辑和重复使用。
* **全局提示词**：在所有租户之间共享。这些提示词无法存储变量，也无法编辑或删除。
  * 全局提示词仍可由**创建该提示词的组织**编辑和删除；在该组织中，它显示在“组织提示词”下。
* **搜索功能：**侧边栏顶部的搜索栏可帮助用户按名称或关键词快速查找已保存的提示词。
* **图标说明：**每个已保存的提示词都有一组操作图标
  * **箭头** – 启动提示词
  * **钢笔** – 编辑提示词（仅适用于本组织的提示词）
  * **垃圾桶** – 删除提示词（仅适用于本组织的提示词）

### 3. 保存提示词

点击 **Save Prompt** 按钮会打开一个弹出窗口，可将当前提示词保存起来以供日后使用。

<div align="left"><figure><img src="../../.gitbook/assets/workflow_notification_card_overview.png" alt="保存提示词弹出窗口"><figcaption></figcaption></figure></div>

#### **保存提示词弹出窗口中的字段**

* **提示词名称：**输入一个名称以便识别此提示词。
* **公开保存提示词（复选框）：**勾选后，提示词将保存为**全局提示词**。全局提示词在所有租户之间共享，且无法存储变量**值**（仅存储变量**名称**）。
* **编辑变量：**打开[**提示词变量弹出窗口**](prompt-writing-guide.md#prompt-variables-popup)，以便在保存前查看或调整变量定义。

**操作**

* **取消：**关闭弹出窗口，不保存。
* **保存：**使用指定的名称和可见性设置保存提示词。

### 4. 提示词执行控制

提示词运行时，用户可以使用以下控制选项管理执行过程或进行干预：

* **暂停提示词：**暂时暂停当前执行。适用于查看当前状态或为后续步骤准备系统。
* **恢复提示词：**从暂停处继续执行。 ![](<../../.gitbook/assets/image (4).png>)
* **取消提示词：**完全停止执行并重置会话。如果提示词运行不正确或输入发生变化，需要中止或重新启动时，此操作会很有帮助。
* **接管控制：**允许用户直接与系统交互并手动干预。如果 Operator 卡住或误解某个步骤，此操作会很有帮助。接管控制会**自动暂停**提示词，并切换到手动模式，直到你选择恢复或取消。

### 5. Operator 详细视图

启动提示词后，会出现一个额外按钮，用户可通过该按钮切换到**详细执行视图**。 ![](<../../.gitbook/assets/Detailed view .jpg>)

* **打开详细视图：**此按钮会打开专用视图，逐步实时显示 Operator 正在执行的操作。

在详细视图中，用户可以：

* 监控正在执行的各项操作（例如点击、输入和等待）。
* 查看当前处于活动状态的步骤。
* 如果提示词执行遇到问题，找出问题发生的位置。
* 使用相同的**暂停**、**恢复**、**取消**和**接管控制**操作。

<div align="left"><figure><img src="../../.gitbook/assets/detailed view 2 .jpg" alt="DocBits Operator 详细视图，显示提示词 Open google.com then search for Alan MacMasters，步骤已完成，侧边栏中有已保存的提示词" width="563"><figcaption></figcaption></figure></div>
