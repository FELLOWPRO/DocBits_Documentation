# Mapeo de campos de ZUGFeRD 2.3.2

## Resumen

ZUGFeRD 2.3.2 fue la versión inicial del estándar. Aunque es antigua, muchos documentos todavía utilizan este formato. DocBits ofrece compatibilidad total para extraer datos de archivos XML de ZUGFeRD 2.3.2.

## Mapeo de campos de cabecera

### Identificación de la factura

| Ruta CII de ZUGFeRD | Campo de DocBits | Campo de Infor BOD | Tipo | Descripción |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Número de factura |
| `ExchangedDocument/TypeCode` | `INVOICE_TYPE_CODE` | `DocumentType` | STRING | Código de tipo de factura |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Fecha de emisión de la factura |

### Tipo y subtipo de documento (controlado por TRA)

El XSLT TRANSFORMATION predeterminado emite dos campos derivados:

| Campo DocBits | Origen | Lógica |
| :--- | :--- | :--- |
| `INVOICE_TYPE` | `CrossIndustryInvoice/ExchangedDocument/TypeCode` | UNCL 1001 `381` o `261` → **Credit Note**; cualquier otro código → **Invoice** |
| `INVOICE_SUB_TYPE` | `SupplyChainTradeTransaction/ApplicableHeaderTradeAgreement/BuyerOrderReferencedDocument/IssuerAssignedID` | No vacío → **Purchase Invoice**; vacío/ausente → **Cost Invoice** |

### Desglose de impuestos (clasificado por niveles)

Los bloques `ApplicableTradeTax` se distribuyen en tres niveles basados en la tasa (no en `[1]`/`[2]`/`[3]` posicionales): los campos de tasa estándar (`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`) capturan rate ≥ 19; los campos de tasa reducida (`*_2`) capturan 0 < rate < 19; los campos de tasa cero (`*_3`) capturan rate = 0. Véase [ZUGFeRD Tax Breakdown](../README.md#tax-breakdown-tier-classified) para la lista completa de campos.

| Ruta CII de ZUGFeRD | Campo de DocBits | Campo de Infor BOD | Tipo | Descripción |
| :--- | :--- | :--- | :--- | :--- |
| `ApplicableTradeTax/RateApplicablePercent` (nivel 1) | `TAX_RATE` | `TaxPercent` | NUMBER | IVA a tasa estándar (≥ 19) |
| `ApplicableTradeTax/BasisAmount` (nivel 1) | `NET_AMOUNT` | `TaxableAmount` | AMOUNT | Importe neto a tasa estándar |
| `ApplicableTradeTax/CalculatedAmount` (nivel 1) | `TAX_AMOUNT` | `TaxAmount` | AMOUNT | Importe del impuesto a tasa estándar |

### Referencias de documentos

| Ruta CII de ZUGFeRD | Campo de DocBits | Campo de Infor BOD | Tipo | Descripción |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerOrderReferencedDocument/ID` | `PURCHASE_ORDER` | `CustomerOrderID` | STRING | Número de pedido de compra |
| `ContractReferencedDocument/ID` | `CONTRACT_NUMBER` | `ContractID` | STRING | Referencia del contrato |
| `DespatchAdviceReferencedDocument/ID` | `DELIVERY_NOTE` | `ShipmentID` | STRING | Referencia de albarán de entrega |

### Información del proveedor (vendedor)

| Ruta CII de ZUGFeRD | Campo de DocBits | Campo de Infor BOD | Tipo | Descripción |
| :--- | :--- | :--- | :--- | :--- |
| `SellerTradeParty/ID` | `VENDOR_ID` | `SupplierPartyID` | STRING | ID del proveedor |
| `SellerTradeParty/Name` | `VENDOR_NAME` | `SupplierPartyName` | STRING | Nombre del proveedor |
| `SellerTradeParty/PostalTradeAddress/Line1` | `VENDOR_ADDRESS` | `SupplierAddress1` | STRING | Línea de dirección 1 |
| `SellerTradeParty/PostalTradeAddress/PostcodeCode` | `VENDOR_POSTAL_CODE` | `SupplierPostalCode` | STRING | Código postal |
| `SellerTradeParty/PostalTradeAddress/CityName` | `VENDOR_CITY` | `SupplierCity` | STRING | Ciudad |
| `SellerTradeParty/PostalTradeAddress/CountryID` | `VENDOR_COUNTRY` | `SupplierCountryCode` | STRING | Código de país |

## Mapeo de artículos de línea

| Ruta CII de ZUGFeRD | Campo de DocBits | Campo de Infor BOD | Tipo | Descripción |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Número de línea |
| `SpecifiedTradeProduct/BuyerAssignedID` | `ITEM_NUMBER` | `BuyerItemID` | STRING | Número de artículo del comprador |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Descripción del artículo |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Cantidad facturada |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Precio unitario neto |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Total de la línea |
