# 故障排除

## 新列未显示在验证界面上

* 添加列之前，文档就已处理完成。更改仅适用于之后上传或重新启动的文档，**请重新启动文档**（Dashboard → document menu → Restart）。
* 该列处于**隐藏**状态。请检查 Table Columns 列表中的标记。
* 该列被添加到了**其他表格**，而不是当前显示的表格。验证界面会显示此文档类型中的表格；请对照 *Table name* 列。
* 该文档不属于你配置的文档类型。

## 列已显示，但始终为空

* 该供应商已有**训练规则**，但新列尚未映射到这些规则中。请在表格训练中打开该供应商的一份文档并映射此列，或在该列上设置 *Use AI*。
* 使用 AI 提取时，文档中的值无法识别（没有表头、经过缩写或使用了其他语言）。请添加一个[AI 表格标签](../../../../../end-user-and-partner-section/end-user-section/ai-table/ai-table-tags.md)，为该列命名，或在训练中映射该列。

## “Column name already exists”

表格中已存在技术名称相同的列。如果列表中没有显示该列，则它是一个隐藏的默认列：提示信息会显示 *Please activate it in Table Column settings*。请取消选中该列的 *Hidden*，而不是新建一列。

## 必填列导致审批受阻

表格上的提示信息会指出该列。请填写每一行中的单元格；或者，如果该值在此文档中不存在，请取消选中该列的 *Is Required*，重新启动文档后重试。请考虑该列是否确实应该设为必填（请参阅[最佳实践](best-practices-2.md)）。

## AI 将错误的值填入列中

常见情况：`CHARGES` 获取了行合计，导致每一行都无法通过行合计检查，并显示 *Line total does not match quantity x unit price (expected …, got …)*，因为费用属于公式 `quantity × unit price + charges` 的一部分。

* 如果训练规则能够正确提取该列，请取消选中该列的 *Use AI*。
* 如果该供应商没有规则，请训练一次表格（Table training），将该列绑定到正确的位置；如果供应商从不打印该值，也可以隐藏此列。
* 最后可采用的办法是，在文档类型的 More Settings 中启用 *Skip table validation*，这样会关闭整个文档类型的所有表格检查；此时系统将不再检测此不匹配，也不会检测为空的必填列。

## PO 匹配：“Line Item Table is missing Mandatory column”

PO 匹配需要默认列：项目编号、单价、数量和总金额。其中一列可能被隐藏，或被自定义列替代。请取消隐藏默认列，或在表格训练中将该值映射到对应的默认列。

## 删除列后脚本或导出失败

脚本或导出映射仍引用已删除列的 *Column name*。请移除此引用，或使用相同标题重新添加该列；系统会根据标题生成技术名称，因此名称会再次匹配。

## 进一步查阅

* [表格提取故障排除](../../../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md)：提取质量、OCR、E-Text
* [训练行字段 / 表格训练](../../../../setup/document-training/training-line-fields-table-training/README.md)
