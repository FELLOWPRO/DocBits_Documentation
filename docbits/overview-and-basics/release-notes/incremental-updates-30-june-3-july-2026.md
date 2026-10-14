# Hotfixes 30 June – 3 July 2026

_What this prod upgrade delivered, in plain language. Each service shows the
version now live on production. Services not listed had no customer-facing changes
in this window._

---

## Highlights

- **AI chat on Activity Logs.** A new AI chat panel on the Activity Logs page lets
  you ask questions about log activity directly, without digging through raw
  entries.
- **Outbound e-mail import tracking.** The Import Log now records outbound mail
  alongside inbound, with quick-filter chips for Errors / Inbound / Outbound —
  failing mailboxes are automatically deactivated after repeated failures, admins
  can be notified by e-mail on import failure, and retries now run up to 15 times
  over roughly 5 hours before giving up.
- **Clearer e-mail import errors.** Login failures now show the real underlying
  reason, with dedicated messages for an invalid certificate or a wrong Gmail
  app-password.
- **Login loop fixed.** Some users could get stuck in a repeated sign-in loop
  during token refresh — resolved.
- **Steadier document processing.** Fixed a crash during data extraction from
  unrounded coordinate values, barcode reading now retries recoverable failures
  instead of giving up silently, and a rare case where a document could be
  exported twice at the same time is fixed.
- **Validation screen improvements.** You can now zoom further into documents,
  fields no longer get cleared by scripts when their value hasn't actually
  changed, and the dashboard remembers your page position when you navigate back.

---

## Web App — live: `10.35.7`

- **AI chat panel** added to the Activity Logs page (#15512).
- **Import Log:** new Errors / Inbound / Outbound quick-filter chips; failure
  notification recipients toggle and field for inbound e-mail settings.
- **Validation screen:** document zoom now goes beyond the previous default size;
  fields emptied by validation scripts now correctly keep their value when the
  script returns the same value.
- **Dashboard:** page position is kept when navigating back to the table; the
  column-resize handle no longer spills outside the table header.
- **Auto Accounting screen:** fixed a validation error.
- **DocBits Tasks:** fixed a permissions issue.
- **Watchdog logs:** added a time-range filter and an adjustable rows-per-page
  selector.
- **Fixes:** a chart error ("Element not found") on the Boards page; a broken
  delete-export link on Activity Logs; layout fixes on the Layout Builder screen;
  a missing translation on the Activity Logs time-range filter.
- **Auto-update:** further hardening of the automatic app-update mechanism
  (faster boot cleanup, more reliable version detection, cache purge before a
  recovery reload).

## API Service — live: `12.48.1`

- **Faster document-script loading:** validation scripts are now cached
  server-side (6-hour cache) instead of being fetched every time.
- **More accurate amount confidence:** confidence scoring now accounts for
  documents that use different decimal-separator conventions.
- **Reliability:** document validation always runs the single active script
  version, and which version ran is now logged; a rare case where a document
  could be exported twice at the same time is fixed; supplier-specific
  extraction rules apply correctly again after a forced re-OCR.
- **E-mail import:** backend support added for outbound-mail logging and
  failure-notification e-mails (see Email Service, below).

## Auth Service — live: `1.68.5`

- **Fixed a login loop** some users could hit while their session token was
  being refreshed.
- **Faster organisation-admin screens:** user and subscription data now loads in
  bulk instead of one record at a time.
- **Fixed a rare database conflict** when linking a user to an organisation.

## Email Service — live: `1.37.4`

- **Import Log now tracks outbound mail** as well as inbound, with a filter to
  show only inbound, outbound, or failed imports.
- **Failing mailboxes are now auto-deactivated** after repeated failures, and
  admins can be notified by e-mail when an import fails; retries now run up to
  15 times over roughly 5 hours before giving up.
- **Clearer login-failure messages:** shows the real underlying reason, a
  dedicated message for an invalid certificate, and a specific message for a
  wrong Gmail app-password.
- **Fixed inbound routing** incorrectly rewriting server addresses for
  EU-region accounts.
- More resilient against brief Redis connection drops.

## Extraction Service — live: `1.49.0`

- **Fixed a crash during extraction** caused by unrounded coordinate values.
- **More accurate amount confidence** for documents with mixed decimal-separator
  formats; small tax-total rounding differences no longer block a match.

## Docflow Service — live: `2.4.2`

- **Reworked authentication for advanced (Celery-based) workflows**, with
  guards so a failed authentication check can no longer crash a workflow run.
- **Clearer response** when a workflow step tries to run against a workflow
  that no longer exists.

## Barcode Service — live: `1.15.7`

- **Barcode reading now automatically retries** recoverable failures instead of
  silently giving up.

## OCR Service — live: `1.7.3`

- **Fixed an OCR failure** caused by a Redis hostname-lookup issue.
- Health-check Redis disconnects are no longer logged as errors, cutting down
  false alerts.

## PO Match Service — live: `1.55.8`

- **Fixed notes not appearing** on PO Match records.

---

## No customer-facing changes in this window

Stable, no notable product changes between 30 June – 3 July: Auto Accounting
(`1.18.7`), Docnet (`1.54.6`), FTP (`1.30.2`), Fulltext (`1.35.7`), Operator
(`1.39.5`). Auto Accounting received internal deployment-configuration
maintenance only. Ideas Service could not be reached for a version check during
this window.

<!-- Generated by the docbits-changelog skill (version-boundary mode, resolved
     from the prod version table supplied by the user). Window 2026-06-30 →
     2026-07-03. -->
