# Structuring and Improving Table Extraction in DocBits

Once a table is extracted and the initial column mapping is complete, you can enhance the quality and structure of the data using several built-in tools. This guide walks you through:

* Grouping rows
* Manual row selection
* Column mapping
* Header refinement using regex

These tools are especially helpful when dealing with complex or inconsistent document layouts.

### 1. Grouping Rows

Documents like invoices or order confirmations often contain table entries where one column (e.g., a description) spans multiple lines, while other columns (e.g., quantity or price) only use one line.

Take this German invoice example — the “Bezeichnung” (description) column spans multiple rows:

![multi-line description](https://lh7-us.googleusercontent.com/Vino2M4Esor3IRHGqBd5Brx7_lKPIwEOlRYBHzMXw4WoacFNW39hbWuwoUNGocubx4Bh9_BvUBqZSWA4U_NmU8FBw4Q1_AiTASgMx-2MLKvsHLJY057oqyks0fQ5b7mI577JTX5rBKdEG90O9F5TcoU)

Initially, DocBits extracts each row separately:

![initial extraction](https://lh7-us.googleusercontent.com/UX5OdkW59HPVROnNzSeZbDw4NYTPbfayDLIXBQi0pwHzUEJ1B5t7I9uKBNc0dmOB3Cile8Xv6AdgVXuUd0aMbQFGWagBCEetw8P-N4zgG_cGTjWHhpDtGQZg27UZKdCDJ5FeEDJgFAYtTB8kZrMSdho)

You can then **group rows based on a column**, such as “Position.” This merges related lines into a single, structured entry:

![grouped result](https://lh7-us.googleusercontent.com/PxA6h2udUuYd1YmHV97t-bzfZzipFpdA5t8gjpGXWx9sA-I4tW3tYwD28icv88UEmitz0EAaWuGkU5ZwqAjcQnoOkmg9u1AcBJW3nITU6eFa0foHB-AQPb0qv0AWaaEwM6WvwaEcAODEUzKtvRZOMN0)

### 2. Manual Row Selection

In some cases, the text on a document is spread across several columns in a single row, making it difficult to assign automatically.

Here’s an example where the “PRAEF” line overlaps **Bezeichnung**, **Menge**, **ME**, and **Preis in EUR**:

![row misalignment](https://lh7-us.googleusercontent.com/LbVbmfdOBpeCWDftPvW0qjEHjbLmWYRrAGTZHVW8VEHQTEvl5GoqH2wkFE5iUOySmF50b1V8CDAZhfMzPTeMQscmc61SDKaqSCW-y0Z7fjlwOjhtjxWD44oCsgHmwrgrBD4cuEGgn9JY_UX3t9jRlPs)

#### 🔧 How to Manually Assign Values:

1.  **Enable Training Mode**

    ![training mode toggle](https://lh7-us.googleusercontent.com/4D8iCXk0p_Mur8bX_11ne_2iA-GOxoFi2OQWlSEvrH1auoE0ksnYXpZx3Pw3PUJJRZJN85dnQlSSBB369FfafXAy8adjFZcnepQnODSaaIj69cxtUKFAXPgn5eyPE6jbJuzStJALMgumlt49Z1Pv3FY)
2.  **Activate Row Edit Mode**

    ![row edit mode](https://lh7-us.googleusercontent.com/8YQmo_WRuKKVjk1a_eoxSBiQr0GncuS4BmCA0aI9aOlrbsIvdj8dZlurxxBHp2lH4ozT4HPWw9qYDW7xLQ7u2DSyU8DrNzSBC7LjzKLTDJ2tudY9a_DENDoK5Aya6L1hcf1WF1RD92S_DzhGVV4Gh6Q)
3.  **Select and Map Text**\
    Click the correct piece of text and assign it to a **blue** column header.

    ![editable columns](https://lh7-us.googleusercontent.com/i2tlbwl9qFE0clthaoRPe7kcPRiURCvemuLEjBK4uAnfsR4auXbftMfEY1ZW5WXwezTBVSG5hbNRkddwIeLtrgJUvZoeKGdPKN8f75O_dPdIWkm4EFALfAj-evDUI3UKrgNOTNjF37C1bBLtE95OA1w)

> Note: Violet-colored columns are already system-mapped and cannot be manually edited.

### 3. Mapping Columns

Column mapping links your extracted data to the expected column headers, ensuring consistency and exportability.

To map or remap a column:

1. Click the column header in the extraction view.
2. Choose the correct target column from the dropdown.

![mapping dropdown](https://lh7-us.googleusercontent.com/X_65pCWrI4HMFr_aiA0eoSDp-yIYy49lULzAZaiIgnr0aIowlLSed21MuehkGLs4UIdQousdfhiZi5pnQtpZ0uUn6dxlzii7WPQvov-kN1_Jimsi6U6zowOLxjBzZzZ47kaRhduAVBd_Ya9QQtXTpJ4)

You can adjust the mapping as often as needed.

### 4. Extract From Above / Below

Some documents are structured in a way where relevant table values don't appear on the same row as other data. In these cases, DocBits allows you to control **where the data should be extracted from**:

* **Extract from Above**: Use this when the value for the current row appears **in the line above**.
* **Extract from Below**: Use this when the value appears **in the line beneath** the current row.

**Where to Find It**

1. Enter **Training Mode**.
2. Click the three dots (⋯) on a column header.
3. Under the **"Extract From"** option, choose `Above` or `Below` depending on the document layout.

### 5. Amount Format

Some columns, such as **Quantity** or **Unit Price**, contain numeric or date values that may follow different formatting conventions depending on the document's origin or locale. DocBits allows you to specify the format these values should follow to ensure accurate extraction and interpretation.

**Amount Format Options:**

* Define the expected number or date format for the column, such as US (MM/DD/YYYY, decimal with dot), Poland (DD.MM.YYYY, decimal with comma), Germany, and others.
* This helps DocBits correctly parse and standardize values even if the document uses a different regional format.

**Where to Find It**

1. Enter **Training Mode**.
2. Click the three dots (⋯) on the header of a supported column (e.g., Quantity, Unit Price).
3. Under the **Amount Format** option, select the desired format matching your document's locale.

### 6. Improving Table Extraction with Regex

### **What It Does**

This feature allows you to define a regex for each table header, improving extraction accuracy and ensuring correct results.

### **How to Use It**

1. Open a document from the supplier for which you want to define a regex.
2.  Navigate to the **Table Extraction** view.\\

    <figure><img src="../../../../.gitbook/assets/image (417).png" alt=""><figcaption></figcaption></figure>
3. Enable **Training Mode**.
4.  Select the table header you want to refine, then choose **Regex**.\\

    <figure><img src="../../../../.gitbook/assets/image (416).png" alt=""><figcaption></figcaption></figure>
5.  A popup will appear where you can enter and define your regex.\\

    <figure><img src="../../../../.gitbook/assets/iScreen Shoter - Google Chrome - 250303135020.jpg" alt=""><figcaption></figcaption></figure>
6.  Click **Validate** to check the regex, then **Save Changes** to apply it.\\

    <figure><img src="../../../../.gitbook/assets/iScreen Shoter - Google Chrome - 250303135153.jpg" alt=""><figcaption></figcaption></figure>
7. **Save the rule and confirm** to apply the changes.

### When to Use Each Feature

Use these tools to increase extraction accuracy and reduce manual work:

* **Grouping**: When a description or any column spans multiple rows and needs to be combined for clarity.
* **Manual Row Selection**: When rows aren’t structured cleanly, and parts of the content fall into the wrong columns.
* **Column Mapping**: When the automatically detected column names don’t match your structure or need refinement.
* **Regex Rules**: When table headers vary slightly across documents from the same supplier or OCR introduces inconsistencies.
