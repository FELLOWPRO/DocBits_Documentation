# Selecting a Supplier-Specific AI Model for Field and Table Extraction

In the tools section of the **Validation screen**, you can choose the AI model used for **Field Extraction** and **Table Extraction**.\
The selected **AI model** is applied to all documents for the current supplier only.

To change the model, open the options menu by clicking the **More options** (three dots) button on the right side of the screen, then choose one of the available models:<br>

* **Full** – Highest accuracy; costs 2 tokens per document
* **Fast** – Default tier; costs 1 token per document
* **Nexus** – Costs 1 token per document
* **Nexus Flash** – Faster tier of the Nexus family; costs 1 token per document
* **Auto** – DocBits decides per document whether Fast suffices or Full is needed; costs 1 token per document
* **Auto Nexus** – Like Auto, but restricted to the Nexus model family; costs 1 token per document

<figure><img src="../../../.gitbook/assets/selecting_a_supplier_specific_ai_model_1.png" alt="Options menu of the validation screen with the AI Model dropdown"><figcaption><p>Open the options menu and pick the AI model for this supplier.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/selecting_a_supplier_specific_ai_model_2.png" alt="AI Model dropdown open with Full, Fast, Nexus, Nexus Flash, Auto and Auto Nexus"><figcaption><p>The AI Model dropdown with the six available options.</p></figcaption></figure>

If the **field extraction** or **table extraction** results are not satisfactory, try switching to another model to improve accuracy.

To configure the AI model **globally for suppliers without a custom model** or to **manage which model is active for each supplier**, please refer to the corresponding documentation [**here**](../../../administration-and-setup/settings/document-processing/classification-and-extraction/ai-model.md).
