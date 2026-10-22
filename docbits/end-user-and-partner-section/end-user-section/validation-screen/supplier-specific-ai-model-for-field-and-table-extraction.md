# Selecting a Supplier-Specific AI Model for Field and Table Extraction

In the tools section of the **Validation screen**, you can choose the AI model used for **Field Extraction** and **Table Extraction**.\
This entry point changes the override for the current extraction-template context. The preference is stored by organization and template (`tfidf_id`); the supplier association does not guarantee that every template or historical document for that supplier changes. With no override, the applicable organization setting is used.

To change the model, open the options menu by clicking the **More options** (three dots) button on the right side of the screen, then choose one of the available models:<br>

The menu currently provides **Full**, **Fast**, **Nexus**, **Nexus Flash**, **Auto** and **Auto Nexus**. Check the current UI information and subscription terms for availability and charges. Do not assume that one option is always the most accurate or fastest, or that every organization defaults to Fast.

Selecting a different model can require confirmation and restart extraction. Check the document and scope before confirming. Opening the menu alone does not change the setting; no model was selected or confirmed for these illustrations.

<figure><img src="../../../.gitbook/assets/selecting_a_supplier_specific_ai_model_1.png" alt="Options menu of the validation screen with the AI Model dropdown"><figcaption><p>Options menu for the illustrated extraction-template context, using a synthetic example invoice.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/selecting_a_supplier_specific_ai_model_2.png" alt="AI Model dropdown open with Full, Fast, Nexus, Nexus Flash, Auto and Auto Nexus"><figcaption><p>The AI Model dropdown with six options and a synthetic example invoice; no model change is shown.</p></figcaption></figure>

If extraction results are unsatisfactory, compare other available models using approved test documents and check the extracted values, processing time and charges. A switch may reprocess a document and does not guarantee improvement.

To configure the **organization default** or review **template-specific overrides**, please refer to the corresponding documentation [**here**](../../../administration-and-setup/settings/document-processing/classification-and-extraction/ai-model.md).
