---
description: Podrška za danski OIOUBL 2.1 elektronski dokument u DocBits-u
---

# 🇩🇰 Denmark OIOUBL 2.1

| Svojstvo | Vrednost |
|----------|-------|
| **Zemlja / Region** | Danska |
| **Vrste dokumenata** | Faktura (Faktura), Kreditna nota |
| **Format** | XML (UBL 2.1) |
| **Standard** | OIOUBL 2.1 (Offentlig Information Online UBL) |
| **Lokalizacija** | `da_DK` |

OIOUBL (Offentlig Information Online UBL) je danski standard za e-fakture zasnovan na UBL 2.1. Obavezan je za fakture upućene subjektima javnog sektora u Danskoj i široko se koristi u B2B transakcijama. DocBits prepoznaje OIOUBL 2.1 dokumente po prisustvu `<cbc:CustomizationID>OIOUBL-2.1</cbc:CustomizationID>`. Identifikator profila `urn:www.nesubl.eu:profiles:profile5:ver2.0` označava NES (Severno-evropski podzup) profil fakture.

## Status podrške

| Komponenta | Status |
|-----------|--------|
| Pregled | ✅ Podržano |
| Ekstrakcija polja | ✅ Podržano |
| Transformacija | ✅ Podržano |

## Podrazumevani pregled

<figure><img src="denmark-oioubl-preview.png" alt="Denmark OIOUBL 2.1 invoice preview in DocBits"><figcaption><p>Podrazumevani DocBits pregled za danski OIOUBL 2.1 račun (Faktura)</p></figcaption></figure>

## Mapiranje polja

### Zaglavlje polja

| Polje u DocBits-u | Izvorni XML element | Napomene |
|---|---|---|
| `invoice_id` | `cbc:ID` | Broj fakture |
| `invoice_date` | `cbc:IssueDate` | Datum izdavanja u ISO 8601 formatu |
| `due_date` | `cbc:DueDate` | Rok plaćanja |
| `invoice_type` | `cbc:InvoiceTypeCode` | UNCL 1001 šifra (380=Faktura, 381=Kreditna nota) |
| `currency` | `cbc:DocumentCurrencyCode` | Uvek `DKK` (danska kruna) |
| `purchase_order` | `cac:OrderReference/cbc:ID` | Referentni broj narudžbenice kupca |
| `buyer_reference` | `cbc:BuyerReference` | Interna referenca kupca / EAN lokacijski broj |
| `note` | `cbc:Note` | Slobodan tekst sa uputstvima za plaćanje ili napomenama |
| `net_amount` | `cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` | Neto iznos bez PDV-a |
| `tax_amount` | `cac:TaxTotal/cbc:TaxAmount` | Ukupan iznos PDV-a (standardna stopa 25%) |
| `total_amount` | `cac:LegalMonetaryTotal/cbc:PayableAmount` | Ukupan iznos sa PDV-om |
| `tax_rate` | `cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent` | Stopa PDV-a u % |
| `supplier_name` | `cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` | Naziv kompanije dobavljača |
| `supplier_id` | `cac:AccountingSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID` | CVR broj (npr. `DK12345678`) |
| `supplier_vat` | `cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | PDV/CVR broj |
| `supplier_address` | `cac:AccountingSupplierParty/.../cbc:StreetName` | Adresa dobavljača |
| `supplier_city` | `cac:AccountingSupplierParty/.../cbc:CityName` | Grad dobavljača |
| `supplier_postal_code` | `cac:AccountingSupplierParty/.../cbc:PostalZone` | Poštanski broj dobavljača |
| `supplier_country` | `cac:AccountingSupplierParty/.../cbc:IdentificationCode` | ISO šifra zemlje (`DK`) |
| `customer_name` | `cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` | Naziv kompanije kupca |
| `customer_id` | `cac:AccountingCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` | CVR broj |
| `customer_vat` | `cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | PDV/CVR broj |
| `customer_address` | `cac:AccountingCustomerParty/.../cbc:StreetName` | Adresa kupca |
| `customer_city` | `cac:AccountingCustomerParty/.../cbc:CityName` | Grad kupca |
| `customer_postal_code` | `cac:AccountingCustomerParty/.../cbc:PostalZone` | Poštanski broj kupca |
| `customer_country` | `cac:AccountingCustomerParty/.../cbc:IdentificationCode` | ISO šifra zemlje (`DK`) |
| `iban` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` | Bankovni račun / IBAN |
| `bic` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cbc:ID` | BIC/SWIFT kod |

### Tabela stavki (`INVOICE_TABLE`)

Putanja reda: `cac:InvoiceLine`

| Kolona | Izvorni XML element | Napomene |
|---|---|---|
| `POSITION` | `cbc:ID` | Redni broj stavke |
| `DESCRIPTION` | `cac:Item/cbc:Name` | Naziv/opis artikla |
| `QUANTITY` | `cbc:InvoicedQuantity` | Fakturisana količina |
| `UNIT_PRICE` | `cac:Price/cbc:PriceAmount` | Jedinična cena bez PDV-a |
| `NET_AMOUNT` | `cbc:LineExtensionAmount` | Ukupan iznos stavke bez PDV-a |

## Pravilo klasifikacije

DocBits prepoznaje OIOUBL 2.1 dokumente podudaranjem elementa `CustomizationID`:

| Tip elektronskog dokumenta | Obrazac |
|--------------------------|---------|
| OIOUBL 2.1 | `<cbc:CustomizationID>OIOUBL-2\.1\s*</cbc:CustomizationID>` |

Korenski element je `<Invoice>` (ili `<CreditNote>`) u UBL 2.1 imenskom prostoru `urn:oasis:names:specification:ubl:schema:xsd:Invoice-2`.

## Srodni resursi

- [Trenutno podržani standardi e-faktura](../../currently-supported-e-invoice-standards/)
- [Podržani elektronski dokumenti](./)
