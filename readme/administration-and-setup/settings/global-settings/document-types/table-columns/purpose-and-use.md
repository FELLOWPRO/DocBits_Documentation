# Purpose and use

A table column is one field of the line-item table. Everything that DocBits does with a table (extraction, validation, PO matching, export) works on the columns configured here.

## Where a column shows up

| Place | What the column does there |
|---|---|
| **Validation screen** | One column in the line-item table. The *Title* is the header, the *Column Type* decides the editor (amount, date, text, yes/no). Hidden columns are not shown. |
| **Table training** | When you train a supplier's table, you map each detected table column to one of these configured columns. Only configured columns can be mapped. |
| **AI table extraction** | The AI fills the configured columns. A column marked *Use AI* is filled by the AI even for suppliers with trained rules. |
| **Validation rules** | Line-item checks such as *quantity × unit price = line total* run on the default columns `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `CHARGES`, `DISCOUNT`. |
| **PO matching** | Needs the default columns item number, unit price, quantity and total amount. Without them the document shows *Line Item Table is missing Mandatory column for PO*. |
| **Export** | Every non-hidden column is part of the line-item data sent to the ERP. The export mapping references the *Column name*. |
| **Scripts** | Scripts read and write columns by *Column name*, for example `row["TOTAL_AMOUNT"]`. |

## Scope

* Table columns are configured **per table**, and a table belongs to a **document type**. Invoice columns do not affect delivery notes.
* The configuration is **per organization**. Sub-organizations inherit it.
* Which columns are *filled* for a given supplier is decided by that supplier's training or by the AI; the column configuration only says which columns exist.

## Typical reasons to change the configuration

* A customer-specific value must be captured per line (cost centre, project number, internal article number) → add a column.
* A default column is never used and clutters the validation screen → hide it.
* A column must always be filled before export → mark it *Required*.
* A value comes from the ERP lookup and must not be edited by users → mark it *Read Only*.
* The AI captures a column better than the trained rules (for example free-text descriptions) → mark it *Use AI*.

## Related pages

* [Adding a new column](adding-a-new-column.md)
* [Editing and deleting columns](editing-and-deleting-columns.md)
* [Table Extraction Troubleshoot](../../../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md)
