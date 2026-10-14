# Purchase order tolerance settings / Additional purchase order tolerance

## **Setting to configure Purchase Order Tolerances**

Go to **Settings → General Settings → Document Types → More Settings → Purchase Order Section → PO Tolerance Setting**

### **How It Works**

When enabled, this setting allows you to define tolerances for **Quantity** and/or **Unit Price**. These tolerances can be set either as a percentage or as a fixed value. This means that an invoice can deviate from the purchase order (PO) within the specified tolerance range without being flagged as a mismatch, providing flexibility while ensuring seamless processing.

<mark style="color:red;">**NOTE**</mark>**:** Tolerances work in both directions; that is, the invoice value may be either higher or lower than the PO value within the allowed range.

### **Setting It Up**

1. **Enable the Setting:**
   * Turn on the PO Tolerance Setting using the toggle button.
2. **Configure Tolerances:**
   * Four fields will appear:
     * One field for the **Quantity Tolerance Amount**.
     * One field for the **Unit Price Tolerance Amount**.
   * Behind each field, there is a dropdown menu where you can select the tolerance type:
     * **Percent:** Indicates a percentage tolerance.
     * **Value:** Indicates a fixed amount by which the value can differ.

<figure><img src="../../../../../../.gitbook/assets/image (407).png" alt=""><figcaption></figcaption></figure>

### **Example Scenario:**

* Suppose the **Unit Price Tolerance** is set to **5%**.
* The purchase order includes two lines:
  * **Line 1:** Unit Price = **$5.00**
  * **Line 2:** Unit Price = **$2.00**
* On the invoice:
  * **Line 1:** The unit price is adjusted to **$4.80** (**within** the 5% tolerance).
  * **Line 2:** The unit price is adjusted to **$2.20** (**outside** the 5% tolerance).
* **Outcome:**
  * Line 1 is **not flagged** as a mismatch because $4.80 is within 5% of $5.00.
  * Line 2 **is flagged** as a mismatch because $2.20 exceeds the allowed 5% deviation from $2.00. The user is now required to take action to resolve the mismatch before the invoice can be processed further.

<figure><img src="../../../../../../.gitbook/assets/image (408).png" alt=""><figcaption></figcaption></figure>

## Setting to configure Additional Purchase Order Tolerance Settings

Go to **Settings → General Settings → Document Types → More Settings → Purchase Order Section → Additional PO Tolerance Setting**

### **How It Works**

When enabled, this setting allows you to define tolerances for **Freight**, **Charges**, and/or **Tax**. These tolerances can be set either as a percentage or as a fixed value, enabling invoices to vary slightly from the PO values without being flagged as mismatches. This provides additional flexibility and ensures that minor differences do not interrupt the workflow.

<mark style="color:red;">**NOTE**</mark>**:** Just like the standard tolerance settings, these tolerances apply in both directions—allowing for increases or decreases within the set limits.

### **Setting It Up**

1. **Enable the Setting:**
   * Turn on the Additional PO Tolerance Setting using the toggle button.
2. **Configure Tolerances:**
   * Six fields will become visible:
     * One field each for the tolerance amounts for **Freight**, **Charges**, and **Tax**.
   * Each field has an accompanying dropdown menu where you can choose the tolerance type:
     * **Percent:** The tolerance is defined as a percentage.
     * **Value:** The tolerance is defined as a fixed amount.

<figure><img src="../../../../../../.gitbook/assets/image (409).png" alt=""><figcaption></figcaption></figure>
