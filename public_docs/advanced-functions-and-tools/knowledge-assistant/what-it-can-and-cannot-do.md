# What it can and cannot do

The Knowledge Assistant is a **research aid with sources**. It finds what is in your documents and shows where. It replaces neither checking at the source nor a professional, legal or quality-assurance decision. For chemistry, life sciences and dangerous goods in particular: **open the source and read the passage yourself before every decision.**

Our tests used invented, short and clean demo documents (30 per industry, eight industries). How well the assistant works with your documents only a pilot with your own documents can show.

Labels used below:

* **Proven in test:** observed this way in our tests (November 2026).
* **Known limitation:** applies today; we state it explicitly.
* **Planned / being fixed:** in progress or announced; not yet available.

## Answers

| Statement | Label |
| --- | --- |
| Answers come from your uploaded documents and name the document. A click opens the place where the answer was found. In the tests the assistant named the source for answerable questions, with two individual exceptions that did not recur. | Proven in test |
| In about 650 test questions, 654 of 656 were answered correctly through the programming interface and 143 of 144 in the browser. The failures were a page number off by one, an answer without a source reference and a weak difference question. This is a result with short demo documents, not a promise for your documents. | Proven in test |
| A language model can be wrong. For numbers that involve money, safety or deadlines, open the source. | Known limitation |
| If a detail is missing, the assistant says "not in the documents" (88 of 88 such test questions without an invented value). This means: not in the uploaded documents, not: does not exist. Source references can appear in that case; they are documents that were checked, not proof. | Proven in test |
| For contradictions between two versions the assistant names the newer one and points to the older one; for two different values it names both with their sources. | Proven in test |
| Validity questions: if an expired document itself carries the note "valid", the answer sometimes hedges. With the addition "Answer with yes or no and state the valid-until date." it was clear in the cases we checked. | Proven in test |
| Calculation questions across several documents (difference of two values) were answered correctly in the test. A difference question about a section number, which is not a quantity, was not. | Proven in test |
| Totals, lists and filters across many documents ("all open invoices over 10,000 EUR") come from the DocBits dashboard and the extracted fields, not from the Knowledge Assistant. | Known limitation |
| The Knowledge Assistant makes no decisions and gives no legal advice. Approving, paying and assessing stay with your specialists. It is not an archive; originals stay in your archive or document management system. | Known limitation |
| The Knowledge Assistant is not a validated system. For GxP uses, for example in life sciences, use it only as a lookup aid, not as a validated basis for decisions. | Known limitation |

## Documents and formats

| Statement | Label |
| --- | --- |
| PDF, scanned PDF, Word, Excel, Markdown, text and photos (as text) were read and answered with a source. The source preview works for these formats; for Excel the row is not highlighted, for images the text is not confirmed. | Proven in test |
| E-mail files (.eml) and XML files are rejected on upload. Import by web address is switched off. | Known limitation |
| Processing time was 8 to 23 seconds per document for small files (2 to 137 KB). We did not measure times for large files. | Proven in test |
| The screen states a maximum of 50 MB per file. We did not test files of that size, nor many large files at once. | Known limitation |
| Volume: we tested with 30 documents per knowledge base set. We did not test knowledge bases with hundreds or thousands of documents. | Known limitation |
| Long, clause-heavy contracts, correspondence, handwriting, stamps and poor copies are not tested; check against the source here. | Known limitation |
| The automatic short description of Excel and CSV documents sometimes fails. The content is still read and answers questions. | Known limitation |

## PDF tables

| Statement | Label |
| --- | --- |
| <!-- CHECK: assumption, no failure test; confirm or remove --> Tables in PDF are read **row by row**. In our tests, questions about a single entry, the highest and lowest value and the number of rows of an overview table were correct. Merged cells, several tables on one page and tables spanning several pages are not tested; check values there in the preview. | Known limitation |

## Scans

| Statement | Label |
| --- | --- |
| Scanned PDFs are read by text recognition and are then searchable. This applies to printed, clean, full-page scans. | Proven in test |
| Without reachable text recognition a scan stays without text; the document then ends with an error message instead of hanging. An image that covers only part of the page is not treated as a scan. | Proven in test |
| Please check handwriting, stamps and poor copies against the source. | Known limitation |

