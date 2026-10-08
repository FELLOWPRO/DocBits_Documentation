# DocBits Roadmap

_Planning status as of 7 October 2026. Each release lists the planned
sandbox date (when customers can test it) and the planned production date. The
themes describe what is planned for the release, not what has already shipped;
scope and dates can move. Hotfixes between releases are documented in the
[Release Notes](release-notes/README.md)._

| Release | Sandbox | Production |
|---|---|---|
| R1.1 | 16 October 2026 | 4 November 2026 |
| R1.2 | 16 February 2027 | 3 March 2027 |
| R1.3 | 1 June 2027 | 16 June 2027 |
| R1.4 | 5 October 2027 | 20 October 2027 |

---

## R1.1 — Sandbox 16 October 2026 · Production 4 November 2026

**Transformation rules and layouts**

- A rule engine for extracted field and column values: set, replace or derive
  values with nested condition groups, with a settings screen to manage the
  rules. The "is one of" condition takes several values, the rule list can be
  searched by rule ID, and rules also run after the master data lookup.
- Layout selection rules get the same nested conditions and an optional
  execution log. Layout selection works independently of where a document came
  from.
- Manage Layouts, Custom Validation Rules and Transformation Rules no longer
  need the beta switch.
- Clear precedence rules for field labels on header fields and table columns.
  Users can create their own translation keys for field settings and table
  columns.
- A table column can be assigned again after it was deleted, and the supplier
  item price table shows all of its columns.

**Approval and validation screens**

- The three line-item tables on the approval screen (invoice lines, compare
  lines, PO matching) share one style.
- The last-opened side panel (activity stream or approval history) is
  remembered per user.
- Merge documents from the approval screen with the document uploader.
- Custom validation rules handle shipping costs generically, show a field
  message instead of a general error when a required field is empty, and rules
  that reported a false negative are corrected. System default rules can be
  duplicated.
- A mismatch between quantity and net amount on an AI-extracted table is
  reported, an invoice with a matched purchase order is no longer classified as
  a cost invoice, and a date reformatted by a rule is accepted.
- An approval screen that hung on the loading overlay after approving or
  rejecting is fixed. A loading bar replaces the plain loading icon, and page
  URLs are friendlier.
- Opening a document link after the session has expired leads to the login
  page instead of a 404.

**Duplicate detection**

- Custom fields appear in the duplicate detection result, and the duplicate
  settings can be searched.
- "Block Duplicate Document Export" blocks the export of a detected duplicate.

**Workflows and tasks**

- A "New workflow" button, logs for advanced workflows, a clearer watchdog log
  screen, and workflow steps that change a field or checkbox apply reliably.
- Adding a line in a decision tree keeps the user names instead of showing IDs.
- Every status change of a document is logged.
- Creating a new e-mail template works again.
- The task list shows its tasks on first load.

**Import**

- E-mail import moves a mail out of the inbox only after the upload is
  confirmed, treats a redelivered forward as one delivery, records who last
  saved, and lists an attachment once with the reason when it fails.
- FTP and SFTP import get a true delete-after-import option next to move and
  archive. Passwords are no longer corrupted when a configuration is edited,
  the connection test works for new SFTP connections, and a failed SFTP
  connection or wrong login shows a specific message instead of a general error.
- Administrators are told in the Settings Assistant when a configured FTP or
  e-mail import stops working.
- The scanner app upload works again.
- Purchase order BOD files uploaded in the US region stay in the US region.

**Document processing and extraction**

- When the barcode service hangs, the document shows the error instead of
  sitting in "Processing" indefinitely.
- A new, cheaper AI model tier ("Eco") for extraction.
- With structured AI extraction, trained supplier item numbers stay trained,
  and item number and supplier item number are no longer swapped.
- UBL e-document templates are adjusted; extraction corrections for amounts,
  tax rates, unit prices and purchase order numbers on specific supplier
  layouts.
- Additional date formats are recognised.
- A cost invoice with two VAT rates keeps both accounting lines.

**Purchase order matching**

- Matching requires a quantity column, uses the price per base unit quantity,
  and the last-line fallback can be switched per customer.
- Delivery note lines can be selected individually.
- The e-document screen no longer freezes on invoices with more than 250 lines.

**Touchless Intelligence**

- More detail in the Touchless report, and the Touchless checkbox reflects the
  saved setting.

**Dashboard, accounts and subscription**

- The dashboard can hold up to 10,000 documents per search, and a custom date
  filter is applied correctly.
- Discount due date and invoice due date are available as layout fields and
  filled on import.
- Shared dashboard users are kept when a dashboard is saved, and "Updated by"
  shows the right person.
