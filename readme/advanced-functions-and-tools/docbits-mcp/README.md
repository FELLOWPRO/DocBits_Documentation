# DocBits MCP

DocBits exposes a **Model Context Protocol (MCP)** server that lets AI assistants work with your documents, extraction, search, analytics, and configuration — directly from a chat or coding session. Any MCP-compatible client can connect: **Claude Code**, **Claude Desktop**, **Google Gemini CLI**, **OpenAI Codex**, or any custom integration.

The server is mounted on the DocBits API at `/v3/mcp` and is scoped to your organization — every call runs with the permissions of the user (or API key) that connected.

{% hint style="info" %}
**Endpoint:** `https://<region>.<env>.api.docbits.com/v3/mcp`

For example `https://eu.dev.api.docbits.com/v3/mcp` (EU dev) or `https://eu.api.docbits.com/v3/mcp` (EU production). See [Setup & Configuration](setup-and-configuration.md) for the full host matrix and how to sign in.
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

DocBits MCP groups ~90 tools into the categories below. Most mirror existing DocBits REST endpoints — see the [API Reference](../../README.md) for request/response detail. An assistant picks the right tool automatically from your request; the tables are a map of what is available.

### Documents & Processing

| Tool | Description |
|------|-------------|
| `list_documents` | List documents for the organization (filterable) |
| `get_document` / `get_document_by_name` | Open a document by ID or filename |
| `upload_document` | Upload a new document for processing |
| `get_document_status` | Current pipeline status of a document |
| `get_document_logs` | Processing log entries for a document |
| `restart_document` | Re-run the processing pipeline |
| `delete_document` | Delete a document |
| `get_pending_documents_count` | How many documents await validation |

### Extraction & Validation

| Tool | Description |
|------|-------------|
| `get_extracted_fields` / `get_document_fields` | Read extracted header fields |
| `get_extracted_tables` | Read extracted line-item tables |
| `extract_table_ai` / `extract_table_only` | Re-extract tables (AI or rules) |
| `update_document_fields` | Correct or set field values |
| `validate_document` | Run field validation rules |
| `approve_document` | Approve a validated document |
| `validate_and_export` | Validate then export to the ERP |
| `get_export_preview` | Preview the export payload before sending |

### Search & Dashboard

| Tool | Description |
|------|-------------|
| `search_documents` / `search_documents_by_name` | Full-text and filename search |
| `query_document_dashboard` | Natural-language dashboard query |
| `explain_document_dashboard_query` | Show how a query was interpreted |
| `get_search_capabilities` | Which search features the org has enabled |
| `compare_search_modes` | Compare keyword vs. vector results |

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
