# Explain extraction and troubleshoot

[AI Table](README.md) · [Structured Output for Tables](structured-output.md)

## See what the AI did

Four buttons under the table explain the extraction.

<figure><img src="../../../.gitbook/assets/ai-table-explain-buttons-en.png" alt="Explain extraction, Open as page, Processing pipeline and AI advice buttons"><figcaption><p>The explain buttons.</p></figcaption></figure>

* **Explain extraction** opens _How the AI table arrived at its values_: the document, the AI extraction (tier, number of raw columns and rows), the mapping to your structure and the result per column with the origin of each column.
* **Open as page** shows the same explanation in its own window.
* **Processing pipeline** lists the processing steps of the document and where it stopped.
* **AI advice** asks Nexus how the extraction can get better and lists concrete recommendations, for example _Enable structured output_ or _Add an instruction tag for Net Amount_. It is advice only; you decide.

<figure><img src="../../../.gitbook/assets/ai-table-explain-en.png" alt="Explain extraction dialog with four steps"><figcaption><p>Explain extraction: four steps from document to result.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/ai-table-advice-en.png" alt="AI advice dialog with two recommendations"><figcaption><p>AI advice proposes the next steps.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/ai-table-pipeline-en.png" alt="Processing pipeline dialog"><figcaption><p>The processing pipeline shows where a document stopped, here at field validation.</p></figcaption></figure>

These explanations belong to the **Analytics Dashboard** module. Without the module licence, or when your role has no access to the Analytics tab, DocBits tells you what to ask your admin for (activate the module under Settings → Modules, or grant the tab to your role under Settings → Roles).

## Practical examples

| Situation                                                                     | What to do                                                                                                                                                                                                                                          |
| ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A value is in the wrong column, for example _Unit price_ sits in _Net amount_ | Click the column name and map it to the right column. Then **Save as training** if the supplier always prints it like this.                                                                                                                         |
| A column stays empty in every row, for example _Discount_                     | Add the column under **Extra columns for the AI**, or write an instruction with the wording the invoice uses, such as _Fill the Discount Amount column from the column called "Rabatt" on the invoice._ Check with **Test change**, then **Apply**. |
| The AI does not know what to do (nothing in the prompt)                       | Click **Suggest with Nexus** and insert what fits.                                                                                                                                                                                                  |
| A price must be divided or rounded                                            | Write the rule in the prompt, for example _The unit price is the net amount divided by the quantity_.                                                                                                                                               |
| Amounts are read with the wrong separators (1.234,50 versus 1,234.50)         | Open the column's three-dots menu, choose **Amount Formatting** and pick the right format.                                                                                                                                                          |
| The label sits below the value                                                | Three-dots menu → **Extract From** → **Below**.                                                                                                                                                                                                     |
| A column is not needed for this supplier                                      | Three-dots menu → **Delete column**. **Save as training** keeps it hidden for the supplier.                                                                                                                                                         |
| A row is wrong or missing                                                     | Remove it with the **x**, or add one with **Add new table row** and type the values.                                                                                                                                                                |
| The same corrections are needed again and again                               | Use **Save as training** so the next documents of this supplier come out right. For complex layouts [train the table](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/) instead.                      |

{% hint style="info" %}
Not every wrapped description line can be repaired with an instruction. If lines of one item are split into several rows, edit the rows or use the classic table training.
{% endhint %}
