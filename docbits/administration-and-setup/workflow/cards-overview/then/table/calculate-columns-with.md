# Calculate columns

This card applies a calculation to two columns of the same table and saves the result in a destination column for each row.

## When and where to use it

Use the card when the next workflow step needs calculated line values, such as **quantity × unit price**. Add it under **Then**, in **Table**. First check that both input columns contain numbers and that the required values are complete.

<figure><img src="../../../../../.gitbook/assets/workflow-card-calc-columns-v2-configured-en-20261024.png" alt="Version 2 card: INVOICE_TABLE, Quantity × Unit price → TOTAL_AMOUNT. The interface displays the table name twice." width="651"><figcaption><p>Version 2 card: INVOICE_TABLE, Quantity × Unit price → TOTAL_AMOUNT. The interface displays the table name twice.</p></figcaption></figure>

## Admin video

**40 seconds · English.** Mike explains when to use the card, configures multiplication and shows the saved results on the same example invoice.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-calc-columns-admin/v1/en.mp4" %}

[Watch with English subtitles](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-calc-columns-admin/v1/en.html) · [Read the transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-calc-columns-admin/v1/en.txt)

## Configure the card

| Setting | Example selection |
| --- | --- |
| Table | `INVOICE_TABLE` |
| First column | `QUANTITY` — Quantity |
| Operation | `*` — multiplication |
| Second column | `UNIT_PRICE` — Unit price |
| Result column | `TOTAL_AMOUNT` — Total Amount |

You can also select `+` (addition), `-` (subtraction) or `/` (division). Column order matters for subtraction and division. Select the table and column identifiers configured in your organization.

<!-- workflow-card-practical-example-20261021 -->

## Practical example

The example invoice contains two rows. The destination column does not exist before the calculation:

| Row | Quantity | Unit price | Saved result in `TOTAL_AMOUNT` |
| --- | --- | --- | --- |
| 1 | 2 | 10 | 20 |
| 2 | 3 | 4 | 12 |

In the demonstrated test, the card creates the destination column. After reopening the invoice, **20.00** and **12.00** remain visible. The input columns and the original `NET_AMOUNT` values are preserved in this example. If the selected destination column already contains values, the calculation replaces them.

## Checks and counterexamples

- Check both input columns and verify the saved results after calculating.
- A missing price can produce zero in the illustrated example. Zero does not establish that the input is complete: check the source values before calculating.
- Text such as `ABC` instead of a number causes a calculation error. Correct the value and check the case again.
- The missing-price and nonnumeric-text cases in the diagram show expected example outcomes. They are not additional executions of the invoice demonstrated in the video.
