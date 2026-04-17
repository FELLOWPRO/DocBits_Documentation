---
description: Podrška za indijsku GST e-fakturu u DocBits-u
---

# 🇮🇳 India GST E-Invoice

| Svojstvo | Vrednost |
|----------|-------|
| **Zemlja / Region** | Indija |
| **Tipovi dokumenata** | Faktura (INV), Kreditna nota (CRN), Debitna nota (DBN) |
| **Format** | XML (`<SignedInvoice>`) |
| **Standard** | GST E-Invoice (GSTN Invoice Registration Portal) |
| **Locale** | `en_IN` |

Indijska GST e-faktura je obavezni standard elektronskog fakturisanja u okviru indijskog GST (Goods and Services Tax) sistema, koji upravlja GSTN (GST Network). Preduzeća koja prelaze propisani prag prometa moraju generisati e-fakture putem IRP (Invoice Registration Portal), koji potpisuje fakturu i vraća **IRN** (Invoice Reference Number — SHA-256 hash od 64 karaktera) i QR kod.

DocBits detektuje GST E-Invoice dokumente prisustvom `<SignedInvoice>` kao korenskog elementa. Format uključuje tri GST poreske komponente:

| Poreska komponenta | Opis |
|--------------|-------------|
| IGST | Integrisani GST — primenjuje se na međudržavne transakcije |
| CGST | Centralni GST — primenjuje se na transakcije unutar države (centralna komponenta) |
| SGST | Državni GST — primenjuje se na transakcije unutar države (državna komponenta) |

Identifikator poreskog obveznika je **GSTIN** (Goods and Services Tax Identification Number), alfanumerički kod od 15 karaktera u formatu `29AABCU9603R1ZM` (2-cifreni kod države + 10-cifreni PAN + broj entiteta + kontrolna cifra). Datumi koriste format `DD/MM/GGGG`.

## Status podrške

| Komponenta | Status |
|-----------|--------|
| Pregled | ✅ Podržano |
| Ekstrakcija polja | ✅ Podržano |
| Transformacija | ✅ Podržano |

## Podrazumevani pregled

<figure><img src="india-gst-e-invoice-preview.png" alt="India GST E-Invoice preview in DocBits"><figcaption><p>Podrazumevani DocBits pregled za indijsku GST e-fakturu</p></figcaption></figure>

## Mapiranje polja

### Polja zaglavlja

| DocBits polje | Izvorni XML element | Napomene |
|---|---|---|
| `invoice_id` | `Invoice/DocDtls/No` | Broj fakture |
| `invoice_date` | `Invoice/DocDtls/Dt` | Datum izdavanja (`DD/MM/GGGG`) |
| `invoice_type` | `Invoice/DocDtls/Typ` | INV=Faktura, CRN=Kreditna nota, DBN=Debitna nota |
| `currency` | Fiksno: `INR` | Uvek indijska rupija |
| `net_amount` | `Invoice/ValDtls/AssVal` | Oporeziva / procenjena vrednost |
| `tax_amount` | `Invoice/ValDtls/IgstVal` + `CgstVal` + `SgstVal` | Ukupan iznos GST-a |
| `total_amount` | `Invoice/ValDtls/TotInvVal` | Ukupna vrednost fakture uklj. GST |
| `igst_amount` | `Invoice/ValDtls/IgstVal` | Iznos integrisanog GST-a |
| `cgst_amount` | `Invoice/ValDtls/CgstVal` | Iznos centralnog GST-a |
| `sgst_amount` | `Invoice/ValDtls/SgstVal` | Iznos državnog GST-a |
| `cess_amount` | `Invoice/ValDtls/CesVal` | Iznos cesa (ako je primenjivo) |
| `supplier_name` | `Invoice/SellerDtls/LglNm` | Pravno ime prodavca |
| `supplier_id` | `Invoice/SellerDtls/Gstin` | GSTIN prodavca (15 karaktera, npr. `29AABCU9603R1ZM`) |
| `supplier_trade_name` | `Invoice/SellerDtls/TrdNm` | Trgovačko ime prodavca |
| `supplier_address` | `Invoice/SellerDtls/Addr1` | Adresa prodavca red 1 |
| `supplier_city` | `Invoice/SellerDtls/Loc` | Grad / lokacija prodavca |
| `supplier_postal_code` | `Invoice/SellerDtls/Pin` | PIN kod prodavca |
| `supplier_state_code` | `Invoice/SellerDtls/Stcd` | Kod države prodavca (2 cifre) |
| `buyer_name` | `Invoice/BuyerDtls/LglNm` | Pravno ime kupca |
| `buyer_id` | `Invoice/BuyerDtls/Gstin` | GSTIN kupca |
| `buyer_trade_name` | `Invoice/BuyerDtls/TrdNm` | Trgovačko ime kupca |
| `buyer_address` | `Invoice/BuyerDtls/Addr1` | Adresa kupca red 1 |
| `buyer_city` | `Invoice/BuyerDtls/Loc` | Grad / lokacija kupca |
| `buyer_postal_code` | `Invoice/BuyerDtls/Pin` | PIN kod kupca |
| `buyer_state_code` | `Invoice/BuyerDtls/Stcd` | Kod države kupca |
| `irn` | `Irn` | Referentni broj fakture (SHA-256 hash od 64 karaktera) |
| `ack_number` | `AckNo` | IRP broj potvrde |
| `ack_date` | `AckDt` | IRP datum potvrde |

### Tabela stavki (`INVOICE_TABLE`)

Putanja reda: `Invoice/ItemList/Item`

| Kolona | Izvorni XML element | Napomene |
|---|---|---|
| `POSITION` | `SlNo` | Redni broj stavke |
| `DESCRIPTION` | `PrdDesc` | Opis proizvoda / usluge |
| `QUANTITY` | `Qty` | Fakturisana količina |
| `UNIT` | `Unit` | Jedinica mere (npr. `OTH`, `NOS`, `KGS`) |
| `UNIT_PRICE` | `UnitPrice` | Jedinična cena |
| `VAT_RATE` | `GstRt` | Stopa GST u % (npr. 18%) |
| `VAT` | `IgstAmt` (ili `CgstAmt` + `SgstAmt`) | Iznos GST po stavci |
| `NET_AMOUNT` | `AssAmt` | Oporezivi iznos po stavci |

## Pravilo klasifikacije

DocBits detektuje India GST E-Invoice dokumente podudaranjem korenskog elementa:

| Tip elektronskog dokumenta | Obrazac |
|--------------------------|---------|
| INDIA GST E-INVOICE | Korenski element sadrži `<SignedInvoice` |

## Povezano

- [Trenutno podržani standardi e-fakture](../../currently-supported-e-invoice-standards/)
- [Podržani elektronski dokumenti](./)
