---
description: Podrška za AUNZ PINT SELF-BILLING elektronske dokumente u DocBits
---

# 🇦🇺 AUNZ PINT SELF-BILLING

| Svojstvo | Vrednost |
|----------|-------|
| **Država / Regija** | Australija / Novi Zeland |
| **Tipovi dokumenata** | Self-Billing faktura |
| **Format** | UBL 2.1 XML |
| **Standard** | PINT A-NZ Self-Billing |
| **Locale** | `en_AU` |

AUNZ PINT Self-Billing je self-billing varijanta A-NZ Peppol International modela fakturisanja. U self-billing scenarijima, kupac kreira fakturu u ime dobavljača. Ovaj tip dokumenta prati istu PINT A-NZ strukturu, ali sa zamenjenim ulogama strana — `AccountingCustomerParty` postaje fakturišuća strana, a `AccountingSupplierParty` je fakturisana strana.

## Status podrške

| Komponenta | Status |
|-----------|--------|
| Pregled | ✅ Podržano |
| Ekstrakcija polja | ✅ Podržano |
| Transformacija | ✅ Podržano |

## Podrazumevani pregled

<figure><img src="aunz-pint-preview.png" alt="Pregled AUNZ PINT Self-Billing fakture u DocBits"><figcaption><p>Podrazumevani DocBits pregled za AUNZ PINT Self-Billing fakturu</p></figcaption></figure>

## Mapiranje polja

Mapiranje polja je identično kao kod [AUNZ PINT](aunz-pint.md) sa sledećom ključnom razlikom:

- **Uloge strana su zamenjene**: U self-billing-u, kupac je fakturišuća strana, a dobavljač je fakturisana strana
- `CustomizationID` sadrži `urn:peppol.org:pint:selfbilling-1@aunz` umesto `billing-1@aunz`

Za kompletnu tabelu mapiranja polja, pogledajte [AUNZ PINT](aunz-pint.md#field-mapping).

## Pravilo klasifikacije

DocBits prepoznaje self-billing dokumente podudaranjem `CustomizationID`:

```
urn:peppol.org:pint:selfbilling-1@aunz
```

I self-billing i redovno fakturisanje se klasifikuju pod elektronski tip dokumenta `PINT A-NZ`.

## Takođe pogledajte

- [AUNZ PINT](aunz-pint.md)
- [Podržani elektronski dokumenti](./)
