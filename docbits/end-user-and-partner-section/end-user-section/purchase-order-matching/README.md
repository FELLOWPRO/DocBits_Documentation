# Purchase Order Matching Screen

Use **PO Matching** to compare the purchase order lines loaded for a document with its extracted invoice lines. The purchase order data may come from an ERP integration or another configured import. The screen shows the document alongside the two tables so you can check numbers, quantities, prices, and differences before saving or exporting.

## Match invoice lines to a purchase order

The walkthrough starts with a recognized purchase order number and three matched invoice lines. It then shows manual search as an exception, an intentional wrong connection, a partial match, automatic matching and saving. Check the result after reloading; saving a match does not itself approve or export the invoice.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/po-matching-customer/v4/en.mp4" %}

[Watch the video with subtitles](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/po-matching-customer/v4/en.html)

{% hint style="info" %}
The recording uses synthetic test data with three extracted invoice lines and their purchase order. Paper, archive boxes and delivery total EUR 118 net. The full match shows EUR 118 matched and nothing open.
{% endhint %}

<figure><img src="../../../.gitbook/assets/po-tutorial-v4-full-en.png" alt="Full match: all three invoice lines are connected, with EUR 118 matched and EUR 0 open."><figcaption><p>Full match: all three invoice lines are connected, with EUR 118 matched and EUR 0 open.</p></figcaption></figure>

## Find and inspect a purchase order

1. Open the invoice in **PO Matching**. When its purchase order number is recognized, DocBits loads the corresponding order. Use manual search when the number is missing or you need to inspect another order.
2. Select the filter icon beside the search box for **Keyword**, **Supplier**, **Status**, **Order Status**, dates, amount range, sorting, and the number of records shown. Select **More** for additional criteria. Select **Apply** to search or **Clear** to reset the filters.
3. Select a purchase order number above the table to inspect its lines. The refresh icon beside the number reloads that order's data. A reload may depend on the configured integration.
4. Compare each purchase order line with the invoice and its extracted table. The **+** opens existing matching details; it does not itself connect the line to the invoice.

<figure><img src="../../../.gitbook/assets/po-tutorial-v4-search-en.png" alt="Manual search shows the three lines of the test purchase order. Use the filters when needed; a recognized order number does not require a second search."><figcaption><p>Manual search shows the three lines of the test purchase order. Use the filters when needed; a recognized order number does not require a second search.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/po-tutorial-v4-partial-en.png" alt="Partial match: paper accounts for EUR 50 matched; EUR 68 remains open. Partial match does not mean a fixed fifty-percent threshold."><figcaption><p>Partial match: paper accounts for EUR 50 matched; EUR 68 remains open. Partial match does not mean a fixed fifty-percent threshold.</p></figcaption></figure>

## Match lines and review the result

When both tables contain lines, connect an invoice line to the corresponding purchase order line by dragging it, or use the line context menu's matching actions. **Auto Match** attempts to connect eligible lines using your organization's rules. Check the result before saving: a matching item number alone does not prove that quantity, price, or delivery terms agree. See [Purchase Order Matching Tools](purchase-order-matching-tools.md) for the toolbar, column controls, and manual actions, and [Keyboard Shortcuts](keyboard-shortcuts.md) for keyboard actions.

If a document is not matched, read the reason shown above the purchase order area. It may say that the PO number is missing, the order was not found, its lines are unavailable, or the invoice has no extracted lines. Correct the document or configuration indicated by that reason. An administrator can inspect [matching rules](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) and [table extraction](../../../administration-and-setup/settings/document-processing/classification-and-extraction/README.md) when no invoice lines appear.

Common messages and next steps:

| What you see | What to check |
| --- | --- |
| No purchase order number | Enter or correct the PO number on the document, then save. |
| No purchase order was found | Check the number and whether the order was imported into this organization. |
| The order was found but is not connected | Try **Auto Match**, or connect the lines manually after checking both tables. |
| No order lines match | Compare the invoice values with the order and check the matching history. |
| No invoice line items | Check [table extraction](../../../administration-and-setup/settings/document-processing/classification-and-extraction/README.md) before trying to match. |
| No open order lines | Check the [consumed-line statuses](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/consumed-po-line-status.md) and excluded statuses. |

{% hint style="warning" %}
Saving can trigger matching again after a changed or newly detected PO number. Check the displayed result after saving. If a match cannot be saved, read the error shown on the screen and ask an administrator to check the [transformation](../../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md) and [matching rules](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md).
{% endhint %}

Use **Matching history** (clock icon, where your permissions allow it) to inspect how a previous match was decided. It is a read-only view. You can review which rules ran and why a candidate did not match; opening history does not export the document.

### More than one line per match

A single invoice line may correspond to several order lines, or the other way around, where your matching rules allow it. Open the **+** details on a line to inspect any existing multi-match. Check the combined quantity and price, not just one line. An empty detail panel means there is no multi-match to inspect. See [Purchase Order Matching Tools](purchase-order-matching-tools.md) for changing connections.

### Quantities, differences, and discounts

Depending on configuration, matching can compare ordered, received, or remaining delivery quantity, as well as unit price, item number, and other mapped fields. A difference may be accepted if the document type has a configured tolerance. Check the displayed mismatch before accepting it. The [tolerance settings](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md) and [discount guidance](discounts.md) explain these cases.

The totals area, when available, helps reconcile the net amount from the invoice with matched lines and charges. If **Unsettled amount** remains, inspect the individual line values and any [costing element](../../../administration-and-setup/settings/document-processing/classification-and-extraction/table-extraction-for-costing-element.md) before export.

## Check totals and save

Review the invoice preview on the right and compare the line totals and any charges. For a full explanation of the actions in the top toolbar, see [Purchase Order Matching Tools](purchase-order-matching-tools.md). Select **Save** after changing matches. Select **Export** only after you have checked the document and the matching result; the arrow beside Export shows additional configured export choices. Your organization may have different export actions.

The preview toolbar lets you move between document pages, zoom, download the original, and open a larger view. Use it to verify that the purchase order number and line values really appear on the invoice. If you leave with unsaved matching changes, they may be lost.

The available comparisons and tolerance values depend on your document-type settings. Read [PO Matching Rules](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md), [Tolerance Settings](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md), [Disabled Statuses](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-disable-statuses.md), and [Consumed PO Line Status](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/consumed-po-line-status.md) for administrator settings. For many-to-one lines, see [Discounts](discounts.md) and the [Matching Tools](purchase-order-matching-tools.md).
