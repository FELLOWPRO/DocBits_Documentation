# Table Extraction for costing Element

Navigate to **Settings → Document Processing → Classification and Extraction**

<figure><img src="../../../.gitbook/assets/image (430).png" alt="Classification and Extraction settings page in DocBits with the rule cards Table Extraction, AI Table extraction and Table extraction for costing element"><figcaption></figcaption></figure>

<mark style="color:red;">**Note:**</mark> To enable table extraction for **Costing Elements**, you must first import the relevant Costing Element table into **DocBits**. Without this configuration, users will encounter the following error when opening a document:

_**"Costing elements are not properly configured. Please ask your admin to configure it."**_

## Steps to Import Costing Elements from M3

1. **Access PPS280 in M3:**
   * From the M3 homepage, press `Command + R` and search for **PPS280**.
   * Select any/all lines from the results.
2. **Export the Data:**
   *   In the next menu, click **TOOLS → Export to Excel**.\\

       <figure><img src="../../../.gitbook/assets/image (431).png" alt="M3 PPS280 Costing Element screen with the Tools menu open listing Personalize, User Settings and Link Manager"><figcaption></figcaption></figure>
   *   Choose **Export All Rows**, then press **EXPORT**.

       <figure><img src="../../../.gitbook/assets/image (432).png" alt="Export to Excel dialog with the options Export currently selected rows, Export all rows, data format choices and the buttons Export to Excel and Cancel"><figcaption></figcaption></figure>
3. **Modify the Excel File:**\
   Open the downloaded Excel file and make the following changes:
   * **Rename columns:**
     * Column A → `costing_element`
     * Column B → `description`
     * Column H → `charge_operator`
     * Column J → `charge_type`
     * Column K → `distribution_method`
     * Column L → `distribution_type`
     * Column N → `charge_sequence_number`.
       * Enter the appropriate sequence numbers.
       * If left empty, the system will default to **10**.
   * **Remove all other columns** that are **not listed above**, even if they **contain data or are not empty**.
4. **Visual Example – Before and After:**\
   Below are examples of the Excel file _before_ and _after_ applying the required modifications:
   *   **Before Modification:**

       <figure><img src="../../../.gitbook/assets/image (106).png" alt="Excel sheet before modification with columns A to N starting with Elemnt Name and rows of costing element data"><figcaption></figcaption></figure>
   *   **After Modification:**

       <figure><img src="../../../.gitbook/assets/image (107).png" alt="Excel sheet after modification with the renamed columns costing_element, description, charge_operator, charge_type, distribution_method, distribution_type and charge_sequence_number"><figcaption></figcaption></figure>
5. **Convert to CSV:**
   * Save the modified Excel file as a `.csv`
6. **Upload to DocBits:**

* Go to **Settings → Document Processing → Master Data Lookup**
*   Click on the Plus next to imported

    <figure><img src="../../../.gitbook/assets/image (433).png" alt="Master Data Lookup page in DocBits with the tree Input data, ERP API Data, Imported and DocBits Master Data"><figcaption></figcaption></figure>
* Fill in the required informations
  * **Data Type**: `costing_element`
  * **File**: Select your modified `.csv` file
  * **Delimiter**: `comma`
  * **On Conflict**: Choose a conflict resolution strategy
  *   **Auto-generate ID**: Make sure this option is **checked**\\

      <figure><img src="../../../.gitbook/assets/image (434).png" alt="Upload CSV dialog with Data Type costing_element, the file Costing-Element_Modified.csv, Delimiter comma, On Conflict REPLACE and Auto Generate Id"><figcaption></figcaption></figure>