- Archived documents can be moved back out of the "Archived" status.
- Users can log in again after a password reset.
- The subscription plan page shows usage for the plan and its features.

**Export and EDI**

- An additional Infor M3 export step for extra invoice information.
- A packing list with several container numbers is exported as one record per
  container.
- Re-importing a receive delivery no longer fails on a duplicate key, and
  receive delivery BODs are applied in the right order.
- EDI mappings for invoice, purchase order and order confirmation are updated.
- Testing the connection of a new Infor IDM or Infor LN export configuration
  works.

**Security**

- The organisation guard for API keys is enforced on every environment.

---

## R1.2 — Sandbox 16 February 2027 · Production 3 March 2027

**Approval and purchase order matching**

- A "Pending input" state pauses a document until someone answers, without
  breaking the workflow or the audit history, and approvers can ask questions
  without interrupting the approval flow.
- A document can be reassigned to another user (first phase).
- Pre-payment invoices can be matched before the goods receipt while "Match on
  received quantity" stays active.
- The matching screen offers only viable PO lines, and multi-line matches that
  skip the price comparison still show the unit price on the approval screen.
- A receipt availability flag compares invoiced and received quantities.
- Order confirmations: costing elements shown while approval is pending,
  colour-coded surcharge positions in PO matching, and the item number column
  in the invoice line items.
- Supplier RMA lines are handled.

**Import and classification**

- The supplier type is derived from the line items.
- The support ticket form accepts attachments and links the organisation
  automatically.

**Settings and automation**

- The "Set sub-organisation" script becomes a transformation rule.
- Standard columns can be removed from a document type.

**Export**

- The export history lists exported documents again.
- Freight invoices export to Infor LN.
- Export file names are configurable.
- Extended Vertex tax integration.

---

## R1.3 — Sandbox 1 June 2027 · Production 16 June 2027

**Auto Accounting Rule Manager**

- Rules assign accounts and dimensions automatically, scoped per
  sub-organisation and document type, with an audit screen that shows which
  rule fired.
- A rule can look up master data and assign several fields at once, or
  populate a value from a table line column.
- Fields and dimensions can be cleared individually, line items can be deleted
  (including lines without an amount), and rules keep working on fields that
  changed from text to dropdown.
- Predictions support multiple tax codes and dimensions, vouchers and booking
  references. The Auto Accounting screens are available in several languages.

**Purchase order matching**

- The match icon navigates, scrolls and highlights across tabs, including
  one-to-many matches.
- Unit conversion with aliases (for example KG and TO), a configurable
  rounding variance with a rounding account, and calculations with four
  decimals shown as three.

**Usability**

- The execution order of document scripts is visible in the frontend.
- Enter and Tab move through fields on the keyboard.

**Export**

- An incomplete document in Infor LN is deleted after a failed export.
- The database connector includes all relevant tables.

---

## R1.4 — Sandbox 5 October 2027 · Production 20 October 2027

**Auto Accounting on the approval screen**

- Approvers can work with auto accounting directly on the approval screen.
- Approval can be gated on accounting fields such as nominal code or country,
  with an AP correction when a document is returned.
- A tax code dropdown on Auto Accounting without setting up multiple tax
  lines.
- Dimensions are stored in a new structure so large dimension sets load
  faster, and the Rule Manager gets a feedback round.

**Approval**

- An improved approval flow, delegation to another user during approval, and
  an "Export & Next" button.

**Purchase order matching and export guards**

- Over-matched invoices, where the invoiced quantity exceeds the received
  quantity, are recognised on the matching screen, and units of measure are
  converted during invoice matching.
- Charge codes (toll, transport, energy) are recognised and their cost
  distributed.
- Export is blocked with a warning when the matched quantity exceeds or differs
  too much from the received quantity, or when the booking date is before the
  warehouse entry date.

**Import and settings**

- A retry mechanism for FTP, e-mail and inbound e-mail import with automatic
  and manual reprocessing, and the sender address is available from e-mail
  import.
- Settings can be searched across all toggles and sub-pages.
- The e-mail server setup lets you replace an expired OAuth or client secret
  without setting the mailbox up again.
- The supplier item number map (item number conversion table) can be filled
  from a CSV import.
- The approval history can be exported through SFTP export.

**DocNet Agents**

- Order intake: a customer order becomes a sales order in Infor M3 or Infor
  LN (first version, text documents).

<!-- Generated from Jira "Release No." (customfield_10392) on 2026-10-07 by the
     docbits-roadmap skill. Releases up to R1.4 only; R1.5 and later are not
     published yet. Themes only; ticket keys, customer names and internal work
     are deliberately left out. Rerun the skill to refresh. -->
