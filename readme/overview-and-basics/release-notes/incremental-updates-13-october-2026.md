# DocBits Release Notes — 13 October 2026

_What changes in the DocBits production hotfix on 13 October 2026 (release
R1.0.15), covering everything since the [15 September hotfix](incremental-updates-15-september-2026.md).
Each service lists the version being deployed, then what's new or fixed in
plain language. Services not listed had no customer-facing changes._

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/release-notes/2026-10-13/en.mp4" %}

---

## Highlights

- **The Settings Assistant.** A chat bar on every settings page answers
  questions about your organisation's setup, in your language and from the
  DocBits documentation. It reads the current state of your settings and
  explains them (group permissions, import channels, purchase order switches,
  accounting). When you ask it to switch something on or off, it shows a
  preview first, waits for your confirmation, and offers an undo. "Open
  setting" jumps straight to the setting, even inside a collapsed section, and
  highlights it. Organisation admins turn the assistant on or off on Company
  Information. It only answers DocBits questions and never changes anything
  without confirmation.
- **New AI tiers.** The Fast and Full tiers run on new models. A new Auto tier
  picks Fast or Full per document, and Nexus Flash joins Nexus. A vision mode
  (hybrid or auto) decides when the page image is sent along. Stored AI model
  preferences move to the new tiers on their own, and screens show tier names
  only. "Use AI" is a dropdown (Standard, Yes, No) with a preview of what
  structured extraction will request.
- **Header field check.** The validation screen has a "Header field check"
  button next to Save. Its report lists every header field with where the value
  came from (AI, rule, script or master data), a compact table with source
  filter, search and sorting, and the same field labels as the validation
  screen. The origin popup shows the source of each value in one strip.
- **Sign-in and organisation security.** An MFA challenge can be used once on
  every sign-in path, and enrolling an authenticator needs the e-mail code.
  Organisations own a list of verified e-mail domains; a social login (for
  example Microsoft) joins the organisation that lists the domain and never
  creates an organisation, user or subscription by itself. Only organisation
  admins change organisation preferences and write or approve purchase order
  match rules. Cached answers can no longer leak across organisations.
- **Purchase order matching and charges.** Charges the purchase order expects
  as zero get an absolute floor, charge tolerance also applies to charges the
  order does not budget, and one field can list several costing elements whose
  amounts are split in proportion to the purchase order. A match column can
  carry an "allow mismatch" flag. Workflow cards compare charges per list, and
  the workflow execution limit rises from 30 to 50.
- **Fewer wrong numbers.** Amounts show in each user's personal format
  (Switzerland and Slovenia included), date-only values keep their calendar day
  in every timezone, the US total equation accounts for additional amounts and
  multi-tax invoices, and documents with 0.00 header amounts no longer fall
  into the wrong candidate pass.

---

## Also fixed in this release

- The dashboard no longer stays empty when a race sets the sub-organisation
  filter to the organisation id and thereby excludes every document.
- Dimension values can be selected again for every user.
- A customer-reported upload error is fixed.
- "Match on total" works for suppliers whose invoice has a single line, and
  for the supplier setups reported in DRFS-708 and DRFS-820.
- SPS e-documents: the 810 charges are adjusted, the 855 charges layout is
  updated, and the customer logo in the e-document preview is corrected.

---

## Web App — `10.78.9.4`

**Settings Assistant**
- A right-side chat drawer with a toggle sits on all settings pages. The
  conversation survives page changes, is capped at 20 messages, and shows the
  changes it applied with an undo.
- Greets you with questions that fit the current settings page and shows
  setting cards with an on/off switch. Esc closes menus first, Stop aborts a
  running answer, and screenshots in answers open in a lightbox.
- Applying a change opens a dialog with preview, confirm and undo.
- Every setting is searchable from the sidebar, and the found setting is
  highlighted in a different colour. "Open setting" scrolls to the target
  inside a collapsed accordion.
- An organisation admin switch for the assistant sits on Company Information.
- AI advice is attributed to Nova, and only tier names appear, never model ids.

**Validation screen and document handling**
- New "Header field check" button with report, per-field origin and help page
  (see Highlights). Source labels and status chips stay inside their cells.
- The "from master data" text badges next to field labels are gone; the origin
  popup carries that information.
- One shared field validation runs everywhere, which removes the generic "One
  or more fields need validation" error after Auto Accounting.
- Tooltips on the field popup buttons (Delete, Clear, Confirm) say what each
  does before you click.
- An optimistic row now shows what was stored, not what was typed. A column
  remap asks for confirmation only when a visible column loses its mapping.
