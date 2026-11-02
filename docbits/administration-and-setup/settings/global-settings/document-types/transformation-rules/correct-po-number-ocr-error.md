# Correct an OCR error in a PO number

The third character of `06O123` is the **letter O**. If extraction produces `060123`, use a conditional prefix transformation to correct the known pattern without a custom script.



## Video walkthrough

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/po-number-ocr-correction-preview-admin/v2/en.mp4" %}
Mike demonstrates the prefix correction, five preview cases and the saved document result.
{% endembed %}

[Watch with English captions, chapters and transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/po-number-ocr-correction-preview-admin/v2/en.html).

The walkthrough uses a synthetic invoice with a deliberately prepared extraction error. Processing waits are shortened.

## Configure the prefix correction

1. Open **Settings → Document Types → settings (gear) → Transformation Rules → Manage transformation rules**. An organisation administrator must enable transformation rules for the selected document type.
2. Create a **Header field** rule with **Purchase Order** as its target. Read from **the field itself**.
3. Under **Only when…**, select **Purchase Order → starts with → `060`**.
4. Remove the initial Trim step. Add **Affix → Strip prefix → `060`**, then **Affix → Add prefix → `06O`**. Enter a capital letter O in the second step. The condition limits both steps to the affected prefix; the remaining characters stay unchanged.
5. Check the live preview, save the rule and reopen it. Test a document, save it, then reload it to verify the persisted purchase order value.

## Test the result

| Sample input | Expected result | Reason |
| --- | --- | --- |
| `060123` | `06O123` | Affected prefix |
| `060987` | `06O987` | Another affected value; suffix preserved |
| `06O123` | `06O123` | Already correct; condition does not match |
| `160123` | `160123` | Different prefix; condition does not match |
| `1060123` | `1060123` | `060` inside the value is not a matching prefix |

This example corrects a known extraction pattern; it does not prove OCR accuracy, that the purchase order exists or that PO matching succeeded. Use this rule only where the expected numbering convention requires `06O`; a legitimate `060` prefix would also be changed. Add supplier conditions when the convention applies only to particular suppliers.

## Why two Affix steps?

 The current editor requires a separate source field for position-dependent steps such as **Find & replace**, even when **Run only once per document** is on. The two prefix steps above work on the same field. After correction, its value no longer starts with `060`, so the condition skips it on subsequent saves.
