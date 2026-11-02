---
description: MEXICO CFDI 3.3 electronic document support in DocBits
---

# 🇲🇽 MEXICO CFDI 3.3

<!-- edocs-country-scope -->

{% hint style="info" %}
Check the country guide for version limits, effective configuration and the country explainer. [Mexico](countries/mexico.md). Check the namespace, version and TipoDeComprobante. A credit-note document is not identified by a negative amount alone; parsing does not certify SAT clearance.
{% endhint %}

| Property             | Value                                              |
| -------------------- | -------------------------------------------------- |
| **Country / Region** | Mexico                                             |
| **Document Types**   | Invoice, Credit Note, Payment Receipt              |
| **Format**           | XML                                                |
| **Standard**         | CFDI 3.3 (Comprobante Fiscal Digital por Internet) |

CFDI 3.3 is the previous generation of the Mexican digital tax receipt standard issued by the SAT (Servicio de Administración Tributaria). While superseded by CFDI 4.0, many historical invoices still use this version. It includes the UUID (folio fiscal), RFC identifiers, and IEPS/IVA tax calculations.

## Support Status

| Component        | Status      |
| ---------------- | ----------- |
| Preview          | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation   | ✅ Supported |

## Default Preview

<figure><img src="../../../../../../.gitbook/assets/mexico-cfdi-3-3-preview.png" alt="Mexico CFDI 3.3 invoice preview in DocBits"><figcaption><p>Default DocBits preview for a Mexico CFDI 3.3 invoice</p></figcaption></figure>

## Related

* [Supported Electronic Documents](./)
