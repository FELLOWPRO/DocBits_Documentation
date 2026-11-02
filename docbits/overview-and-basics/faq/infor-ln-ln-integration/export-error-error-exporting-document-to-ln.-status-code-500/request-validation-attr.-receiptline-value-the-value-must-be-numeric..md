# Request validation; Attr. 'ReceiptLine', Value " " : the value must be numeric.

## **Step 1: Investigate the Purchase Order**

**1. Check the Purchase Order from the Dashboard**

* If the document status is **Export Error**:
  1. Locate the document on the dashboard.
  2. Click on it and then select the **Fields Validation** button to navigate back to the field validation screen.
* If the document status is **Ready for Validation**:
  1. Click on the document to proceed directly to the **Field Validation** screen.
* If the document is in **Pending Approval status**:
  1. Navigate to the **Approval Screen**.
  2. Next to the **Invoice Line Items**, locate the **Purchase Order Table.**
  3. Go to 3. Check for the Delivery Number step.

**2. Verify the Purchase Order**

1. On the **Field Validation** screen, ensure the correct Purchase Order is selected.
2. Once the correct Purchase Order is confirmed, click on the Purchase Order next to the extracted table, to open the **Purchase Order Table** view.

**3. Check for the Delivery Number**

* In the Purchase Order Table, look for the **Delivery Number** column:
  * **If a Delivery Number is present**, proceed to the **Approval Screen** and check again if it is present, when present go to **Step 3**.
  * **If no Delivery Number is present**, follow **Step 2** to address this issue.

## Step 2: Verify the Purchase Order in LN

Before sending the Purchase Order to DocBits, verify that the **Delivery Number** is correctly assigned in **LN**. Check the **Purchase Order** details in **LN** to ensure that it is complete and accurate. If the **Delivery Number** is missing or incorrect, this could be the cause of the export error.

If the **Purchase Order** appears correct and contains the necessary details, you can proceed to the next step.

## **Step 3: Open DocBits Settings**

1. Open **DocBits** and go to the **Settings** section.
2. Navigate to **Document Processing**.
3. Select **Export**.
4. In the **Export** section, click on the **three dots** icon next to the export that is not working and select **Edit**.
5. In the **Edit Export Settings** menu, click **Download the LN-Mapping** file.

## **Step 3: Edit LN-Mapping File**

1. Open the downloaded **LN-Mapping** file.
2. Search for the field **IRF\_ReceiptLine**.
   * If the field **IRF\_ReceiptLine** is present and set to **nothing** (empty), update it to **TF\_delivery\_line**.
   * If the field **IRF\_ReceiptLine** is **not present**, add it to the file and set its value to **TF\_delivery\_line**.
3. For the field **InvoiceReceiptFields,** add **ReceiptLine** to the values.

It should look like the following:

<figure><img src="../../../../.gitbook/assets/image (117).png" alt="Mapping file excerpt with InvoiceReceiptFields and IRF_ entries, with the ReceiptLine field mapped to TF_delivery_line highlighted" width="563"><figcaption></figcaption></figure>

## **Step 4: Add the Updated File Back to DocBits**

1. Go back to the **Export** section in DocBits where you previously downloaded the **LN-Mapping** file.
2. Upload the edited **LN-Mapping** file with the new updates.

## Step 5: Retry the Export

After confirming that the **Purchase Order** has a **Delivery Number** and ensuring the **Export file is correct**, follow these steps to retry the export:

1. **Return to the Dashboard:**
   * Go back to the dashboard and find the document with the export error.
2. **Retry the Export Process:**
   * Click on the document with the export error.
   * If the **Purchase Order** has a valid **Delivery Number** and the **Export file** is correct, proceed to retry the export.
3. **Check the Export Result:**
   * After retrying, check the export process again to see if the issue has been resolved and the document no longer shows as an export error.
   * If the export is successful, the issue should be resolved.
4. **Further Investigation (if the problem persists):**
   * If the issue persists after retrying the export, contact support for further investigation into possible configuration or system issues.
