# eDocs MCP

The DocBits API exposes a **Model Context Protocol (MCP)** server with tools for inspecting and customizing electronic document (eDoc) processing. Any MCP-compatible client — Claude Code, Claude Desktop, or custom integrations — can connect and use these tools.

## What Can You Do?

With the eDocs MCP tools you can:

- **Inspect** how any electronic document type is classified and what extraction rules apply
- **Test** documents through the full processing pipeline without saving to the database
- **Create custom rules** for your organization — XSLT previews, extraction paths, transformations
- **Update** a custom rule with a new version (with or without immediately activating it)
- **Delete** a custom rule to revert back to the built-in default
- **Verify** that all supported eDoc fixtures are processed correctly

## Permission Model

DocBits ships with a library of built-in default rules shared across all customers. These defaults use the reserved org ID `00000000-0000-0000-0000-000000000000`.

**The default rules are immutable via MCP.** Every write tool checks your organization ID before making any request. If it resolves to the default org, the operation is immediately rejected — no API call is ever made.

Customers can only create, change, or delete rules **within their own organization**. When a custom rule exists for your org, it takes precedence over the default. Deleting a custom rule restores the default behavior automatically.

```
Your org rule  ──► used if present
      │
      ▼ (if absent)
Default rule   ──► built-in, immutable via MCP
```

## Tools Overview

### Inspection (read-only)

| Tool | Description |
|------|-------------|
| `test_electronic_document` | Dry-run the full eDoc pipeline — classification, extraction, preview — without saving |
| `list_electronic_document_types` | List all supported eDoc types with configuration status |
| `get_extraction_rules` | Show the XPath rules used to extract fields for a given document type |
| `get_extracted_fields` | Get header fields extracted from a processed document |
| `get_extracted_tables` | Get line items extracted from a processed document |
| `get_preview_pdf` | Retrieve the XSLT-rendered preview PDF for a document |
| `get_preview_image` | Retrieve a rendered page image for a processed document |

### Customization (org-scoped, default org blocked)

| Tool | Description |
|------|-------------|
| `list_edoc_custom_attributes` | List your org's custom overrides vs. built-in defaults for a document type |
| `create_edoc_custom_attribute` | Create a new custom rule (EXTRACTION_PATHS, TRANSFORMATION, or PREVIEW) |
| `update_edoc_custom_attribute` | Add a new version of a custom rule, optionally activating it immediately |
| `delete_edoc_custom_attribute` | Delete a custom rule — the system falls back to the default automatically |
| `preview_edoc_custom_xslt` | Dry-run a XSLT transformation against an XML document before activating |

### Verification

| Tool | Description |
|------|-------------|
| `verify_electronic_documents` | Upload fixtures and verify classification, extraction, and preview end-to-end |
| `validate_all_edocs` | Run all eDoc fixtures through a dry-run pipeline and report issues |

## Attribute Types

Each customizable rule has a specific type and format:

| Attribute Name | Format | Purpose |
|----------------|--------|---------|
| `EXTRACTION_PATHS` | JSON | XPath expressions that map XML nodes to DocBits fields |
| `TRANSFORMATION` | XSLT | Stylesheet applied to the XML before extraction |
| `PREVIEW` | XSLT | Stylesheet that renders the human-readable PDF preview |
| `STRUCTURE_DESCRIPTOR` | JSON | Structure map for EDI documents only |

The `create_edoc_custom_attribute` tool infers the correct format from the attribute name automatically.

## Quick Start

### List what your org has customized

```
list_edoc_custom_attributes
  electronic_document_type: "XRECHNUNG 2.1 CII"
```

Returns two lists: `custom` (your org's overrides) and `default` (shared rules you inherit).

### Create a custom preview for XRechnung

```
create_edoc_custom_attribute
  electronic_document_type: "XRECHNUNG 2.1 CII"
  attribute_name: "PREVIEW"
  attribute_value: "<xsl:stylesheet ...>...</xsl:stylesheet>"
```

Returns the new `attribute_id` — save it for updates and deletion.

### Update an existing custom rule

```
update_edoc_custom_attribute
  attribute_id: "069cd17c-673c-7c94-8000-b512417eefe3"
  new_value: "<xsl:stylesheet ...>...</xsl:stylesheet>"
  activate: true
```

Creates a new version and activates it. The previous version is kept in history.

### Revert to the default

```
delete_edoc_custom_attribute
  attribute_id: "069cd17c-673c-7c94-8000-b512417eefe3"
```

Removes the custom override. The system falls back to the built-in default rule immediately.

## Safety Rules

| Action | Allowed |
|--------|---------|
| Read default rules | ✅ Yes |
| Create custom rule for your org | ✅ Yes |
| Update custom rule for your org | ✅ Yes |
| Delete custom rule for your org | ✅ Yes |
| Modify or delete default rules | ❌ **Never** — blocked at MCP layer |

Attempting to write to `00000000-0000-0000-0000-000000000000` returns:

```json
{
  "error": true,
  "blocked": true,
  "detail": "Writing to the default org is forbidden via MCP. Default rules are immutable and shared across all customers."
}
```
