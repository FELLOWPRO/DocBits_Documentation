# Troubleshooting

## The new column does not appear on the validation screen

* The document was processed before the column was added. Changes apply to documents uploaded or restarted afterwards, **restart the document** (Dashboard → document menu → Restart).
* The column is **Hidden**. Check the flag in the Table Columns list.
* The column was added to a **different table** than the one shown. The validation screen shows the tables of the document type; compare the *Table name* column.
* The document is not of the document type you configured.

## The column is there but always empty

* The supplier has **trained rules** and the new column is not mapped in them. Open one of the supplier's documents in table training and map the column, or set *Use AI* on the column.
* With AI extraction the value is not recognisable on the document (no header, abbreviated, in a different language). Add an [AI table tag](../../../../../end-user-and-partner-section/end-user-section/ai-table/ai-table-tags.md) that names the column, or map it in training.

## "Column name already exists"

A column with the same technical name is already in the table. If it is not in the list, it is a hidden default column: the message says *Please activate it in Table Column settings*. Unset *Hidden* on that column instead of creating a new one.

## Approval is blocked by a required column

The message on the table names the column. Either fill the cell in every row, or (if the value does not exist on this document) untick *Is Required* for the column, restart the document and try again. Consider whether the column should be required at all (see [Best practices](best-practices-2.md)).

## The AI fills a column with the wrong value

Typical case: `CHARGES` receives the line total, and every row then fails the line-total check with *Line total does not match quantity x unit price (expected …, got …)*, because charges are part of the formula `quantity × unit price + charges`.

* Untick *Use AI* on the column if the trained rules capture it correctly.
* If the supplier has no rules, train the table once (Table training) so the column is bound to the right position, or hide the column if the supplier never prints that value.
* As a last resort, *Skip table validation* in the document type's More Settings switches every table check off for the whole document type; the mismatch is then no longer caught, and neither are empty required columns.

## PO matching: "Line Item Table is missing Mandatory column"

PO matching needs the default columns item number, unit price, quantity and total amount. One of them is hidden or was replaced by a custom column. Unhide the default column, or map the value to it in table training.

## A script or export fails after deleting a column

The script or export mapping still references the deleted *Column name*. Remove the reference, or add the column again with the same title; the technical name is derived from the title and matches again.

## Where to look further

* [Table Extraction Troubleshoot](../../../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md): extraction quality, OCR, E-Text
* [Training Line Fields / Table Training](../../../../setup/document-training/training-line-fields-table-training/README.md)
