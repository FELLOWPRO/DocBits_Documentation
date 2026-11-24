# Knowledge Assistant for Chemicals

Before anyone acts on an old version, a contradictory certificate or an expired specification, one question shows which value applies and where it is written.

<!-- VIDEO: rag/chemicals/v1/en.mp4 noch nicht veröffentlicht -->

{% hint style="info" %}
The examples on this page use **invented demo data**: 30 fictitious documents for this industry. Company names, document numbers and values are made up.
{% endhint %}

## What the template provides

An administrator switches on the template for this industry under **Knowledge Assistant** → **Settings** → **Industry templates**. See [Tasks and where to find them](../tasks-and-where-to-find-them.md#switch-on-an-industry-template-administrator). The card then shows "On · 3 agents · 3 knowledge bases".

**Knowledge bases** (you upload your documents into them):

<!-- CHECK-DEV: confirm knowledge base and assistant names on dev -->

* Safety data sheets and substance data
* Batches and certificates
* Compliance and deadlines

**Assistants** (you choose one in Chat):

* Safety data sheet checker
* Invoice reconciliation for chemicals
* Weekly report of deadlines and certificates

The exact names appear on the template card and in Chat.

## Example questions from the demo set

| Question | Answer |
| --- | --- |
| Which value currently applies to the quantity threshold in inspection report PB-2601-4654? | 161 t according to version 2. Version 1 stated 285 t and is no longer valid. Both files are linked. |
| Are there contradictory statements on the water content of batch CH-2601-6586? | Yes: 0.93 % in the original and 1.36 % in the copy, each with its file name. |
| Is specification SP-2601-6995 still valid today (23 November 2026)? | No. The document states "valid until 27.05.2025". |

You can ask in German, English or French. In our tests the answer followed the language of the question, whatever the language of the document.

## What stays with you

* **Check:** every answer names its source. Open it and read the passage before you act. If something is not in your documents, the assistant says "not in the documents".
* **Control:** the template is off until your administrator switches it on. Switching it off removes the assistants; your documents stay.
* **Separation:** documents and answers are separated per organization.
* **Decision:** the assistant looks things up and compares. Approving, paying and assessing stay with your specialists. It gives no legal advice.

## Not tested with the demo set

The invoice reconciliation, and the section-by-section reading of safety data sheets (sections 1 to 16), were not tested with the demo set. The assistant is a lookup aid: it does not replace the safety data sheet or a risk assessment, and it gives no legal advice.

How well the assistant works with your documents, such as long contracts, handwriting, stamps or poor copies, only a pilot with your own documents can show. See [What it can and cannot do](../what-it-can-and-cannot-do.md).
