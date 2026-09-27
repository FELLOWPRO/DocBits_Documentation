# DocBits Release Notes — 12–25 August 2026

_What changes in the DocBits production upgrade on 25 August 2026, covering
everything since the 12 August release. Each service lists the version being
deployed, then what's new or fixed in plain language. Services not listed had
no customer-facing changes._

---

## Highlights

- **Stricter organisation isolation.** A security sweep closed several places
  where data from one organisation could be read or written from another:
  document scripts, sub-organisation user lists, group memberships and the
  processing token a document carries through the pipeline are now all checked
  against the caller's organisation. Approvals also enforce four-eyes properly:
  the second approver must be a different person than the first.
- **Documents stop getting stuck.** Four separate causes of documents hanging
  forever were fixed: exports that stayed in "Exporting" after being denied,
  restarts that froze when a processing step crashed, barcode splits that never
  reported back, and the accounting screen hanging on "Preparing…". In each
  case the document now either finishes or shows a real error you can act on.
- **Credit notes are recognised as credit notes.** XRechnung 3.0, 3.0.1 and
  3.0.2 credit notes in CII syntax, pure CII credit notes and ZUGFeRD 2.4 /
  Factur-X 1.08 documents are all classified correctly now, with the total
  read from the right field. Scanned documents that mention both "invoice"
  and "credit note" are resolved by which keyword sits closer to the document
  type, and amounts turn positive again when you reclassify a credit note back
  to an invoice.
- **PO matching does arithmetic you can trust.** Tolerances are compared as
  exact decimals instead of floating-point values, are based on the purchase
  order value, and invoices that reference several purchase orders are matched
  against all of them. Columns you never mapped no longer distort the line
  amount check, and when required columns are missing, the error names them.
- **Workflow runs keep their work.** A workflow that writes a field value now
  writes it onto the document in a way a later export can't silently revert.
  Retried triggers no longer discard what the run already did, and two
  triggers hitting the same document queue up instead of stealing each other's
  lock.
- **Password-reset e-mails send again.** They were silently never leaving the
  server. The reset form also shows real feedback after you submit, and the
  response no longer reveals whether an account exists.

---

## Web App — `10.55.0`

### Signing in and accounts

- Password reset works end to end again: the mail arrives, the form confirms
  the submission, and the answer is the same whether or not the address has an
  account.
- If your organisation requires two-factor enrollment, the login screen now
  says so instead of failing without a message.
- Administrators can no longer switch on organisation-wide MFA enforcement
  before login enrollment is available, which previously could lock people
  out.

### Validation screen

- The zoom slider now goes up to 150% (it used to stop at 80%), and zooming
  into a table works past the container width instead of doing nothing.
- Empty amount fields count as 0 instead of firing an error toast, and a
  double click on the document image is ignored when no field is selected.
- The banner shown when another session holds the document lock had no text;
  it explains itself now. Tagging a table no longer triggers a false "document
  was modified externally" warning about your own change.
- In the AI table, a column remap that would unmap another column asks for
  confirmation first, and values that aren't numbers are flagged in AMOUNT and
  NUMBER columns.
- The "Extracted table" tab links to manual table training again when it is
  empty.
- Item numbers in the Compare line-item table are shown as identifiers, not
  rounded like amounts.
- Approver fields resolve user and group ids to names, so they never show a
  raw id or sit empty. Task deadlines are converted through one UTC-aware
  path, so every viewer sees the same date.
- Documents sent back to validation show a loading spinner instead of a dead
  screen while they are prepared.

### Accounting

- Splitted line items keep their % sign after pressing Enter, and 0 % is
  accepted as a value.
- In the account filter, Enter commits the first matching account instead of
  doing nothing.
- Flexdimension characters are mapped by dimension id, so dimensions land in
  the right column even when the order differs.
- A failed accounting preparation recovers with an error message instead of
  hanging on "Preparing…" forever, and reopening a document no longer serves
  stale data from the previous one.

### PO matching

- Opening PO Matching without every mandatory column mapped is possible again;
  when something needed is missing, the message names the exact columns.
- Columns that aren't mapped to anything are hidden when the screen opens,
  after asking you once, and they no longer flow into the line amount
  calculation.
- The matched quantity refreshes after saving, and the missing-column popup
  routes you to Field Validation where you can fix it.

### Dashboard and search

- Dropdown-based columns (invoice type, status and similar) show their label
  in your interface language instead of the raw stored value.
