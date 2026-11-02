# Purchase order disable statuses

## **Overview**

The **PO disable statuses** setting specifies which purchase order (PO) line statuses are restricted in the matching screen. A line with a configured disabled status is shown with strikethrough and is not draggable for a match. Use the setting to control matching eligibility for the relevant document type.

## **Activation Steps**

1. Open **Settings → Document Types**.
2. Find the document type you want to configure. The example below uses **Invoice**. Open its gear button (**More settings**).

<figure><img src="../../../../../../.gitbook/assets/po-disable-statuses-invoice-card-native-en-20261102.png" alt="Current English Invoice standard document-type card header with Activate and Extraction controls and the More settings gear"><figcaption><p>The existing Invoice card and its More settings gear. The Activate and Extraction controls are separate from the PO status selection.</p></figcaption></figure>

3. Open the **Purchase Order** accordion and locate **PO disable statuses**.

<figure><img src="../../../../../../.gitbook/assets/po-disable-statuses-field-native-en-20261102.png" alt="Current English PO disable statuses field with its dropdown arrow and Apply button"><figcaption><p>The PO disable statuses field and its Apply button. The empty selection shown here is an example of the existing test configuration.</p></figcaption></figure>

### **How to Identify a Disabled Purchase Order**

In the [Purchase Order Matching Screen](https://docs.docbits.com/end-user-and-partner-section/end-user-section/purchase-order-matching), a line whose status is disabled is marked with strikethrough and cannot be dragged into a match. Check the line's status and the disabled-status list for the document type when reviewing why the line is unavailable.

<figure><img src="../../../../../../.gitbook/assets/po-disabled-row-historical-values-masked-20261102.png" alt="Redacted historical PO matching row with Canceled status; record-specific numeric values are masked"><figcaption><p>A retained historical PO matching example with Canceled status. Record identifiers, quantities, prices and matched values are masked for privacy.</p></figcaption></figure>

### **How to set it up**

1. Click the **PO disable statuses** field to open the available statuses.
2. Select the checkboxes for the statuses your process excludes from matching. Clear a checkbox to remove that status from the selection.

<figure><img src="../../../../../../.gitbook/assets/po-disable-statuses-options-native-en-20261102.png" alt="Current English PO disable statuses dropdown with all eleven status checkboxes and the Apply button; surrounding page content is masked"><figcaption><p>The current status options with their existing unchecked state. The surrounding page content is masked; the dropdown and Apply button are unchanged.</p></figcaption></figure>

3. Click **Apply** to save the selection for this document type. Opening the dropdown alone does not save a change.

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
