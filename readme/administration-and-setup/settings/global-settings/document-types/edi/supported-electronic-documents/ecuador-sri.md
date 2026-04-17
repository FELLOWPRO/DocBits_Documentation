---
description: Ondersteuning voor Ecuador SRI (Factura Electrónica, SRI 1.0.0 – 2.1.0) elektronische documenten in DocBits
---

# 🇪🇨 Ecuador SRI

| Eigenschap | Waarde |
|-----------|--------|
| **Land / Regio** | Ecuador |
| **Documenttypen** | Factura (Factuur), Nota de Crédito, Nota de Débito, Guía de Remisión, Comprobante de Retención |
| **Formaat** | XML |
| **Standaard** | SRI (Servicio de Rentas Internas) |
| **Landinstelling** | `es_EC` |

De Ecuador SRI elektronische factuurstandaard wordt uitgegeven onder het gezag van de Servicio de Rentas Internas (SRI), de belastingdienst van Ecuador. Documenten gebruiken een eigen XML-formaat met een `<factura id="comprobante" version="X.X.X">` hoofdelement. DocBits detecteert automatisch de versie via het `version`-attribuut en het documenttype via `codDoc`:

| Versie-attribuut | Documenttype |
|-----------------|--------------|
| `1.0.0` | SRI 1.0.0 |
| `1.1.0` | SRI 1.1.0 |
| `2.0.0` | SRI 2.0.0 |
| `2.1.0` | SRI 2.1.0 / FACTURA ELECTRONICA |

Het factuurnummer is samengesteld uit drie velden: `estab-ptoEmi-secuencial` (bijv. `001-001-000000001`). De `claveAcceso` is een toegangssleutel van 49 cijfers die door de SRI wordt uitgegeven voor documentauthenticatie. Ecuador gebruikt de **Amerikaanse Dollar (USD)** als officiële valuta.

## Ondersteuningsstatus

| Component | Status |
|-----------|--------|
| Voorbeeld | ✅ Ondersteund |
| Veldextractie | ✅ Ondersteund |
| Transformatie | ✅ Ondersteund |

## Standaard voorbeeld

<figure><img src="ecuador-sri-preview.png" alt="Ecuador SRI Factura voorbeeld in DocBits"><figcaption><p>Standaard DocBits-voorbeeld voor een Ecuador SRI Factura Electrónica (versie 2.1.0)</p></figcaption></figure>

## Veldkoppeling

### Kopvelden

| DocBits-veld | Bron-XML-element | Opmerkingen |
|---|---|---|
| `invoice_id` | `estab` + `ptoEmi` + `secuencial` | Samengesteld: `001-001-000000001` |
| `invoice_date` | `infoFactura/fechaEmision` | Datumformaat `DD/MM/YYYY` |
| `due_date` | `infoFactura/pagos/pago/plazo` + `unidadTiempo` | Betalingstermijn (bijv. `30 dias`) |
| `currency` | Vast: `USD` | Altijd Amerikaanse Dollar (officiële valuta van Ecuador) |
| `invoice_type` | Vast: `Factura` | Label van het documenttype |
| `net_amount` | `infoFactura/totalSinImpuestos` | Netto totaal excl. btw |
| `tax_amount` | `infoFactura/totalConImpuestos/totalImpuesto/valor` | Btw-bedrag (IVA) |
| `total_amount` | `infoFactura/importeTotal` | Totaalbedrag incl. btw |
| `supplier_name` | `infoTributaria/razonSocial` | Bedrijfsnaam van de uitgever |
| `supplier_id` | `infoTributaria/ruc` | RUC — 13-cijferig belastingidentificatienummer |
| `supplier_tax_id` | `infoTributaria/ruc` | RUC (zelfde als supplier_id) |
| `supplier_address` | `infoTributaria/dirMatriz` | Hoofdkantooradres van de uitgever |
| `payment_terms` | `infoFactura/pagos/pago/formaPago` | SRI-betalingsmethodecode |
| `buyer_name` | `infoFactura/razonSocialComprador` | Bedrijfsnaam van de koper |
| `buyer_id` | `infoFactura/identificacionComprador` | RUC of CI van de koper |

### Regelitemtabel (`INVOICE_TABLE`)

Regelpad: `detalles/detalle`

| Kolom | Bron-XML-element | Opmerkingen |
|---|---|---|
| `POSITION` | Opeenvolgend volgnummer | Regelnummer op basis van 1 |
| `DESCRIPTION` | `descripcion` | Artikelomschrijving |
| `QUANTITY` | `cantidad` | Hoeveelheid |
| `UNIT_PRICE` | `precioUnitario` | Eenheidsprijs excl. btw |
| `VAT_RATE` | `impuestos/impuesto/tarifa` | Btw-tarief in % (bijv. 15%) |
| `VAT` | `impuestos/impuesto/valor` | Btw-bedrag per regel |
| `NET_AMOUNT` | `precioTotalSinImpuesto` | Regeltotaal excl. btw |

## Classificatieregels

DocBits detecteert Ecuador SRI-documenten door het hoofdelement en het versie-attribuut te matchen:

| Type elektronisch document | Patroon |
|---------------------------|---------|
| ECUADOR SRI / FACTURA ELECTRONICA | `<factura id="comprobante"` (elke versie) |
| ECUADOR SRI 1.0.0 | `<factura id="comprobante" version="1.0.0">` |
| ECUADOR SRI 1.1.0 | `<factura id="comprobante" version="1.1.0">` |
| ECUADOR SRI 2.0.0 | `<factura id="comprobante" version="2.0.0">` |
| ECUADOR SRI 2.1.0 | `<factura id="comprobante" version="2.1.0">` |

Het hoofdelement is `<factura>` met `id="comprobante"`. Het `version`-attribuut bepaalt de specifieke SRI-versie. Classificatie gebruikt het principe **eerste overeenkomst wint**, gesorteerd op patroonlengte (langste/meest specifieke eerst).

## Gerelateerd

- [Momenteel ondersteunde e-factuurstandaarden](../../currently-supported-e-invoice-standards/)
- [Ondersteunde elektronische documenten](./)
