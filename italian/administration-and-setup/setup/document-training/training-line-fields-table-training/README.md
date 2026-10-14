# Training Line Fields/Table Training

## Table Training: When and How to Use It

DocBits uses AI-based table extraction by default, which works across suppliers. However, when you need more control over how line items are extracted for a specific supplier, you can use **Table Training** to define the structure manually.

#### &#x20;**Important: Supplier-Specific Training**

Table training is **specific to each supplier**. If you train a table layout for one supplier, the rules apply only to that supplier’s documents.\
Other suppliers will continue to use AI-based table extraction unless trained separately.

#### When Should You Use Table Training?

Use Table Training **only when the document layout is stable**, and you want to ensure consistent, high-quality extraction. It is best suited for suppliers who:

* Use a **fixed invoice format** over time.
* Require **precise mapping** of line items to specific fields.
* Are **high-volume suppliers**, where consistent automation is valuable.

#### When Not to Use Table Training

Avoid using Table Training if:

* The supplier **frequently changes their invoice layout** (e.g., every couple of months).
* You do not regularly receive documents from that supplier.
* The default AI extraction works **well enough** without manual training.

In such cases, retraining the table repeatedly would be inefficient and time-consuming.



## How to use It:

**Training Mode** is used to teach DocBits how to correctly extract line items from a specific supplier’s document layout.

When you're in Training Mode, you define:

* **Where the table is located** on the document.
* **Which areas correspond to each column** (e.g., Quantity, Description, Unit Price).

This mode creates a **reusable extraction template** for that supplier, so future documents with the same layout will be processed automatically — no need to retrain.

**Key Characteristics:**

* **Mapped columns are read-only** — you can’t manually change the text.
* You **cannot add or delete rows**.
* The focus is on **mapping positions**, not correcting values.
* Once you’ve finished mapping the table and its columns, click **“Save Rules”** so DocBits learns and applies this training to similar documents from the same supplier.



**Correction Mode** allows you to **fix extraction errors** in the table data for the current document. It’s used when DocBits has already attempted to extract the table, but the results need small corrections.

Use Correction Mode when:

* Some **values are missing or misaligned**.
* An **empty or duplicate line** was extracted and needs to be removed.

**What You Can Do in Correction Mode:**

* **Manually adjust values** in mapped columns (e.g., fix misplacements).
* **Delete rows** that shouldn’t be part of the table.
* **Add rows** that were missed entirely during extraction.
