# 分析仪表板

## 概述

**分析仪表板**可全面展示文档处理性能。它会追踪文档在处理旅程各个阶段所花费的时间（从导入到导出），帮助您发现瓶颈、比较不同组织、文档类型和供应商的性能，并将结果与 **DocBits 全球平均值**进行基准比较。

每份文档都会经过以下不同阶段：

**新建**（已导入）→ **处理中**（正在处理）→ **待验证**（等待用户审核）→ **待审批**（等待审批）→ **导出**（已完成并导出）

文档在每个阶段都会耗费时间。分析仪表板会准确显示耗时**多少**，以及应**重点改进哪里**。

### 两类瓶颈

仪表板可帮助您区分：

* **系统瓶颈** — DocBits 执行自动处理所需的时间（OCR 和文本提取、文档分类、字段提取、自动验证）。可通过配置和系统资源进行优化。
* **用户瓶颈** — 等待人工验证和审批所花费的时间（队列等待时间、人工数据更正、审核与验证、审批工作流）。可通过工作流和资源分配进行优化。

## 如何启用

分析仪表板由模块设置控制。启用后，左侧边栏中会显示一个 **分析仪表板**入口。

1. 前往 **设置 → 文档处理 → 模块 → 仪表板和分析**。
2. 启用 **分析仪表板**选项。

<mark style="color:red;">**注意**</mark>：分析仪表板需要 **AI 仪表板订阅**。

<mark style="color:red;">**注意**</mark>：只有拥有**管理员**权限的用户才能访问分析仪表板。

## 流程类型

选择适合分析的视角。每种流程类型都能从不同角度呈现相同的数据。

| 流程类型 | 用途 | 关键问题 |
| --- | --- | --- |
| **状态** | 追踪文档从导入到导出的生命周期 | *“文档从导入到导出的总耗时是多少？”* |
| **处理** | 分析技术模块的性能 | *“哪些处理步骤存在瓶颈？”* |
| **用户交互** | 分析人工接触点和等待时间 | *“文档等待用户处理的时间有多长？”* |

使用仪表板顶部的 **流程类型**切换开关，在不同视角之间切换。

<figure><img src="../.gitbook/assets/analytics_dashboard_flow_types.png" alt="流程类型切换开关"><figcaption></figcaption></figure>

### 状态流程

追踪文档从**新建**到**已导出**的处理旅程，适用于端到端生命周期分析。

<figure><img src="../.gitbook/assets/analytics_dashboard_status_flow.png" alt="状态流程"><figcaption></figcaption></figure>

### 处理流程

分析所有**技术处理模块**（OCR、分类、提取、验证）的性能，适用于发现系统侧瓶颈。

<figure><img src="../.gitbook/assets/analytics_dashboard_processing_flow.png" alt="处理流程"><figcaption></figcaption></figure>

### 用户交互流程

聚焦于**人工接触点**，包括队列等待时间、人工验证、审核和审批，适用于发现工作流和人员配置方面的瓶颈。

<figure><img src="../.gitbook/assets/analytics_dashboard_user_interaction_flow.png" alt="用户交互流程"><figcaption></figcaption></figure>

## 筛选选项

仪表板支持强大的多维筛选。所有图表、卡片和表格都会根据当前启用的筛选条件实时更新。

### 搜索

按**名称**或**唯一 ID**即时查找任何文档。

<figure><img src="../.gitbook/assets/analytics_dashboard_filter_search.png" alt="搜索筛选器"><figcaption></figcaption></figure>

### 流程步骤

选择特定步骤以聚焦分析。切换步骤的启用状态也会重新计算仪表板其他组件中的时间指标。

<figure><img src="../.gitbook/assets/analytics_dashboard_filter_flow_steps.png" alt="流程步骤筛选器"><figcaption></figcaption></figure>

### 子组织、文档类型、供应商、组

比较以下维度的性能：

* **子组织** — 不同的业务部门或租户
* **文档类型** — 发票、采购订单、送货单等
* **供应商** — 用于确定哪些供应商导致处理时间最长
* **组** — 比较分配给不同用户组的文档处理性能（适用于**状态**和**用户交互**流程类型）

<figure><img src="../.gitbook/assets/analytics_dashboard_filter_dimensions.png" alt="子组织、文档类型、供应商和组筛选器"><figcaption></figcaption></figure>

<mark style="color:red;">**注意**</mark>：**组**筛选器仅适用于**直接分配给组**的文档。分配给个人用户的文档（即使该用户属于某个组）也**不会**包含在组筛选结果中。

### 仅已导出的文档

默认启用。仪表板指标仅统计已完成导出的文档。

<mark style="color:red;">**注意**</mark>：禁用此选项可能导致平均值不准确，因为尚未完成处理的文档也会纳入计算。

<figure><img src="../.gitbook/assets/analytics_dashboard_only_exported_toggle.png" alt="仅已导出的文档切换开关"><figcaption></figcaption></figure>

### 时间范围

分析从 **7 天**到**整整一年**的任意时段，也可以使用日期选择器设置**自定义范围**。

