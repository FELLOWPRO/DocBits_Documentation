# Knowledge Assistant for Trade and Wholesale

Before you approve an invoice, file a complaint about a delivery or renew a contract, the agreed term is in front of you together with the place in the document.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/rag/trade/v2/en.mp4" %}

_Demo with invented data · English · 1:18 min · Full HD_

[Video with subtitles](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/rag/trade/v2/en.html) · [Download video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/rag/trade/v2/en.mp4)

{% hint style="info" %}
The examples on this page use **invented demo data**: 30 fictitious documents for this industry. Company names, document numbers and values are made up.
{% endhint %}

## What the template provides

An administrator switches on the template for this industry under **Knowledge Assistant** → **Settings** → **Industry templates**. See [Tasks and where to find them](../tasks-and-where-to-find-them.md#switch-on-an-industry-template-administrator). The card then shows "On · 3 agents · 3 knowledge bases".

**Knowledge bases** (you upload your documents into them):

* Lieferantenverträge und Konditionen
* Artikel- und Produktdokumentation
* Lieferanten-Compliance und Zertifikate

**Assistants** (you choose one in Chat):

* Konditionen-Prüfer
* Reklamations-Assistent
* Wöchentlicher Fristenbericht

The names and descriptions come with the template and are currently in German. The same names appear under **Knowledge Base** and in the agent selection in Chat.

## Example questions from the demo set

| Question | Answer |
| --- | --- |
| State the payment term and notice period of supply contract LV-2607-9239. | 16 days and 11 months. Source: a scanned contract. |
| Are there contradictory statements on the packing unit of item AR-2605-3582? | Yes: 123 pieces in the original and 84 pieces in the copy. Both files are named. |
| Is complaint record RK-2604-5870 still valid today (23 November 2026)? | No. It is valid until 9 May 2025, with a note that the document still says "status: valid". |

You can ask in German, English or French. In our tests the answer followed the language of the question, whatever the language of the document.

## What stays with you

* **Check:** every answer names its source. Open it and read the passage before you act. If something is not in your documents, the assistant says "not in the documents".
* **Control:** the template is off until your administrator switches it on. Switching it off removes the assistants; your documents stay.
* **Separation:** documents and answers are separated per organization.
* **Decision:** the assistant looks things up and compares. Approving, paying and assessing stay with your specialists. It gives no legal advice.

## Not tested with the demo set

Checking an invoice against a framework contract and drafting a complaint were not tested with the demo set, which contains no invoices. The assistant does not pay, terminate or send anything.

How well the assistant works with your documents, such as long contracts, handwriting, stamps or poor copies, only a pilot with your own documents can show. See [What it can and cannot do](../what-it-can-and-cannot-do.md).
