# Tasks and where to find them

Everything starts in the DocBits client under **Knowledge Assistant**. On the left you find **Chat**, **Knowledge Base**, **Agents**, **Automations** and **Settings**. You ask questions in **Chat**, manage documents in the **Knowledge Base**, and an administrator switches on the industry template under **Settings**.

The Knowledge Assistant screens are currently in English, so the names below appear exactly as on screen. <!-- CHECK-DEV: UI language of the Knowledge Assistant on dev; adjust this sentence -->

Status column: **Available** works in our tests. **Limited** works with the stated limitation. **Not available** is deliberately switched off or not offered. **In preparation** is not yet released to users.

## Task and click path

| Task | Click path | What happens | Status |
| --- | --- | --- | --- |
| Switch on the Knowledge Assistant | Settings → Modules → Document Integration → card **Knowledge Assistant** (administrator) | The **Knowledge Assistant** entry appears in the menu. | Available <!-- CHECK-DEV: confirm module card path and wording --> |
| Switch on an industry template | Knowledge Assistant → Settings → **Industry templates** (administrator only) | Three knowledge bases and three assistants are created. | Available |
| Ask a question | Knowledge Assistant → Chat → choose an assistant under **Custom Agents** → type the question | You get an answer with source references. | Available |
| Open a source | Chat → click the source reference below the answer | The document opens on the right at the place where the answer was found. | Available; limited for Excel and images |
| Start a new conversation | Chat → **New chat** | An empty conversation without the earlier history. | Available |
| Create a knowledge base | Knowledge Base → **Create Knowledge Base** | You choose type and indexing and enter a name. | Available |
| Upload documents | Knowledge Base → open a knowledge base → **Add Document** → **Upload Document** | The files are read and made searchable. | Available; photos limited |
| Upload a whole folder | Knowledge Base → **Add Document** → **Upload Folder** | The folder structure is kept. | Limited: the structure was tested, the selection dialog was not |
| Write text directly | Knowledge Base → **Add Document** → **Online Edit** | You write a Markdown document and release it with **Publish**. | Available |
| Read the processing status | Knowledge Base → knowledge base → document list, **Status** column | Completed, Failed or May be stuck; a click shows the parsing timeline. | Available |
| Process a document again | Select a document → **Rebuild Document** | The document is read again. | Available |
| Folders and tags | Knowledge Base → knowledge base → folder tree on the left; **Add tags** in the document row | Documents can be sorted and filtered. | Available |
| Move documents between folders | Select documents → **Move to folder** | The document changes folder without being read again. | Available |
| Download several documents | Select documents → **Download selected** | You get a ZIP file with the originals. | Available |
| Edit text sections | Open a document → section list → pencil on the section | The changed text is used for answers right away. | Available |
| Maintain metadata | Open a document → metadata pencil | Up to 20 custom fields per document. | Available |
| Trace changes | Knowledge base → Settings (gear) → **Management & Audit** → **Activity** | A list of creation, upload and changes with time and person. | Available |
| View images from documents | Knowledge base → **Gallery** tab | Shows images embedded in documents. | Limited |
| Weekly overview | Knowledge Assistant → **Automations** | An assistant compiles an overview of expiring documents. | Limited |
| Copy a knowledge base | **Copy** function of the knowledge base | The copy is created in the background, including folders. | Limited: the path in the screens was not checked separately |
| Move documents between knowledge bases | – | Not offered in the multi-selection. | Not available |
| Fetch a document by web address | – | Import by web address is switched off. | Not available |
| Use DocBits documents as a knowledge source | – | Use invoices and contracts from DocBits without uploading again. | In preparation |

## Switch on the Knowledge Assistant (administrator)

<!-- CHECK-DEV: replace with real screenshot and exact wording of the module card after dev is green -->

1. Open **Settings** → **Modules** → **Document Integration**.
2. Find the card **Knowledge Assistant** and switch it on.
3. Reload DocBits. The **Knowledge Assistant** entry now appears in the menu.

{% hint style="info" %}
If the **Knowledge Assistant** entry is missing in the menu, the module is not switched on for your organization. Ask your administrator.
{% endhint %}

## Switch on an industry template (administrator)

Open **Knowledge Assistant** → **Settings** → **Industry templates**. Templates exist for Construction, Chemicals, Electrical, Trade, Food, Life sciences, Mechanical engineering and Transport. See [Industry templates](industry-templates/README.md) for what each one provides.

1. Open the card of your industry and switch it on. The card then shows "On · 3 agents · 3 knowledge bases".
2. Upload documents to the knowledge bases.
3. To switch it off, choose **Switch off**. The assistants disappear; knowledge bases and documents stay. Switching it on again creates no duplicates.

Only administrators see the **Industry templates** tab. Members without administrator rights use Chat and the existing assistants.

## Ask a question and open the source

Open **Chat**, choose an assistant under **Custom Agents** and ask your question. Every answer with a place of origin shows a source reference. A click opens the preview on the right. PDF, scanned PDF, Word, Markdown and text show the place where the answer was found.

* **Excel:** The file opens, but the row is not highlighted. The preview says "Could not pinpoint the cited passage; the original is open".
* **Images and photos:** The preview shows the image. The text inside is not confirmed ("exact text not confirmed").
* Source references can also appear next to "not in the documents". They list documents the assistant checked; they are not proof of a value.
* **Be precise**, for example by using the document number. If you ask about a number that does not exist, the assistant answers "not in the documents" instead of giving the value of a similar number.

<!-- screenshot: chat answer with source reference (dev) -->

## Upload documents and read the status

