# Consumed PO line status

**Consumed PO line status** colors purchase order lines in the matching view according to how much of each line has already been matched. Turn it on for the invoice document type if your team needs to spot unused, partly used, and fully used PO lines quickly. The color is a visual aid; check the **Matched Quantity** and the selected PO quantity column before deciding whether a line can be matched again.

## Turn on the setting

1. Open **Settings → Document Types**. Find the document type used for your invoices and select the gear on its card to open **More Settings**. The screenshot shows the **Invoice** card. Leave the **Activate** and **Extraction** switches as they are.

   <figure><img src="../../../../../../.gitbook/assets/consumed-po-line-document-types-en.png" alt="Document Types page with the Invoice card and its More Settings gear"><figcaption><p>Open More Settings from the Invoice card.</p></figcaption></figure>

2. Expand **Purchase Order** if it is collapsed. Find **Consumed PO line status** and turn on its switch. This is a separate setting from **Update Document Purchase Order Status** further down the same section.

   <figure><img src="../../../../../../.gitbook/assets/consumed-po-line-settings-en.png" alt="Purchase Order section of More Settings, with the Consumed PO line status switch visible"><figcaption><p>Choose the Consumed PO line status switch.</p></figcaption></figure>

   <figure><img src="../../../../../../.gitbook/assets/consumed-po-line-toggle-en.png" alt="Close view of the Consumed PO line status label and switch"><figcaption><p>The switch is off in this example; turn it on to show the matching colors.</p></figcaption></figure>

3. Open an invoice with purchase order matching and inspect its PO lines. The examples below show how the line colors relate to matching state. For the matching steps, see [Purchase Order Matching](../../../../../../end-user-and-partner-section/end-user-section/purchase-order-matching/README.md).

## Read the PO line colors

| Appearance | Meaning | What to check |
| --- | --- | --- |
| Plain or white | No quantity on this PO line has been matched yet. | Check the PO quantity and invoice line before matching. |
| Blue tint | You selected the line in the current matching view. | Selection is temporary; it does not mean the line is fully matched. |
| Pale orange | Some quantity has been matched, but the matched quantity is below the selected PO quantity. | Check how much quantity remains. |
| Pale violet | The matched quantity is at least the selected PO quantity. | Do not assume more quantity is available. |

<figure><img src="../../../../../../.gitbook/assets/image (470).png" alt="PO line with zero matched quantity and no status color"><figcaption><p>No quantity has been matched yet.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/image (472).png" alt="PO line with a blue selection tint in the matching view"><figcaption><p>The line is selected for the current match.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/consumed_po_line_status.png" alt="PO line with a pale orange background and a matched quantity below the PO quantity"><figcaption><p>The line is partly used.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/image (473).png" alt="PO line with a pale violet background and a matched quantity equal to the PO quantity"><figcaption><p>The line is fully used.</p></figcaption></figure>

A crossed-out line has a different meaning: its PO status may be excluded by [PO disable statuses](purchase-order-disable-statuses.md). Check that setting if a line cannot be selected.
