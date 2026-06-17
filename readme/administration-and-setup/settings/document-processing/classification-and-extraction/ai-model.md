# AI Model

## Overview

The **AI Model** setting allows you to define which AI model is used by default for **field extraction** and **table extraction** during document processing.\
In this section, you can review the token cost for each model and see which model is currently assigned to each supplier.

## How to Access

1.  Navigate to **Settings** → **Document Processing** → **Classification and Extraction**

    <figure><img src="../../../../.gitbook/assets/settings_classification_and_extraction.png" alt=""><figcaption></figcaption></figure>
2.  Scroll down to the **Table Extraction** section

    <figure><img src="../../../../.gitbook/assets/ai_model_1.png" alt=""><figcaption></figcaption></figure>

## AI Model Options

DocBits offers three AI model options for field and table extraction. They differ in the balance between **extraction accuracy**, **processing speed**, and **token cost per document** — so you can match the option to the kind of documents you process. Hover over the info icon next to the setting to see the token cost for the currently selected option.

* **Full** – The most thorough option, with the highest extraction accuracy. Best for complex layouts, low-quality scans, or documents where precision matters most. As the most powerful option it is also the slowest, at **2 tokens per document**.
* **Fast** – A balanced option that combines strong accuracy with quicker processing at a lower cost. This is the recommended default for most everyday documents, at **1 token per document**.
* **Turbo** – The quickest and most economical option. Best suited to high volumes of simple, clean, well-structured documents where speed and low cost matter more than maximum accuracy, at **1 token per document**.

| Option | Best for | Accuracy | Speed | Token cost |
|--------|----------|----------|-------|------------|
| **Full** | Complex layouts, poor scans, high-precision needs | Highest | Slowest | 2 / document |
| **Fast** | Everyday documents (recommended default) | High | Fast | 1 / document |
| **Turbo** | High volumes of simple, clean documents | Good | Fastest | 1 / document |

<figure><img src="../../../../.gitbook/assets/ai_model_2.png" alt=""><figcaption></figcaption></figure>

## AI Model Assignment Table

You can also configure supplier-specific **AI models** directly in the **Validation screen**, allowing you to fine-tune extraction accuracy for individual suppliers.\
\
For more information, please refer to the corresponding documentation [here](../../../../end-user-and-partner-section/end-user-section/validation-screen/supplier-specific-ai-model-for-field-and-table-extraction.md).

The assignment table displays the AI model settings for each supplier and includes the following details:

* **Supplier ID** – The unique identifier of the supplier
* **AI Model** – The AI model currently assigned to the supplier
* **E-Text**: Indicates whether the E-Text feature is enabled
* **Action** – Contains the option to delete the entry

<figure><img src="../../../../.gitbook/assets/ai_model_3.png" alt=""><figcaption></figcaption></figure>

### Delete Entry – Reset Supplier-Specific Settings

To reset a supplier’s AI model setting to the default:

1.  Click the trashcan icon in the **Action** column next to the supplier entry.

    <figure><img src="../../../../.gitbook/assets/ai_model_4.png" alt=""><figcaption></figcaption></figure>
2.  A confirmation dialog will appear—confirm that you want to delete the entry.

    <figure><img src="../../../../.gitbook/assets/ai_model_5.png" alt=""><figcaption></figcaption></figure>

Once deleted, the supplier will revert to using the default **AI model** for **field extraction** and **table extraction**.
