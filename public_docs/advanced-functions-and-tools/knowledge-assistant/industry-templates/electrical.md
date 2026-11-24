# Knowledge Assistant for Electrical and Industrial Goods

Before a certificate goes to your customer or you commit to a warranty payment, one answer shows which version applies, whether the document has expired and whether two copies contradict each other.

<!-- VIDEO: rag/electrical/v1/en.mp4 noch nicht veröffentlicht -->

{% hint style="info" %}
The examples on this page use **invented demo data**: 30 fictitious documents for this industry. Company names, document numbers and values are made up.
{% endhint %}

## What the template provides

An administrator switches on the template for this industry under **Knowledge Assistant** → **Settings** → **Industry templates**. See [Tasks and where to find them](../tasks-and-where-to-find-them.md#switch-on-an-industry-template-administrator). The card then shows "On · 3 agents · 3 knowledge bases".

**Knowledge bases** (you upload your documents into them):

<!-- CHECK-DEV: confirm knowledge base and assistant names on dev -->

* Product documentation
* Suppliers and certificates
* Service

**Assistants** (you choose one in Chat):

* Conformity assistant
* Invoice checker for industrial goods
* Weekly report: expiring certificates, declarations and contracts

The exact names appear on the template card and in Chat.

## Example questions from the demo set

| Question | Answer |
| --- | --- |
| Are there contradictory figures for the tensile strength of heat SZ-2609-7050? | Yes: 399 N/mm² in the original test certificate and 625 N/mm² in the copy. Both files are named. |
| Is warranty GB-2610-4566 still valid today (23 November 2026)? | No. The terms say "valid until 07.02.2025", although the document carries the note "status: valid". |
| Which labour time currently applies to service report SB-2611-4115? | 2.6 hours from version 2. The 9.1 hours from version 1 no longer apply. |

You can ask in German, English or French. In our tests the answer followed the language of the question, whatever the language of the document.

## What stays with you

* **Check:** every answer names its source. Open it and read the passage before you act. If something is not in your documents, the assistant says "not in the documents".
* **Control:** the template is off until your administrator switches it on. Switching it off removes the assistants; your documents stay.
* **Separation:** documents and answers are separated per organization.
* **Decision:** the assistant looks things up and compares. Approving, paying and assessing stay with your specialists. It gives no legal advice.

## Not tested with the demo set

Matching an invoice against an order is not shown with the demo set. The assistant does not release conformity and does not assess standards; release and payment stay with you.

How well the assistant works with your documents, such as long contracts, handwriting, stamps or poor copies, only a pilot with your own documents can show. See [What it can and cannot do](../what-it-can-and-cannot-do.md).
