---
description: >-
  Where the value of a header field comes from, and how it is created — the
  explanation behind the Header Field Check on the validation screen.
---

# Header Field Check: Where the Data Comes From

The **Header Field Check** button sits next to **Save** on the validation screen. It opens the report *Where does each value come from?*: for every header field it shows what was on the document, what changed the value on the way, what DocBits shows now, and why.

This page explains how a value is created and what each source means. No expert knowledge needed.

{% hint style="info" %}
The Header Field Check is part of the **Analytics** module. If the button is greyed out, an administrator can grant it to your role under **Settings › Roles**.
{% endhint %}

## A value is always created in this order

| Step | What happens |
| --- | --- |
| **1. Read** | The value is read from the document — by a trained rule, by the AI, or directly from an e-invoice. |
| **2. Transform** | The customer's scripts and transformation rules change the value that was read: shorten it, add to it, adjust its format. |
| **3. Look up** | The value is searched for in the master data. If something is found, the master data record replaces the value that was read. |
| **4. Display** | The user only sees the result. What happened along the way is shown by the Header Field Check. |

Steps 2 and 3 do not always run — but when they do, they change the value. That is exactly where most reported cases come from.

## The sources — what each one means

The icons are the same ones the report shows in its **Action** column and in the filter bar at the top.

### Trained rule

DocBits remembers where a field sits on this type of document, because someone once marked it there.

* **Example:** Supplier “Bornemann” — always in the same place at the top left.
* **If it is wrong:** mark the correct place on the document and save — the rule learns from it.

### AI

No fixed pattern. The AI reads the document like a person and decides for itself which text belongs to which field.

* **Example:** Invoice date, amounts, payment terms.
* **If it is wrong:** correct it. Switch it on and off under **Settings › OCR header fields**.

### E-invoice

With XRechnung or ZUGFeRD nothing is recognised: the value is already a data field in the document and is taken over directly.

* **Example:** Invoice number from the sender's XML field.
* **If it is wrong:** the error lies with the sender. DocBits shows exactly which XML field the value came from.

### Script / transformation rule

After reading, the customer's logic steps in and reshapes the value. The document stays the same — the value does not.

* **Example:** `1001 / LS 206776` becomes `1001`.
* **If it is wrong:** do not look for it on the document. Check **Settings › Scripts** or **Transformation rules**.

### Master data

The value that was read is searched for in your own data — orders, suppliers. A match replaces the value and pulls further fields along with it.

* **Example:** `1001` finds order `06O051001` — and the supplier and buyer then come from there too.
* **If it is wrong:** check **Settings › Lookup configuration**. It says there whether the search is exact or also accepts partial matches.

### Calculated

Not read, but calculated from other fields.

* **Example:** Due date from invoice date plus payment terms.
* **If it is wrong:** usually one of the fields it is calculated from is wrong.

### Barcode

Read from a barcode or QR code on the document.

* **Example:** The invoice number is encoded in the QR code.
* **If it is wrong:** check the barcode settings of the document type.

## The one thing that is misunderstood most often

{% hint style="warning" %}
When a field suddenly contains a value that does not appear like that on the document, it was almost never the AI — but step 2 or step 3. Most often the master data match, which also accepts partial matches: `1001` matches `06O051001`, and with the order that was found, the supplier changes too.
{% endhint %}

In the report, such a field is marked red. The **Action** column shows the master data record together with a red *partial match only* chip, and the matched part of the value is highlighted.

## Reading the report

* **Status chips** at the top count the fields that came unchanged from the document, changed on the way, or are not on the document as shown. Click a chip to show only those fields; click it again to show all.
* **Source filter:** the row of icons shows every extraction method. Click one to show only the fields that went through it.
* **Action:** every step the value went through, with the icon of its source. The step the current value comes from is highlighted. Hover to see what each step did, from which value to which.
* **Reason:** the status of the field. The (i) icon explains why the value is what it is.
* Long values are shortened with … — hover to see the full value.
