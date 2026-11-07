# 表格列

表格列定义文档类型的行项目表包含哪些列：DocBits 会向每列提取什么内容、用户在验证屏幕上看到什么内容，以及导出时发送到 ERP 的内容。

**位置：**Settings → Document Processing → Document Types → Table Columns

<figure><img src="../../../../../.gitbook/assets/structured-output-column-choice-zh-20261104.png" alt="当前 Use AI 下拉菜单，包含默认、是和否。未更改任何选项。标题单元格已隐藏以保护数据。"><figcaption><p>当前 Use AI 下拉菜单，包含默认、是和否。未更改任何选项。标题单元格已隐藏以保护数据。</p></figcaption></figure>

## 您会看到什么

每一行对应一个表格中的一列。列表显示：

| 列 | 含义 |
|---|---|
| **列名称** | 技术名称，根据标题生成（大写字母，单词之间用下划线分隔）。用于脚本、导出映射和 API。之后无法更改。 |
| **标题** | 在验证屏幕上显示的标签。可通过 *操作* 列中的翻译图标（*更新翻译键*）进行更改。 |
| **列类型** | `AMOUNT`、`STRING`、`DATE`、`NUMBER`、`BOOLEAN` 或 `CURRENCY`。决定验证和格式设置方式。 |
| **表格名称** | 此列所属的表格，例如 `INVOICE_TABLE`。 |
| **Required** | 只要任意行中的此列为空，文档就无法获批。 |
| **Read Only** | 用户可以看到该值，但无法编辑。 |
| **隐藏** | 此列既不显示，也不会导出。可用于关闭不需要的默认列。 |
| **Use AI** | 三态 AI 选择：默认继承文档类型的 AI 选择，是明确请求该列，否将其排除出基础架构。此设置独立于必填、只读和隐藏。 |
| **操作** | 翻译图标：重命名标题。信息图标：显示标签的来源（您的翻译、默认值或键）。三点菜单：*Delete*，仅适用于贵组织创建的列；默认列只能隐藏。 |

列表上方有两个按钮：

* **创建新表格**：为文档类型添加第二个行项目表（例如，在项目表旁添加费用表）。
* **添加新表格列**：打开 [添加新列](adding-a-new-column.md) 中所述的对话框。

## 默认列和自定义列

每种文档类型都自带一组默认列（发票包括：项目编号、描述、数量、单价、总金额、税额等）。这些列属于 DocBits，而非贵组织，因此无法删除；您可以将其隐藏。自行添加的列属于贵组织，可以删除。

{% hint style="info" %}
**更改仅适用于新文档。** 添加、隐藏或删除的列会应用于更改后上传或重新启动的文档。仪表板上已有的文档会保留提取时的表格。重新启动文档以应用新配置。
{% endhint %}

## 相关页面

* [用途和使用方式](purpose-and-use.md)：表格列会显示在哪里
* [添加新列](adding-a-new-column.md)
* [编辑和删除列](editing-and-deleting-columns.md)
* [最佳实践](best-practices-2.md)
* [故障排除](troubleshooting-1.md)
* [训练行字段 / 表格训练](../../../../setup/document-training/training-line-fields-table-training/README.md)：教 DocBits 识别供应商的表格位置
* [AI 表格](../../../../../end-user-and-partner-section/end-user-section/ai-table/README.md)：用户在验证屏幕上看到的内容

## Use AI：默认、是或否

打开正确文档类型及表格的[表格列](README.md)。**利用人工智能 (Use AI)** 是三态下拉选择，不是复选框；更改后立即保存。

| 当前菜单选项 | 对基础架构的影响 |
| --- | --- |
| **Default · 已请求** 或 **默认值 · 未请求** | 采用 DocBits 对该文档类型和列名的默认 AI 选择。“默认”不等于始终开启，也不等于始终关闭。 |
| **是的，已请求** | 明确要求 AI 返回该配置列。 |
| **No · 未请求** | 从基础架构中排除此列，即使它通常属于默认 AI 请求。 |

恢复“默认”会移除明确的是/否选择。新建自定义列通常不属于默认 AI 列集合；若需要 AI 返回，应选择“是”。默认 AI 列不等于所有系统自带列，请以显示的实际效果和预览为准。

**Required**、**Read Only**和**隐藏**分别控制完整性检查、可编辑性和可见性，不替代 AI 选择。“否”不会删除列或清除已有值，也不阻止规则、脚本或其他来源填充值。供应商训练和额外 AI 标签可能扩展实际请求，相关矛盾也需要处理。Structured Output 开关不会自动替换纯规则提取结果。

[表格的 Structured Output](../../../../../end-user-and-partner-section/end-user-section/ai-table/structured-output.md).
