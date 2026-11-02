# DocBits Release Notes — 4–14 July 2026

_A rundown of what changed for you in this DocBits release. Every service below
lists the version now rolling out, followed by what's new or fixed in plain
language — no ticket numbers, no engineering jargon. Services not listed had no
customer-facing changes in this window._

---

## Highlights

- **Multi-organisation login.** Users who belong to several organisations now
  get a proper organisation picker at login, an organisation switcher in the
  header, and a default-organisation setting. Sessions are securely bound to
  one organisation at a time, and the app automatically follows the region of
  the active organisation. Logging in against the wrong region now retries the
  correct one automatically instead of failing.
- **Release channels (frozen / latest).** Organisations can now be pinned to a
  stable ("frozen") release while others receive the latest updates — enabling
  controlled rollouts. The Service Versions dialog shows a new *Release*
  column, and administrators manage the channel from Company Information.
  Several services show larger version jumps in this window purely because of
  the new channel version numbering — those jumps carry no functional change.
- **Configurable rules engines.** Three new rule systems arrive in the API
  (each off by default, enabled per organisation): **validation rules** that
  check extracted values and flag failures directly on the document,
  **transformation rules** that clean up or rewrite extracted field and table
  values automatically, and **rule-based layout selection** that picks the
  right document layout by rules instead of by where the document came from.
- **E-mail import transparency.** The e-mail import log now shows one
  expandable row per attachment, tells you which documents were created (with
  buttons that jump straight to them on the dashboard), flags skipped and
  split items, and lets you download the original e-mail as an `.eml` file.
- **AI table extraction.** A new structured AI extraction mode for tables,
  with a "Use AI" checkbox per table and per column in Document Type settings.
- **Web App stability.** Fixed an infinite reload loop after an expired
  session, fixed the broken Layout Builder, and extraction tables now have a
  draggable height resizer.
- **New: Auth Bridge Service.** A new service keeps login data continuously in
  sync between the EU and US regions, with self-healing and monitoring built
  in.

---

## API Service — live: `12.57.8`

- **Validation rules (new, per organisation):** an administrator-configurable
  rules engine checks extracted values (totals, required fields, and more) and
  marks failures directly on the document, including which rule fired. Rules
  can be tested in a dry run before enabling, can be switched on per document
  type, and ship with a starter catalogue of default rules (all disabled until
  you opt in).
- **Transformation rules (new, per organisation):** automatically clean up or
  rewrite extracted field and table values during processing — configurable
  per document type or for the whole organisation.
- **Rule-based layout selection (new):** document layouts can now be chosen by
  configurable rules instead of being tied to the document's origin. Existing
  origin-based behaviour is migrated automatically, layout templates can be
  renamed, and duplicate layout titles are prevented.
- **Faster dashboard exports:** exports triggered from the dashboard are now
  dispatched to a dedicated worker instead of waiting for a polling cycle, so
  they start promptly.
- **Duplicate Detection export block fixed:** the export block for suspected
  duplicates works again.
- **Settings that wouldn't stick:** fixed saved preferences occasionally not
  persisting when an older deleted copy of the same setting existed.
- **Documents with unusual characters:** fixed save errors caused by invisible
  NUL characters in extracted data.
- **Correct "Updated by":** documents uploaded automatically as e-documents no
  longer show a system user as the last editor — the field stays empty until a
  person actually edits.
- **Scanned PDFs with a good text layer:** a new option lets DocBits trust the
  text already embedded in a scanned page instead of re-running OCR — faster
  and often more accurate.
- **E-invoices:** more robust detection of embedded XML when the original file
  needs to be re-checked.
- **Tasks:** new organisation toggle that lets non-administrators use the
  "All" filter in the task list.
- **Line-item matching:** fuzzy-matching behaviour is now configurable per
  line.
- **Stability:** WebSocket connections close cleanly on errors instead of
  raising server exceptions; permission-cache synchronisation verifies and
  repairs itself; the service version is now visible on the health endpoint.

## Auth Service — live: `1.71.1`

- **Multi-organisation login:** login now asks which organisation to enter
  when a user belongs to several, sessions are bound to that organisation,
  and new endpoints support selecting, switching, and setting a default
  organisation. Duplicate or conflicting organisation memberships were cleaned
  up and are now prevented at the database level, with faster membership
  lookups.
- **Default organisation fixes:** logging in auto-selects your default
  organisation (not an arbitrary one), and changing the default takes effect
  immediately instead of showing stale profile data.
- **Logout fixed:** resolved a server error (HTTP 500) on logout and restored
  the token-revocation endpoint.
- **Token safety:** token verification and caching now respect the
  organisation a token was issued for, and token revocation is centralised.
- **Release channels:** the organisation's release channel is stored here,
  manageable by org administrators, and exposed to the app and routing layer.

## Auth Bridge Service — live: `0.2.4.2` _(new service)_

- **What it is:** a new service that continuously replicates authentication
  data between the EU and US regions, so accounts and logins stay consistent
  across regions.
