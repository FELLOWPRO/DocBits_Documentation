# Export Tax Codes to LN

## **Overview:**

\
This guide will walk you through the setup process to ensure tax codes are correctly exported from DocBits to LN.

## **Single Tax Codes**

### **Step 1: Set Up List of Values**

1.  Go to **Settings** -> **Document Processing** -> **List of Values**.

    <figure><img src="../../../.gitbook/assets/site-extra-list-of-values-en.png" alt="Value lists in DocBits; organization-specific list names are hidden."><figcaption><p>Value lists in DocBits; organization-specific list names are hidden.</p></figcaption></figure>
2.  Click **New**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_2 (1).png" alt="List of Values settings page with existing lists and the New button highlighted"><figcaption></figcaption></figure>
3.  Create a list with the name `Tax_Country` and click **Save**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_3.png" alt="Create New list dialog with the name Tax_Country entered and the Save button highlighted" width="375"><figcaption></figcaption></figure>
4.  Create the following three additional lists:

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div align="left"><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt="Create New list dialog with the name Tax_Code_Full entered and the Save button highlighted"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt="Create New list dialog with the name Tax_Code_Reduced entered and the Save button highlighted"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt="Create New list dialog with the name Tax_Code_Free entered and the Save button highlighted"><figcaption></figcaption></figure></div>
5.  Click on one of the newly created lists to open it. Then, press the **Add Row** button to add a new row.

    <figure><img src="../../../.gitbook/assets/TaxCode_4.png" alt="List of Values page with the empty Tax_Country list expanded and the Add Row button highlighted"><figcaption></figcaption></figure>
6.  Enter the desired respective values from **LN** and press **Save** to save the changes.

    * If you have multiple values, you can click **Add More Values** to add them.

    <div align="left"><figure><img src="../../../.gitbook/assets/TaxCodes_5.png" alt="Create values dialog with the value DE entered in the Name field and Add More Values highlighted"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/site-extra-list-value-new-en.png" alt="New-value form: suborganization, synonyms and translations. No value was entered or saved; the language choice concerns the value translation."><figcaption><p>New-value form: suborganization, synonyms and translations. No value was entered or saved; the language choice concerns the value translation.</p></figcaption></figure></div>

    * **NOTE:** You can find the Tax Codes in LN under: **Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

    <figure><img src="../../../.gitbook/assets/TaxCodes_LN.png" alt="LN Tax Codes by Country screen for country AT listing tax codes such as 000, 001 and 002"><figcaption></figcaption></figure>

### **Step 2: Add Fields in DocBits**

1.  Navigate to **Settings** -> **Global Settings** -> **Document Types**.

    <figure><img src="../../../.gitbook/assets/site-extra-document-types-en.png" alt="Document types: select the fields for the relevant type. No switches were changed."><figcaption><p>Document types: select the fields for the relevant type. No switches were changed.</p></figcaption></figure>
2.  Choose the **Fields** menu corresponding to the Document Type where you wish to add the fields.

    <figure><img src="../../../.gitbook/assets/TaxCodes_7.png" alt="Document Types page with the Fields link of the Invoice type highlighted"><figcaption></figcaption></figure>
3.  Under **VAT & Amounts**, create six new fields as follows:

    <figure><img src="../../../.gitbook/assets/TaxCodes_8.png" alt="Fields page of the Invoice type with the Create Field button highlighted in the VAT &amp; Amounts group"><figcaption></figcaption></figure>

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>Name</strong></td><td><strong>Title</strong></td><td><strong>Field Type</strong></td><td><strong>List of Values</strong></td></tr><tr><td><code>tax_country</code></td><td>Tax Country</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>Tax Country Reduced</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>Tax Country Free</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>Tax Code</td><td>Dropdown</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>Tax Code Reduced</td><td>Dropdown</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>Tax Code Free</td><td>Dropdown</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10 (1).png" alt="Document field details dialog for tax_country, a Dropdown field using the Tax_Country list"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11 (1).png" alt="Document field details dialog for tax_country_2, a Dropdown field using the Tax_Country list"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt="Document field details dialog for tax_country_3, a Dropdown field using the Tax_Country list"><figcaption></figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13 (1).png" alt="Document field details dialog for tax_code_without_country, a Dropdown using the Tax_Code_Full list"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14 (1).png" alt="Document field details dialog for tax_code_without_country_2, a Dropdown using the Tax_Code_Reduced list"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15 (1).png" alt="Document field details dialog for tax_code_without_country_3, a Dropdown using the Tax_Code_Free list"><figcaption></figcaption></figure></div>

