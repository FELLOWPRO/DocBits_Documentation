# Debug Collector

The Debug Collector captures a complete snapshot of your DocBits session — network activity, errors, browser environment, and performance metrics — and packages it as a single HTML report. Attach the report to a support ticket and we have everything needed to reproduce what you saw.

## How to access

Press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> on Windows and Linux, or <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> on macOS. The Performance Analysis dialog opens immediately.

<figure><img src="../../.gitbook/assets/debug-collector-dialog.png" alt="Debug Collector dialog"><figcaption><p>The Performance Analysis dialog shows the last collected snapshot.</p></figcaption></figure>

## What gets captured

A snapshot contains everything support needs to investigate an issue:

* **API calls** — the last 60 REST and WebSocket calls, with timing, status codes, and the URLs that were hit. Long-running calls (over two seconds) are flagged separately.
* **Errors** — recent JavaScript errors and unhandled promise rejections from the browser console.
* **Console logs** — the most recent log messages from the application.
* **Environment** — browser version, operating system, screen size, and active feature flags.
* **User context** — your role, organisation, and the page you were on when the snapshot was taken.
* **Performance metrics** — page load timings (LCP, FCP), memory usage, and DOM size.
* **Trace IDs** — correlation IDs that link the snapshot to backend log entries.

## Generating a snapshot

Open the dialog with the shortcut and review the data. Use the **Generate report** button to produce an HTML file you can save locally or attach to a support ticket. The report opens in a new tab and can be downloaded with the browser's Save As dialog.

## Submitting to support

The Debug Collector report includes trace IDs (Faro, support_trace_id, search_trace_id) that link your snapshot to the backend. When you open a ticket, attach the HTML report — our support team can correlate it with server-side logs without asking you for additional information.

## Privacy and data handling

The Debug Collector is designed to be safe to attach to a ticket:

* Authentication tokens and sensitive headers are redacted from captured API calls.
* The snapshot is local until you explicitly export or share it.
* No data is sent automatically — pressing the shortcut only shows you the dialog.

<mark>Review the snapshot before sharing if you handled documents containing customer data. Any document IDs visible in URLs will appear in the report.</mark>
