# Debug Collector

The Debug Collector captures a complete snapshot of your DocBits session — network activity, errors, browser environment, and performance metrics — packages it as a JSON report, and (optionally) opens a support ticket directly from the same dialog.

## How to access

Press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> on Windows and Linux, or <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> on macOS. The Performance Report dialog opens immediately.

<figure><img src="../../.gitbook/assets/debug-collector-dialog.png" alt="Debug Collector dialog"><figcaption><p>The Performance Report dialog shows the captured snapshot and a built-in support ticket form.</p></figcaption></figure>

## What gets captured

* **API calls** — the last 60 REST and WebSocket calls, with timing, status codes, and the URLs that were hit. Calls slower than two seconds are flagged separately.
* **Errors** — recent JavaScript errors and unhandled promise rejections from the browser console.
* **Console logs** — the most recent log messages from the application.
* **Environment** — browser version, operating system, screen size, and active feature flags.
* **User context** — your role, organisation, and the page you were on when the snapshot was taken.
* **Performance metrics** — page load timings (LCP, FCP), memory usage, and DOM size.
* **Trace IDs** — correlation IDs that link the snapshot to backend log entries.

## Creating a support ticket from the dialog

You don't need to download or attach anything manually — the dialog has a **Create Support Ticket** form built in.

1. Fill in your email, leave the suggested subject or replace it, pick a priority, and add any notes that explain what you were doing when the issue happened.
2. Click **Send Report**. The JSON snapshot is attached and the ticket is created in one step.

That's it — support receives the ticket with all the data needed to reproduce.

If you want a local copy of the snapshot, use **Copy Debug Data** to copy the JSON to your clipboard, or your browser's Save As to keep the report as a `.json` file.

## Privacy and data handling

* Authentication tokens and sensitive headers are redacted from captured API calls before the snapshot is built.
* Nothing leaves your browser until you press **Send Report** — the shortcut only opens the dialog.

<mark>Review the snapshot before sending if you were handling documents containing customer data. Document IDs visible in URLs will appear in the report.</mark>
