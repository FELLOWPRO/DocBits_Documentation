---
hidden: true
noIndex: true
---

# M3\_OLD

## Importing an API Connection Template in Infor M3

This guide explains how to import an API Connection Template to quickly configure key settings for integration with Infor M3. Using a template allows you to establish a predefined connection setup, simplifying the process and ensuring consistency.

<mark style="color:red;">**Note**</mark>: For detailed configuration of specific areas such as Auto Accounting, Supplier Integration, Purchase Orders, or Table Extraction for costing elements, refer to the corresponding documentation:

* [Auto Accounting](m3/auto-accounting.md)
* [Suppliers and Purchase Order](m3/suppliers-and-purchase-orders.md)
* [How to import all suppliers](m3/how-to-import-all-suppliers.md)
* [Table Extraction for costing element](m3/table-extraction-for-costing-element.md)

### **Download the Template**

Before importing, download the required connection template using the file below:

{% file src="../../.gitbook/assets/DocBits-Dev-Import-Template (1).xml" %}

### Importing Template

#### Steps to Import a Connection Template

1. **Access Infor ION Desk:**
   *   Navigate to **InforOS** → **ION Desk** → **Connect** → **Connection Points**.

       ![](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH_r3RAGOvJE6Ok67ST_272zFfhB_TTFYg3b-NwFq0CAv2o)
2. **Import the Template:**
   *   Click on the **Import** button.

       <figure><img src="../../.gitbook/assets/m3_import_2.png" alt=""><figcaption></figcaption></figure>
   * Select the appropriate **Template File** from your local system.
   *   Click **OK** to begin the import process.

       <figure><img src="../../.gitbook/assets/m3_import_3.png" alt="" width="327"><figcaption></figcaption></figure>
3. **Confirmation:**
   *   If the import is successful, a confirmation message will be displayed.

       <figure><img src="../../.gitbook/assets/m3_import_4.png" alt=""><figcaption></figcaption></figure>
4. **Post-Import Configuration:**
   * After importing the template, you can customize specific connection settings as needed.
   * Don’t forget to import or configure your **Service Account** for authentication and access control.

<figure><img src="../../.gitbook/assets/m3_import_5.png" alt=""><figcaption></figcaption></figure>
