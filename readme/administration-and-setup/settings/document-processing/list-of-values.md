# List Of Values

## Overview

The **Liste des valeurs** feature allows you to create and manage predefined sets of values. This is particularly useful for configuring dropdown menus in the [**Champs**](../global-settings/document-types/fields/) section, which can later be used in **Validation sur le terrain**.

These lists can be customized for different sub-organizations and support multiple languages, providing flexibility across **DocBits**.

## How to Access?

You can access the **Liste des valeurs** by navigating to **Settings → Document Processing → List of Values**.

## How to Add or Delete a List

### Create a New List of Values

1.  Click **Nouveau** in the upper-right corner of the screen.

    <figure><img src="../../../.gitbook/assets/s150-list_of_values_1-fr.png" alt="Vue des listes de valeurs avec les noms configurés masqués."><figcaption><p>Vue des listes de valeurs avec les noms configurés masqués.</p></figcaption></figure>
2. Enter a **Nom** for your list.
3. _(Optional)_ Select a **Sous-organisation** for which the list should be active.
4.  Click **Enregistrer** to create the list.

### How to Delete a List

To delete a list, click the trash can icon next to the corresponding list.

<mark style="color:red;">**Note**</mark>: The list will be deleted immediately. Lists marked with the [**Standard**](list-of-values.md#system-defined-lists-and-rows) tag cannot be deleted.

## How to Add, Edit, or Remove Values from an Existing List&#x20;

You can manage values in an existing **Liste des valeurs** using one of the following methods:

* [**Manually add values**](list-of-values.md#manually-add-values) – Enter values individually through the interface.
* [**Import values from a CSV file**](list-of-values.md#import-values-from-a-csv-file) – Upload a CSV file to add multiple values at once.

### Manually Add Values

1.  Click on the list you want to modify.

2.  Click on **Actions.**

3.  Click on **Add Row.**

Now you can specify multiple properties for each entry:

**Valeur**: This is how the item will be stored internally within **DocBits**. It remains the same across all languages and also serves as the default display text during field validation if no label is specified for the selected language.

**Étiquette**: This is the text displayed on the validation screen, based on the selected language. If no label is available for the active language in DocBits, the system will default to displaying the **Valeur**.

**Langue**: Specifies the language in which the label will be displayed.\
A more detailed explanation can be found [here](list-of-values.md#add-translations-to-your-values).

**Sous-organisations**: Specifies which **sub-organization** the row should be active for. If left blank, the row will be available for all organizations.

**Synonymes**: Here you can specify additional values that help train your document.\
For example, if **EUR** is your primary **value**, you can add EURO and € as **synonyms**. When the document is trained using any of these **synonyms**, **DocBits** will automatically recognize and select EUR as the corresponding value from your list.\
<mark style="color:red;">**Note**</mark>: Each synonym must be confirmed by pressing **Enter** to add it to the list.

4.  After entering all desired properties, click the **Enregistrer** button to add the row.

### Import Values from a CSV File

To add multiple values at once via CSV import:

1.  Click on the list you want to update.

2.  Click **Actes**.

3.  Click on **Télécharger le CSV**.

4. Click **Fichier** to browse and select the CSV file you want to upload.
5. Choose the appropriate **Délimiteur** used in the CSV file (`;` or `,`).
6.  Click **Télécharger** to import the values.

### Edit Existing Values

1. Locate the row you want to edit.
2. Click the three dots in the **Actes** column.
3.  Select **Éditer** from the dropdown menu.

4. Make the required changes.
5.  Click **Enregistrer** to apply your changes.

### Delete Values

1. Locate the row you want to delete.
2. Click the three dots in the **Actes** column.
3.  Select **Supprimer** from the dropdown menu.

<mark style="color:red;">**Note**</mark>: The row will be deleted immediately. Rows marked with the [**Défaut**](list-of-values.md#system-defined-lists-and-rows) tag cannot be deleted.

## Add Translations to Your Values

You can add as many translations as there are supported languages in **DocBits**.

To add a translation:

1.  Click the plus (+) icon.

2.  Select a language from the dropdown menu.

3.  Enter the desired translation in the **Étiquette** field.

4.  To add another translation, click the plus (+) icon again.

5.  To remove a translation, click the trash can icon.

6.  When finished, click the **Enregistrer** button to save your translations.

<mark style="color:red;">**Note**</mark>: If no **Étiquette** is available for the active language, DocBits will default to displaying the **Valeur**.

## System-Defined Lists and Rows

Some lists are pre-created by the system and are marked with the **Standard** tag. These lists cannot be deleted, but you can add new rows to them and remove those newly added rows if necessary.

Within these standard lists, certain rows are marked with the **Défaut** tag—these are system-defined entries. You can add new **labels** in different languages, but these default rows cannot be deleted.
