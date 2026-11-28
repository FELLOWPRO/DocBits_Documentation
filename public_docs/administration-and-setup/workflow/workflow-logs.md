# 工作流日志

有关高级日志视图的讲解式说明，请观看 [Find the relevant execution](advanced-workflow-builder/videos.md#find-the-relevant-execution) 和 [Trace nodes and diagnose](advanced-workflow-builder/videos.md#trace-nodes-and-diagnose)。这两个章节均提供英语和德语版本，并附有字幕文件和文字稿。

## **概述**

**工作流日志**允许用户分析某个文档执行了哪些 Workflow、了解执行结果，并深入查看条件级别的详细信息，以便进行调试或验证。

## **访问工作流日志**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4" %}

**视频：** 阅读工作流日志 · 1:34 · [Captions (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.vtt)

<details>

<summary>文字稿</summary>

**打开工作流日志** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=0.25)

每个文档都会保留在其上运行过的 Workflow 日志。在文档 Dashboard 中，打开某个文档的 Actions 菜单，然后选择 Workflow Logs。

**运行及其结果** · [0:12](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=12.15)

顶部显示共有多少次运行，以及其中多少次以错误、条件不满足或成功结束。下方逐条列出每次运行及其 Workflow、时间、时长和结果。

**一次运行的路径** · [0:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=25.716)

将分隔条向左拖动，为日志留出更多空间。然后点击一次运行，查看它走过的路径。每张卡片都会显示其结果：绿色表示成功，橙色表示条件不满足，红色表示错误。这里的 And 卡片以条件不满足结束，因此其后的 Then 卡片没有运行。

**卡片为何如此结束** · [0:45](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=45.35)

选择一张卡片即可阅读其日志。日志会说明该卡片比较了什么，以及它为何如此结束。此处文档已准备就绪，可以进行验证，但该卡片预期的是待处理的第二次批准。

**错误及其原因** · [0:58](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=58.283)

以错误结束的运行会把出错的卡片显示为红色。这里的 And 卡片无法从文档中读取送货地址。数据缺失始终是错误，因此其后的 Then 卡片没有运行。

**查找运行** · [1:13](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=73.216)

运行次数很多时，可以使用搜索按名称查找 Workflow，并使用筛选按钮按状态或日期缩小列表范围。

**执行限制提示** · [1:23](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=83.116)

当某个 Workflow 在此文档上达到其执行次数上限时，顶部会出现一条提示。关于执行限制的视频对此进行了解释。

</details>

要访问工作流日志：

1. 前往 **Dashboard**。
2. 点击所需文档旁的 **Actions menu**（三点图标）。
3. 从菜单中选择 **Workflow Logs**。
   * <mark style="color:red;">**Note**</mark>：必须启用 Workflow 功能才能访问此选项。
4.  将打开一个 **side panel**，显示已执行 Workflow 的摘要。\\

    <div align="left"><figure><img src="../../.gitbook/assets/image (5).png" alt="Dashboard with the workflow logs side panel showing summary counters and a table of executed workflows with result icons" width="563"><figcaption></figcaption></figure></div>

## **以独立页面打开日志**

side panel 会遮挡文档列表。对于需要查看较长时间的文档 Workflow，可以将同一日志以完整页面打开：在面板标题栏中选择新窗口图标。该页面的地址为 `/workflows/logs/<document id>`，因此你可以将其保持在第二个浏览器窗口中打开，或把该地址发送给有权访问该文档的同事。

该页面显示与面板相同的摘要计数器、相同的已执行 Workflow 表格以及相同的详细信息视图。

## **切换到其他文档**

在完整页面上，列表上方的搜索字段可按名称或 ID 查找文档。搜索结果会显示每个文档的上传日期、受理人以及状态，因此你可以区分名称相似的文档。选择某个结果会加载其工作流日志，并将该文档写入地址。搜索范围涵盖你的权限允许你查看的组织内文档；当没有匹配项时，DocBits 会在字段下方给出说明，而不是显示空列表。

## **工作流日志面板的组成部分**

#### **1. 工作流摘要计数器**

位于日志面板顶部：

* **蓝色**：已执行的 Workflow 总数。
* **红色**：以**错误**结束的 Workflow。
* **黄色**：因条件不匹配而**未完成**的 Workflow。
* **绿色**：成功**执行**的 Workflow。

#### **2. 工作流执行表格**

表格中的每一行代表一次 Workflow 执行，包含：

* **Workflow Name**
* **Timestamp**（Created On）
* **Runtime**（秒）
* **Result Icon**：
  * 绿色对勾：Workflow 已成功执行。
  * 红色叉号：Workflow 执行时发生错误。
  * 橙色短横线：由于条件未满足，执行已停止

点击每行左侧的**箭头**可展开 **Workflow** 详细信息视图。

<div align="left"><figure><img src="../../.gitbook/assets/workflow_test9_match_check_overview.png" alt="Expanded workflow log row showing When and And condition cards with green checks and a grayed card that was not met, plus card logs" width="563"><figcaption></figcaption></figure></div>

### **工作流详细信息视图**

点击某个 Workflow 行会打开其**详细执行日志**，其中显示：

#### **条件评估**

* **When...** 区块：初始条件。
* **And...** 区块：附加条件。
* **Then...** 区块：所有条件均满足时执行的操作。

每个条件行会显示：

* **绿色对勾**：条件已满足。
* **橙色短横线**：条件未满足。
* **红色叉号**：条件**因错误而**失败

### **重要行为说明**

如果 Workflow 中的某个条件**未满足**，系统会**停止评估该 Workflow 内的任何后续卡片**。此行为可避免不必要的处理\
作为一种视觉提示，**未满足其条件**的卡片会显示为**灰色**，同一 Workflow 中的**所有后续卡片**也会显示为**灰色**，表示它们**未被执行**。
