# DocBits MCP

DocBits exposes a **Model Context Protocol (MCP)** server that lets AI assistants work with your documents, extraction, search, analytics, and configuration — directly from a chat or coding session. Any MCP-compatible client can connect: **Claude Code**, **Claude Desktop**, **Google Gemini CLI**, **OpenAI Codex**, or any custom integration.

The server is mounted on the DocBits API at `/v3/mcp` and is scoped to your organization — every call runs with the permissions of the user (or API key) that connected.

{% hint style="info" %}
**Endpoint — use your region (EU or US):**

- Production (EU) — `https://eu.api.docbits.com/v3/mcp`
- Production (US) — `https://us.api.docbits.com/v3/mcp`

See [Setup & Configuration](setup-and-configuration.md) for the full host matrix and how to sign in with OAuth.
{% endhint %}

## What Can You Do?

With DocBits MCP an assistant can, on your behalf:

- **Find and read documents** — list, search (full-text and fielded), open a document, read its status, logs, page images, and export preview
- **Work on extracted data** — read extracted fields and tables, correct field values, extract tables with AI, validate, approve, and export to your ERP
- **Query the dashboard** — run dashboard queries in natural language, compare search modes, and inspect search capabilities
- **Pull analytics** — executive summaries, success rates, volume trends, top document types, and pending-task detail
- **Handle e-invoices (eDocs)** — list electronic-document types, test and verify e-documents, manage custom extraction attributes
- **Manage master data** — upsert vendor master data, trigger supplier lookups, import supplier-invoice BODs, maintain payment-term and discount mappings
- **Read and change configuration** — organization preferences, document types, field settings, users, and cache
- **Check health** — API and Celery health, current user, and API info

## Tools Overview

DocBits MCP groups well over a hundred tools into the categories below (the exact number grows with every release; your assistant lists the current set). Most mirror existing DocBits REST endpoints, see the [API Reference](../../README.md) for request/response detail. An assistant picks the right tool automatically from your request; the tables are a map of what is available.

### Documents & Processing

| Tool | Description |
|------|-------------|
| `list_documents` | List documents for the organization (filterable) |
| `get_document` / `get_document_by_name` | Open a document by ID or filename |
| `upload_document` | Upload a new document for processing |
| `get_document_status` | Current pipeline status of a document |
| `get_document_logs` | Processing log entries for a document |
| `query_org_logs` | Page through the organization's service logs |
| `restart_document` | Re-run the processing pipeline |
| `delete_document` | Delete a document |
| `get_pending_documents_count` | How many documents await validation |

### Extraction & Validation

| Tool | Description |
|------|-------------|
| `get_extracted_fields` / `get_document_fields` | Read extracted header fields |
| `get_extracted_tables` | Read extracted line-item tables |
| `get_document_for_validation` / `get_next_document` | Open a document the way the validation screen does; fetch the next one in the queue |
| `get_page_image` | Page image for visual checks |
| `update_document_fields` | Correct or set field values |
| `validate_document` | Run field validation rules |
| `approve_document` | Approve a validated document |
| `validate_and_export` | Validate then export to the ERP |
| `get_export_preview` | Preview the export payload before sending |

### Table Extraction

Everything the validation screen and the table-column settings can do with line-item tables. Configuration tools change the organization's document types; extraction and correction tools work on one document; rule tools store what DocBits learned for a supplier.

| Tool | Description |
|------|-------------|
| `list_tables` / `get_table_config` | Tables and columns of a document type, with the Required / Read Only / Hidden / Use AI flags |
| `create_table` | Add a second line-item table to a document type |
| `add_table_column` / `delete_table_column` | Add or soft-delete a table column |
| `set_ai_table_config` | Switch AI table extraction, vision and structured mode for the organization |
| `extract_table_ai` | Run the AI table extraction on a document (text or vision) |
| `extract_table_only` | Extract the table without touching the header fields (rules or AI) |
| `extract_table_nonai` | Rule-based extraction from coordinates you pass, the first step of a table training through the API |
| `apply_ai_table_formatting` / `apply_table_feedback` | Reformat an AI table: hide columns, remap, apply user feedback |
| `remap_table_columns` | Change which extracted column feeds which configured column |
| `save_table_rules` / `save_table_training_rules` | Store the coordinate rules or the AI formatting rules for the supplier, so the next document extracts the same way |
| `delete_table_training_rules` | Remove a supplier's saved rules; the next document falls back to the AI |
| `get_table_extraction_report` / `list_table_report_suppliers` | Per-supplier report of how tables are extracted (rules, AI, model), with a preview |
| `compare_table_extraction_models` | Extract the same document with two AI tiers and compare the tables |

### Search & Dashboard

