# Mapeo de ZUGFeRD 2.2

## Resumen

ZUGFeRD 2.2 continúa la alineación con EN 16931 e incorpora otras actualizaciones del estándar CII.

## Mapeo de campos de cabecera

### Identificación de la factura

| Ruta CII de ZUGFeRD               | Campo de DocBits | Campo de Infor BOD | Tipo   | Descripción                    |
| --------------------------------- | ---------------- | ------------------ | ------ | ------------------------------ |
| `ExchangedDocument/ID`            | `INVOICE_NUMBER` | `DocumentID`       | STRING | Número de factura              |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE`   | `DocumentDateTime` | DATE   | Fecha de emisión de la factura |

### Tipo y subtipo de documento (controlado por TRA)

El XSLT TRANSFORMATION predeterminado emite dos campos derivados:

| Campo DocBits      | Origen                                                                                                     | Lógica                                                                         |
| ------------------ | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| `INVOICE_TYPE`     | `CrossIndustryInvoice/ExchangedDocument/TypeCode`                                                          | UNCL 1001 `381` o `261` → **Credit Note**; cualquier otro código → **Invoice** |
| `INVOICE_SUB_TYPE` | `SupplyChainTradeTransaction/ApplicableHeaderTradeAgreement/BuyerOrderReferencedDocument/IssuerAssignedID` | No vacío → **Purchase Invoice**; vacío/ausente → **Cost Invoice**              |

### Desglose de impuestos (clasificado por niveles)

Los bloques `ApplicableTradeTax` se distribuyen en tres niveles basados en la tasa (no en índices posicionales): los campos de tasa estándar (`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`) capturan rate ≥ 19; los campos de tasa reducida (`*_2`) capturan 0 < rate < 19; los campos de tasa cero (`*_3`) capturan rate = 0. Véase [ZUGFeRD Tax Breakdown](./#desglose-de-impuestos-clasificado-por-niveles) para la lista completa de campos.

### Moneda e importes

| Ruta CII de ZUGFeRD   | Campo de DocBits   | Campo de Infor BOD    | Tipo   | Descripción                |
| --------------------- | ------------------ | --------------------- | ------ | -------------------------- |
| `InvoiceCurrencyCode` | `CURRENCY`         | `CurrencyCode`        | STRING | Moneda de la factura       |
| `TaxBasisTotalAmount` | `TOTAL_NET_AMOUNT` | `TaxBasisTotalAmount` | AMOUNT | Importe neto total         |
| `TaxTotalAmount`      | `TOTAL_TAX_AMOUNT` | `TaxTotalAmount`      | AMOUNT | Importe total de impuestos |
| `GrandTotalAmount`    | `TOTAL_AMOUNT`     | `GrandTotalAmount`    | AMOUNT | Total general              |

## Mapeo de artículos de línea

| Ruta CII de ZUGFeRD                      | Campo de DocBits | Campo de Infor BOD | Tipo   | Descripción              |
| ---------------------------------------- | ---------------- | ------------------ | ------ | ------------------------ |
| `AssociatedDocumentLineDocument/LineID`  | `POSITION`       | `LineNumber`       | STRING | Número de línea          |
| `SpecifiedTradeProduct/Name`             | `DESCRIPTION`    | `ItemDescription`  | STRING | Descripción del artículo |
| `BilledQuantity`                         | `QUANTITY`       | `InvoicedQuantity` | NUMBER | Cantidad facturada       |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE`     | `UnitPrice`        | AMOUNT | Precio unitario neto     |
| `LineTotalAmount`                        | `TOTAL_AMOUNT`   | `ExtendedAmount`   | AMOUNT | Total de la línea        |
