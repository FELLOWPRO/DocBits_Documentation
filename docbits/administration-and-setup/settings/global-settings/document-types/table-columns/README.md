# Table Columns

Table columns define which columns the line-item table of a document type has: what DocBits extracts into each column, what the user sees on the validation screen, and what is sent to the ERP on export.

**Where:** Settings → Global Settings → Document Types → Table Columns

<figure><img src="../../../../../.gitbook/assets/table-columns_list.png" alt="Table Columns list with the Required, Read Only, Hidden and Use AI flags per column"><figcaption><p>Table Columns: one row per column, flags are switched directly in the list</p></figcaption></figure>

## What you see

Each row is one column of one table. The list shows:

| Column | Meaning |
|---|---|
| **Column name** | Technical name, generated from the title (upper case, underscores). Used in scripts, export mappings and the API. Cannot be changed later. |
| **Title** | Label shown on the validation screen. Change it with the translate icon in the *Actions* column (*Update translation key*). |
| **Column Type** | `AMOUNT`, `STRING`, `DATE`, `NUMBER`, `BOOLEAN` or `CURRENCY`. Determines validation and formatting. |
| **Table name** | The table the column belongs to, for example `INVOICE_TABLE`. |
| **Is Required** | The document cannot be approved while this column is empty in any row. |
| **Read Only** | Users see the value but cannot edit it. |
| **Hidden** | The column is neither shown nor exported. Used to switch off default columns you do not need. |
| **Use AI** | The AI table extraction fills this column, even when a supplier has trained rules. |
| **Actions** | Translate icon: rename the title. Info icon: where the shown label comes from (your translation, the default, the key). Three-dot menu: *Delete*, only for columns your organization created; default columns can only be hidden. |

Two buttons above the list:

* **Create new table**: a second line-item table for the document type (for example a charges table next to the item table).
* **Add new table column**: opens the dialog described in [Adding a new column](adding-a-new-column.md).

## Default columns and your own columns

Every document type ships with a set of default columns (for invoices: item number, description, quantity, unit price, total amount, tax, …). They belong to DocBits, not to your organization, so they cannot be deleted, hide them instead. Columns you add yourself belong to your organization and can be deleted.

{% hint style="info" %}
**Changes apply to new documents only.** A column you add, hide or delete appears on documents that are uploaded or restarted after the change. Documents already on the dashboard keep their table as it was extracted. Restart a document to pick up the new configuration.
{% endhint %}

## Related pages

* [Purpose and use](purpose-and-use.md): where table columns show up
* [Adding a new column](adding-a-new-column.md)
* [Editing and deleting columns](editing-and-deleting-columns.md)
* [Best practices](best-practices-2.md)
* [Troubleshooting](troubleshooting-1.md)
* [Training Line Fields / Table Training](../../../../setup/document-training/training-line-fields-table-training/README.md): teach DocBits where a supplier's table is
* [AI Table](../../../../../end-user-and-partner-section/end-user-section/ai-table/README.md): what the user sees on the validation screen
