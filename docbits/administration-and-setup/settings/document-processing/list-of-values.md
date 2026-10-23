# List Of Values

## Overview

The **List of Values** feature allows you to create and manage predefined sets of values. This is particularly useful for configuring dropdown menus in the [**Fields**](../global-settings/document-types/fields/) section, which can later be used in **Field Validation**.

These lists can be customized for different sub-organizations and support multiple languages, providing flexibility across **DocBits**.

## How to Access?

You can access the **List of Values** by navigating to **Settings → Document Processing → List of Values**.

<figure><img src="../../../.gitbook/assets/settings_list_of_values.png" alt="Settings menu in DocBits with Document Processing expanded and List of Values highlighted among Import, Rule Management and Export entries"><figcaption></figcaption></figure>

## How to Add or Delete a List

### Create a New List of Values

1.  Click **New** in the upper-right corner of the screen.

    <figure><img src="../../../.gitbook/assets/s150-list_of_values_1.png" alt="English list-of-values overview with configured list names hidden."><figcaption><p>English list-of-values overview with configured list names hidden.</p></figcaption></figure>
2. Enter a **Name** for your list.
3. _(Optional)_ Select a **Sub-Organization** for which the list should be active.
4.  Click **Save** to create the list.

    <figure><img src="../../../.gitbook/assets/list_of_values_2.png" alt="Dialog Create New list in the List of Values page with a Name field, a Sub-Organizations dropdown and a Save button"><figcaption></figcaption></figure>

### How to Delete a List

To delete a list, click the trash can icon next to the corresponding list.

<figure><img src="../../../.gitbook/assets/list_of_values_13.png" alt="List of Values page showing the configured lists ISO_Currency, Steuercode, Invoice_Sub_Type and Invoice_Type with the Document Processing menu open"><figcaption></figcaption></figure>

