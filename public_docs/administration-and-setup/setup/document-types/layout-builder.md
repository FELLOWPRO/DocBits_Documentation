# 布局构建器

使用布局构建器来排列用户在验证或审批文档时看到的字段和控件。每个布局都属于一个文档类型、一个来源和一个布局类型，因此保存前请先在页面顶部确认这三项。

{% embed url="https://youtu.be/-m45XGiIeig" %}
DocBits Layout Builder Tutorial: Create Custom Document Layouts for Faster, Cleaner Validation
{% endembed %}

## 打开布局

1. 打开 **Settings → Document Types**。
2. 选择要编辑的文档类型并打开 **Layout Builder**。对于文档子类型，请打开该子类型的 Layout Builder 操作。
3. 检查页眉。左侧选择器是 **origin**（例如 **Default**），其后依次是 **Document Type**（例如 **Invoice**）和 **Layout type**（例如 **Field Validation**）。每个选择器都会打开一个列表；选择其他条目即可加载该布局。如果无法使用 Layout Builder，可能需要管理员为您的组织启用该模块。

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/layout-builder-overview.png" alt="DocBits 中一张发票的 Layout Builder，包含 origin、文档类型和布局类型选择器，Structure、Fields 和 Elements 选项卡，布局区域以及右侧的 Properties 面板"><figcaption><p>Layout Builder：页眉中的选择器、左侧的元素列表、中间的布局区域以及右侧的 Properties 面板。</p></figcaption></figure>

## 使用页眉

* **Document Type** 和 **Layout type** 用于切换布局。页面会重新加载您选择的布局。
* 在 **Save** 旁边，DocBits 显示该布局是否有**未保存的更改**。保存后，它会显示布局上次保存的时间。
* **Save** 保存所选文档类型、来源和布局类型的布局。
* **More** 菜单（三个点）包含 **Auto Generate template**、**Apply Default layout to Origins**、**Use default template**、**Edit JSON**、**Copy JSON** 和 **Layout settings**。**Auto Generate template** 和 **Use default template** 会替换自定义布局，因此请先确认所选的文档类型和布局。**Edit JSON** 用于高级配置，仅在您了解模板格式时才应使用。
* 如果在存在未保存更改的情况下离开页面，DocBits 会询问是保存还是放弃这些更改。

## 认识编辑器的各个区域

左侧有三个选项卡：

| 选项卡 | 用途 |
| --- | --- |
| **Structure** | 以树状结构查看布局。分组及其字段按其在布局区域中出现的顺序列出，并显示已放置和可用的字段数量。 |
| **Fields** | 为该文档类型配置的所有字段，按字段组分组并默认折叠。筛选器可在 **All**、**Unused** 和 **Hidden** 字段之间切换，字段标签下方显示技术字段名称。 |
| **Elements** | 呈现和交互控件，例如 Text、Label、Check Box、分隔符、表格、按钮和子分组。 |

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/layout-builder-structure.png" alt="Layout Builder 的 Structure 选项卡，显示展开为字段的分组 Invoice details、Payment details、Purchase Order 和 Delivery Details"><figcaption><p>Structure 选项卡以分组和字段的树状结构显示已构建的布局。</p></figcaption></figure>

选择一个条目即可添加，或将其拖入布局区域。分组标题告诉验证文档的人员该部分应包含什么内容。请先在 [Document Types](README.md) 中创建或重命名可复用的文档字段。

## 在布局区域中操作

* **Main layout** 显示文档本身的布局。**Table** 显示用于行项目的表格布局。
* **Document** 打开或关闭布局区域旁的示例文档，以便将布局与真实文档对照。
* 分组绘制为卡片；分组内的字段可以排列成行，并设置不同的宽度。

## 更改元素特性

在布局区域选择一个元素或分组。右侧的 **Properties** 始终可见，并按区块组织：

* **Display** – 标签、字段名称、标签位置和元素宽度。
* **Behaviour** – 只读、隐藏和 Tab 键顺序。
* **Values & lists** – 为该元素提供的值。
* **Automation** – 填充或更改该元素的规则。
* **Borders & spacing** – 元素的外观。

宽度请选择预设值（25、33、50、66、75 或 100 百分比），而不要手动输入数值；然后在布局区域检查效果。显示哪些区块和选项取决于所选元素。更多详情请参阅[配置字段属性](../../settings/global-settings/document-types/layout-manager/configuring-field-properties.md)。

## 翻译按钮标签

**Save Rules**、**Auto Accounting**、**PO Match**、**Export**、**Export Without Validation** 和 **Reject** 等按钮的标签由一个翻译键解析得出。查看器会以打开该布局的用户所用语言显示标签。如果该键没有对应语言的文本，DocBits 会显示布局中保存的标签。

* 独立按钮在 **Properties** 中有一个 **Translation Key** 字段。
* **Invoice Buttons** 将多个按钮归为一组。可为单个子按钮设置键，或在分组面板的列表中为每个子按钮分别设置一个键。

在此更改之前构建的布局会保留其标签：DocBits 会为它们填入每种按钮类型的默认键。保存了键的布局会保留该键，重新加载后也是如此。

## Save and go back to Dashboard

类型为 **Save and go back to Dashboard** 的按钮会像 **Save** 一样存储文档值，然后打开 Dashboard。该类型适用于审核人员依次处理文档队列的布局。

* 在布局区域添加一个按钮元素，并在其 **Properties** 中选择该类型。
* 如果保存失败，按钮会停留在验证界面，不会打开 Dashboard，因此可以先修正该问题。
* 标签的解析方式与其他任何按钮的标签相同；参见上文的*翻译按钮标签*。

## 检查并保存

排列好分组和字段，在布局区域检查布局，结果正确后使用页眉中的 **Save**。有关特定来源的布局，请参阅[来源布局](origin-layouts.md)。

{% hint style="info" %}
截图显示的是 DocBits 测试组织中的合成设置，应用界面语言为英文。采集截图期间没有保存或替换任何布局。
{% endhint %}
