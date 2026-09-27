# Calculate PO unit price

## **Overview**

You can choose to automatically calculate the **unit price** of every purchase order line from the line's **amount** and **quantity**, instead of using the unit price that came with the purchase order. This is particularly useful when the unit price in the purchase order (in Infor ERP / SAP) differs from the price on the document. Such discrepancies may arise if a discount is applied to the unit price in the purchase order, while the document only applies the discount to the net amount.

## **Activation Steps**

1.  Navigate to **Settings** -> **Global Settings** -> **Document Types**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_1.png" alt=""><figcaption></figcaption></figure>
2.  Select the desired document type and click on **More Settings**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_2.png" alt=""><figcaption></figcaption></figure>
3.  In the **Purchase Order** section, enable the option **Calculate PO Unit Price**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_3.png" alt=""><figcaption></figcaption></figure>

## How the price is calculated

Once the setting is activated, the unit price of a purchase order line is calculated as:

**`Unit Price = Line Amount ÷ Quantity × Unit Price Per`**

where the **line amount** is chosen like this:

| Purchase order line carries                                                              | Line amount used                       |
| ---------------------------------------------------------------------------------------- | -------------------------------------- |
| a **net amount** (`extended_amount`) that is greater than 0 and not above the line total | the net amount                         |
| no net amount, or a net amount above the line total                                      | the line **total** (`total_amount`)    |
| no positive amount at all, or no positive quantity                                       | nothing is calculated, the PO price stays |

Why the net amount comes first: ERP feeds (Infor BODs) send the net line amount as `extended_amount` and carry **tax and charges on top** in `total_amount`. Dividing a taxed total by the quantity gives a gross unit price, and every invoice that is priced net then shows as _unit price under-matched_ although it is correct. Example from a real purchase order line: quantity 9, net amount 879.84, total 954.63 (8.5 % tax) — the net-based price is 97.76 and matches the invoice; the total-based price would be 106.07.

A net amount that is **larger** than the line total cannot be a net amount, so the total is used in that case. A `Unit Price Per` of 0 or empty counts as 1.

{% hint style="info" %}
The calculated price is written to the purchase order snapshot that is stored on the document, and it is **recalculated every time the document is matched** (Auto PO Match, manual match, matching on save). A document that was matched before the setting was changed therefore picks up the new price on its next match — no reload of the purchase order is needed.
{% endhint %}

## Example:

<figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_4.png" alt="" width="563"><figcaption></figcaption></figure>

In this case, the unit price (without the discount) is extracted from the document, while the purchase order in the ERP stores the unit price with the discount applied. This results in a mismatch in the unit price. With the setting activated, the unit price is taken from the line amount and quantity instead, so both sides agree.

## Related settings

* [Purchase Order Matching Rules](purchase-order-matching-rules.md) — the rules compare the **effective** unit price, which is this calculated price when the setting is on.
* [Purchase Order Tolerance Settings](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md) — how much the invoice price may deviate from the calculated price.
