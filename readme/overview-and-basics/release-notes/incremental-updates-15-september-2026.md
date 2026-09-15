# DocBits Release Notes — 15 September 2026

_What changes in the DocBits production hotfix on 15 September 2026 (release
R1.0.13), covering everything since the 1 September release. Each service lists
the version being deployed, then what's new or fixed in plain language. Services
not listed had no customer-facing changes._

---

## Highlights

- **One set of rules for the dashboard search.** `field=value` is now exactly
  this value on every search engine, `field:value` means contains (with `value*`
  and `*value` for starts-with and ends-with), and `field!=value` also returns
  documents that have no value at all. A search without a chip is a substring
  search across every field, business identifiers included. Result count and
  result list describe the same set of documents, and a search that hit the
  result window or ran without the full-text index says so instead of reporting
  "complete". The dashboard's own search connection (WebSocket) never reached
  the full-text index before; it does now.
- **Suppliers are recognised more often.** When one lookup field (tax id,
  IBAN, supplier number) matches exactly one supplier, that supplier is used
  even if a broad field such as the name matches several. XRechnung CII and
  Facturae documents carry their supplier fields again. Where master data
  replaced an extracted value, the validation screen says so and lets you
  restore the original.
- **Purchase order matching explains itself.** The screen says why there is no
  match and why a match was not kept, matching history lists the
  transformation rules that ran, and PO unit prices are derived from the net
  amount. Manual matches work again for organisations without a fallback rule,
  and a killed matching task marks the document as failed instead of parking
  it in "Queue" forever.
- **Stuck documents and false errors.** Organisations that upload continuously
  had documents demoted to a queue priority that was never served during
  business hours (866 documents stuck in "new" at one customer). A retry
  sweeper could overwrite a successfully exported document with "error" hours
  later and fire the export-error mail for it. That path is closed.
- **Touchless Intelligence.** The Analytics tab that measures how many
  documents pass through DocBits without a human touch gets its full first
  release: issue clusters with AI advice, bulk analysis, change proposals with
  preview, apply and undo, a per-supplier AI diagnosis, and a pipeline-flow
  diagram per document.
- **Faster where data is large.** The accounting dropdown works for
  organisations with more than 2,000 accounts, the E-Documents rules page
  pages its 1,600 rules on the server instead of freezing the browser, and
  Refresh on the purchase order dashboard returns fresh data instead of a
  cached list.
- **Security.** Frontend source maps stop shipping with every deploy,
  master-data lookup filters are bound as SQL parameters instead of
  interpolated, an expired token is rejected even on a cache hit, and the
  organisation guard on the processing token is enforced independently of the
  layer in front of it.

---

## Web App — `10.66.3`

### Signing in and accounts

- The "Updating DocBits v10.59.3.1 → v10.59.3.1" overlay that reloaded forever
  on sandbox is fixed. A same-version reload no longer shows the overlay, the
  loop is bounded per tab, and a banner offers manual recovery if it happens
  again.
- The System Admin checkbox can be ticked on an existing user. Creating a
  system admin from the frontend now has an effect; a sync job used to reset
  the flag on every run.

### Dashboard and search

- New operator rules, also described in the search help popup: `=` is exactly
  this value (case-insensitive), `:` is contains, `: value*` starts with,
  `: *value` ends with, `!=` is everything that is not exactly this value
  including documents without a value. Quotes only group a value with spaces.
- A quoted phrase such as `"Johnson and Johnson"` is searched as one phrase.
  "and" and "or" inside quotes are no longer read as connectors.
- When a bare search finds nothing, the dashboard explains the rule and offers
  one-click chips (`Invoice number : <term>`, `Purchase order : <term>`,
  `Supplier ID : <term>`).
- A search with zero results resets the pager. Before, the pagination kept the
  previous search's count.
- Requisition numbers and requisitioners are found by a plain search, without
  a chip.

### Validation screen

- Values that master data replaced are marked. An amber badge shows the
  original and the current value, the dataset and how it matched, and a button
  restores the extracted value. Values confirmed by master data or filled from
  the purchase order get their own labels. Before, all of them carried the
  "Extracted using saved rules" badge.
- The approval stamp is saved even when the page already carries another
  annotation. Downloaded annotated documents were missing the stamp in that
  case.
- "Hide non mapped columns" keeps columns you trained by hand (for example Item
  Number and Purchase Order).
- Saving extraction rules works after you type a page number and then draw a
  box for a field. That sequence used to crash the save.
- Train Model runs in the background. The screen shows "training started",
  polls for the result and reports success or failure. Large organisations
  used to get a gateway error while training carried on server-side.
