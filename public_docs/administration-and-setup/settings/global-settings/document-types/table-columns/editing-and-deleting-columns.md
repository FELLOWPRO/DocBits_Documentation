# Editing and deleting columns

The checkbox flags control required values, editability and visibility. Use AI is configured separately in its three-state dropdown below.

Everything except the title is changed directly in the list; there is no edit dialog.

**Where:** Settings → Global Settings → Document Types → Table Columns

## Switching a flag

Tick or untick the checkbox in the row. The change is saved immediately (*Successfully saved*).

| Flag | On | Off |
|---|---|---|
| **Is Required** | Approval is blocked while the column is empty in any row; the validation screen marks the cell. | Empty cells are allowed. |
| **Read Only** | The value is shown but cannot be typed over. Use it for values that come from a lookup or a script. | Users can edit the cell. |
| **Hidden** | The column disappears from the validation screen and from the export. Its data is kept. | The column is shown and exported. |


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

## Use AI: Default, Yes or No

Open [Table Columns](README.md) for the correct document type and table. **Use AI** is a three-state dropdown, not a checkbox. Changes save immediately.

| Choice in the current menu | Meaning for the base schema |
| --- | --- |
| **Default · requested** or **Default · not requested** | Uses the DocBits default for this document type and column name. Default does not always mean on or always mean off. |
| **Yes · requested** | Explicitly requests this configured column from the AI. |
| **No · not requested** | Excludes it from the base schema even if it belongs to the default AI selection. |

Returning to **Default** removes the explicit Yes/No choice. A newly created custom column normally does not belong to the default AI selection; set it to **Yes** if the AI should return it. Default AI columns are not the same as all built-in columns. Check the displayed effect and preview.

**Required**, **Read Only** and **Hidden** control completeness checks, editability and visibility. None replaces the AI choice. **No** neither deletes the column nor clears existing values and does not stop rules, scripts or other sources from filling it. Supplier training and additional AI tags can extend a run's request; resolve conflicting instructions there too. The Structured Output switch does not automatically replace a purely rule-based result.

[Structured Output for Tables](../../../../../end-user-and-partner-section/end-user-section/ai-table/structured-output.md).
