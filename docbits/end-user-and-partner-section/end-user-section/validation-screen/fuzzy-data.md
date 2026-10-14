# Fuzzy Data

### **Overview**

Fuzzy Data fields allow users to populate related fields based on approximate matches from master data. These fields are identified by a **blue icon** next to them.

<figure><img src="../../../.gitbook/assets/fuzzy_data_field_icon.png" alt="Fuzzy Data Field Icon"><figcaption></figcaption></figure>

### **Functionality**

#### **What Do Fuzzy Data Fields Do?**

* They populate related fields based on their value or input.
* The three standard fields using Fuzzy Data are:
  * **Purchase Order**
  * **Supplier**
  * **Vendor ID**

#### **Using Fuzzy Data Fields**

1. **Selecting a Purchase Order**
   *   Clicking the **blue icon** next to the Purchase Order field opens a **selection window**.


       <figure><img src="../../../.gitbook/assets/fuzzy_data_selection_window.png" alt="Fuzzy Data Selection Window"><figcaption></figcaption></figure>
   * This window contains a table with all purchase orders from the **master data lookup table**.
   * Enabling the **"Display all columns"** option shows additional details.
   * Select a **Purchase Order** and click **Proceed**:
     * If the system finds a Purchase Order in the document, it filters for it automatically.
     * If no match is found, you can **create custom filters** to find the correct Purchase Order.
     * Multiple filters can be added; enabling **"Match all filters"** ensures that all conditions must be met.
     * Available filter options:
       * **Smart**
       * **Contains**
       * **Exact**
       * **Starts with**
       * **Ends with**
   * A button next to **Proceed** allows users to **create a new task/notification**.
2. **Selecting a Supplier or Vendor ID**
   * The process is the same as for Purchase Orders.
   * The difference is that **Supplier and Vendor ID fields use the Supplier Master Data Table** instead of the Purchase Order Header Master Data Table.

#### **Field Population Hint**

* If a field is populated using Fuzzy Data rather than being extracted from the document, a **small hint or info icon** appears to indicate that the data was **not extracted from the document** but filled based on master data.

### **Administrator Configuration**

{% content-ref url="../../../administration-and-setup/setup/document-types/fuzzy-data-configuration-with-master-data.md" %}
[fuzzy-data-configuration-with-master-data.md](../../../administration-and-setup/setup/document-types/fuzzy-data-configuration-with-master-data.md)
{% endcontent-ref %}

{% content-ref url="../../../administration-and-setup/setup/document-types/fuzzy-data-configuration-with-list-of-values.md" %}
[fuzzy-data-configuration-with-list-of-values.md](../../../administration-and-setup/setup/document-types/fuzzy-data-configuration-with-list-of-values.md)
{% endcontent-ref %}



{% embed url="https://www.youtube.com/watch?v=vT5HuGjAYV0" %}