- Dark mode: the scissors cursor on the split screen and the mode toggle on the
  Auto Accounting screen are readable again.

### Purchase order matching

The changes announced in [Hotfixes 8 September 2026](incremental-updates-8-september-2026.md)
reach production with this release: the match survives saving, matching runs
again when the PO number is corrected, the screen says why there is no match
and why a match was not kept, matching history shows the transformation rules,
and the PO unit price is calculated from the net amount. In addition:

- The Auto Match button also exports the document when "PO Auto Match and
  Export" is on. Before, the export only happened when the document was opened
  from the dashboard via "PO Match".
- The quantity/unit price tolerance popup stays open when the server rejects the
  save, so the entered values are not lost.
- The purchase order dashboard's Refresh button clears the server-side cache
  before reloading. A purchase order imported from the ERP appeared only after
  seven to eight minutes.

### Auto accounting

- Organisations with more than 2,000 accounts search the account list on the
  server. The dropdown was empty on sandbox for such organisations, and page
  loads took five seconds.
- Accounts referenced by a document are resolved in batches: a 100-line
  document with two splits per line needs 4 requests instead of 403.
- The Auto Accounting and PO tables headings follow the label set in the layout
  builder instead of a hard-coded text.

### Settings

- Settings → E-Documents → Rules pages, searches and sorts the 1,600-rule
  catalogue on the server. The tab used to render every rule at once and
  freeze the browser. "Reset all" is one call instead of one per rule.
- Document type Advanced Settings show the stored state of each toggle. A saved
  `false`, a `0` tolerance or an empty select were being replaced by the
  default, and switching document types left the previous type's values
  behind.
- Transformation rules: a "Set value" action saves. The editor sent it under a
  name the server rejects.
- The document sub types link is shown on standard document types.
- The SMB export's JPL mapping downloads as `.properties`, so the file can be
  uploaded again. It was named `.xml` and rejected on the way back in.

### Workflows

- Renaming a workflow keeps the card changes made in the same session. New
  workflows are created in one save request, and template renames are
  persisted.
- An exported workflow file contains the whole export envelope (version, name,
  description). Advanced workflows can be imported again; before, the file lost
  its version and was read back as a standard workflow and rejected.
- Column filters on the workflow list combine with AND. With a name and a date
  filter active, rows matching only the name slipped into the result.
- Task deadlines use the date format from your user settings in the list, the
  board and the detail view.

### Analytics: Touchless Intelligence

The Touchless tab (Analytics → Touchless) measures how many documents run
through DocBits without a person touching them, and why the others did not.
This release completes it:

- **Issue clusters with evidence.** Documents that needed a touch are grouped
  by cause. Each cluster card names the fields, validation codes and error
  messages it fails on, and its supplier, or says there is none. Clusters that
  DocBits can fix (a rule, a field setting) are separated from those only the
  supplier can fix, and the AI analysis budget goes to the fixable ones first.
- **AI analysis, labelled as such.** A cluster card says whether a language
  model wrote the advice or a rule did, what the analysis counted and when it
  stopped being true, and whether a click will reuse a cached analysis. If the
  AI advisor cannot run in this environment, the tab says why.
- **Bulk analysis.** Analyse many clusters in one run, see cluster by cluster
  what the run is doing, and find the results afterwards. The result list
  survives navigation and reload, and the run no longer hangs on "Running · 0/6
  done" in a sub-organisation view.
- **Change proposals.** A recommendation becomes something you can act on: a
  proposal that targets the field that blocks the documents, a preview that
  shows what it would do (nothing is saved), apply, measured effect, and undo.
  Agents reach the same steps through MCP tools. Fix steps deep-link to the
  settings page they name, pre-filtered by document type, field or rule.
- **Supplier diagnosis.** The supplier page explains an empty state instead of
  showing zeros, and offers a per-supplier AI diagnosis. Up to five suppliers
  can be picked and compared side by side.
- **Pipeline flow.** A diagram per document and per cluster shows the path
  through intake, classification, e-document check, supplier, OCR, extraction,
  validation, PO matching, approval and export, with the stage that stopped it.
- **Purchase order matching reasons.** The matching decision is traced per
  document (stage, pass, rule, column) and condensed into the Touchless result.
  Reason codes distinguish "purchase order not found" from "line mismatch" and
  "required field missing", and the advisor's tolerance proposals target the
  rule engine that decides.
- **Correct numbers.** KPI tiles respect the sub-organisation filter and count
  only documents the drill-down can list.

### DocNet

- The Activities feed, the Recent Activity widget and the mission timeline are
  translated. Audit summaries were English in all 22 languages.
