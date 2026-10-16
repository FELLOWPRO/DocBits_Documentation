---
description: Unterstützung für das elektronische Dokument AUSTRIA EBINTERFACE in DocBits
---

# 🇦🇹 AUSTRIA EBINTERFACE

| Eigenschaft | Wert |
|-------------|------|
| **Land / Region** | Austria |
| **Dokumenttypen** | Invoice, Credit Note |
| **Format** | XML |
| **Standard** | ebInterface (versions 4.3 – 6.1) |
| **Locale** | `de_AT` |

ebInterface ist der österreichische E-Rechnungsstandard, der von der Wirtschaftskammer Österreich (WKÖ — Wirtschaftskammer Österreich) gepflegt wird. Er definiert ein strukturiertes XML-Format für elektronische Rechnungen, das hauptsächlich im B2G- (Business-to-Government) und B2B-Bereich in Österreich eingesetzt wird. DocBits unterstützt alle Versionen von 4.3 bis 6.1, die jeweils durch ihren eigenen XML-Namespace identifiziert werden.

## Unterstützungsstatus

| Komponente | Status |
|------------|--------|
| Vorschau | ✅ Supported |
| Feldextraktion | ✅ Supported |
| Transformation | ✅ Supported |

## Standard-Vorschau

<figure><img src="austria-ebinterface-preview.png" alt="Austria ebInterface Rechnungsvorschau in DocBits"><figcaption><p>Standardvorschau in DocBits für eine AUSTRIA EBINTERFACE-Rechnung</p></figcaption></figure>

## Feldzuordnung

### Kopfzeilenfelder

| DocBits-Feld | Quell-XML-Element | Hinweise |
|---|---|---|
| `invoice_id` | `eb:InvoiceNumber` | Rechnungsnummer |
| `invoice_date` | `eb:InvoiceDate` | Datum im ISO-8601-Format |
| `due_date` | `eb:PaymentConditions/eb:DueDate` | Fälligkeitsdatum der Zahlung |
| `delivery_date` | `eb:Delivery/eb:Date` | Lieferdatum |
| `currency` | `@eb:InvoiceCurrency` | Root-Attribut, für AT stets `EUR` |
| `total_amount` | `eb:TotalGrossAmount` | Bruttobetrag inkl. MwSt. |
| `net_amount` | `eb:Tax/eb:VAT/eb:VATItem/eb:TaxedAmount` | Netto-Steuerbemessungsgrundlage |
| `tax_amount` | `eb:Tax/eb:VAT/eb:VATItem/eb:Amount` | MwSt.-Betrag |
| `purchase_order` | `eb:OrderReference/eb:OrderID` | Bestellreferenz |
| `payment_terms` | `eb:PaymentConditions/eb:Comment` | Zahlungsbedingungen als Freitext |
| `supplier_name` | `eb:Biller/eb:Address/eb:Name` | Firmenname des Rechnungsstellers |
| `supplier_tax_id` | `eb:Biller/eb:VATIdentificationNumber` | Österreichische UID (z. B. ATU12345678) |
| `supplier_street` | `eb:Biller/eb:Address/eb:Street` | Straßenadresse des Rechnungsstellers |
| `supplier_city` | `eb:Biller/eb:Address/eb:Town` | Stadt des Rechnungsstellers |
| `supplier_postal_code` | `eb:Biller/eb:Address/eb:ZIP` | Postleitzahl des Rechnungsstellers |
| `supplier_country` | `eb:Biller/eb:Address/eb:Country/@eb:CountryCode` | ISO-Ländercode |
| `supplier_email` | `eb:Biller/eb:Address/eb:Email` | E-Mail des Rechnungsstellers |
| `supplier_iban` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:IBAN` | IBAN des Rechnungsstellers |
| `customer_name` | `eb:InvoiceRecipient/eb:Address/eb:Name` | Firmenname des Empfängers |
| `customer_tax_id` | `eb:InvoiceRecipient/eb:VATIdentificationNumber` | UID des Empfängers |
| `customer_street` | `eb:InvoiceRecipient/eb:Address/eb:Street` | Straßenadresse des Empfängers |
| `customer_city` | `eb:InvoiceRecipient/eb:Address/eb:Town` | Stadt des Empfängers |
| `customer_postal_code` | `eb:InvoiceRecipient/eb:Address/eb:ZIP` | Postleitzahl des Empfängers |
| `customer_country` | `eb:InvoiceRecipient/eb:Address/eb:Country/@eb:CountryCode` | ISO-Ländercode |
| `iban` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:IBAN` | Zahlungs-IBAN |
| `bic` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:BIC` | Zahlungs-BIC |

### Positionszeilentabelle (`INVOICE_TABLE`)

Zeilenpfad: `eb:Details/eb:ItemList/eb:ListLineItem`

| Spalte | Quell-XML-Element | Hinweise |
|---|---|---|
| `POSITION` | Sequential index | Zeilennummer (beginnt bei 1) |
| `DESCRIPTION` | `eb:Description` | Produkt-/Leistungsbeschreibung |
| `QUANTITY` | `eb:Quantity` | Numerische Menge |
| `UNIT` | `eb:Quantity/@eb:Unit` | Einheitencode (z. B. `STK` = Stück) |
| `UNIT_PRICE` | `eb:UnitPrice` | Einzelpreis exkl. MwSt. |
| `VAT_RATE` | `eb:VAT/eb:VATItem/eb:VATRate` | MwSt.-Satz in % |
| `VAT` | `eb:VAT/eb:VATItem/eb:TaxedAmount` | MwSt.-Betrag je Position |
| `NET_AMOUNT` | `eb:LineItemAmount` | Zeilensumme exkl. MwSt. |

## Klassifizierungsregeln

DocBits erkennt die ebInterface-Version anhand des XML-Namespace:

| Version | Namespace |
|---------|-----------|
| ebInterface 4.3 | `http://www.ebinterface.at/schema/4p3/` |
| ebInterface 5.0 | `http://www.ebinterface.at/schema/5p0/` |
| ebInterface 6.0 | `http://www.ebinterface.at/schema/6p0/` |
| ebInterface 6.1 | `http://www.ebinterface.at/schema/6p1/` |

Alle Versionen verwenden das Wurzelelement `<eb:Invoice>` mit dem jeweiligen Namespace-URI.

## Verwandte

- [Austria ebInterface 6.0](austria-ebinterface-6-0.md)
- [Austria ebInterface 6.1](austria-ebinterface-6-1.md)
- [Unterstützte elektronische Dokumente](./)
