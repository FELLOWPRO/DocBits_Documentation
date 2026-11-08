# 使用仪表板

<!-- touchless-admin-video-v2-20261104:start -->
**视频章节（审核版）：** [选择与数据时间戳](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/zh.html#chapter=01)。
<!-- touchless-admin-video-v2-20261104:end -->

### 筛选

| 筛选 | 作用 |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **7D / 30D / 90D** | 关键指标和队列所用的期间。默认为 30 天 |
| **Document Type** | 将 Touchless 指标及相关分析限定为某一类型，例如 INVOICE。已学习规则提案目前有独立的选择，见下文 |
| **Segment field / Segment value** | 仅当您的组织通过同一文档类型运行多个流程时使用（例如 `order_type` 字段中的直接、间接和 EAM 订单）。选择字段可查看细分，选择值可将全部内容收窄到该值 |
| **Document ID** | 为某一份文档打开 **Document Trace** |

您在 DocBits 顶部选择的**子组织**会收窄关键指标和供应商队列。问题集群和 AI 分析则始终覆盖整个组织。

### 顶层文档类型与已学习规则提案

在当前核对的实现中，顶部的选择器与**已学习规则提案**中的文档类型相互独立。该区域会自行加载可用类型，初始选择第一项。因此，上方选择 **ORDER_CONFIRMATION** 时，下方仍可能保留 **INVOICE**。这些提案针对的是发票，而不是为指标所选的订单确认。

应用规则之前，请核对该区域中显示的类型。如果那里没有可用的匹配类型，说明尚未建立针对该类型的提案。该区域还使用自己的数据基础，例如最近 60 天已更正的文档，而不会自动采用上方的期间。这里描述的是当前彼此独立的控件；并不表示同步已经实现。

### 五项关键指标

<figure><img src="../../../.gitbook/assets/touchless-report-kpi-zh-20261104.png" alt="当前 30 天发票报告：107 份完全自动处理的发票加上 11 份仅需审批的发票，合计 118 份，占 201 份的 58.7% AP Touchless。仅 Pure 为 53.2%。AP 卡片已显示合计数量 118。虚构的培训历史；未证实执行过 ERP 导出。"><figcaption><p>当前 30 天发票报告：107 份完全自动处理的发票加上 11 份仅需审批的发票，合计 118 份，占 201 份的 58.7% AP Touchless。仅 Pure 为 53.2%。AP 卡片已显示合计数量 118。虚构的培训历史；未证实执行过 ERP 导出。</p></figcaption></figure>

| 卡片                   | 显示内容                                             | 示例（说明性）                                                      |
| ---------------------- | ------------------------------------------------- | --------------------------------------------------------------------------- |
| **Pure touchless**     | 百分比以及与目标值的差值   | **63.2 %** · “120 documents” · “−6.8 pp vs 70 % target”（红色，低于目标） |
| **AP touchless** | 合并的百分比与数量：Pure 加仅审批 | **78.9%** · 此示例中为“150 documents”，其中 Pure 120、仅审批 30 |
| **AP assisted**        | 文档数量及其占比           | **30** · 15.8 %                                                             |
| **Process exceptions** | 文档数量及其占比           | **10** · 5.3 %                                                              |
| **Diagnosis coverage** | 有多少受阻文档具有**已知**原因 | **80 %** · “10 without a known cause”                                       |

* 在当前截图中，107 份完全自动处理加上 11 份仅审批的发票为 **118 ÷ 201 = 58.7% AP Touchless**。仅 Pure 为 **107 ÷ 201 = 53.2%**。这两个百分比相互重叠，不可相加。
* 没有可计量内容时，卡片显示破折号（—）而不是 **0 %**。破折号表示“无数据”，而不是“零”。
* **Diagnosis coverage** = 具有已知阻塞原因的文档 ÷ 所有受阻文档。示例：50 份受阻文档，其中 10 份原因未知 → 40 ÷ 50 = **80 %**。数值偏低意味着“我们还不清楚文档为何停下”。在尝试修复单个原因之前，先改善这一点。
* **点击卡片**可在新标签页中打开该数字背后的文档列表（“View the documents behind this number”）。文档数为 0 的卡片不可点击。

### Touchless 比率随时间变化

<figure><img src="../../../.gitbook/assets/touchless-report-trend-zh-20261104.png" alt="当前报告趋势：粉色为 Pure Touchless，蓝色为包含仅审批文档的合并比率。虚线标示 70% 的目标。这些曲线使用虚构的培训案例，不构成实际的流程改进。"><figcaption><p>当前报告趋势：粉色为 Pure Touchless，蓝色为包含仅审批文档的合并比率。虚线标示 70% 的目标。这些曲线使用虚构的培训案例，不构成实际的流程改进。</p></figcaption></figure>

当前图表显示 **Pure Touchless**、**合并的 AP Touchless 比率**以及**目标线**。蓝色包含 Pure 和仅审批，因此它位于粉色线之上或与之重合；不要把这两个值相加。每个点都有各自符合条件的已完成文档数，因此单日比率并不自动等于整个期间的比率。较短期间显示每日点，较长期间显示每周点。单独的仅审批结果类别与此合并线不同。

**示例。**您在 10 月 1 日开启自动 PO 匹配后，pure 比率在两周内从 55 % 升至 68 %。图表会显示曲线转向的那一天，便于您调查时间点。前后关联本身并不能证明是这项设置带来了改进。请比较文档类型、供应商构成和其他变更。

### Touchless 首先在哪里流失

<figure><img src="../../../.gitbook/assets/touchless-blocking-stages.png" alt="按首个阻塞阶段和原因统计的受阻文档柱状图"><figcaption><p>按文档首次停止的阶段和原因统计的受阻文档。此处 <strong>Field validation: Required field missing</strong> 损失的文档最多（58 份），其次是 <strong>Export mapping failed</strong>（46 份）和 <strong>PO item mismatch</strong>（27 份）。示例组织，使用演示数据；供应商名称为虚构。</p></figcaption></figure>

按流水线阶段统计**受阻文档**的柱状图：即让文档停下的**第一个**阶段。

**示例。**柱条：Supplier Identification 12、Field Validation 41、PO Line Match 7。最高的柱子提示您先查看 **Field Validation**。提取值缺失是可能原因之一；确认之前，请比较原始发票、字段规则和可用的源数据。

### 供应商机会

<figure><img src="../../../.gitbook/assets/touchless-supplier-queue.png" alt="Supplier opportunities 表，包含 volume、pure rate、lost documents、root cause、recoverable documents、expected lift、confidence 和 status"><figcaption><p>供应商队列（缩短为首四行）。第一家供应商有 106 份文档、38.7 % 的 pure 比率和 65 份可挽回文档，因此修复它价值 <strong>+21 pp</strong>。示例组织，使用演示数据；供应商名称为虚构。</p></figcaption></figure>

该队列回答**“我们应该先修复哪家供应商？”**。它按**可挽回**文档数排序，从高到低，每页 25 行。

| 列                         | 含义                                                                                                                                                   |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Supplier Number / Supplier** | 供应商。无法识别供应商的文档显示为 **No supplier identified (n documents)**                                                  |
| **Volume**                     | 该期间内该供应商符合条件的文档数                                                                                                          |
| **Pure Rate**                  | pure touchless 文档的占比。达到或超过目标为绿色，低于目标为红色                                                                          |
| **Lost Documents**             | 最终成为 AP assisted 或流程异常的文档。并不总意味着有人参与：ERP 拒收或停滞七天的文档也计入 |
| **Root Cause**                 | 修复责任的归属：Configuration、ERP integration、Export、Extraction、Master data、Measurement、PO matching、User process、Validation 或 Unknown          |
| **Recoverable**                | 原因可由 DocBits 修复的流失文档：配置、主数据或供应商模板                                                               |
| **Expected Lift**              | 如果该供应商所有可挽回文档都能 touchless 运行，贵组织的比率将提升多少**百分点**（**+x pp**）               |
| **Confidence**                 | **High**、**Medium** 或 **Low**：诊断的确定程度                                                                                                |
| **Status**                     | New、Open、Investigating、In progress、Confirmed、Resolved、Dismissed。文档数过少的供应商显示 **NEEDS\_DIAGNOSIS**                       |

**示例。**贵组织在该期间有 1,000 份符合条件的文档。供应商 A 有 40 份可挽回文档，供应商 B 有 90 份流失文档但只有 10 份可挽回（其问题在供应商一侧）。

* 供应商 A：40 ÷ 1,000 = **预期提升 +4.0 pp**
* 供应商 B：10 ÷ 1,000 = **+1.0 pp**，尽管 B 的流失文档更多

队列将 A 排在 B 之前，因为**预期提升**是相对整个组织来衡量的，而不是相对该供应商。只有四份问题文档的供应商无法排在有四百份问题文档的供应商之前。

使用搜索框（“Search supplier number or name”）查找供应商。点击某一行可打开 **Supplier Diagnosis**。

### 比较供应商

<figure><img src="../../../.gitbook/assets/touchless-compare-suppliers.png" alt="Compare suppliers 页面，三家供应商并排显示，并有各结果的柱状图"><figcaption><p>三家供应商并排比较：pure 比率、流失与可挽回文档、根本原因、预期提升，以及各结果的柱状图。每个 <strong>Open</strong> 都指向 Supplier Diagnosis。示例组织，使用演示数据；供应商名称为虚构。</p></figcaption></figure>

点击 **Compare suppliers**，勾选**两到五家**供应商（每家都会列出其受阻文档数），然后点击 **Compare**。

比较结果会并排显示各供应商的 **Pure rate**、**Lost documents**、**Recoverable**、**Root cause**、**Expected lift**，各结果的柱状图，以及指向每个 **Supplier Diagnosis** 的链接。

**示例。**供应商 A 和 B 发送相同的发票版式。B 的 pure 比率为 80 %，A 只有 35 %。A 的诊断提示“Master data”。在确认该原因之前，请比较原始发票、提取值和导入的供应商记录。仅凭比率差异不能证明版式正确，也不能证明 A 的主数据不完整。

### 使用 AI 分析

按钮 **Analyse n clusters with AI** 会分析 touchless 潜力最高的问题集群（每个集群至少达到最低文档数）。每个集群约需 13 秒，覆盖**整个组织**。只有管理员可以启动。

运行时，您会看到每个集群显示 **Queued**、**Running**、**Done**、**Already analysed** 或 **Error**，并带有 **Open cluster** 链接。如果环境中 AI 已关闭或未配置，该按钮会被禁用并说明原因，此时**页面上的其他所有内容仍可正常使用**。

## 使用 Touchless Intelligence：日常工作流程

1. **每周**：打开该选项卡，对照目标检查**比率**和**趋势**。
2. 查看**诊断覆盖率**。低于约 80 % 时，先查明文档为何停下。
3. 阅读 **Where touchless is lost first**，选择最大的阶段。
4. 打开 **Supplier opportunities**。按 **Expected lift** 排序，选取状态为 **RECOVERABLE** 的首家供应商。
5. 阅读**问题集群**，检查 **Missing evidence**，然后按照 **What to change** 操作。
6. 修复一个已确认的原因。对于受支持的 DocBits 提案，使用预览和变更历史。对于 Infor 更正，另行记录来源并导入；它不会自动生成 DocBits 设置变更条目。
7. 两周后检查**前后**结果。

## 谁可以查看

* 该选项卡属于 Analytics Dashboard。管理员为组织启用它。如果选项卡缺失，请联系管理员。
* **组织管理员**始终可以查看。
* 当管理员为其角色授予 **Analytics dashboard** 选项卡权限后（**Settings → Roles**），其他用户才能查看。没有授权时，只有管理员可以访问。
* 部分操作仅限管理员：**AI analysis**、**应用和撤销变更**、**已学习规则提案**以及 **Consulting report**。

如果没有权限，页面会显示 _Action not allowed, please contact the administrator_。

## 相关页面

* [Touchless Intelligence](./)
* [指标与计算](touchless-metrics.md)
* [完整示例：价格与数量](touchless-examples.md)
* [供应商诊断与问题集群](touchless-supplier-diagnosis.md)
* [PO 匹配诊断](touchless-po-matching-diagnosis.md)
* [文档追踪](touchless-document-trace.md)
* [变更提案与报告](touchless-change-proposals.md)
* [通过 MCP 解释和改进 Touchless](touchless-mcp.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->
<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
