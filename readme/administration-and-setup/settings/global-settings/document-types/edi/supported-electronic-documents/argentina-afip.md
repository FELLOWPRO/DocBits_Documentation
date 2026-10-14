---
description: Unterstützung des elektronischen Dokuments ARGENTINA AFIP in DocBits
---

# 🇦🇷 ARGENTINA AFIP

| Eigenschaft          | Wert                                                                       |
| -------------------- | -------------------------------------------------------------------------- |
| **Land / Region**    | Argentinien                                                                |
| **Dokumenttypen**    | Rechnung                                                                   |
| **Format**           | XML                                                                        |
| **Standard**         | AFIP Comprobante Electrónico (Administración Federal de Ingresos Públicos) |
| **Locale**           | `es_AR`                                                                    |

Der Standard ARGENTINA AFIP ist das elektronische Rechnungsformat der argentinischen Bundessteuerbehörde (AFIP). Dokumente werden über `<tipoComprobante>` identifiziert, z. B. Typ `001` = Factura A. Jede Rechnung enthält eine CAE-Nummer (Código de Autorización Electrónica) und einen Barcode zur AFIP-Validierung.

## Unterstützungsstatus

| Komponente       | Status         |
| ---------------- | -------------- |
| Vorschau         | ✅ Unterstützt |
| Feldextraktion   | ✅ Unterstützt |
| Transformation   | ✅ Unterstützt |

## Standardvorschau

<figure><img src="../../../../../../.gitbook/assets/argentina-afip-preview.png" alt="Vorschau einer Argentina-AFIP-Rechnung in DocBits"><figcaption><p>Standardvorschau von DocBits für eine ARGENTINA-AFIP-Rechnung vom Typ Factura A</p></figcaption></figure>

## Feldzuordnung

### Kopffelder

| DocBits-Feld           | Quell-XML-Element                                    | Hinweise                                                     |
| ---------------------- | ---------------------------------------------------- | ------------------------------------------------------------ |
| `invoice_id`           | `<puntoVenta>` + `<numeroComprobante>`               | Format: `PPPP-NNNNNNNN`                                      |
| `invoice_date`         | `<cabecera>/<fechaEmision>`                          |                                                              |
| `due_date`             | `<cabecera>/<fechaVencimiento>`                      |                                                              |
| `currency`             | Fest: `ARS`                                          | Immer Argentinischer Peso                                    |
| `total_amount`         | `<totales>/<total>`                                  |                                                              |
| `net_amount`           | `<totales>/<netoGravado>` oder `<subtotal>`          |                                                              |
| `tax_amount`           | `<totales>/<totalIVA>`                               |                                                              |
| `supplier_name`        | `<emisor>/<razonSocial>`                             |                                                              |
| `supplier_id`          | `<emisor>/<CUIT>` oder `<cabecera>/<CUIT>`           | CUIT = argentinische Steuernummer                            |
| `supplier_address`     | `<emisor>/<domicilioComercial>/<calle>` + `<numero>` |                                                              |
| `supplier_postal_code` | `<emisor>/<domicilioComercial>/<codigoPostal>`       |                                                              |
| `supplier_city`        | `<emisor>/<domicilioComercial>/<localidad>`          |                                                              |
| `supplier_country`     | Fest: `AR`                                           |                                                              |
| `buyer_name`           | `<receptor>/<razonSocial>`                           |                                                              |
| `buyer_id`             | `<receptor>/<CUIT>`                                  |                                                              |
| `buyer_address`        | `<receptor>/<domicilio>/<calle>` + `<numero>`        |                                                              |
| `buyer_postal_code`    | `<receptor>/<domicilio>/<codigoPostal>`              |                                                              |
| `buyer_city`           | `<receptor>/<domicilio>/<localidad>`                 |                                                              |
| `buyer_country`        | Fest: `AR`                                           |                                                              |
| `iban`                 | `<PAYMENT/IBAN>`                                     | Meist leer – AFIP-Dokumente enthalten selten Bankdaten       |
| `bic`                  | `<PAYMENT/BIC>`                                      | Meist leer                                                   |
| `payment_terms`        | `<PAYMENT_TERMS>`                                    | Meist leer                                                   |
| `purchase_order`       | `<PURCHASE_ORDER>`                                   | Meist leer                                                   |

### Positionstabelle (`INVOICE_TABLE`)

Zeilenpfad: `<items>/<item>`

| Spalte        | Quellattribut / -element   | Hinweise                                                     |
| ------------- | -------------------------- | ------------------------------------------------------------ |
| `POSITION`    | Attribut `@numero`         | Positionsnummer                                              |
| `DESCRIPTION` | `<descripcion>`            |                                                              |
| `QUANTITY`    | `<cantidad>`               |                                                              |
| `UNIT`        | `<unidadMedida>`           | AFIP-Einheitencode (z. B. `7` = Stück)                       |
| `UNIT_PRICE`  | `<precioUnitario>`         |                                                              |
| `VAT_RATE`    | `<alicuotaIVA>`            | z. B. `21.00` für den argentinischen Standard-Mehrwertsteuersatz |
| `VAT`         | `<importeIVA>`             |                                                              |
| `NET_AMOUNT`  | `<subtotal>`               | Zeilensumme vor Steuern                                      |

## Klassifizierungsregel

DocBits erkennt ARGENTINA-AFIP-Dokumente über das Regex-Muster:

```
<tipoComprobante>001\s*</tipoComprobante>
```

Typ `001` entspricht **Factura A** (Rechnung an mehrwertsteuerpflichtige Käufer). Andere Comprobante-Typen werden vom Standard ARGENTINA FACTURA ELECTRONICA behandelt.

## Verwandte Seiten

* [ARGENTINA FACTURA ELECTRONICA](argentina-factura-electronica.md)
* [Unterstützte elektronische Dokumente](./)