4.  After saving each field, click on **Save Settings** to apply the changes.

    <figure><img src="../../../.gitbook/assets/TaxCodes_20 (2).png" alt="Fields page listing the six new tax country and tax code fields with Save Settings highlighted"><figcaption></figcaption></figure>

### **Step 3: Edit Layout**

1.  Go to **Settings** -> **Global Settings** -> **Document Types**.

    <figure><img src="../../../.gitbook/assets/site-extra-document-types-en.png" alt="Document types: select the fields for the relevant type. No switches were changed."><figcaption><p>Document types: select the fields for the relevant type. No switches were changed.</p></figcaption></figure>
2.  Open the **Edit Layout** menu for the Document Type you want to edit.

    <figure><img src="../../../.gitbook/assets/TaxCodes_19.png" alt="Document Types page with the Edit layout link of the Invoice type highlighted"><figcaption></figcaption></figure>
3.  Select the appropriate **Document Origin** for which you want to apply the Tax Codes

    <figure><img src="../../../.gitbook/assets/TaxCodes_26.png" alt="Layout Builder with the document origin dropdown open, listing Default, Deutsch, United States and other origins"><figcaption></figcaption></figure>
4.  Scroll down to the **Tax Details** section.

    <figure><img src="../../../.gitbook/assets/TaxCodes_21.png" alt="Layout Builder showing the Tax Details group with net amount, tax amount, VAT rate and tax code fields"><figcaption></figcaption></figure>
5. Expand the **Form Elements** dropdown menu.
6.  In the **Tax Details** section, use the **Horizontal Separator Tool**. Drag and drop it between the sub-sections within the tax section to clearly separate them and reduce confusion.

    <figure><img src="../../../.gitbook/assets/TaxCodes_22 (1).png" alt="Layout Builder with the Horizontal Separator form element being dragged between the Tax Details sub-sections"><figcaption></figcaption></figure>
7. Expand the **Form Fields** dropdown menu.
8.  Search for **Tax Country** and drag and drop the field into its respective area.

    <figure><img src="../../../.gitbook/assets/TaxCodes_23 (2).png" alt="Layout Builder with the Tax Country, Tax Country Reduced and Tax Country Free fields dragged into the Tax Details group"><figcaption></figcaption></figure>
9.  Search for **Tax Code** and drag and drop the field into its corresponding area.

    <figure><img src="../../../.gitbook/assets/TaxCodes_24 (1).png" alt="Layout Builder with the Tax Code, Tax Code Reduced and Tax Code Free fields dragged into the Tax Details group"><figcaption></figcaption></figure>
10. Save the template.

    <figure><img src="../../../.gitbook/assets/TaxCodes_25.png" alt="Layout Builder with Tax Country and Tax Code fields placed in each section and the Save button highlighted"><figcaption></figcaption></figure>

### Step 4: Verify that Everything Worked

After uploading a new document into DocBits with the correct document settings selected, you should now be able to select the tax codes you added to the lists in Step 1.

<figure><img src="../../../.gitbook/assets/TaxCodes_31.png" alt="Field Validation screen with the Tax Code dropdown open, showing the values 510 and 800"><figcaption></figcaption></figure>

## Multi Tax Code

### **Step 1: Set Up List of Values**

1.  Go to **Settings** -> **Document Processing** -> **List of Values**.

    <figure><img src="../../../.gitbook/assets/site-extra-list-of-values-en.png" alt="Value lists in DocBits; organization-specific list names are hidden."><figcaption><p>Value lists in DocBits; organization-specific list names are hidden.</p></figcaption></figure>
