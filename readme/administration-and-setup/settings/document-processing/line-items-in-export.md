# Line Items in Export

What happens to the line-item table when a document is approved and exported depends on the export method. This page explains which columns leave DocBits, which ones are mandatory, and why an export can show fewer lines than the validation screen.

## Two kinds of export

| Export method | What is sent for the table |
|---|---|
| **webhook**, **watcher**, **sftp**, **infor_sftp** (JSON / XML) | The table as it is on the validation screen: every non-hidden [table column](../global-settings/document-types/table-columns/README.md) of every row, with value, formatted value and confidence. |
| **infor-m3-cloud**, **infor-m3-toml-cloud**, **infor-idm-***, **infor-gls840-onpremise**, **infor-m3-oc-charges-onpremise** (Infor ERP / SAP BODs) | Not the raw table. DocBits builds **receipt lines** and **cost lines** from it (see below) and maps them onto the BOD fields with the mapping configured under [Exporting to Infor](../../../infor-integration-and-configuration/exporting-to-infor/README.md). |

## Receipt lines and cost lines (Infor exports)

An ERP invoice line is either a **receipt line**, it settles a purchase-order receipt, or a **cost line**, it books an amount to a ledger account with dimensions. DocBits decides per invoice line:

* **Receipt lines** come from **PO matching**. Every invoice line that was matched to a PO line (Dashboard → PO Match, or automatically with *PO auto match*) becomes a receipt line carrying the PO number, PO line, receipt line and the matched quantity and amount. An invoice with no PO match has **no receipt lines**, the export preview then shows `receipt_lines: []`, which is correct, not a bug.
* **Cost lines** come from the **accounting record** that the cost-accounting step (or Auto Accounting) creates: ledger account, dimensions, amount, quantity per line. An invoice without an accounting record has no cost lines.
* **Tax lines** are built from the header tax amounts, not from the table.

So for Infor exports, the line-item table is the *input* to PO matching and accounting; what the ERP receives is the result of those two steps. A line that is neither PO-matched nor accounted does not reach the ERP.

{% hint style="warning" %}
For PO matching to work, the table must have the default columns **item number, unit price, quantity and total amount**. If one of them is hidden, the validation screen shows *Line Item Table is missing Mandatory column for PO* and no receipt lines can be built.
{% endhint %}

## Mandatory columns and the approval dialog

Before a document can be approved, DocBits checks the table:

1. Every column marked **Is Required** (Settings → Document Types → Table Columns) must have a value in every row.
2. Every row must pass the **line-total check**: `total = quantity × unit price + charges − discount` within 0.02. Failing rows are marked; the message names the expected and the actual value.
3. The **sum of the line totals** is compared with the net amount in the header. A difference is a warning and does not block approval.

The approval dialog lists what is still missing. An admin can switch every table check off per document type with **Skip table validation** (Document Types → More Settings), line totals and required columns are then no longer checked; the header checks stay.

Details of the messages: [Table Extraction Troubleshoot](../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md#messages-on-the-table).

## Empty table

* **JSON / XML exports** send the document with `tables: []` (or the table with zero rows). The receiving system must handle an empty table.
* **Infor exports** with no receipt lines and no cost lines send only the header and tax lines. Most ERPs reject an invoice without lines, configure Auto Accounting or a default cost line for such document types, or route them to a different export.
* A document type **without a table** (no table configured) never sends line data; that is expected for document types such as order confirmations that are matched at header level.

## Checking before you approve

Partners and support with API or MCP access can request the export payload for a document before it is sent: the MCP tool `get_export_preview(doc_id)` returns exactly what the export will send, `receipt_lines`, `cost_lines` and `tax_lines` for Infor exports, `tables` for JSON exports. Use it when the ERP reports missing lines: if `receipt_lines` is empty, the invoice was not PO-matched; if `cost_lines` is empty, no accounting record exists.

## Related pages

* [Export](export.md): export configurations and methods
* [Table Columns](../global-settings/document-types/table-columns/README.md)
* [Exporting to Infor](../../../infor-integration-and-configuration/exporting-to-infor/README.md): BOD field mappings for receipt, cost and tax lines