- Free-text search accepts parentheses as plain text; it used to reject the
  query. The "not equal" filter operator stays selected, and editing a filter
  by hand no longer corrupts the field name.
- Selecting a sub-organisation in quick search inserts its name, not its uuid,
  and the sub-org autocomplete no longer lists duplicates.
- The dashboard can now fetch up to 10,000 documents per search window, so
  large result sets page correctly.
- The duplicate-document panel shows the same resolved columns as the main
  list, and multi-word supplier filter values survive pressing Enter.

### Tasks

- The assignment e-mail goes out when a task is assigned, once. Editing a task
  or marking it done no longer re-sends it, and the "assigned on" date stays
  the date of assignment. Task e-mails also render properly in Outlook.

### Workflow Builder

- Search, sort order and pagination in the workflow list stay consistent
  while you filter.
- The "run workflow on change" toggle in the layout builder now gates the run,
  and enabling it requires picking a workflow.

### Settings and administration

- The WatchDog download link and setup command point to the environment you
  are in, not always production.
- Decision Trees: the selected document field stays highlighted when the
  picker reopens, truncated labels get a tooltip, and user names (not raw ids)
  are shown when adding a line.
- The System Admin checkbox is editable when editing a user.
- Analytics: Core Web Vitals render from the real measurement data, and the
  logs service view works.
- "Use Default Template" in the layout manager copies the default layout as
  intended.
- Custom field labels no longer override the bundled translations of standard
  fields.
- Supplier portal quotes: submitting a quote with a REF1 value outside the
  allowed list is blocked.
- MediOrder gets duplicate document detection on its validation screen.

## API Service — `12.82.3`

### Security and organisation isolation

- Switching the acting organisation is validated against your actual
  membership and fails closed, and an internal test endpoint that could be
  abused to cross organisations was shut.
- Document scripts can no longer be read or overwritten across organisations,
  neither via the apply-to-document call nor via a foreign version id on save.
- Sub-organisation user lists and group member lists only return people from
  the caller's organisation, and adding several users to a group at once no
  longer drops all but the first.
- A credential from the wrong organisation is refused before it can become a
  document's processing token, and full-text search queries run as the calling
  user rather than a service identity.
- Four-eyes approval is enforced: the second approver must differ from the
  person who approved first.
- The live PO Dashboard list is scoped to the user's sub-organisations.

### Document pipeline

- Documents denied for export no longer sit in "Exporting" forever, and export
  errors always carry a message instead of an empty one.
- When a processing step crashes, the document goes to an error state instead
  of being stuck in "restart in progress" with no way out.
- A barcode split that fails or times out marks the document as Error instead
  of silently showing "Running", and a split that produces no children keeps
  the parent and flags it instead of deleting everything.
- A failed retry can no longer overwrite a document that meanwhile finished
  processing.
- Documents restarted without user interaction and split children now run
  under a durable organisation token, so long-running processing doesn't die
  with an expired session.
- An empty layout-template response is no longer cached for six hours, which
  used to make layouts vanish until the cache expired.

### Extraction and e-documents

- Amounts written with a trailing minus ("100,00-") are parsed as negative
  instead of being dropped.
- Swiss documents are detected as Swiss (CHF, CHE VAT numbers, CH IBANs)
  instead of defaulting to German conventions, and dates written with
  typographic dashes parse correctly.
- XRechnung 3.0, 3.0.1 and 3.0.2 credit notes in CII syntax are classified as
  credit notes with the total read from the grand total field; the same goes
  for pure CII credit notes. A declared ZUGFeRD 2.4 / Factur-X 1.08 version
  wins over the generic profile identifier, and bare XRechnung types resolve
  to their UBL or CII twin instead of failing.
- Dropdown (list-of-values) fields such as Tax Country and Tax Code keep their
  value through field transformation; they were being emptied.
- Table extraction: a failure in a numbers-only column stays in that column
  instead of killing the whole table, AI table extraction gets a timeout that
  survives multi-batch runs, and two crashes on unusual table shapes (rows
  without page positions, ragged column counts) are fixed.
- Source rule patterns match case-insensitively.

### Export

- A tax check that fails during export preview returns a readable error
  instead of a server error, on both preview endpoints.
- SFTP export can send the original document alongside the converted one.
- When export configurations exist on several levels, the most specific one
  wins consistently.
