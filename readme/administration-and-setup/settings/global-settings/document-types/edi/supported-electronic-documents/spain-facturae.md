---
description: Španija Facturae (3.2, 3.2.1, 3.2.2) – Podrška za elektronske dokumente u DocBits-u
---

# 🇪🇸 Španija Facturae

| Svojstvo | Vrednost |
|----------|----------|
| **Zemlja / Region** | Španija |
| **Tipovi dokumenata** | Faktura (Factura), Kreditna nota |
| **Format** | XML |
| **Standard** | Facturae 3.2 / 3.2.1 / 3.2.2 (Agencia Tributaria / AEAT) |
| **Lokalizacija** | `es_ES` |

Facturae je obavezni španski standard za elektronsko fakturisanje, kojim upravljaju Agencia Estatal de Administración Tributaria (AEAT) i Ministarstvo finansija. Obavezan je za fakture upućene španskim javnim institucijama i široko se koristi u B2B transakcijama. Korenski element je `<fe:Facturae>` sa verzioniranim URL-om prostora imena. DocBits detektuje verziju putem atributa `xsi:schemaLocation`, koji upućuje na jedan od zvaničnih URL-ova šeme:

| Verzija | URL šeme |
|---------|---------|
| Facturae 3.2 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2.xml` |
| Facturae 3.2.1 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2_1.xml` |
| Facturae 3.2.2 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2_2.xml` |

## Status podrške

| Komponenta | Status |
|-----------|--------|
| Pregled | ✅ Podržano |
| Ekstrakcija polja | ✅ Podržano |
| Transformacija | ✅ Podržano |

## Podrazumevani pregled

<figure><img src="spain-facturae-preview.png" alt="Pregled fakture Španija Facturae u DocBits-u"><figcaption><p>Podrazumevani pregled u DocBits-u za fakturu Španija Facturae 3.2.2</p></figcaption></figure>

## Mapiranje polja

### Polja zaglavlja

| DocBits polje | Izvorni XML element | Napomene |
|---|---|---|
| `invoice_id` | `Invoices/Invoice/InvoiceHeader/InvoiceNumber` | Broj fakture |
| `invoice_date` | `Invoices/Invoice/InvoiceIssueData/IssueDate` | Datum izdavanja (GGGG-MM-DD) |
| `due_date` | `PaymentDetails/Installment/InstallmentDueDate` | Rok plaćanja |
| `invoice_type` | `Invoices/Invoice/InvoiceHeader/InvoiceDocumentType` | FC=Faktura, NC=Kreditna nota |
| `currency` | `Invoices/Invoice/InvoiceIssueData/InvoiceCurrencyCode` | Uvek `EUR` |
| `purchase_order` | `Invoices/Invoice/InvoiceHeader/ReceiverContractReference` | Referenca porudžbine / ugovora kupca |
| `net_amount` | `Invoices/Invoice/InvoiceTotals/TotalGrossAmountBeforeTaxes` | Neto iznos bez PDV-a |
| `tax_amount` | `Invoices/Invoice/InvoiceTotals/TotalTaxOutputs` | Ukupan PDV |
| `total_amount` | `Invoices/Invoice/InvoiceTotals/InvoiceTotal` | Ukupan iznos sa PDV-om |
| `tax_rate` | `TaxesOutputs/Tax/TaxRate` | Stopa PDV-a u % (standardna 21%) |
| `payment_terms` | `PaymentDetails/Installment/PaymentMeans` | Kod načina plaćanja |
| `supplier_name` | `Parties/SellerParty/LegalEntity/CorporateName` | Naziv dobavljača |
| `supplier_id` | `Parties/SellerParty/TaxIdentification/TaxIdentificationNumber` | NIF/CIF (npr. `ES12345678A`) |
| `supplier_tax_id` | `Parties/SellerParty/TaxIdentification/TaxIdentificationNumber` | Španski NIF ili CIF |
| `supplier_address` | `Parties/SellerParty/LegalEntity/AddressInSpain/Address` | Adresa dobavljača |
| `supplier_city` | `Parties/SellerParty/LegalEntity/AddressInSpain/Town` | Grad dobavljača |
| `supplier_postal_code` | `Parties/SellerParty/LegalEntity/AddressInSpain/PostCode` | Poštanski broj dobavljača |
| `supplier_country` | `Parties/SellerParty/LegalEntity/AddressInSpain/CountryCode` | ISO kod zemlje (`ESP`) |
| `buyer_name` | `Parties/BuyerParty/LegalEntity/CorporateName` | Naziv kupca |
| `buyer_id` | `Parties/BuyerParty/TaxIdentification/TaxIdentificationNumber` | NIF/CIF kupca |
| `buyer_address` | `Parties/BuyerParty/LegalEntity/AddressInSpain/Address` | Adresa kupca |
| `buyer_city` | `Parties/BuyerParty/LegalEntity/AddressInSpain/Town` | Grad kupca |
| `buyer_postal_code` | `Parties/BuyerParty/LegalEntity/AddressInSpain/PostCode` | Poštanski broj kupca |
| `buyer_country` | `Parties/BuyerParty/LegalEntity/AddressInSpain/CountryCode` | ISO kod zemlje (`ESP`) |
| `iban` | `PaymentDetails/Installment/AccountToBeCredited/IBAN` | IBAN primaoca |

### Tabela stavki (`INVOICE_TABLE`)

Putanja reda: `Invoices/Invoice/Items/InvoiceLine`

| Kolona | Izvorni XML element | Napomene |
|---|---|---|
| `POSITION` | `ItemDescription` | Redni broj / opis koji se koristi kao identifikator |
| `DESCRIPTION` | `ItemDescription` | Opis artikla |
| `QUANTITY` | `Quantity` | Fakturisana količina |
| `UNIT` | `UnitOfMeasure` | Jedinica mere (npr. `units`) |
| `UNIT_PRICE` | `UnitPriceWithoutTax` | Jedinična cena bez PDV-a |
| `VAT_RATE` | `TaxesOutputs/Tax/TaxRate` | Stopa PDV-a u % (obično 21%) |
| `VAT` | `TaxesOutputs/Tax/TaxAmount/TotalAmount` | Iznos PDV-a po stavci |
| `NET_AMOUNT` | `TotalCost` | Ukupno po stavci bez PDV-a |

## Pravila klasifikacije

DocBits detektuje Facturae dokumente podudaranjem atributa `xsi:schemaLocation` na korenskom elementu `<fe:Facturae>`:

| Tip elektronskog dokumenta | Obrazac |
|--------------------------|---------|
| FACTURAE 3.2 | `xsi:schemaLocation` sadrži `Facturaev3_2.xml` (ne 3_2_1 ili 3_2_2) |
| FACTURAE 3.2.1 | `xsi:schemaLocation` sadrži `Facturaev3_2_1.xml` |
| FACTURAE 3.2.2 | `xsi:schemaLocation` sadrži `Facturaev3_2_2.xml` |

Korenski element je `<fe:Facturae>` sa prostorom imena `http://www.facturae.es/Facturae/2014/v3.2.2/Facturae` (specifičan za verziju). Klasifikacija koristi princip **prvi pronalazak pobeđuje**, pri čemu se specifičniji obrasci (3.2.2, 3.2.1) proveravaju pre opšteg 3.2.

## Srodni sadržaji

- [Trenutno podržani standardi e-faktura](../../currently-supported-e-invoice-standards/)
- [Podržani elektronski dokumenti](./)
