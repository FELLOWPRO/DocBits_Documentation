# PO Shipment Order Setting

## **Overview**

The **PO Shipment Order** section provides a breakdown of delivery and invoicing status for matched Purchase Order items. This section appears within the **Purchase Order Matching** screen when the feature is enabled.

## **How to Enable**

To activate this feature:

1. Go to **Settings** → **Module**.
2. Open the **Purchase Order** section (*PO Matching & Validation*).
3.  Enable the **PO Shipment Order** option.\
    \


    <div align="left"><figure><img src="../../../../.gitbook/assets/po-shipment-order-module-setting.png" alt="Purchase Order section in Settings → Module with the PO Shipment Order switch" width="563"><figcaption><p>Settings → Module → Purchase Order</p></figcaption></figure></div>

The same section holds two related switches: **PO dashboard** adds a Purchase Order dashboard to the navigation, and **Shipment Order Dashboard** adds a Shipment Order dashboard that lists incoming deliveries per Purchase Order item.

## **Where It Appears**

Once enabled, the PO Shipment Order section becomes visible in the Purchase Order Matching interface.

<figure><img src="../../../../.gitbook/assets/PO-Shipment-Order-1.jpg" alt="PO Shipment Order section in the Purchase Order Matching screen"><figcaption></figcaption></figure>

### **PO Shipment Order – Field Descriptions**

* **Item ID**\
  Identifies the specific item in the purchase order.
* **Delivery Number**\
  Reference number for the shipment or delivery.
* **Shipped Quantity**\
  Quantity that has been delivered or received.
* **Invoiced Quantity**\
  Quantity that has already been invoiced.
* **Invoice Open Quantity**\
  Quantity still open for invoicing (calculated as _Shipped Quantity – Invoiced Quantity_).
* **Progress Bar and Percentage**
  * Shows how much of the shipped quantity has been matched with invoices.
  * Starts at 0% for new POs.
  * Updates cumulatively across multiple invoices.
  * Reflects total progress of invoiced vs. shipped items.
* **Promised Delivery Date**\
  The expected delivery date for the PO item.
*   **Late Indicator**

    Displays the number of days the delivery is late based on the **Promised Delivery Date**.
