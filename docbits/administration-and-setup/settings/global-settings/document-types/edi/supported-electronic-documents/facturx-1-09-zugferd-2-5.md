---
description: FACTURX 1.09 - ZUGFERD 2.5 electronic document support in DocBits
---

# 🇫🇷 FACTURX 1.09 - ZUGFERD 2.5

<!-- edocs-country-scope -->

{% hint style="info" %}
Check the country guide for version limits, effective configuration and the country explainer. [France](countries/france.md). The XML marker 1p0 and Factur-X XMP Version 1.0 do not identify a publication release. Keep the generic label when the release is unknown.
{% endhint %}

| Property | Value |
|----------|-------|
| **Country / Region** | France / Germany |
| **Document Types** | Invoice, Credit Note (verify the effective mapping) |
| **Format** | CII (PDF/A-3 embedded) |
| **Standard** | Factur-X 1.09 / ZUGFeRD 2.5 |
| **Based On** | EN 16931 |

ZUGFeRD 2.5 and Factur-X 1.09 are equivalent releases. The hybrid format embeds CII D22B XML in PDF/A-3; UBL is not its XML syntax. See the [FeRD release reference](https://www.ferd-net.de/publikationen-produkte/publikationen/detailseite/zugferd-25-english).

The standard defines MINIMUM, BASIC WL, BASIC, EN16931 and EXTENDED profiles. A profile name in the catalogue does not establish automatic detection or complete field coverage. MINIMUM and BASIC WL can omit line-item information needed by your integration.

This page describes the June 2026 release. The later [Factur-X 1.09.2 / ZUGFeRD 2.5.2 release](https://fnfe-mpe.org/factur-x/factur-x_en/) must be identified separately; a family identifier such as `1p0` alone is insufficient.

## Support Status

The read-only development catalogue check on 31 October 2026 found `FACTURX 1.09 - ZUGFERD 2.5` for `INVOICE`.

| Component | Configuration observed |
|-----------|------------------------|
| Preview | `PREVIEW` (XSLT) |
| Field extraction | `EXTRACTION_PATHS` (JSON) |
| Transformation | `TRANSFORMATION` (XSLT) |

These entries confirm available configuration, not successful processing of every file or profile. Check the effective Default or Custom source and active version in your organisation. Standard backward compatibility does not guarantee unchanged extraction or transformation results. Test representative invoices and credit notes, required fields and the ERP export separately; legal validation and delivery-network requirements need their own acceptance.

## Related

- [ZUGFeRD 2.5](zugferd-2-5.md)
- [ZUGFeRD Configuration](../zugferd/configuration.md)
- [ZUGFeRD Field Mapping](../zugferd/README.md)
- [Supported Electronic Documents](./)
