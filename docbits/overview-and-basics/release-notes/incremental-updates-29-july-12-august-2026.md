# DocBits Release Notes — 29 July – 12 August 2026

_What changed in the DocBits production upgrade rolled out on 10–12 August
2026, covering everything since the 29 July release. Each service lists the
version that went live, then what's new or fixed in plain language. Services
not listed (Auto Accounting `1.21.1`, Ideas `0.3.1`, OCR `1.10.3`, Operator
`1.42.1`, PO Match `1.59.3`, FTP `1.32.4`) had no customer-facing changes._

---

## Highlights

- **FacturaE support.** Spanish FacturaE 3.1 e-invoices are classified and
  extracted out of the box, with full field mappings. In the same wave,
  ebInterface (Austria) mappings became version-true, Factur-X and ZUGFeRD
  defaults gained the company name path, and several wrong default mappings
  for discounts, VAT and unit prices were corrected.
- **Dashboard search and sorting repaired.** Sorting no longer depends on
  which columns happen to be visible, an OR filter combined with a range or
  equality no longer wipes out the search phrases, supplier names show in
  quick search again, and ISO-formatted dates are read correctly.
- **AI extraction corrects itself.** A provable net/total amount swap made by
  the AI is undone automatically, AI-scanned fields no longer come back wrong
  after a document restart, and AI table extraction processes documents in
  page batches so long tables arrive complete.
- **Workflows survive an auth hiccup.** A briefly unreachable auth service is
  retried instead of failing the run, and a workflow trigger that cannot
  authenticate reports the error instead of leaving the document stuck.
- **Hard-to-read PDFs extract again.** When the standard PDF text decoder
  cannot read a page (common with Ghostscript-produced files), extraction
  falls back to a second engine instead of returning nothing.
- **MFA works across regions.** Two-factor enrollment data is replicated
  between the EU and US regions, so a second factor set up in one region is
  honoured in the other.

---

## Web App — `10.49.4`

### Signing in and accounts

- Logging out in one browser tab logs the other tabs out too, without the
  error toasts that used to appear when tabs disagreed about the session.
- Changing your own password in the profile goes through the dedicated
  self-service endpoint, so it works without admin permissions.
- Passkey sign-in from the non-home region shows translated error messages,
  and its submit button is visible.

### Validation screen

- The "Extracted table" tab no longer spins forever when an AI table already
  exists.
- Documents whose barcode data is missing no longer break the barcode
  assignment view.
- M3 multi-tax lines offer the tax code as a dropdown fed from the list of
  values instead of a free-text field.
- Opening large supplier invoices is noticeably faster.

### Tasks

- Kanban columns page as you scroll, so boards with many tasks load quickly.
- The open-task counter in the sidebar counts tasks in your sub-organisation
  context, not the context of whichever document happens to be open.

### Workflow Builder

- The workflow list keeps your search, sort order, page and page size when you
  open a workflow and come back, including via the breadcrumb, and the page
  opens on the List tab by default.

### Settings and administration

- The Master Data page no longer comes up blank because of a sorting race, and
  sorting by badges doesn't crash the page anymore.
- A subscription in "cancelling" state can be resumed.
- The XSLT detail page reports load errors instead of showing nothing, and the
  e-mail notification settings use the full page width with a working logs
  pane.
- The organisation picker for multi-org users has correct row layout, sizing
  and theme colors, scrolls properly, and offers a filter for accounts with
  many organisations.
- Analytics: a failed metrics request shows an error state instead of
  rendering zeros, and the usage widgets report honestly when no measurement
  data is available.
- Obsolete cache options were removed from the cache management page, and the
  Users and Groups pages lost their nested double scrollbars.
- "Use Default Template" in the layout manager no longer crashes or sits dead;
  it also stops claiming that no default layout exists.
- Selection rules keep their text-match, presence and regex operators when a
  rule is reopened.
- Document Types support per-type transformation rules, and the rule list UI
  gained a fix-value action.
- Purchase order status badges map correctly for ERP-cased status values.
- DocNet (AI Workforce) screens including the Agent Wizard are translated, and
  the new/edit idea dialog scrolls horizontally.
- Supplier portal quotes: managed units of measure show in the line-item
  table, approval styling applies to contract quotes only, and the comparison
  line no longer appears when both values are identical.
- The error page's JSON fallback is readable in dark mode, and reports use a
  proper "last 7 days" label instead of a stray "7".

## API Service — `12.74.0`

### Dashboard and search

- Sorting works regardless of which columns are visible, and a keyword the
  search delegates to full-text no longer leaves a broken SQL fragment behind.
