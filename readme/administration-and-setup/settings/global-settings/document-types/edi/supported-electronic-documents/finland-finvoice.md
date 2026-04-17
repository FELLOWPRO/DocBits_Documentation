---
description: Unterstützung für finnische Finvoice-Dokumente (1.3, 2.0, 2.01, 3.0) in DocBits
---

# 🇫🇮 Finnland Finvoice

| Eigenschaft | Wert |
|----------|-------|
| **Land / Region** | Finnland |
| **Dokumenttypen** | Rechnung (Lasku), Gutschrift (Hyvityslasku) |
| **Format** | XML |
| **Standard** | Finvoice 1.3 / 2.0 / 2.01 / 3.0 (Finance Finland / Finanssiala) |
| **Gebietsschema** | `fi_FI` |

Finvoice ist der E-Rechnungsstandard des finnischen Bankensektors, entwickelt und gepflegt von Finance Finland (Finanssiala ry). Er wird sowohl für B2B- als auch für B2G-Rechnungsstellung verwendet und über die finnische Bankinfrastruktur übertragen. Das Wurzelelement ist `<Finvoice>` mit einer versionierten Namespace-URL. DocBits erkennt die Version über das Attribut `xmlns`:

| Version | Namespace-URL |
|---------|--------------|
| Finvoice 1.3 | `http://www.finvoice.fi/schema/finvoice13` |
| Finvoice 2.0 | `http://www.finvoice.fi/schema/finvoice20` |
| Finvoice 2.01 | `http://www.finvoice.fi/schema/finvoice201` |
| Finvoice 3.0 | `http://www.finvoice.fi/schema/finvoice30` |

Das finnische Unternehmens-ID-Format (Y-tunnus) lautet `1234567-8` (7 Ziffern + Prüfziffer) und dient als Parteikennung. Die Umsatzsteuer-Identifikationsnummer hat das Präfix `FI` gefolgt von 8 Ziffern (z.B. `FI12345678`). Datumsangaben werden im Format `CCYYMMDD` kodiert.

## Unterstützungsstatus

| Komponente | Status |
|-----------|--------|
| Vorschau | ✅ Unterstützt |
| Feldextraktion | ✅ Unterstützt |
| Transformation | ✅ Unterstützt |

## Standardvorschau

<figure><img src="finland-finvoice-preview.png" alt="Finnland Finvoice 3.0 Rechnungsvorschau in DocBits"><figcaption><p>Standardvorschau in DocBits für eine finnische Finvoice 3.0-Rechnung (Lasku)</p></figcaption></figure>

## Feldzuordnung

### Kopfzeilenfelder

