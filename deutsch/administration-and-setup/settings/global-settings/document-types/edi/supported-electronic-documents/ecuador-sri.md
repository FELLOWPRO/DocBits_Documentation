---
description: Ecuador SRI (Factura Electrónica, SRI 1.0.0 – 2.1.0) Unterstützung für elektronische Dokumente in DocBits
---

# 🇪🇨 Ecuador SRI

| Eigenschaft | Wert |
|-------------|------|
| **Land / Region** | Ecuador |
| **Dokumenttypen** | Factura (Rechnung), Nota de Crédito, Nota de Débito, Guía de Remisión, Comprobante de Retención |
| **Format** | XML |
| **Standard** | SRI (Servicio de Rentas Internas) |
| **Gebietsschema** | `es_EC` |

Der ecuadorianische SRI-Standard für elektronische Rechnungen wird unter der Aufsicht des Servicio de Rentas Internas (SRI), der ecuadorianischen Steuerbehörde, herausgegeben. Dokumente verwenden ein proprietäres XML-Format mit dem Wurzelelement `<factura id="comprobante" version="X.X.X">`. DocBits erkennt die Version automatisch anhand des `version`-Attributs und den Dokumenttyp anhand von `codDoc`:

| version-Attribut | Dokumenttyp |
|------------------|-------------|
| `1.0.0` | SRI 1.0.0 |
| `1.1.0` | SRI 1.1.0 |
| `2.0.0` | SRI 2.0.0 |
| `2.1.0` | SRI 2.1.0 / FACTURA ELECTRONICA |

Die Rechnungsnummer setzt sich aus drei Feldern zusammen: `estab-ptoEmi-secuencial` (z. B. `001-001-000000001`). Der `claveAcceso` ist ein 49-stelliger Zugriffsschlüssel, der vom SRI zur Dokumentenauthentifizierung ausgestellt wird. Ecuador verwendet den **US-Dollar (USD)** als offizielle Währung.

## Unterstützungsstatus

| Komponente | Status |
|------------|--------|
| Vorschau | ✅ Unterstützt |
| Feldextraktion | ✅ Unterstützt |
| Transformation | ✅ Unterstützt |

## Standardvorschau

<figure><img src="ecuador-sri-preview.png" alt="Ecuador SRI Factura Vorschau in DocBits"><figcaption><p>Standardvorschau in DocBits für eine Ecuador SRI Factura Electrónica (Version 2.1.0)</p></figcaption></figure>

## Feldzuordnung

### Kopfzeilenfelder

| DocBits-Feld | Quell-XML-Element | Hinweise |
|---|---|---|
| `invoice_id` | `estab` + `ptoEmi` + `secuencial` | Zusammengesetzt: `001-001-000000001` |
| `invoice_date` | `infoFactura/fechaEmision` | Datumsformat `DD/MM/YYYY` |
| `due_date` | `infoFactura/pagos/pago/plazo` + `unidadTiempo` | Zahlungsziel (z. B. `30 dias`) |
| `currency` | Fest: `USD` | Immer US-Dollar (Ecuadors offizielle Währung) |
| `invoice_type` | Fest: `Factura` | Dokumenttypbezeichnung |
| `net_amount` | `infoFactura/totalSinImpuestos` | Nettosumme ohne MwSt. |
| `tax_amount` | `infoFactura/totalConImpuestos/totalImpuesto/valor` | MwSt.-Betrag (IVA) |
| `total_amount` | `infoFactura/importeTotal` | Gesamtbetrag inkl. MwSt. |
| `supplier_name` | `infoTributaria/razonSocial` | Name des ausstellenden Unternehmens |
| `supplier_id` | `infoTributaria/ruc` | RUC — 13-stellige Steuernummer |
| `supplier_tax_id` | `infoTributaria/ruc` | RUC (identisch mit supplier_id) |
| `supplier_address` | `infoTributaria/dirMatriz` | Hauptsitzadresse des Ausstellers |
| `payment_terms` | `infoFactura/pagos/pago/formaPago` | SRI-Zahlungsartcode |
| `buyer_name` | `infoFactura/razonSocialComprador` | Name des Käuferunternehmens |
| `buyer_id` | `infoFactura/identificacionComprador` | RUC oder CI des Käufers |

### Positionstabelle (`INVOICE_TABLE`)

Zeilenpfad: `detalles/detalle`

| Spalte | Quell-XML-Element | Hinweise |
|---|---|---|
| `POSITION` | Fortlaufender Index | 1-basierte Zeilennummer |
| `DESCRIPTION` | `descripcion` | Artikelbeschreibung |
| `QUANTITY` | `cantidad` | Menge |
| `UNIT_PRICE` | `precioUnitario` | Einzelpreis ohne MwSt. |
| `VAT_RATE` | `impuestos/impuesto/tarifa` | MwSt.-Satz in % (z. B. 15 %) |
| `VAT` | `impuestos/impuesto/valor` | MwSt.-Betrag pro Position |
| `NET_AMOUNT` | `precioTotalSinImpuesto` | Positionssumme ohne MwSt. |

## Klassifizierungsregeln

DocBits erkennt Ecuador-SRI-Dokumente anhand des Wurzelelements und des version-Attributs:

| Elektronischer Dokumenttyp | Muster |
|---------------------------|--------|
| ECUADOR SRI / FACTURA ELECTRONICA | `<factura id="comprobante"` (beliebige Version) |
| ECUADOR SRI 1.0.0 | `<factura id="comprobante" version="1.0.0">` |
| ECUADOR SRI 1.1.0 | `<factura id="comprobante" version="1.1.0">` |
| ECUADOR SRI 2.0.0 | `<factura id="comprobante" version="2.0.0">` |
| ECUADOR SRI 2.1.0 | `<factura id="comprobante" version="2.1.0">` |

Das Wurzelelement ist `<factura>` mit `id="comprobante"`. Das `version`-Attribut bestimmt die spezifische SRI-Version. Die Klassifizierung verwendet das **First-Match-Wins**-Prinzip, sortiert nach Musterlänge (längste/spezifischste zuerst).

## Verwandte Themen

- [Aktuell unterstützte E-Rechnungsstandards](../../currently-supported-e-invoice-standards/)
- [Unterstützte elektronische Dokumente](./)
