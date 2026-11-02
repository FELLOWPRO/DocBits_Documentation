# Set Negative Sign for Credit Notes

### Overview

The **Set Negative Sign for Credit Notes** setting makes sure that **credit notes** are stored with **negative amounts**. A credit note reverses or refunds part of an invoice, so in accounting its values should reduce the totals — that is, they should be negative. When this setting is on, DocBits applies that negative sign for you automatically.

This setting is **enabled by default**.

### What Does It Do?

When a document is recognized as a **credit note**, DocBits automatically turns its amounts into negative values during processing. This affects the monetary fields, including the net amounts, tax amounts and totals (e.g. net amount, tax amount, total tax amount, total net amount and total amount).

* **Enabled (default)** — Credit note amounts are saved as negative values (for example, `150.00` becomes `-150.00`). Regular invoices are not affected.
* **Disabled** — Amounts are kept exactly as they were read from the document, without any sign change.

{% hint style="info" %}
This only applies to documents identified as **credit notes**. Normal invoices are always left unchanged.
{% endhint %}

### Benefits

* **Correct bookkeeping**: Credit notes reduce balances, so negative values are what your accounting and ERP systems expect.
* **No manual editing**: Your team doesn’t have to flip the sign by hand on every credit note.
* **Consistency**: Every credit note is handled the same way across your organization.

### How to Use

1. Go to **Settings**.
2. Select **Document Processing**.
3. Select **Module**.
4. Open the **Document Type** section.
5. Find **Set Negative Sign for Credit Notes** and switch the toggle on or off.

### When to Use This Feature

* **Keep it enabled** if your accounting or ERP system expects credit notes to arrive with negative amounts (this is the most common setup).
* **Disable it** only if your downstream system already handles the sign itself, or expects credit note amounts to stay positive.
