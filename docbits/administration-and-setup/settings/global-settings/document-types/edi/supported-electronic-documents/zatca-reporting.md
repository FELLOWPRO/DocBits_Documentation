---
description: ZATCA REPORTING electronic document support in DocBits
---

# 🇸🇦 ZATCA REPORTING

<!-- edocs-country-scope -->

{% hint style="info" %}
Check the country guide for version limits, effective configuration and the country explainer. [Saudi Arabia](countries/saudi-arabia.md). These labels describe different processes and invoice variants. Parsing does not prove signing, clearance or reporting through ZATCA.
{% endhint %}

| Property             | Value                                 |
| -------------------- | ------------------------------------- |
| **Country / Region** | Saudi Arabia                          |
| **Document Types**   | Reported Invoice                      |
| **Format**           | UBL 2.1 XML                           |
| **Standard**         | ZATCA Reporting (Phase 2 Integration) |

ZATCA Reporting refers to the Phase 2 integration mode where standard tax invoices are reported to the ZATCA platform within 24 hours of issuance. The reported invoice includes a cryptographic stamp, QR code, and UUID assigned by ZATCA's Fatoorah portal.

## Support Status

| Component        | Status      |
| ---------------- | ----------- |
| Preview          | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation   | ✅ Supported |

## Default Preview

<figure><img src="../../../../../../.gitbook/assets/zatca-reporting-preview.png" alt="ZATCA Reporting invoice preview in DocBits"><figcaption><p>Default DocBits preview for a Saudi Arabia ZATCA Reporting invoice</p></figcaption></figure>

## Related

* [Supported Electronic Documents](./)