<mark style="color:red;">**Note**</mark>: The list will be deleted immediately. Lists marked with the [**Standard**](list-of-values.md#system-defined-lists-and-rows) tag cannot be deleted.

## How to Add, Edit, or Remove Values from an Existing List

You can manage values in an existing **List of Values** using one of the following methods:

* [**Manually add values**](list-of-values.md#manually-add-values) – Enter values individually through the interface.
* [**Import values from a CSV file**](list-of-values.md#import-values-from-a-csv-file) – Upload a CSV file to add multiple values at once.

### Manually Add Values

1.  Click on the list you want to modify.

    <figure><img src="../../../.gitbook/assets/list_of_values_3.png" alt="List of Values page with the list entries ISO_Currency, Steuercode, Invoice_Sub_Type and Invoice_Type and the list selector List open"><figcaption></figcaption></figure>
2.  Click on **Actions.**

    <figure><img src="../../../.gitbook/assets/list_of_values_4.png" alt="List of Values page showing the list selector List open above the columns Value, Sub-Organizations, Synonyms, Language, Label and Actions"><figcaption></figcaption></figure>
3.  Click on **Add Row.**

    <figure><img src="../../../.gitbook/assets/list_of_values_5.png" alt="List of Values page with the Actions menu open offering Add Row and Upload CSV above the Value, Sub-Organizations, Synonyms, Language, Label and Actions columns"><figcaption></figcaption></figure>

Now you can specify multiple properties for each entry:

<figure><img src="../../../.gitbook/assets/list_of_values_6.png" alt="List of Values page with the Actions menu open offering Add Row and Upload CSV and a SAVE and CANCEL row editing toolbar"><figcaption></figcaption></figure>

**Value**: This is how the item will be stored internally within **DocBits**. It remains the same across all languages and also serves as the default display text during field validation if no label is specified for the selected language.

**Label**: This is the text displayed on the validation screen, based on the selected language. If no label is available for the active language in DocBits, the system will default to displaying the **Value**.

**Language**: Specifies the language in which the label will be displayed.\
A more detailed explanation can be found [here](list-of-values.md#add-translations-to-your-values).

**Sub-Organizations**: Specifies which **sub-organization** the row should be active for. If left blank, the row will be available for all organizations.

**Synonyms**: Here you can specify additional values that help train your document.\
For example, if **EUR** is your primary **value**, you can add EURO and € as **synonyms**. When the document is trained using any of these **synonyms**, **DocBits** will automatically recognize and select EUR as the corresponding value from your list.\
<mark style="color:red;">**Note**</mark>: Each synonym must be confirmed by pressing **Enter** to add it to the list.

4.  After entering all desired properties, click the **Save** button to add the row.

    <figure><img src="../../../.gitbook/assets/list_of_values_11.png" alt="List of Values page with an empty row for editing showing Sub-Organizations and Synonyms dropdowns plus Save and Cancel icons"><figcaption></figcaption></figure>

### Import Values from a CSV File

<mark style="color:red;">**Note:**</mark> When importing a CSV file, only the following columns are processed: **Value**, **Sub-Organization**, **Synonyms**, **Language**, and **Label**.\
Any additional columns included in the CSV file are **ignored** during the import.

To add multiple values at once via CSV import:

1.  Click on the list you want to update.

    <figure><img src="../../../.gitbook/assets/list_of_values_3.png" alt="List of Values page with the list entries ISO_Currency, Steuercode, Invoice_Sub_Type and Invoice_Type and the list selector List open"><figcaption></figcaption></figure>
2.  Click **Actions**.

    <figure><img src="../../../.gitbook/assets/list_of_values_4.png" alt="List of Values page showing the list selector List open above the columns Value, Sub-Organizations, Synonyms, Language, Label and Actions"><figcaption></figcaption></figure>
3.  Click on **Upload CSV**.

    <figure><img src="../../../.gitbook/assets/list_of_values_7.png" alt="List of Values page with the Actions menu open offering Add Row and Upload CSV above the table columns"><figcaption></figcaption></figure>
4. Click **File** to browse and select the CSV file you want to upload.
5. Choose the appropriate **Delimiter** used in the CSV file (`;` or `,`).
6.  Click **Upload** to import the values.

    <figure><img src="../../../.gitbook/assets/list_of_values_8.png" alt="List of Values page showing the ISO_Currency, Steuercode, Invoice_Sub_Type and Invoice_Type lists and the Document Processing menu expanded"><figcaption></figcaption></figure>

### Edit Existing Values

1. Locate the row you want to edit.
2. Click the three dots in the **Actions** column.
3.  Select **Edit** from the dropdown menu.

    <figure><img src="../../../.gitbook/assets/list_of_values_10.png" alt="List of values table with the Actions column dropdown open showing Edit and Delete options"><figcaption></figcaption></figure>
4. Make the required changes.
5.  Click **Save** to apply your changes.

    <figure><img src="../../../.gitbook/assets/list_of_values_11.png" alt="List of Values page with an empty row for editing showing Sub-Organizations and Synonyms dropdowns plus Save and Cancel icons"><figcaption></figcaption></figure>

### Delete Values

1. Locate the row you want to delete.
2. Click the three dots in the **Actions** column.
3.  Select **Delete** from the dropdown menu.

    <figure><img src="../../../.gitbook/assets/list_of_values_12.png" alt="List of values table with the Actions dropdown open and the Delete option highlighted"><figcaption></figcaption></figure>

<mark style="color:red;">**Note**</mark>: The row will be deleted immediately. Rows marked with the [**Default**](list-of-values.md#system-defined-lists-and-rows) tag cannot be deleted.

## Add Translations to Your Values

You can add as many translations as there are supported languages in **DocBits**.

To add a translation:

1.  Click the plus (+) icon.

    <figure><img src="../../../.gitbook/assets/list_of_values_14.png" alt="List of values table with a new empty row for Value, Sub-Organizations, Synonyms, Language and Label"><figcaption></figcaption></figure>
2.  Select a language from the dropdown menu.

    <figure><img src="../../../.gitbook/assets/list_of_values_15.png" alt="Row editor with the Language dropdown open listing English, Spanish, French, Italian, Dutch and Chinese"><figcaption></figcaption></figure>
3.  Enter the desired translation in the **Label** field.

    <figure><img src="../../../.gitbook/assets/list_of_values_16.png" alt="Row editor with a German language row and the translation zeile entered in the Label field"><figcaption></figcaption></figure>
4.  To add another translation, click the plus (+) icon again.

    <figure><img src="../../../.gitbook/assets/list_of_values_17.png" alt="Row editor with two translation rows for English and German above the Save and Cancel buttons"><figcaption></figcaption></figure>
5.  To remove a translation, click the trash can icon.

    <figure><img src="../../../.gitbook/assets/list_of_values_18.png" alt="Row editor with English, Dutch, Italian and German language rows in the list of values"><figcaption></figcaption></figure>
6.  When finished, click the **Save** button to save your translations.

    <figure><img src="../../../.gitbook/assets/list_of_values_19.png" alt="Row editor with English and German translation rows and the Save and Cancel buttons below"><figcaption></figcaption></figure>

<mark style="color:red;">**Note**</mark>: If no **Label** is available for the active language, DocBits will default to displaying the **Value**.

## System-Defined Lists and Rows

Some lists are pre-created by the system and are marked with the **Standard** tag. These lists cannot be deleted, but you can add new rows to them and remove those newly added rows if necessary.

<figure><img src="../../../.gitbook/assets/list_of_values_9.png" alt="ISO_Currency list open with Add Row and Upload CSV buttons and currency values EUR, PKR and USD"><figcaption></figcaption></figure>

Within these standard lists, certain rows are marked with the **Default** tag—these are system-defined entries. You can add new **labels** in different languages, but these default rows cannot be deleted.

<figure><img src="../../../.gitbook/assets/list_of_values_20.png" alt="ISO_Currency list with an open row editor showing Language English and the label Euro above Save and Cancel"><figcaption></figcaption></figure>
