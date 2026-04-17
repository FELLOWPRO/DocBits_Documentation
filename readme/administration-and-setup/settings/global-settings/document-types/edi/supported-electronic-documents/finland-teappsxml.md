---
description: Unterstützung für finnische TEAPPSXML-Dokumente in DocBits
---

# 🇫🇮 Finnland TEAPPSXML

| Eigenschaft | Wert |
|----------|-------|
| **Land / Region** | Finnland |
| **Dokumenttypen** | Rechnung, Gutschrift |
| **Format** | XML |
| **Standard** | TEAPPSXML 3.0 (Tieto / Finnisches Bankwesen) |
| **Gebietsschema** | `fi_FI` |

TEAPPSXML (Tietotekniikan ja viestinnän toimiala) ist ein finnischer elektronischer Rechnungsstandard, der hauptsächlich im Bank- und Finanzsektor verwendet wird. Das Wurzelelement ist `<TEAPPSXML>` mit dem Namespace `urn:TEAPPSXML:3.0`. DocBits erkennt TEAPPSXML-Dokumente am Vorhandensein von `xmlns="urn:TEAPPSXML:"` im Wurzelelement.

Das TEAPPSXML-Format verwendet Elementnamen in Großbuchstaben und eine flache Struktur mit separaten Abschnitten `<SENDER>`, `<RECEIVER>`, `<INVOICE>` und `<PAYMENTINFO>`. Das finnische Unternehmens-ID-Format (Y-tunnus) lautet `1234567-8`, und Umsatzsteuer-IDs verwenden das Präfix `FI` (z.B. `FI12345678`).

## Unterstützungsstatus

| Komponente | Status |
|-----------|--------|
| Vorschau | ✅ Unterstützt |
| Feldextraktion | ✅ Unterstützt |
| Transformation | ✅ Unterstützt |

## Standardvorschau

<figure><img src="finland-teappsxml-preview.png" alt="Finnland TEAPPSXML Rechnungsvorschau in DocBits"><figcaption><p>Standardvorschau in DocBits für eine finnische TEAPPSXML-Rechnung</p></figcaption></figure>

## Feldzuordnung

### Kopfzeilenfelder

| DocBits-Feld | Quell-XML-Element | Hinweise |
|---|---|---|
| `invoice_id` | `INVOICE/INVOICENUMBER` | Rechnungsnummer |
| `invoice_date` | `INVOICE/INVOICEDATE` | Ausstellungsdatum (JJJJ-MM-TT) |
| `due_date` | `INVOICE/DUEDATE` | Zahlungsfälligkeitsdatum (JJJJ-MM-TT) |
| `invoice_type` | `INVOICE/INVOICE_TYPE` | Nachrichtentyp (INVOICE) |
| `currency` | `INVOICE/CURRENCY` | Währungscode (typischerweise `EUR`) |
| `purchase_order` | `INVOICE/REFERENCENUMBER` | Zahlungsreferenznummer |
| `payment_reference` | `INVOICE/REFERENCENUMBER` | Finnische Zahlungsreferenz (viitenumero) |
| `net_amount` | `INVOICE/TOTALVATEXCLUDED` | Nettobetrag exkl. MwSt. |
| `tax_amount` | `INVOICE/TOTALVAT` | Gesamter MwSt.-Betrag |
| `total_amount` | `INVOICE/TOTALAMOUNT` | Gesamtbetrag inkl. MwSt. |
| `payment_terms` | `INVOICE/PAYMENT_TERMS` | Zahlungsmethode (z.B. `BANKTRANSFER`) |
| `supplier_name` | `SENDER/NAME` | Name des Absenderunternehmens |
| `supplier_id` | `SENDER/ID` | Finnische Unternehmens-ID (Y-tunnus, z.B. `1234567-8`) |
| `supplier_tax_id` | `SENDER/VATNUMBER` | Umsatzsteuer-ID (z.B. `FI12345678`) |
| `supplier_address` | `SENDER/ADDRESS/STREET` | Straßenadresse des Absenders |
| `supplier_city` | `SENDER/ADDRESS/CITY` | Stadt des Absenders |
| `supplier_postal_code` | `SENDER/ADDRESS/POSTCODE` | Postleitzahl des Absenders |
| `supplier_country` | `SENDER/ADDRESS/COUNTRY` | ISO-Ländercode (`FI`) |
| `supplier_bic` | `SENDER/BANK/BIC` | BIC-Code der Absenderbank |
| `buyer_name` | `INVOICE/BUYER/NAME` | Name des Käuferunternehmens |
| `buyer_id` | `INVOICE/BUYER/ID` | Finnische Unternehmens-ID des Käufers |
| `buyer_address` | `INVOICE/BUYER/ADDRESS_LINE_1` | Käuferadresse |
| `buyer_city` | `INVOICE/BUYER/CITY` | Stadt des Käufers |
| `buyer_postal_code` | `INVOICE/BUYER/POSTAL_CODE` | Postleitzahl des Käufers |
| `buyer_country` | `INVOICE/BUYER/COUNTRY` | ISO-Ländercode (`FI`) |
| `iban` | `PAYMENTINFO/BENEFICIARYACCOUNT/IBAN` | IBAN des Begünstigten |
| `bic` | `PAYMENTINFO/BENEFICIARYACCOUNT/BIC` | BIC-Code des Begünstigten |

### Positionstabelle (`INVOICE_TABLE`)

Zeilenpfad: `INVOICE/LINES/LINE`

| Spalte | Quell-XML-Element | Hinweise |
|---|---|---|
| `POSITION` | `LINENUMBER` | Laufende Zeilennummer |
| `DESCRIPTION` | `ARTICLENAME` | Artikelname/-beschreibung |
| `QUANTITY` | `QUANTITY` | Berechnete Menge |
| `UNIT` | `UNIT` | Maßeinheit (z.B. `KPL` = Stück) |
| `UNIT_PRICE` | `UNITPRICE` | Stückpreis exkl. MwSt. |
| `VAT_RATE` | `VATRATE` | MwSt.-Satz in % (Standard 25,5%) |
| `VAT` | Berechnet | MwSt.-Betrag pro Zeile |
| `NET_AMOUNT` | `LINEAMOUNT` | Zeilensumme exkl. MwSt. |

## Klassifizierungsregel

DocBits erkennt TEAPPSXML-Dokumente durch Abgleich des Attributs `xmlns` am Wurzelelement `<TEAPPSXML>`:

| Elektronischer Dokumenttyp | Muster |
|--------------------------|---------|
| TEAPPSXML | `xmlns` enthält `urn:TEAPPSXML:` |

## Verwandte Themen

- [Aktuell unterstützte E-Rechnungsstandards](../../currently-supported-e-invoice-standards/)
- [Finnland Finvoice](./finland-finvoice.md)
- [Unterstützte elektronische Dokumente](./)
