# Knowledge Assistant for Transport, Customs and Aviation Parts

When a damage claim or an inspection comes in, you get the documents for a shipment together quickly, even from a scan, and you see differences between the papers before evidence is lost.

<!-- VIDEO: rag/transport/v1/en.mp4 noch nicht veröffentlicht -->

{% hint style="info" %}
The examples on this page use **invented demo data**: 30 fictitious documents for this industry. Company names, document numbers and values are made up.
{% endhint %}

## What the template provides

An administrator switches on the template for this industry under **Knowledge Assistant** → **Settings** → **Industry templates**. See [Tasks and where to find them](../tasks-and-where-to-find-them.md#switch-on-an-industry-template-administrator). The card then shows "On · 3 agents · 3 knowledge bases".

**Knowledge bases** (you upload your documents into them):

<!-- CHECK-DEV: confirm knowledge base and assistant names on dev -->

* Freight
* Customs and dangerous goods
* Aviation

**Assistants** (you choose one in Chat):

* Freight damage assistant CMR
* Evidence watch
* Parts provenance checker

The exact names appear on the template card and in Chat.

## Example questions from the demo set

| Question | Answer |
| --- | --- |
| Which vehicle plate and damage remark are recorded for shipment CMR-2602-1062? | Vehicle plate XX-NR 4471, damage remark "pallet tipped", with the consignment note as source. |
| Are there contradictory statements on the gross mass of customs declaration ZA-2609-9833? | Yes: 17,478 kg in the original and 8,194 kg in the copy. The assistant names both files and says that they contradict each other. |
| Is release certificate PN-2607-5726 still valid today (23 November 2026)? | The document says valid until 8 June 2025. The assistant states the date, points out the conflict with the status and leaves the decision to you. |

You can ask in German, English or French. In our tests the answer followed the language of the question, whatever the language of the document.

## What stays with you

* **Check:** every answer names its source. Open it and read the passage before you act. If something is not in your documents, the assistant says "not in the documents".
* **Control:** the template is off until your administrator switches it on. Switching it off removes the assistants; your documents stay.
* **Separation:** documents and answers are separated per organization.
* **Decision:** the assistant looks things up and compares. Approving, paying and assessing stay with your specialists. It gives no legal advice.

## Not tested with the demo set

Drafting a damage claim letter and the comparison of order, delivery note and release certificate for parts were not tested with the demo set. The assistant gives no legal advice, accepts no liability and releases no part.

How well the assistant works with your documents, such as long contracts, handwriting, stamps or poor copies, only a pilot with your own documents can show. See [What it can and cannot do](../what-it-can-and-cannot-do.md).