- BOD exports can carry column type attributes via mapping.

### Import and master data

- The e-mail Import Log is complete: rejected and failed inbound e-mails
  always get a log row with an accurate reason. No more silent drops.
- Purchase order BOD imports keep sub-lines attached to the right line; a
  carried-over flag used to attach them to the wrong one.
- Importing a CSV with several new suppliers works (their generated ids no
  longer collide), cash discount term aliases import and honour the
  "on conflict" setting, and the on-conflict IGNORE choice applies beyond
  suppliers.
- The supplier suggestion (TF-IDF) keeps its supplier id when a preference is
  updated, so suggestions stop pointing at nothing.

### Other fixes

- Dashboard rows resolve dropdown labels in the user's language, without
  blocking the request.
- After editing fields, the PO match status updates instead of showing the
  pre-edit state.
- Purchase Order Change documents get five Purchase-Order-parity fields and a
  default field validation layout.
- Error responses across 152 endpoints return readable messages instead of raw
  exception objects, and the logs analytics page no longer answers with 502
  for organisations without a log index.

## Auth Service — `1.77.9`

- Password-reset e-mails were silently never sending; fixed, together with the
  thread-safety issue underneath it.
- A replayed refresh token is rejected: the authoritative database check runs
  every time now instead of being skipped on a cache hit.
- Two-factor authentication: an authenticator app can be enrolled alongside
  e-mail codes, and removing the last passkey or regenerating backup codes
  requires a fresh second factor first.
- A valid sub-organisation id is no longer rejected with "Organization not
  found", and an API key created in a sub-organisation resolves its technical
  user from that sub-organisation.
- Editing an organisation validates the partner id and no longer resets the
  organisation type as a side effect.
- "Remaining tokens" in the subscription view is anchored to the contract
  year, not the calendar year.

## Auth Bridge Service — `0.5.7`

- Account replication between the EU and US regions recovers on its own. A
  dropped replication stream reattaches in place, replication keeps flowing
  while a reconciliation runs, and reconciliation memory is bounded so the
  service stops crash-looping on large tables.

## Barcode Service — `1.18.7`

- Barcode reading runs under a time limit and reports a timeout instead of
  hanging, which used to leave the document stuck in processing.

## Docflow Service — `2.9.8`

- Field values written by a workflow card land on the document in both stored
  representations, so a later export no longer reverts them.
- A retried trigger keeps the work the run already did, contended triggers on
  the same document queue up instead of stealing the lock, and an escalated
  retry is ranked first in the queue.
- Purchase order comparison cards: tolerances compare as exact decimals and
  are based on the purchase order value, reversed comparison directions are
  available as options, a group assignee is reported as a group instead of
  failing a user-id comparison, assignment ids compare correctly as UUIDs,
  lines with empty numeric values are skipped, and a "received" comparison
  without any received data reports missing data instead of pretending to
  match.
- The Apply Decision Table card has been retired.

## Email Service — `1.41.0`

- Gmail imports pick up each attachment exactly once; duplicates from
  overlapping fetches are gone.
- The import read-cursor only advances after an import is confirmed, so a
  crash mid-import can no longer skip e-mails.
- When an import configuration is deactivated because a similar one exists,
  that deactivation is visible and notified instead of silent.

## Extraction Service — `1.54.5`

- Whether a document is a credit note or an invoice is resolved by which
  keyword sits closer to the document type mention, instead of first match
  wins.
- When several tax interpretations are within tolerance, the exact
  reconciliation is preferred over a near miss.
- After a forced re-OCR the document type and locale are restored, so table
  extraction and training work on re-OCR'd documents again.
- Documents without a document type no longer crash table rule lookup.

## FTP Service — `1.32.8`

- Folder scanning does one listing round trip per folder with a bounded depth,
  so imports from large FTP directories are much faster and stop timing out.

## Fulltext Service — `1.42.3`

- Documents whose stored search payload had no extracted fields are re-indexed
  from the database, so they show up in dashboard search again.
- The dashboard search window supports up to 10,000 documents.
- Facet searches no longer fail when semantic search is active.

## OCR Service — `1.10.7`

- The OCR time budget is sized by real per-page cost, so long documents finish
  instead of hitting the pipeline limit.

## PO Match Service — `1.59.8`

- Table lines with zero quantity are skipped in mismatch checks instead of
  producing false mismatches.
- When required PO-match columns are missing, the result names them.
