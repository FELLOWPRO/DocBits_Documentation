---
description: BRAZIL CT-E ondersteuning voor elektronische documenten in DocBits
---

# 🇧🇷 BRAZIL CT-E

| Eigenschap | Waarde |
|------------|--------|
| **Land / Regio** | Brazilië |
| **Documenttypen** | Transportfactuur (Conhecimento de Transporte Eletrônico) |
| **Formaat** | XML |
| **Standaard** | CT-e 3.0 (elektronisch vracht-/transportvrachtbrief) |
| **Taal** | `pt_BR` |

CT-e (Conhecimento de Transporte Eletrônico, `<mod>57</mod>`) is het Braziliaanse elektronische transportdocument dat wordt uitgegeven door logistieke bedrijven en vrachtvervoerders. Het documenteert de transportdienst, de vrachtkostenwaarde, herkomst- en bestemmingsgemeenten (`cMunIni` / `cMunFim`), en de vrachtprijs (`vTPrest`). In tegenstelling tot NF-e gebruikt CT-e `cteProc` als rootelement en verwijst het naar gekoppelde NF-e-documenten.

## Ondersteuningsstatus

| Component | Status |
|-----------|--------|
| Voorbeeld | ✅ Ondersteund |
| Veldextractie | ✅ Ondersteund |
| Transformatie | ✅ Ondersteund |

## Standaard Voorbeeld

<figure><img src="brazil-cte-preview.png" alt="Brazil CT-e voorbeeld in DocBits"><figcaption><p>Standaard DocBits-voorbeeld voor een BRAZIL CT-E document</p></figcaption></figure>

## Veldmapping

### Kopvelden

| DocBits Veld | Bron XPath | Opmerkingen |
|---|---|---|
| `invoice_id` | `//*[local-name()='ide']/*[local-name()='nCT']` | CT-e-nummer |
| `invoice_date` | `//*[local-name()='ide']/*[local-name()='dhEmi']` | ISO 8601 met BRT-offset |
| `currency` | Vast: `BRL` | Altijd Braziliaanse Real |
| `total_amount` | `//*[local-name()='vPrest']/*[local-name()='vTPrest']` | Totale waarde van de transportdienst |
| `net_amount` | `//*[local-name()='vPrest']/*[local-name()='vRec']` | Te ontvangen bedrag |
| `tax_amount` | `//*[local-name()='ICMS']//*[local-name()='vICMS']` | ICMS op transportdienst |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']` | Naam van de vervoerder (transportadora) |
| `supplier_id` | `//*[local-name()='emit']/*[local-name()='CNPJ']` | CNPJ van de vervoerder |
| `buyer_name` | `//*[local-name()='dest']/*[local-name()='xNome']` | Naam van de geadresseerde (destinatário) |
| `buyer_id` | `//*[local-name()='dest']/*[local-name()='CNPJ']` | CNPJ van de geadresseerde |

> CT-e bevat geen regelitemtabel — de transportdienst is een enkelvoudige kosten op documentniveau.

## Classificatieregel

DocBits detecteert BRAZIL CT-E documenten via:

```
http://www.portalfiscal.inf.br/cte
```

in de XML-naamruimte (rootelement `<cteProc>`).

## Gerelateerd

- [BRAZIL NF-E](brazil-nfe.md)
- [BRAZIL NFC-E](brazil-nfce.md)
- [BRAZIL NFS-E](brazil-nfse.md)
- [Ondersteunde elektronische documenten](./)
