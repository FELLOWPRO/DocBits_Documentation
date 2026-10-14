# More Settings

## Overview

In the "More Settings" section, you can find various options related to individual document types. Once a setting is activated, it will apply only to that specific document type. This page provides a brief overview of what each setting does.

## How to Access

1.  Navigate to **Settings** → **Global Settings** → **Document Types**.

    <figure><img src="../../../../../.gitbook/assets/disablpe_po_status_1.png" alt=""><figcaption></figcaption></figure>
2.  Select the desired document type and click on **More Settings**.

    <figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_2.png" alt=""><figcaption></figcaption></figure>

## Table Extraction

* **Skip table validation**: Enables bypassing the standard validation process for table data. This option is useful in scenarios where flexible data handling is required or when certain validation steps can be skipped to improve performance during data processing.

## Duplicate Detection

* [**Duplicate Document Detection**](duplicate-document-handling.md): This allows you to detect and handle duplicate documents.

## In Review

* **Design in Review Form**: Configure the layout of review forms using the **Layout Builder**. This layout determines how content is presented during the document review process. For detailed instructions on how to use the **Layout Builder**, click [here](../../../../setup/document-types/layout-builder.md).

## Reject

* **Design Reject Form**: Configure the layout using the **Layout Builder** for the reject form displayed during the document review process. For detailed instructions on how to use the **Layout Builder**, click [here](../../../../setup/document-types/layout-builder.md).

## Export PDF Format

* **Export File Format**: Allows you to specify the PDF format to be used when exporting documents.

## Approval

* **Approve before export**: Ensures that documents must be approved before they can be exported from the system. You can also configure the layout of the approval screen using the **Layout Builder**. For detailed instructions on how to use the **Layout Builder**, click [here](../../../../setup/document-types/layout-builder.md).
* **Approve before export V2**: Activates Approval V2, which supports the use of dynamic fields in place of static ones. You can also customize the layout of the approval screen using the **Layout Builder**. For detailed instructions on how to use the **Layout Builder**, click [here](../../../../setup/document-types/layout-builder.md).
* **Second Approval**: Adds an additional layer of approval for enhanced validation and greater control over document processing. You can also customize the layout of the approval screen using the **Layout Builder**. For detailed instructions on how to use the **Layout Builder**, click [here](../../../../setup/document-types/layout-builder.md).
* [**Approval Stamp**](approval/approval-stamp.md): Adds a stamp to the document when it is approved.
* [**Approval History**](approval/approval-history.md): Enables the display of approval history in both the approval screen and field validation.

## Purchase Order

* [**PO table in layout builder**](purchase-order/po-table-in-layout-builder.md): Enables the inclusion of purchase order tables in the layout builder for customized document layouts.
* [**Auto check for PO updates**](purchase-order/auto-check-for-po-updates.md): When enabled, the system displays a visual indicator in the Purchase Order Matching screen to show when a purchase order has been updated, prompting users to refresh for the latest information.
* **Auto update PO data**: Activating this will automatically update the PO data when new data is available.
* [**Consumed PO line status**](purchase-order/consumed-po-line-status.md): This setting enhances the Purchase Order Matching screen by applying color coding to purchase order lines.
* [**Calculate PO unit price**](purchase-order/calculate-po-unit-price.md): This lets you calculate the PO unit price using the net amount and quantity, instead of extracting it.
* [**Purchase Order**](purchase-order/purchase-order.md): Toggles whether the document should be processed in the Purchase Order Matching screen. You can also specify which quantity term the matching process should be based on.
* [**Export not matched PO lines**](purchase-order/export-not-matched-po-lines.md): This feature controls the export of purchase order lines. When disabled, only matched lines are exported. When enabled, all purchase order lines are exported, even if they are not matched to an order confirmation line.
* [**PO Tolerance Setting**](purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md): This feature lets you set tolerance levels for quantity and unit price, accommodating minor discrepancies without flagging them as mismatches.
* [**Additional PO Tolerance Setting**](purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md#setting-to-configure-additional-purchase-order-tolerance-settings): This feature lets you set additional tolerance levels for freight, charges, and taxes, accommodating minor discrepancies without flagging them as mismatches.
* [**Alternate Export**](purchase-order/alternate-export.md): This allows you to set up an alternative export for specific statuses.
* [**PO disable statuses**](purchase-order/purchase-order-disable-statuses.md): Allows you to disable specific statuses from being considered in the matching process.
* **Ignore Already Matched Lines**: Activating this will skip lines that have already been matched during a new matching process.
* [**Update Document Purchase Order Status**](purchase-order/update-document-purchase-order-status.md): When enabled, the PO Status column on the dashboard is automatically updated whenever the status of the purchase order changes.
* [**Supplier Item Number Map**](purchase-order/supplier-item-number-map-admin-documentation.md): A utility setting that maps supplier item numbers to internal item numbers, ensuring accuracy in inventory and purchase order management.