## Page numbers

| Statement | Label |
| --- | --- |
| For long documents (about 30 pages) the page number was correct for all ten questions in the repeat run; in the first run one was off by one page. A page number is not guaranteed: confirm the page in the preview. | Known limitation |

## Images and gallery

| Statement | Label |
| --- | --- |
| The gallery shows only images **embedded in documents** (for example in PDF or Word), and only if image processing is on. Photos and scans uploaded on their own do not appear there. | Known limitation |
| Descriptions of gallery images are currently empty ("No caption"); searching for description text in the gallery returns nothing. | Known limitation |
| Photos uploaded on their own are read by text recognition. Questions about the written text in the photo were correct in 24 of 24 runs. The assistant does not judge image content (for example "Is the pallet damaged?"). | Proven in test |
| <!-- CHECK-DEV FIX-FOTO --> Uploading a photo in the screens is blocked until image processing is on. | Planned / being fixed |

## Organizations, permissions and data

| Statement | Label |
| --- | --- |
| Each organization has its own area. A second organization got no access to the first one's knowledge base, documents, download and assistants. | Proven in test |
| Roles: someone who may only read (Viewer) cannot upload, change, delete or download. Members have Contributor rights by default. | Proven in test |
| Deleted documents no longer appear in answers; the storage is released. | Proven in test |
| **Sub-organizations are not separated.** The Knowledge Assistant separates by organization. All users of an organization see the same knowledge bases, even if they are assigned to different sub-organizations in DocBits. Plan confidential documents accordingly. <!-- CHECK: source-code analysis, not tested live --> | Known limitation |
| There is a storage quota per organization; when it is exceeded the upload is rejected. | Proven in test |

Questions about processing location, the language model used and data processing agreements are answered for your environment, bindingly, in your quotation. This documentation makes no statement about them.

## Language

| Statement | Label |
| --- | --- |
| German, English and French were tested. In all tests the answer language followed the question, even when the document was written in another language. This is **not guaranteed**; state the desired language in the question if needed. We did not test other languages. | Proven in test |
| The Knowledge Assistant screens are in English. <!-- CHECK-DEV: UI language --> Some messages still appear in Chinese. | Known limitation |

## Operation and functions

| Statement | Label |
| --- | --- |
| <!-- CHECK-DEV FIX-CHUNK --> Saving the section size in the knowledge base settings does not work reliably at the moment. | Planned / being fixed |
| Mermaid diagrams in Markdown documents are not drawn. | Known limitation |
| On screen, documents cannot be moved between knowledge bases; between folders within one knowledge base they can. | Known limitation |
| The copy of a knowledge base has the same name as the original. | Known limitation |
| DocBits documents (invoices, delivery notes, contracts) as a knowledge source without uploading again: the transfer is technically built, the selection on screen is missing. | In preparation |
| The weekly overview (Automations) is off by default, delivers its result into the assistant's history and sends no e-mail. In the tests it ran on manual start in all eight industries. | Proven in test |
| Tools that require signing in to an external service cannot currently be signed in to in the Knowledge Assistant. | Known limitation |
| Wiki and knowledge graph were tested on a separate demo knowledge base, not on the industry templates. | Known limitation |

## Response times

| Statement | Label |
| --- | --- |
| Response time was 6 to 9 seconds on average, single answers up to 25 seconds (several tests ran at the same time). Questions about contradictions took the longest (11 to 15 seconds). No answer took longer than 60 seconds. | Proven in test |

## Not available

These are not part of the Knowledge Assistant today and are not offered: web search, running code in a sandbox, chat channels such as e-mail or messengers, your own language models, separate sub-organizations and a desktop app. We state no date for any of them.

## Not tested (no statement possible)

* Chat attachments, the assistant's memory and automatic takeover from external data sources.
* Load from several organizations at once, very large imports, parallel uploads of files over 20 MB.
* Download of more than 200 documents or very large volumes.
* Behavior when the summary or embedding service fails during a text change.

See also: [Tasks and where to find them](tasks-and-where-to-find-them.md) and [Troubleshooting](troubleshooting.md).
