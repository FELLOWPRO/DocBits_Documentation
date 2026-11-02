# AI Table

The AI Extracted Table is the line-item table that DocBits reads with AI when a supplier has no trained table rules. It appears on the validation screen below the header fields. This page covers when you get it, how to re-run it, and how to shape what it extracts.

## When you get the AI table

* An admin has switched on **AI Table extraction** (Settings → Document Processing → Classification and Extraction). If it is off, the table area shows *AI Table will display here. Enable in …*.
* The supplier has **no saved rules**. As soon as someone trains the supplier's table and clicks *Save Rules*, the saved rules replace the AI table for that supplier; the rows then appear in the *Extracted table* tab instead of the *AI Extracted table* tab.
* Exception: columns marked **Use AI** in the table-column settings are filled by the AI even for suppliers with saved rules, see [Use AI per column](#use-ai-per-column).

Which AI tier reads the table (Fast, Full, Nexus) is set per organization and can be overridden per supplier under *More settings* on the validation screen, see [Supplier-Specific AI Model](../validation-screen/supplier-specific-ai-model-for-field-and-table-extraction.md).

## Re-extracting the AI table

Use this when rows are missing or a column is shifted and you want the AI to try again, for example after adding a [tag](ai-table-tags.md):

1. Add or change [tags](ai-table-tags.md) in the field below the table and click **Apply**. The AI rebuilds the table for this document with your tags and column changes; nothing is stored for the supplier yet. If the document has PO-matched lines, DocBits warns that the matches are removed by the rebuild.
2. Happy with the result? Click **Save** (*Save Rules*) so the next document of this supplier is extracted the same way.
3. To start over, click **Delete** (*Delete Rules*): DocBits confirms *Rules has been deleted successfully* and runs the AI extraction again without any saved tags or formatting.

*Delete Rules* removes the tags and formatting rules saved for this supplier, not the table-column configuration. To re-extract the whole document (header and table) after an admin changed settings or columns, use *Restart* in the document menu on the dashboard instead.

## Use AI per column

Each table column has a **Use AI** flag (Settings → Global Settings → Document Types → [Table Columns](../../../administration-and-setup/settings/global-settings/document-types/table-columns/README.md)). With the flag on, the AI fills that column even when the supplier has saved rules; the other columns keep coming from the rules. Typical use: a free-text description column that trained rules capture badly, or a value that moves around on the page.

Be aware that the AI then guesses that column from the whole row. If it consistently puts the wrong value there (for example the line total into *Charges*) the line-total check fails on every row. In that case switch *Use AI* off for that column, or add a tag that tells the AI what the column is.

## Structured extraction

With **Use Structured Extraction (AI)** enabled in the organization settings, the AI returns the table in a fixed structure that maps straight onto the configured table columns instead of copying the supplier's column headers. Column names then always match your configuration; a column the supplier prints but you have not configured is not extracted. Ask your admin to switch it on when supplier headers vary a lot and you spend time remapping.

## Working with the extracted table

Here are the key capabilities and usage instructions:

* **Deleting Columns**: If certain columns in the extracted table are not needed, users can easily remove them by clicking the "Delete column" icon (represented by three vertical dots) next to the column header. This helps declutter the table and focus only on relevant information.

<figure><img src="../../../.gitbook/assets/ai-table1.png" alt=""><figcaption></figcaption></figure>

* **Changing Currency Format**: The currency format can be changed by selecting the desired format from the dropdown menu next to the "Currency" field. This ensures that the currency values are displayed in the preferred format, making it easier to interpret and analyze the financial data.

<figure><img src="../../../.gitbook/assets/ai-table2.png" alt=""><figcaption></figcaption></figure>

* **Showing/Hiding Non-Mapped Columns**: By default, only the mapped columns (columns with extracted data) are visible in the table. However, users can choose to show or hide the non-mapped columns by clicking the "Hide non mapped columns" or "Show non mapped columns" button at the bottom of the table. This feature is useful when users want to review all available columns, even if they don't currently contain data.

<figure><img src="../../../.gitbook/assets/ai-table3.png" alt=""><figcaption></figcaption></figure>

* **Changing Table Headers**: The table headers (column names) can be modified by clicking on the header and entering the desired name. This feature allows users to customize the column names to better align with their terminology or preferences, making the data more readable and understandable.

<figure><img src="../../../.gitbook/assets/ai-table4.png" alt=""><figcaption></figcaption></figure>

* **Saving what you changed**: **Save** next to the tags (tooltip *Save Rules*) stores the current column mapping, hidden columns and tags for this supplier. The next document of the supplier is extracted with them.

These features give you control over the extracted data. When the same supplier needs the same corrections every time, train the table once instead, [Training Line Fields / Table Training](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md), and the AI table is no longer used for that supplier.
