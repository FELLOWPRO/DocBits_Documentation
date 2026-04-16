---
description: AUNZ PINT SELF-BILLING elektronisch document ondersteuning in DocBits
---

# 🇦🇺 AUNZ PINT SELF-BILLING

| Eigenschap | Waarde |
|----------|-------|
| **Land / Regio** | Australië / Nieuw-Zeeland |
| **Documenttypen** | Self-Billing Factuur |
| **Formaat** | UBL 2.1 XML |
| **Standaard** | PINT A-NZ Self-Billing |
| **Locale** | `en_AU` |

AUNZ PINT Self-Billing is de self-billing-variant van het A-NZ Peppol International factuurmodel. Bij self-billing-scenario's maakt de koper de factuur namens de leverancier. Dit documenttype volgt dezelfde PINT A-NZ-structuur maar met omgekeerde partijrollen — de `AccountingCustomerParty` wordt de facturerende partij en de `AccountingSupplierParty` is de gefactureerde partij.

## Ondersteuningsstatus

| Onderdeel | Status |
|-----------|--------|
| Voorbeeld | ✅ Ondersteund |
| Veldextractie | ✅ Ondersteund |
| Transformatie | ✅ Ondersteund |

## Standaard voorbeeld

<figure><img src="aunz-pint-preview.png" alt="AUNZ PINT Self-Billing factuur voorbeeld in DocBits"><figcaption><p>Standaard DocBits voorbeeld voor een AUNZ PINT Self-Billing factuur</p></figcaption></figure>

## Veldtoewijzing

De veldtoewijzing is identiek aan [AUNZ PINT](aunz-pint.md) met het volgende belangrijke verschil:

- **Partijrollen zijn omgekeerd**: Bij self-billing is de koper de facturerende partij en de leverancier is de gefactureerde partij
- De `CustomizationID` bevat `urn:peppol.org:pint:selfbilling-1@aunz` in plaats van `billing-1@aunz`

Voor de volledige veldtoewijzingstabel, zie [AUNZ PINT](aunz-pint.md#field-mapping).

## Classificatieregel

DocBits detecteert self-billing-documenten door de `CustomizationID` te matchen:

```
urn:peppol.org:pint:selfbilling-1@aunz
```

Zowel self-billing als reguliere facturatie worden geclassificeerd onder het elektronische documenttype `PINT A-NZ`.

## Zie ook

- [AUNZ PINT](aunz-pint.md)
- [Ondersteunde elektronische documenten](./)
