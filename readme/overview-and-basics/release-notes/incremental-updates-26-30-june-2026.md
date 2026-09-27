# Hotfixes 26–30 June 2026

_What this prod upgrade delivered, in plain language. Each service shows the
version now live on production. Services not listed had no customer-facing changes
in this window._

---

## Highlights

- **One connection for AI assistants ([DocBits MCP](https://docs.docbits.com/advanced-functions-and-tools/docbits-mcp)).** A single, unified gateway now
  serves all DocBits tools — including DocFlow — through the main API, so AI
  assistants (Claude, Gemini CLI, Codex) connect through one reliable endpoint
  instead of several.
- **Smarter multilingual dashboard search.** Search connectors (**AND / OR**) now
  appear in your language with colour highlighting, invoice sub-types offer a value
  dropdown, and search-syntax messages are localised — with smoother keyboard
  handling throughout.
- **Smoother approvals & permissions.** Approval is no longer triggered when the
  packaging unit from an order confirmation is empty, normal users can approve
  costing elements again after the access-control migration, and document-level
  permissions apply correctly even when a table column already exists.
- **The app updates itself.** When a new version ships, DocBits now refreshes
  automatically instead of interrupting you with a "Refresh Now" popup.
- **More robust purchase-order matching.** Column value transforms, crash guards
  for lines missing a price or quantity, and automatic retry on dropped database
  connections make matching steadier.
- **Fewer errors across the board.** Many rare server errors on dashboards,
  supplier invoices, PO records and OCR jobs were tracked down and fixed.

---

## Web App — live: `10.34.4`

- **Dashboard quick search:** localised **AND / OR** connectors (de/fr) with
  colour syntax highlighting; invoice sub-type value dropdown; localised
  search-syntax error messages; smoother keyboard experience; the
  "full-text required" warning now renders inline so the layout no longer jumps.
- **Approvals & permissions:** fixed approval wrongly triggered when the packaging
  unit from an order confirmation is empty; normal users can approve costing
  elements again after the access-control migration; document-level permissions now
  apply when a table column already exists.
- **Auto-update:** the app refreshes automatically on a new version instead of
  showing a "Refresh Now" popup; removed the old version-info dialog.
- **Inbound e-mail settings:** new failure-notification recipients toggle and
  field; the import log now shows outbound activity and the failure reason; the
  inbound address copies reliably.
- **Document split:** the Document Split screen now scrolls.
- **Dark mode:** fixes for table extraction, the task counter, and closed-document
  markers on the dashboard.
- **Usability & stability:** dashboard export UI fixes; sticky table headers no
  longer bleed through dialogs; the DocNet dashboard no longer crashes on a failed
  stats request; field scripts no longer revert emptied fields back to their old
  values; PO settings checkboxes and layout fixes; classify-list display fixes.
- **Suppliers:** supplier organisations can now register via magic link.

## API Service — live: `12.46.8`

- **DocBits MCP gateway:** a unified gateway now proxies DocFlow tools through the
  main API, so AI assistants reach every DocBits tool through one endpoint; the MCP
  endpoint is served without a redirect that could break connections.
- **Accounting:** cost-center validation added for the accounting ID.
- **OCR routing:** documents are sent for a full re-OCR when supplier e-text is
  turned off, so text stays reliable.
- **Infor ERP / SAP:** additional charges route correctly when the ERP already
  holds the charge at a zero amount.
- **Reliability (fewer server errors):** hardened dashboard, supplier-invoice,
  PO-record and task-manager queries so they no longer return rare 500 errors;
  more resilient organisation-cache synchronisation and stored-file cleanup.
- **Cleaner dashboard filters:** removed the redundant invoice-number filter field;
  corrected PO-matched quantity.
- **Developer API docs:** the Swagger UI now offers a spec dropdown (OpenAPI 3.0
  plus the Infor Swagger 2.0 view) with DocBits branding.

## Auth Service — live: `1.68.0`

- **Faster sign-out / token revocation:** bulk token revoke no longer runs for
  minutes and drops the connection.
- **Fixed set-password e-mails** so they render correctly.
- **Suppliers:** supplier organisations can register with a magic link.
- **Sign-in stability:** a member is no longer locked out on a transient
  organisation-lookup miss, and an invalid organisation id now returns a clean
  message instead of an error.

## Docflow Service — live: `2.4.1`

- **Reliable AI gateway:** fixed hangs and timeouts on the DocFlow MCP endpoint
  (handshake, client disconnects, duplicate responses) — the DocFlow side of the
  unified DocBits MCP gateway.

## OCR Service — live: `1.7.1`

- **Steadier OCR processing:** background reply queues expire automatically and
  transient connection failures are retried, so fewer OCR jobs get stuck.

## PO Match Service — live: `1.55.7`

- **Value transforms** are now applied on item-id, unit-code and static-value
  columns during rule matching.
- **Crash guards:** a line missing a price or quantity, an unusual weighted-key
  combination, or an impossible division no longer crash matching.
- **Reliability:** database writes retry automatically on dropped or SSL-closed
  connections.
- **Infor ERP / SAP:** additional charges route correctly when the ERP holds the
  charge at a zero amount.

## Fulltext Service — live: `1.35.6`

- **Faster re-indexing:** all synchronisation phases now fan out so autoscaling
  kicks in, fixing slow serial re-indexing and a stuck 0% progress widget.
- **Steadier statistics:** cross-region document-stats requests are bounded so they
  no longer time out.

---

## No customer-facing changes in this window

Stable, no notable product changes between 26–30 June: Auto Accounting (`1.18.6`),
Barcode (`1.15.6`), Docnet (`1.54.6`), Email (`1.36.4`), Extraction (`1.48.7`),
FTP (`1.30.1`), Operator (`1.39.5`). Auto Accounting and FTP received internal
maintenance only.

<!-- Generated by the docbits-changelog skill (prod-delta mode). Versions read live
     from prod (do-fra1-polydocs/prod); window 2026-06-26 → 2026-06-30. -->
