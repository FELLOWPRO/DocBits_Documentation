---
description: Spanien Facturae (3.2, 3.2.1, 3.2.2) – Unterstützung für elektronische Dokumente in DocBits
---

# 🇪🇸 Spanien Facturae

| Eigenschaft | Wert |
|-------------|------|
| **Land / Region** | Spanien |
| **Dokumenttypen** | Rechnung (Factura), Gutschrift |
| **Format** | XML |
| **Standard** | Facturae 3.2 / 3.2.1 / 3.2.2 (Agencia Tributaria / AEAT) |
| **Locale** | `es_ES` |

Facturae ist der spanische Pflichtstandard für elektronische Rechnungen, der von der Agencia Estatal de Administración Tributaria (AEAT) und dem Finanzministerium verwaltet wird. Er ist für Rechnungen an spanische Behörden verpflichtend und wird auch im B2B-Bereich weit verbreitet eingesetzt. Das Wurzelelement ist `<fe:Facturae>` mit einer versionierten Namespace-URL. DocBits erkennt die Version anhand des `xsi:schemaLocation`-Attributs, das auf eine der offiziellen Schema-URLs verweist:

| Version | Schema-URL |
|---------|-----------|
| Facturae 3.2 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2.xml` |
| Facturae 3.2.1 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2_1.xml` |
| Facturae 3.2.2 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2_2.xml` |

## Unterstützungsstatus

| Komponente | Status |
|------------|--------|
| Vorschau | ✅ Unterstützt |
| Feldextraktion | ✅ Unterstützt |
| Transformation | ✅ Unterstützt |

## Standardvorschau

<figure><img src="spain-facturae-preview.png" alt="Spanien Facturae Rechnungsvorschau in DocBits"><figcaption><p>Standardvorschau in DocBits für eine Spanien Facturae 3.2.2 Rechnung</p></figcaption></figure>

## Feldzuordnung

### Kopfzeilenfelder

| DocBits-Feld | XML-Quellelement | Hinweise |
|---|---|---|
| `invoice_id` | `Invoices/Invoice/InvoiceHeader/InvoiceNumber` | Rechnungsnummer |
| `invoice_date` | `Invoices/Invoice/InvoiceIssueData/IssueDate` | Ausstellungsdatum (JJJJ-MM-TT) |
| `due_date` | `PaymentDetails/Installment/InstallmentDueDate` | Fälligkeitsdatum der Zahlung |
| `invoice_type` | `Invoices/Invoice/InvoiceHeader/InvoiceDocumentType` | FC=Rechnung, NC=Gutschrift |
| `currency` | `Invoices/Invoice/InvoiceIssueData/InvoiceCurrencyCode` | Immer `EUR` |
| `purchase_order` | `Invoices/Invoice/InvoiceHeader/ReceiverContractReference` | Bestellreferenz des Käufers |
| `net_amount` | `Invoices/Invoice/InvoiceTotals/TotalGrossAmountBeforeTaxes` | Nettobetrag exkl. MwSt. |
| `tax_amount` | `Invoices/Invoice/InvoiceTotals/TotalTaxOutputs` | Gesamter MwSt.-Betrag |
| `total_amount` | `Invoices/Invoice/InvoiceTotals/InvoiceTotal` | Gesamtbetrag inkl. MwSt. |
| `tax_rate` | `TaxesOutputs/Tax/TaxRate` | MwSt.-Satz in % (Standard 21%) |
| `payment_terms` | `PaymentDetails/Installment/PaymentMeans` | Zahlungsart-Code |
| `supplier_name` | `Parties/SellerParty/LegalEntity/CorporateName` | Name des Lieferanten |
| `supplier_id` | `Parties/SellerParty/TaxIdentification/TaxIdentificationNumber` | NIF/CIF (z. B. `ES12345678A`) |
| `supplier_tax_id` | `Parties/SellerParty/TaxIdentification/TaxIdentificationNumber` | Spanische NIF oder CIF Steuernummer |
| `supplier_address` | `Parties/SellerParty/LegalEntity/AddressInSpain/Address` | Lieferantenanschrift |
| `supplier_city` | `Parties/SellerParty/LegalEntity/AddressInSpain/Town` | Stadt des Lieferanten |
| `supplier_postal_code` | `Parties/SellerParty/LegalEntity/AddressInSpain/PostCode` | Postleitzahl des Lieferanten |
| `supplier_country` | `Parties/SellerParty/LegalEntity/AddressInSpain/CountryCode` | ISO-Ländercode (`ESP`) |
| `buyer_name` | `Parties/BuyerParty/LegalEntity/CorporateName` | Name des Käufers |
| `buyer_id` | `Parties/BuyerParty/TaxIdentification/TaxIdentificationNumber` | NIF/CIF des Käufers |
| `buyer_address` | `Parties/BuyerParty/LegalEntity/AddressInSpain/Address` | Käuferanschrift |
| `buyer_city` | `Parties/BuyerParty/LegalEntity/AddressInSpain/Town` | Stadt des Käufers |
| `buyer_postal_code` | `Parties/BuyerParty/LegalEntity/AddressInSpain/PostCode` | Postleitzahl des Käufers |
| `buyer_country` | `Parties/BuyerParty/LegalEntity/AddressInSpain/CountryCode` | ISO-Ländercode (`ESP`) |
| `iban` | `PaymentDetails/Installment/AccountToBeCredited/IBAN` | IBAN des Begünstigten |

### Positionstabelle (`INVOICE_TABLE`)

Zeilenpfad: `Invoices/Invoice/Items/InvoiceLine`

| Spalte | XML-Quellelement | Hinweise |
|---|---|---|
| `POSITION` | `ItemDescription` | Positionssequenz / Beschreibung als Bezeichner |
| `DESCRIPTION` | `ItemDescription` | Artikelbeschreibung |
| `QUANTITY` | `Quantity` | Berechnete Menge |
| `UNIT` | `UnitOfMeasure` | Maßeinheit (z. B. `units`) |
| `UNIT_PRICE` | `UnitPriceWithoutTax` | Einzelpreis exkl. MwSt. |
| `VAT_RATE` | `TaxesOutputs/Tax/TaxRate` | MwSt.-Satz in % (typisch 21%) |
| `VAT` | `TaxesOutputs/Tax/TaxAmount/TotalAmount` | MwSt.-Betrag pro Position |
| `NET_AMOUNT` | `TotalCost` | Positionssumme exkl. MwSt. |

## Klassifizierungsregeln

DocBits erkennt Facturae-Dokumente anhand des `xsi:schemaLocation`-Attributs am Wurzelelement `<fe:Facturae>`:

| Elektronischer Dokumenttyp | Muster |
|---------------------------|--------|
| FACTURAE 3.2 | `xsi:schemaLocation` enthält `Facturaev3_2.xml` (nicht 3_2_1 oder 3_2_2) |
| FACTURAE 3.2.1 | `xsi:schemaLocation` enthält `Facturaev3_2_1.xml` |
| FACTURAE 3.2.2 | `xsi:schemaLocation` enthält `Facturaev3_2_2.xml` |

Das Wurzelelement ist `<fe:Facturae>` mit Namespace `http://www.facturae.es/Facturae/2014/v3.2.2/Facturae` (versionsspezifisch). Die Klassifizierung verwendet das **First-Match-Wins**-Prinzip, wobei spezifischere Muster (3.2.2, 3.2.1) vor dem allgemeinen 3.2 geprüft werden.

## Verwandte Themen

- [Aktuell unterstützte E-Rechnungsstandards](../../currently-supported-e-invoice-standards/)
- [Unterstützte elektronische Dokumente](./)
