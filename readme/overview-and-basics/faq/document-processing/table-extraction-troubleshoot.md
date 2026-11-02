# Table Extraction Troubleshoot

## **Step 1: Open OCR View for Bad Extraction Results**

If the table extraction training results are not good:

1. Open the **OCR View** by clicking on the magnifying glass icon with **OCR** written on it.
2. Review the extraction results and see if the OCR process can improve the data capture.
3. If the results still look bad, try a different document to verify if the issue is document-specific.
4. If the issue is document-specific, use another document for extraction.
   * If the issue persists, follow the next steps.

## **Step 2: Check for E-Text Availability**

1. Check if the document has **e-text** available.
   * You can verify this using a tool like **Adobe Acrobat**.
   * If the document contains e-text, follow **Step 3.**
   * If the document does not contain e-text, follow **Step 4.**

## **Step 3: Turn On E-Text Extraction**

If the document contains e-text, you have two options:

1. **Turn on e-text extraction for just this supplier**:
   * Go back to the **Documents Field Validation**.
   * Click the square with the three dots in the left-side toolbar.
   * Here, activate the **Use E-text if available** option to turn it on for just this supplier.
2. **Turn on e-text extraction for all suppliers**:
   * Go to **Settings** > **Document Processing** > **OCR Settings**.
   * In this section, you will find the **Use E-text if available** option and can turn it on for all suppliers.
3. After enabling e-text extraction, retry the **table extraction training**.
   * If the results improve, the issue is resolved.
   * If the results are still not good, proceed to **Step 4**.

## **Step 4: No E-Text Available - Change AI OCR Version**

If the document does not have e-text available:

1. Go to **Settings** > **Document Processing** > **OCR Settings**.
2. Change the **AI OCR Version** to a different version.
3. Go back to the **Table Extraction Training** and try again.
4. If the result is better:
   * Check other documents from different suppliers to ensure the extraction results for those suppliers are not impacted by this change.
   * **Be cautious, as this change can affect other suppliers' extraction results.**
   * This change can impact other suppliers, so make sure to verify the results thoroughly to ensure it does not negatively affect other suppliers’ document extractions.
5. If the result did not improve after changing the AI OCR version, please **contact us** for further assistance.

## Messages on the table

The extraction can look right and the document still refuses to be approved. These are the messages DocBits shows on or under the line-item table, what triggers them and how to clear them.

| Message | Cause | Fix |
|---|---|---|
| **Required column empty** (cell marked red, column name in the tooltip) | A column marked *Is Required* in the table-column settings has no value in this row. | Fill the cell. If the value never exists for this document type, an admin unticks *Is Required* under Settings → Document Types → Table Columns and you restart the document. |
| **Line total does not match quantity x unit price (expected …, got …)** | DocBits checks every row: `TOTAL_AMOUNT = QUANTITY × UNIT_PRICE + CHARGES`, minus `DISCOUNT`, or × (100 − `DISCOUNT_PERCENT`) / 100, or minus `DISCOUNT_PER_UNIT × QUANTITY`, whichever discount column is filled. A difference above 0.02 raises the message. The check only runs when quantity, unit price and total are all filled. | Compare the four values with the document. Usually one of them was read into the wrong column, a charges or discount value in the wrong cell is the most common case. Correct the cell; the message disappears on save. |
| **Line total does not match quantity x unit price minus discount / minus percentage discount / minus per-unit discount** | Same check, with the discount column that is filled. | As above; check the discount cell first. |
| **Line items add up to … but the net total is …** (warning) | The sum of all `TOTAL_AMOUNT` cells differs from the net amount in the header. | Look for a missing row, a duplicated row, or a header net amount that was read wrongly. A warning does not block approval. |
| **Total does not add up: expected …, got …** (header) | Net + tax (+ shipping in US layouts) differs from the header total. | Header check, not a table problem: correct the header amounts. |
| **Line Item Table is missing Mandatory column for PO like (Item Number, Unit Price, Quantity and Total amount)** | PO matching needs those four default columns and one of them is hidden or replaced by a custom column. | Admin: unhide the default column under Table Columns, or map the value to it in table training. |
| **Table is already extracted by AI. Do you want to train manually?** | You opened table training for a supplier whose table comes from the AI. | Confirm to train; the saved rules then replace the AI table for this supplier. Cancel to keep the AI table. |
| **AI Table will display here. Enable in …** | AI table extraction is switched off for the organization. | Admin: Settings → Document Processing → Classification and Extraction → *AI Table extraction*. |
| **No line items yet** | Nothing was extracted: no rules for this supplier and the AI found no table, or the document has no readable text. | Follow Steps 1–4 above (OCR view, E-Text). Then train the table once, or add rows manually with *Add new table row*. |

### The AI keeps filling a column with the wrong value

Example seen in practice: the AI writes the line total into `CHARGES`. Every row then fails the line-total check, because charges are added to quantity × unit price.

1. If the supplier has saved rules, untick *Use AI* on that column (Settings → Document Types → Table Columns) so the rules fill it.
2. If the supplier has no rules, train the table once so the column is bound to its position on the page, or hide the column if the supplier never prints that value.
3. Add an [AI table tag](../../../end-user-and-partner-section/end-user-section/ai-table/ai-table-tags.md) such as *"charges column is empty on this supplier"*, tags are saved per supplier.

### Switching the table checks off

Settings → Document Types → *your type* → More Settings → **Skip table validation** marks the table of every document of that type as valid: line-total mismatches and empty required columns are no longer reported. The header checks (total = net + tax) stay. Use it only for document types whose tables are informational and not exported to the ERP.
