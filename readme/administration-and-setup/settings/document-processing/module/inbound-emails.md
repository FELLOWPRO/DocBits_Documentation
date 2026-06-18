# Inbound Emails

### Overview

DocBits can pick up documents straight from email — no manual upload needed. There are **two ways** to bring email documents in, both managed under **Settings → Document Processing → Import**:

| Method | How it works | Best for |
|--------|--------------|----------|
| **Email Import account** | DocBits connects to a mailbox you own (**IMAP**, **OAuth Office365**, or **OAuth Office365 – Tenant**) and imports the documents it finds. | A dedicated mailbox that already receives your documents (e.g. `invoices@yourcompany.com`). |
| **Forward Emails (Inbound Emails)** | DocBits gives you a unique address; anyone you authorise can **forward** documents to it. | Ad‑hoc forwarding from many senders without sharing mailbox credentials. |

You can use either method on its own or both together.

### Method 1 — Connect a mailbox (Email Import)

Go to **Settings → Document Processing → Import** and open the **Email Import** section. Click **New** to add a mailbox connection.

<figure><img src="../../../../.gitbook/assets/inbound_emails_email_import_entry.png" alt="Email Import section with the New button"><figcaption><p>In the Email Import section, click <strong>New</strong> to connect a mailbox.</p></figcaption></figure>

The setup wizard opens. The first field, **Protocol**, decides how DocBits connects — choose **IMAP**, **OAuth Office365**, or **OAuth Office365 – Tenant**.

<figure><img src="../../../../.gitbook/assets/inbound_emails_protocol_select.png" alt="The Protocol dropdown showing IMAP, OAuth Office365 and OAuth Office365 - Tenant"><figcaption><p>The <strong>Protocol</strong> dropdown offers the three connection types.</p></figcaption></figure>

#### IMAP

For a standard mailbox, choose **IMAP** and fill in the server details and account credentials:

* **Server name** and **Port** (default `993`) of your mail server.
* **Encryption** — `SSL`, `TLS` or `None`.
* **Username**, **E‑Mail** and **Password** of the mailbox.

<figure><img src="../../../../.gitbook/assets/inbound_emails_imap.png" alt="IMAP connection form with server, port, encryption and credentials"><figcaption><p>The IMAP form: mail server connection plus the mailbox credentials.</p></figcaption></figure>

#### OAuth Office365

For a single Microsoft 365 user mailbox, choose **OAuth Office365**. Instead of a password, you authorise DocBits through Microsoft: pick the **Document Routing** target, then click **Authenticate** and complete the Microsoft sign‑in.

<figure><img src="../../../../.gitbook/assets/inbound_emails_o365.png" alt="OAuth Office365 form with Document Routing and an Authenticate button"><figcaption><p>OAuth Office365 connects through Microsoft sign‑in — no password is stored in DocBits.</p></figcaption></figure>

#### OAuth Office365 – Tenant

To connect at the tenant (organisation) level via an Azure app registration, choose **OAuth Office365 – Tenant** and enter the Azure credentials: **Tenant ID**, **Client App ID** and **Client App Value** (client secret). Use **Test connection** to verify, then **Save**.

<figure><img src="../../../../.gitbook/assets/inbound_emails_o365_tenant.png" alt="Azure Tenant Configuration with Tenant ID, Client App ID and Client App Value"><figcaption><p>OAuth Office365 – Tenant uses an Azure app registration (Tenant ID, Client App ID, client secret).</p></figcaption></figure>

{% hint style="info" %}
**Document Routing** decides where the imported documents go — **DocBits** (the standard dashboard) or **AI Workforce**. After connecting, the wizard’s next steps let you choose which mailbox **folder** to import from, an optional **shared mailbox**, and whether to **move** processed emails to another folder.
{% endhint %}

### Method 2 — Forward emails to DocBits (Inbound Emails)

This method needs the **Inbound Email** module to be switched on first. Go to **Settings → Document Processing → Module**, open the **Document Type** section, find **Inbound Email** and enable the toggle.

<figure><img src="../../../../.gitbook/assets/inbound_emails_1.png" alt="Enabling the Inbound Email module"><figcaption><p>Enable <strong>Inbound Email</strong> under Settings → Document Processing → Module.</p></figcaption></figure>

Once enabled, an **Inbound Emails** section appears under **Settings → Document Processing → Import**. It gives you everything needed to receive forwarded documents:

<figure><img src="../../../../.gitbook/assets/inbound_emails_forward.png" alt="Inbound Emails section: import address, predefined senders and failure-reply address"><figcaption><p>The Inbound Emails section: your import address, the predefined‑senders list, and the failure‑notification address.</p></figcaption></figure>

* **Import address** — a unique, system‑generated address in the form `org_id@environment.inbound.docbits.com`. Forward or send documents to this address and DocBits imports them automatically. Use the copy icon to grab it.
* **Import Document only from predefined E‑Mail(s)** — when enabled, only the sender addresses you list here are accepted; emails from anyone else are ignored. For each sender you may pick a **Sub‑Organization** (leave it empty to assign to the main organisation). Use **Add** to list more senders and **Delete** to remove one.
* **Reply to this email if import can not be done** — when enabled, enter an address that should be notified whenever an import attempt fails, so problems don’t go unnoticed.

Click **Save** to apply your changes.

{% hint style="info" %}
**Which attachments are imported?** DocBits imports **PDF**, **TIFF** and **XML** (e.g. eCOS / EDI e‑invoices) attachments, and unpacks forwarded `.eml` messages to import the documents inside. Detection is based on the **actual file content**, so attachments that a forwarding mail server re‑labels with a generic type (`application/octet-stream`) are still imported correctly. Inline images (signature logos / embedded graphics) are ignored. See [Import → Email Import](../import/README.md#email-import) for the full list and behaviour.
{% endhint %}

### When to use which

* **Use an Email Import account** when documents already land in a dedicated mailbox and you want DocBits to fetch them on its own — IMAP for generic mail servers, OAuth Office365 for Microsoft 365.
* **Use Forward Emails** when people should forward documents on demand, or when you don’t want to share mailbox credentials with DocBits.
* **Combine both** if some documents arrive in a fixed mailbox while others are forwarded ad‑hoc.

{% hint style="info" %}
Restricting senders (Method 2) and choosing the right **Document Routing** target (Method 1) are the two most common ways to keep an inbound pipeline clean — only the documents you expect, sent where you want them.
{% endhint %}
