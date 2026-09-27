# DocBits Roadmap

_Planning status as of 18 September 2026. Each release lists the planned
sandbox date (when customers can test it) and the planned production date. The
themes describe what is planned for the release, not what has already shipped;
scope and dates can move. Hotfixes between releases are documented in the
[Release Notes](release-notes/README.md)._

| Release | Sandbox | Production |
|---|---|---|
| R1.1 | 5 October 2026 | 14 October 2026 |
| R1.2 | 23 November 2026 | 2 December 2026 |
| R1.3 | 8 February 2027 | 17 February 2027 |
| R1.4 | 7 April 2027 | 15 April 2027 |
| R1.5 | 18 May 2027 | 27 May 2027 |
| R1.6 | 6 July 2027 | 15 July 2027 |
| R1.7 | 21 September 2027 | 30 September 2027 |
| R2.0 | to be announced | to be announced |

---

## R1.1 — Sandbox 5 October 2026 · Production 14 October 2026

**Transformation rules and layouts**

- A rule engine for extracted field and column values: set, replace or derive
  values with nested condition groups, with a settings screen to manage the
  rules. Layout selection rules get the same nested conditions.
- Layout selection works independently of where a document came from.
- Clear precedence rules for field labels on header fields and table columns.
- A table column can be assigned again after it was deleted, and the supplier
  item price table shows all of its columns.

**Approval and validation screens**

- The three line-item tables on the approval screen (invoice lines, compare
  lines, PO matching) share one style, and the compare view shows the item
  number that belongs to the line.
- The last-opened side panel (activity stream or approval history) is
  remembered per user.
- Merge documents from the approval screen with the document uploader.
- Custom validation rules handle shipping costs generically, and rules that
  reported a false negative are corrected.
- A loading bar replaces the plain loading icon; friendlier page URLs.

**Duplicate detection**

- Custom fields appear in the duplicate detection result, and the duplicate
  settings can be searched.

**Workflows and tasks**

- A "New workflow" button, logs for advanced workflows, a clearer watchdog log
  screen, and workflow steps that change a field or checkbox apply reliably.
- Adding a line in a decision tree keeps the user names instead of showing IDs.
- Every status change of a document is logged.
- Creating a new e-mail template works again.

**Import**

- E-mail import moves a mail out of the inbox only after the upload is
  confirmed, treats a redelivered forward as one delivery, records who last
  saved, and accepts S/MIME-signed mails.
- FTP import gets a true delete-after-import option next to move and archive.
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

**Purchase order matching**

- Matching requires a quantity column, uses the price per base unit quantity,
  and the last-line fallback can be switched per customer.
- Delivery note lines can be selected individually.
- The e-document screen no longer freezes on invoices with more than 250 lines.

**Touchless Intelligence**

- More detail in the Touchless report, and the Touchless checkbox reflects the
  saved setting.

**Dashboard**

- The dashboard can hold up to 10,000 documents per search.
- Discount due date and invoice due date are available as layout fields and
  filled on import.
- Shared dashboard users are kept when a dashboard is saved, and "Updated by"
  shows the right person.
- Archived documents can be moved back out of the "Archived" status.

**Export and EDI**

- An additional Infor M3 export step for extra invoice information.
- A packing list with several container numbers is exported as one record per
  container.
- Re-importing a receive delivery no longer fails on a duplicate key, and
  receive delivery BODs are applied in the right order.
- EDI mappings for invoice, purchase order and order confirmation are updated.

**Security**

- The organisation guard for API keys is enforced on every environment.

---

## R1.2 — Sandbox 23 November 2026 · Production 2 December 2026

**Approval and purchase order matching**

- A "Pending input" state pauses a document until someone answers, without
  breaking the workflow or the audit history, and approvers can ask questions
  without interrupting the approval flow.
- Pre-payment invoices can be matched before the goods receipt while "Match on
  received quantity" stays active.
- A receipt availability flag compares invoiced and received quantities.
- Order confirmations: costing elements shown while approval is pending,
  colour-coded surcharge positions in PO matching, and the item number column
  in the invoice line items.
