# DocBits Release Notes — 14–23 July 2026

_What changed in the DocBits production upgrade on 23 July 2026 (the Nova
channel update), covering everything since the 14 July release. Each service
lists the version now live, then what's new or fixed in plain language.
Services not listed had no customer-facing changes._

---

## Highlights

- **Support tickets from the error screen.** When something goes wrong, you can
  now open a support ticket directly from the error record. The ticket already
  contains the technical context, so you don't have to describe it.
- **Region-correct inbound e-mail.** US organisations get inbound import
  addresses in their own region, and Microsoft 365 mailboxes on national cloud
  tenants (GCC, 21Vianet and similar) can now be configured with a Cloud
  Instance selection.
- **Clearer PO matching status.** Invoices whose line-item table couldn't be
  mapped used to be labelled "purchase order not found", which sent people
  searching for the wrong problem. They now get their own "table incomplete"
  status with column-level detail on what didn't map.
- **Tax code mapping for e-documents.** A new settings page maps your ERP tax
  codes for electronic documents, and exports check the mapping up front
  instead of failing in the ERP.
- **Script changes are password-protected.** Custom scripts can change how
  documents are processed, so every script edit now requires a password that
  rotates hourly. Ask your administrator for the current one.
- **Turbo AI tier retired.** The Turbo model has reached end of life. Anyone
  who had it selected was moved to Fast automatically; no action needed.

---

## Web App — live: `10.45.1`

### Working with documents

- **Deleted documents:** opening a document that was deleted in the meantime
  shows a proper message instead of script errors.
- **Field Validation:** the page-number input is wider and jumps to the page
  on Enter. A field made read-only by a script still shows its field
  connection.
- **Table extraction:** deleting a column frees its name for re-use, and
  deleted headers no longer reappear in the saved table.
- **Approvals:** users can no longer approve a Sales Tax step their group has
  no permission for, and the approval history shows all entries again. The
  history also names the person who actually approved, including approvals an
  admin made on behalf of the assignee.
- **Suppliers:** the Accounting page no longer shows a false "Supplier is
  missing" warning, and deleting a supplier that only exists from extraction
  no longer leaves the dialog hanging.
- **Tasks and notifications:** the delete option is hidden from users without
  admin rights.

### Dashboard and search

- **Export:** exports use the dashboard you have selected, and the app warns
  you before exporting a dashboard with unsaved changes.
- **Search:** Invoice Type is available as a search field with its list of
  values.
- **Import log:** split documents can be found via their parent document, and
  the Failed Filenames column lists only files that actually failed or were
  skipped.

### Sign-in

- **Deleted accounts:** logging in with a deleted account says so instead of
  failing with a generic error.
- **SSO:** fixed an error when signing in while a different region was
  selected.

### Settings and administration

- **Support tickets:** create a ticket straight from an error record. Tickets
  carry the environment and release channel, and the screenshot capture no
  longer hangs.
- **Workflow Builder:** newly created or renamed cards, e-mail templates and
  other dropdown items appear immediately, without reloading the page.
- **Document Types:** new Structured Extraction setting in the extraction
  section.
- **E-Doc tax codes:** new settings page to map your ERP tax codes for
  electronic documents (see Highlights).
- **AI model selection:** the retired Turbo tier is gone from the dropdown;
  existing selections show Fast.
- **Service Versions dialog:** now scrollable, includes the Auth Bridge
  service, and shows the release channel names Vesta and Nova.
- **Import page:** no longer crashes for organisations with an empty
  subscription entry.

### Smaller fixes

Empty toast notifications are suppressed, the new/edit idea dialog scrolls,
misaligned checkboxes in field settings are aligned again, blocked document
deletions explain why, and E-Document settings handle switching from Default
to Custom cleanly.

## API Service — live: `12.64.3`

- **Script security:** script changes require a time-based password
  (see Highlights).
- **E-Doc tax codes:** ERP tax-code mapping for electronic documents, with a
  central check before export so missing codes surface early.
- **Access control:** admins can grant non-admin users visibility of
  unclassified documents.
- **Personal dashboards:** fixed sharing settings that wouldn't save.
- **Dashboard search:** Invoice Type joins the extended search fields, and
  documents created by a barcode or QR split are found via their parent
  document.
- **Uploads:** repeated uploads of the same file during a network retry no
  longer create duplicate documents.
- **Supplier lookup:** results arrive as soon as the data is ready instead of
  after a fixed wait.
- **Infor export:** unit prices keep four decimal places. M3 exports can
  include zero-amount line charges, and negative LN cost lines are sent as
  positive credits.
- **Approvals:** an approval is only linked to an approval request when the
  approver is its assignee.
- **Login stability:** a temporary failure inside token validation no longer
  logs users out; the app retries instead.
- **Classification:** source rules now match against every document source
  field, not fixed positions.
- **Validation stability:** a field without a name no longer crashes document
  validation.
- **AI models:** the Turbo tier (retired) is remapped to Fast everywhere,
  including fine-tuned variants, with a guard so a retired model can never
  run.

## Auth Service — live: `1.72.8`

- **Login history:** sign-ins via SSO/SAML now appear in the login history,
  and the last-login timestamp is stamped reliably for every login type.
  Viewing another user's login history requires the appropriate admin level.
