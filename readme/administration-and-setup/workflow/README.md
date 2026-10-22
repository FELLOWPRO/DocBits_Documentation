---
description: "DocBits 工作流引擎"
---

# 工作流

<figure><img src="../../.gitbook/assets/Bildschirmfoto 2024-03-12 um 19.42.57.png" alt=""><figcaption></figcaption></figure>

## DocBits 工作流引擎：简化流程自动化

### 理解并准备工作流 <a id="workflow-orientation"></a>

在真实的 DocBits 测试账户中查看仪表板上的八次工作流运行、两个执行顺序为 100/200 的已保存工作流，以及三个通过的测试场景。本教程还介绍标准和高级工作流、许可证、模板和 Card SDK。

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/zh.mp4" %}

[观看带字幕的视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/zh.html) · [打开视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/zh.mp4) · [字幕（WebVTT）](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/zh.vtt) · [文字稿](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/zh.txt) · 2:56

<details>
<summary>章节与文字稿</summary>

| 章节 | 开始时间 |
| --- | --- |
| 认识管理员 | [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/zh.mp4#t=0.000) |
| 组织与访问权限 | [0:03](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/zh.mp4#t=3.958) |
| 仪表板与筛选器 | [0:14](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/zh.mp4#t=14.250) |
| 工作流列表 | [0:50](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/zh.mp4#t=50.167) |
| 执行顺序 | [1:04](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/zh.mp4#t=64.375) |
| 标准工作流 | [1:20](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/zh.mp4#t=80.333) |
| 高级工作流 | [1:33](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/zh.mp4#t=93.042) |
| 许可证 | [1:48](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/zh.mp4#t=108.667) |
| 模板 | [2:06](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/zh.mp4#t=126.250) |
| 测试管理器 | [2:19](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/zh.mp4#t=139.500) |
| Card SDK | [2:32](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/zh.mp4#t=152.458) |
| 准备检查 | [2:43](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/zh.mp4#t=163.625) |

**认识管理员**

我来演示如何在 DocBits 中检查发票。

**组织与访问权限**

好，我先检查顶部显示的组织。 这里的工作流设置属于当前选中的组织。 这次演示使用专门的文档测试账号。

**仪表板与筛选器**

工作流仪表板提供整体概览。 为了展示这个概览，我用一张示例发票，手动执行了两个培训工作流，共运行八次。 这里显示八次总运行，其中六次成功。 另外两次运行没有满足金额条件。成功率也会计入这些正常结束的条件检查。 我按工作流名称筛选，并检查日期范围。统计数字和图表会随筛选更新。 右侧可以切换查看已保存的工作流和测试场景。测试管理器的运行会单独统计。

**工作流列表**

在工作流列表中，我管理每一个工作流，检查名称、标准或高级类型、执行顺序、触发条件以及可用操作。 创建之前，先搜索是否已经存在合适的工作流。

**执行顺序**

如果多个工作流处理同一个文档，执行顺序就很重要。 我检查哪个先运行，以及下一个需要什么数据。 这里，发票审核的顺序值是一百，下一个检查是两百。数值越小，执行越早。

**标准工作流**

对于线性规则，我选择标准工作流。When 定义触发条件，And 添加判断条件，Then 执行操作。卡片库提供当前可用的组成部分。

**高级工作流**

需要不同处理路径时，我使用高级工作流。这个设计器预览显示 Start 和明确的连接。成功、条件不满足以及错误可以走不同的路径。卡片的位置本身不决定执行顺序。

**许可证**

在许可证页面，我分别检查基础工作流和高级工作流。这里两项都未启用。方案窗口显示可用订阅。我只查看并关闭窗口，不修改订阅。打开设计器预览不等于启用工作流引擎。

**模板**

模板可以作为可重复使用的起点。我打开模板库，并查看默认模板选项。应用到自己的流程前，仍然需要检查字段、接收人和每一项操作。

**测试管理器**

测试管理器保存标准和高级工作流的测试场景。 配置完成后，我添加有代表性的输入数据和预期结果。 运行全部测试可以检查修改后的行为。

**Card SDK**

卡片 SDK 用于自定义扩展。开发人员可以使用模板、上传软件包或者从 GitHub 导入。日常管理通常先使用已有的卡片库。

**准备检查**

开始搭建前，我确认组织、访问权限、所需许可证、文档字段和预期结果，再决定线性规则是否足够。 下一个视频会逐步创建标准工作流。

</details>

### 简介

在流程自动化领域，DocBits 工作流引擎以简洁直观的方式脱颖而出。该引擎通过清晰简单的基于规则的结构，简化工作流的创建和管理。其设计的核心原则是“简单的 When-And-Then”规则，将自动化流程拆分为三个基本组成部分：触发器、条件和操作。本指南将说明每个组成部分在系统中的功能，以及它们如何协同工作以实现顺畅的自动化。

### “简单的 When-And-Then”规则说明

DocBits 工作流引擎遵循一个简单而强大的原则，让各种技能水平的用户都能轻松使用工作流自动化。该原则概括为“简单的 When-And-Then”规则，具体如下：

#### [When](./#when-trigger)（触发器） <a id="when-trigger"></a>

* **定义**：“When”组成部分代表工作流的_触发器_。它是启动工作流执行的事件或条件。触发器可以是各种情况，例如收到新邮件、到达特定日期和时间，或创建新文档。
* **示例**：“当提交新的客户表单时……”

#### [And](./#and-condition)（条件） <a id="and-condition"></a>

* **定义**：“And”组成部分引入了操作继续执行所必须满足的_条件_。条件充当筛选器或标准，用于细化触发器，确保工作流仅在特定情况下执行。
* **示例**：“……并且客户属于‘Enterprise’细分群体……”

#### [Then](./#then-action)（操作） <a id="then-action"></a>

* **定义**：最后，“Then”部分指定了触发器发生且条件满足后要执行的_操作_。操作是工作流执行的任务或运作，例如发送邮件、更新数据库，或在项目管理工具中创建任务。
* **示例**：“……然后将潜在客户分配给企业销售团队，并发送欢迎邮件。”

### 组合各组成部分，创建强大的自动化流程

通过组合这三个组成部分——触发器、条件和操作——DocBits 工作流引擎让用户能够创建高度定制且高效的工作流。这种模块化方式不仅简化了自动化设置流程，还提供了灵活性，可创建能够处理各种任务和流程的复杂工作流。

### 结论

DocBits 工作流引擎的“简单的 When-And-Then”规则体现了该引擎致力于提供用户友好平台以实现流程自动化的理念。通过将自动化拆分为触发器、条件和操作这些基本要素，这条简单明了的规则让用户更容易理解、创建和管理工作流。无论您是刚接触工作流自动化，还是经验丰富的专业人士，DocBits 工作流引擎都能提供高效易用的工具，帮助提升工作效率并简化运营。

## 从入门到专家的学习路径

[从入门到专家的学习路径](workflow-learning-path.md). 请按顺序完成各阶段。仅阅读并不足够：每个阶段都要形成自己的配置、可核对的预期与验证依据。P0 用于避免根本性的执行误判；P1 深入讲解数据、业务决策和集成。
