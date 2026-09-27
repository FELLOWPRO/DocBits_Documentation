# Purchase order disable statuses

## **Overview**

The **PO Disable Statuses** setting allows users to specify purchase order (PO) statuses that prevent invoices from being matched to those POs. If a purchase order has a status listed in this setting, it **cannot** be used for invoice matching in the PO matching screen, stopping further processing of related invoices until the PO's status changes to one that is not disabled.\
\
By using this setting, users can ensure that purchase orders with specific statuses do not undergo further invoice processing, reducing errors and preventing unnecessary payments.

## **Activation Steps**

1.  Go to **Settings → Global Settings → Document Types**

    <figure><img src="../../../../../../.gitbook/assets/disablpe_po_status_1.png" alt=""><figcaption></figcaption></figure>
2.  Select the desired document type and click on **More Settings**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_2.png" alt=""><figcaption></figcaption></figure>
3.  In the **Purchase Order** section, navigate to the **PO Disable Statuses** option.

    <figure><img src="../../../../../../.gitbook/assets/disable_po_status_3.png" alt=""><figcaption></figcaption></figure>

### **How to Identify a Disabled Purchase Order**

In the **PO Matching** screen, a disabled purchase order appears **crossed out**. This visually indicates that the PO is currently restricted from being matched due to its status.

<figure><img src="../../../../../../.gitbook/assets/image (390).png" alt=""><figcaption></figcaption></figure>

### **How to set it up**

1. In the **PO Disable Statuses** setting, you will see a selection field on the left side.
2.  Clicking this field opens a dropdown list of available PO statuses.\\

    <div align="center"><figure><img src="../../../../../../.gitbook/assets/image (388).png" alt="" width="372"><figcaption></figcaption></figure></div>
3. Select one or more statuses by clicking on them. Click again to deselect.
4.  Click the **Apply** button to save your changes.

    <figure><img src="../../../../../../.gitbook/assets/disable_po_status_5.png" alt=""><figcaption></figcaption></figure>

**Available Statuses**

* Canceled
* Deleted
* Invoiced
* Open
* Partially Invoiced
* Partially Received
* Received
* Rejected
* Unapproved
* Hold
* Closed
