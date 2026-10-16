# AI Table Tags and Instructions

Tags are how you tell the AI what to do with a table. In the **AI instructions** card below the AI table (see [AI Table](README.md)) you give two kinds of tags:

| Kind | Where you enter it | What the AI does with it |
| --- | --- | --- |
| **Instruction** | **Prompt for the AI**, one instruction per line | Follows it while reading the table, for example how to calculate or which wording to use. |
| **Column** | **Extra columns for the AI** | Must return that column in addition to the usual ones, even if the document does not label it clearly. |

Both are stored together as the supplier's AI tags when you **Save as training**.

<figure><img src="../../../.gitbook/assets/ai-table-prompt-filled-en.png" alt="A prompt line typed into the AI instructions card"><figcaption><p>One instruction per line in <strong>Prompt for the AI</strong>.</p></figcaption></figure>

## Add tags step by step

1. Open the document on the validation screen and stay on the **AI Extracted table** tab.
2. In **Prompt for the AI** write what the AI should do, one instruction per line. Type **@** to insert a column from your configuration.
3. Or open **Extra columns for the AI** and pick the columns the AI must return.
4. Not sure what to write? Click **Suggest with Nexus** and use **Insert** or **Add column** on a suggestion.
5. Click **Test change** to compare the result with the current table. Nothing is written yet.
6. Happy? Click **Apply** (or **Apply result to this document** in the test dialog) to put the result into this document.
7. If every document of this supplier needs it, click **Save as training**. **Delete** removes the saved tags and rules of the supplier layout.

{% hint style="info" %}
Every line in **Prompt for the AI** is an instruction, even a single word (DocBits adds a full stop so the AI does not mistake it for a column name). Columns belong in **Extra columns for the AI**.
{% endhint %}

## Writing good instructions

* **Name the column and the wording of the document.** *Fill the Discount Amount column from the column called "Rabatt".* works better than *find the discount*.
* **One thing per line.** Short lines are easier to test and to remove.
* **Describe calculations plainly.** *The unit price is the net amount divided by the quantity.*
* **Say what to leave alone.** *Ignore the shipping lines at the bottom of the table.*
* **Check the whole table.** A changed prompt re-runs the AI and can change every column.
* **Do not repeat what is already known.** A column tag that duplicates another tag, or equals a header field, is ignored.

## Examples

| Problem | Tag |
| --- | --- |
| Discount column stays empty | Extra column **Discount Amount** and the instruction *Fill the Discount Amount column from the column called "Rabatt".* |
| Quantity and unit are in one cell | *Put the number into Quantity and the unit of measure into Unit.* |
| Unit price is not printed | *The unit price is the net amount divided by the quantity.* |
| Dates must be ISO | *Write all dates as YYYY-MM-DD.* |
| Amounts in a foreign currency | *Round all amounts to two decimals.* |

The columns you can pick are the table columns configured for the document type, see [Table Columns](../../../administration-and-setup/settings/global-settings/document-types/table-columns/README.md).

## Before you save

* **Test change** first. It never writes anything.
* **Save as training** applies to the supplier's layout, so the next documents are read with your tags. Check on the next document that the chip says **Training applied**.
* If **Save extraction rules (Admin only)** is on, ask an organization admin to save.
* Tags change how the AI reads the table. For stable column positions of a recurring layout, [train the table](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md) instead.
