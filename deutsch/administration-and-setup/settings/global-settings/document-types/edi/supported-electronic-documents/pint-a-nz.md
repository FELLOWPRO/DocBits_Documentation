---
description: Unterstützung für elektronisches Dokument PINT A-NZ in DocBits
---

# 🇦🇺 PINT A-NZ

| Eigenschaft | Wert |
|----------|-------|
| **Land/Regio** | Australien / Neuseeland |
| **Dokumenttypen** | Rechnung, Gutschrift |
| **Format** | UBL 2.1 XML |
| **Standard** | PINT A-NZ (Peppol International Model for Australia-New Zealand) |
| **Locale** | `en_AU` |

PINT A-NZ (Peppol International Model for Australia-New Zealand) ist die lokalisierte Peppol-Rechnungsspezifikation für die Australien/Neuseeland-Region. Sie erweitert das globale PINT-Modell um A-NZ-spezifische Geschäftsregeln, Steuerkategorien (GST) und Identifikationsschemata (ABN, NZBN). Dies ist die technische Referenzseite mit der vollständigen Feldzuordnung.

## Unterstützungsstatus

| Komponente | Status |
|-----------|--------|
| Vorschau | ✅ Unterstützt |
| Feldextraktion | ✅ Unterstützt |
| Transformation | ✅ Unterstützt |

## Standardvorschau

<figure><img src="aunz-pint-preview.png" alt="PINT A-NZ Rechnungsvorschau in DocBits"><figcaption><p>Standard-DocBits-Vorschau für eine PINT A-NZ-Rechnung</p></figcaption></figure>

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

```
urn:peppol.org:pint:billing-1@aunz
```

Für Self-Billing-Dokumente lautet das Muster:

```
urn:peppol.org:pint:selfbilling-1@aunz
```

Beide werden unter dem elektronischen Dokumenttyp `PINT A-NZ` klassifiziert.

## Verwandt

- [AUNZ PINT](aunz-pint.md) — Übersicht und A-NZ-spezifische Funktionen
- [AUNZ PINT Self-Billing](aunz-pint-self-billing.md) — Self-Billing-Variante
- [Unterstützte elektronische Dokumente](./)