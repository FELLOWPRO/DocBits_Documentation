---
description: AUNZ PINT SELF-BILLING electronic document support in DocBits
---

# 🇦🇺 AUNZ PINT SELF-BILLING

| Property | Value |
|----------|-------|
| **Country / Region** | Australia / New Zealand |
| **Document Types** | Self-Billed Invoice |
| **Format** | UBL 2.1 XML |
| **Standard** | PINT A-NZ Self-Billing |
| **Locale** | `en_AU` |

AUNZ PINT Self-Billing is the self-billing variant of the A-NZ Peppol International invoice model. In self-billing scenarios, the buyer creates the invoice on behalf of the supplier. This document type follows the same PINT A-NZ structure but with reversed party roles — the `AccountingCustomerParty` becomes the invoicing party and the `AccountingSupplierParty` is the party being billed.

## Support Status

| Component | Status |
|-----------|--------|
| Preview | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation | ✅ Supported |

## Default Preview

<figure><img src="aunz-pint-preview.png" alt="AUNZ PINT Self-Billing invoice preview in DocBits"><figcaption><p>Default DocBits preview for an AUNZ PINT Self-Billing invoice</p></figcaption></figure>

## Field Mapping

The field mapping is identical to [AUNZ PINT](aunz-pint.md) with the following key difference:

- **Party roles are reversed**: In self-billing, the buyer is the invoicing party and the supplier is the party being billed
- The `CustomizationID` contains `urn:peppol.org:pint:selfbilling-1@aunz` instead of `billing-1@aunz`

For the complete field mapping table, see [AUNZ PINT](aunz-pint.md#field-mapping).

## Classification Rule

DocBits detects self-billing documents by matching the `CustomizationID`:

```
urn:peppol.org:pint:selfbilling-1@aunz
```

Both self-billing and regular billing patterns classify under the `PINT A-NZ` electronic document type.

## Related

- [AUNZ PINT](aunz-pint.md)
- [Supported Electronic Documents](./)