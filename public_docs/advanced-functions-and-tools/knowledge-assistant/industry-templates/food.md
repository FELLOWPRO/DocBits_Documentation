# Knowledge Assistant for Food and Beverage

On audit day or when an incident is suspected, you find the evidence for a raw material, such as a supplier certificate, a specification or a CCP record, in its valid version and with the exact passage, once these documents are in your knowledge base.

<!-- VIDEO: rag/food/v1/en.mp4 noch nicht veröffentlicht -->

{% hint style="info" %}
The examples on this page use **invented demo data**: 30 fictitious documents for this industry. Company names, document numbers and values are made up.
{% endhint %}

## What the template provides

An administrator switches on the template for this industry under **Knowledge Assistant** → **Settings** → **Industry templates**. See [Tasks and where to find them](../tasks-and-where-to-find-them.md#switch-on-an-industry-template-administrator). The card then shows "On · 3 agents · 3 knowledge bases".

**Knowledge bases** (you upload your documents into them):

* Lieferanten und Rückverfolgung
* Spezifikationen und Kennzeichnung
* Qualitätssystem und HACCP

**Assistants** (you choose one in Chat):

* Rückruf- und Rückverfolgungs-Assistent
* Spezifikations- und Allergen-Assistent
* Wöchentliche Zertifikats- und Auditfristen

The names and descriptions come with the template and are currently in German. The same names appear under **Knowledge Base** and in the agent selection in Chat.

## Example questions from the demo set

| Question | Answer |
| --- | --- |
| What is the currently valid audit result for certificate IFS-2606-4336? | 78.6 % according to version 2. It replaces version 1 with 97.5 %. |
| Are there contradictory statements on shelf life for specification RS-2605-5290? | Yes: 269 days in the original and 464 days in the copy. Both files are linked. |
| Give the critical limit and the deviations for CCP record CCP-2610-4258. | 67 °C and 2 deviations, read from a scanned record. |

You can ask in German, English or French. In our tests the answer followed the language of the question, whatever the language of the document.

## What stays with you

* **Check:** every answer names its source. Open it and read the passage before you act. If something is not in your documents, the assistant says "not in the documents".
* **Control:** the template is off until your administrator switches it on. Switching it off removes the assistants; your documents stay.
* **Separation:** documents and answers are separated per organization.
* **Decision:** the assistant looks things up and compares. Approving, paying and assessing stay with your specialists. It gives no legal advice.

## Not tested with the demo set

The assistant does not approve labels, does not decide on a recall and does not block suppliers. It shows what your documents say. Lists and totals across many documents still come from your DocBits dashboard or your ERP.

How well the assistant works with your documents, such as long contracts, handwriting, stamps or poor copies, only a pilot with your own documents can show. See [What it can and cannot do](../what-it-can-and-cannot-do.md).
