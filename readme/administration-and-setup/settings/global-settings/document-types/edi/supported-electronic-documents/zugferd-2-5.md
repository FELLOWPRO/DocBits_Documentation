---
description: ZUGFERD 2.5 electronic document support in DocBits
---

# 🇩🇪 ZUGFERD 2.5

| Property | Value |
|----------|-------|
| **Country / Region** | Germany |
| **Document Types** | Invoice, Credit Note |
| **Format** | CII (PDF/A-3 embedded) or UBL XML |
| **Standard** | ZUGFeRD 2.5 |
| **Based On** | EN 16931 |

ZUGFeRD 2.5 (the FeRD/FNFE-MPE common publication of June 2026) is equivalent to Factur-X 1.09. Its CII XML uses the UN/CEFACT D22B base, which is backwards-compatible with D16B, so the full ZUGFeRD 2.4 extraction and transformation contract continues to apply. The EXTENDED profile adds new fields for payment means and BIC, a third-party payee (factor), and the allowance/charge tax-exemption reason.

All five profiles are supported: MINIMUM, BASIC WL, BASIC, EN 16931 (COMFORT) and EXTENDED. DocBits classifies the CII and UBL variants separately.

## Support Status

| Component | Status |
|-----------|--------|
| Preview | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation | ✅ Supported |

## Related

- [Factur-X 1.09 / ZUGFeRD 2.5](facturx-1-09-zugferd-2-5.md)
- [ZUGFeRD Configuration](../zugferd/configuration.md)
- [ZUGFeRD Field Mapping](../zugferd/README.md)
- [Supported Electronic Documents](./)
