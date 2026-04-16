---
description: Supporto documenti elettronici AUNZ PINT SELF-BILLING in DocBits
---

# 🇦🇺 AUNZ PINT SELF-BILLING

| Proprietà | Valore |
|----------|-------|
| **Paese / Regione** | Australia / Nuova Zelanda |
| **Tipi di documento** | Fattura di autofatturazione |
| **Formato** | UBL 2.1 XML |
| **Standard** | PINT A-NZ Self-Billing |
| **Locale** | `en_AU` |

AUNZ PINT Self-Billing è la variante di autofatturazione del modello di fatturazione Peppol International A-NZ. Nello scenario di autofatturazione, l'acquirente crea la fattura per conto del fornitore. Questo tipo di documento segue la stessa struttura PINT A-NZ ma con ruoli delle parti invertiti — `AccountingCustomerParty` diventa la parte fatturante e `AccountingSupplierParty` è la parte fatturata.

## Stato del supporto

| Componente | Stato |
|-----------|--------|
| Anteprima | ✅ Supportato |
| Estrazione campi | ✅ Supportato |
| Trasformazione | ✅ Supportato |

## Anteprima predefinita

<figure><img src="aunz-pint-preview.png" alt="Anteprima fattura AUNZ PINT Self-Billing in DocBits"><figcaption><p>Anteprima predefinita DocBits per una fattura AUNZ PINT Self-Billing</p></figcaption></figure>

## Mappatura dei campi

La mappatura dei campi è identica a [AUNZ PINT](aunz-pint.md) con la seguente differenza principale:

- **I ruoli delle parti sono invertiti**: Nell'autofatturazione, l'acquirente è la parte fatturante e il fornitore è la parte fatturata
- Il `CustomizationID` contiene `urn:peppol.org:pint:selfbilling-1@aunz` invece di `billing-1@aunz`

Per la tabella completa della mappatura dei campi, vedere [AUNZ PINT](aunz-pint.md#field-mapping).

## Regola di classificazione

DocBits rileva i documenti di autofatturazione corrispondendo il `CustomizationID`:

```
urn:peppol.org:pint:selfbilling-1@aunz
```

Sia l'autofatturazione che la fatturazione regolare sono classificate sotto il tipo di documento elettronico `PINT A-NZ`.

## Vedi anche

- [AUNZ PINT](aunz-pint.md)
- [Documenti elettronici supportati](./)