2.  Click **New**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_2 (1).png" alt="List of Values settings page with existing lists and the New button highlighted"><figcaption></figcaption></figure>
3.  Create a list with the name `Tax_Country` and click **Save**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_3.png" alt="Create New list dialog with the name Tax_Country entered and the Save button highlighted" width="375"><figcaption></figcaption></figure>
4.  Create the following three additional lists:

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div align="left"><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt="Create New list dialog with the name Tax_Code_Full entered and the Save button highlighted"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt="Create New list dialog with the name Tax_Code_Reduced entered and the Save button highlighted"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt="Create New list dialog with the name Tax_Code_Free entered and the Save button highlighted"><figcaption></figcaption></figure></div>
5.  Click on one of the newly created lists to open it. Then, press the **Add Row** button to add a new row.

    <figure><img src="../../../.gitbook/assets/TaxCode_4.png" alt="List of Values page with the empty Tax_Country list expanded and the Add Row button highlighted"><figcaption></figcaption></figure>
6.  Enter the desired respective values from **LN** and press **Save** to save the changes.

    * If you have multiple values, you can click **Add More Values** to add them.

    <div align="left"><figure><img src="../../../.gitbook/assets/TaxCodes_5.png" alt="Create values dialog with the value DE entered in the Name field and Add More Values highlighted"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/site-extra-list-value-new-en.png" alt="New-value form: suborganization, synonyms and translations. No value was entered or saved; the language choice concerns the value translation."><figcaption><p>New-value form: suborganization, synonyms and translations. No value was entered or saved; the language choice concerns the value translation.</p></figcaption></figure></div>

    * **NOTE:** You can find the Tax Codes in LN under: **Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

    <figure><img src="../../../.gitbook/assets/TaxCodes_LN.png" alt="LN Tax Codes by Country screen for country AT listing tax codes such as 000, 001 and 002"><figcaption></figcaption></figure>

### **Step 2: Add Fields in DocBits**

1.  Navigate to **Settings** -> **Global Settings** -> **Document Types**.

    <figure><img src="../../../.gitbook/assets/site-extra-document-types-en.png" alt="Document types: select the fields for the relevant type. No switches were changed."><figcaption><p>Document types: select the fields for the relevant type. No switches were changed.</p></figcaption></figure>
2.  Choose the **Fields** menu corresponding to the Document Type where you wish to add the fields.

    <figure><img src="../../../.gitbook/assets/TaxCodes_7.png" alt="Document Types page with the Fields link of the Invoice type highlighted"><figcaption></figcaption></figure>
3.  Under **VAT & Amounts**, create six new fields as follows:

    <figure><img src="../../../.gitbook/assets/TaxCodes_8.png" alt="Fields page of the Invoice type with the Create Field button highlighted in the VAT &amp; Amounts group"><figcaption></figcaption></figure>

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>Name</strong></td><td><strong>Title</strong></td><td><strong>Field Type</strong></td><td><strong>Value</strong></td></tr><tr><td><code>tax_country</code></td><td>Tax Country</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>Tax Country Reduced</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>Tax Country Free</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>Tax Code</td><td>Dropdown</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>Tax Code Reduced</td><td>Dropdown</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>Tax Code Free</td><td>Dropdown</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10 (1).png" alt="Document field details dialog for tax_country, a Dropdown field using the Tax_Country list"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11 (1).png" alt="Document field details dialog for tax_country_2, a Dropdown field using the Tax_Country list"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt="Document field details dialog for tax_country_3, a Dropdown field using the Tax_Country list"><figcaption></figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13 (1).png" alt="Document field details dialog for tax_code_without_country, a Dropdown using the Tax_Code_Full list"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14 (1).png" alt="Document field details dialog for tax_code_without_country_2, a Dropdown using the Tax_Code_Reduced list"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15 (1).png" alt="Document field details dialog for tax_code_without_country_3, a Dropdown using the Tax_Code_Free list"><figcaption></figcaption></figure></div>

4.  After saving each field, click on **Save Settings** to apply the changes.

    <figure><img src="../../../.gitbook/assets/TaxCodes_20 (2).png" alt="Fields page listing the six new tax country and tax code fields with Save Settings highlighted"><figcaption></figcaption></figure>

### **Step 3: Edit Layout**

1.  Go to **Settings** -> **Global Settings** -> **Document Types**.

    <figure><img src="../../../.gitbook/assets/site-extra-document-types-en.png" alt="Document types: select the fields for the relevant type. No switches were changed."><figcaption><p>Document types: select the fields for the relevant type. No switches were changed.</p></figcaption></figure>
