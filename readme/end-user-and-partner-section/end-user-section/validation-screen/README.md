# Validation Screen

{% embed url="https://youtu.be/CmmQIxOaF6E?si=gYE-U-Jv4dLPi2xT" %}

## Overview

<div data-full-width="false"><figure><img src="../../../.gitbook/assets/validation_screen_overview.png" alt="Validation Screen Overview"><figcaption></figcaption></figure></div>

### Document Origin

{% embed url="https://youtu.be/-m45XGiIeig" %}
DocBits Origin Setting Explained: Country Standards for Dates & Number Formats
{% endembed %}

## **Save Button:**

<figure><img src="../../../.gitbook/assets/validation_screen_save_button.png" alt="Save Button"><figcaption></figcaption></figure>

* **Save Button:**
  * **Purpose:** Saves the current state of the document or script being worked on.
  * **Use Case:** After making changes or annotations to a document, use this button to ensure all modifications are saved.

### **Add special Rules:**

<figure><img src="../../../.gitbook/assets/validation_screen_add_special_rules.png" alt="Add Special Rules Button"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/validation_screen_add_script_example.png" alt="Add Script Example"><figcaption></figcaption></figure>

* **Add Special Rules / Add Script in DocBits:**
  * **Purpose:** Allows users to implement specific rules or scripts that customize how documents are processed.
  * **Use Case:** Use this feature to automate tasks like data extraction or format validation, enhancing workflow efficiency.

{% hint style="info" %}
See here add[ Script in DocBits](../../../administration-and-setup/settings/global-settings/document-types/script/scripting-in-docbits/)
{% endhint %}

### **Fuzzy Fields:**

<figure><img src="../../../.gitbook/assets/validation_screen_fuzzy_fields.png" alt="Fuzzy Fields"><figcaption></figcaption></figure>

* **Fuzzy Fields:**
  * **Purpose:** Helps in identifying and correcting fields where the data may not be a perfect match but is close enough.
  * **Use Case:** Useful in data validation processes where exact matches are not always possible, such as slightly misspelled names or addresses.

### **Required fields:**

<figure><img src="../../../.gitbook/assets/validation_screen_required_fields.png" alt="Required Fields"><figcaption></figcaption></figure>

There are fields that are required for further editing, these can be edited in the settings.

Use the tool tip to find out if:

* Is it a mandatory field (required)
* Validation required
* Low confidence
* Full tax amount missmatch

**Required Fields:**

* **Purpose:** Identifies mandatory fields within documents that must be filled out or corrected before further processing.
* **Use Case:** Ensures that essential data is captured accurately, maintaining data integrity and compliance with business rules.

<figure><img src="https://lh7-us.googleusercontent.com/3-ZXi-fUcWlM0nUaOAQbY7bynchbIN30JReKRdijyMFvX_GIHrnbcismANdOi6UfYa6GCPvk9wnOixya0E_rBk3V8hQduS-gBZJi4k0Kq8jeN93DxC2w5J-YRqeV9IkVB6oiH8tm0-y7gWJO_8fBplo" alt=""><figcaption></figcaption></figure>

## Extracted table (line items)

<figure><img src="../../../.gitbook/assets/validation_screen_line_items_table.png" alt="Line-item table on the validation screen with the table toolbar"><figcaption><p>The extracted table below the header fields</p></figcaption></figure>

Below the header fields DocBits shows the line-item table of the document, one row per invoice line, one column per [table column](../../../administration-and-setup/settings/global-settings/document-types/table-columns/README.md) configured for the document type. When a document type has several tables (for example items and charges), each table has its own tab above the grid.

### Where the table comes from

Above the grid there is one tab per extraction path the organization has switched on:

| Tab | Meaning |
|---|---|
| **Extracted table** | Rule-based extraction (*Table Extraction* setting). For a supplier with a trained table these rows come from the saved rules and are extracted the same way on every document of that supplier; for an untrained supplier the tab may be empty. |
| **AI Extracted table** | The AI table extraction (*AI Table Extraction* setting). Filled when the supplier has no saved rules, and for columns marked *Use AI* even when rules exist. A tooltip *AI table not found* on the tab means the AI returned nothing for this document. |
| **PO Tables** | Only in the layout builder: the purchase-order lines used for matching. |

If neither tab appears, both table settings are off for the organization (Settings → Document Processing → Classification and Extraction). Which AI tier reads the table is set per organization and can be overridden per supplier, see [Supplier-Specific AI Model](supplier-specific-ai-model-for-field-and-table-extraction.md).

### Working in the table

