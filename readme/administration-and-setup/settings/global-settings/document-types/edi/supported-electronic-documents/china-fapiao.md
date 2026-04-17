---
description: Podrška za kineske elektronske dokumente China Fapiao (FAPIAO, E-FAPIAO, Opšta PDV faktura, Posebna PDV faktura) u DocBits-u
---

# 🇨🇳 China Fapiao

| Svojstvo | Vrednost |
|----------|-------|
| **Zemlja / Region** | China |
| **Vrste dokumenata** | Opšta PDV faktura (普通发票), Posebna PDV faktura (专用发票), E-Fapiao |
| **Format** | XML |
| **Standard** | Fapiao (发票), State Taxation Administration |
| **Lokalizacija** | `zh_CN` |

Fapiao (发票) je kineski standard poreske fakture koji se izdaje pod nadležnošću Državne poreske uprave (STA / 国家税务总局). Svi Fapiao dokumenti dele prostor imena `urn:china:tax:fapiao:1.0`. DocBits automatski prepoznaje tip Fapiao-a putem elementa `fapiao_type` i usmerava ka odgovarajućim pravilima ekstrakcije:

| Vrednost fapiao_type | Vrsta dokumenta |
|-------------------|--------------|
| 普通发票 | Opšta PDV faktura (FAPIAO / GENERAL VAT INVOICE) |
| 专用发票 | Posebna PDV faktura (SPECIAL VAT INVOICE) |
| 电子发票 | E-Fapiao (E-FAPIAO) |

## Status podrške

| Komponenta | Status |
|-----------|--------|
| Pregled | ✅ Supported |
| Ekstrakcija polja | ✅ Supported |
| Transformacija | ✅ Supported |

## Podrazumevani pregled

<figure><img src="china-fapiao-preview.png" alt="Pregled kineske Fapiao opšte PDV fakture u DocBits-u"><figcaption><p>Podrazumevani DocBits pregled kineske Fapiao opšte PDV fakture (普通发票)</p></figcaption></figure>

## Mapiranje polja

### Polja zaglavlja

| DocBits polje | Izvorni XML element | Napomene |
|---|---|---|
| `invoice_id` | `fapiao_head/fapiao_number` | Fapiao broj — 8 cifara (发票号码) |
| `invoice_date` | `fapiao_head/issue_date` | Datum izdavanja (ISO 8601) |
| `currency` | Fiksno: `CNY` | Uvek kineski juan renminbi |
| `total_amount` | `total/total_with_tax` | Ukupan iznos uklj. PDV (价税合计) |
| `net_amount` | `total/total_amount` | Neto oporezivi iznos bez PDV (金额) |
| `tax_amount` | `total/total_tax` | Ukupan iznos PDV (税额) |
| `supplier_name` | `seller/name` | Naziv prodajnog preduzeća (销售方名称) |
| `supplier_id` | `seller/taxpayer_id` | PIB prodavca — 18 znakova (纳税人识别号) |
| `supplier_address` | `seller/address` | Adresa prodavca |
| `supplier_country` | Fiksno: `CN` | Uvek Kina |
| `iban` | `seller/bank_account` | Broj bankovnog računa prodavca |
| `buyer_name` | `buyer/name` | Naziv kupujućeg preduzeća (购买方名称) |
| `buyer_id` | `buyer/taxpayer_id` | PIB kupca (纳税人识别号) |
| `buyer_address` | `buyer/address` | Adresa kupca |
| `buyer_country` | Fiksno: `CN` | Uvek Kina |

### Tabela stavki (`INVOICE_TABLE`)

Putanja reda: `items/item`

| Kolona | Izvorni XML element | Napomene |
|---|---|---|
| `POSITION` | `seq` | Redni broj stavke |
| `DESCRIPTION` | `name` + `spec` | Naziv artikla i specifikacija (spojeni) |
| `QUANTITY` | `quantity` | Količina |
| `UNIT` | `unit` | Jedinica mere (npr. 箱, 台, 项) |
| `UNIT_PRICE` | `unit_price` | Jedinična cena bez PDV |
| `VAT_RATE` | `tax_rate` | Stopa PDV u % (obično 6%, 9% ili 13%) |
| `VAT` | `tax_amount` | Iznos PDV po stavci |
| `NET_AMOUNT` | `amount` | Ukupno po stavci bez PDV |

## Pravila klasifikacije

DocBits prepoznaje China Fapiao dokumente podudaranjem XML prostora imena i `fapiao_type`:

| Vrsta elektronskog dokumenta | Obrazac |
|--------------------------|---------|
| CHINA GENERAL VAT INVOICE | `urn:china:tax:fapiao:1.0` + `<fapiao_type>普通发票</fapiao_type>` |
| CHINA SPECIAL VAT INVOICE | `urn:china:tax:fapiao:1.0` + `<fapiao_type>专用发票</fapiao_type>` |
| CHINA E-FAPIAO | `urn:china:tax:fapiao:1.0` + `<fapiao_type>电子发票</fapiao_type>` |

Koren element je `<fapiao>` sa prostorom imena `urn:china:tax:fapiao:1.0`. Klasifikacija koristi princip **first-match-wins** sortiran po dužini obrasca (najduži prvi).

## Povezano

- [Trenutno podržani standardi e-faktura](../../currently-supported-e-invoice-standards/)
- [Podržani elektronski dokumenti](./)
