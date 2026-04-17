---
description: Ondersteuning voor China Fapiao (FAPIAO, E-FAPIAO, Algemene BTW-factuur, Bijzondere BTW-factuur) elektronische documenten in DocBits
---

# 🇨🇳 China Fapiao

| Eigenschap | Waarde |
|----------|-------|
| **Land / Regio** | China |
| **Documenttypen** | Algemene BTW-factuur (普通发票), Bijzondere BTW-factuur (专用发票), E-Fapiao |
| **Formaat** | XML |
| **Standaard** | Fapiao (发票), State Taxation Administration |
| **Landinstelling** | `zh_CN` |

Fapiao (发票) is de Chinese belastingfactuurstandaard uitgegeven onder de autoriteit van de State Taxation Administration (STA / 国家税务总局). Alle Fapiao-documenten delen de naamruimte `urn:china:tax:fapiao:1.0`. DocBits detecteert automatisch het Fapiao-type via het element `fapiao_type` en leidt dit naar de juiste extractieregels:

| Waarde fapiao_type | Documenttype |
|-------------------|--------------|
| 普通发票 | Algemene BTW-factuur (FAPIAO / GENERAL VAT INVOICE) |
| 专用发票 | Bijzondere BTW-factuur (SPECIAL VAT INVOICE) |
| 电子发票 | E-Fapiao (E-FAPIAO) |

## Ondersteuningsstatus

| Component | Status |
|-----------|--------|
| Voorvertoning | ✅ Supported |
| Veldextractie | ✅ Supported |
| Transformatie | ✅ Supported |

## Standaardvoorvertoning

<figure><img src="china-fapiao-preview.png" alt="Voorvertoning China Fapiao Algemene BTW-factuur in DocBits"><figcaption><p>Standaard DocBits-voorvertoning voor een China Fapiao Algemene BTW-factuur (普通发票)</p></figcaption></figure>

## Veldkoppeling

### Headervelden

| DocBits-veld | Bron-XML-element | Opmerkingen |
|---|---|---|
| `invoice_id` | `fapiao_head/fapiao_number` | Fapiao-nummer — 8 cijfers (发票号码) |
| `invoice_date` | `fapiao_head/issue_date` | Uitgiftedatum (ISO 8601) |
| `currency` | Vast: `CNY` | Altijd Chinese Yuan Renminbi |
| `total_amount` | `total/total_with_tax` | Totaalbedrag incl. BTW (价税合计) |
| `net_amount` | `total/total_amount` | Netto belastbaar bedrag excl. BTW (金额) |
| `tax_amount` | `total/total_tax` | Totaal BTW-bedrag (税额) |
| `supplier_name` | `seller/name` | Naam van het verkopende bedrijf (销售方名称) |
| `supplier_id` | `seller/taxpayer_id` | BTW-nummer verkoper — 18 tekens (纳税人识别号) |
| `supplier_address` | `seller/address` | Adres verkoper |
| `supplier_country` | Vast: `CN` | Altijd China |
| `iban` | `seller/bank_account` | Bankrekeningnummer verkoper |
| `buyer_name` | `buyer/name` | Naam van het kopende bedrijf (购买方名称) |
| `buyer_id` | `buyer/taxpayer_id` | BTW-nummer koper (纳税人识别号) |
| `buyer_address` | `buyer/address` | Adres koper |
| `buyer_country` | Vast: `CN` | Altijd China |

### Regelitemtabel (`INVOICE_TABLE`)

Regelpad: `items/item`

| Kolom | Bron-XML-element | Opmerkingen |
|---|---|---|
| `POSITION` | `seq` | Regelvolgordernummer |
| `DESCRIPTION` | `name` + `spec` | Artikelnaam en specificatie (samengevoegd) |
| `QUANTITY` | `quantity` | Hoeveelheid |
| `UNIT` | `unit` | Maateenheid (bijv. 箱, 台, 项) |
| `UNIT_PRICE` | `unit_price` | Eenheidsprijs excl. BTW |
| `VAT_RATE` | `tax_rate` | BTW-tarief in % (doorgaans 6%, 9% of 13%) |
| `VAT` | `tax_amount` | BTW-bedrag per regel |
| `NET_AMOUNT` | `amount` | Regeltotaal excl. BTW |

## Classificatieregels

DocBits detecteert China Fapiao-documenten door de XML-naamruimte en `fapiao_type` te matchen:

| Type elektronisch document | Patroon |
|--------------------------|---------|
| CHINA GENERAL VAT INVOICE | `urn:china:tax:fapiao:1.0` + `<fapiao_type>普通发票</fapiao_type>` |
| CHINA SPECIAL VAT INVOICE | `urn:china:tax:fapiao:1.0` + `<fapiao_type>专用发票</fapiao_type>` |
| CHINA E-FAPIAO | `urn:china:tax:fapiao:1.0` + `<fapiao_type>电子发票</fapiao_type>` |

Het rootelement is `<fapiao>` met naamruimte `urn:china:tax:fapiao:1.0`. Classificatie gebruikt het principe **first-match-wins**, gesorteerd op patroonlengte (langste eerst).

## Gerelateerd

- [Momenteel ondersteunde e-factuurstandaarden](../../currently-supported-e-invoice-standards/)
- [Ondersteunde elektronische documenten](./)
