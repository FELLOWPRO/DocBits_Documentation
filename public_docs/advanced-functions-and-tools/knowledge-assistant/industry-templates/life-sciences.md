# Knowledge Assistant for Life Sciences

Find expired supplier documents, superseded versions and contradictory figures yourself, before an auditor does. Every answer shows the document, its version and status, and the passage.

<!-- VIDEO: rag/life-sciences/v1/en.mp4 noch nicht veröffentlicht -->

{% hint style="info" %}
The examples on this page use **invented demo data**: 30 fictitious documents for this industry. Company names, document numbers and values are made up.
{% endhint %}

## What the template provides

An administrator switches on the template for this industry under **Knowledge Assistant** → **Settings** → **Industry templates**. See [Tasks and where to find them](../tasks-and-where-to-find-them.md#switch-on-an-industry-template-administrator). The card then shows "On · 3 agents · 3 knowledge bases".

**Knowledge bases** (you upload your documents into them):

* Gelenkte Dokumente (SOP-Bibliothek)
* Regelwerke und Leitlinien (mit Stand)
* Lieferanten, Qualitätsvereinbarungen und Zertifikate

**Assistants** (you choose one in Chat):

* SOP-Auskunft
* Regulatorik-Rechercheur
* Wöchentlicher Zertifikats- und Fristenbericht

The names and descriptions come with the template and are currently in German. The same names appear under **Knowledge Base** and in the agent selection in Chat.

## Example questions from the demo set

| Question | Answer |
| --- | --- |
| Is audit report AB-2606-5182 still valid today (23 November 2026)? | No. It was valid until 3 July 2025, although the document itself says "Status: valid". |
| What is the currently valid audit interval in quality agreement QV-2606-2101? | 33 months according to version 2. Version 1 stated 25 months and is superseded. Both files are listed as sources. |
| Are there contradictory figures for the 0.5 µm particle limit in guideline excerpt LL-2609-9744? | Yes: 342,228 per m³ in the original and 290,560 per m³ in the copy, with both sources. |

You can ask in German, English or French. In our tests the answer followed the language of the question, whatever the language of the document.

## What stays with you

* **Check:** every answer names its source. Open it and read the passage before you act. If something is not in your documents, the assistant says "not in the documents".
* **Control:** the template is off until your administrator switches it on. Switching it off removes the assistants; your documents stay.
* **Separation:** documents and answers are separated per organization.
* **Decision:** the assistant looks things up and compares. Approving, paying and assessing stay with your specialists. It gives no legal advice.

## Not tested with the demo set

The Knowledge Assistant is a lookup aid. It is **not a validated GxP system** and replaces neither your quality management system nor your deadline register. Every answer is a pointer that you check against the original. Patient data and raw study data do not belong in the knowledge bases. The demo set contains no CAPA or deviation reports, batch records or training records, so we make no statement about them.

How well the assistant works with your documents, such as long contracts, handwriting, stamps or poor copies, only a pilot with your own documents can show. See [What it can and cannot do](../what-it-can-and-cannot-do.md).
