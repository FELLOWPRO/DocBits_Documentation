# Export Tax Codes to LN

## **Overview:**

\
This guide will walk you through the setup process to ensure tax codes are correctly exported from DocBits to LN.

## **Single Tax Codes**

### **Step 1: Set Up List of Values**

1.  Go to **Settings** -> **Document Processing** -> **List of Values**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_1.png" alt="Settings menu open with the Document Processing group and the List of Values entry"><figcaption>Settings: Document Processing > List of Values</figcaption></figure>
2.  Click **New**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_2 (1).png" alt="List of Values page with the existing lists and the New button"><figcaption>List of Values page with the existing lists</figcaption></figure>
3.  Create a list with the name `Tax_Country` and click **Save**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_3.png" alt="Create New list dialog with the name Tax_Country entered" width="375"><figcaption>Create the list Tax_Country</figcaption></figure>
4.  Create the following three additional lists:

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div align="left"><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt="Create New list dialog with the name Tax_Code_Full entered"><figcaption>Create the list Tax_Code_Full</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt="Create New list dialog with the name Tax_Code_Reduced entered"><figcaption>Create the list Tax_Code_Reduced</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt="Create New list dialog with the name Tax_Code_Free entered"><figcaption>Create the list Tax_Code_Free</figcaption></figure></div>
5.  Click on one of the newly created lists to open it. Then, press the **Add Row** button to add a new row.

    <figure><img src="../../../.gitbook/assets/TaxCode_4.png" alt="List of Values page with the Add Row button below the opened list"><figcaption>Add a row to the opened list</figcaption></figure>
6.  Enter the desired respective values from **LN** and press **Save** to save the changes.

    * If you have multiple values, you can click **Add More Values** to add them.

    <div align="left"><figure><img src="../../../.gitbook/assets/TaxCodes_5.png" alt="Create values dialog with one LN tax code entered in the Name field"><figcaption>Enter the LN tax code in the Name field</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_27.png" alt="Create values dialog with the value 800 added through Add More Values"><figcaption>Add a second value with Add More Values</figcaption></figure></div>

    * **NOTE:** You can find the Tax Codes in LN under: **Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

    <figure><img src="../../../.gitbook/assets/TaxCodes_LN.png" alt="Infor LN Tax Codes by Country session for Austria with the Tax Code and Kind of Tax columns"><figcaption>LN: Common > Taxation > Master Data > Tax Codes > Tax Codes by Country</figcaption></figure>

### **Step 2: Add Fields in DocBits**

1.  Navigate to **Settings** -> **Global Settings** -> **Document Types**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_6.png" alt="Global Settings menu open with the Document Types entry"><figcaption>Settings: Global Settings > Document Types</figcaption></figure>
2.  Choose the **Fields** menu corresponding to the Document Type where you wish to add the fields.

    <figure><img src="../../../.gitbook/assets/TaxCodes_7.png" alt="Document Types page with the Fields menu below each document type"><figcaption>Open the Fields menu of the document type</figcaption></figure>
3.  Under **VAT & Amounts**, create six new fields as follows:

    <figure><img src="../../../.gitbook/assets/TaxCodes_8.png" alt="Fields tab with the VAT &amp; Amounts group and the Create New button"><figcaption>Fields tab: the VAT &amp; Amounts group</figcaption></figure>

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>Name</strong></td><td><strong>Title</strong></td><td><strong>Field Type</strong></td><td><strong>List of Values</strong></td></tr><tr><td><code>tax_country</code></td><td>Tax Country</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>Tax Country Reduced</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>Tax Country Free</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>Tax Code</td><td>Dropdown</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>Tax Code Reduced</td><td>Dropdown</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>Tax Code Free</td><td>Dropdown</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10 (1).png" alt="Document field details dialog for tax_country with field type Dropdown and list Tax_Country"><figcaption>Field tax_country: Dropdown, list Tax_Country</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11 (1).png" alt="Document field details dialog for tax_country_2 with title Tax Country Reduced"><figcaption>Field tax_country_2: Dropdown, list Tax_Country</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt="Document field details dialog for tax_country_3 with title Tax Country Free"><figcaption>Field tax_country_3: Dropdown, list Tax_Country</figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13 (1).png" alt="Document field details dialog for tax_code_without_country with list Tax_Code_Full"><figcaption>Field tax_code_without_country: Dropdown, list Tax_Code_Full</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14 (1).png" alt="Document field details dialog for tax_code_without_country_2 with list Tax_Code_Reduced"><figcaption>Field tax_code_without_country_2: Dropdown, list Tax_Code_Reduced</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15 (1).png" alt="Document field details dialog for tax_code_without_country_3 with list Tax_Code_Free"><figcaption>Field tax_code_without_country_3: Dropdown, list Tax_Code_Free</figcaption></figure></div>