- Pages past the OCR page limit are read-only and marked, in the Auto
  Accounting viewer too. The old import page-restriction panel is retired.
- A PO table appears for every purchase order number in a multi-PO header
  field, and the Layout Builder labels PO tabs from the PO table key and no
  longer reports the module as disabled when the PO table is on.
- The proposal card prints the tolerance instead of `[object Object]`, and the
  Approval compare screen stops rounding configured comparison columns (item
  numbers).

**Accounts, settings and errors**
- Every error toast and login error shows the trace id of the failed request,
  so support can find it. Dashboard WebSocket errors reject exactly the request
  they name.
- Company Information lists the organisation's e-mail domains.
- Admins can re-send the "Set your password" e-mail from the user page.
- Global admins set the contract start in the subscription table.
- Org admins see the Executive Dashboard tab and the XSLT add and delete
  buttons. Members save layouts as their own preference.
- A session without an organisation gets a clear error and the organisation
  picker instead of an empty dashboard.
- Amounts follow the user's personal number format, and date-only values keep
  their day in every timezone.
- Master data sends sub-organisation ids only when they differ from the
  organisation id, and custom master data headers go out as headers.
- The Tables mask no longer clips the "Use AI" dropdown, the AI hint text no
  longer covers the training line, and the AI table keeps its direct Apply
  button, with an icon-only header check and a licence message.
- Table extraction icons render again after the old icon font was removed.

**Tasks board**
- The board loads its first page with fewer duplicate requests, Enter runs the
  search at once, late answers are matched to the right search, the footer shows
  the real hit count instead of the page capacity, and a delete started in one
  organisation is cancelled before it is sent when you switch organisation.

---

## API Service — `12.83.293`

**Settings Assistant and MCP**
- Chat endpoint with guardrails: only DocBits questions, no change without
  confirmation, unclear or meta questions get help instead of a refusal, and
  answers stream cards first, then text.
- Read-only building blocks for every settings area (group permissions, import
  channels, PO matching, accounting, e-mail domains), a catalogue of deep links
  with a find-setting tool, and doc search with images from the DocBits docs.
- Wave 1 apply flow: preview, confirm and undo for supported settings, one
  scope rule for all three, safe against double confirmation and expiry.
- MCP tools never read files from the server in remote mode, and fixture and
  lab tools run on dev only.

**AI**
- New models behind the Fast and Full tiers, the Auto tier, Nexus Flash and
  the vision mode preference. Stored `AI_MODEL` preferences are moved to the
  new tiers.
- "Use AI" documents what structured extraction requests.

**Security and isolation**
- Only organisation admins change organisation preferences.
- The `/accounting/rebuild` call trains only the caller's organisation, fails
  closed on a failed organisation lookup and answers 400 for a bad id.
- XSLT, XML and PDF rendering deny file and network access, resolve no
  external includes, and invoice bytes are sanitised before they reach the
  transformer. Rendered PDF previews allow trusted image hosts only.
- Cache keys carry the organisation and the same identifier always gives the
  same key, so a foreign organisation id can no longer read cached data. Org-wide
  dashboard cache clears on every document change are gone.
- The organisation's e-mail domain list passes through to Auth.

**Purchase order matching and export**
- A field can list several costing elements whose amounts are split in
  proportion to the PO.
- Approval substitutes link to the active approval request, healed-approval
  saves no longer block, and a document pending approval is refused for export.
- PDF/A annotation keeps catalog and embedded XML, so e-invoices keep their XML
  after annotation. UBL invoices with the bare EN 16931 CustomizationID are
  classified (ecosio).
- GRPR rounds to the 6 decimals M3 accepts. Base unit of measure conversion factors are added to
  the frozen line.
- Soft-deleted trainings and formatting rules are respected, and MCP
  `update_document_fields` no longer confirms a write it lost. `get_table_rules`
  answers a typed miss, and an empty translations payload uses its fall-back.
- Slovenian amounts use `sl_SI` and saved preferences are migrated. Custom
  classification labels sent as UUID ids resolve. Shared dashboards keep
  `created_by` and the share list on update.
- Dashboard error frames carry the request's `request_id`, and every failed
  JSON answer carries a trace id.
- The system restarts only unhealthy workers instead of the whole API fleet
  and checks the registered task list correctly. The hang monitor queue is
  consumed again.

---

## Auth Service — `1.78.49`

- A multi-factor challenge is single-use on every sign-in path, not only the
  MCP flow. Enrolling needs the e-mail code, no enrol token is issued after a
  shared-password login, and users are notified when a factor is enrolled.
