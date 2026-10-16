# 示例

展示如何将 eDocs MCP 工具组合使用的端到端示例。

## 示例 1：为 XRechnung 创建自定义预览

本示例将演示自定义 PREVIEW 规则的完整生命周期：
1. 检查现有规则
2. 预览 XSLT，但不启用它
3. 创建自定义规则
4. 将其更新为新版本
5. 恢复为默认规则

### 步骤 1：检查现有自定义设置

调用 `list_edoc_custom_attributes`：

```json
{
  "electronic_document_type": "XRECHNUNG 2.1 CII",
  "doc_type_key": "INVOICE"
}
```

响应会显示两个列表。如果 `PREVIEW` 属性的 `custom` 列表为空，说明贵组织当前使用的是内置默认预览样式表。

### 步骤 2：创建规则前测试 XSLT

使用现有属性 ID（从 `list` 响应中选择一个默认 ID）以及以 base64 编码的示例 XML 文件调用 `preview_edoc_custom_xslt`：

```json
{
  "attribute_id": "<attribute_id_from_list>",
  "file_content_base64": "<base64_encoded_xrechnung_xml>",
  "file_name": "test_invoice.xml"
}
```

检查渲染后的输出，确认 XSLT 生成了预期结果，然后再提交。

### 步骤 3：创建自定义规则

调用 `create_edoc_custom_attribute`：

```json
{
  "electronic_document_type": "XRECHNUNG 2.1 CII",
  "attribute_name": "PREVIEW",
  "attribute_value": "<?xml version=\"1.0\"?><xsl:stylesheet xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\" version=\"2.0\">...</xsl:stylesheet>",
  "doc_type_key": "INVOICE"
}
```

保存响应中的 `attribute_id`。从此之后，贵组织处理的每一张 XRechnung 2.1 CII 发票都会使用您的自定义预览。

### 步骤 4：使用新版本更新规则

之后，如果您想优化 XSLT，请调用 `update_edoc_custom_attribute`：

```json
{
  "attribute_id": "<your_attribute_id>",
  "new_value": "<?xml version=\"1.0\"?><xsl:stylesheet ...><!-- improved version --></xsl:stylesheet>",
  "activate": true
}
```

设置 `activate: true` 会立即切换到新版本。先前版本会保留在历史记录中。设置 `activate: false` 可将其保存为草稿，之后再单独启用。

### 步骤 5：恢复为内置默认规则

如果您想恢复默认预览，请调用 `delete_edoc_custom_attribute`：

```json
{
  "attribute_id": "<your_attribute_id>"
}
```

自定义规则将被移除，系统会自动回退到共享默认样式表。不会影响其他客户。

---

## 示例 2：自定义 EDI 的提取路径

贵组织收到的 EDI 发票使用了非标准字段布局。本示例展示如何为贵组织覆盖提取路径。

### 步骤 1：检查当前规则

```
list_edoc_custom_attributes
  electronic_document_type: "EDI"
  doc_type_key: "INVOICE"
```

如果您在 `default` 中看到 `EXTRACTION_PATHS` 条目，但在 `custom` 中没有看到，说明贵组织继承了共享的 XPath 规则。

### 步骤 2：创建自定义提取路径

使用调整后的 XPath JSON 调用 `create_edoc_custom_attribute`：

```json
{
  "electronic_document_type": "EDI",
  "attribute_name": "EXTRACTION_PATHS",
  "attribute_value": "{\"invoice_id\": \"//Invoice/ID/text()\", \"invoice_date\": \"//Invoice/IssueDate/text()\", \"total_amount\": \"//Invoice/LegalMonetaryTotal/TaxInclusiveAmount/text()\"}",
  "doc_type_key": "INVOICE"
}
```

### 步骤 3：通过试运行测试进行验证

使用示例 EDI 文件调用 `test_electronic_document`，确认自定义提取路径能够提取正确的值：

```json
{
  "file_content_base64": "<base64_encoded_edi_xml>",
  "file_name": "sample_edi_invoice.xml"
}
```

响应包含 `extracted_fields` 和一个 `preview.image_base64` PNG。请检查两者，确认无误后再投入使用。

---

## 示例 3：运行完整的 eDoc 验证

发布更改前，请验证所有受支持的 eDoc 测试样例仍能通过：

```
validate_all_edocs
  fixture_filter: "xrechnung*"
  limit: 0
```

该工具会将每个 XRechnung 测试样例送入处理流程，并按样例报告通过/失败/警告状态。全部通过表示您的自定义设置没有影响其他文档类型。

若要快速测试单一类型：

```
verify_electronic_documents
  fixture_filter: "zugferd*"
  limit: 3
```

这会上传最多 3 个 ZUGFeRD 测试样例，等待处理完成，并端到端验证分类、提取和预览生成。
