# MCP configuration guide evidence

Reviewed on 2026-10-18. The guide is translated into all nine documentation languages and linked from MCP, eDocs and country-overview navigation.

- `source-review.json`: reviewed implementation commit, file hashes and actual tool argument signatures. This is source verification, not a deployment capability probe.
- `validation.json`: Markdown structure, navigation titles, new/rewritten local links, genuine screenshot references and 107 JSON examples checked against the implementation signatures.
- `source-branches.json`: exact source-branch/main-folder parity for all changed translated files.

Connection examples use EU sandbox and explicit browser OAuth login. Codex guidance was checked against the fetched official MCP documentation at https://developers.openai.com/codex/mcp and installed CLI help. Claude add/login commands were checked with installed CLI help; the official Claude documentation fetch returned HTTP 403.

Corrected the old XSLT-preview examples to `attribute_id`, `candidate_value`, `doc_id`. Distinguished active-config dry runs from candidate previews and inactive drafts. Documented immediately active first custom versions, explicit `activate: false` for updates, value IDs for activation/rollback, Extraction Paths-only comparison, generic settings preview/confirm/undo and the UI fallback.

The guide reuses existing genuine development screenshots and links the localized UI video. No new recording, live configuration change, document restart, approval, ERP export, or end-to-end acceptance test was performed for this addition. Ticket evidence remains an investigation of a likely organization-configuration cause, not proof of a product regression or completed fix.
