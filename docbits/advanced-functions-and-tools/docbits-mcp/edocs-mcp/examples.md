# Examples

For copyable prompts and the full diagnosis, draft, activation and rollback procedure, see [Configure DocBits with Claude or Codex](../configuration-with-claude-or-codex.md). The examples below use the current tool arguments. Replace all placeholders with values returned for your own organization and pass complete, correctly JSON-escaped source code.

## 1. Change an existing Custom rule

Read the effective `TRANSFORMATION` with `get_edoc_attribute_source`. Use the exact format label returned by classification:

```json
{
  "electronic_document_type": "<detected_type_from_response>",
  "attribute_name": "TRANSFORMATION",
  "doc_type_key": "INVOICE",
  "source": "effective"
}
```

Record `attribute_id`, `active_value_id`, `active_version` and `value`. Read `source: "default"` separately for comparison. Read history with `list_edoc_attribute_versions`. The following edit loop assumes an existing organization-owned Custom attribute.

Preview the full candidate without saving it with `preview_edoc_custom_xslt`. Use a document already present in the same organization:

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "candidate_value": "<complete_candidate_xslt>",
  "doc_id": "<test_document_id_in_this_org>"
}
```

The result is transformed XML for `TRANSFORMATION`, PDF for `PREVIEW`, or fields/tables for `EXTRACTION_PATHS`. The preview does not select a saved draft and does not test later scripts or exports.

After reviewing the diff and preview, reread the active source and save a draft with `update_edoc_custom_attribute`. Explicitly use `activate: false`; this tool defaults to `true`.

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "new_value": "<complete_reviewed_xslt>",
  "activate": false
}
```

After tests in the test organization and confirmation of the exact change, call `activate_edoc_attribute_version`. `draft_id` is the version value ID. Then read the effective source again. Rollback uses the previously recorded `active_value_id` in the same call.

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "draft_id": "<value_id_of_reviewed_version>"
}
```

## 2. If no Custom attribute exists

`create_edoc_custom_attribute` creates an immediately active first version, not a draft. Test a new override in a test organization or use the supported DocBits editor flow. Do not create or delete a production override just to obtain a preview. Preserve required custom mappings; shared defaults must not be modified globally.

## 3. Test the active configuration

Call `test_electronic_document` with the original XML encoded as base64:

```json
{
  "file_content_base64": "<base64_of_original_xml>",
  "file_name": "credit-note-test.xml"
}
```

This tests the currently active rules without saving a document. It does not test an inactive draft. Remote HTTP MCP cannot read a local `file_path` on your computer. `compare_edoc_extraction` compares Extraction Paths only and requires a Custom Extraction Paths attribute; it does not compare Transformations.

`validate_all_edocs` dry-runs the available server fixtures. `verify_electronic_documents` uploads and processes fixtures and therefore creates documents. Neither proves successful ERP delivery. Use representative samples, check stored fields/amounts and export separately, and do not bulk-restart historical documents.
