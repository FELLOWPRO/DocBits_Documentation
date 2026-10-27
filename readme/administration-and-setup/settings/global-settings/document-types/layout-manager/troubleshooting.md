# Troubleshooting

## Troubleshooting common issues&#x20;

### Fields do not match the scanned documents:

* Compare the layout with the sample document: open the layout in the **Layout Builder** and use **Document** above the canvas to show the scanned document next to the fields.
* Check that the field you see on the canvas is the field you mean. Select it and read the grey **Field Name** in the **Properties** panel — two fields can carry similar labels, and the technical name is the one that is captured.
* Check that the field is placed where people expect it. **Structure** shows the layout as a tree in the order it appears on the document; drag groups and fields to reorder them.
* If a field is missing on the screen, open **Fields**, switch the filter to **Unused** and drag the field into the group where it belongs.

### A field cannot be entered or is not visible on the document:

* Select the field and check its **Properties**: **Readonly** keeps the field visible but not editable, **Hidden** keeps it out of the layout. Both are set per layout, so the same field can behave differently on the validation, approval, reject and review screens.
* **Element width** decides how much of the row a field takes — 25, 33, 50, 66, 75 or 100 percent of the width.

### Data is not extracted correctly:

* The Layout Builder only decides which fields are shown and in which order. Extraction, OCR and matching are configured on the field itself: go to **Settings → Document Types**, find the document type and select **Fields**.
* Check the capture quality on the sample document in the **Document** preview before changing the layout — a field that is captured wrongly there is a field settings or model problem, not a layout problem.

### Faulty data validation:

* Validation rules are not part of the layout. Check them in the document type's **Validation Rules** settings and in the **Fields** settings of the affected field.
* In the layout, **Readonly**, **Hidden** and a **Label** only change what the user sees; they cannot make a value valid or invalid.

### A layout change does not reach the documents:

* Select **Save** in the header of the Layout Builder. Unsaved changes are lost when you leave the screen.
* Each screen has its own layouts and its own rules: the **Field Validation**, **Approval**, **Reject** and **Review** tabs hold separate layouts, so a rule on the approval screen never changes the validation screen.
* Check that the document really gets this layout. Open **Selection rules** for the screen and look at the rule that matches the document's origin — rules are evaluated by priority and the first match wins. The **FALLBACK** row is the layout used when no rule matches.
* The **System default** layout can be viewed but not changed. Select **Clone** on its card, edit the copy and point a selection rule at it.

### Document layouts are confusing or inefficient:

* Group related fields instead of listing everything in one block, and put the fields people need first inside each group.
* Keep fields that belong together side by side with **Element width**, and use **Tab Index** to set the order in which the keyboard moves through the fields.
* Use the **Table** view of the canvas for line items — a long line-item table is easier to read when the important columns come first.

By applying these best practices and troubleshooting as appropriate, you can create efficient and accurate document layouts that enable smooth data capture and processing.
