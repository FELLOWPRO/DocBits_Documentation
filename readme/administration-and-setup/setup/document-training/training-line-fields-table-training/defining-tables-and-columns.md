# Defining Tables and Columns

Use this guide to manually define tables and columns for line-item extraction in DocBits. This is especially useful when automatic detection doesn't fully capture the table structure, or when you need to add custom fields.

### 1. Access the Table Extraction View

Open the document in the Field Validation view and click the table-extraction button in the footer on the right (its tooltip reads **“Go to table extraction view”**) to enter the table extraction view.

<figure><img src="../../../../.gitbook/assets/define_tables_and_columns_1-en-20261014.png" alt="Footer of the Field Validation view with the table extraction button highlighted on the right." width="563"><figcaption><p>The table extraction button in the footer of the Field Validation view.</p></figcaption></figure>

### 2. Activate Training Mode

To manually define or modify tables and columns, switch on the **“Training Mode”** toggle in the header on the right.

<div align="center"><figure><img src="../../../../.gitbook/assets/define_tables_and_columns_2-en-20261014.png" alt="Training Mode toggle in the table extraction header, shown switched on." width="375"><figcaption><p>The Training Mode toggle in the table extraction header.</p></figcaption></figure></div>

### 3. Define the Table Area

After entering Training Mode, you can define where the table is on the document. You have two options:

#### Option 1: Use Auto-Detect

Click the **“Autodetect tables”** button to let DocBits try to identify the table area on its own.

<figure><img src="../../../../.gitbook/assets/define_tables_and_columns_3-en-20261014.png" alt="Toolbar in the image panel with the Autodetect tables button and its tooltip visible." width="375"><figcaption><p>The Autodetect tables button in the image panel toolbar.</p></figcaption></figure>

If detection is successful, the table outline will be displayed automatically. You can then proceed to define the columns.

#### Option 2: Define Table Manually

If auto-detection fails or is inaccurate, you can manually define the table:

1. Click the **“Edit”** button to activate table selection mode.
2. Draw a rectangle around the table area on the left-hand document view.

<figure><img src="../../../../.gitbook/assets/define_tables_and_columns_4-en-20261014.png" alt="Table extraction toolbar in edit mode showing the Edit and Save buttons." width="563"><figcaption><p>The Edit button switches the image panel into table selection mode.</p></figcaption></figure>

While table selection mode is active, the header shows the banner **“Table selection mode: On”**. Click **“Save”** when the rectangle covers the whole table.

### 4. Add and Define Columns

Once the tables are defined you can manually define the columns with the **“Add Column”** button in the image panel toolbar. The header then shows the banner **“Column add mode: On”**.

<figure><img src="../../../../.gitbook/assets/define_tables_and_columns_5-en-20261014.png" alt="Image panel toolbar in column add mode with the Add Column button and its tooltip." width="563"><figcaption><p>The Add Column button starts column add mode.</p></figcaption></figure>

Define and sort the columns via drag and drop on the document. Repeat this for the tables on the other pages as well. As an alternative, if the tables are equal on each page, you can use the **“Use same columnn for all”** button to use the same columns for all tables defined in the document. This functionality copies the columns that you have defined to all other pages as well:

<figure><img src="../../../../.gitbook/assets/define_tables_and_columns_6-en-20261014.png" alt="Image panel toolbar in column mode with the Use same columnn for all button and its tooltip." width="563"><figcaption><p>The button that copies the defined columns to every page of the document.</p></figcaption></figure>

Use the **zoom** feature (**“Zoom in”** and **“Zoom out”**) to better define columns on cluttered or complex documents, for example, when a lot of information is close together and this makes it difficult to define the columns:

<figure><img src="../../../../.gitbook/assets/define_tables_and_columns_7-en-20261014.png" alt="Image panel toolbar with the Zoom in and Zoom out buttons and their tooltips." width="277"><figcaption><p>The Zoom in and Zoom out buttons in the image panel toolbar.</p></figcaption></figure>

If you defined a column by mistake, it can be selected by clicking it and deleted with the **“Delete selected column”** button:

<figure><img src="../../../../.gitbook/assets/define_tables_and_columns_9-en-20261014.png" alt="Image panel toolbar with the Delete selected column button and its tooltip." width="563"><figcaption><p>The Delete selected column button in the image panel toolbar.</p></figcaption></figure>

<mark style="color:red;">**Note**</mark>: The button is only visible if the column is selected.

If you are done defining all tables and all columns on your document, use the **“Save”** button to activate your changes and to extract the data from the document:

<figure><img src="../../../../.gitbook/assets/define_tables_and_columns_8-en-20261014.png" alt="Image panel toolbar in column mode with the Save button and its tooltip." width="563"><figcaption><p>The Save button applies the defined tables and columns.</p></figcaption></figure>

The data of all defined areas will be extracted and shown on the right side:

<figure><img src="../../../../.gitbook/assets/define_tables_and_columns_10-en-20261014.png" alt="Right-hand panel listing the extracted columns of the trained table after saving." width="375"><figcaption><p>The extracted column data shown in the right-hand panel.</p></figcaption></figure>

### 5. Review the Extracted Columns

The right-hand panel lists every column that was extracted from the trained table. Check that all columns you defined appear there before you continue; a missing column means the table rectangle or the column boundaries have to be corrected on the document. The available tuning options are described in [Advanced Settings](advanced-settings.md), and irregular layouts are covered in [Structuring and Improving Table Extraction in DocBits](improving-table-extraction-with-regex.md).

### 6. Save and Extract

Click **“Save Rules”** once all tables and columns have been defined.

<figure><img src="../../../../.gitbook/assets/define_tables_and_columns_10b-en-20261014.png" alt="Right-hand panel with the Save Rules and Delete Rules buttons below the extracted columns." width="375"><figcaption><p>The Save Rules and Delete Rules buttons below the extracted columns.</p></figcaption></figure>

* This tells DocBits where to find table data for this specific supplier.
* The next time a document from the same supplier is uploaded, DocBits will automatically extract the table using the saved rules.

<mark style="color:red;">**Note**</mark>: This training is supplier-specific. It will not apply to documents from other suppliers.

To remove the trained rules again, use the **“Delete Rules”** button next to **“Save Rules”**; see [Save and Delete Rules](save-and-delete-rules.md) for details.
