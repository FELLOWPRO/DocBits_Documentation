# Troubleshooting

Most problems are solved with **Rebuild Document** (process the document again) or with a more precise question. The tables list only cases we observed in our tests. For how to reach each function, see [Tasks and where to find them](tasks-and-where-to-find-them.md).

## Documents and processing

| Symptom | Cause (short) | Action |
| --- | --- | --- |
| The document shows **May be stuck**; the timeline says "No progress for N minutes" | Processing has not reported anything for a long time. | Open the document, choose **Stop parsing**, then **Rebuild Document**. If you do nothing, the system sets the document to Failed by itself after a while. |
| The document shows **Failed** with "task stuck in processing…" | A stall was ended automatically. | **Rebuild Document**. If it stays that way, report the document name to support. |
| A scanned PDF has no text after processing, or shows Failed and the message mentions text recognition | Text recognition could not be reached, or the image covers only part of the page and the page is treated as a text page. | **Rebuild Document** a little later. Create scans full-page where possible. If it persists, contact your administrator. |
| A damaged file shows **Failed** | The file cannot be read. For damaged Word files it can take up to about 3 minutes until Failed appears. | Open the file in its original program, save it again and upload it again. |
| The upload is rejected | E-mail files (.eml), XML files, empty files and a file that is already in the knowledge base are not accepted. Import by web address is switched off. | Convert the file to a supported format, for example PDF. For a duplicate, the existing document stays unchanged. |
| The upload stops with **Storage quota exceeded** | Your organization's storage quota is reached. | Delete documents you no longer need; the space is freed. For more space contact your administrator. A document written with **Online Edit** can also end as Failed later when the quota is reached. |
| A photo cannot be uploaded, **Upload and parse** is grey | <!-- CHECK-DEV FIX-FOTO --> For photos, image processing ("Multimodal") must be on and a model chosen. | Switch on image processing and choose a model (administrator). |
| After **Save and Close** in the knowledge base settings the values are wrong | <!-- CHECK-DEV FIX-CHUNK --> Saving the section size does not work reliably at the moment; existing settings may be reset. | Do not change these values for now. Viewing and closing without saving is harmless. |
| An Excel document is searchable but has no short description | The automatic description of table documents sometimes fails. The content is still read. | No action needed, questions work. Enter a description by hand if you want one. |

## Questions and answers

| Symptom | Cause (short) | Action |
| --- | --- | --- |
| The answer is "not in the documents" although you know the document | The document is not yet Completed, was deleted, or the number in your question differs. The assistant does not mix up similar numbers. | Check the status, copy the number exactly from the document and ask again. |
| A validity question ("Is … still valid?") ends with "To be clarified" or "Not unambiguous" instead of Yes or No | The document names an expired valid-until date but itself carries the note "valid". The answer then hedges. | Add: **"Answer with yes or no and state the valid-until date."** With this wording the assistant gave a clear No with the date in the cases we checked. |
| An answer has no clickable source reference | In rare individual cases the value was correct but the reference was missing. | Ask again or add "Name the source." Always check the value in the document. |
| A page number for a long document is off by one | In one test run the answer said page 8; the passage was on page 7. | Always open the preview and confirm the page there. |
| A question about a photo stays unanswered, or the gallery is empty ("No caption") | Photos uploaded on their own are read by text recognition: ask about the **text** in the photo, not about what the image shows. The gallery shows only images embedded in documents, and the descriptions are currently empty. | Ask for values written in the photo, for example numbers, classes or quantities. For the gallery, image processing of the knowledge base must be on. |
| Excel as a source opens, but the row is not highlighted | The preview cannot jump to a row in tables. | The file opens; search there for the stated value. |
| An answer takes longer | In our tests answers took 6 to 9 seconds on average, single ones up to 25 seconds; questions about contradictions took the longest. | Wait, do not submit the question again. |

## Industry template and permissions

| Symptom | Cause (short) | Action |
| --- | --- | --- |
| The **Industry templates** tab is missing in Settings | You are not an administrator. Only administrators see the tab. | Ask your administrator to switch the template on. |
| The template is on, but the assistants are missing in Chat | You are signed in to another organization, or the template was switched off with **Switch off**. Templates apply per organization; assistants disappear when switched off, documents stay. | Check the organization at the top right and check that the card under **Industry templates** shows "On". |
| Upload, edit, delete and download are not offered | Your role is Viewer. | Ask your administrator to change your role to Contributor. |

## Operation

| Symptom | Cause (short) | Action |
| --- | --- | --- |
| A folder cannot be moved; the message appears in Chinese | The target folder lies inside the folder being moved. The message is not yet translated. | Choose a target folder outside the moved folder. Other messages, for example when cancelling processing, are in part not yet translated either. |
| An error appears when saving metadata | At most 20 fields per document are possible. | Remove fields you do not need. |
| "Chunk was modified by another user" appears when you edit a section | A second person changed the same section. | Reload the page and make the change again. |
| A Mermaid diagram in a Markdown document appears as one line of text | Diagrams in Markdown are not drawn. | Also store the information as text or a table. |
| The copy of a knowledge base cannot be told apart from the original | The copy has the same name. | Rename the copy. |

## Precautionary notes

These did not occur in our tests:

* **A document stays on "In queue" for a long time.** With large imports, documents wait in turn. Wait a few minutes; if **May be stuck** appears, proceed as above.
* **Numbers from PDF tables look wrong.** Check the value in the preview (see [What it can and cannot do](what-it-can-and-cannot-do.md#pdf-tables)).
* **The answer is in the wrong language.** In all tests the answer followed the language of the question, even for documents in another language. This is not guaranteed. If needed, state in the question which language you want the answer in.
* **The Knowledge Assistant menu entry is missing.** The module must be switched on for your organization. Contact your administrator.
