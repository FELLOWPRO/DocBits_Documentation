# AI Table

使用 AI Table 检查提取的明细、修正列，并为供应商版式保存适用指令。请按任务选择下方指南。Structured Output 有独立配置指南，涵盖默认/是/否、覆盖、预览及完整示例。

* [设置与覆盖](configuration.md)
* [表格的 Structured Output](structured-output.md)
* [列与修正](columns-and-corrections.md)
* [AI 指令](ai-instructions.md)
* [AI 表格标签和指令](ai-table-tags.md)
* [提取说明与问题诊断](explain-extraction.md)
* [助手与权限](assistant-and-permissions.md)
* [视频](videos.md)

## 何时会显示 AI 表格

* 管理员已启用 **AI Table extraction**（设置 → 文档处理 → 分类和提取，参见[管理员设置](./#settings-for-admins)）。如果未启用，表格区域会显示 _AI Table will display here. Enable in …_。
* 检查可读文本或所选 Vision 输入。已保存的传统表格规则仍可能决定实际路径；请核对[实际使用的提取路径](../../../overview-and-basics/faq/document-processing/which-extraction-path-was-used.md)。
* 每列有独立的三态 Use AI 选择。还需检查实际来源和供应商规则；Structured Output 不会替换所有基于规则的表格。

读取表格的 AI 层级（Fast、Full、Nexus）按组织设置，也可以按供应商覆盖，参见[供应商专属 AI 模型](../validation-screen/supplier-specific-ai-model-for-field-and-table-extraction.md)。

## AI 表格概览

<figure><img src="../../../.gitbook/assets/ai-table-overview-en.png" alt="带有列标题和四行内容的 AI Extracted table"><figcaption><p>两个选项卡、AI Extracted table 及其列标题。</p></figcaption></figure>

* **选项卡。** _AI Extracted table_ 显示 AI 读取的内容。_Extracted table_ 是根据已训练规则生成的传统表格。文档包含 AI 表格时，默认打开 AI 选项卡。
* **列标题。** 每列都显示名称、一个小型**来源**符号（将鼠标悬停在其上，可查看 _AI · mapping_、_AI · synonym_ 等信息，了解 AI 如何匹配该列）、一个**三点**菜单，以及映射列对应的**名称按钮**，点击后可以更改列的对应关系。
* **行按钮。** 行首的 **x** 可以删除该行。右键单击某行，可选择 _Select as additional cost_ / _Remove as additional cost_。
* **页脚工具栏。** 屏幕底部的图标可以添加或隐藏列和行，参见[页脚工具栏](./#footer-toolbar)。
* 表格下方的 **AI instructions** 卡片：提示、额外列、**Test change**、**Apply**、**Save as training**、**Delete**、**Export**，参见[向 AI 提供指令](./#give-the-ai-instructions)。

{% hint style="info" %}
只有在你可以编辑文档时，列控件才可用。如果这些控件显示为灰色，说明文档为只读状态，或已在其他会话中锁定。如果红色横幅显示文档已由你自己的用户在其他会话中锁定，**Unlock** 会接管该锁定。
{% endhint %}


## 管理员设置 <a id="settings-for-admins"></a>

继续阅读: [设置与覆盖](configuration.md).

### 按列使用 AI <a id="use-ai-per-column"></a>

继续阅读: [表格的 Structured Output](structured-output.md).

<a id="选择正确的列重新映射"></a>
<a id="三点菜单"></a>
<a id="页脚工具栏-"></a>
<a id="footer-toolbar"></a>

## 更改列

继续阅读: [列与修正](columns-and-corrections.md).

<a id="使用-nexus-提供建议"></a>
<a id="测试应用和保存各按钮的功能"></a>

## 向 AI 提供指令 <a id="give-the-ai-instructions"></a>

继续阅读: [AI 指令](ai-instructions.md).


## 查看 AI 的处理结果

继续阅读: [提取说明与问题诊断](explain-extraction.md).


## 实际示例

继续阅读: [提取说明与问题诊断](explain-extraction.md).

<a id="向管理员提出规则建议"></a>

## Assistant 与 AI 表格

继续阅读: [助手与权限](assistant-and-permissions.md).


## 谁可以执行哪些操作 <a id="who-can-do-what"></a>

继续阅读: [助手与权限](assistant-and-permissions.md).

<a id="1-阅读-ai-表格"></a>
<a id="2-修正列并教会-docbits"></a>
<a id="3-三种常见问题"></a>
<a id="4-折扣税费和数量为零的行"></a>
<a id="5-ai-已能正确读取的内容"></a>
<a id="6-assistant-以及谁可以更改什么"></a>

## 视频系列

继续阅读: [视频](videos.md).

## 相关页面

* [AI 表格标签和指令](ai-table-tags.md)
* [训练行字段 / 表格训练](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/)
* [供应商专属 AI 模型](../validation-screen/supplier-specific-ai-model-for-field-and-table-extraction.md)
* [使用了哪种提取路径？](../../../overview-and-basics/faq/document-processing/which-extraction-path-was-used.md)
* [Touchless Intelligence](../../../administration-and-setup/analytics-dashboard/touchless-intelligence/)
