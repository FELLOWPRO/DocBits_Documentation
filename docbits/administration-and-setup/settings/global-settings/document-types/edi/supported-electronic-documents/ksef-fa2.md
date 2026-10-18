---
description: KSEF FA2 electronic document support in DocBits
---

# 🇵🇱 KSEF FA2

<!-- edocs-country-scope -->

{% hint style="info" %}
Check the country guide for version limits, effective configuration and the country explainer. [Poland](countries/poland.md). FA2 and FA3 use different structures. Confirm the source schema and test the appropriate mapping; parsing does not submit an invoice to KSeF.
{% endhint %}

| Property             | Value                       |
| -------------------- | --------------------------- |
| **Country / Region** | Poland                      |
| **Document Types**   | Invoice, Corrective Invoice |
| **Format**           | XML                         |
| **Standard**         | KSeF FA(2)                  |

KSeF FA2 is the second schema version of the Polish National e-Invoice System. It defines the XML structure for structured invoices (faktury) including seller/buyer data, line items, VAT rates, and payment terms as required by Polish tax law.

## Support Status

| Component        | Status      |
| ---------------- | ----------- |
| Preview          | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation   | ✅ Supported |

## Default Preview

<figure><img src="../../../../../../.gitbook/assets/ksef-preview.png" alt="KSeF FA(2) invoice preview in DocBits"><figcaption><p>Default DocBits preview for a Poland KSeF FA(2) invoice</p></figcaption></figure>

## Related

* [Supported Electronic Documents](./)
