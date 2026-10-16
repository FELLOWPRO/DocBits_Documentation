---
description: Unterstützung für elektronisches Dokument AUNZ PINT in DocBits
---

# 🇦🇺 AUNZ PINT

| Eigenschaft | Wert |
|----------|-------|
| **Land/Regio** | Australien / Neuseeland |
| **Dokumenttypen** | Rechnung, Gutschrift |
| **Format** | UBL 2.1 XML |
| **Standard** | PINT A-NZ (Peppol International Model for Australia-New Zealand) |
| **Locale** | `en_AU` |

AUNZ PINT ist die australische/neuseeländische Implementierung des Peppol International (PINT) Rechnungsmodells. Es definiert ein UBL 2.1-basiertes Rechnungsformat, das auf die A-NZ-regulatorischen Anforderungen zugeschnitten ist, einschließlich ABN/NZBN-Identifikation, GST-Abwicklung und Konformität mit den A-NZ Peppol Authority-Spezifikationen. DocBits unterstützt sowohl die Standard-Rechnungs- als auch die Gutschrift-Dokumenttypen unter dem elektronischen Dokumenttyp `PINT A-NZ` sowie die Self-Billing-Variante.

## Unterstützungsstatus

| Komponente | Status |
|-----------|--------|
| Vorschau | ✅ Unterstützt |
| Feldextraktion | ✅ Unterstützt |
| Transformation | ✅ Unterstützt |

## Standardvorschau

<figure><img src="aunz-pint-preview.png" alt="AUNZ PINT Rechnungsvorschau in DocBits"><figcaption><p>Standard-DocBits-Vorschau für eine AUNZ PINT-Rechnung</p></figcaption></figure>

## Feldzuordnung

### Kopffelder

| DocBits-Feld | Quell-XPath (UBL 2.1) | Hinweise |
|---|---|---|
| `invoice_id` | `cbc:ID` | Rechnungsnummer |
| `invoice_date` | `cbc:IssueDate` | ISO 8601-Datum |
| `due_date` | `cbc:DueDate` | Fälligkeitsdatum |
| `currency` | `cbc:DocumentCurrencyCode` | Typischerweise `AUD` oder `NZD` |
| `total_amount` | `cbc:PayableAmount` (in `cac:LegalMonetaryTotal`) | Gesamtsumme inkl. GST |
| `net_amount` | `cbc:TaxExclusiveAmount` (in `cac:LegalMonetaryTotal`) | Zwischensumme excl. GST |
| `tax_amount` | `cbc:TaxAmount` (in `cac:TaxTotal`) | GST-Betrag |
| `purchase_order` | `cbc:BuyerReference` | Bestellreferenz des Käufers |
| `payment_terms` | `cbc:Note` (in `cac:PaymentTerms`) | Zahlungshinweise als Freitext |
| `supplier_name` | `cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` | Lieferantenname |
| `supplier_id` | `cac:AccountingSupplierParty/cac:Party/cbc:EndpointID` | ABN (schemeID 0151) |
| `supplier_tax_id` | `cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | ABN oder GST-Nummer |
| `supplier_street` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName` | Lieferantenstraße |
| `supplier_city` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:CityName` | Lieferantenort |
| `supplier_postal_code` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:PostalZone` | Lieferanten-PLZ |
| `supplier_country` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode` | ISO-Ländercode (`AU` oder `NZ`) |
| `buyer_name` | `cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` | Käufer-Firmenname |
| `buyer_id` | `cac:AccountingCustomerParty/cac:Party/cbc:EndpointID` | ABN/NZBN (schemeID 0151) |
| `buyer_street` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName` | Käuferstraße |
| `buyer_city` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName` | Käuferort |
| `buyer_postal_code` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:PostalZone` | Käufer-PLZ |
| `buyer_country` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode` | ISO-Ländercode |
| `iban` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` | Zahlungskonto-ID |

### Positionsregeltabelle (`INVOICE_TABLE`)

Zeilenpfad: `cac:InvoiceLine`

| Spalte | Quell-XPath (UBL 2.1) | Hinweise |
|---|---|---|
| `POSITION` | `cbc:ID` | Positionsnummer |
| `DESCRIPTION` | `cac:Item/cbc:Description` | Produkt-/Dienstleistungsbeschreibung |
| `QUANTITY` | `cbc:InvoicedQuantity` | Menge (Einheitencode in `@unitCode`) |
| `UNIT` | `cbc:InvoicedQuantity/@unitCode` | Einheitencode (z.B. `C62` = Stück, `EA` = je) |
| `UNIT_PRICE` | `cac:Price/cbc:PriceAmount` | Einzelpreis excl. GST |
| `VAT_RATE` | `cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` | GST-Satz in % |
| `VAT` | *(berechnet aus Steuerbetrag)* | GST-Betrag pro Zeile |
| `NET_AMOUNT` | `cbc:LineExtensionAmount` | Zeilensumme excl. GST |

## Klassifikationsregel

DocBits erkennt PINT A-NZ-Dokumente durch Abgleich des `CustomizationID`-Elements:

| Muster | Regeltyp | Elektronischer Dokumenttyp |
|---------|-----------|--------------------------|
| `urn:peppol.org:pint:billing-1@aunz` | STRING_CONTAINS | PINT A-NZ (Rechnung) |
| `urn:peppol.org:pint:selfbilling-1@aunz` | STRING_CONTAINS | PINT A-NZ (Self-Billing-Rechnung) |

Beide Muster werden unter dem elektronischen Dokumenttyp `PINT A-NZ` klassifiziert. Das Wurzelelement ist `<Invoice>` für Standardrechnungen und `<CreditNote>` für Gutschriften.

### A-NZ-spezifische Funktionen

- **ABN/NZBN-Identifikatoren**: Verwendet `schemeID="0151"` für Australian Business Numbers und New Zealand Business Numbers
- **GST-Steuer**: Verwendet die `S` (Standard rated) Steuerkategorie mit dem GST-Steuerschema
- **CustomizationID**: Muss das Suffix `@aunz` enthalten, um als PINT A-NZ klassifiziert zu werden (vs. globales PINT)

## Verwandt

- [AUNZ PINT Self-Billing](aunz-pint-self-billing.md)
- [PINT A-NZ](pint-a-nz.md)
- [Unterstützte elektronische Dokumente](./)