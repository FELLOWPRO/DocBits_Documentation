# 自定义验证规则

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/custom-validation-rules/v1/en.mp4" %}

## 概述

自定义校验规则允许管理员针对 DocBits 从文档中提取的数据定义**自己的检查**——无需编写脚本，也无需等待产品变更。

一条规则回答三个问题：

1. **在哪里**显示问题？在表头字段上，还是在表格行的某个单元格上。
2. **何时**应用该规则？始终应用，还是仅对满足某个条件的文档（或行）应用——参见 [Rule Conditions (Applies when)](rule-conditions-applies-when.md)。
3. **必须满足什么**？字段必须已填写、符合某种格式、处于某个范围、匹配某个列表、与另一字段比较结果正确，或能够加总相符。

当检查失败时，DocBits 会在 **validation screen** 上标记该字段或单元格，并显示您的消息——与内置检查完全一样。严重级别为 **Error** 时，在问题修复之前文档无法校验；为 **Warning** 时，文档同样会被拦截，但用户可以通过在字段上确认该消息来消除警告，而无需更改值——参见 [Acknowledge a warning on the validation screen](custom-validation-rules.md#acknowledge-a-warning-on-the-validation-screen)。

规则按**文档类型**定义，并作用于该类型的每个文档：在处理过程中以及每次保存文档时运行。

### 它们解决的问题

| 业务需求                                                     | 不使用自定义规则时                     | 使用自定义规则时                                                                                  |
| ------------------------------------------------------------ | -------------------------------------- | ------------------------------------------------------------------------------------------------- |
| 金额超过 250 EUR 的德国发票必须显示供应商的税号              | 需要写脚本，或者靠用户自己记住         | 在 Supplier Tax ID 上设置 **Required**，_applies when_ origin 为 DE 且总金额大于 250              |
| 某供应商的发票号码始终形如 `INV-123456`                      | 输入错误会进入 ERP                     | 针对该供应商，在 Invoice Number 上设置 **Pattern** `^INV-\d{6}$`                                   |
| 每个物料行都需要大于零的数量                                 | 数量为 0 的行也会被导出                | 在 Quantity 列上设置 **Range**（最小值 0.01）                                                      |
| 到期日不得早于发票日期                                       | 付款运行出错                           | **Compare fields**：Due Date 晚于或等于 Invoice Date                                               |
| 各行金额加总必须等于净额                                     | 只有固定的内置检查                     | **Formula** `sum(row.NET_AMOUNT) == header.total_net_amount`，并使用您自己的容差                    |
| 只允许使用您的 ERP 已知的货币                                | ERP 中出现导出错误                     | 在 Currency 上设置 **List of Values**                                                             |
| 标记异常值但不强制更正                                       | 需要写脚本，或者靠用户自己记住         | 任何严重级别为 **Warning** 的规则——用户通过 **Acknowledge** 确认该值                               |

## 启用自定义校验规则

自定义校验规则按**文档类型**开启，没有组织级别的总开关。

1. 依次进入 **Settings → Document Processing → Document Types**。
2. 在文档类型的卡片上，点击 **settings**（齿轮）图标。
3. 打开 **Custom Validation Rules** 区域并打开开关。
4. 点击 **Manage validation rules** 打开规则列表。

<figure><img src="../../../../.gitbook/assets/doc-type-settings-rule-toggles.png" alt="The rule toggles in the additional settings of a document type"><figcaption><p>Manage Layouts、Custom Validation Rules 与 Transformation Rules 的开关</p></figcaption></figure>

从现在起，文档类型的卡片上还会显示 **Validation Rules** 链接，以及用于执行日志的 **Logs** 链接。

<figure><img src="../../../../.gitbook/assets/doc-types-rules-links.png" alt="The document type card with the Validation Rules link"><figcaption><p>文档类型卡片上的链接</p></figcaption></figure>

{% hint style="warning" %}
**该开关会取代内置的金额检查。** 当某个文档类型启用了自定义校验规则时，硬编码的检查“总金额 = 净额 + 税额”以及行金额 / 折扣检查**不会**为该文档类型运行；由可配置的规则取代它们。在开启之前，请将您依赖的检查重建为规则（参见 [recipes](custom-validation-rules.md#recipes)）。关闭该开关会恢复内置检查。所有其他字段校验（必填字段、格式、主数据）仍会继续运行。
{% endhint %}

## 规则列表

**Document Types →（文档类型）→ Validation Rules** 会列出该文档类型的所有规则。

<figure><img src="../../../../.gitbook/assets/s150-validation-rules-list.png" alt="Custom validation rule management with configuration names hidden."><figcaption><p>隐藏了配置名称的自定义校验规则管理界面。</p></figcaption></figure>

每张卡片显示规则的名称和描述，以及**级别**（Header / Line / Table）、**严重级别**（Error / Warning）、错误所附加的**字段**及其**来源**的标记。使用右侧的开关启用或停用规则，使用 **⋮** 菜单编辑、复制或删除规则。可以按级别（**All / Header / Line / Table**）和状态（**All / Active / Inactive**）筛选列表，或对列表进行搜索。

### System default、Customized 与 Custom 规则

| 来源               | 是什么                                                               | 您可以做什么                                                                                                                                                                                                       |
| ------------------ | -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **System default** | DocBits 为所有组织随附的规则。                                       | 无法直接编辑——构建器会显示“This is a system default rule and cannot be edited.”。点击 **Customize** 创建您自己的可编辑副本，或将其关闭以在您的组织中停用该规则。                                                   |
| **Customized**     | 您的组织更改过或关闭过的系统默认规则。                               | 可以像自己的规则一样编辑。**Reset to Default** 会删除您的副本并恢复原始规则。                                                                                                                                      |
| **Custom**         | 您的组织创建的规则。                                                 | 编辑、**Duplicate**、**Delete**。                                                                                                                                                                                  |

对系统默认规则的更改绝不会影响其他组织。

## 创建规则

点击 **New rule**。构建器包含三个步骤。**Test rule** 和 **Save** 位于右上角。

### 步骤 1 — 名称与范围

<figure><img src="../../../../.gitbook/assets/validation-rule-step1.png" alt="Step 1 of the validation rule builder for a header field rule"><figcaption><p>表头字段规则的第 1 步</p></figcaption></figure>

| 设置                               | 作用                                                                                                                                                                             |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Rule level**                     | 规则检查的对象以及错误的显示位置——参见 [Rule levels](custom-validation-rules.md#rule-levels)。                                                                                    |
| **Severity**                       | **Error** 会将字段标记为无效，并在值更正之前阻止校验。**Warning** 同样会拦截文档，但用户可以在 validation screen 上通过 **Acknowledge** 消除该警告而无需更改值。                  |
| **Rule Name**                      | 显示在列表中、日志中，以及呈现给管理员。请让名称描述规则本身（“Supplier tax ID required for German invoices”）。                                                                  |
| **Rule key**                       | 根据名称生成的技术键。之后重命名规则时该键保持不变。首次保存前点击铅笔图标可自行选择键；保存之后即固定。                                                                          |
| **Description**                    | 供其他管理员参考的可选说明。                                                                                                                                                      |
| **Table name**                     | _仅用于表格行。_ 被检查行的表格，例如 `INVOICE_TABLE`。                                                                                                                           |
| **Attach error to field / column** | 在 validation screen 上显示错误的字段（对于表格行则是列）。                                                                                                                       |
| **Log execution**                  | 每次评估写入一条日志记录，包括规则应用或未应用的原因。参见 [Logs](custom-validation-rules.md#logs)。                                                                              |

#### 规则级别

| 级别             | 运行方式                                        | 错误显示在                  | 可读取                                                                            | 典型规则                                              |
| ---------------- | ----------------------------------------------- | --------------------------- | -------------------------------------------------------------------------------- | ---------------------------------------------------- |
| **Header field** | 每个文档运行一次                                | 一个表头字段                | `header.*`, `doc.*`                                                              | “Supplier tax ID is required for German invoices”      |
| **Table line**   | 所选表格的每一行运行一次                        | 失败行的单元格              | `row.*`（当前行）, `header.*`, `doc.*`                                            | “Quantity must be greater than zero”                   |
| **Whole table**  | 每个文档运行一次，同时查看所有行                | 一个表头字段                | 跨行的汇总（`sum()`, `count()`, `min()`, `max()`）, `header.*`, `doc.*`            | “The line net amounts must add up to the net amount”   |

<figure><img src="../../../../.gitbook/assets/validation-rule-line-step1.png" alt="Step 1 for a table line rule"><figcaption><p>表格行规则：被检查的表格以及显示错误的列</p></figcaption></figure>

### 步骤 2 — Applies when

决定规则是对每个文档运行，还是仅对部分文档运行。留空则检查每个文档。否则添加条件行——例如“Document Origin is Deutsch”和“Total Amount greater than 250”——并用 **All** / **ANY** 以及嵌套分组将它们组合起来。

<figure><img src="../../../../.gitbook/assets/applies-when-nested-example.png" alt="An Applies when condition"><figcaption><p>该检查仅对金额高于 250 且货币为 EUR 或无货币的德国文档运行</p></figcaption></figure>

对于表格行规则，条件还可以使用当前行的列，并且会**逐行**评估：不匹配的行不会被检查。

<figure><img src="../../../../.gitbook/assets/applies-when-row-condition.png" alt="A row condition"><figcaption><p>仅检查物料行（带物料编号的行）</p></figcaption></figure>

条件的详细说明——每个字段、运算符和比较规则，以及大量示例——见 [Rule Conditions (Applies when)](rule-conditions-applies-when.md)。

### 步骤 3 — 检查：必须满足什么

选择一项检查。卡片下方的设置会随您所选的检查而变化。

<figure><img src="../../../../.gitbook/assets/validation-rule-step3-required.png" alt="Step 3 with the Required check selected"><figcaption><p>七种检查。Required 无需进一步设置</p></figcaption></figure>

#### Required — 字段必须有值

当字段为空（缺失或仅含空格）时失败。无需进一步设置。

与 **Applies when** 一起使用，即可使字段成为**有条件**必填。必须始终填写的字段，最好在字段设置中配置为必填字段。

> _Supplier Tax ID is required_ — 当 _Document Origin is Deutsch_ 且 _Total Amount greater than 250_ 时适用。

#### Formula — 金额必须加总相符

一种算术比较。表达式包含**一个**比较运算符（`==`、`!=`、`>`、`>=`、`<`、`<=`）；两侧都可以使用 `+ - * /`、数字、括号和字段引用。

<figure><img src="../../../../.gitbook/assets/validation-rule-formula.png" alt="A Formula check"><figcaption><p>带容差和消息占位符的整表公式</p></figcaption></figure>

* 点击表达式下方的标签可插入函数和字段前缀：`sum()`、`count()`、`min()`、`max()`、`default()`、`coalesce()`、`header.`、`doc.`。输入字段名时，会打开匹配字段的列表。
* `sum(row.NET_AMOUNT)`、`count(row.ITEM_NUMBER)`、`min(...)`、`max(...)` 作用于所有行，仅在 **Whole table** 级别可用。`count()` 统计该列已填写的行数。
* `default(header.discount, 0)` 在字段为空时使用 `0`；`coalesce(header.a, header.b, 0)` 使用第一个已填写的值。
* **Tolerance**：对于 `==` 和 `!=`，差额不超过该金额即视为相等。可使用 `0.01` 或 `0.05` 来吸收舍入误差。它对 `<`、`>`、`<=` 和 `>=` 无效。
* 为空或无法读取的金额按 `0` 计算。除以零时会跳过该规则，而不是引发错误。
* 在错误消息中，`{actual}` 会被替换为左侧的结果，`{expected}` 会被替换为右侧的结果。

示例：

| 用途                                       | 级别         | 表达式                                                                     | 容差      |
| ------------------------------------------ | ------------ | -------------------------------------------------------------------------- | --------- |
| 表头合计一致                               | Header field | `header.total_amount == header.total_net_amount + header.total_tax_amount` | 0.01      |
| 各行加总等于净额                           | Whole table  | `sum(row.NET_AMOUNT) == header.total_net_amount`                           | 0.05      |
| 行金额 = 数量 × 单价                       | Table line   | `row.NET_AMOUNT == row.QUANTITY * row.UNIT_PRICE`                          | 0.01      |
| 税额不高于净额的 19 %                      | Header field | `header.total_tax_amount <= header.total_net_amount * 0.19`                | –         |
| 至少一行                                   | Whole table  | `count(row.ITEM_NUMBER) >= 1`                                              | 0         |

#### Pattern — 匹配格式 / 正则表达式

值必须匹配**正则表达式**。该表达式是在值中进行搜索，因此当整个值都必须匹配时，请用 `^`（开头）和 `$`（结尾）将其锚定。如果大小写无关紧要，请勾选 **Case-insensitive match**。

| 格式                                               | 正则表达式                       |
| -------------------------------------------------- | -------------------------------- |
| `INV-` 后跟六位数字                                | `^INV-\d{6}$`                    |
| 德国增值税号                                       | `^DE\d{9}$`                      |
| 以 45 开头且长度为 10 位的采购订单                 | `^45\d{8}$`                      |
| 仅数字                                             | `^\d+$`                          |
| IBAN（粗略检查）                                   | `^[A-Z]{2}\d{2}[A-Z0-9]{11,30}$` |

#### Range — 介于最小值和最大值之间

值必须是介于 **Minimum** 和 **Maximum** 之间的数字（两者均包含）。可填写其中一项或两项。不是数字的值会失败。诸如 `1.234,56` 这样的格式化金额可以被识别。

边界值本身以普通数字输入：可选的正负号和数字，允许使用逗号作为小数分隔符（`0,5`）。千位分隔符、指数和文字在保存时会被拒绝，并提示该边界不是数字。请至少填写一个边界，因为既没有最小值也没有最大值的范围不会被保存，并且请保持最小值小于或等于最大值。

<figure><img src="../../../../.gitbook/assets/validation-rule-line-range.png" alt="A Range check"><figcaption><p>仅设置最小值的范围：数量必须至少为 0.01</p></figcaption></figure>

#### Compare fields — 例如到期日 ≥ 发票日期

使用_等于_、_不等于_、_大于_、_小于_、_等于或晚于（≥）_或_等于或早于（≤）_将一个字段的值与另一字段、**today** 或固定值进行比较。数字按数字比较，日期按日期比较。

* Due Date **on or after (≥)** Invoice Date
* Invoice Date **on or before (≤)** today——不允许日期在未来的发票
* Discount **less than** 100

#### Allowed values — 来自固定列表

值必须是您输入的其中一个值，**每行一个值**。可选不区分大小写。适用于简短、稳定的列表（`EUR`、`CHF`、`USD`）。

#### List of Values — 来自命名的 LOV

与 _Allowed values_ 类似，但值来自在 **Settings › List of Values** 下管理的共享 **List of Values**。选择该列表，而不是重新输入；当列表发生变化时，规则会使用新的值（经过短暂的缓存延迟后）。只有列表条目的值有效，标签不算。

{% hint style="info" %}
除 **Required** 外，每项检查在**值为空时都会通过**。对 Purchase Order 的 Pattern 规则不会对没有采购订单的发票报错。如果空值也是问题，请添加一条 Required 规则，或用 _Applies when … is not empty_ 限制该规则。
{% endhint %}

#### 错误消息与错误代码

* **Error message shown to the processing user** — validation screen 上的文本。请说明**问题所在**以及**该怎么做**：“Supplier tax ID is missing. German invoices over 250 EUR must show it.”
* **Error code** — 简短的技术代码，例如 `REQUIRED_CONDITIONAL`、`FORMAT_MISMATCH`、`OUT_OF_RANGE`、`DATE_ORDER`、`LINES_HEADER_MISMATCH`、`VALUE_NOT_ALLOWED`。它会出现在导出和日志中，便于您对错误进行分组。

#### 保存时跳过字段的情况

校验规则需要文档页面上的位置。如果字段带有值但在页面上没有位置，就无法为其附加任何规则——此时保存不会只报告成功：DocBits 会列出每个被跳过的字段，并说明该规则未能为其保存。

请在模板或映射中为该字段指定位置，然后再次保存规则。

## 测试规则

点击 **Test rule** 可针对某个文档运行当前版本的规则——无论是否已保存。输入 **Document ID**，或切换到 **By Document JSON** 并粘贴已提取的数据。**不会保存任何内容**，文档也不会被更改。

结果有以下三种之一：

| 结果                                 | 含义                                                                                                                 |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| **Rule failed — error raised**       | 条件匹配且检查失败。消息的显示方式与用户看到的完全一致。                                                             |
| **Rule passed**                      | 条件匹配且检查通过。表格行规则会显示每一行的结果（“4 of 4 checked rows passed”）。                                    |
| **Rule skipped — scope not matched** | 该文档的 _Applies when_ 条件为假，因此未进行任何检查，也未引发任何错误。                                              |

<figure><img src="../../../../.gitbook/assets/validation-rule-test-result.png" alt="Test rule: rule failed"><figcaption><p>该德国发票没有供应商税号：规则以所配置的消息失败</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/validation-rule-test-skipped.png" alt="Test rule: rule skipped"><figcaption><p>同一规则将阈值提高到 1000：该发票（469.18）不在范围内，因此规则被跳过</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/validation-rule-line-test.png" alt="Test rule: per-row results"><figcaption><p>表格行规则会报告每一个被检查的行</p></figcaption></figure>

请至少在一个应当失败的文档、一个应当通过的文档和一个应当被跳过的文档上测试每条新规则。

## 规则的运行时机

* **在处理过程中**，与其他校验一起，在提取和转换规则之后运行。
* 在 validation screen 上**每次保存**文档时运行。
* **规则更改之后**，现有文档**不会**一次性全部重新检查。每个文档会在下次保存或重新处理时用新规则重新检查。已经导出的文档不受影响。
* 规则按优先级顺序运行（然后按 key）。一个字段只显示**一条**错误：如果两条规则在同一字段上失败，则以第一条为准；后续规则不会覆盖它。
* 警告会被单独收集，绝不会遮盖错误：同时违反硬性规则的字段只显示该错误，此时也没有需要确认的内容。
* 如果规则无法评估——例如公式中出现除以零——则会被跳过。有缺陷的规则绝不会错误地将文档标记为无效。

## 在 validation screen 上确认警告

严重级别为 **Warning** 的失败规则会像错误一样拦截文档：在字段被确认之前，文档无法校验。区别在于用户需要做什么。

在 validation screen 上，规则的消息会显示在字段下方，并带有一个 **Acknowledge** 按钮。单击一次即可确认该字段上的所有警告，而不更改其值。随后消息会被替换为提示 **Acknowledged. Changing the value asks again.**。

该确认只对确认时所依据的值有效。如果用户修改了该值、重新提取了该值，或该字段以不同结果被重新检查，警告会再次出现，必须重新确认。显示硬性错误的字段无法确认——请在那里更正该值。

在只读文档上不会显示该按钮，因此那里的警告必须由能够编辑该字段的人员解决。

**Acknowledge** 按钮仅对表头字段提供。

## Logs

在规则中开启 **Log execution** 可记录每次评估。打开 **Document Types →（文档类型）→ Logs**。页面在卡片标题中显示文档类型和条目数量；刷新按钮会重新加载列表。

使用 **Find by** 选择搜索方式——**Rule key**、**Rule ID** 或 **Document**——并在 **Selector** 中输入相应的值。按文档搜索时，**Rule Type** 为必填。使用 **Outcome**、**Executed** 以及 **From date** / **To date** 范围缩小结果。

<figure><img src="../../../../.gitbook/assets/core6847-rule-execution-logs-en.png" alt="The rule execution logs"><figcaption><p>Rule Execution Logs 页面：上方是筛选条件，下方每次评估一行。在您搜索之前，表格会提示您应输入什么。</p></figcaption></figure>

打开一个条目可查看其详细信息，包括**条件跟踪**：_Applies when_ 的每一行及其期望值、文档的实际值以及是否通过。参见 [Read the condition trace](rule-conditions-applies-when.md#read-the-condition-trace-in-the-logs)。

同一页面也会显示转换规则和布局选择规则的日志。

## 配方

可将这些规则作为起点复制使用。字段和列键来自标准 **Invoice** 文档类型；请根据您的文档类型进行调整。

**1. 金额超过 250 EUR 的德国发票需要供应商税号** Header field · Error · 附加到 _Supplier Tax ID_ · Applies when **All**：_Document Origin_ 为 _Deutsch_，_Total Amount_ 大于 _250_ · 检查 **Required** · 消息 “Supplier tax ID is missing. German invoices over 250 EUR must show it.” · 代码 `REQUIRED_CONDITIONAL`。

**2. 表头合计相符**（取代内置检查）Header field · Error · 附加到 _Total Amount_ · 始终 · **Formula** `header.total_amount == header.total_net_amount + header.total_tax_amount`，容差 `0.01` · 消息 “Total {actual} does not equal net plus tax ({expected}).”

**3. 各行加总等于净额**（取代内置检查）Whole table · Error · 附加到 _Total Net Amount_ · 始终 · **Formula** `sum(row.NET_AMOUNT) == header.total_net_amount`，容差 `0.05` · 消息 “Line net amounts add up to {actual}, but the invoice net amount is {expected}.” · 代码 `LINES_HEADER_MISMATCH`。

**4. 物料行的数量必须为正** Table line · Error · 表格 `INVOICE_TABLE`，列 `QUANTITY` · Applies when _row.ITEM\_NUMBER_ 不为空 · **Range** 最小值 `0.01` · 代码 `OUT_OF_RANGE`。

**5. 行金额 = 数量 × 单价** Table line · Warning · 列 `NET_AMOUNT` · 始终 · **Formula** `row.NET_AMOUNT == row.QUANTITY * row.UNIT_PRICE`，容差 `0.01`。

**6. 某个供应商的发票号码格式** Header field · Error · _Invoice Number_ · Applies when _Supplier ID_ 为 _20723_ · **Pattern** `^INV-\d{6}$`。

**7. 到期日不早于发票日期** Header field · Error · _Due Date_ · 始终 · **Compare fields** Due Date _on or after (≥)_ Invoice Date · 代码 `DATE_ORDER`。

**8. 不允许日期在未来的发票** Header field · Error · _Invoice Date_ · 始终 · **Compare fields** Invoice Date _on or before (≤)_ today。

**9. 仅允许已批准的货币（确认而非更正）** Header field · **Warning** · _Currency_ · 始终 · **List of Values** _approved\_currencies_ · 代码 `VALUE_NOT_ALLOWED`。用户必须先确认该警告，文档才能被校验。

**10. 金额超过 5,000 时必须填写采购订单** Header field · Error · _Purchase Order_ · Applies when _Total Amount_ 大于 _5000_ · **Required**。

## 最佳实践

* **先以警告形式开始。** 新规则先以 **Warning** 严重级别保存，观察几天（Test rule、日志），然后再切换为 **Error**。这样用户不会被强制更正该值，但在确认每一次命中之前都会被拦截。
* **一条规则，一条消息。** 几条带有清晰消息的小规则比一条大公式更容易理解。
* **用 Applies when 取代副本。** 一条带条件的规则胜过为五个供应商分别复制五份。
* **对金额要宽容。** 请始终为金额公式设置容差。
* **按业务规则命名规则**，而不是按技术手段命名（“Due date not before invoice date”，而不是“Compare rule 3”）。
* 规则运行正常后**关闭 Log execution**；它会在每次保存时写入一条记录。

## 故障排除

| 现象                                       | 需要检查的内容                                                                                                                                      |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| 规则始终不报错                             | 该文档类型是否启用了此功能，规则是否为 **Active**？对该文档运行 **Test rule**：“skipped”表示 _Applies when_ 为假。                                 |
| 空字段未被报告                             | 只有 **Required** 会报告空值。请添加一条 Required 规则。                                                                                            |
| 内置的合计检查消失了                       | 在启用自定义规则期间这是预期行为。请将它们重建为 Formula 规则（配方 2 和 3）。                                                                     |
| 更改后的规则对文档没有影响                 | 文档会在下次保存时重新检查。请保存或重新处理该文档。                                                                                                |
| Pattern 匹配了不应匹配的值                 | 模式会在值内部搜索。请用 `^` 和 `$` 锚定。                                                                                                          |
| 字段上只显示两条错误中的一条               | 一个字段只显示第一条失败的规则。请调整优先级，或将其中一条规则附加到另一字段。                                                                       |
| _Applies when_ 中缺少表格列                | 它们仅在 **Table line** 级别可用。                                                                                                                  |
| 无法更改系统默认规则                       | 点击 **Customize** 创建您自己的副本。                                                                                                               |

## 相关内容

* [Rule Conditions (Applies when)](rule-conditions-applies-when.md) — 深入了解条件
* [Transformation Rules](transformation-rules/) — 在校验之前更正这些值
* [Layout Selection Rules](layout-manager/layout-selection-rules.md) — 选择文档所使用的布局
* [Setting Validation and Match Score](fields/setting-validation-and-match-score.md) — 每个字段的校验设置
