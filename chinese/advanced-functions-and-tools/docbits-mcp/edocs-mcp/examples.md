# 示例

可复制的提示词以及完整的诊断、草稿、激活和回退流程，请参阅[使用 Claude 或 Codex 配置 DocBits](../configuration-with-claude-or-codex.md)。以下示例使用当前参数。请将所有占位符替换为本组织响应中的值，并提供完整且正确进行 JSON 转义的源代码。

## 1. 修改已有 Custom 规则

使用 `get_edoc_attribute_source` 读取实际生效的 `TRANSFORMATION`。格式名称必须与分类返回值完全一致：

```json
{
  "electronic_document_type": "<detected_type_from_response>",
  "attribute_name": "TRANSFORMATION",
  "doc_type_key": "INVOICE",
  "source": "effective"
}
```

记录 `attribute_id`、`active_value_id`、`active_version` 和 `value`。另行读取 `source: "default"` 以进行比较，并使用 `list_edoc_attribute_versions` 读取历史。以下操作要求本组织已有相应 Custom 属性。

使用 `preview_edoc_custom_xslt` 预览完整候选代码，不保存。文档必须已存在于同一组织中：

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "candidate_value": "<complete_candidate_xslt>",
  "doc_id": "<test_document_id_in_this_org>"
}
```

`TRANSFORMATION` 返回转换后的 XML，`PREVIEW` 返回 PDF，`EXTRACTION_PATHS` 返回字段和表格。预览不会选择已保存的草稿，也不测试后续脚本或导出。

审核差异与预览后，重新读取激活源代码，再使用 `update_edoc_custom_attribute` 保存草稿。必须明确传入 `activate: false`；工具默认值为 `true`。

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "new_value": "<complete_reviewed_xslt>",
  "activate": false
}
```

在测试组织完成测试并确认具体更改后，调用 `activate_edoc_attribute_version`。`draft_id` 是版本值 ID。随后重新读取生效源代码。回退时使用同一调用，将之前记录的 `active_value_id` 作为版本值 ID。

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "draft_id": "<value_id_of_reviewed_version>"
}
```

## 2. 如果还没有 Custom 属性

`create_edoc_custom_attribute` 会创建立即激活的首个版本，而不是草稿。请在测试组织验证新的覆盖规则，或使用 DocBits 编辑器支持的流程。不要仅为获得预览而创建或删除生产覆盖规则。保留必要的自定义映射；不要全局修改共享默认规则。

## 3. 测试当前激活的配置

调用 `test_electronic_document`，将原始 XML 编码为 base64：

```json
{
  "file_content_base64": "<base64_of_original_xml>",
  "file_name": "credit-note-test.xml"
}
```

此操作测试当前激活规则且不保存文档，不会测试未激活草稿。远程 HTTP MCP 无法读取您电脑上的本地 `file_path`。`compare_edoc_extraction` 只比较 Extraction Paths，并要求已有自定义提取路径属性；它不比较转换。

`validate_all_edocs` 对可用服务器测试文件进行试运行。`verify_electronic_documents` 会上传并处理测试文件，因此会创建文档。两者都不能证明 ERP 已接收。请使用代表性样本，单独检查已保存字段、金额和导出，不要批量重新处理历史文档。
