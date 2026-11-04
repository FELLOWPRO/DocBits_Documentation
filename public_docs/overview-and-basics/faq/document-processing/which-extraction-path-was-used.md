# Which extraction path was used?

"Why does this table look like that?" is answered by finding out *what* DocBits did for this document: saved rules, the AI table, which AI tier, and where it went wrong. This page is the checklist support and partners use before changing any configuration.

## 1. Look at the tabs on the validation screen

Open the document and look at the tabs above the line-item table:

| What you see | Path |
|---|---|
| Rows in the **Extracted table** tab | Rule-based path. The supplier has a trained table; the rows come from the saved coordinate rules and the AI was not involved (except for columns marked *Use AI*). |
| Rows in the **AI Extracted table** tab, *Tags* field below | AI path. No saved rules matched; the AI table extraction produced the rows, using the organization's AI tier or the tier set for this supplier under *More settings* → *Supplier-Based AI Model*. |
| *AI table not found* tooltip on the AI tab | The AI path ran and returned nothing for this document. |
| No table tabs at all | Both table settings are off for the organization, nothing extracted the table. |
| *No line items yet* | The path ran but found no rows (no readable text, no table on the page, or the rules did not match this layout). |

Header fields carry their own source badge next to the value: *Extracted using AI*, *Learned from validated AI extraction*, *Extracted using saved rules (FELLOW_KV2)*, *Extracted from electronic document*, *Calculated from vendor master data*. These badges describe the header field, not the table.

## 2. Check the supplier's configuration

* **Settings → Document Processing → Classification and Extraction → AI Model**: the table under the selector lists every supplier with a stored model or training. A supplier in this list with *training data* has saved rules; *reset the training data* removes them.
* **Settings → Document Processing → OCR Settings**: *Use E-Text if available* and *Use AI data for tables* change what text the extraction sees. A supplier can override E-Text under *More settings* on the validation screen.
* **Settings → Global Settings → Document Types → Table Columns**: hidden, required and *Use AI* flags. A hidden column is never filled; a *Use AI* column is filled by the AI even for suppliers with rules.

## 3. Reproduce without the UI (API / MCP)

With API or MCP access you can ask the same questions programmatically:

| Question | Tool |
|---|---|
| Was this table produced by the AI? | `get_extracted_tables(doc_id)`: each table carries `is_ai_table: true/false`. |
| What do the rules give, what does the AI give? | `get_table_extraction_report(doc_id, mode="nonai")` and again with `mode="ai"`, the report shows the configured structure, the extracted rows and the page preview for each path. Compare the two. |
| Which columns are configured, with which flags? | `get_table_config(doc_type)` |
| Does the AI tier matter? | `compare_table_extraction_models(doc_id)`, runs two tiers on the same document (needs a document with a supplier number). |
| Redo the extraction on this document | `extract_table_ai(doc_id)` (AI) or `restart_document(doc_id)` (whole pipeline). |
| What did the pipeline log for this document? | `get_document_logs(doc_id)` |

The DocBits MCP tools are described under [DocBits MCP](../../../advanced-functions-and-tools/docbits-mcp/README.md).

## 4. Read the logs

**Settings → Log Settings** (Activity Logging) shows the events of all services. For a table question:

* Filter by the document's file name or ID in *Search logs*.
* Use the *Service* filter: the extraction itself runs in the extraction service and the Celery workers, not in the `api` service. If you only see `api` lines, widen the filter.
* A normal run logs, in order: document received → OCR / E-Text → classification → field extraction → table extraction (rules lookup, then AI when no rules match) → validation → status change. The step that is missing or reports an error is the one to look at.

## 5. Decide: configuration, data, or bug

| Symptom | Most likely | Next step |
|---|---|---|
| Table right for supplier A, wrong for supplier B, same document type | Per-supplier: B has no rules, or old rules that no longer match B's layout | Train B's table once (or delete B's rules so the AI takes over). |
| Table wrong for every supplier since a certain date | Organization setting changed (AI tier, structured extraction, vision, table columns) | Compare the settings with the change date; restart one document to confirm. |
| Same document: rules path empty, AI path correct | Rules do not match this layout variant | Re-train with this document, or delete the rules. |
| Same document: both paths empty | No readable text (scan without OCR text, image-only PDF) | OCR view on the validation screen; enable E-Text if the PDF has a text layer; try another OCR version. |
| One column wrong on every row, rest fine | Column mapping or *Use AI* flag | Table Columns settings; remap in table training. |
| Rows missing at page breaks or after a subtotal | Layout the AI or rules did not follow | Train the table with a multi-page document; add a tag such as *"table continues on page 2"*. |
| Extraction step missing in the logs, document stuck in *running* | Infrastructure (worker backlog), not configuration | Check the pending tasks (`get_pending_tasks_detail` via MCP) and contact support with the document ID. |

## What to send to support

* Document ID and organization
* Which tab holds the rows (Extracted table / AI Extracted table / none) and the AI tier in use
* Whether the supplier has saved rules and when they were last saved
* One example document where it works and one where it does not, if you have both

## Related pages

* [Table Extraction Troubleshoot](table-extraction-troubleshoot.md): extraction quality, OCR, E-Text, table messages
* [Training Line Fields / Table Training](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md)
* [AI Table](../../../end-user-and-partner-section/end-user-section/ai-table/README.md)
* [Log Settings](../../../administration-and-setup/settings/log-settings/README.md)