* **Edit a cell**: click into it and type. Amount, number and date columns are validated while you type.
* **Add new table row**: appends an empty row at the end. Use it when a line was not recognised.
* **Delete a row**: the trash icon at the end of the row.
* **Add empty mapped columns**: shows the configured columns the AI left empty, so you can fill them by hand.
* **Restore Table Column**: brings back a column you removed from the view for this document.
* **Delete table**: clears all rows of this table on this document. The configuration is not touched.
* **Add new table column** (admins): the same dialog as in the table-column settings, without leaving the document.
* **Tags** (AI table only): short text hints for the AI, for example *"the last column is the net amount"*. See [AI Table Tags](../ai-table/ai-table-tags.md).
* **Apply** / **Save** / **Delete** next to the tags: *Apply* re-runs the AI table for this document with the tags and column changes you made, without storing anything (if the document has PO-matched lines, DocBits warns that the matches are removed); *Save Rules* stores the current column mapping and tags for this supplier; *Delete Rules* removes them and re-runs the AI extraction for this document.
* **Export**: downloads the table as a CSV file.
* **Go to table extraction view**: opens table training for this document. Use it when the same supplier keeps coming out wrong: draw the table once, map the columns and click *Save Rules*; from then on the rows appear in the *Extracted table* tab. See [Training Line Fields / Table Training](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md).

{% hint style="info" %}
If the table was extracted by the AI and you open table training, DocBits asks *Table is already extracted by AI. Do you want to train manually?* After you save rules, the AI table is no longer used for this supplier.
{% endhint %}

### Re-extracting the table

* **Same document, AI table:** add or change tags and click **Apply**; the AI table is rebuilt for this document only. To also drop the supplier's saved tags and formatting, click **Delete** (*Delete Rules*): DocBits confirms *Rules has been deleted successfully* and runs the AI extraction again.
* **Same document, trained rules:** open *Go to table extraction view*, correct the table and click *Save & re-extract*.
* **Whole document again (header and table):** Dashboard → document menu → *Restart*. Needed after an admin changed the table columns or the extraction settings.

### What blocks approval

The table is checked when you save or approve. A red cell or a message under the table means one of:

| Message | Cause | What to do |
|---|---|---|
| Required column empty | A column marked *Is Required* has no value in this row. | Fill the cell, or ask an admin whether the column must be required. |
| *Line total does not match quantity x unit price (expected …, got …)* | `quantity × unit price + charges − discount` differs from the line total by more than 0.02. Often one of the four values was read into the wrong column. | Correct the value that is wrong on the document; if a column such as *Charges* is consistently filled with the wrong value, tell your admin (see [Troubleshooting](../../../administration-and-setup/settings/global-settings/document-types/table-columns/troubleshooting-1.md)). |
| *Line items add up to … but the net total is …* | The sum of the line totals differs from the net amount in the header. | Check for a missing or duplicated row, or a header amount read wrongly. |
| *Line Item Table is missing Mandatory column for PO* | PO matching needs item number, unit price, quantity and total amount; one of them is hidden. | Admin: unhide the column under Table Columns. |

An admin can switch all table checks off for a document type with *Skip table validation* (Document Types → More Settings); line mismatches and empty required columns are then not reported.

More on the checks: [Automatic Checks on the Validation Screen](automatic-checks-on-the-validation-screen.md) and [Table Extraction Troubleshoot](../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md).

### **Magnify Glass:**

<figure><img src="../../../.gitbook/assets/validation_screen_magnifying_glass.png" alt="Magnifying Glass Icon" width="118"><figcaption></figcaption></figure>

* **Magnifying Glass (Magnify Glass):**
  * **Purpose:** Provides a zoomed-in view of a selected area of the document.
  * **Use Case:** Helps in examining fine details or small text in documents, ensuring accuracy in data entry or review.

<figure><img src="../../../.gitbook/assets/validation_screen_zoomed_view.png" alt="Zoomed Document View"><figcaption></figcaption></figure>

### **Open new window:**

<figure><img src="../../../.gitbook/assets/validation_screen_open_new_window.png" alt="Open New Window Icon" width="130"><figcaption></figcaption></figure>

* **Open New Window:**
  * **Purpose:** Opens a new window for side-by-side document comparison or multitasking.
  * **Use Case:** Useful when comparing two documents or when referencing additional information without leaving the current document.

### **Keyboard shortcuts:**

<figure><img src="../../../.gitbook/assets/validation_screen_keyboard_shortcuts.png" alt="Keyboard Shortcuts Icon" width="145"><figcaption></figcaption></figure>

1. **Keyboard Shortcuts:**
   * **Purpose:** Allows users to perform actions quickly using keyboard combinations.
   * **Use Case:** Enhances speed and efficiency in document navigation and processing by minimizing reliance on mouse navigation.

### **Tasks:**

<figure><img src="../../../.gitbook/assets/validation_screen_tasks_button.png" alt="Tasks Button" width="55"><figcaption></figcaption></figure>

To share internal information, you can create tasks and assign them to a specific employee or group within the company.

* **Tasks:**
  * **Purpose:** Enables users to create tasks related to documents and assign them to team members.
  * **Use Case:** Facilitates collaboration and task management within teams, ensuring everyone knows their responsibilities.

<figure><img src="../../../.gitbook/assets/validation_screen_task_creation.png" alt="Task Creation Dialog" width="218"><figcaption></figcaption></figure>

### Approval History

<figure><img src="../../../.gitbook/assets/approval_history_button.png" alt="Approval History Button"><figcaption></figcaption></figure>

**Note:** The approval history must be activated before it can be displayed here.