4.  After saving each field, click on **Save Settings** to apply the changes.

    <figure><img src="../../../.gitbook/assets/TaxCodes_20 (2).png" alt="Fields tab with the Save Settings button above the field list"><figcaption>Save Settings to apply the new fields</figcaption></figure>

### **Step 3: Edit Layout**

1.  Go to **Settings** -> **Global Settings** -> **Document Types**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_6.png" alt="Global Settings menu open with the Document Types entry"><figcaption>Settings: Global Settings > Document Types</figcaption></figure>
2.  Open the **Edit Layout** menu for the Document Type you want to edit.

    <figure><img src="../../../.gitbook/assets/TaxCodes_19.png" alt="Document Types page with the Edit layout link below each document type"><figcaption>Open Edit layout of the document type</figcaption></figure>
3.  Select the appropriate **Document Origin** for which you want to apply the Tax Codes

    <figure><img src="../../../.gitbook/assets/TaxCodes_26.png" alt="Layout Builder with the Document Origin selector and the template toolbar"><figcaption>Layout Builder: select the Document Origin</figcaption></figure>
4.  Scroll down to the **Tax Details** section.

    <figure><img src="../../../.gitbook/assets/TaxCodes_21.png" alt="Layout Builder with the Tax Details group and its fields in the element tree"><figcaption>Scroll to the Tax Details group</figcaption></figure>
5. Expand the **Form Elements** dropdown menu.
6.  In the **Tax Details** section, use the **Horizontal Separator Tool**. Drag and drop it between the sub-sections within the tax section to clearly separate them and reduce confusion.

    <figure><img src="../../../.gitbook/assets/TaxCodes_22 (1).png" alt="Layout Builder with the Form Elements dropdown expanded"><figcaption>Expand Form Elements</figcaption></figure>
7. Expand the **Form Fields** dropdown menu.
8.  Search for **Tax Country** and drag and drop the field into its respective area.

    <figure><img src="../../../.gitbook/assets/TaxCodes_23 (2).png" alt="Layout Builder with the Tax Country field dropped into the Tax Details area"><figcaption>Drag Tax Country into the Tax Details area</figcaption></figure>
9.  Search for **Tax Code** and drag and drop the field into its corresponding area.

    <figure><img src="../../../.gitbook/assets/TaxCodes_24 (1).png" alt="Layout Builder with the Tax Code field placed below Tax Country"><figcaption>Drag Tax Code into the Tax Details area</figcaption></figure>
10. Save the template.

    <figure><img src="../../../.gitbook/assets/TaxCodes_25.png" alt="Layout Builder with the saved template and both tax fields in the Tax Details group"><figcaption>Saved template with the two tax fields</figcaption></figure>

### Step 4: Verify that Everything Worked

After uploading a new document into DocBits with the correct document settings selected, you should now be able to select the tax codes you added to the lists in Step 1.

<figure><img src="../../../.gitbook/assets/TaxCodes_31.png" alt="Field validation view of an invoice with the Tax Country and Tax Code dropdowns filled"><figcaption>The new dropdowns in the validation view</figcaption></figure>

## Multi Tax Code

### **Step 1: Set Up List of Values**

1.  Go to **Settings** -> **Document Processing** -> **List of Values**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_1.png" alt="Settings menu open with the Document Processing group and the List of Values entry"><figcaption>Settings: Document Processing > List of Values</figcaption></figure>
2.  Click **New**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_2 (1).png" alt="List of Values page with the existing lists and the New button"><figcaption>List of Values page with the existing lists</figcaption></figure>
3.  Create a list with the name `Tax_Country` and click **Save**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_3.png" alt="Create New list dialog with the name Tax_Country entered" width="375"><figcaption>Create the list Tax_Country</figcaption></figure>
4.  Create the following three additional lists:

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div align="left"><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt="Create New list dialog with the name Tax_Code_Full entered"><figcaption>Create the list Tax_Code_Full</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt="Create New list dialog with the name Tax_Code_Reduced entered"><figcaption>Create the list Tax_Code_Reduced</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt="Create New list dialog with the name Tax_Code_Free entered"><figcaption>Create the list Tax_Code_Free</figcaption></figure></div>
5.  Click on one of the newly created lists to open it. Then, press the **Add Row** button to add a new row.

    <figure><img src="../../../.gitbook/assets/TaxCode_4.png" alt="List of Values page with the Add Row button below the opened list"><figcaption>Add a row to the opened list</figcaption></figure>