| DocBits-Feld | Quell-XML-Element | Hinweise |
|---|---|---|
| `invoice_id` | `InvoiceDetails/InvoiceNumber` | Rechnungsnummer |
| `invoice_date` | `InvoiceDetails/InvoiceDate` | Datum im Format `CCYYMMDD`, konvertiert zu ISO 8601 |
| `due_date` | `InvoiceDetails/PaymentTermsDetails/InvoiceDueDate` | Zahlungsfälligkeitsdatum (`CCYYMMDD`) |
| `invoice_type` | `InvoiceDetails/InvoiceTypeCode` | INV01=Rechnung, CRE01=Gutschrift |
| `currency` | `InvoiceDetails/InvoiceTotalVatExcludedAmount/@AmountCurrencyIdentifier` | Währungscode (typischerweise `EUR`) |
| `net_amount` | `InvoiceDetails/InvoiceTotalVatExcludedAmount` | Nettobetrag exkl. MwSt. |
| `tax_amount` | `InvoiceDetails/InvoiceTotalVatAmount` | Gesamter MwSt.-Betrag |
| `total_amount` | `InvoiceDetails/InvoiceTotalVatIncludedAmount` | Gesamtbetrag inkl. MwSt. |
| `tax_rate` | `InvoiceDetails/VatSpecificationDetails/VatRatePercent` | MwSt.-Satz in % (Standard 25,5%) |
| `supplier_name` | `SellerPartyDetails/SellerOrganisationName` | Name des Lieferantenunternehmens |
| `supplier_id` | `SellerPartyDetails/SellerPartyIdentifier` | Finnische Unternehmens-ID (Y-tunnus, z.B. `1234567-8`) |
| `supplier_vat` | `SellerPartyDetails/SellerOrganisationTaxCode` | Umsatzsteuer-ID (z.B. `FI12345678`) |
| `supplier_address` | `SellerPartyDetails/SellerPostalAddressDetails/SellerStreetName` | Lieferantenadresse |
| `supplier_city` | `SellerPartyDetails/SellerPostalAddressDetails/SellerTownName` | Stadt des Lieferanten |
| `supplier_postal_code` | `SellerPartyDetails/SellerPostalAddressDetails/SellerPostCodeIdentifier` | Postleitzahl des Lieferanten |
| `supplier_country` | `SellerPartyDetails/SellerPostalAddressDetails/CountryCode` | ISO-Ländercode (`FI`) |
| `buyer_name` | `BuyerPartyDetails/BuyerOrganisationName` | Name des Käuferunternehmens |
| `buyer_id` | `BuyerPartyDetails/BuyerPartyIdentifier` | Finnische Unternehmens-ID (Y-tunnus) |
| `buyer_address` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerStreetName` | Käuferadresse |
| `buyer_city` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerTownName` | Stadt des Käufers |
| `buyer_postal_code` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerPostCodeIdentifier` | Postleitzahl des Käufers |
| `buyer_country` | `BuyerPartyDetails/BuyerPostalAddressDetails/CountryCode` | ISO-Ländercode (`FI`) |
| `iban` | `EpiDetails/EpiBfiPartyDetails/EpiBfiIdentifier` | Empfänger-IBAN (EPI-Zahlungsdetails) |
| `bic` | `EpiDetails/EpiPaymentInstructionId` | BIC/SWIFT-Code |
| `payment_terms` | `InvoiceDetails/PaymentTermsDetails/PaymentTermsFreeText` | Freitextliche Zahlungsbedingungen |

### Positionstabelle (`INVOICE_TABLE`)

Zeilenpfad: `InvoiceRow`

| Spalte | Quell-XML-Element | Hinweise |
|---|---|---|
| `POSITION` | `InvoiceRow/ArticleIdentifier` | Artikel-/Produktcode |
| `DESCRIPTION` | `InvoiceRow/ArticleName` | Artikelname/-beschreibung |
| `QUANTITY` | `InvoiceRow/DeliveredQuantity` | Gelieferte Menge |
| `UNIT` | `InvoiceRow/DeliveredQuantity/@QuantityUnitCode` | Einheitencode (z.B. `KPL` = Stück) |
| `UNIT_PRICE` | `InvoiceRow/UnitPriceAmount` | Stückpreis exkl. MwSt. |
| `VAT_RATE` | `InvoiceRow/RowVatRatePercent` | MwSt.-Satz in % pro Zeile |
| `VAT` | `InvoiceRow/RowVatAmount` | MwSt.-Betrag pro Zeile |
| `NET_AMOUNT` | `InvoiceRow/RowAmount` | Zeilensumme exkl. MwSt. |

## Klassifizierungsregeln

DocBits erkennt Finvoice-Dokumente durch Abgleich des Attributs `xmlns` am Wurzelelement `<Finvoice>`:

| Elektronischer Dokumenttyp | Muster |
|--------------------------|---------|
| FINVOICE 1.3 | `xmlns` enthält `http://www.finvoice.fi/schema/finvoice13` |
| FINVOICE 2.0 | `xmlns` enthält `http://www.finvoice.fi/schema/finvoice20` (nicht 2.01) |
| FINVOICE 2.01 | `xmlns` enthält `http://www.finvoice.fi/schema/finvoice201` |
| FINVOICE 3.0 | `xmlns` enthält `http://www.finvoice.fi/schema/finvoice30` |

Die Klassifizierung verwendet das Prinzip **erster Treffer gewinnt**, wobei spezifischere Muster (2.01) vor dem allgemeinen 2.0 ausgewertet werden.

## Verwandte Themen

- [Aktuell unterstützte E-Rechnungsstandards](../../currently-supported-e-invoice-standards/)
- [Finnland TEAPPSXML](./finland-teappsxml.md)
- [Unterstützte elektronische Dokumente](./)
