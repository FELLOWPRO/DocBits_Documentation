# Editing and deleting columns

Everything except the title is changed directly in the list; there is no edit dialog.

**Where:** Settings → Global Settings → Document Types → Table Columns

## Switching a flag

Tick or untick the checkbox in the row. The change is saved immediately (*Successfully saved*).

| Flag | On | Off |
|---|---|---|
| **Is Required** | Approval is blocked while the column is empty in any row; the validation screen marks the cell. | Empty cells are allowed. |
| **Read Only** | The value is shown but cannot be typed over. Use it for values that come from a lookup or a script. | Users can edit the cell. |
| **Hidden** | The column disappears from the validation screen and from the export. Its data is kept. | The column is shown and exported. |
| **Use AI** | The AI table extraction fills this column, also for suppliers that have trained rules. | The column is filled by the trained rules, or by the AI when no rules exist. |

{% hint style="info" %}
Flags take effect on documents uploaded or restarted **after** the change. Open documents keep their current table until they are restarted.
{% endhint %}

## Renaming the title

Click the translate icon in the *Actions* column (*Update translation key*), enter the new label and confirm. The info icon next to it shows which label is currently in effect and where it comes from. Only the label changes; the technical *Column name* stays the same, so scripts, export mappings and trained rules keep working.

## Changing the type or the table

Not possible. Hide the column (or delete it if it is your own) and add a new one with the right type.

## Deleting a column

The delete action is only offered for columns your organization created. Default columns cannot be deleted, hide them.

1. Open the three-dot menu in the *Actions* column and choose **Delete**. The entry is missing for default columns.
2. Confirm.

What happens:

* The column is removed from the configuration. Documents processed **from now on** no longer have it.
* Documents already extracted keep the column and its values until they are restarted.
* Trained rules that mapped this column keep working for the other columns; the mapping for the deleted column is ignored.
* If the column is referenced in an export mapping or a script, remove that reference; otherwise the export or the script fails with a missing-column error.

## Undoing a deletion

A deleted column cannot be restored from the list. Add it again with the same title: the technical name is derived from the title, so a column created with the same title gets the same *Column name* and existing mappings match again.