2.  Open the **Edit Layout** menu for the Document Type you want to edit.

    <figure><img src="../../../.gitbook/assets/TaxCodes_19.png" alt="Document Types page with the Edit layout link of the Invoice type highlighted"><figcaption></figcaption></figure>
3.  Select the appropriate **Document Origin** for which you want to apply the Tax Codes

    <figure><img src="../../../.gitbook/assets/TaxCodes_26.png" alt="Layout Builder with the document origin dropdown open, listing Default, Deutsch, United States and other origins"><figcaption></figcaption></figure>
4.  Scroll down to the **Tax Details** section.

    <figure><img src="../../../.gitbook/assets/TaxCodes_21.png" alt="Layout Builder showing the Tax Details group with net amount, tax amount, VAT rate and tax code fields"><figcaption></figcaption></figure>
5. Expand the **Form Elements** dropdown menu.
6.  In the Tax Details section use the **Sub Group** Tool. Drag and Drop it next to an existing field

    <figure><img src="../../../.gitbook/assets/TaxCodesMulti_1.png" alt="Layout Builder with the Sub Group form element being dragged into the Tax Details group"><figcaption></figcaption></figure>
7.  To name your subgroup, click on the subgroup and enter your desired name in the **Label** field.

    <div><figure><img src="../../../.gitbook/assets/TaxCodesMulti_2.png" alt="Layout Builder showing an empty Sub Group inside the Tax Details group"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodesMulti_3.png" alt="Layout Builder properties panel with the Label field of the sub group highlighted"><figcaption></figcaption></figure></div>
8.  Drag and drop the fields that correspond to this group into the **Sub Group** field.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_4.png" alt="Layout Builder with the tax fields being dragged into the sub group named RATE 1"><figcaption></figcaption></figure>
9. Expand the **Fields** dropdown menu.
10. Search for **Tax** and drag and drop the respective fields, such as **Tax Country** and **Tax Code**, into the corresponding subgroup.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_5.png" alt="Layout Builder with the Tax Country and Tax Code fields being dragged into the RATE 1 sub group"><figcaption></figcaption></figure>
11. Repeat steps 5 through 10 2 times to reach the following state:

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_6.png" alt="Layout Builder with the RATE 1, REDUCED RATE and FREE RATE sub groups, each with tax country and tax code fields"><figcaption></figcaption></figure>
12. Save the template.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_7.png" alt="Layout Builder with the three tax rate sub groups complete and the Save button highlighted"><figcaption></figcaption></figure>

### Step 4: Verify that Everything Worked and resulting changes

After uploading a new document into DocBits with the correct document settings selected, you will be able to select the tax codes you added in Step 1 and add multiple tax codes configured in Step 3.

* The document will begin with three distinct sections: one for Tax Full amounts, one for Tax Reduced amounts, and one for Tax Free amounts.
* Clicking the plus button within a section will create a duplicate, allowing multiple submissions at the selected tax rate.

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_8.png" alt="Field Validation screen with the VAT &amp; Amounts rate sections and the plus button to duplicate RATE 1 highlighted"><figcaption></figcaption></figure>

* Sections can be deleted by clicking the remove button.

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_9.png" alt="Field Validation screen with a duplicated RATE 2 section and its minus button highlighted for removal"><figcaption></figcaption></figure>

* Total Amounts will be calculated as a sum of all sections
* Validation of Total Amount will be modified based on all tax-sections
* Scripts for new sections can only be applied once fields have been added to the view.

### Note for LN:

In **LN** USt Position will be filled out based on the position number from the Tax Code/Tax Country dropdown menu. Only the Position number will be sent to export.

<figure><img src="../../../.gitbook/assets/TaxCodesLN_2.png" alt="LN Cost Lines by External Invoice table showing one cost line with ledger account and amount"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/TaxCodesLN_3.png" alt="LN Tax Lines by External Invoice table showing tax line 1 with country DEU, tax code 500 and tax amounts"><figcaption></figcaption></figure>

#### **Export Mapping**

To link the Tax Line with the Cost Line:

1. Add `TaxLine` to the **InvoiceCostFields** list.
2. Add the following entry, following the example below:\
   `ICF_TaxLine = TF_position`

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_10.png" alt="Export mapping configuration with TaxLine added to InvoiceCostFields and the entry ICF_TaxLine=TF_position highlighted"><figcaption></figcaption></figure>