| Tool | Description |
|------|-------------|
| `search_documents` / `search_documents_by_name` | Full-text and filename search |
| `query_document_dashboard` | Natural-language dashboard query |
| `explain_document_dashboard_query` | Show how a query was interpreted |
| `get_search_capabilities` | Which search features the org has enabled |
| `compare_search_modes` | Compare keyword vs. vector results |
| `diagnose_document_search` | Why a document does or does not show up for a given search, classical vs. full-text, side by side |
| `inspect_document_search_index` | Whether a document is present in the document, text and vector indices, and when each was written |
| `get_dashboard_columns` / `set_dashboard_columns` | Read or change the columns shown on the document dashboard |

### Touchless Intelligence

Why documents need human involvement and what to change so that fewer do. Every tool here is read-only except `touchless_apply_change`, which writes exactly one previewed setting change.

| Tool | Description |
|------|-------------|
| `touchless_get_summary` | Touchless scorecard for the organization: how many documents went through untouched, by period and segment |
| `touchless_list_segments` | Values you can segment the numbers by (supplier, document type, …) |
| `touchless_rank_supplier_opportunities` | Suppliers ranked by how much manual work they cause |
| `touchless_diagnose_supplier` | Why one supplier's documents stop for a human |
| `touchless_get_issue_cluster` | One recurring issue and the documents it affected |
| `touchless_get_document_trace` | Full touchless history of one document |
| `touchless_explain_pipeline` | Where in the pipeline a document or a cluster stopped |
| `touchless_explain_po_match` / `touchless_get_po_match_evidence` | Why PO matching succeeded or failed, with the rule set and tolerance maths |
| `touchless_get_recommendations` | What to change, not just what went wrong |
| `touchless_list_change_proposals` | Setting changes that would raise the touchless rate, with the expected lift |
| `touchless_preview_change` | Dry-run one proposal: nothing is written |
| `touchless_apply_change` | Apply one previewed proposal to the organization |
| `touchless_verify_change` | What an applied change turned out to be worth |

### Analytics & BI

| Tool | Description |
|------|-------------|
| `get_executive_summary` | High-level KPIs for the organization |
| `get_success_rates` | Touchless / straight-through rates |
| `get_volume_trends` | Document volume over time |
| `get_top_document_types` | Most frequent document types |
| `get_pending_tasks_detail` | Detail of outstanding work |

### Electronic Documents (e-invoices)

| Tool | Description |
|------|-------------|
| `list_electronic_document_types` | Supported e-invoice formats (ZUGFeRD, XRechnung, Factur-X, UBL, …) |
| `test_electronic_document` | Classify and extract a sample e-document |
| `verify_electronic_documents` / `validate_all_edocs` | Verify e-document extraction |
| `list_edoc_custom_attributes` / `create_edoc_custom_attribute` | Manage custom extraction attributes |

### Master Data

| Tool | Description |
|------|-------------|
| `upsert_vendor_master_data` | Create or update vendor master data |
| `trigger_supplier_lookup` | Enrich a document from supplier master data |
| `import_supplier_invoice_bod` | Import a supplier-invoice BOD |
| `get_supplier_invoice` | Read the persisted supplier-invoice (BOD) data by invoice, supplier or document |
| `upsert_payment_term_mapping` / `upsert_discount_mapping` | Maintain calculation mappings |

### Configuration, Admin & Health

| Tool | Description |
|------|-------------|
| `get_preferences` / `get_preference` / `set_preference` | Read and change org preferences |
| `list_document_types` / `get_field_settings` | Inspect the document-type and field setup |
| `list_users` | List organization users |
| `clear_org_cache` | Clear cached configuration |
| `check_api_health` / `check_celery_health` | Service health |
| `get_current_user` / `get_api_info` | Identity and API metadata |

## Next steps

- [**Setup & Configuration**](setup-and-configuration.md) — connect Claude Code, Gemini CLI, or Codex (with login or API key)
- [**Examples**](examples.md) — real things customers ask the assistant to do
- [**Electronic Documents (eDocs)**](../edocs-mcp/README.md) — deep dive on the eDoc tools: inspect/test e-invoice processing and manage custom extraction/preview rules (same endpoint, same login)
- [**Workflows & Cards (DocFlow)**](../docflow-mcp/README.md) — manage advanced workflows and partner cards

{% hint style="info" %}
**One MCP for everything.** The eDoc tools and the **Workflows & Cards (DocFlow)** tools run on the **same** `api.docbits.com/v3/mcp` endpoint with the same DocBits login. DocFlow tools appear there with the prefix `docflow_` (for example `docflow_list_workflows`); the DocFlow page documents them under their bare names. Connecting to the DocFlow host directly is still possible but no longer necessary.
{% endhint %}