- Agents see fields the document type defines but extraction left empty. They
  used to conclude such fields did not exist and skip mandated updates without
  attempting a write.

### Security

- Frontend source maps are stripped from every deploy. Every environment
  served them, production included.

---

## API Service — `12.83.156`

### Supplier recognition and master data

- A supplier is identified when one lookup field is unique. With several
  searchable fields, the results were combined as a union, so a broad name
  match with four suppliers drowned out a tax id that matched exactly one.
  Fields that match nothing no longer veto the fields that did. See
  [Master Data Settings](../../administration-and-setup/settings/global-settings/document-types/fields/master-data-settings.md)
  for how the fields work together.
- Master-data replacements are recorded with their origin: dataset,
  configuration, source field, operator and match kind. The validation screen
  shows this and can restore the extracted value.
- Cash Discount Term is imported from the supplier BOD; ERP-synced suppliers
  had it empty. A Discount Term Overwrite entered as the full code ("143",
  "012", "X08") is applied; only the percent prefix was consulted before.
- Master data lookups are capped at 1,000 rows per page and pivot in SQL. A
  19,000-record lookup took five seconds per call and blocked the API.
- Filter property names and data types in the master-data lookup are bound as
  SQL parameters. They were interpolated into the query.

### Document processing

- Documents from an organisation that uploads continuously were demoted to
  priority 9, which the queue only serves when every higher priority is empty.
  The demotion is now capped at 3. The reconciler that should re-queue stuck
  documents had no working credentials in production; it does now.
- A finished, exported document is never overwritten with "error". A workflow
  flag that was never cleared kept the retry sweeper picking up a successfully
  exported document once a minute until the retry limit stamped it "error" and
  fired the customer's export-error mail, 2 h 17 min after the export.
- Merging and appending accepts `.PDF` and `.Pdf` files. Scanner output named
  `SCAN0001.PDF` was rejected with "Only PDF files are allowed."
- Cache invalidation scans the key space once instead of twice and only clears
  the lookup data types a BOD changed. Every BOD used to wipe the whole lookup
  cache for the organisation, blocking the API while it walked everyone's keys.
- Model retraining runs as a background task and returns immediately with a
  status the UI polls.
- A processing token from another organisation is rejected independently of
  the sub-organisation membership check in front of it.
- The user sync leaves the system-user flag alone instead of resetting it on
  every run.

### Export

- M3 receipt lines pair the exported unit price with the invoice line's own
  price basis. The price travelled with the PO line's divisor and the ERP
  repriced the line at 1,000 times the invoiced amount.
- A table export survives a line whose purchase order has been removed; the
  line is exported without a price basis.

### E-documents

- XRechnung CII invoices whose due payable amount is 0.00 because a prepaid
  amount offsets the total show the grand total (BT-112) as total amount. The
  customer saw "total amount 0,00".
- XRechnung CII and Facturae documents deliver their supplier fields again.
  Stale organisation-level overrides were shadowing the correct default
  mapping, so supplier recognition could never match.
- The validation rules catalogue is paged, searched and sorted on the server,
  with facets for the filter bar.

### Classification

- Swiss documents are classified `de_CH`, `fr_CH` or `it_CH` from their content
  (CHF amounts, CHE VAT numbers, CH IBAN). The locale was taken from the
  organisation default and Swiss documents got `de_DE`.

### Dashboard search

- One operator semantics on Postgres and ClickHouse: `=` exact, `:` contains
  with edge wildcards, `!=` complement including empty values. On Postgres, `=`
  used to be a prefix match, so `invoice_id=911892112` also returned
  911892112333.
- A bare search is a substring search over every field, business identifiers
  included. A hyphenated identifier such as `2026-003` is one literal, and the
  clause type no longer changes after the fifth character.
- The invoice number chip is exact on Postgres, as it already was on the
  index. Leading zeros, float forms and case are treated the same in free text
  and in chips.
- The dashboard's WebSocket search carries the caller's credential to the
  full-text service. Every delegation was refused before, so the dashboard
  silently searched Postgres alone and presented the answer as complete.
- Result count and result list run on one set of predicates. The count used to
  be a Postgres approximation while the list came from the index.
- Vector search caps at the real result window and reports the cap instead of
  showing "(50)" as an exact total.
- A search that ran without the full-text index (index minutes behind,
  capability lookup failed, degraded field resolution) reports its window
  status instead of "complete".
- Document scripts that call the full-text search authenticate correctly and
  surface failures instead of returning an empty result.

### Purchase order matching (in-process matcher)

For organisations that match in the API rather than in the PO Match Service:
a corrected PO number is matched in the save that corrects it.

### Analytics