- Organisations own a list of e-mail domains, each assignable once. A social
  login joins the organisation that lists the verified domain, never invents an
  organisation, user or subscription, and refuses without naming anybody while
  the administrators are told instead. Hilco SSO and the domains Microsoft
  returns are handled.
- Every refused login carries a trace id. Admins can re-send the "Set your
  password" e-mail. The contract balance is signed and the contract start is
  audited.

## Auth Bridge — `0.5.7`

- The EU and US account replication keeps its connection fed during
  reconciliation, reattaches a dropped replication slot on its own, uses
  bounded memory, and treats an existing replication origin as success. Cross
  region sign-in is more reliable.

## Docflow Service — `2.10.22`

- The separate unit price card reads the organisation's default field
  definitions for charges and compares every costing element a field lists.
- The workflow execution limit rises from 30 to 50, and workflow log searches
  reject an id that is not a UUID.

## Docnet Service — `1.56.15`

- `list_document_fields` reports every configured table column, including
  those that are empty.

## Extraction Service — `1.56.0.1`

- Tiers: new models behind Fast and Full, Auto, Nexus Flash and a vision
  mode. Vision requests to the inference host stay under its size limit.
- Table extraction with Nexus batches pages (two per batch), runs batches in
  parallel with a measured timeout, retries transient errors and splits a
  batch that timed out. Header fields are read from all batches.
- US totals: additional amounts are part of the total equation, pair 1 counts
  in the pair-2 guard, low-score candidates are skipped when taxes are not
  zero, and "above" and "below" match multi-word labels.
- Identifier fields repair characters that really occur, and invisible
  characters are treated by what they mean, so an "O" no longer turns into an
  odd character.

## Fulltext Service — `1.42.41`

- New index for the DocBits documentation, with ingest and search endpoints,
  images in answers and a deadline for the whole search. It feeds the Settings
  Assistant.

## PO Match Service — `1.59.48`

- Absolute floor for charges the purchase order expects as zero, and charge
  tolerance for charges the order does not budget.
- A column can carry an "allow mismatch" flag. Several costing elements per
  field are split in proportion.
- Only organisation admins write or approve match rules, and rule conditions
  accept a whitelisted expression grammar only.
- Rule changes can be simulated against an override rule set without writing,
  for Touchless change proposals. PO extra columns to match are read from the
  document type attribute, with a migration of the old preference.

---

_Not affected in this release: Auto Accounting, Barcode, E-Mail, FTP, Ideas,
OCR, Operator. FTP and Operator carry only internal maintenance._

<!-- Release R1.0.15 (sandbox 02-10-26, planned prod 14-10-26, deployed Tuesday 13 Oct 2026).
Versions on prod before this deploy: API 12.83.222, Auth 1.78.38, Auth Bridge 0.4.2,
Docflow 2.10.18, Docnet 1.56.13, Extraction 1.55.50.1, Fulltext 1.42.38, PO Match 1.59.39,
Web App 10.70.6.
Held back (Release No. names a later release; announce with that release):
R1.1: CORE-6145, CORE-6148 (import failure notice and card per channel), CORE-6127 and
CORE-6136 (run transformation rules after master data lookup), CORE-6117, CORE-6072, CORE-6071,
CORE-2452, CORE-2444, DRFS-779, CORE-554 (rule execution logs from the dashboard), CORE-550, CORE-6278,
CORE-6180, CORE-6168, DMB-431, OBO-160, DRFS-806 (date tolerance for PO matching and approval).
R1.0.16: CORE-6103 (assistant drafts transformation rules), DRFS-822 (charge cards use only
matched POs, trigger status filter), DPG-170 (cost invoice export gate), OBO-159 (the "x" on a
field stores "leave empty" on its own; field suppression).
R1.2 / R1.4: DRFS-535 (receipt availability flag), DOP-53 (UOM conversion).
Added from the Ready for Production Release list: DRFS-742, DU-220, MAR-67, DRFS-708, DRFS-820,
DRFS-723, DRFS-724, DRFS-726. Not on the page (no matching code in the delta, check by hand):
MEF-169 (S/MIME invoices from Datatronic, Email Service version unchanged), DMB-391.
Shipped although Release No. is empty or stale: OBO-156, CORE-6102, CORE-6154, CORE-6155,
CORE-6150, CORE-6169, CORE-6181, CORE-6183, CORE-6185, CORE-6187, CORE-2606, CORE-2461,
CORE-2457, CORE-6092 (R1.0.14 labels). -->
