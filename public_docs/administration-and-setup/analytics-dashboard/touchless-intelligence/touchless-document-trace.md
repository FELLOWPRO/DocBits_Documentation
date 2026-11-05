# 文档追踪

<!-- touchless-admin-video-v2-20261104:start -->
**视频章节（审核版）:** [比较执行记录](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/zh.html#chapter=08).
<!-- touchless-admin-video-v2-20261104:end -->

在 **Document ID** 中输入文档 ID，或从集群中打开一个示例文档，即可查看 **这份文档发生了什么** 。

页眉显示文件、其状态（例如 **进行中** ）、您正在查看的运行及其首个阻塞点，以及一个带有文档 ID 的 **文档** 按钮。

<figure><img src="../../../.gitbook/assets/touchless-nova-trace-overview-zh.png" alt="Dev NOVA：第一次测试运行的处理路径和真实记录值"><figcaption><p>2026 年 11 月 4 日在 Dev NOVA 11.0.3 重新截取。虚构测试发票停在字段验证阶段。分类、供应商查找、表头提取和表格提取均包含真实记录值，右侧卡片显示文档和运行历史。这是正在运行的产品界面。 本版本的路径阶段名称仍为英语；摘要中的“邮政信箱”实际指采购订单号，“已屏蔽”在此表示处理受阻。</p></figcaption></figure>

 **管道路径** 显示 14 个阶段：Intake、Classification、E-Document Validation、Supplier Identification、Text Recognition、Header Extraction、Table Extraction、Field Validation、PO Lookup、PO Line Match、Approval、Workflow Routing、Export、ERP Acknowledgement。每个阶段带有一种状态：

| 状态 | 含义 |
| --- | --- |
| **通过** （绿色） | 该阶段顺利完成 |
| **止步于此** （橙色） | 该阶段阻止了文档 |
| **未到达** | 路径中位于首个阻塞点之后的阶段；请检查日志中是否还记录了额外执行情况 |
| **未记录任何内容** （虚线） | 该阶段没有记录任何数据 |
| **不适用** | 该阶段不适用于此文档 |

### 阶段日志

路径下方的 **阶段日志** 列出相同的阶段以及各阶段记录的内容。每行左右两侧分别是状态圆点和状态词。

* 每个值都是一个 **值标签** ：带单位的数字，例如 **置信度 100 %** 、 **阈值 60 %** 、 **失败规则 0** 、 **8 个缺失字段** 或 **0 个映射缺口** 。百分比显示为 `97 %`，绝不显示为 `0.97`。
* **详情** 会展开某个阶段记录的完整值列表，包括它考虑过的备选项。
* 阻止文档的阶段会说明原因，例如 **字段验证失败** 。
* 没有任何阶段记录的值显示为 **未记录** ，绝不显示为编造的值。值均为数字和固定词汇，绝不是文档正文。
* 当支持人员需要时， **显示原始诊断** 可打开原始数据。

<figure><img src="../../../.gitbook/assets/touchless-nova-trace-stage-log-zh.png" alt="Dev NOVA：含置信度、提取记录值和字段验证阻塞的阶段日志"><figcaption><p>真实的第一次运行：分类置信度 100%，供应商候选数 0，表格行数 1，映射缺口 7。阶段通过仅表示该阶段已执行，并不证明供应商匹配成功或所有发票值都正确。字段验证报告缺少必填字段。</p></figcaption></figure>

### 运行与变化

通过运行选择器选择一次尝试，运行历史显示其结果和首个阻塞点。已记录的差异将所选运行与其前一次运行比较，并非自动与当前运行比较。差异标记包含单位，相同值保持无变化。

文档卡片列出类型、供应商、发票号、采购订单、页数及记录的分析方法。本例的手动方法对应测试导入时指定的文档类型。因此，100% 分类值不是自动分类准确率的独立证明。

### 阅读供应商和表格详情

<figure><img src="../../../.gitbook/assets/touchless-nova-trace-supplier-zh.png" alt="Dev NOVA：区分已找到的标识、主数据查询和供应商匹配"><figcaption><p>本次运行在发票上找到供应商名称，并查询主数据，但未匹配到供应商。测试发票未提供增值税号、IBAN、电子邮件地址或 GLN。主数据无匹配与未找到发票值是不同的诊断结果。 底部的“比赛结果由”指匹配判定来源，与比赛无关。</p></figcaption></figure>

分别检查三个问题：文档上是否存在该标识，是否进行了查询，以及是否匹配到了供应商。绿色阶段本身无法回答这三个问题。

<figure><img src="../../../.gitbook/assets/touchless-nova-trace-table-zh.png" alt="Dev NOVA：第一次运行的表格详情显示七个映射缺口"><figcaption><p>详情显示 1 个表格、1 行及 7 个映射缺口。判断提取错误之前，应先检查列映射。底部的比较说明不能作为所选第一次运行的有效比较基准，因为第一次运行没有前一次运行。</p></figcaption></figure>

### 识别真实的人工重启

<figure><img src="../../../.gitbook/assets/touchless-nova-trace-runs-zh.png" alt="Dev NOVA：两个真实运行的阶段记录值对比，数值未变化"><figcaption><p>同一张测试发票经过真实的人工重启，期间没有修改发票字段。新增运行只能证明再次尝试，不能证明改进成功。相同值显示为无变化，没有编造差异标记。</p></figcaption></figure>

人工重启属于人工干预。此案例只有在之后成功完成时，才会归入 AP Assisted。只要仍在处理中，就不计入已完成文档的比率分母。

证据范围。本案例未证明业务审批、成功导出或 ERP 确认。旧版采购订单匹配器在这里没有记录决策路径，因此不能作为已完成 Infor 比对的证据。NOVA 11.0.3 的日志可能在字段验证阻塞后仍记录采购订单查找通过，而处理路径却将其显示为后续阶段，需同时检查两种视图。摘要卡片也可能显示发票号未记录，但提取结果中已存在该值；核对数值时应查看原件与提取字段。

## 区分提取问题和源数据问题

核对原件与更正前的字段及行项目，再比较导入订单与当前 Infor，包括单位、价格单位及导入时间。证据不足时保持原因未确认。

 **示例：**  原件与提取都是 10 €，导入订单为 9 €。这说明订单有差异，不是已证实的提取错误。先确认约定价格。人工重启后成功归为 AP Assisted。参见[指标计算](touchless-metrics.md)。反复缺字段只证明重复阻塞，不一定缺默认值；检查原件、提取、验证及配置。

## 核实初始提取和连续阻塞的证据

选择同一文档及执行，核对订单号、币种、数量、单位、价格单位、单价和金额。区分当前值与更正前值；切换执行不保证恢复每个历史单元格。缺少初始值时标记为 **无法评估** ，先定义核查范围与样本量。比较导入副本、时间和当前 Infor。

第一次执行可能等待订单，下一次导入后才发现价格差异；第一次不证明已到达后续检查。人工重启在成功后仍是 AP Assisted；最终 ERP 错误优先。没有记录就是缺少证据。

工具及人工操作分类见[Touchless 与 MCP](touchless-mcp.md)。

## 相关页面

* [Touchless Intelligence](./)
* [供应商诊断和问题集群](touchless-supplier-diagnosis.md)
* [采购订单匹配诊断](touchless-po-matching-diagnosis.md)

本页面的屏幕截图显示中文界面。

<!-- Alignment 2026-11-04: correct extraction is distinct from process Touchless; KPI numerator and denominator verified. -->

<!-- Completion 2026-11-04: localized MCP examples, AP actions, original-value evidence and owned synthetic PO cards. -->

这五张新截图展示 Dev NOVA 11.0.3 的本地化界面及同一张专门创建的测试发票。任何单独的原件与字段示意图都仅用于说明该数值比较。