6.  Enter the desired respective values from **LN** and press **Save** to save the changes.

    * If you have multiple values, you can click **Add More Values** to add them.

    <div align="left"><figure><img src="../../../.gitbook/assets/TaxCodes_5.png" alt="Create values dialog with one LN tax code entered in the Name field"><figcaption>Enter the LN tax code in the Name field</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_27.png" alt="Create values dialog with the value 800 added through Add More Values"><figcaption>Add a second value with Add More Values</figcaption></figure></div>

    * **NOTE:** You can find the Tax Codes in LN under: **Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

    <figure><img src="../../../.gitbook/assets/TaxCodes_LN.png" alt="Infor LN Tax Codes by Country session for Austria with the Tax Code and Kind of Tax columns"><figcaption>LN: Common > Taxation > Master Data > Tax Codes > Tax Codes by Country</figcaption></figure>

### **Step 2: Add Fields in DocBits**

1.  Navigate to **Settings** -> **Global Settings** -> **Document Types**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_6.png" alt="Global Settings menu open with the Document Types entry"><figcaption>Settings: Global Settings > Document Types</figcaption></figure>
2.  Choose the **Fields** menu corresponding to the Document Type where you wish to add the fields.

    <figure><img src="../../../.gitbook/assets/TaxCodes_7.png" alt="Document Types page with the Fields menu below each document type"><figcaption>Open the Fields menu of the document type</figcaption></figure>
3.  Under **VAT & Amounts**, create six new fields as follows:

    <figure><img src="../../../.gitbook/assets/TaxCodes_8.png" alt="Fields tab with the VAT &amp; Amounts group and the Create New button"><figcaption>Fields tab: the VAT &amp; Amounts group</figcaption></figure>

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>Name</strong></td><td><strong>Title</strong></td><td><strong>Field Type</strong></td><td><strong>Value</strong></td></tr><tr><td><code>tax_country</code></td><td>Tax Country</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>Tax Country Reduced</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>Tax Country Free</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>Tax Code</td><td>Dropdown</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>Tax Code Reduced</td><td>Dropdown</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>Tax Code Free</td><td>Dropdown</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10 (1).png" alt="Document field details dialog for tax_country with field type Dropdown and list Tax_Country"><figcaption>Field tax_country: Dropdown, list Tax_Country</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11 (1).png" alt="Document field details dialog for tax_country_2 with title Tax Country Reduced"><figcaption>Field tax_country_2: Dropdown, list Tax_Country</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt="Document field details dialog for tax_country_3 with title Tax Country Free"><figcaption>Field tax_country_3: Dropdown, list Tax_Country</figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13 (1).png" alt="Document field details dialog for tax_code_without_country with list Tax_Code_Full"><figcaption>Field tax_code_without_country: Dropdown, list Tax_Code_Full</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14 (1).png" alt="Document field details dialog for tax_code_without_country_2 with list Tax_Code_Reduced"><figcaption>Field tax_code_without_country_2: Dropdown, list Tax_Code_Reduced</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15 (1).png" alt="Document field details dialog for tax_code_without_country_3 with list Tax_Code_Free"><figcaption>Field tax_code_without_country_3: Dropdown, list Tax_Code_Free</figcaption></figure></div>

4.  After saving each field, click on **Save Settings** to apply the changes.

    <figure><img src="../../../.gitbook/assets/TaxCodes_20 (2).png" alt="Fields tab with the Save Settings button above the field list"><figcaption>Save Settings to apply the new fields</figcaption></figure>

### **Step 3: Edit Layout**

1.  Go to **Settings** -> **Global Settings** -> **Document Types**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_6.png" alt="Global Settings menu open with the Document Types entry"><figcaption>Settings: Global Settings > Document Types</figcaption></figure>
2.  Open the **Edit Layout** menu for the Document Type you want to edit.

    <figure><img src="../../../.gitbook/assets/TaxCodes_19.png" alt="Document Types page with the Edit layout link below each document type"><figcaption>Open Edit layout of the document type</figcaption></figure>
