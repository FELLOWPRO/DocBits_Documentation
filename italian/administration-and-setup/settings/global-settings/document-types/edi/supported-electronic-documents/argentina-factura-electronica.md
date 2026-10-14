---
description: Supporto dei documenti elettronici ARGENTINA FACTURA ELECTRONICA in DocBits
---

# 🇦🇷 ARGENTINA FACTURA ELECTRONICA

| Proprietà               | Valore                                                                      |
| ----------------------- | --------------------------------------------------------------------------- |
| **Paese / Regione**     | Argentina                                                                   |
| **Tipi di documento**   | Fattura                                                                     |
| **Formato**             | XML                                                                         |
| **Standard**            | Argentina Factura Electrónica (tipi di comprobante AFIP diversi dalla Factura A) |
| **Impostazioni locali** | `es_AR`                                                                     |

ARGENTINA FACTURA ELECTRONICA copre l'insieme più ampio di documenti elettronici argentini AFIP oltre alla Factura A (tipo 001). Comprende altri tipi di comprobante come Factura B (tipo 006), Factura C (tipo 011), Nota de Crédito (tipo 003) e altre varianti. DocBits riconosce automaticamente il tipo di documento da `<tipoComprobante>` e applica l'estrazione appropriata.

## Stato del supporto

| Componente          | Stato       |
| ------------------- | ----------- |
| Anteprima           | ✅ Supportata |
| Estrazione dei campi | ✅ Supportata |
| Trasformazione      | ✅ Supportata |

## Anteprima predefinita

<figure><img src="../../../../../../.gitbook/assets/argentina-factura-electronica-preview.png" alt="Anteprima di Argentina Factura Electronica in DocBits"><figcaption><p>Anteprima predefinita di DocBits per un documento ARGENTINA FACTURA ELECTRONICA</p></figcaption></figure>

## Mappatura dei campi

### Campi di intestazione

| Campo DocBits    | Elementi XML di origine                                                   | Note                                                  |
| ---------------- | ------------------------------------------------------------------------- | ----------------------------------------------------- |
| `invoice_id`     | `//NumeroFactura`, `//cbte_nro`, `//CbteNro`, `//InvoiceNumber`           | Più XPath di riserva per gli schemi varianti          |
| `invoice_date`   | `//FechaEmision`, `//cbte_fch`, `//CbteFch`, `//IssueDate`                |                                                       |
| `due_date`       | `//fechaVencimiento`, `//fechaVtoPago`                                    |                                                       |
| `currency`       | `//Moneda`, `//mon_id`, `//MonId`, riserva: `ARS`                         |                                                       |
| `total_amount`   | `//MontoTotal`, `//imp_total`, `//ImpTotal`, `//TotalAmount`              |                                                       |
| `net_amount`     | `//MontoNeto`, `//imp_neto`, `//ImpNeto`, `//NetAmount`                   |                                                       |
| `tax_amount`     | `//MontoIVA`, `//imp_iva`, `//ImpIVA`, `//TaxAmount`                      |                                                       |
| `supplier_name`  | `//NombreProveedor`, `//razon_social`, `//RazonSocial`, `//SellerName`    |                                                       |
| `supplier_id`    | `//CUITProveedor`, `//cuit`, `//Cuit`, `//SellerID`                       | CUIT = codice fiscale argentino                       |
| `buyer_name`     | `//NombreComprador`, `//nombre_cliente`, `//NombreCliente`, `//BuyerName` |                                                       |
| `buyer_id`       | `//CUITComprador`, `//doc_nro`, `//DocNro`, `//BuyerID`                   |                                                       |
| `iban`           | `//PAYMENT/IBAN`                                                          | Di solito vuoto                                       |
| `bic`            | `//PAYMENT/BIC`                                                           | Di solito vuoto                                       |
| `payment_terms`  | `//PAYMENT_TERMS`                                                         | Di solito vuoto                                       |
| `purchase_order` | `//PURCHASE_ORDER`                                                        | Di solito vuoto                                       |

### Tabella delle righe (`INVOICE_TABLE`)

Percorso della riga: `<items>/<item>`, `<Items>/<Item>` oppure `<Detalle>/<Linea>`

| Colonna       | Attributo / Elemento di origine         | Note                          |
| ------------- | --------------------------------------- | ----------------------------- |
| `POSITION`    | `@numero`, `<numero>` oppure `position()` | Numero progressivo della riga |
| `DESCRIPTION` | `<descripcion>`, `<Descripcion>`        |                               |
| `QUANTITY`    | `<cantidad>`, `<Cantidad>`              |                               |
| `UNIT_PRICE`  | `<precioUnitario>`, `<PrecioUnitario>`  |                               |
| `VAT_RATE`    | `<alicuotaIVA>`, `<AlicuotaIVA>`        | ad es. `21.00`                |
| `VAT`         | `<importeIVA>`, `<ImporteIVA>`          |                               |
| `NET_AMOUNT`  | `<subtotal>`, `<Subtotal>`, `<importe>` | Totale della riga             |

## Regola di classificazione

DocBits riconosce i documenti ARGENTINA FACTURA ELECTRONICA in base all'assenza del marcatore della Factura A: i documenti con valori di `<tipoComprobante>` diversi da `001` (ad es. `003`, `006`, `011`) vengono indirizzati a questo standard.

## Correlati

* [ARGENTINA AFIP](argentina-afip.md)
* [Documenti elettronici supportati](./)
