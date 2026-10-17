---
description: FACTURX electronic document support in DocBits
---

# 🇫🇷 FACTURX

<!-- edocs-country-scope -->

{% hint style="info" %}
Check the country guide for version limits, effective configuration and the country explainer. [France](countries/france.md). The XML marker 1p0 and Factur-X XMP Version 1.0 do not identify a publication release. Keep the generic label when the release is unknown.
{% endhint %}

| Property             | Value                  |
| -------------------- | ---------------------- |
| **Country / Region** | France / Germany       |
| **Document Types**   | Invoice, Credit Note   |
| **Format**           | CII (PDF/A-3 embedded) |
| **Standard**         | Factur-X               |
| **Based On**         | EN 16931               |

A harmonized CII Guideline ID can identify a family and profile while sharing the same 1p0 marker across several releases. Factur-X XMP Version 1.0 is a schema marker, not a publication such as 1.08 or 1.09. ZUGFeRD XMP can declare its version. When authoritative metadata is absent, keep the generic family result and confirm the original file with the sender.

## Support Status

| Component        | Status      |
| ---------------- | ----------- |
| Preview          | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation   | ✅ Supported |

## Default Preview

<figure><img src="../../../../../../.gitbook/assets/facturx-preview.png" alt="Factur-X invoice preview in DocBits"><figcaption><p>Default DocBits preview for a France Factur-X invoice</p></figcaption></figure>

## Related

* [ZUGFeRD Configuration](../zugferd/)
* [ZUGFeRD Field Mapping](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/administration-and-setup/settings/global-settings/document-types/edi/zugferd/versions/README.md)
* [Supported Electronic Documents](./)
