---
hidden: true
noIndex: true
---

# Email

Go to the Settings menu and select “Import” under Document Processing.

<figure><img src="../../../../.gitbook/assets/email1.png" alt=""><figcaption></figcaption></figure>

Scroll to the bottom of the page and select the NEW button to create a new email import.

<figure><img src="../../../../.gitbook/assets/email2.png" alt=""><figcaption></figcaption></figure>

After pressing NEW, the following menu will be shown to you.

<figure><img src="../../../../.gitbook/assets/email3.png" alt=""><figcaption></figcaption></figure>

Here you can select which Protocol you would like.

<figure><img src="../../../../.gitbook/assets/email4.png" alt="" width="207"><figcaption></figcaption></figure>

## Supported attachment types

DocBits imports the following document attachments from incoming emails:

| Type | File extensions | Used for |
| --- | --- | --- |
| **PDF** | `.pdf` | Invoices, delivery notes, scanned documents |
| **TIFF** | `.tif`, `.tiff` | Scanned / faxed documents |
| **XML** | `.xml` | Structured e-invoices (e.g. ZUGFeRD/Factur-X, XRechning, Peppol) |
| **EDI** | – | Electronic Data Interchange messages |

{% hint style="info" %}
If a forwarding gateway re-labels a document as `application/octet-stream`, DocBits still detects it from the file content and extension, and `.eml` emails are unpacked so an inner PDF/XML is imported.
{% endhint %}

Other attachments are **not** imported:

* Images such as PNG, JPG, GIF or BMP — inline images (email signatures, logos) in forwarded mails are ignored automatically and never counted as failures.
* Office files (Word, Excel, PowerPoint) and other non-document formats.

If an email arrives without a supported attachment, and sender notification is enabled, the sender receives an email explaining that the document could not be imported, together with a link back to this page.