3.  Select the appropriate **Document Origin** for which you want to apply the Tax Codes

    <figure><img src="../../../.gitbook/assets/TaxCodes_26.png" alt="Layout Builder with the Document Origin selector and the template toolbar"><figcaption>Layout Builder: select the Document Origin</figcaption></figure>
4.  Scroll down to the **Tax Details** section.

    <figure><img src="../../../.gitbook/assets/TaxCodes_21.png" alt="Layout Builder with the Tax Details group and its fields in the element tree"><figcaption>Scroll to the Tax Details group</figcaption></figure>
5. Expand the **Form Elements** dropdown menu.
6.  In the Tax Details section use the **Sub Group** Tool. Drag and Drop it next to an existing field

    <figure><img src="../../../.gitbook/assets/TaxCodesMulti_1.png" alt="Layout Builder with the Sub Group tool in the Form Elements dropdown"><figcaption>Select the Sub Group tool</figcaption></figure>
7.  To name your subgroup, click on the subgroup and enter your desired name in the **Label** field.

    <div><figure><img src="../../../.gitbook/assets/TaxCodesMulti_2.png" alt="Layout Builder with a new empty subgroup next to an existing field"><figcaption>Drop the subgroup next to a field</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodesMulti_3.png" alt="Properties panel with the Label field of the new subgroup"><figcaption>Name the subgroup in the Label field</figcaption></figure></div>
8.  Drag and drop the fields that correspond to this group into the **Sub Group** field.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_4.png" alt="Layout Builder with the tax fields moved into the new subgroup"><figcaption>Move the tax fields into the subgroup</figcaption></figure>
9. Expand the **Fields** dropdown menu.
10. Search for **Tax** and drag and drop the respective fields, such as **Tax Country** and **Tax Code**, into the corresponding subgroup.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_5.png" alt="Layout Builder with Tax Country and Tax Code inside the subgroup"><figcaption>Tax Country and Tax Code in the subgroup</figcaption></figure>
11. Repeat steps 5 through 10 2 times to reach the following state:

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_6.png" alt="Layout Builder with three tax subgroups for full, reduced and free rates"><figcaption>Three subgroups for full, reduced and free</figcaption></figure>
12. Save the template.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_7.png" alt="Layout Builder with the saved multi-tax template"><figcaption>Save the multi-tax template</figcaption></figure>

### Step 4: Verify that Everything Worked and resulting changes

After uploading a new document into DocBits with the correct document settings selected, you will be able to select the tax codes you added in Step 1 and add multiple tax codes configured in Step 3.

* The document will begin with three distinct sections: one for Tax Full amounts, one for Tax Reduced amounts, and one for Tax Free amounts.
* Clicking the plus button within a section will create a duplicate, allowing multiple submissions at the selected tax rate.

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_8.png" alt="Field validation view with three separate tax sections and the plus and remove buttons"><figcaption>Three tax sections in the validation view</figcaption></figure>

* Sections can be deleted by clicking the remove button.

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_9.png" alt="Field validation view with one tax section duplicated by the plus button"><figcaption>Add another section with the plus button</figcaption></figure>

* Total Amounts will be calculated as a sum of all sections
* Validation of Total Amount will be modified based on all tax-sections
* Scripts for new sections can only be applied once fields have been added to the view.

### Note for LN:

In **LN** USt Position will be filled out based on the position number from the Tax Code/Tax Country dropdown menu. Only the Position number will be sent to export.

<figure><img src="../../../.gitbook/assets/TaxCodesLN_2.png" alt="Infor LN Tax Lines by External Invoice session with the tax position column"><figcaption>LN: Tax Lines by External Invoice</figcaption></figure>

<figure><img src="../../../.gitbook/assets/TaxCodesLN_3.png" alt="Infor LN Tax Lines by External Invoice session showing the position number"><figcaption>LN: the position number is exported as USt Position</figcaption></figure>

#### **Export Mapping**

To link the Tax Line with the Cost Line:

1. Add `TaxLine` to the **InvoiceCostFields** list.
2. Add the following entry, following the example below:\
   `ICF_TaxLine = TF_position`

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_10.png" alt="Export mapping file with the ICF_TaxLine entry next to the invoice cost fields"><figcaption>Export mapping: ICF_TaxLine = TF_position</figcaption></figure>
