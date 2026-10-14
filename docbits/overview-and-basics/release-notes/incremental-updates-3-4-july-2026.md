# DocBits Release Notes — 3–4 July 2026

_A rundown of what changed for you in this DocBits release. Every service below
lists the version now running in production, followed by what's new or fixed in
plain language — no ticket numbers, no engineering jargon. Services not listed
had no customer-facing changes in this window._

---

## Highlights

- **Zero-downtime deploys, fleet-wide.** API, Auto Accounting, Docflow,
  Extraction, OCR, and PO Match now shut down cleanly when a new release rolls
  out. Previously, a request that was mid-flight during a deploy could be cut
  off; now every in-flight request finishes before the old version stops, so
  releases no longer cause brief blips for users.
- **E-invoice export improvements.** Exporting a document to multiple export
  configurations at once is now more reliable — duplicate-export checks run
  once per batch instead of per item, and a new export endpoint prevents the
  export status from flickering when several exports are triggered together.
  XRechnung/ZUGFeRD documents also get more consistent field mapping.
- **Steadier document processing.** Fixed a crash that could take down an
  entire OCR document when a single page failed, fixed the Purchase-Order
  delivery sync only ever fetching the first 100 records, and hardened several
  services against brief database-connection drops.
- **E-mail attachments recovered.** Fixed a case where e-mail attachments could
  arrive corrupted or missing bytes during inbound import.
- **Workflow reliability.** Fixed workflows getting stuck due to a lock that
  didn't clear correctly, and fixed rescheduling logic so skipped workflow
  steps are handled and logged correctly.
- **New: Ideas Service.** A new backend service (Ideas, v0.3.0) has joined the
  production fleet.

---

## API Service — live: `12.52.4`

- **OCR reliability:** a crash on a single page no longer fails the whole
  document.
- **Export:** duplicate-export checks now run once per batch instead of once
  per item; a new export endpoint prevents the export status from flickering
  when multiple exports run at the same time; XRechnung/ZUGFeRD documents get
  more consistent canonical field mapping.
- **Purchase Orders:** fixed delivery sync only fetching the first 100 records
  per order.
- **Activity Logs:** fixed the "Next" page button jumping to an unrelated time
  window.
- **Master Data Lookup:** fixed a server error (HTTP 500).
- **Search indexing:** added a delivery-proof marker and retry so documents are
  reliably queued for full-text search.
- **Zero-downtime deploys:** in-flight requests now finish before a release
  restarts the service.
- General stability fixes resolving several recurring background errors.

## Auth Service — live: `1.68.7`

- Internal reliability and maintenance only in this window.

## Auto Accounting — live: `1.18.8`

- **Zero-downtime deploys:** in-flight requests now finish before a release
  restarts the service.

## Barcode Service — live: `1.15.8`

- Internal deployment-configuration fix only in this window.

## Docflow Service — live: `2.5.3`

- **New export option** for sending a document to multiple export
  configurations at once.
- **Fixed workflows getting stuck** due to a lock that didn't clear correctly
  regardless of status.
- **Fixed workflow rescheduling** so skipped steps are handled and logged
  correctly instead of silently dropped.
- **Faster startup:** databases are now pre-warmed in the background.
- More resilient against brief database-connection drops.
- Improved date-field parsing for workflow cards.
- **Zero-downtime deploys:** in-flight requests now finish before a release
  restarts the service.

## Email Service — live: `1.37.9`

- **Fixed inbound attachments** that could arrive corrupted or missing bytes.
- **Clearer errors** when a mailbox folder can't be fetched, instead of a
  generic failure.

## Extraction Service — live: `1.49.6`

- **Fixed crashes** on documents with an unrecognised document type and on
  tables with an unusual/malformed shape.
- More resilient against brief database-connection drops mid-query.
- **Zero-downtime deploys:** in-flight requests now finish before a release
  restarts the service.

## FTP Service — live: `1.30.3`

- Internal framework upgrade only in this window.

## Fulltext Service — live: `1.36.3`

- **Search indexing:** a periodic sweep now repairs any documents that failed
  to reach the search index for any organisation.
- **ERP sync:** fixed a stuck lock that could block ERP synchronisation after
  a failed retry.

## OCR Service — live: `1.7.8`

- **Fixed OCR authentication** so organisation API keys work correctly again.
- **Zero-downtime deploys:** in-flight requests now finish before a release
  restarts the service.

## Operator Service — live: `1.39.7`

- Internal deployment-reliability fixes only in this window.

## PO Match Service — live: `1.56.0`

- **Fixed a crash** when sorting PO Match quantities that included empty
  values.
- **Zero-downtime deploys:** in-flight requests now finish before a release
  restarts the service.

## Web App — live: `10.36.9`

- **Fixed an error** when returning to Field Validation from another screen.
- **Fixed the "Scripts" button** routing to a 404 page.
- **Activity Logs:** fixed an incorrect "Page 2 of 1" display and fixed the
  WARN severity filter matching nothing.

---

## No customer-facing changes in this window

Auth Service, Barcode Service, FTP Service, Operator Service, and Docnet
Service (`1.54.6`, unchanged) received internal or deployment-configuration
maintenance only.

<!-- Generated by the docbits-changelog skill (version-boundary mode: exact
     git ranges between the ALT and NEU version-bump commits supplied by the
     user, per service). Window ~2026-07-01 → 2026-07-04. -->
