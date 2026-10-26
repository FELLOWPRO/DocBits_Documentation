# PO Table in Layout Builder

This setting controls the accessibility of the **Purchase Order (PO) table** in the **Layout Builder** and the **Validation Screen**.

### **How to Enable the PO Table**

To enable this feature:

1. Go to **Settings → General Settings → Document Types → More Settings → Purchase Order Section → PO Table in Layout Builder**.
2. Enable the setting to make the **Purchase Order table** visible.

<figure><img src="../../../../../../.gitbook/assets/iScreen Shoter - Google Chrome - 250210131953.jpg" alt=""><figcaption></figcaption></figure>

### **Functionality:**

* **When enabled**:
  * The **Purchase Order table** appears inside the **Table Section** in the **Layout Builder**.
  *   No notification about the module being disabled will be shown.\


      <figure><img src="../../../../../../.gitbook/assets/image (404).png" alt=""><figcaption></figcaption></figure>
* **When disabled**:
  * A hint will indicate that the module is disabled.
  *   The **PO table** will not be visible in the **Validation Screen**.\


      <figure><img src="../../../../../../.gitbook/assets/image (403).png" alt=""><figcaption></figcaption></figure>

**How to Access the Layout Builder**

1. Navigate to **Settings → General Settings → Document Types → Edit Layout**.

<figure><img src="../../../../../../.gitbook/assets/iScreen Shoter - Google Chrome - 250210135142.jpg" alt=""><figcaption></figcaption></figure>

**Adding the PO Table Back to the Layout**

If the **PO table** is missing or has been removed, follow these steps:

1. Open the **Layout Builder**.
2. Under **Form Elements**, select **Extracted Tables**.
3. Add the **PO table** to your layout.

<div align="left"><figure><img src="../../../../../../.gitbook/assets/iScreen Shoter - Google Chrome - 250210135437.jpg" alt=""><figcaption></figcaption></figure></div>

Once added and enabled, the **PO table** will be visible in the **Layout Builder** and the **Validation Screen** when a **purchase order** is available for an invoice.

<div align="center"><figure><img src="../../../../../../.gitbook/assets/iScreen Shoter - Google Chrome - 250210133655.jpg" alt=""><figcaption></figcaption></figure></div>

## Display per-item charge price in approval layouts

Approval layouts (for example the Pending Approval layout of an Order Confirmation) have one more option on the **PO Tables** element: **Display per-item charge price**.

You find it in the **Layout Builder**: select the **PO Tables** element on the canvas and open the element's properties on the right.

* **On**, or not set at all: a costing element shows the per-item price and the total effective cost, for example `181.8182 (200.00)`.
* **Off**: a costing element shows only the total effective cost, for example `200.00`.
* Tax costing elements keep showing their tax rate in both cases.

The option only changes the display. The stored value stays the per-item price, because approving the document saves it as the approved unit price.

The checkbox is only offered on approval layouts. Validation layouts have no charge comparison table, so the option does not appear there. Existing approval layouts keep the current display until you clear the checkbox.