<figure><img src="../.gitbook/assets/analytics_dashboard_filter_time_range.png" alt="时间范围筛选器"><figcaption></figcaption></figure>

## 流程步骤卡片

每张卡片都根据所选的**流程类型**代表一个流程步骤。卡片会随您的选择调整：**状态**类型显示生命周期阶段，**处理**类型显示处理模块，**用户交互**类型显示人工接触点。

每张卡片显示：

* 该步骤的**最短、平均、最长**耗时
* **您的平均耗时**与 **DocBits 全球平均值**的对比（开启对比切换开关时）
* 一个选择圆圈，用于在平均时间图表、时间趋势图和数据表所用的汇总时间计算中**纳入或排除**该步骤

标题栏中的**全选**切换开关可让您一次性纳入或排除所有步骤。

<figure><img src="../.gitbook/assets/analytics_dashboard_flow_steps_card.png" alt="显示最短、平均、最长耗时的流程步骤卡片"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/analytics_dashboard_step_toggle.png" alt="启用或停用步骤的切换开关"><figcaption></figcaption></figure>

### 与全球平均值比较

**与全球平均值比较**切换开关控制是否在卡片和图表中显示 DocBits 全球平均值。启用后，每张卡片上的平均耗时会以颜色标示：

* **绿色** — 您的平均耗时小于或等于全球平均值
* **橙色** — 您的平均耗时比全球平均值高出不超过 **+25%**
* **红色** — 您的平均耗时比全球平均值高出 **+25%** 或更多

<figure><img src="../.gitbook/assets/analytics_dashboard_global_average_comparison.png" alt="与 DocBits 全球平均值比较"><figcaption></figcaption></figure>

## 平均时间图表

平均时间图表展示所选流程步骤的处理时间分布。使用**分组依据**选择器，按不同维度进行比较：

* **流程步骤** — 查看哪些步骤耗时最多
* **子组织** — 识别不同业务部门之间的差异
* **文档类型** — 比较不同文档类型的处理时间
* **供应商** — 找出处理时间最长的供应商
* **组** — 比较分配给不同用户组的文档处理情况（仅适用于状态和用户交互流程类型）

启用**与全球平均值比较**后，图表还会显示 DocBits 全球平均值，供您进行基准比较。

<figure><img src="../.gitbook/assets/analytics_dashboard_average_time_chart.png" alt="平均时间图表"><figcaption></figcaption></figure>

## 顶部文档

**顶部文档**卡片会列出符合当前筛选条件的单份文档，并按总耗时排序。

* **排序顺序**切换开关 — 在**降序**（最慢的排在前面）和**升序**（最快的排在前面）之间切换。
* **每页条数**下拉菜单和分页功能 — 浏览结果集中的各页。
* 点击文档旁边的眼睛图标可**隐藏/显示**该文档。隐藏的文档不会纳入仪表板的任何时间计算。
* 点击标题栏中的眼睛图标，可**隐藏/显示**当前筛选结果中的所有文档。
* **点击文档**（文件名或进度条）可将其文档 ID 复制到剪贴板。

<figure><img src="../.gitbook/assets/analytics_dashboard_top_documents.png" alt="顶部文档"><figcaption></figcaption></figure>

## 时间趋势图

追踪性能随时间的变化趋势并发现异常。时间趋势图显示当前所选流程步骤的**平均耗时**，并可按以下维度分组：

* **流程步骤** — 每个所选步骤各显示一条线
* **子组织**
* **文档类型**
* **供应商**
* **组**（适用于**状态**和**用户交互**流程类型）

借助此图表，您可以轻松发现某个供应商的耗时突然上升，或某种文档类型的耗时逐渐增加，并在其演变成严重问题前及时处理。

<figure><img src="../.gitbook/assets/analytics_dashboard_time_trend.png" alt="时间趋势图"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/analytics_dashboard_time_trend_grouped.png" alt="按组显示的时间趋势图"><figcaption></figcaption></figure>

## 数据表

数据表提供对当前筛选条件下所有底层行数据的完整访问。

* 将列**拖入隐藏列面板**（位于表格左侧）可从视图中移除这些列。隐藏列会用于聚合计算，且**最短/最长/平均**耗时会根据可见列动态重新计算。将列标签拖回表格，或点击 **+** 图标，可恢复该列。
* 点击列标题可**排序**，也可以通过拖放**重新排列**列。
* 点击卡片标题栏中的按钮**下载 CSV**。导出的内容仅包含当前可见列。

<figure><img src="../.gitbook/assets/analytics_dashboard_data_table.png" alt="数据表"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/analytics_dashboard_data_table_hide_columns.png" alt="隐藏列以重新计算聚合结果"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/analytics_dashboard_data_table_export.png" alt="将数据表导出为 CSV"><figcaption></figcaption></figure>

## 无接触智能

**无接触智能**选项卡会显示有多少文档无需人工接触即可在 DocBits 中完成处理，以及其他文档在哪个环节停止。请参阅[无接触智能](touchless-intelligence.md)。
