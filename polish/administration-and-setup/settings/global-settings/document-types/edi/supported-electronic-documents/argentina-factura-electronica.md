---
description: Obsługa dokumentów elektronicznych ARGENTINA FACTURA ELECTRONICA w DocBits
---

# 🇦🇷 ARGENTINA FACTURA ELECTRONICA

| Właściwość           | Wartość                                                                 |
| -------------------- | ----------------------------------------------------------------------- |
| **Kraj / Region**    | Argentyna                                                               |
| **Typy dokumentów**  | Invoice                                                                 |
| **Format**           | XML                                                                     |
| **Standard**         | Argentina Factura Electrónica (typy comprobante AFIP inne niż Factura A) |
| **Ustawienia regionalne** | `es_AR`                                                            |

ARGENTINA FACTURA ELECTRONICA obejmuje szerszy zestaw argentyńskich dokumentów elektronicznych AFIP poza Factura A (typ 001). Należą do nich inne typy comprobante, takie jak Factura B (typ 006), Factura C (typ 011), Nota de Crédito (typ 003) i inne warianty. DocBits automatycznie rozpoznaje typ dokumentu na podstawie `<tipoComprobante>` i stosuje odpowiednią ekstrakcję.

## Status obsługi

| Komponent        | Status       |
| ---------------- | ------------ |
| Podgląd          | ✅ Obsługiwany |
| Ekstrakcja pól   | ✅ Obsługiwana |
| Transformacja    | ✅ Obsługiwana |

## Domyślny podgląd

<figure><img src="../../../../../../.gitbook/assets/argentina-factura-electronica-preview.png" alt="Podgląd Argentina Factura Electronica w DocBits"><figcaption><p>Domyślny podgląd DocBits dla dokumentu ARGENTINA FACTURA ELECTRONICA</p></figcaption></figure>

## Mapowanie pól

### Pola nagłówka

| Pole DocBits     | Źródłowe elementy XML                                                     | Uwagi                                                  |
| ---------------- | ------------------------------------------------------------------------- | ------------------------------------------------------ |
| `invoice_id`     | `//NumeroFactura`, `//cbte_nro`, `//CbteNro`, `//InvoiceNumber`           | Wiele zapasowych ścieżek XPath dla wariantów schematów |
| `invoice_date`   | `//FechaEmision`, `//cbte_fch`, `//CbteFch`, `//IssueDate`                |                                                        |
| `due_date`       | `//fechaVencimiento`, `//fechaVtoPago`                                    |                                                        |
| `currency`       | `//Moneda`, `//mon_id`, `//MonId`, wartość zapasowa: `ARS`                |                                                        |
| `total_amount`   | `//MontoTotal`, `//imp_total`, `//ImpTotal`, `//TotalAmount`              |                                                        |
| `net_amount`     | `//MontoNeto`, `//imp_neto`, `//ImpNeto`, `//NetAmount`                   |                                                        |
| `tax_amount`     | `//MontoIVA`, `//imp_iva`, `//ImpIVA`, `//TaxAmount`                      |                                                        |
| `supplier_name`  | `//NombreProveedor`, `//razon_social`, `//RazonSocial`, `//SellerName`    |                                                        |
| `supplier_id`    | `//CUITProveedor`, `//cuit`, `//Cuit`, `//SellerID`                       | CUIT = argentyński numer identyfikacji podatkowej      |
| `buyer_name`     | `//NombreComprador`, `//nombre_cliente`, `//NombreCliente`, `//BuyerName` |                                                        |
| `buyer_id`       | `//CUITComprador`, `//doc_nro`, `//DocNro`, `//BuyerID`                   |                                                        |
| `iban`           | `//PAYMENT/IBAN`                                                          | Zwykle puste                                           |
| `bic`            | `//PAYMENT/BIC`                                                           | Zwykle puste                                           |
| `payment_terms`  | `//PAYMENT_TERMS`                                                         | Zwykle puste                                           |
| `purchase_order` | `//PURCHASE_ORDER`                                                        | Zwykle puste                                           |

### Tabela pozycji (`INVOICE_TABLE`)

Ścieżka wiersza: `<items>/<item>`, `<Items>/<Item>` lub `<Detalle>/<Linea>`

| Kolumna       | Atrybut / element źródłowy              | Uwagi                 |
| ------------- | --------------------------------------- | --------------------- |
| `POSITION`    | `@numero`, `<numero>` lub `position()`  | Numer kolejny pozycji |
| `DESCRIPTION` | `<descripcion>`, `<Descripcion>`        |                       |
| `QUANTITY`    | `<cantidad>`, `<Cantidad>`              |                       |
| `UNIT_PRICE`  | `<precioUnitario>`, `<PrecioUnitario>`  |                       |
| `VAT_RATE`    | `<alicuotaIVA>`, `<AlicuotaIVA>`        | np. `21.00`           |
| `VAT`         | `<importeIVA>`, `<ImporteIVA>`          |                       |
| `NET_AMOUNT`  | `<subtotal>`, `<Subtotal>`, `<importe>` | Wartość pozycji       |

## Reguła klasyfikacji

DocBits wykrywa dokumenty ARGENTINA FACTURA ELECTRONICA na podstawie braku znacznika Factura A — dokumenty z wartościami `<tipoComprobante>` innymi niż `001` (np. `003`, `006`, `011`) są kierowane do tego standardu.

## Powiązane

* [ARGENTINA AFIP](argentina-afip.md)
* [Obsługiwane dokumenty elektroniczne](./)
