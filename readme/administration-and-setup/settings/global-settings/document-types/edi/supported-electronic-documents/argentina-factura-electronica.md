---
description: Unterstützung des elektronischen Dokuments ARGENTINA FACTURA ELECTRONICA in DocBits
---

# 🇦🇷 ARGENTINA FACTURA ELECTRONICA

<!-- edocs-country-scope -->

{% hint style="info" %}
Die Länderanleitung enthält Versionsgrenzen, die tatsächlich verwendete Konfiguration und das Erklärvideo zum Land. [Argentinien](countries/argentina.md). Für den Gutschrift-Klassifizierungseintrag ist im geprüften Status kein eigenes Extraktionspaket ausgewiesen. Prüfen Sie die tatsächlich verwendete Zuordnung und testen Sie ein echtes Gutschriftbeispiel.
{% endhint %}

| Eigenschaft          | Wert                                                                    |
| -------------------- | ----------------------------------------------------------------------- |
| **Land / Region**    | Argentinien                                                             |
| **Dokumenttypen**    | Rechnung                                                                |
| **Format**           | XML                                                                     |
| **Standard**         | Argentina Factura Electrónica (AFIP-Comprobante-Typen jenseits von Factura A) |
| **Locale**           | `es_AR`                                                                 |

ARGENTINA FACTURA ELECTRONICA umfasst die erweiterte Menge der argentinischen elektronischen AFIP-Dokumente jenseits von Factura A (Typ 001). Dazu gehören weitere Comprobante-Typen wie Factura B (Typ 006), Factura C (Typ 011), Nota de Crédito (Typ 003) und andere Varianten. DocBits erkennt den Dokumenttyp automatisch anhand von `<tipoComprobante>` und wendet die passende Extraktion an.

## Unterstützungsstatus

| Komponente       | Status         |
| ---------------- | -------------- |
| Vorschau         | ✅ Unterstützt |
| Feldextraktion   | ✅ Unterstützt |
| Transformation   | ✅ Unterstützt |

## Standardvorschau

<figure><img src="../../../../../../.gitbook/assets/argentina-factura-electronica-preview.png" alt="Vorschau von Argentina Factura Electronica in DocBits"><figcaption><p>Standardvorschau von DocBits für ein Dokument vom Typ ARGENTINA FACTURA ELECTRONICA</p></figcaption></figure>

## Feldzuordnung

### Kopffelder

| DocBits-Feld     | Quell-XML-Elemente                                                        | Hinweise                                                  |
| ---------------- | ------------------------------------------------------------------------- | --------------------------------------------------------- |
| `invoice_id`     | `//NumeroFactura`, `//cbte_nro`, `//CbteNro`, `//InvoiceNumber`           | Mehrere XPath-Fallbacks für abweichende Schemata          |
| `invoice_date`   | `//FechaEmision`, `//cbte_fch`, `//CbteFch`, `//IssueDate`                |                                                           |
| `due_date`       | `//fechaVencimiento`, `//fechaVtoPago`                                    |                                                           |
| `currency`       | `//Moneda`, `//mon_id`, `//MonId`, Fallback: `ARS`                        |                                                           |
| `total_amount`   | `//MontoTotal`, `//imp_total`, `//ImpTotal`, `//TotalAmount`              |                                                           |
| `net_amount`     | `//MontoNeto`, `//imp_neto`, `//ImpNeto`, `//NetAmount`                   |                                                           |
| `tax_amount`     | `//MontoIVA`, `//imp_iva`, `//ImpIVA`, `//TaxAmount`                      |                                                           |
| `supplier_name`  | `//NombreProveedor`, `//razon_social`, `//RazonSocial`, `//SellerName`    |                                                           |
| `supplier_id`    | `//CUITProveedor`, `//cuit`, `//Cuit`, `//SellerID`                       | CUIT = argentinische Steuernummer                         |
| `buyer_name`     | `//NombreComprador`, `//nombre_cliente`, `//NombreCliente`, `//BuyerName` |                                                           |
| `buyer_id`       | `//CUITComprador`, `//doc_nro`, `//DocNro`, `//BuyerID`                   |                                                           |
| `iban`           | `//PAYMENT/IBAN`                                                          | Meist leer                                                |
| `bic`            | `//PAYMENT/BIC`                                                           | Meist leer                                                |
| `payment_terms`  | `//PAYMENT_TERMS`                                                         | Meist leer                                                |
| `purchase_order` | `//PURCHASE_ORDER`                                                        | Meist leer                                                |

### Positionstabelle (`INVOICE_TABLE`)

Zeilenpfad: `<items>/<item>`, `<Items>/<Item>` oder `<Detalle>/<Linea>`

| Spalte        | Quellattribut / -element                | Hinweise        |
| ------------- | --------------------------------------- | --------------- |
| `POSITION`    | `@numero`, `<numero>` oder `position()` | Positionsnummer |
| `DESCRIPTION` | `<descripcion>`, `<Descripcion>`        |                 |
| `QUANTITY`    | `<cantidad>`, `<Cantidad>`              |                 |
| `UNIT_PRICE`  | `<precioUnitario>`, `<PrecioUnitario>`  |                 |
| `VAT_RATE`    | `<alicuotaIVA>`, `<AlicuotaIVA>`        | z. B. `21.00`   |
| `VAT`         | `<importeIVA>`, `<ImporteIVA>`          |                 |
| `NET_AMOUNT`  | `<subtotal>`, `<Subtotal>`, `<importe>` | Zeilensumme     |

## Klassifizierungsregel

DocBits erkennt ARGENTINA-FACTURA-ELECTRONICA-Dokumente über das Fehlen der Factura-A-Kennzeichnung: Dokumente mit `<tipoComprobante>`-Werten ungleich `001` (z. B. `003`, `006`, `011`) werden diesem Standard zugeordnet.

## Verwandte Seiten

* [ARGENTINA AFIP](argentina-afip.md)
* [Unterstützte elektronische Dokumente](./)
