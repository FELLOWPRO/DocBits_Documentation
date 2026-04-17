---
description: Podrška za elektronske dokumente Finska TEAPPSXML u DocBits-u
---

# 🇫🇮 Finska TEAPPSXML

| Svojstvo | Vrednost |
|----------|-------|
| **Zemlja / Region** | Finska |
| **Tipovi dokumenata** | Faktura, Kreditna nota |
| **Format** | XML |
| **Standard** | TEAPPSXML 3.0 (Tieto / Finski bankarski sektor) |
| **Lokalizacija** | `fi_FI` |

TEAPPSXML (Tietotekniikan ja viestinnän toimiala) je finski standard elektronske fakture koji se koristi prvenstveno u bankarskom i finansijskom sektoru. Koreni element je `<TEAPPSXML>` sa imenskim prostorom `urn:TEAPPSXML:3.0`. DocBits detektuje TEAPPSXML dokumente prisustvom `xmlns="urn:TEAPPSXML:"` u korenom elementu.

Format TEAPPSXML koristi nazive elemenata velikim slovima i ravnu strukturu sa odvojenim sekcijama `<SENDER>`, `<RECEIVER>`, `<INVOICE>` i `<PAYMENTINFO>`. Format finskog poslovnog ID-ja (Y-tunnus) je `1234567-8`, a PDV brojevi koriste prefiks `FI` (npr. `FI12345678`).

## Status podrške

| Komponenta | Status |
|-----------|--------|
| Pregled | ✅ Podržano |
| Ekstrakcija polja | ✅ Podržano |
| Transformacija | ✅ Podržano |

## Podrazumevani pregled

<figure><img src="finland-teappsxml-preview.png" alt="Pregled fakture Finska TEAPPSXML u DocBits-u"><figcaption><p>Podrazumevani pregled u DocBits-u za finsku TEAPPSXML fakturu</p></figcaption></figure>

## Mapiranje polja

### Polja zaglavlja

| Polje DocBits | Izvorni XML element | Napomene |
|---|---|---|
| `invoice_id` | `INVOICE/INVOICENUMBER` | Broj fakture |
| `invoice_date` | `INVOICE/INVOICEDATE` | Datum izdavanja (GGGG-MM-DD) |
| `due_date` | `INVOICE/DUEDATE` | Rok plaćanja (GGGG-MM-DD) |
| `invoice_type` | `INVOICE/INVOICE_TYPE` | Tip poruke (INVOICE) |
| `currency` | `INVOICE/CURRENCY` | Kod valute (obično `EUR`) |
| `purchase_order` | `INVOICE/REFERENCENUMBER` | Referentni broj plaćanja |
| `payment_reference` | `INVOICE/REFERENCENUMBER` | Finska referenca plaćanja (viitenumero) |
| `net_amount` | `INVOICE/TOTALVATEXCLUDED` | Neto iznos bez PDV-a |
| `tax_amount` | `INVOICE/TOTALVAT` | Ukupan iznos PDV-a |
| `total_amount` | `INVOICE/TOTALAMOUNT` | Ukupan iznos sa PDV-om |
| `payment_terms` | `INVOICE/PAYMENT_TERMS` | Metod plaćanja (npr. `BANKTRANSFER`) |
| `supplier_name` | `SENDER/NAME` | Naziv kompanije pošiljaoca |
| `supplier_id` | `SENDER/ID` | Finski poslovni ID (Y-tunnus, npr. `1234567-8`) |
| `supplier_tax_id` | `SENDER/VATNUMBER` | PDV broj (npr. `FI12345678`) |
| `supplier_address` | `SENDER/ADDRESS/STREET` | Adresa pošiljaoca |
| `supplier_city` | `SENDER/ADDRESS/CITY` | Grad pošiljaoca |
| `supplier_postal_code` | `SENDER/ADDRESS/POSTCODE` | Poštanski broj pošiljaoca |
| `supplier_country` | `SENDER/ADDRESS/COUNTRY` | ISO kod države (`FI`) |
| `supplier_bic` | `SENDER/BANK/BIC` | BIC kod banke pošiljaoca |
| `buyer_name` | `INVOICE/BUYER/NAME` | Naziv kompanije kupca |
| `buyer_id` | `INVOICE/BUYER/ID` | Finski poslovni ID kupca |
| `buyer_address` | `INVOICE/BUYER/ADDRESS_LINE_1` | Adresa kupca |
| `buyer_city` | `INVOICE/BUYER/CITY` | Grad kupca |
| `buyer_postal_code` | `INVOICE/BUYER/POSTAL_CODE` | Poštanski broj kupca |
| `buyer_country` | `INVOICE/BUYER/COUNTRY` | ISO kod države (`FI`) |
| `iban` | `PAYMENTINFO/BENEFICIARYACCOUNT/IBAN` | IBAN primaoca |
| `bic` | `PAYMENTINFO/BENEFICIARYACCOUNT/BIC` | BIC kod primaoca |

### Tabela stavki (`INVOICE_TABLE`)

Putanja reda: `INVOICE/LINES/LINE`

| Kolona | Izvorni XML element | Napomene |
|---|---|---|
| `POSITION` | `LINENUMBER` | Redni broj stavke |
| `DESCRIPTION` | `ARTICLENAME` | Naziv / opis artikla |
| `QUANTITY` | `QUANTITY` | Fakturisana količina |
| `UNIT` | `UNIT` | Jedinica mere (npr. `KPL` = komad) |
| `UNIT_PRICE` | `UNITPRICE` | Jedinična cena bez PDV-a |
| `VAT_RATE` | `VATRATE` | Stopa PDV-a u % (standardno 25,5%) |
| `VAT` | Izračunato | Iznos PDV-a po redu |
| `NET_AMOUNT` | `LINEAMOUNT` | Ukupan iznos reda bez PDV-a |

## Pravilo klasifikacije

DocBits detektuje TEAPPSXML dokumente podudaranjem atributa `xmlns` na korenom elementu `<TEAPPSXML>`:

| Tip elektronskog dokumenta | Obrazac |
|--------------------------|---------|
| TEAPPSXML | `xmlns` sadrži `urn:TEAPPSXML:` |

## Srodni sadržaji

- [Trenutno podržani standardi e-fakturisanja](../../currently-supported-e-invoice-standards/)
- [Finska Finvoice](./finland-finvoice.md)
- [Podržani elektronski dokumenti](./)
