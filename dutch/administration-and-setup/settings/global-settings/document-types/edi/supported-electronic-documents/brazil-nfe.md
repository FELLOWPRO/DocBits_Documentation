---
description: BRAZIL NF-E ondersteuning voor elektronische documenten in DocBits
---

# 🇧🇷 BRAZIL NF-E

| Eigenschap | Waarde |
|------------|--------|
| **Land / Regio** | Brazilië |
| **Documenttypen** | Factuur (Nota Fiscal Eletrônica) |
| **Formaat** | XML |
| **Standaard** | NF-e 4.0 (Nota Fiscal Eletrônica — goederen & interstatelijk handelsverkeer) |
| **Taal** | `pt_BR` |

NF-e (Nota Fiscal Eletrônica, `<mod>55</mod>`) is de Braziliaanse elektronische factuur voor goederen en interstatelijk handelsverkeer, gereguleerd door SEFAZ. Elke NF-e bevat een unieke 44-cijferige toegangssleutel (`chNFe`), gedetailleerde productregelitems en meerlaagse belastinggegevens (ICMS, IPI, PIS, COFINS). DocBits classificeert NF-e door de naamruimte `http://www.portalfiscal.inf.br/nfe` te detecteren.

## Ondersteuningsstatus

| Component | Status |
|-----------|--------|
| Voorbeeld | ✅ Ondersteund |
| Veldextractie | ✅ Ondersteund |
| Transformatie | ✅ Ondersteund |

## Standaard Voorbeeld

<figure><img src="brazil-nfe-preview.png" alt="Brazil NF-e voorbeeld in DocBits"><figcaption><p>Standaard DocBits-voorbeeld voor een BRAZIL NF-E document</p></figcaption></figure>

## Veldmapping

### Kopvelden

| DocBits Veld | Bron XPath | Opmerkingen |
|---|---|---|
| `invoice_id` | `//*[local-name()='ide']/*[local-name()='nNF']` | Nota Fiscal-nummer |
| `invoice_date` | `//*[local-name()='ide']/*[local-name()='dhEmi']` | ISO 8601 met BRT-offset |
| `currency` | Vast: `BRL` | Altijd Braziliaanse Real |
| `total_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vNF']` | Totale NF-e-waarde |
| `net_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vProd']` | Totale productwaarde |
| `tax_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vICMS']` | ICMS-belastingtotaal |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']` | Naam van de uitgevende onderneming |
| `supplier_id` | `//*[local-name()='emit']/*[local-name()='CNPJ']` of `CPF` | CNPJ (14 cijfers) of CPF (11 cijfers) |
| `buyer_name` | `//*[local-name()='dest']/*[local-name()='xNome']` | Naam van de ontvangende onderneming |
| `buyer_id` | `//*[local-name()='dest']/*[local-name()='CNPJ']` of `CPF` | CNPJ of CPF |

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
| `PIS_AMOUNT` | `*[local-name()='imposto']/*[local-name()='PIS']//*[local-name()='vPIS']` | PIS-belasting per regel |
| `COFINS_AMOUNT` | `*[local-name()='imposto']/*[local-name()='COFINS']//*[local-name()='vCOFINS']` | COFINS-belasting per regel |
| `VAT_RATE` | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='pICMS']` | ICMS-tarief (%) |

## Classificatieregel

DocBits detecteert BRAZIL NF-E documenten door te controleren op de tekenreeks:

```
http://www.portalfiscal.inf.br/nfe
```

in de XML-naamruimte (`mod=55` voor NF-e, `mod=65` voor NFC-e worden afzonderlijk onderscheiden).

## Gerelateerd

- [BRAZIL NFC-E](brazil-nfce.md)
- [BRAZIL CT-E](brazil-cte.md)
- [BRAZIL NFS-E](brazil-nfse.md)
- [Ondersteunde elektronische documenten](./)
