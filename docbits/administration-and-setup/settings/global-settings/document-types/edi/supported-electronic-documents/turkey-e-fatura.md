---
description: TURKEY E-FATURA electronic document support in DocBits
---

# 🇹🇷 TURKEY E-FATURA

<!-- edocs-country-scope -->

{% hint style="info" %}
Check the country guide for version limits, effective configuration and the country explainer. [Turkey](countries/turkey.md). Check the source profile and document structure. The family label does not identify every UBL-TR release or establish delivery through the tax platform.
{% endhint %}

| Property             | Value                                   |
| -------------------- | --------------------------------------- |
| **Country / Region** | Turkey                                  |
| **Document Types**   | Invoice, Credit Note                    |
| **Format**           | UBL-TR 1.2 XML                          |
| **Standard**         | e-Fatura (GİB - Revenue Administration) |

Turkey e-Fatura is the primary electronic invoice standard mandated by the GİB (Revenue Administration) for B2B transactions between registered taxpayers. Invoices are exchanged through registered integrators and the GİB platform. The format uses UBL-TR, Turkey's localized version of UBL, with Turkish-specific fields for TCKN/VKN tax identification.

## Support Status

| Component        | Status      |
| ---------------- | ----------- |
| Preview          | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation   | ✅ Supported |

## Default Preview

<figure><img src="../../../../../../.gitbook/assets/turkey-e-fatura-preview.png" alt="Turkey E-Fatura invoice preview in DocBits"><figcaption><p>Default DocBits preview for a Turkey E-Fatura invoice</p></figcaption></figure>

## Related

* [Supported Electronic Documents](./)
* [TURKEY E-ARSIV](turkey-e-arsiv.md)