1. Knowledge Base → open a knowledge base → **Add Document** → **Upload Document**.
2. Choose files. On the confirmation page you can set tags and options, for example whether a summary is created. Then choose **Upload and parse**.
3. The upload panel shows counters ("Parsing 0 of 7") and intermediate states ("Waiting to parse", "Generating summary...", "Searchable, still optimizing", "Done"). You can leave the page; processing continues.

Notes on files:

* The screen states a maximum of **50 MB per file** for PDF, office formats, text and Markdown. We have not tested files of that size.
* In our tests PDF, scanned PDF, Word, Excel, Markdown, text and photos were read. E-mail files (.eml) and XML files are rejected, and so are empty files.
* Uploading the same file again is rejected; the existing one stays unchanged.
* **Photos:** <!-- CHECK-DEV: photo upload after fix (FIX-FOTO). Replace the next sentences with the verified behavior. --> **Upload and parse** stays disabled for photos until image processing ("Multimodal") is switched on and a model is chosen. This is a known limitation.

### Status

| Display | Meaning | What to do |
| --- | --- | --- |
| Completed | Read and searchable. | Nothing. |
| Failed | Processing failed; the message is shown on the card. | Select the document → **Rebuild Document**. If it fails again, see [Troubleshooting](troubleshooting.md). |
| May be stuck | No progress for a while. | Open the timeline, choose **Stop parsing**, then **Rebuild Document**. Without action the document is set to Failed automatically after a while. |

Open the **parsing timeline** by clicking the document. It shows the phases (read document, form sections, vectors, post-processing) with their duration. If there is a stall, a notice appears: "No progress for N minutes; this may be stuck".

When a stall ends automatically, the error message reads "task stuck in processing…". Use **Rebuild Document** to try again.

<!-- CHECK-DEV: timeline tooltip (FIX-TOOLTIP). If still showing raw keys keep the next sentence; otherwise delete it. -->
In the timeline tooltip, some processing settings still show technical names instead of readable text. This does not affect processing.

## Create a knowledge base

Knowledge Base → **Create Knowledge Base**. You choose:

* **Content type:** Documents or FAQ.
* **Indexing (Indexing Strategy):** "RAG Search" for searching documents, "Wiki" for linked wiki pages. The knowledge graph is a separate tab (**Knowledge Graph**).
* **Images:** the **Image Processing** tab controls how images inside documents are processed.

The models for embedding, summary and image processing are predefined; you do not choose an embedding model. You can change the indexing while the knowledge base is empty, but not afterwards ("The indexing strategy cannot be changed once the knowledge base contains content").

<!-- CHECK-DEV: chunk size saving (FIX-CHUNK). Replace the caution below with the verified behavior. -->
{% hint style="warning" %}
**Saving the section size:** Saving the section size (**Chunking Settings**) with **Save and Close** does not work reliably at the moment: the change may not take effect and existing settings may be reset. Do not change these values for now. Viewing them and closing without saving is harmless.
{% endhint %}

## Folders and tags

* The **folder tree** is on the left in the knowledge base. Move documents with **Move to folder**; they are not read again.
* Moving a folder into its own subfolder is rejected. We tested renaming, moving and merging folders through the DocBits interface for developers (API), not separately in the screens.
* **Tags:** use **Add tags** in the document row, or select several documents and choose **Batch Tag**. Caution: **Batch Tag replaces the existing tags** of the selected documents.
* Filtering by several tags shows documents that have any one of the tags (OR).
* Automatic tags (Auto-Tag, at most 3 per document) are optional, off by default and only affect documents processed after you switch them on.

## Edit text sections

In a document, the section list shows a pencil, the history and a switch for each section. After you save, the section is indexed again and answers use the new text. Earlier versions stay in the history and can be restored. If two people edit the same section at the same time, the second person gets a conflict message ("Chunk was modified by another user") and has to reload. After a change you can regenerate the document summary or enter it by hand.

## Metadata

Each document can have up to 20 custom fields (shown as "20/20"). A 21st field is rejected.

## Copy, move and download

* **Copying a knowledge base** runs in the background and takes over documents and folders. The copy has the same name as the original; rename it so you can tell them apart.
* **Bulk download:** select documents → **Download selected**. You get a ZIP file with the original file names. Only roles with edit rights (Contributor and above) may download; Viewers may not.
* We did not test downloading more than 200 documents or very large volumes.

## Wiki, knowledge graph and gallery

* **Gallery** (tab next to Documents): shows images **embedded in documents** (for example in PDF or Word), provided image processing is on. Photos uploaded on their own do not appear there; they are read by text recognition and are available for questions. Descriptions of the images are currently empty ("No caption").
* **Wiki and knowledge graph:** a graph assistant names, for a document, the related documents with sources, for example which reports refer to a consignment note. We tested this on a separate demo knowledge base, not yet on the industry templates. Treat it as built, but not yet tested end to end.

## Weekly overview (Automations)

**Automations** contains one assistant per industry template that compiles what is about to expire according to your documents, with the place of origin and a note where a date is missing. In our tests the overview ran successfully on manual start in all eight industries.

Limitations: it is switched off by default. The result appears in the assistant's history; there is no e-mail delivery. We did not separately test starting it from the **Automations** screen. We checked the result for success and form, not every line for correctness.

## Roles

* **Administrator:** switches the module and industry templates on and off.
* **Contributor (default role for members):** uploads, edits and deletes their own knowledge bases and creates new ones.
* **Viewer:** reads and asks. Uploading, editing, deleting, creating and downloading are blocked for Viewers and not offered on screen.

See also: [Troubleshooting](troubleshooting.md) and [What it can and cannot do](what-it-can-and-cannot-do.md).
