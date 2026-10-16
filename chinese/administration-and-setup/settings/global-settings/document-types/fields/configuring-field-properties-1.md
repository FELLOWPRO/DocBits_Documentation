# 配置字段属性

使用 **设置 → 文档类型 → 字段** 控制某个文档类型的字段行为。请先选择文档类型；下方示例显示的是英文界面中的 **Invoice**。

<figure><img src="../../../../../.gitbook/assets/dbdc155-field-properties-overview-en.png" alt="英文 Invoice 字段设置，包含识别阈值、搜索、字段属性列和 Save Settings"><figcaption>DocBits 沙盒组织中的 Invoice 字段设置。</figcaption></figure>

## 查找字段并更改其属性

1. 在 **Search by Name** 中输入字段名称或标签。此操作会筛选列表，不会更改字段。
2. 找到字段所在行。例如，**Invoice number** 的技术名称为 `invoice_id`。
3. 调整该行中的控件，然后选择 **Save Settings**。表格上方和下方均提供相同的保存按钮。

<figure><img src="../../../../../.gitbook/assets/dbdc155-field-properties-filtered-en.png" alt="英文 Invoice number 字段，显示 Required、Read Only、Hidden、Force Validation、Use AI、OCR 和 Match Score 控件"><figcaption>搜索 `invoice_id` 后显示的 Invoice number 行。</figcaption></figure>

| 控件 | 用途 |
| --- | --- |
| **Required** | 将验证时必须填写的信息标记为必填。更改此设置后，请检查文档的验证结果。 |
| **Read Only** | 显示字段，但不允许用户编辑其值。 |
| **Hidden** | 在常规文档视图中隐藏该字段。 |
| **Force Validation** | 要求字段通过验证。请另行配置详细规则；此复选框不是规则编辑器。 |
| **Use AI** | 请求或停止对该字段进行 AI 提取。该行会显示是否已请求提取。 |
| **OCR** | 输入字段的 OCR 置信度阈值。这是一个数值，不是开关或语言设置。 |
| **Match Score** | 输入字段的匹配阈值。这是一个数值，不是开关。 |

**Recognition Settings** 下的 **OCR** 和 **Match Score** 滑块会将相应的值应用到整个字段列表。列标题正下方的复选框会将 **Required**、**Read Only**、**Hidden** 或 **Force Validation** 应用到整个列表。选择 **Save Settings** 前，请检查受影响的行。**Restore Defaults** 会重置字段配置；只有在确实要替换自己的更改时才使用此选项。

## 此视图中的其他控件

- **Create new group** 和 **Create field** 分别用于添加分组或字段。请参阅[添加和编辑字段](adding-and-editing-fields.md)。
- **Master Data Settings** 会打开[主数据配置](master-data-settings.md)。
- 最左侧的复选框用于选择字段。相邻菜单中的 **Reassign Field Group** 可用于重新分配所选字段的分组。
- **Formula** 加号按钮会打开该字段的公式编辑器。**info** 图标会显示字段信息。标准字段无法使用删除图标。

有关验证和匹配的更多信息，请参阅[设置验证和匹配分数](setting-validation-and-match-score.md)。
