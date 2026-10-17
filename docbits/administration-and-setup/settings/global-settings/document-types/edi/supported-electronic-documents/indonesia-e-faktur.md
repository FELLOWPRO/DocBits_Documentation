---
description: INDONESIA E-FAKTUR electronic document support in DocBits
---

# 🇮🇩 INDONESIA E-FAKTUR

<!-- edocs-country-scope -->

{% hint style="info" %}
Check the country guide for version limits, effective configuration and the country explainer. [Indonesia](countries/indonesia.md). The entry does not state a release number. Confirm the actual XML payload; a printed invoice or QR image does not establish XML support.
{% endhint %}

| Property             | Value                                      |
| -------------------- | ------------------------------------------ |
| **Country / Region** | Indonesia                                  |
| **Document Types**   | Tax Invoice (Faktur Pajak)                 |
| **Format**           | XML/CSV                                    |
| **Standard**         | e-Faktur (DJP - Direktorat Jenderal Pajak) |

e-Faktur is the Indonesian electronic tax invoice system operated by the Directorate General of Taxes (DJP). It is mandatory for all PKP (Pengusaha Kena Pajak) taxpayers and includes the NSFP (Nomor Seri Faktur Pajak) serial number, NPWP tax identifiers, and PPN (VAT) calculations.

## Support Status

| Component        | Status      |
| ---------------- | ----------- |
| Preview          | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation   | ✅ Supported |

## Default Preview

<figure><img src="../../../../../../.gitbook/assets/indonesia-e-faktur-preview.png" alt="Indonesia E-Faktur invoice preview in DocBits"><figcaption><p>Default DocBits preview for an Indonesia E-Faktur invoice</p></figcaption></figure>

## Related

* [Supported Electronic Documents](./)
