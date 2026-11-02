---
description: ZUGFERD 2.3 electronic document support in DocBits
---

# 🇩🇪 ZUGFERD 2.3

<!-- edocs-country-scope -->

{% hint style="info" %}
Check the country guide for version limits, effective configuration and the country explainer. [Germany](countries/germany.md). Syntax, publication version and profile are different choices. Do not infer a Factur-X publication from the shared 1p0 marker.
{% endhint %}

| Property             | Value                  |
| -------------------- | ---------------------- |
| **Country / Region** | Germany                |
| **Document Types**   | Invoice, Credit Note   |
| **Format**           | CII (PDF/A-3 embedded) |
| **Standard**         | ZUGFeRD 2.3            |
| **Based On**         | EN 16931               |

ZUGFeRD 2.3, released in September 2024, is equivalent to Factur-X 1.0.07. It updates the CII XML to the D22B specification, adds improved validation rules, and introduces support for the XRechnung reference profile to meet German B2G requirements.

## Support Status

| Component        | Status      |
| ---------------- | ----------- |
| Preview          | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation   | ✅ Supported |

## Default Preview

<figure><img src="../../../../../../.gitbook/assets/zugferd-preview.png" alt="ZUGFeRD 2.3 invoice preview in DocBits"><figcaption><p>Default DocBits preview for a Germany ZUGFeRD 2.3 invoice</p></figcaption></figure>

## Related

* [ZUGFeRD Configuration](../zugferd/)
* [ZUGFeRD Field Mapping](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/administration-and-setup/settings/global-settings/document-types/edi/zugferd/versions/README.md)
* [Supported Electronic Documents](./)
