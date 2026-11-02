---
description: ZATCA SIMPLIFIED electronic document support in DocBits
---

# 🇸🇦 ZATCA SIMPLIFIED

<!-- edocs-country-scope -->

{% hint style="info" %}
Check the country guide for version limits, effective configuration and the country explainer. [Saudi Arabia](countries/saudi-arabia.md). These labels describe different processes and invoice variants. Parsing does not prove signing, clearance or reporting through ZATCA.
{% endhint %}

| Property             | Value                        |
| -------------------- | ---------------------------- |
| **Country / Region** | Saudi Arabia                 |
| **Document Types**   | Simplified Tax Invoice       |
| **Format**           | UBL 2.1 XML                  |
| **Standard**         | ZATCA Simplified Tax Invoice |

ZATCA Simplified Tax Invoice is used for B2C transactions in Saudi Arabia where the total amount (including VAT) does not exceed SAR 1,000. Unlike standard tax invoices, simplified invoices do not require buyer identification but must include a QR code with the TLV-encoded seller information, VAT amount, and timestamp.

## Support Status

| Component        | Status      |
| ---------------- | ----------- |
| Preview          | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation   | ✅ Supported |

## Default Preview

<figure><img src="../../../../../../.gitbook/assets/zatca-simplified-preview.png" alt="ZATCA Simplified invoice preview in DocBits"><figcaption><p>Default DocBits preview for a Saudi Arabia ZATCA Simplified invoice</p></figcaption></figure>

## Related

* [Supported Electronic Documents](./)
