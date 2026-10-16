# 字段是否存在

<figure><img src="../../../../../.gitbook/assets/image (50).png" alt="" width="563"><figcaption></figcaption></figure>

## **用途：**

此工作流卡片旨在根据文档中指定字段的存在情况或状态自动执行操作。通过判断该字段为空、缺失还是已填充，它可以帮助工作流精确、准确地处理文档。

## **卡片组件：**

1. **字段名称**
   * **描述：**指定要评估的字段名称。
   * **详情：**该名称必须与文档中使用的确切标识符一致，以确保准确检测字段。
2. **运算符**
   * **描述**：定义根据字段的存在情况或状态触发工作流的条件。
   * **选项**：
     * **为空/不在文档中：**如果字段缺失，或字段存在但为空，则触发工作流。
     * **在文档中/不为空：**如果字段存在于文档中且包含值，则触发工作流。

## **功能：**

* **状态检测：**卡片会监控指定字段，以评估其是否存在及其状态。
* **条件评估：**
  * 系统会根据所选运算符，评估指定字段是否处于定义的状态（为空/不在文档中或在文档中/不为空）。
*

```
**Action Execution:**
```

```
* **Empty/Not in Document Condition:** If the field's state matches this condition (i.e., the field is either absent from the document or present but empty), the system initiates the associated actions. These may include generating alerts, flagging the document for review, or halting the workflow.
* **In Document/Not Empty Condition:** If the field's state matches this condition (i.e., the field exists in the document and contains a value), the system triggers the associated actions. These could involve enabling subsequent workflow steps, updating records, or triggering notifications.
```

## **设置和配置：**

* 用户可从可用文档字段列表中选择字段，并通过下拉菜单选择运算符。菜单提供“为空/不在文档中”或“在文档中/不为空”选项，含义清晰明确。

## **结论：**

“字段存在与状态验证”工作流卡片是文档处理工作流中的重要工具，可确保准确处理缺失或已填充的字段。通过根据字段状态自动执行操作，该卡片有助于提高数据完整性、减少错误，并确保工作流顺畅、高效地运行。
