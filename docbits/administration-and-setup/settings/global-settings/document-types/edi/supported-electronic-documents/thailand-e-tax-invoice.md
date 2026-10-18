---
description: THAILAND E-TAX INVOICE electronic document support in DocBits
---

# 🇹🇭 THAILAND E-TAX INVOICE

<!-- edocs-country-scope -->

{% hint style="info" %}
Check the country guide for version limits, effective configuration and the country explainer. [Thailand](countries/thailand.md). The label does not name a release. Confirm the source XML structure; signature verification and revenue-platform delivery need separate checks.
{% endhint %}

| Property             | Value                                          |
| -------------------- | ---------------------------------------------- |
| **Country / Region** | Thailand                                       |
| **Document Types**   | Tax Invoice, Receipt                           |
| **Format**           | XML (PDF/A-3 embedded)                         |
| **Standard**         | e-Tax Invoice & e-Receipt (Revenue Department) |

Thailand e-Tax Invoice is the electronic tax invoice and receipt standard regulated by the Revenue Department. It uses a hybrid format similar to ZUGFeRD, embedding structured XML data within a PDF/A-3 document. The system requires digital signing with a certificate issued by a Thai CA.

## Support Status

| Component        | Status      |
| ---------------- | ----------- |
| Preview          | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation   | ✅ Supported |

## Default Preview

<figure><img src="../../../../../../.gitbook/assets/thailand-e-tax-invoice-preview.png" alt="Thailand e-Tax Invoice preview in DocBits"><figcaption><p>Default DocBits preview for a Thailand e-Tax Invoice</p></figcaption></figure>

## Related

* [Supported Electronic Documents](./)
