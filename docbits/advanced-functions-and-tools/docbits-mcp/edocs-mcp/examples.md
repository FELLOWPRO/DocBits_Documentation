# Examples

End-to-end examples showing how to use the eDocs MCP tools together.

## Example 1: Create a Custom Preview for XRechnung

This example walks through the full lifecycle of a custom PREVIEW rule:
1. Check what rules already exist
2. Preview the XSLT without activating it
3. Create the custom rule
4. Update it to a new version
5. Revert to the default

### Step 1: Check existing customizations

Call `list_edoc_custom_attributes`:

```json
{
  "electronic_document_type": "XRECHNUNG 2.1 CII",
  "doc_type_key": "INVOICE"
}
```

The response shows two lists. If `custom` is empty for the `PREVIEW` attribute, your org is currently using the built-in default preview stylesheet.

### Step 2: Test your XSLT before creating it

Call `preview_edoc_custom_xslt` with an existing attribute ID (use a default one from the `list` response) and a sample XML file encoded as base64:

```json
{
  "attribute_id": "<attribute_id_from_list>",
  "file_content_base64": "<base64_encoded_xrechnung_xml>",
  "file_name": "test_invoice.xml"
}
```

Inspect the rendered output to verify your XSLT produces the expected result before committing it.

### Step 3: Create the custom rule

Call `create_edoc_custom_attribute`:

```json
{
  "electronic_document_type": "XRECHNUNG 2.1 CII",
  "attribute_name": "PREVIEW",
  "attribute_value": "<?xml version=\"1.0\"?><xsl:stylesheet xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\" version=\"2.0\">...</xsl:stylesheet>",
  "doc_type_key": "INVOICE"
}
```

Save the `attribute_id` from the response. From this point on, every XRechnung 2.1 CII invoice processed by your organization will use your custom preview.

### Step 4: Update the rule with a new version

Later, if you want to refine the XSLT, call `update_edoc_custom_attribute`:

```json
{
  "attribute_id": "<your_attribute_id>",
  "new_value": "<?xml version=\"1.0\"?><xsl:stylesheet ...><!-- improved version --></xsl:stylesheet>",
  "activate": true
}
```

Setting `activate: true` immediately switches to the new version. The previous version is preserved in history. Set `activate: false` to save as a draft and activate it separately.

### Step 5: Revert to the built-in default

If you want to go back to the default preview, call `delete_edoc_custom_attribute`:

```json
{
  "attribute_id": "<your_attribute_id>"
}
```

The custom rule is removed and the system falls back to the shared default stylesheet automatically. No other customers are affected.

---

## Example 2: Customize Extraction Paths for EDI

Your organization receives EDI invoices with a non-standard field layout. This example shows how to override the extraction paths for your org.

### Step 1: Check the current rules

```
list_edoc_custom_attributes
  electronic_document_type: "EDI"
  doc_type_key: "INVOICE"
```

If you see an `EXTRACTION_PATHS` entry in `default` but not in `custom`, your org inherits the shared XPath rules.

### Step 2: Create your custom extraction paths

Call `create_edoc_custom_attribute` with your adjusted XPath JSON:

```json
{
  "electronic_document_type": "EDI",
  "attribute_name": "EXTRACTION_PATHS",
  "attribute_value": "{\"invoice_id\": \"//Invoice/ID/text()\", \"invoice_date\": \"//Invoice/IssueDate/text()\", \"total_amount\": \"//Invoice/LegalMonetaryTotal/TaxInclusiveAmount/text()\"}",
  "doc_type_key": "INVOICE"
}
```

### Step 3: Verify with a dry-run test

Call `test_electronic_document` with a sample EDI file to confirm the custom extraction paths pick up the right values:

```json
{
  "file_content_base64": "<base64_encoded_edi_xml>",
  "file_name": "sample_edi_invoice.xml"
}
```

The response includes `extracted_fields` and a `preview.image_base64` PNG — inspect both to verify correctness before going live.

---

## Example 3: Run a Full eDoc Verification

Before shipping a change, verify that all supported eDoc fixtures still pass:

```
validate_all_edocs
  fixture_filter: "xrechnung*"
  limit: 0
```

The tool runs every XRechnung fixture through the pipeline and reports pass/fail/warn per fixture. A clean run confirms your customizations haven't broken other document types.

To test just a single type quickly:

```
verify_electronic_documents
  fixture_filter: "zugferd*"
  limit: 3
```

This uploads up to 3 ZUGFeRD fixtures, waits for processing, and verifies classification, extraction, and preview generation end-to-end.
