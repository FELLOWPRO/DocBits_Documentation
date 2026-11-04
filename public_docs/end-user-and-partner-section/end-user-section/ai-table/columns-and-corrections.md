# 列与修正

[AI Table](README.md) · [表格的 Structured Output](structured-output.md)

## 更改列

### 选择正确的列（重新映射）

如果某个值位于错误的列中，可以使用此功能。例如，净额出现在 _Total amount_ 中，或者发票中有数量，但 _Quantity_ 为空。

1. 点击标题中的**列名称**。
2. 选择值实际所属的已配置表格列。

<figure><img src="../../../.gitbook/assets/ai-table-map-column-en.png" alt="在表格标题上方展开的列名称列表"><figcaption><p>点击列名称，然后选择它应该对应的列。列表会显示所有已配置的表格列。</p></figcaption></figure>

DocBits 会立即重新排列表格，此更改仅适用于当前文档。如果所选列已被另一列使用，对话框 _Remap "…"?_ 会警告另一列将变为未映射状态。确认后即可继续；另一列随后会显示错误图标 _Select a column to map from dropdown_，你可以为其选择对应的列。

### 三点菜单

<figure><img src="../../../.gitbook/assets/ai-table-column-menu-en.png" alt="包含 Delete column 和 Extract From 的三点菜单"><figcaption><p>列的三点菜单。</p></figcaption></figure>

| 条目 | 功能 |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Delete column**     | 隐藏该列。确认提示会显示 _Modifications will be discarded_；选择 **Done**。系统会在删除该列后重新生成表格。使用页脚工具栏中的 **Restore Table Column** 可恢复隐藏的列。 |
| **Disable column**    | 对于你自行添加的列：隐藏该列，但不重新运行 AI。 |
| **Amount Formatting** | 仅适用于金额列。选择数字的读取方式（小数分隔符和千位分隔符）。**Auto** 由 DocBits 自动判断。 |
| **Extract From**      | 指示 AI 从列标签的**上方**或**下方**一行提取值。如果值位于通常的位置，请留空。 |

### 页脚工具栏 <a id="footer-toolbar"></a>

<figure><img src="../../../.gitbook/assets/ai-table-footer-toolbar-en.png" alt="表格页脚工具栏图标"><figcaption><p>验证界面页脚中的表格图标，从左到右排列。</p></figcaption></figure>

| 图标（工具提示） | 功能 |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Go to table extraction view**                           | 打开传统表格训练。如果文档包含 AI 表格，DocBits 会发出警告：_Table is already extracted by AI. Do you want to train manually? In future AI table will not extracted for this supplier_。 |
| **Add empty mapped columns**                              | 打开 **Columns settings**，以添加 AI 未填充的已配置列，方便你手动输入值。 |
| **Show non mapped columns**（显示未映射列）/ **Hide non mapped columns**（隐藏未映射列） | 显示或隐藏 AI 返回但未映射到已配置列的列。默认情况下，这些列处于隐藏状态。此操作只会更改当前文档的视图。 |
| **Block table extraction for this supplier**（禁止对此供应商执行表格提取）              | 关闭该供应商的表格提取。 |
| **Delete table**                                          | 清空编辑器中的表格。 |
| **Add new table column**（添加新的表格列）                                  | 添加自定义列。仅限管理员使用。 |
| **Add new table row**                                     | 添加空行。 |
| **Ignore table validation**                               | 忽略当前文档的表格验证。 |
| **Restore Table Column**                                  | 恢复所有已删除的列。 |

<figure><img src="../../../.gitbook/assets/ai-table-columns-settings-en.png" alt="包含两个列表的 Columns settings 对话框"><figcaption><p>Columns settings：使用箭头按钮将列从 <em>Available columns</em> 移至 <em>Columns in table</em>，然后选择 <strong>Done</strong>。</p></figcaption></figure>
