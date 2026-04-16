---
description: Obsługa dokumentów elektronicznych AUNZ PINT SELF-BILLING w DocBits
---

# 🇦🇺 AUNZ PINT SELF-BILLING

| Właściwość | Wartość |
|----------|-------|
| **Kraj / Region** | Australia / Nowa Zelandia |
| **Typy dokumentów** | Faktura self-billing |
| **Format** | UBL 2.1 XML |
| **Standard** | PINT A-NZ Self-Billing |
| **Locale** | `en_AU` |

AUNZ PINT Self-Billing to wariant self-billing modelu fakturowania Peppol International A-NZ. W scenariuszach self-billing kupujący tworzy fakturę w imieniu dostawcy. Ten typ dokumentu następuje po tej samej strukturze PINT A-NZ, ale z odwróconymi rolami stron — `AccountingCustomerParty` staje się stroną fakturowaną, a `AccountingSupplierParty` jest stroną fakturowaną.

## Status wsparcia

| Komponent | Status |
|-----------|--------|
| Podgląd | ✅ Obsługiwany |
| Ekstrakcja pól | ✅ Obsługiwany |
| Transformacja | ✅ Obsługiwany |

## Domyślny podgląd

<figure><img src="aunz-pint-preview.png" alt="Podgląd faktury AUNZ PINT Self-Billing w DocBits"><figcaption><p>Domyślny podgląd DocBits dla faktury AUNZ PINT Self-Billing</p></figcaption></figure>

## Mapowanie pól

Mapowanie pól jest identyczne jak w [AUNZ PINT](aunz-pint.md) z następującą kluczową różnicą:

- **Role stron są odwrócone**: W self-billing kupujący jest stroną fakturowaną, a dostawca jest stroną fakturowaną
- `CustomizationID` zawiera `urn:peppol.org:pint:selfbilling-1@aunz` zamiast `billing-1@aunz`

Pełną tabelę mapowania pól znajdziesz w [AUNZ PINT](aunz-pint.md#field-mapping).

## Reguła klasyfikacji

DocBits wykrywa dokumenty self-billing poprzez dopasowanie `CustomizationID`:

```
urn:peppol.org:pint:selfbilling-1@aunz
```

Zarówno self-billing, jak i zwykłe fakturowanie są klasyfikowane pod elektronicznym typem dokumentu `PINT A-NZ`.

## Zobacz także

- [AUNZ PINT](aunz-pint.md)
- [Obsługiwane dokumenty elektroniczne](./)