- **Self-healing:** it detects and repairs data drift between regions —
  including making sure deletions propagate — and recovers automatically from
  connection loss instead of dropping data.
- **Safety and monitoring:** an earlier bidirectional replication loop was
  stopped and is now actively detected and gated; error tracking and alerting
  are wired in; and the service reports its version in the Service Versions
  dialog.

## Docflow Service — live: `2.6.1`

- **Workflow cards accept empty values:** checkbox and partner cards no longer
  fail when a field is legitimately empty; card type checks are stricter and
  more predictable.
- **Workflows re-run on real changes:** the workflow lock again respects the
  document status from the trigger, and now also tracks the document version —
  so a document whose data genuinely changed can go through the workflow again
  even with the same status, while true duplicates stay blocked.
- **Bigger advanced workflows:** the limit on workflow nodes was raised and is
  now configurable per environment.
- **Alternate export:** workflow-triggered alternate exports are now labelled
  as such so downstream systems can distinguish them.
- **Resilience:** the service reconnects automatically when a database
  connection is dropped mid-use, tolerates a slower message broker instead of
  failing, and failed API requests are now logged with full context and
  traceable execution IDs.

## Email Service — live: `1.38.4`

- **Import log, rebuilt for traceability:** every imported e-mail now records
  which documents were created from it, with per-attachment detail rows.
- **Original e-mail download:** the original message can be downloaded as an
  `.eml` file straight from the import log.
- **Attachment recovery:** the corruption-recovery path now also handles
  plain-text messages, so more damaged inbound e-mails are recovered instead
  of skipped.

## Extraction Service — live: `1.51.6`

- **Tax/net no longer swapped:** fixed a case on US documents where the tax
  amount could be assigned as larger than the net amount when several
  candidate pairs were found.
- **Multiple tax rates per supplier:** extraction now handles suppliers whose
  invoices carry different tax rates on one document.
- **AI table extraction (new, opt-in):** structured AI extraction endpoints
  for tables, activated per organisation via feature flag.
- **Faster AI calls:** tuned the AI model configuration used during extraction
  to avoid unnecessary processing time.
- **Crash fix:** resolved an error on documents that produced an empty
  candidate list during extraction.

## Fulltext Service — live: `1.37.2`

- **Search index migrations repaired:** restored migration definitions that
  had drifted, keeping search index upgrades reliable.
- Internal routing work for the new release-channel infrastructure.

## PO Match Service — live: `1.58.2`

- **More tolerant matching:** PO matching no longer fails on unusual data —
  non-text item numbers, missing quantities, and non-text amount values are
  now handled gracefully instead of erroring.

## Web App — live: `10.41.8`

- **Multi-organisation experience:** new organisation picker page at login,
  a dedicated organisation-switcher icon in the header, default-organisation
  settings, and the app follows the region of your active organisation.
  Logging in against the wrong region silently retries the correct region and
  routes you to the organisation picker when needed.
- **No more endless reloads:** fixed an infinite reload loop that could occur
  when the server rejected a stored session token — the app now forces a real
  token refresh instead of reloading forever.
- **Layout Builder fixed:** the Layout Builder works again, and layout
  selection is decoupled from the document's origin (matching the new
  rule-based selection in the API).
- **Extraction tables:** line-item tables now have a draggable resize handle
  so you can give the table more room while validating.
- **E-mail import log:** new skipped status and split badges, expandable
  per-attachment rows, original-e-mail download, and document-ID buttons that
  jump straight to the dashboard filtered to that document.
- **Dashboard search:** the query-value dropdown now shows the localized label
  for list-of-values fields, and the search help examples were reworked.
- **Settings reliability:** user preferences now load reliably when signing in
  via SSO, and the save confirmation is only shown when the save actually
  succeeded.
- **Tasks:** the "All" filter can be restored for non-administrators via a new
  organisation toggle.
- **Watchdog logs:** no longer capped at 10,000 entries, plus general
  usability improvements.
- **Support tickets:** the support form pre-fills your e-mail address from
  your profile.
- **Document Type settings:** new "Use AI" checkbox on tables and columns to
  control AI-assisted table extraction.
- **Service Versions dialog:** new *Release* column showing each service's
  channel (frozen/latest), routed so it stays fast for pinned organisations.
- **Field Validation:** fixed an error when returning to Field Validation from
  another screen, and the "Scripts" button no longer routes to a 404 page.

---

## Version renumbering only (no functional changes)

**Auto Accounting** (`1.20.1`), **Barcode Service** (`1.17.1`), **OCR
Service** (`1.9.1`), **FTP Service** (`1.31.1`), **Operator Service**
(`1.40.2`), and **Ideas Service** (`0.3.1`) were re-versioned as part of the
new release-channel infrastructure. Their larger-looking version jumps carry
no feature or behaviour changes in this window. **Docnet Service** (`1.54.6`)
is unchanged since 19 June.

<!-- Generated by the docbits-changelog skill (version-boundary mode: exact
     git ranges between the ALT (2026-07-03/04) and NEU (2026-07-09..14)
     version-bump commits supplied by the user, per service). -->