- Touchless: all backend changes behind the Web App section above, including
  stage evidence recorded by each pipeline stage, the PO-match trace, change
  proposals with preview, apply and revert, and bulk status in one call per
  tick.

---

## PO Match Service — `1.59.34`

- A PO line's unit price is derived from its net amount, not its taxed total,
  and a document's PO snapshot re-derives its unit prices at match time.
- The service records where each PO number candidate came from and which
  numbers a run looked up. A document's own invoice number is never a PO
  candidate. A dropped match leaves its reason on the document for the screen.
- Manual matching works for organisations whose rules carry no `is_fallback`
  flag. Users picked lines, pressed match, and nothing came back.
- No more documents orphaned in "Queue": database statement timeouts,
  keepalives and an explicit soft-time-limit handler mark the task as failed
  instead of relying on a kill that left no trace.
- Tolerance changes are read per matching request, so a tolerance saved a
  moment ago is used by the next match.
- The five-stage decision trace is persisted per document for Touchless.

---

## Auth Service — `1.78.27`

- Token expiry is enforced on cache hits. A cached entry could authenticate for
  up to nine hours after the token expired.
- Token verification stops writing an unchanged `org_id` back to the user row
  on every request, which produced an UPDATE per call.
- A memory leak that drove the autoscaler to maximum replicas is fixed, and
  the service is back to two workers.
- The system-user flag can be changed on an existing user when no other member
  holds it.

---

## Auth Bridge Service — `0.5.7`

- When the EU ↔ US replication stream dies, the replication slot is reattached
  in place instead of rebuilding the bridge and re-running the full startup
  reconcile, during which the slot sat inactive.

---

## Extraction Service — `1.55.33`

- AI table extraction: amount columns are typed as numbers with a description,
  and fabricated non-numeric values in amount columns (a "St." copied from the
  neighbouring cell into unit price per) are dropped instead of stored.
- US invoices: sub-cent float noise no longer decides between candidate
  net/tax pairs (268.28 + 22.13 was losing to net = total, tax = 0).

---

## Fulltext Service — `1.42.35`

- The search-result cache is on in every environment; production, sandbox and
  stage had been running without it since the active env files were created.
  Upload and deletion invalidate it, so a search after an upload sees the new
  document.
- A plain search for a bare invoice number returns the exact-match invoice.
  Written currency values, legacy boolean mappings, dates and tax flags survive
  the slim index rebuild, and index entries without fields are detected and
  recovered from extraction.
- Exact `=` on a dynamic text field compares the whole value only. A wildcard
  on the analysed path made `note_field=53173` match "PO 53173 / 2024".
- A bare hyphenated identifier such as `2026-003` is one literal, not a bag of
  tokens.
- Read paths stop creating the index they read, and every zero-hit answer
  carries a window status and reason.
- The vector search's service-side limit of 50 is gone.

---

## Docflow Service — `2.10.11`

- Advanced workflow imports are gated on the organisation's entitlement, and a
  batch is checked before anything is written. An organisation without the
  advanced module could import an advanced workflow it then had no way to open.
- A workflow rename rides the save, and template renames are persisted.

---

## Docnet Service — `1.56.12`

- Field discovery returns every header field the layout defines, populated or
  not, and matches what the write guard checks. Agents skipped mandated field
  updates because empty fields looked absent.
- Identities are cached under the same organisation-scoped key the API uses,
  so the organisation API-key boundary holds across both services.

---

## Email Service — `1.41.6`

- Shared Office 365 mailboxes with more than ten subfolders resolve every
  folder. Microsoft Graph pages folders ten at a time; the 11th and later
  configurations failed every poll with "unable to find the selected Folder".

---

## FTP Service — `1.32.18`

- The SFTP scheduler starts in each worker process instead of before the fork.
  Periodic SFTP imports were silently failing with a corrupted scheduler
  state, while a fresh process worked fine.

---

## Auto Accounting `1.21.7`, Barcode `1.18.14`, OCR `1.10.11`, Operator `1.42.12`, Ideas `0.3.6`

Build and deployment changes only (base image update, CI credentials). No
change in behaviour.

<!-- Release R1.0.13. Announced: tickets with Jira "Release No." = R1.0.13 and a
     status on sandbox or beyond, plus DOCB-14454, DOCB-14450, DOCB-14415,
     DOCB-14419, DOCB-14431, DOCB-14045/46 (no Release No., on sandbox).
     Held back (Release No. R1.1): DRFS-778, DRFS-712, MEF-165, MEF-166, DOCB-14389.
     Labelled R1.0.12 but code ships now: DRFS-746/748/749/750/751, DOCB-14282. -->