**Approval History:**

* **Purpose**: Displays document approval history in field validation, with red indicating rejected and the app's color indicating approved.
* **Use Case**: Useful for organizations that require a transparent record of approval actions during field validation.

<figure><img src="../../../.gitbook/assets/approval_history_list_view.png" alt="Approval History List View"><figcaption></figcaption></figure>

### **Annotation mode:**

<figure><img src="../../../.gitbook/assets/validation_screen_annotation_mode.png" alt="Annotation Mode Button" width="187"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/annotation_mode_example.png" alt="Annotation Mode Example"><figcaption></figcaption></figure>

{% embed url="https://youtu.be/ay0gGtwlqRE" %}
DocBits Annotation Mode Tutorial: Add Notes in Validation & Download With/Without Annotations
{% endembed %}

You can leave annotations on a document. This can be helpful to leave information for other users who further edit this document.

* **Annotation Mode:**
  * **Purpose:** Lets users leave notes or annotations directly on the document.
  * **Use Case:** Useful for providing feedback, instructions, or important notes to other team members who will work on the document later.

### **Merge:**

<figure><img src="../../../.gitbook/assets/validation_screen_merge_documents.png" alt="Merge Documents Button" width="60"><figcaption></figcaption></figure>

Documents can be merged here, for example if a page of an invoice was missing, these pages can be merged later in this way without the entire document having to be deleted or re-uploaded.

* **Merge Documents:**
  * **Purpose:** Combines multiple documents into a single file.
  * **Use Case:** Handy in scenarios where parts of a document are scanned separately and need to be consolidated.

### **OCR view:**

<figure><img src="../../../.gitbook/assets/validation_screen_ocr_view_button.png" alt="OCR View Button" width="77"><figcaption></figcaption></figure>

In the OCR view, the text is automatically filtered from the document. This is used to recognize relevant features, such as the postal code, contract number, invoice number and the sorting of a document.

* **OCR View:**
  * **Purpose:** Automatically recognizes text within documents using Optical Character Recognition technology.
  * **Use Case:** Streamlines the process of digitizing printed or handwritten texts, making them searchable and editable.

<figure><img src="../../../.gitbook/assets/validation_screen_ocr_view_example.png" alt="OCR View Example"><figcaption><p>OCR</p></figcaption></figure>

### **Create ticket:**

<figure><img src="../../../.gitbook/assets/validation_screen_create_ticket_button.png" alt="Create Ticket Button" width="97"><figcaption></figcaption></figure>

Unlike tasks that are passed on internally within the company, this support ticket is important to notify us and to immediately create a ticket in the event of errors and/or discrepancies. This makes the process much easier because you can immediately send the bug with the appropriate document. There is also the option to set priority, take a screenshot of the document or upload one.

* **Create Ticket:**
  * **Purpose:** Allows users to report issues or discrepancies by creating a support ticket.
  * **Use Case:** Essential for quick resolution of problems and bugs, helping maintain the integrity and smooth functioning of the system.

<figure><img src="../../../.gitbook/assets/validation_screen_create_ticket_form.png" alt="Create Ticket Form" width="237"><figcaption></figcaption></figure>

### **Document skript Logs:**

<figure><img src="../../../.gitbook/assets/validation_screen_script_logs_button.png" alt="Document Script Logs Button" width="160"><figcaption></figcaption></figure>

Scripts can be created in the settings under Document Types; this information will then be displayed here.

* **Document Script Logs:**
  * **Purpose:** Displays logs related to scripts that have been implemented for different document types.
  * **Use Case:** Useful for tracking and debugging script actions on documents, helping users understand the automated processes and correct any issues.

<figure><img src="../../../.gitbook/assets/document_script_logs_view.png" alt="Document Script Logs View"><figcaption></figcaption></figure>

### **More settings:**

<figure><img src="../../../.gitbook/assets/more_settings_menu_icon.png" alt="More Settings Menu Icon"><figcaption></figcaption></figure>

### **Document Flow:**

There you will find the flow of the document

* **Purpose:** Shows the sequence and progression of document processing within the system.
* **Use Case:** Helps in tracking document status through different stages, ensuring that all necessary processing steps are followed.

### **Go to layout Template:**

* With this option you will be redirected and can edit your layout or use the default template
* **Go to Layout Template:**
  * **Purpose:** Redirects users to a layout editor where they can modify existing templates or apply a default one.
  * **Use Case:** Enables customization of document layouts to meet specific business needs or preferences, enhancing the document’s visual and functional alignment with company standards.

### Use E-Text if Available

* **Purpose:** Enables DocBits to use e-text for all documents from a specific supplier if available, improving extraction accuracy.
* **Use Case:** Enhances text extraction by leveraging embedded text instead of OCR, which can lead to more precise results for this supplier.

### [Supplier-Based AI Model](supplier-specific-ai-model-for-field-and-table-extraction.md)

* **Purpose:** Allows selection between three different AI models to optimize extraction results for a specific supplier.
* **Use Case:** Ensures better extraction accuracy by choosing the most suitable AI model for each supplier’s document structure and content.
