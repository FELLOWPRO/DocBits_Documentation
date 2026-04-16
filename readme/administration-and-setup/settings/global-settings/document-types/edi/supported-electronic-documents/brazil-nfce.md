---
description: BRAZIL NFC-E ondersteuning voor elektronische documenten in DocBits
---

# 🇧🇷 BRAZIL NFC-E

| Eigenschap | Waarde |
|------------|--------|
| **Land / Regio** | Brazilië |
| **Documenttypen** | Consumentenfactuur (Nota Fiscal de Consumidor Eletrônica) |
| **Formaat** | XML |
| **Standaard** | NFC-e 4.0 (retail / kassafactuur voor eindconsumenten) |
| **Taal** | `pt_BR` |

NFC-e (Nota Fiscal de Consumidor Eletrônica, `<mod>65</mod>`) is de Braziliaanse elektronische factuur voor retailverkopen aan eindconsumenten. Het deelt het NF-e XML-schema (naamruimte `nfeProc`) maar gebruikt modelcode 65. NFC-e documenten bevatten doorgaans een CPF (persoonlijk belastingnummer) voor de koper in plaats van een CNPJ, en bevatten geen PIS/COFINS per regel voor eenvoudige retailtransacties.

## Ondersteuningsstatus

| Component | Status |
|-----------|--------|
| Voorbeeld | ✅ Ondersteund |
| Veldextractie | ✅ Ondersteund |
| Transformatie | ✅ Ondersteund |

## Standaard Voorbeeld

<figure><img src="brazil-nfce-preview.png" alt="Brazil NFC-e voorbeeld in DocBits"><figcaption><p>Standaard DocBits-voorbeeld voor een BRAZIL NFC-E document</p></figcaption></figure>

## Veldmapping

### Kopvelden

| DocBits Veld | Bron XPath | Opmerkingen |
|---|---|---|
| `invoice_id` | `//*[local-name()='ide']/*[local-name()='nNF']` | Nota Fiscal-nummer |
| `invoice_date` | `//*[local-name()='ide']/*[local-name()='dhEmi']` | ISO 8601 met BRT-offset |
| `currency` | Vast: `BRL` | Altijd Braziliaanse Real |
| `total_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vNF']` | Totale NFC-e-waarde |
| `net_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vProd']` | Subtotaal producten |
| `tax_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vICMS']` | ICMS-belastingtotaal |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']` | Naam van de retailer |
| `supplier_id` | `//*[local-name()='emit']/*[local-name()='CNPJ']` of `CPF` | CNPJ of CPF |
| `buyer_name` | `//*[local-name()='dest']/*[local-name()='xNome']` | Naam van de consument |
| `buyer_id` | `//*[local-name()='dest']/*[local-name()='CPF']` of `CNPJ` | CPF (particulier) of CNPJ |

### Regelitemtabel (`INVOICE_TABLE`)

Rijpad: `//*[local-name()='det']`

| Kolom | Relatief XPath | Opmerkingen |
|---|---|---|
| `POSITION` | `@nItem` | Volgnummer van het item |
| `ITEM_CODE` | `*[local-name()='prod']/*[local-name()='cProd']` | Productcode |
| `DESCRIPTION` | `*[local-name()='prod']/*[local-name()='xProd']` | Productomschrijving |
| `NCM_CODE` | `*[local-name()='prod']/*[local-name()='NCM']` | NCM douaneclassificatie |
| `CFOP_CODE` | `*[local-name()='prod']/*[local-name()='CFOP']` | Fiscale operatiecode |
| `UNIT` | `*[local-name()='prod']/*[local-name()='uCom']` | Meeteenheid |
| `QUANTITY` | `*[local-name()='prod']/*[local-name()='qCom']` | Commerciële hoeveelheid |
| `UNIT_PRICE` | `*[local-name()='prod']/*[local-name()='vUnCom']` | Eenheidsprijs |
| `TOTAL_AMOUNT` | `*[local-name()='prod']/*[local-name()='vProd']` | Regeltotaal |
| `ICMS_AMOUNT` | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='vICMS']` | ICMS-belasting per regel |
| `VAT_RATE` | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='pICMS']` | ICMS-tarief (%) |

## Classificatieregel

DocBits detecteert BRAZIL NFC-E documenten via het patroon `<mod>65</mod>` binnen de XML met naamruimte `http://www.portalfiscal.inf.br/nfe`.

## Gerelateerd

- [BRAZIL NF-E](brazil-nfe.md)
- [BRAZIL CT-E](brazil-cte.md)
- [BRAZIL NFS-E](brazil-nfse.md)
- [Ondersteunde elektronische documenten](./)
