---
description: KSEF FA3 electronic document support in DocBits
---

# 🇵🇱 KSEF FA3

<!-- edocs-country-scope -->

{% hint style="info" %}
Check the country guide for version limits, effective configuration and the country explainer. [Poland](countries/poland.md). FA2 and FA3 use different structures. Confirm the source schema and test the appropriate mapping; parsing does not submit an invoice to KSeF.
{% endhint %}

| Property             | Value                       |
| -------------------- | --------------------------- |
| **Country / Region** | Poland                      |
| **Document Types**   | Invoice, Corrective Invoice |
| **Format**           | XML                         |
| **Standard**         | KSeF FA(3)                  |

KSeF FA3 is the latest schema version of the Polish National e-Invoice System. It adds support for additional document types, improved handling of corrective invoices, and updated validation rules aligned with the latest Polish VAT regulations.

## Support Status

| Component        | Status      |
| ---------------- | ----------- |
| Preview          | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation   | ✅ Supported |

## Default Preview

<figure><img src="../../../../../../.gitbook/assets/ksef-preview.png" alt="KSeF FA(3) invoice preview in DocBits"><figcaption><p>Default DocBits preview for a Poland KSeF FA(3) invoice</p></figcaption></figure>

## Related

* [Supported Electronic Documents](./)