- Columns that are not mapped no longer feed the table amount calculation.
- Supplier RMA lines are handled.

**Import and classification**

- The sender address is available from e-mail import.
- The supplier type is derived from the line items.

**Settings and automation**

- The "Set sub-organisation" script becomes a transformation rule.
- Standard columns can be removed from a document type.

**Export**

- The export history lists exported documents again.
- Freight invoices export to Infor LN.

---

## R1.3 — Sandbox 8 February 2027 · Production 17 February 2027

**Auto Accounting Rule Manager**

- Rules assign accounts and dimensions automatically, scoped per
  sub-organisation and document type, with an audit screen that shows which
  rule fired.
- A rule can populate a value from a table line column.
- Fields and dimensions can be cleared individually, line items can be deleted
  (including lines without an amount), and rules keep working on fields that
  changed from text to dropdown.

**Purchase order matching**

- The match icon navigates, scrolls and highlights across tabs, including
  one-to-many matches.
- Unit conversion with aliases (for example KG and TO), a configurable
  rounding variance with a rounding account, and calculations with four
  decimals shown as three.

**Export**

- Configurable export file names.
- An incomplete document in Infor LN is deleted after a failed export.
- The database connector includes all relevant tables.

---

## R1.4 — Sandbox 7 April 2027 · Production 15 April 2027

**Import**

- A retry mechanism for FTP, e-mail and inbound e-mail import with automatic
  and manual reprocessing.

**DocNet Agents**

- Order intake: a customer order becomes a sales order in Infor M3 or Infor
  LN (first version, text documents).

**Approval**

- An improved approval flow, delegation to another user during approval, and
  an "Export & Next" button.

**Purchase order matching**

- Only viable PO lines are offered on the matching screen.
- Over-matched invoices, where the invoiced quantity exceeds the received
  quantity, are recognised on the matching screen, and units of measure are
  converted during invoice matching.

**Other**

- Feedback round on the Rule Manager.
- The support ticket form accepts attachments and links the organisation
  automatically.
- Extended Vertex tax integration.

---

## R1.5 — Sandbox 18 May 2027 · Production 27 May 2027

**Auto Accounting**

- Rule Manager lookup action: match master data and assign several fields at
  once.
- Predictions support multiple tax codes and dimensions, vouchers and booking
  references.
- Auto Accounting screens in several languages.

**Approval and purchase order matching**

- Reassign a document to another user.
- Column order on the PO matching screen is saved per user.
- Charge codes (toll, transport, energy) are recognised and their cost
  distributed.

**Export guards**

- Export is blocked with a warning when the matched quantity exceeds or differs
  too much from the received quantity, or when the booking date is before the
  warehouse entry date.

**Usability**

- The execution order of document scripts is visible in the frontend.
- Enter and Tab move through fields on the keyboard.

---

## R1.6 — Sandbox 6 July 2027 · Production 15 July 2027

**Settings**

- Settings can be searched across all toggles and sub-pages.
- The e-mail server setup lets you replace an expired OAuth or client secret
  without setting the mailbox up again.
- The supplier item number map (item number conversion table) can be filled
  from a CSV import.

**Auto Accounting**

- Dimensions are stored in a new structure so large dimension sets load
  faster.

---

## R1.7 — Sandbox 21 September 2027 · Production 30 September 2027

**Auto Accounting on the approval screen**

- Approvers can work with auto accounting directly on the approval screen.
- Approval can be gated on accounting fields such as nominal code or country,
  with an AP correction when a document is returned.
- A tax code dropdown on Auto Accounting without setting up multiple tax
  lines.

---

## R2.0 — Sandbox to be announced · Production to be announced

**Auto Accounting**

- Fields backed by a list also accept free text.
- Required fields are validated.
- Model predictions fill accounting fields automatically (hybrid mode with the
  trained prediction model), with an audit trail of what the model filled.

<!-- Generated from Jira "Release No." (customfield_10392) on 2026-09-18 by the
     docbits-roadmap skill. Themes only; ticket keys, customer names and
     internal work are deliberately left out. Rerun the skill to refresh. -->
