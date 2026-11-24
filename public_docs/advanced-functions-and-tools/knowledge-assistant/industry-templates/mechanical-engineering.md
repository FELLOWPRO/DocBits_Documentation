# Knowledge Assistant for Mechanical and Plant Engineering

Your service team gives every answer on maintenance, spare parts and suppliers from the valid document, with the source in view, so no technician sets off with the wrong part or an outdated plan.

<!-- VIDEO: rag/mechanical-engineering/v1/en.mp4 noch nicht veröffentlicht -->

{% hint style="info" %}
The examples on this page use **invented demo data**: 30 fictitious documents for this industry. Company names, document numbers and values are made up.
{% endhint %}

## What the template provides

An administrator switches on the template for this industry under **Knowledge Assistant** → **Settings** → **Industry templates**. See [Tasks and where to find them](../tasks-and-where-to-find-them.md#switch-on-an-industry-template-administrator). The card then shows "On · 3 agents · 3 knowledge bases".

**Knowledge bases** (you upload your documents into them):

* Technische Dokumentation und Konformität
* Service, Ersatzteile und Störungen
* Lieferanten, Einkauf und Qualitätsnachweise

**Assistants** (you choose one in Chat):

* Konformitäts-Assistent Maschinenverordnung
* Service-Assistent Ersatzteile und Störungen
* Wöchentliche Frist- und Zertifikatsübersicht

The names and descriptions come with the template and are currently in German. The same names appear under **Knowledge Base** and in the agent selection in Chat.

## Example questions from the demo set

| Question | Answer |
| --- | --- |
| Are there contradictory statements on the lead time of spare part ET-2607-2048? | 18 days in the original parts list and 3 days in the copy. One click on the source opens the document at that place. |
| Is agreement QS-2603-4841 still valid today (23 November 2026)? | No. It was valid until 25 March 2025. |
| Which maintenance interval currently applies to plan WP-2603-6421? (asked in English) | 2,521 operating hours according to version 2; version 1 with 4,055 has been replaced. The answer comes in English. |

You can ask in German, English or French. In our tests the answer followed the language of the question, whatever the language of the document.

## What stays with you

* **Check:** every answer names its source. Open it and read the passage before you act. If something is not in your documents, the assistant says "not in the documents".
* **Control:** the template is off until your administrator switches it on. Switching it off removes the assistants; your documents stay.
* **Separation:** documents and answers are separated per organization.
* **Decision:** the assistant looks things up and compares. Approving, paying and assessing stay with your specialists. It gives no legal advice.

## Not tested with the demo set

The assistant reads text only. It does not understand drawings or image content. It does not approve conformity and does not replace a technical or legal review.

How well the assistant works with your documents, such as long contracts, handwriting, stamps or poor copies, only a pilot with your own documents can show. See [What it can and cannot do](../what-it-can-and-cannot-do.md).
