# Examples

Once DocBits MCP is connected (see [Setup & Configuration](setup-and-configuration.md)), you talk to your assistant in plain language — it picks the right DocBits tools for you. Below are realistic things customers do, with the kind of prompt you'd type and the tools the assistant uses behind the scenes.

{% hint style="info" %}
These work the same in Claude Code, Gemini CLI, and Codex — the prompts are natural language, not commands.
{% endhint %}

## Triage the work queue

> *"How many documents are waiting for validation, and what types are they?"*

Uses `get_pending_documents_count`, `get_pending_tasks_detail`, `get_top_document_types`. The assistant summarizes the backlog and can drill into any document.

> *"Show me the invoices that errored today and tell me why."*

Uses `search_documents` / `query_document_dashboard` + `get_document_logs` to find errored documents and explain the failure from the logs.

## Find and inspect a document

> *"Open invoice INV-2026-00231 and show the extracted fields and the line items."*

Uses `get_document_by_name`, `get_extracted_fields`, `get_extracted_tables`. The assistant returns the header data and the table, and can fetch the page image with `get_page_image` if you want to see the source.

> *"Search all documents from vendor 'ACME GmbH' last month over €10,000."*

Uses `search_documents` / `query_document_dashboard` with fielded filters.

## Correct and approve

> *"On document 84213, set the PO number to 4500098123 and the due date to 2026-07-15, then validate it."*

Uses `update_document_fields` then `validate_document`. The assistant reports any validation errors so you can fix them.

> *"Validate and export document 84213 to the ERP, but show me the export preview first."*

Uses `get_export_preview`, then `validate_and_export` once you confirm.

## Fix a table extraction

> *"The line-item table on this delivery note is wrong — re-extract it with AI and verify it."*

Uses `extract_table_ai` + `verify_table_extraction`. Useful for documents where the rule-based extraction missed rows.

## Analytics & reporting

> *"Give me an executive summary for this month: volume trend, touchless rate, and top 5 document types."*

Uses `get_executive_summary`, `get_volume_trends`, `get_success_rates`, `get_top_document_types`. Great for a quick management update without opening the dashboard.

## E-invoicing (eDocs)

> *"Which electronic invoice formats are enabled for us, and does this ZUGFeRD file extract correctly?"*

Uses `list_electronic_document_types` + `test_electronic_document`, then `verify_electronic_documents` to confirm the extracted fields.

## Master data & supplier enrichment

> *"Add a new vendor (name, VAT, IBAN) to master data, then re-run supplier lookup on document 84500."*

Uses `upsert_vendor_master_data` + `trigger_supplier_lookup`.

## Configuration changes

> *"Enable QR-code extraction for our organization and confirm the preference is set."*

Uses `set_preference` (which clears the cache automatically) + `get_preference` to confirm.

> *"List our document types and show the field settings for 'Invoice'."*

Uses `list_document_types` + `get_field_settings`.

## Health & diagnostics

> *"Is the DocBits API and the processing worker healthy right now? Who am I connected as?"*

Uses `check_api_health`, `check_celery_health`, `get_current_user`.

---

## Tips

- **Be specific about the document** — an ID or exact filename is fastest; otherwise the assistant will search first.
- **Ask for a preview before exporting** — `get_export_preview` lets you confirm the ERP payload before `validate_and_export` sends it.
- **Permissions apply** — the assistant can only do what your DocBits user or API key is allowed to do. Approvals and exports respect your role and ACLs.
- **Production care** — the MCP acts on real data. On customer/production environments, prefer read/preview actions and confirm before approving, exporting, or deleting.