- **Legacy accounts:** deleting a legacy user account works again instead of
  silently doing nothing.
- **Bulk user administration:** add existing users to sub-organisations and
  groups in bulk via CSV, matched by e-mail address. Also fixed a crash on
  unevenly filled CSV rows and a server error when adding two or more new
  users at once.
- **Member lists:** deleted users no longer appear in sub-organisation member
  lists.
- **Single sign-on:** a series of hardening fixes. Expired tokens now return a
  clean "expired" response, organisations without a SAML configuration get a
  proper not-found answer instead of a wrong login flow, logout always
  completes even when the sign-out request can't be verified, and several
  crashes around missing identity-provider configuration are gone.
- **Session tokens:** fixed short-lived session tokens being rejected as
  invalid even though they weren't expired.
- **Management tooling:** organisation region is visible in the management
  API, the system user of an organisation can be reassigned, and plan and
  usage administration gained dedicated endpoints. These changes affect
  DocBits staff tooling, not the customer app.

## Email Service — live: `1.39.9`

- **Region-correct import:** inbound e-mail domains exist per region, and
  mails arriving in the wrong region are forwarded to the right one. US
  organisations no longer depend on the EU inbound path.
- **Microsoft 365:** national cloud tenants are configured via a Cloud
  Instance selection, fixing O365 imports for US customers. An invalid tenant
  now produces a clear login error instead of a server error, and incomplete
  tenant credentials fail immediately with a message rather than silently.
- **Inbox hygiene:** e-mails without attachments are moved out of the inbox
  instead of piling up.
- **No duplicates on retry:** uploads to the document API carry an idempotency
  key, so a retried delivery can't create the same document twice.
- **Source naming:** O365 sources with a folder configured include the account
  e-mail in their name, so similar sources are distinguishable.
- **Import log housekeeping:** import log entries are kept for 90 days and
  cleaned up automatically after that.

## PO Match Service — live: `1.59.1`

- **"Table incomplete" status:** invoices whose line-item table couldn't be
  mapped get their own status instead of the misleading "purchase order not
  found" (see Highlights). The dashboard shows it with the not-matched icon.
- **Better error detail:** table-mapping failures name the specific column
  that didn't map.
- **Cleaner API behaviour:** requests for PO rules that don't exist return a
  proper not-found answer, and corrupt cache entries are dropped instead of
  causing repeated errors.
- **Match on total:** fixed a bug in matching against the purchase-order
  total.

## Fulltext Service — live: `1.38.3`

- **European number formats:** amounts written with a decimal comma
  (`1.234,56`) are normalised before indexing, so amount searches and filters
  work regardless of number format.
- **ERP counts:** fixed a token error that could interrupt the live count
  stream on the dashboard.
- **Indexing resilience:** indexing now rides out temporary database and
  auth-service hiccups (automatic retry, fallback to the primary database)
  and discards malformed queue messages instead of retrying them forever.

## OCR Service — live: `1.9.9`

- **Large documents:** the OCR time budget scales with document size, so very
  large files no longer fail with a timeout.
- **Unusual characters:** a sanitizer cleans characters the OCR engine can't
  represent, fixing failures on documents with exotic symbols.
- **Fewer transient failures:** temporary storage connection errors are
  retried automatically.

## Extraction Service — live: `1.52.0`

- **Zero-tax US invoices:** fixed a case where the correct net/tax pair was
  dropped when the tax amount is zero.
- **Table extraction:** tables stay editable when the configured mapping
  expects more columns than the document provides, and a crash on unusual row
  data is fixed.
- **AI models:** Turbo tier retirement, mirrored from the API Service.

## Docflow Service — live: `2.7.2`

- **PO matching in workflows:** missing comparison values are treated as
  missing data rather than a mismatch.
- **Order confirmation cards:** buyer and responsible person are resolved
  reliably.
- **Freight charges:** when neither side has charges, the case is resolved by
  the operator card instead of stalling.
- **Security:** workflow API tokens are validated against the organisation
  they belong to.
- **Faster triggering:** the check for active workflows is cached, and the
  background workers restart cleanly instead of leaving stalled processes
  behind.

## Barcode Service — live: `1.17.4`

- **Long-running splits:** the connection to the task queue is kept alive
  during long barcode jobs, so splitting large batches no longer stalls near
  the end.

## FTP Service — live: `1.31.2`

- **Import log housekeeping:** same 90-day retention and cleanup as the Email
  Service.

---

## Unchanged in this release

**Auth Bridge** (`0.3.6`), **Auto Accounting** (`1.20.1`), **Docnet**
(`1.55.1`), **Operator** (`1.40.2`) and **Ideas** (`0.3.1`) carry no changes
in this window.

<!-- Generated by the docbits-changelog skill (version-boundary mode), then
     reconciled on 23 Jul 2026 against the Nova versions actually deployed
     (Web App 10.45.1, API 12.64.3, Auth 1.72.8, Email 1.39.9, PO Match
     1.59.1, OCR 1.9.9, Docflow 2.7.2, FTP 1.31.2). Manage Layouts and
     Custom Validation Rules were removed from this page: DOCB-13719 gated
     both behind a beta query parameter, so they are not generally available
     in 10.45.1. -->
