---
description: MYINVOIS electronic document support in DocBits
---

# 🇲🇾 MYINVOIS

<!-- edocs-country-scope -->

{% hint style="info" %}
Check the country guide for version limits, effective configuration and the country explainer. [Malaysia](countries/malaysia.md). The inspected extraction path is XML based. The national platform also accepts JSON, but that does not establish JSON import support in this DocBits mapping.
{% endhint %}

| Property             | Value                                                 |
| -------------------- | ----------------------------------------------------- |
| **Country / Region** | Malaysia                                              |
| **Document Types**   | Invoice, Credit Note, Debit Note, Self-Billed Invoice |
| **Format**           | UBL 2.1 XML                                    |
| **Standard**         | MyInvois (LHDN - Lembaga Hasil Dalam Negeri)          |

MyInvois is Malaysia's e-invoicing system operated by the Inland Revenue Board (LHDN). Effective August 2024 for large enterprises, it requires all invoices to be submitted to the MyInvois portal for validation and receive a unique identifier. The system uses UBL 2.1 and supports both XML and JSON submission formats.

## Support Status

| Component        | Status      |
| ---------------- | ----------- |
| Preview          | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation   | ✅ Supported |

## Default Preview

<figure><img src="../../../../../../.gitbook/assets/myinvois-preview.png" alt="MyInvois invoice preview in DocBits"><figcaption><p>Default DocBits preview for a Malaysia MyInvois invoice</p></figcaption></figure>

## Related

* [Supported Electronic Documents](./)
