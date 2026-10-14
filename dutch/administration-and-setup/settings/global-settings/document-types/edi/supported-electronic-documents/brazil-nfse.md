---
description: BRAZIL NFS-E ondersteuning voor elektronische documenten in DocBits
---

# 🇧🇷 BRAZIL NFS-E

| Eigenschap | Waarde |
|------------|--------|
| **Land / Regio** | Brazilië |
| **Documenttypen** | Dienstenfactuur (Nota Fiscal de Serviços Eletrônica) |
| **Formaat** | XML |
| **Standaard** | NFS-e 2.04 (ABRASF nationale standaard voor gemeentelijke dienstenfacturen) |
| **Taal** | `pt_BR` |

NFS-e (Nota Fiscal de Serviços Eletrônica) is de Braziliaanse elektronische factuur voor diensten, uitgegeven op gemeentelijk niveau. DocBits ondersteunt het ABRASF (Associação Brasileira das Secretarias de Finanças das Capitais) standaardschema. NFS-e documenten gebruiken een andere XML-structuur dan NF-e: de voornaamste belasting is ISS (Imposto Sobre Serviços) in plaats van ICMS, en leverancier/koper worden aangeduid als `PrestadorServico` / `TomadorServico`. Het element `Discriminacao` bevat de vrije-tekst dienstomschrijving.

## Ondersteuningsstatus

| Component | Status |
|-----------|--------|
| Voorbeeld | ✅ Ondersteund |
| Veldextractie | ✅ Ondersteund |
| Transformatie | ✅ Ondersteund |

## Standaard Voorbeeld

<figure><img src="brazil-nfse-preview.png" alt="Brazil NFS-e voorbeeld in DocBits"><figcaption><p>Standaard DocBits-voorbeeld voor een BRAZIL NFS-E document</p></figcaption></figure>

## Veldmapping

### Kopvelden

| DocBits Veld | Bron XPath | Opmerkingen |
|---|---|---|
| `invoice_id` | `//*[local-name()='Numero']` | NFS-e-nummer |
| `invoice_date` | `//*[local-name()='DataEmissao']` | ISO 8601 uitgifte datum |
| `currency` | Vast: `BRL` | Altijd Braziliaanse Real |
| `total_amount` | `//*[local-name()='ValorServicos']` | Brutowaardevan de dienst |
| `net_amount` | `//*[local-name()='ValorLiquidoNfse']` | Nettowaarde na aftrekposten |
| `tax_amount` | `//*[local-name()='ValorIss']` | ISS (gemeentelijke dienstenbelasting) |
| `supplier_name` | `//*[local-name()='PrestadorServico']//*[local-name()='RazaoSocial']` | Naam van de dienstverlener |
| `supplier_id` | `//*[local-name()='PrestadorServico']//*[local-name()='Cnpj']` | CNPJ van de dienstverlener |
| `buyer_name` | `//*[local-name()='TomadorServico']//*[local-name()='RazaoSocial']` | Naam van de dienstafnemer |
| `buyer_id` | `//*[local-name()='TomadorServico']//*[local-name()='Cnpj']` | CNPJ van de dienstafnemer |

> NFS-e beschrijft een enkele dienst in het element `Discriminacao` in plaats van regelitems. Er wordt geen `INVOICE_TABLE` geëxtraheerd.

## Classificatieregel

DocBits detecteert BRAZIL NFS-E documenten via de naamruimte:

```
http://www.abrasf.org.br/nfse.xsd
```

## Gerelateerd

- [BRAZIL NF-E](brazil-nfe.md)
- [BRAZIL NFC-E](brazil-nfce.md)
- [BRAZIL CT-E](brazil-cte.md)
- [Ondersteunde elektronische documenten](./)
