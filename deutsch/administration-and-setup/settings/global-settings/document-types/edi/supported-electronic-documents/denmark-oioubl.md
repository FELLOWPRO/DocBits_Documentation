---
description: Unterstützung elektronischer Dokumente nach dänischem OIOUBL 2.1-Standard in DocBits
---

# 🇩🇰 Denmark OIOUBL 2.1

| Eigenschaft | Wert |
|-------------|------|
| **Land / Region** | Dänemark |
| **Dokumenttypen** | Rechnung (Faktura), Gutschrift |
| **Format** | XML (UBL 2.1) |
| **Standard** | OIOUBL 2.1 (Offentlig Information Online UBL) |
| **Locale** | `da_DK` |

OIOUBL (Offentlig Information Online UBL) ist der dänische E-Invoicing-Standard auf Basis von UBL 2.1. Er ist für Rechnungen an dänische Behörden und öffentliche Einrichtungen verpflichtend und wird auch im B2B-Bereich häufig eingesetzt. DocBits erkennt OIOUBL 2.1-Dokumente anhand des Elements `<cbc:CustomizationID>OIOUBL-2.1</cbc:CustomizationID>`. Der Profilbezeichner `urn:www.nesubl.eu:profiles:profile5:ver2.0` kennzeichnet das NES (Northern European Subset) Rechnungsprofil.

## Unterstützungsstatus

| Komponente | Status |
|------------|--------|
| Vorschau | ✅ Unterstützt |
| Feldextraktion | ✅ Unterstützt |
| Transformation | ✅ Unterstützt |

## Standardvorschau

<figure><img src="denmark-oioubl-preview.png" alt="Denmark OIOUBL 2.1 invoice preview in DocBits"><figcaption><p>Standardvorschau in DocBits für eine dänische OIOUBL 2.1-Rechnung (Faktura)</p></figcaption></figure>

## Feldzuordnung

### Kopfzeilenfelder

| DocBits-Feld | Quell-XML-Element | Hinweise |
|---|---|---|
| `invoice_id` | `cbc:ID` | Rechnungsnummer |
| `invoice_date` | `cbc:IssueDate` | Ausstellungsdatum nach ISO 8601 |
| `due_date` | `cbc:DueDate` | Fälligkeitsdatum der Zahlung |
| `invoice_type` | `cbc:InvoiceTypeCode` | UNCL 1001-Code (380=Rechnung, 381=Gutschrift) |
| `currency` | `cbc:DocumentCurrencyCode` | Immer `DKK` (Dänische Krone) |
| `purchase_order` | `cac:OrderReference/cbc:ID` | Bestellreferenznummer des Käufers |
| `buyer_reference` | `cbc:BuyerReference` | Interne Referenz des Käufers / EAN-Standortnummer |
| `note` | `cbc:Note` | Freitext-Zahlungshinweise oder Anmerkungen |
| `net_amount` | `cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` | Nettobetrag ohne MwSt. |
| `tax_amount` | `cac:TaxTotal/cbc:TaxAmount` | Gesamter MwSt.-Betrag (Standardsatz 25 %) |
| `total_amount` | `cac:LegalMonetaryTotal/cbc:PayableAmount` | Gesamtbetrag inkl. MwSt. |
| `tax_rate` | `cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent` | MwSt.-Satz in % |
| `supplier_name` | `cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` | Firmenname des Lieferanten |
| `supplier_id` | `cac:AccountingSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID` | CVR-Nummer (z. B. `DK12345678`) |
| `supplier_vat` | `cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | Umsatzsteuer-/CVR-Nummer |
| `supplier_address` | `cac:AccountingSupplierParty/.../cbc:StreetName` | Straßenadresse des Lieferanten |
| `supplier_city` | `cac:AccountingSupplierParty/.../cbc:CityName` | Stadt des Lieferanten |
| `supplier_postal_code` | `cac:AccountingSupplierParty/.../cbc:PostalZone` | Postleitzahl des Lieferanten |
| `supplier_country` | `cac:AccountingSupplierParty/.../cbc:IdentificationCode` | ISO-Ländercode (`DK`) |
| `customer_name` | `cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` | Firmenname des Kunden |
| `customer_id` | `cac:AccountingCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` | CVR-Nummer |
| `customer_vat` | `cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | Umsatzsteuer-/CVR-Nummer |
| `customer_address` | `cac:AccountingCustomerParty/.../cbc:StreetName` | Straßenadresse des Kunden |
| `customer_city` | `cac:AccountingCustomerParty/.../cbc:CityName` | Stadt des Kunden |
| `customer_postal_code` | `cac:AccountingCustomerParty/.../cbc:PostalZone` | Postleitzahl des Kunden |
| `customer_country` | `cac:AccountingCustomerParty/.../cbc:IdentificationCode` | ISO-Ländercode (`DK`) |
| `iban` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` | Bankkonto / IBAN |
| `bic` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cbc:ID` | BIC/SWIFT-Code |

### Positionstabelle (`INVOICE_TABLE`)

Zeilenpfad: `cac:InvoiceLine`

| Spalte | Quell-XML-Element | Hinweise |
|---|---|---|
| `POSITION` | `cbc:ID` | Positionsfolgenummer |
| `DESCRIPTION` | `cac:Item/cbc:Name` | Artikelname / Beschreibung |
| `QUANTITY` | `cbc:InvoicedQuantity` | Berechnete Menge |
| `UNIT_PRICE` | `cac:Price/cbc:PriceAmount` | Stückpreis ohne MwSt. |
| `NET_AMOUNT` | `cbc:LineExtensionAmount` | Zeilensumme ohne MwSt. |

## Klassifizierungsregel

DocBits erkennt OIOUBL 2.1-Dokumente durch Abgleich des `CustomizationID`-Elements:

| Elektronischer Dokumenttyp | Muster |
|---------------------------|--------|
| OIOUBL 2.1 | `<cbc:CustomizationID>OIOUBL-2\.1\s*</cbc:CustomizationID>` |

Das Wurzelelement ist `<Invoice>` (oder `<CreditNote>`) im UBL 2.1-Namespace `urn:oasis:names:specification:ubl:schema:xsd:Invoice-2`.

## Verwandte Themen

- [Aktuell unterstützte E-Invoice-Standards](../../currently-supported-e-invoice-standards/)
- [Unterstützte elektronische Dokumente](./)
