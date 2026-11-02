---
description: ZUGFERD 1.0 COMFORT electronic document support in DocBits
---

# 🇩🇪 ZUGFERD 1.0 COMFORT

<!-- edocs-country-scope -->

{% hint style="info" %}
Check the country guide for version limits, effective configuration and the country explainer. [Germany](countries/germany.md). Syntax, publication version and profile are different choices. Do not infer a Factur-X publication from the shared 1p0 marker.
{% endhint %}

| Property             | Value                        |
| -------------------- | ---------------------------- |
| **Country / Region** | Germany                      |
| **Document Types**   | Invoice, Credit Note         |
| **Format**           | CII (PDF/A-3 embedded)       |
| **Standard**         | ZUGFeRD 1.0, Comfort profile |
| **Based On**         | ZUGFeRD 1.0 specification    |

The Comfort profile of ZUGFeRD 1.0 extends the Basic profile with additional fields for payment terms, delivery information, and detailed tax breakdowns. It enables fully automated invoice processing without manual data entry.

## Support Status

| Component        | Status      |
| ---------------- | ----------- |
| Preview          | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation   | ✅ Supported |

## Default Preview

<figure><img src="../../../../../../.gitbook/assets/zugferd-preview.png" alt="ZUGFeRD 1.0 Comfort invoice preview in DocBits"><figcaption><p>Default DocBits preview for a Germany ZUGFeRD 1.0 Comfort invoice</p></figcaption></figure>

## Related

* [ZUGFeRD Configuration](../zugferd/)
* [ZUGFeRD Field Mapping](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/administration-and-setup/settings/global-settings/document-types/edi/zugferd/versions/README.md)
* [Supported Electronic Documents](./)
