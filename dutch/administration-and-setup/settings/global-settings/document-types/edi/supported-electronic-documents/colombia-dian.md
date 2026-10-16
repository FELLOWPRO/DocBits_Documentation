---
description: Ondersteuning voor Colombiaanse DIAN elektronische documenten in DocBits (Factura Electrónica, Documento Soporte)
---

# 🇨🇴 Colombia DIAN

| Eigenschap | Waarde |
|----------|-------|
| **Land / Regio** | Colombia |
| **Documenttypen** | Factuur (Factura Electrónica), Creditnota (Nota de Crédito), Documento Soporte |
| **Formaat** | XML (UBL 2.1) |
| **Standaard** | DIAN 2.1 (Dirección de Impuestos y Aduanas Nacionales) |
| **Landinstelling** | `es_CO` |

De Colombiaanse elektronische factuurstandaard wordt geregeld door de **DIAN** (Dirección de Impuestos y Aduanas Nacionales). Deze is gebaseerd op UBL 2.1 met DIAN-specifieke extensies (`sts:DianExtensions`). DocBits detecteert Colombia DIAN-documenten via de DIAN-naamruimte en routeert op basis van `CustomizationID`:

| CustomizationID | Documenttype |
|-----------------|--------------|
| 10 | Factura Electrónica de Venta (FACTURA ELECTRONICA) |
| 20 | Nota de Crédito (Creditnota) |
| 91 | Nota de Crédito por devolución |
| 92 | Nota de Débito |
| DS | Documento Soporte (DOCUMENTO SOPORTE) |

De DIAN-identificator (**NIT** — Número de Identificación Tributaria) gebruikt `schemeID="31"` in het UBL `CompanyID`-element.

## Ondersteuningsstatus

| Component | Status |
|-----------|--------|
| Voorbeeld | ✅ Ondersteund |
| Veldextractie | ✅ Ondersteund |
| Transformatie | ✅ Ondersteund |

## Standaardvoorbeeld

<figure><img src="colombia-dian-preview.png" alt="Colombia DIAN Factura Electrónica voorbeeld in DocBits"><figcaption><p>Standaard DocBits-voorbeeld voor een COLOMBIA FACTURA ELECTRONICA (CustomizationID 10)</p></figcaption></figure>

## Veldtoewijzing

### Koptekstvelden

| DocBits-veld | Bron-XML-element | Opmerkingen |
|---|---|---|
| `invoice_id` | `cbc:ID` | Factuurnummer met voorvoegsel (bijv. `SETP990000001`) |
| `invoice_date` | `cbc:IssueDate` | Uitgiftedatum (ISO 8601) |
| `due_date` | `cbc:DueDate` | Vervaldatum betaling |
| `currency` | `cbc:DocumentCurrencyCode` | Altijd `COP` (Colombiaanse peso) |
| `total_amount` | `cac:LegalMonetaryTotal/cbc:PayableAmount` | Totaal te betalen incl. btw |
| `net_amount` | `cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` | Nettobedrag excl. btw |
| `tax_amount` | `cac:TaxTotal/cbc:TaxAmount` | Totaal btw-bedrag (standaardtarief 19%) |
| `supplier_name` | `cac:AccountingSupplierParty//cbc:RegistrationName` | Juridische naam leverancier |
| `supplier_id` | `cac:AccountingSupplierParty//cbc:CompanyID` | NIT leverancier (schemeID=31) |
| `buyer_name` | `cac:AccountingCustomerParty//cbc:RegistrationName` | Juridische naam koper |
| `buyer_id` | `cac:AccountingCustomerParty//cbc:CompanyID` | NIT koper (schemeID=31) |

### Regelitemtabel (`INVOICE_TABLE`)

Regelpad: `cac:InvoiceLine` (of `cac:CreditNoteLine`)

| Kolom | Bron-XML-element | Opmerkingen |
|---|---|---|
| `POSITION` | `cbc:ID` | Regelnummer |
| `DESCRIPTION` | `cac:Item/cbc:Description` | Product- of servicebeschrijving |
| `QUANTITY` | `cbc:InvoicedQuantity` | Hoeveelheid met eenheidscode-attribuut |
| `UNIT_PRICE` | `cac:Price/cbc:PriceAmount` | Eenheidsprijs excl. btw |
| `NET_AMOUNT` | `cbc:LineExtensionAmount` | Regeltotaal excl. btw |

## Classificatieregels

DocBits detecteert Colombia DIAN-documenten via de DIAN-naamruimtetekenreeks:

| Type elektronisch document | Patroon |
|--------------------------|---------|
| COLOMBIA FACTURA ELECTRONICA | `http://www.dian.gov.co/contratos/facturaelectronica/v1/Structures` + `DianExtensions` |
| COLOMBIA DOCUMENTO SOPORTE | `http://www.dian.gov.co/contratos/facturaelectronica/v1/Structures` + `CustomizationID=DS` |

Het hoofdelement is `<Invoice>` (UBL 2.1) voor facturen, `<CreditNote>` voor creditnota's. Alle documenten bevatten een `<sts:DianExtensions>`-blok met DIAN-autorisatiegegevens (`InvoiceAuthorization`, `CUFE`/`CUDE` UUID, QR-code).

## Gerelateerd

- [Momenteel ondersteunde e-factuurstandaarden](../../currently-supported-e-invoice-standards/)
- [Ondersteunde elektronische documenten](./)
