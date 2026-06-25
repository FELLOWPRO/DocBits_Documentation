# DocBits Release Notes — 21–25 June 2026

_What this prod upgrade delivered, in plain language. Each service shows the
version now live on production. Services not listed had no customer-facing changes
in this window._

---

## Highlights

- **Smarter dashboard search.** Search documents reliably by amounts and numbers —
  find invoices above a value, or search by **requisition number** — with amount
  ranges that compare real numbers, not text. Invoice sub-types are searchable by
  their translated names.
- **Reliable e-mail notifications.** Status-change alerts now go out for every
  status (no more silently dropped e-mails), and inbound-import receipts and
  failure notices are now properly DocBits-branded with per-recipient controls.
- **Smoother sign-in across regions (EU/US).** Region switching is now a small
  banner instead of a full-screen interruption, single sign-on lands in the
  correct region, and staying signed in across multiple browser tabs is more
  reliable.
- **Permissions fixes.** Users get the access their group grants them — opening,
  editing, approving and restarting documents now work correctly even when groups
  and permissions are configured in less common ways.
- **Steadier document processing.** Documents that previously got stuck after
  upload are automatically picked up again, and a burst from one customer no
  longer slows down others.

---

## Web App — live: `10.32.4`

- **Quick search jump (Cmd/Ctrl + K)** straight to the **E-Invoice Validation**
  setting.
- **Region & sign-in:** region switch shown as a persistent banner instead of a
  blocking screen; single sign-on now redirects to the correct region (EU/US);
  staying logged in across multiple tabs is more reliable.
- **Permissions:** fixed cases where users couldn't **approve**, **edit**, **open**
  or **restart** documents despite having the right group permissions.
- **Inbound e-mail settings:** new “Notify sender” and “Reply to sender on receipt”
  toggles.
- **Usability:** the duplicate-document warning now must be dismissed before
  continuing; the “backend unavailable” banner only appears during real outages;
  task counters update immediately when tasks are completed; dark-mode fix on the
  AI table validation screen.
- **Performance:** fixed a freeze on the e-document screen during field validation
  and PO matching.
- **Search invoice sub-types by their translated names.**

## API Service — live: `12.41.9`

- **Dashboard search overhaul:** requisition number and requisitioner are now
  searchable; amount and number searches return correct results (true numeric
  comparison); total net amount and calculated columns display correctly.
- **Reliable status-alert e-mails** for any document status, with send failures no
  longer hidden.
- **Permissions:** users without a group can open and approve their own documents;
  document visibility for group-less users restored.
- **Document processing reliability:** documents stuck in “new” are automatically
  re-queued; fair-share processing so a large burst from one organisation doesn’t
  starve others; self-healing for rare database sequence issues.
- **Scanned PDFs with a broken text layer are routed to OCR** instead of producing
  unreliable text.
- **Extraction & PO accuracy:** supplier name filled from the connected purchase
  order; duplicate item-number columns removed; better handling of special
  (non-breaking) spaces.
- **Infor ERP / SAP export:** fixed SFTP export authentication.
- **E-invoicing:** ZUGFeRD / e-document extraction-path refinements.

## Auth Service — live: `1.66.0`

- **Fixed missing organisation assignment** for some users (empty org id).

## Docflow Service — live: `2.3.4`

- **Workflow trigger cooldown** is now configurable per environment.

## Email Service — live: `1.35.9`

- **Branded e-mails:** inbound-import receipts and failure notices now use the real
  DocBits logo and colours.
- **Per-organisation controls:** confirmation e-mail on receipt, “notify sender”
  on failure, and reply-to-sender options.
- **More reliable inbound import:** import results are recorded correctly, partial
  failures are reported as failures (not silent successes), and problem characters
  in e-mail bodies no longer break import.
- **EU/US routing:** per-organisation routing to the correct regional API.

## Fulltext Service — live: `1.34.5`

- **Search by amounts and numbers** now works reliably, including thousands
  separators and amount ranges (the engine behind the dashboard search overhaul).
- **Steadier search infrastructure:** orphaned background queues are cleaned up so
  they no longer tie up shared resources.

## PO Match Service — live: `1.54.7`

- **More robust purchase-order matching:** text-based packaging/packing-unit codes
  no longer block a match, and manual line matching handles empty results safely.

---

## No customer-facing changes in this window

Stable, no notable product changes between 21–25 June: Auto Accounting (`1.18.5`),
Barcode (`1.15.6`), Docnet (`1.54.6`), Extraction (`1.48.6`), FTP (`1.30.0`),
OCR (`1.6.8`), Operator (`1.39.5`).

<!-- Generated by the docbits-changelog skill (prod-delta mode). Versions read live
     from prod (do-fra1-polydocs/prod); window 2026-06-21 → 2026-06-25. -->
