# Table Extraction for costing Element

Navigate to **Settings → Document Processing → Classification and Extraction**

<figure><img src="../../../.gitbook/assets/image (430).png" alt="Classification and Extraction settings with the Table extraction for costing element toggle enabled and highlighted by an arrow"><figcaption></figcaption></figure>

<mark style="color:red;">**Note:**</mark> To enable table extraction for **Costing Elements**, you must first import the relevant Costing Element table into **DocBits**. Without this configuration, users will encounter the following error when opening a document:

_**"Costing elements are not properly configured. Please ask your admin to configure it."**_

## Steps to Import Costing Elements from M3

1. **Access PPS280 in M3:**
   * From the M3 homepage, press `Command + R` and search for **PPS280**.
   * Select any/all lines from the results.
2. **Export the Data:**
   *   In the next menu, click **TOOLS → Export to Excel**.\\

       <figure><img src="../../../.gitbook/assets/image (431).png" alt="M3 PPS280 Costing Element page with the Tools menu open and Export to Excel highlighted"><figcaption></figcaption></figure>
   *   Choose **Export All Rows**, then press **EXPORT**.

       <figure><img src="../../../.gitbook/assets/image (432).png" alt="M3 Export to Excel dialog with Export all rows and Source Format selected and the Export to Excel button highlighted"><figcaption></figcaption></figure>
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

       <figure><img src="../../../.gitbook/assets/image (106).png" alt="Exported M3 costing element spreadsheet with original columns such as Elemnt, Name, Fld 1 to Fld 5, Ope, Ctp, Dmt, Dut and Inv"><figcaption></figcaption></figure>
   *   **After Modification:**

       <figure><img src="../../../.gitbook/assets/image (107).png" alt="Modified costing element spreadsheet with columns costing_element, description, charge_operator, charge_type, distribution_method, distribution_type"><figcaption></figcaption></figure>
5. **Convert to CSV:**
   * Save the modified Excel file as a `.csv`
6. **Upload to DocBits:**

* Go to **Settings → Document Processing → Master Data Lookup**
*   Click on the Plus next to imported

    <figure><img src="../../../.gitbook/assets/image (433).png" alt="Master Data Validation settings with the plus icon next to Imported highlighted by an arrow"><figcaption></figcaption></figure>
* Fill in the required informations
  * **Data Type**: `costing_element`
  * **File**: Select your modified `.csv` file
  * **Delimiter**: `comma`
  * **On Conflict**: Choose a conflict resolution strategy
  *   **Auto-generate ID**: Make sure this option is **checked**\\

      <figure><img src="../../../.gitbook/assets/image (434).png" alt="Upload CSV dialog with data type costing_element, a CSV file, comma delimiter, On Conflict REPLACE and Auto Generate Id checked"><figcaption></figcaption></figure>
