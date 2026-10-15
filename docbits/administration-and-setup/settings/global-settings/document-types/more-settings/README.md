# More Settings

## Overview

**More Settings** holds the options that belong to one document type, for example the Invoice. A setting that you switch on here applies only to that document type. The page is made of collapsible cards, one per topic. Open a card to see its settings.

<figure><img src="../../../../../.gitbook/assets/doc-type-settings-overview.png" alt="The cards of the More Settings page for the Invoice document type"><figcaption><p>The cards of the More Settings page, all collapsed.</p></figcaption></figure>

## How to Access

1. Navigate to **Settings** → **Global Settings** → **Document Types**.
2. Select the document type and click **More Settings**.

The breadcrumb at the top of the page shows **Settings / Document Types / More Settings**. The Settings Assistant on the right of the page explains the settings of the open card.

| Card | What you set there |
| ---- | ------------------ |
| [Purchase Order](#purchase-order) | PO matching, tolerances, export of PO lines, supplier item numbers |
| [Manage Layouts](#manage-layouts-custom-validation-rules-and-transformation-rules) | Switch for the Manage Layouts overview |
| [Custom Validation Rules](#manage-layouts-custom-validation-rules-and-transformation-rules) | Your own validation rules for this document type |
| [Transformation Rules](#manage-layouts-custom-validation-rules-and-transformation-rules) | Rules that read a value, change it in steps and write it back |
| [Approval & Rejection](#approval-and-rejection) | Approval workflow and the in-review and reject forms |
| Vertex Tax Verification | Design the form for the Vertex tax verification |
| [E-Invoice Validation](#e-invoice-validation) | Validation of XRechnung, ZUGFeRD and Factur-X invoices |
| [Table Extraction](#table-extraction) | Skip the validation of extracted tables |
| [Export Settings](#export-settings) | Multiple export, PDF format, alternate export |
| [Duplicate Detection](#duplicate-detection) | Detect and block duplicate documents |

## Purchase Order

The **Purchase Order** card (**PO Matching & Validation**) controls how documents of this type are matched with purchase orders.

<figure><img src="../../../../../.gitbook/assets/doc-type-settings-po-options.png" alt="The Purchase Order card with its switches"><figcaption><p>The Purchase Order card with its options.</p></figcaption></figure>

* [**Purchase Order**](purchase-order/purchase-order.md): Toggles whether the document is processed in the Purchase Order Matching screen. You can also specify which quantity the matching is based on.
* [**PO match server side**](purchase-order/purchase-order-matching-rules.md): Matches with the configurable rule set. **Configure PO Matching Rules** opens the [rules page](purchase-order/purchase-order-matching-rules.md).
* [**PO table in layout builder**](purchase-order/po-table-in-layout-builder.md): Enables the inclusion of purchase order tables in the layout builder for customized document layouts.
* [**Auto check for PO updates**](purchase-order/auto-check-for-po-updates.md): Shows a visual indicator in the Purchase Order Matching screen when a purchase order has been updated, prompting users to refresh.
* **Auto update PO data**: Updates the PO data automatically when new data is available. This switch belongs to **Auto check for PO updates**.
* [**Consumed PO line status**](purchase-order/consumed-po-line-status.md): Applies color coding to purchase order lines in the matching screen.
* [**Calculate PO unit price**](purchase-order/calculate-po-unit-price.md): Calculates the PO unit price using the net amount and quantity, instead of extracting it.
* [**Export not matched PO lines**](purchase-order/export-not-matched-po-lines.md): When off, only matched lines are exported. When on, all purchase order lines are exported, even if they are not matched.
* **Ignore Already Matched Lines**: Skips lines that have already been matched during a new matching process.
* [**Update Document Purchase Order Status**](purchase-order/update-document-purchase-order-status.md): Updates the PO Status column on the dashboard whenever the status of the purchase order changes.
* [**Allow Auto Export For Non Matchable PO Lines**, **Auto Match & Export visible to** and **Use Lines Net Amount for Matched Total visible to**](purchase-order/auto-match-and-export-options.md): Decide who sees the Auto Match & Export shortcuts and which documents may export automatically.

### PO Tolerance Setting

<figure><img src="../../../../../.gitbook/assets/doc-type-settings-po-tolerance.png" alt="The PO Tolerance Setting block with quantity and unit price tolerance"><figcaption><p>Tolerance for quantity and unit price.</p></figcaption></figure>

[**PO Tolerance Setting**](purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md) lets you set tolerance levels for quantity and unit price, so that minor discrepancies are not flagged as mismatches. For each value you choose the amount and the unit, either an absolute **Value** or a percentage (**%**). The block also contains [**Additional PO Tolerance Setting**](purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md#setting-to-configure-additional-purchase-order-tolerance-settings) for freight, charges and taxes, and [**PO disable statuses**](purchase-order/purchase-order-disable-statuses.md).

{% hint style="info" %}
When the document type attribute `CUSTOM_RANGE_FOR_PO_TOLERANCE` is on, the unit price and quantity tolerances come from these document type settings and not from the rule set. The rule diagram on the [PO matching rules page](purchase-order/purchase-order-matching-rules.md) shows a note when this is the case.
{% endhint %}

### Supplier Item Number Map

<figure><img src="../../../../../.gitbook/assets/doc-type-settings-po-supplier-item-map.png" alt="The Supplier Item Number Map table"><figcaption><p>The Supplier Item Number Map.</p></figcaption></figure>

The [**Supplier Item Number Map**](purchase-order/supplier-item-number-map-admin-documentation.md) maps supplier item numbers to your internal item numbers, so that lines match even when the supplier uses its own numbers. Search by column to find an entry.

## Manage Layouts, Custom Validation Rules and Transformation Rules

Three cards sit directly below the Purchase Order card:

* **Manage Layouts** switches the Manage Layouts overview on for this document type. See the [Layout Manager](../layout-manager/README.md).
* **Custom Validation Rules** switches your own validation rules on. **Manage Validation Rules** opens them. See [Custom Validation Rules](../custom-validation-rules.md).
* **Transformation Rules** switches the transformation rules on. **Manage Transformation Rules** opens them. See [Transformation Rules](../transformation-rules.md).

<figure><img src="../../../../../.gitbook/assets/doc-type-settings-rule-toggles.png" alt="The Manage Layouts, Custom Validation Rules and Transformation Rules cards"><figcaption><p>The three cards with their switches.</p></figcaption></figure>

## Approval and Rejection

The **Approval & Rejection** card holds the approval workflow and the forms that users see while they review or reject a document.

<figure><img src="../../../../../.gitbook/assets/doc-type-settings-approval.png" alt="The Approval and Rejection card"><figcaption><p>The Approval &#x26; Rejection card.</p></figcaption></figure>

* **Approve before export**: Documents must be approved before they can be exported. **Design Approval Form** opens the **Layout Builder** for the approval screen.
* **Approve before export V2**: Activates Approval V2, which supports dynamic fields in place of static ones.
* **Second Approval**: Adds an additional layer of approval.
* [**Approval Stamp**](approval/approval-stamp.md): Adds a stamp to the document when it is approved.
* [**Approval History**](approval/approval-history.md): Shows the approval history in the approval screen and in field validation.
* **Design In Review Form**: Configures the layout of the review form with the **Layout Builder**.
* **Design Reject Form**: Configures the layout of the reject form with the **Layout Builder**.

For the **Layout Builder** see the [Layout Manager](../layout-manager/README.md).

## E-Invoice Validation

The **E-Invoice Validation** card switches the validation of incoming e-invoices on and lets you decide whether the supplier is notified when an invoice is rejected. See [E-Invoice Validation](../../../document-processing/e-documents/validation-rules.md).

## Table Extraction

<figure><img src="../../../../../.gitbook/assets/doc-type-settings-table-extraction.png" alt="The Table Extraction card"><figcaption><p>The Table Extraction card.</p></figcaption></figure>

* **Skip table validation**: Bypasses the standard validation of table data. Use it when flexible data handling is required or when certain validation steps can be skipped to improve performance.

## Export Settings

<figure><img src="../../../../../.gitbook/assets/doc-type-settings-export-settings.png" alt="The Export Settings card"><figcaption><p>The Export Settings card.</p></figcaption></figure>

* **Multiple Export**: Allows a document to be exported more than once.
* **Export PDF Format**: **Export File Format** sets the PDF format that is used when documents are exported, for example **Original Document**.
* [**Alternate Export**](purchase-order/alternate-export.md): Sets up an alternative export for a chosen document status. Pick the **Status** and the **Export Configuration** that runs for it, then switch the setting on.

## Duplicate Detection

<figure><img src="../../../../../.gitbook/assets/doc-type-settings-duplicate-detection.png" alt="The Duplicate Detection card"><figcaption><p>The Duplicate Detection card.</p></figcaption></figure>

The card contains **Duplicate Document Detection** with the fields that decide what counts as a duplicate and the interval in which documents are compared, plus the options **Duplicate Invoice Detection**, **Block Duplicate Document Export** and **Ignore Tax Free Line**. All three carry a **Recommended** label. See [Duplicate Detection](duplicate-document-handling.md) for how a flagged document is handled.
