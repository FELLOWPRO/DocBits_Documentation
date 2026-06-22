---
hidden: true
noIndex: true
---

# Email

DocBits can import documents from email in two ways. Both are configured under **Settings → Import** (Document Processing).

## Method 1 — Email Import (connect a mailbox)

Connect an email account and DocBits automatically imports documents as new emails arrive. On the Import page, open the **Email Import** section and click **+ New**.

<figure><img src="../../../../.gitbook/assets/email_import_section.png" alt="Email Import section"><figcaption>Email Import — connect a mailbox for automatic document import</figcaption></figure>

Then choose the protocol for your mailbox:

* **IMAP** — see [IMAP](imap.md)
* **OAuth (Office 365)** — see [OAuth Office365](oauth-office365.md)

## Method 2 — Inbound Emails (forward to DocBits)

Forward — or send — emails directly to your organisation's unique inbound address and DocBits imports the attachments automatically. No mailbox connection is required. Open the **Inbound Emails** section on the Import page.

<figure><img src="../../../../.gitbook/assets/inbound_emails_section.png" alt="Inbound Emails section"><figcaption>Inbound Emails — forward documents to your DocBits address</figcaption></figure>

* **Info / E-Mail** — your organisation's unique inbound address (format `<org-id>@inbound.docbits.com`). Forward your documents to this address; use the copy icon to copy it.
* **Import Document only from predefined E-Mail(s)** — when enabled, only emails from the senders you add to the whitelist are imported; emails from any other sender are ignored.
* **Reply to this email if import can not be done** — sends an automatic reply to the sender when the import fails.
* **Notify sender when import fails** — notifies the sender if their email could not be imported.
* **Logs** — open the inbound email processing log. Click **Save** to apply your changes.
