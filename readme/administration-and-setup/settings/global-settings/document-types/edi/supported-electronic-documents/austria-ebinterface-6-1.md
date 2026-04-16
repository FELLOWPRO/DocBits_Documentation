---
description: Podrška za elektronski dokument AUSTRIA EBINTERFACE 6.1 u DocBits
---

# 🇦🇹 AUSTRIA EBINTERFACE 6.1

| Svojstvo | Vrednost |
|----------|-------|
| **Zemlja/Regija** | Austrija |
| **Tipovi dokumenata** | Faktura, Knjižno odobrenje |
| **Format** | XML |
| **Standard** | ebInterface 6.1 |
| **Locale** | `de_AT` |

ebInterface 6.1 je najnovija verzija austrijskog standarda za elektronsko fakturisanje. Uključuje ažurirana pravila validacije, poboljšanu podršku za knjižna odobrenja i proširenu kompatibilnost sa Peppol mrežom za prekogranično fakturisanje. Imenski prostor je `http://www.ebinterface.at/schema/6p1/`.

## Status podrške

| Komponenta | Status |
|-----------|--------|
| Pregled | ✅ Podržano |
| Mapiranje polja | ✅ Podržano |
| Transformacija | ✅ Podržano |

## Podrazumevani pregled

<figure><img src="austria-ebinterface-preview.png" alt="Pregled fakture Austria ebInterface 6.1 u DocBits"><figcaption><p>Podrazumevani DocBits pregled za AUSTRIA EBINTERFACE 6.1 fakturu</p></figcaption></figure>

## Mapiranje polja

### Polja zaglavlja

| DocBits polje | Izvorni XML element | Napomene |
|---|---|---|
| `invoice_id` | `eb:InvoiceNumber` | Broj fakture |
| `invoice_date` | `eb:InvoiceDate` | ISO 8601 datum |
| `due_date` | `eb:PaymentConditions/eb:DueDate` | Datum dospijeća |
| `delivery_date` | `eb:Delivery/eb:Date` | Datum isporuke |
| `currency` | `@eb:InvoiceCurrency` | Koreni atribut, uvek `EUR` za AT |
| `total_amount` | `eb:TotalGrossAmount` | Bruto ukupno sa PDV |
| `net_amount` | `eb:Tax/eb:VAT/eb:VATItem/eb:TaxedAmount` | Neto poreska osnovica |
| `tax_amount` | `eb:Tax/eb:VAT/eb:VATItem/eb:Amount` | Iznos PDV |
| `purchase_order` | `eb:OrderReference/eb:OrderID` | Referenca naloga za nabavku |
| `payment_terms` | `eb:PaymentConditions/eb:Comment` | Uslovi plaćanja u slobodnom tekstu |
| `supplier_name` | `eb:Biller/eb:Address/eb:Name` | Naziv firme izdavaoca |
| `supplier_tax_id` | `eb:Biller/eb:VATIdentificationNumber` | Austrijski UID (npr. ATU12345678) |
| `supplier_street` | `eb:Biller/eb:Address/eb:Street` | Ulica izdavaoca |
| `supplier_city` | `eb:Biller/eb:Address/eb:Town` | Grad izdavaoca |
| `supplier_postal_code` | `eb:Biller/eb:Address/eb:ZIP` | Poštanski broj izdavaoca |
| `supplier_country` | `eb:Biller/eb:Address/eb:Country/@eb:CountryCode` | ISO kod zemlje |
| `supplier_email` | `eb:Biller/eb:Address/eb:Email` | E-pošta izdavaoca |
| `supplier_iban` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:IBAN` | IBAN izdavaoca |
| `customer_name` | `eb:InvoiceRecipient/eb:Address/eb:Name` | Naziv firme primaoca |
| `customer_tax_id` | `eb:InvoiceRecipient/eb:VATIdentificationNumber` | UID primaoca |
| `customer_street` | `eb:InvoiceRecipient/eb:Address/eb:Street` | Ulica primaoca |
| `customer_city` | `eb:InvoiceRecipient/eb:Address/eb:Town` | Grad primaoca |
| `customer_postal_code` | `eb:InvoiceRecipient/eb:Address/eb:ZIP` | Poštanski broj primaoca |
| `customer_country` | `eb:InvoiceRecipient/eb:Address/eb:Country/@eb:CountryCode` | ISO kod zemlje |
| `iban` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:IBAN` | IBAN za plaćanje |
| `bic` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:BIC` | BIC/SWIFT za plaćanje |

### Tabela stavki (`INVOICE_TABLE`)

Putanja redova: `eb:Details/eb:ItemList/eb:ListLineItem`

| Kolona | Izvorni XML element | Napomene |
|---|---|---|
| `POSITION` | Sekvencijalni indeks | Broj reda od 1 |
| `DESCRIPTION` | `eb:Description` | Opis proizvoda/usluge |
| `QUANTITY` | `eb:Quantity` | Numerička količina |
| `UNIT` | `eb:Quantity/@eb:Unit` | Šifra jedinice (npr. `STK` = komad) |
| `UNIT_PRICE` | `eb:UnitPrice` | Jedinična cena bez PDV |
| `VAT_RATE` | `eb:VAT/eb:VATItem/eb:VATRate` | Stopa PDV u % |
| `VAT` | `eb:VAT/eb:VATItem/eb:TaxedAmount` | Iznos PDV po red |
| `NET_AMOUNT` | `eb:LineItemAmount` | Ukupno red bez PDV |

## Pravilo klasifikacije

DocBits otkriva dokumente AUSTRIA EBINTERFACE 6.1 na osnovu niza imenskog prostora:

```
http://www.ebinterface.at/schema/6p1/
```

## Povezano

- [Podržani elektronski dokumenti](./)
- [Austria ebInterface](austria-ebinterface.md)
- [Austria ebInterface 6.0](austria-ebinterface-6-0.md)