- Supplier names appear in quick search again for organisations without
  full-text indexing.
- ISO-formatted dates (2026-08-12) are no longer misread by the day-first
  date normaliser.
- Dashboard exports route bare text values such as invoice numbers to the
  right column.

### E-invoices

- FacturaE 3.1 (Spain): classification rule and complete field mappings.
- XRechnung classification rules are anchored to their syntax family, so a
  UBL document is no longer matched by CII rules and vice versa.
- The accepted version "3.0" covers its whole patch family (3.0.1, 3.0.2).
- CII invoices take the supplier's legal name, using the trading name only as
  fallback.
- ebInterface (Austria) mappings are version-true, with a corrected catch-all
  and rebuilt fixtures.
- Factur-X and ZUGFeRD defaults gained the company name extraction path, and
  default header transforms for tax rate, invoice type and tier-3 fields were
  fixed, along with family-wide discount, VAT and unit-price semantics.
- Source tax category codes are no longer mapped blindly onto your ERP codes.
- Documents that mention both "invoice" and "credit note" prefer the credit
  note classification.

### Documents and extraction

- When the standard PDF decoder cannot read a page's embedded text, extraction
  falls back to a second engine, so affected PDFs extract instead of coming
  back empty.
- The barcode master switch is now `BARCODE_EXTRACTION`; the old QR-code
  setting keeps working as an alias.
- A memory leak in the background scheduler was plugged; it slowly degraded
  processing over days of uptime.
- Suppliers imported without a country stay blank instead of defaulting to
  Germany.

### Export and master data

- Save Rules reports failure when it writes nothing, instead of claiming
  success.
- Zero-amount lines are no longer dropped from auto-accounting exports, and a
  filter that matched every bucket was fixed.
- M3 exports support additional-info post-hooks.
- One failing dataset probe no longer blanks the whole Master Data screen.
- PO caches are invalidated when the ERP updates a purchase order's status, so
  the dashboard stops showing the stale state.

### Administration

- Each preference shows which user last changed it.
- Extraction rules can be deleted by supplier and cloned via new endpoints.
- Status-alert e-mail recipients are compared NULL-safely, fixing a crash in
  notification delivery.

## Auth Service — `1.75.9`

- An organisation API key used against an unrelated organisation is rejected.
- Creating an organisation returned an error while actually saving the row;
  it responds correctly now.
- Signing in with a passkey when none is enrolled returns its own error code,
  so the login screen can say what's wrong.

## Auth Bridge Service — `0.4.2`

- Two-factor enrollment tables are replicated between the EU and US regions,
  and rows are identified by their real primary key.

## Docflow Service — `2.8.7`

- A workflow trigger that cannot authenticate reports the failure instead of
  leaving the document stuck, and a briefly unreachable auth service is
  retried rather than treated as a bad token.
- Quote comparison cards: item numbers are compared only for lines the item
  price matrix describes, lines without a unit of measure or without a price
  are skipped instead of failing the comparison.
- The contracted-price comparison card gained an any/all operator option, and
  card caches are invalidated correctly after migrations and code updates.
- Dropped SSL connections are treated as transient and retried instead of
  failing the run.

## Docnet Service — `1.56.4`

- Health and version endpoints no longer block on live checks, which used to
  make the Service Versions dialog hang.

## Email Service — `1.40.6`

- When an inbound e-mail is skipped, the reason is shown in the import event
  row instead of being silent.
- Attached `.eml` container files are no longer imported as documents.
- A failed Microsoft Office sign-in produces a readable error message, and a
  transport error from the AI service counts as "unclear" rather than a
  rejection.

## Extraction Service — `1.53.8`

- A provable net/total amount swap made by the AI is undone after field
  extraction, and guard failures are logged instead of passing silently.
- AI-scanned fields no longer come back wrong after a document restart.
- AI table extraction batches by pages and accumulates all batches, so long
  tables arrive complete.
- Documents mentioning both "invoice" and "credit note" prefer the credit
  note classification.
- Repeated header/footer cleaning is cached, which speeds up extraction on
  multi-page documents.

## Fulltext Service — `1.41.7`

- An OR filter combined with a range or equality condition no longer erases
  the search phrases.
- Sorting uses the correct index paths and surfaces the real reason when the
  search backend rejects a query; a sort regression that broke raw-query
  search entirely was fixed the same week it appeared.
- Document lookups work on older text-mapped indices.
- The token cache is scoped to the token and organisation pair, so switching
  organisations cannot serve results under the previous context.
