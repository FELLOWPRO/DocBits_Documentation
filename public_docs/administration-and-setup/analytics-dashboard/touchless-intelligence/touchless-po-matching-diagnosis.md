# 采购订单匹配诊断

<!-- touchless-admin-video-v2-20261104:start -->
**视频章节（审核版）：** [跟踪文档](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/zh.html#chapter=07).
<!-- touchless-admin-video-v2-20261104:end -->

## 概述

许多发票停在了采购订单这一步。发票说的是一个内容，采购订单（PO）说的是另一个内容，而配置的检查无法自动消除差异。**即使提取正确，只要源系统数据不同，采购订单匹配仍可能受阻。** 暂时停止还不是最终结果：后续的自动处理可能成功，而一次记录在案的人工更正或重新启动，会让一份成功完成的文档不再是无接触的。

Touchless Intelligence 会显示采购订单匹配**为什么**失败，以及 DocBits **如何**尝试匹配。本页介绍涉及的两个流水线阶段、您会看到的原因，以及**采购订单匹配决策流程**——一张按顺序展示各匹配步骤的示意图。

### 在 Touchless Intelligence 中哪里可以看到采购订单匹配

| 位置 | 您会看到的内容 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Where touchless is lost first**（概览选项卡） | 例如 _PO line match: PO item mismatch_ 这样的柱状条。它告诉您有多少份文档停在这里 |
| **Supplier opportunities** | 根本原因为 **PO matching** 的供应商 |
| **Supplier Diagnosis** 中的 **How this organisation matches** 部分和 **issue cluster** | 带有您组织规则集的决策流程 |
| **Document Trace** | 状态为 **blocked** 的 **PO Line Match** 阶段及其原因 |
| **Settings → Document Types → More Settings → Purchase Order** | 匹配规则本身。参见 [Purchase Order Matching Rules](../../settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) |

## 两个采购订单阶段

| 阶段 | 问题 | 停止原因 |
| ---------------------- | ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **9 · PO Lookup** | 这张发票有对应的采购订单吗？ | _Purchase order not found_ |
| **10 · PO Line Match** | 发票的每一行都匹配到一条采购订单行吗？ | _PO item mismatch_, _PO line identifier mismatch_, _Unit price outside PO tolerance_, _Quantity outside PO tolerance_ |

停在第 9 或第 10 阶段的文档，在供应商队列中会以第一个阻塞原因 **PO matching** 显示。

## 采购订单匹配失败的原因

| 您看到的原因 | 含义 | 典型原因 | 要更改的内容 |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Purchase order not found** | DocBits 未找到发票上采购订单编号对应的采购订单 | 采购订单编号读取错误或缺失；采购订单尚未导入；采购订单属于其他供应商 | 检查该供应商的采购订单编号提取、采购订单主数据导入以及供应商关联 |
| **PO item mismatch** | 发票行未能匹配到采购订单行 | 供应商使用自己的项目编号；描述不同；行项目被合并或拆分 | 检查项目编号映射以及匹配规则中的**规则优先级**；为供应商识别行项目的方式添加一条规则 |
| **PO line identifier mismatch** | 发票上的行编号或标识符与采购订单不符 | 供应商重新编排了行号 | 改为按项目和数量匹配，而不是按行编号匹配 |
| **Unit price outside PO tolerance** | 价格偏差超过了允许的容差 | 真实的价格变动、舍入差异或不同的价格单位 | 检查规则集中的 **Unit price tolerance**；更正采购订单或联系供应商 |
| **Quantity outside PO tolerance** | 数量偏差超过了允许的容差 | 部分交货、超量交货 | 检查 **Match quantity on** 和 **Quantity tolerance** |
| **PO matching service error** | 匹配服务未能给出结果 | 临时的技术问题 | 重新启动文档；如果问题反复出现，请联系支持 |
| **Automatic PO export disabled** | 设置 **Auto export if PO matched 100%** 处于关闭状态，因此已匹配的文档不会被自动导出 | 该设置处于关闭状态 | 如需自动导出，请启用该设置。参见 [Auto Export if PO Matched 100%](../../settings/document-processing/module/auto-export-if-po-matched-100.md) |

{% hint style="info" %}
并非所有采购订单匹配原因都能在 DocBits 中解决。如果供应商发送了错误的采购订单编号，卡片会显示 **Supplier action only**：供应商必须更正文档并重新发送。
{% endhint %}

价格和数量的单独案例及其证据请参见[示例](touchless-examples.md)。


## 采购订单匹配决策流程

决策流程展示 DocBits 如何尝试把发票行匹配到采购订单行。它包含**五个阶段**，第一个匹配成功的阶段即生效：

1. **Single match validation**：按优先级顺序应用规则。这是常规情况，一个发票行和一个采购订单行
2. **Multi match validation**：单项匹配之后，当一侧涉及多行时
3. **Total match validation**：仅在完全没有匹配时使用。将采购订单行的总额与其表格行之和进行比较
4. **Single mismatch validation**：忽略单价，因此即使价格不同，也可以按项目和数量匹配一行
5. **Fallback logic**：只剩一个采购订单行和一个表格行时，将它们配对

在各阶段内部，DocBits 按以下顺序尝试：

* **Exact match for all rules**：所有比较的值完全相同
* **Tolerance-based match**：数值可以在容差范围内偏差
* **Package criteria**：最后一轮，基于规则集的包装相关条件

每一步都会问 **Match found?**。回答 **Yes**（绿色）会进入 **Match found**，文档继续处理。回答 **No match**（红色）则进入下一步；最后一步之后结果为 **No match found**：文档停止，需要人工介入。

<figure><img src="../../../.gitbook/assets/touchless-po-matching-flow.png" alt="采购订单匹配决策流程：规则集标题栏、五个带编号的匹配阶段及其各轮尝试，以及终点 Match found 和 No match found"><figcaption><p>采购订单匹配决策流程，从供应商诊断页面上的 <strong>How this organisation matches</strong> 打开。标题栏显示规则集（版本 7，归本组织所有）以及各项容差。其下是五个阶段及其各轮尝试，自上而下依次执行。绿色通向 <strong>Match found</strong>，红色进入下一步并最终到达 <strong>No match found</strong>。示例组织，演示数据。</p></figcaption></figure>
<!-- English source image: touchless-po-matching-flow.png -->

### 流程图标题栏告诉您什么

| 字段 | 含义 |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Document type** | 规则集所属的文档类型，例如 INVOICE |
| **Rule set version** | 匹配规则的版本，例如 v3 |
| **Rule set owner** | **This organisation**（您自己的规则）或 **Shipped default rule set**（DocBits 的标准规则） |
| **Published** | 该版本的发布时间 |
| **Match quantity on** | 比较哪个数量（订购数量、未结数量） |
| **Tolerance amount** | 容差来自文档类型属性还是来自规则集 |
| **Unit price tolerance** / **Quantity tolerance** | 价格或数量允许的偏差幅度 |
| **Default tolerance** | 所有其他数值的容差 |

在上面的示例中，容差显示为 **not configured** 和 **not in force: attribute decides**。这意味着：规则集本身没有自己的容差，而 **Tolerance amount** 一行说明容差来自**文档类型属性**。容差只有生效时才起决定作用。当价格或数量差异阻塞文档时，请先读这一行：它会告诉您应**在哪里**更改容差。

规则集的状态以备注形式显示：**Active version**（由这些规则决定）、**Approved, not active**、**Draft, not yet in force** 或 **Version state unknown**。只有活动版本起决定作用。

如果转换规则在匹配前更改了文档，示意图会予以说明，例如 _2 applied: (names)_ 或 _"(rule)" rebuilt (table): the PO match was lost here_。这是常见的隐藏原因：一条重新格式化表格的规则可能破坏原本有效的匹配。

## 示例

以下示例中的数字仅用于说明。

### 示例 1：价格在容差范围内

一条发票行的单价为 **10.40**。采购订单行显示 **10.00**。单价容差为 **5 %**。

* **Exact match** 失败（10.40 不是 10.00）。
* **Tolerance-based match** 成功：差异为 **4 %**，在 5 % 以内。
* 该行匹配成功。**Match found.**

如果容差为 **3 %**，基于容差的匹配也会失败。所有阶段结束后，文档会以 **Unit price outside PO tolerance** 停止。示意图会准确显示这条路径，解决办法要么是调整容差（如果 4 % 对您的业务来说可以接受），要么是让供应商更正。

### 示例 2：供应商的项目编号与您的不一样

供应商开具的发票项目编号为 **"A-4711-X"**，您的采购订单显示 **"4711"**。没有规则比较这两者，因此找不到匹配，Touchless Intelligence 会把该供应商的所有发票归入同一个问题簇：**PO line match, PO item mismatch**，27 份文档。

* 在问题簇中您会读到 _27 affected, 27 recoverable_，预期提升例如 **+8.7 pp**。
* 解决办法在您这边：添加或调整一条按供应商项目编号或描述匹配的规则，或者在主数据中维护供应商项目编号。
* 更改规则后，用[变更提案](touchless-change-proposals.md)应用该更改，并在两周后读取 **Change history**：更改前后的 AP touchless 率。

### 示例 3：采购订单还不存在

发票在采购订单导入之前到达。它们以 **Purchase order not found** 停在 **PO Lookup**。问题簇会显示一个短暂的峰值。解决办法是您的流程顺序或采购订单导入的计划，而不是匹配规则。检查 **Where touchless is lost first**：每次导入间隔之后都变高的 _PO lookup: Purchase order not found_ 柱状条指向这个原因。

### 示例 4：一条规则重建了表格

某供应商表格的转换规则生效后，该供应商的匹配率急剧下降。受影响文档的示意图显示 _"(rule)" rebuilt (table): the PO match was lost here_。解决办法是调整或撤销该转换规则，而不是修改匹配规则。

## 处理采购订单匹配问题的常规步骤

1. 打开 **Where touchless is lost first**。采购订单匹配阶段是否排在前三位？
2. 打开 **Supplier opportunities** 并按 **Expected lift** 排序。选择根本原因为 **PO matching** 且状态为 **RECOVERABLE** 的供应商。
3. 打开 **Supplier Diagnosis** 并阅读问题簇：原因、受影响的文档、**What to change**、**Missing evidence**。
4. 打开 **How this organisation matches** 并检查规则集：版本、所有者和容差。
5. 打开一份**示例文档**及其[文档追踪](touchless-document-trace.md)：哪个阶段，哪个原因？
6. 用预览的方式只更改**一项**内容（规则顺序、容差、项目映射），以便 **Change history** 能够衡量它。

## 相关页面

* [Touchless Intelligence](./)
* [供应商诊断和问题簇](touchless-supplier-diagnosis.md)
* [文档追踪](touchless-document-trace.md)
* [变更提案和报告](touchless-change-proposals.md)
* [采购订单匹配规则](../../settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md)
* [采购订单匹配卡片：完整指南](../../workflow/cards-overview/po-matching-complete-guide.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->

<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
