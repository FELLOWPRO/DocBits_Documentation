---
description: ARGENTINA AFIP elektronische Dokumentenunterstützung in DocBits
---

# 🇦🇷 ARGENTINA AFIP

| Eigenschaft | Wert |
|-------------|------|
| **Land / Region** | Argentinien |
| **Dokumenttypen** | Rechnung |
| **Format** | XML |
| **Standard** | AFIP Comprobante Electrónico (Administración Federal de Ingresos Públicos) |
| **Sprache** | `es_AR` |

Der ARGENTINA AFIP-Standard ist das elektronische Rechnungsformat der argentinischen Bundessteuerbehörde (AFIP). Dokumente werden durch `<tipoComprobante>` identifiziert — z.B. Typ `001` = Factura A. Jede Rechnung enthält eine CAE-Nummer (Código de Autorización Electrónica) und einen Barcode zur AFIP-Validierung.

## Unterstützungsstatus

| Komponente | Status |
|------------|--------|
| Vorschau | ✅ Unterstützt |
| Feldextraktion | ✅ Unterstützt |
| Transformation | ✅ Unterstützt |

## Standard-Vorschau

<figure><img src="argentina-afip-preview.png" alt="Argentina AFIP Rechnungsvorschau in DocBits"><figcaption><p>Standard DocBits-Vorschau für eine ARGENTINA AFIP Factura A Rechnung</p></figcaption></figure>

## Feldzuordnung

### Kopffelder

| DocBits-Feld | Quell-XML-Element | Hinweise |
|---|---|---|
| `invoice_id` | `<puntoVenta>` + `<numeroComprobante>` | Format: `PPPP-NNNNNNNN` |
| `invoice_date` | `<cabecera>/<fechaEmision>` | |
| `due_date` | `<cabecera>/<fechaVencimiento>` | |
| `currency` | Fest: `ARS` | Immer Argentinischer Peso |
| `total_amount` | `<totales>/<total>` | |
| `net_amount` | `<totales>/<netoGravado>` oder `<subtotal>` | |
| `tax_amount` | `<totales>/<totalIVA>` | |
| `supplier_name` | `<emisor>/<razonSocial>` | |
| `supplier_id` | `<emisor>/<CUIT>` oder `<cabecera>/<CUIT>` | CUIT = argentinische Steuernummer |
| `supplier_address` | `<emisor>/<domicilioComercial>/<calle>` + `<numero>` | |
| `supplier_postal_code` | `<emisor>/<domicilioComercial>/<codigoPostal>` | |
| `supplier_city` | `<emisor>/<domicilioComercial>/<localidad>` | |
| `supplier_country` | Fest: `AR` | |
| `buyer_name` | `<receptor>/<razonSocial>` | |
| `buyer_id` | `<receptor>/<CUIT>` | |
| `buyer_address` | `<receptor>/<domicilio>/<calle>` + `<numero>` | |
| `buyer_postal_code` | `<receptor>/<domicilio>/<codigoPostal>` | |
| `buyer_city` | `<receptor>/<domicilio>/<localidad>` | |
| `buyer_country` | Fest: `AR` | |
| `iban` | `<PAYMENT/IBAN>` | Meist leer |
| `bic` | `<PAYMENT/BIC>` | Meist leer |
| `payment_terms` | `<PAYMENT_TERMS>` | Meist leer |
| `purchase_order` | `<PURCHASE_ORDER>` | Meist leer |

### Positionstabelle (`INVOICE_TABLE`)

Zeilenpfad: `<items>/<item>`

| Spalte | Quell-Attribut / Element | Hinweise |
|---|---|---|
| `POSITION` | `@numero` Attribut | Positionsnummer |
| `DESCRIPTION` | `<descripcion>` | |
| `QUANTITY` | `<cantidad>` | |
| `UNIT` | `<unidadMedida>` | AFIP-Einheitscode (z.B. `7` = Stück) |
| `UNIT_PRICE` | `<precioUnitario>` | |
| `VAT_RATE` | `<alicuotaIVA>` | z.B. `21.00` für den argentinischen Mehrwertsteuersatz |
| `VAT` | `<importeIVA>` | |
| `NET_AMOUNT` | `<subtotal>` | Zeilensumme vor Steuer |

## Klassifizierungsregel

DocBits erkennt ARGENTINA AFIP-Dokumente über das Regex-Muster:

```
<tipoComprobante>001\s*</tipoComprobante>
```

Typ `001` entspricht **Factura A** (Rechnung an mehrwertsteuerpflichtige Käufer).

## Verwandte Seiten

- [ARGENTINA FACTURA ELECTRONICA](argentina-factura-electronica.md)
- [Unterstützte elektronische Dokumente](./)
