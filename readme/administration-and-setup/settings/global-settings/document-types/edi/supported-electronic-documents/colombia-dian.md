---
description: Unterstützung für elektronische Dokumente aus Kolumbien (DIAN) in DocBits (Factura Electrónica, Documento Soporte)
---

# 🇨🇴 Colombia DIAN

| Eigenschaft | Wert |
|-------------|------|
| **Land / Region** | Colombia |
| **Dokumenttypen** | Rechnung (Factura Electrónica), Gutschrift (Nota de Crédito), Documento Soporte |
| **Format** | XML (UBL 2.1) |
| **Standard** | DIAN 2.1 (Dirección de Impuestos y Aduanas Nacionales) |
| **Gebietsschema** | `es_CO` |

Der kolumbianische Standard für die elektronische Rechnungsstellung wird von der **DIAN** (Dirección de Impuestos y Aduanas Nacionales) reguliert. Er basiert auf UBL 2.1 mit DIAN-spezifischen Erweiterungen (`sts:DianExtensions`). DocBits erkennt Colombia-DIAN-Dokumente anhand des DIAN-Namespaces und leitet sie anhand der `CustomizationID` weiter:

| CustomizationID | Dokumenttyp |
|-----------------|-------------|
| 10 | Factura Electrónica de Venta (FACTURA ELECTRONICA) |
| 20 | Nota de Crédito (Gutschrift) |
| 91 | Nota de Crédito por devolución |
| 92 | Nota de Débito |
| DS | Documento Soporte (DOCUMENTO SOPORTE) |

Der DIAN-Identifikator (**NIT** — Número de Identificación Tributaria) verwendet `schemeID="31"` im UBL-Element `CompanyID`.

## Unterstützungsstatus

| Komponente | Status |
|------------|--------|
| Vorschau | ✅ Unterstützt |
| Feldextraktion | ✅ Unterstützt |
| Transformation | ✅ Unterstützt |

## Standardvorschau

<figure><img src="colombia-dian-preview.png" alt="Vorschau der Colombia DIAN Factura Electrónica in DocBits"><figcaption><p>Standardvorschau in DocBits für eine COLOMBIA FACTURA ELECTRONICA (CustomizationID 10)</p></figcaption></figure>

## Feldzuordnung

### Kopfzeilenfelder

| DocBits-Feld | Quell-XML-Element | Hinweise |
|---|---|---|
| `invoice_id` | `cbc:ID` | Rechnungsnummer mit Präfix (z. B. `SETP990000001`) |
| `invoice_date` | `cbc:IssueDate` | Ausstellungsdatum (ISO 8601) |
| `due_date` | `cbc:DueDate` | Fälligkeitsdatum der Zahlung |
| `currency` | `cbc:DocumentCurrencyCode` | Immer `COP` (Kolumbianischer Peso) |
| `total_amount` | `cac:LegalMonetaryTotal/cbc:PayableAmount` | Gesamtbetrag inkl. IVA |
| `net_amount` | `cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` | Nettobetrag exkl. IVA |
| `tax_amount` | `cac:TaxTotal/cbc:TaxAmount` | Gesamter IVA-Betrag (Normalsatz 19 %) |
| `supplier_name` | `cac:AccountingSupplierParty//cbc:RegistrationName` | Rechtlicher Name des Lieferanten |
| `supplier_id` | `cac:AccountingSupplierParty//cbc:CompanyID` | NIT des Lieferanten (schemeID=31) |
| `buyer_name` | `cac:AccountingCustomerParty//cbc:RegistrationName` | Rechtlicher Name des Käufers |
| `buyer_id` | `cac:AccountingCustomerParty//cbc:CompanyID` | NIT des Käufers (schemeID=31) |

### Positionstabelle (`INVOICE_TABLE`)

Zeilenpfad: `cac:InvoiceLine` (oder `cac:CreditNoteLine`)

| Spalte | Quell-XML-Element | Hinweise |
|---|---|---|
| `POSITION` | `cbc:ID` | Positionsnummer |
| `DESCRIPTION` | `cac:Item/cbc:Description` | Produkt- oder Dienstleistungsbeschreibung |
| `QUANTITY` | `cbc:InvoicedQuantity` | Menge mit Einheitencode-Attribut |
| `UNIT_PRICE` | `cac:Price/cbc:PriceAmount` | Stückpreis exkl. IVA |
| `NET_AMOUNT` | `cbc:LineExtensionAmount` | Zeilensumme exkl. IVA |

## Klassifizierungsregeln

DocBits erkennt Colombia-DIAN-Dokumente anhand der DIAN-Namespace-Zeichenfolge:

| Elektronischer Dokumenttyp | Muster |
|---------------------------|--------|
| COLOMBIA FACTURA ELECTRONICA | `http://www.dian.gov.co/contratos/facturaelectronica/v1/Structures` + `DianExtensions` |
| COLOMBIA DOCUMENTO SOPORTE | `http://www.dian.gov.co/contratos/facturaelectronica/v1/Structures` + `CustomizationID=DS` |

Das Wurzelelement ist `<Invoice>` (UBL 2.1) für Rechnungen und `<CreditNote>` für Gutschriften. Alle Dokumente enthalten einen `<sts:DianExtensions>`-Block mit DIAN-Autorisierungsdaten (`InvoiceAuthorization`, `CUFE`/`CUDE` UUID, QR-Code).

## Verwandte Themen

- [Aktuell unterstützte E-Rechnungsstandards](../../currently-supported-e-invoice-standards/)
- [Unterstützte elektronische Dokumente](./)
