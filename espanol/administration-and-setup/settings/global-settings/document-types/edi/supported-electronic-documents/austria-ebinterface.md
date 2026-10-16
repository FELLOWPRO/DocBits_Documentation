---
description: Soporte para el documento electrónico AUSTRIA EBINTERFACE en DocBits
---
# 🇦🇹 AUSTRIA EBINTERFACE
| Propiedad | Valor |
|-----------|-------|
| **País / Región** | Austria |
| **Tipos de documento** | Factura, Nota de crédito |
| **Formato** | XML |
| **Estándar** | ebInterface (versiones 4.3 – 6.1) |
| **Configuración regional** | `de_AT` |

ebInterface es el estándar austriaco de facturación electrónica mantenido por la Cámara Económica Federal de Austria (WKÖ — Wirtschaftskammer Österreich). Define un formato XML estructurado para facturas electrónicas utilizado principalmente en transacciones B2G (empresa-a-gobierno) y B2B en Austria. DocBits es compatible con todas las versiones desde la 4.3 hasta la 6.1, cada una identificada por su propio espacio de nombres XML.

## Estado de soporte
| Componente | Estado |
|------------|--------|
| Vista previa | ✅ Compatible |
| Extracción de campos | ✅ Compatible |
| Transformación | ✅ Compatible |

## Vista previa predeterminada
<figure><img src="austria-ebinterface-preview.png" alt="Vista previa de factura Austria ebInterface en DocBits"><figcaption><p>Vista previa predeterminada de DocBits para una factura AUSTRIA EBINTERFACE</p></figcaption></figure>

## Asignación de campos
### Campos de encabezado
| Campo DocBits | Elemento XML de origen | Notas |
|---|---|---|
| `invoice_id` | `eb:InvoiceNumber` | Número de factura |
| `invoice_date` | `eb:InvoiceDate` | Fecha en formato ISO 8601 |
| `due_date` | `eb:PaymentConditions/eb:DueDate` | Fecha de vencimiento del pago |
| `delivery_date` | `eb:Delivery/eb:Date` | Fecha de entrega |
| `currency` | `@eb:InvoiceCurrency` | Atributo raíz, siempre `EUR` para AT |
| `total_amount` | `eb:TotalGrossAmount` | Total bruto incluido IVA |
| `net_amount` | `eb:Tax/eb:VAT/eb:VATItem/eb:TaxedAmount` | Base imponible neta |
| `tax_amount` | `eb:Tax/eb:VAT/eb:VATItem/eb:Amount` | Importe del IVA |
| `purchase_order` | `eb:OrderReference/eb:OrderID` | Referencia de orden de compra |
| `payment_terms` | `eb:PaymentConditions/eb:Comment` | Condiciones de pago en texto libre |
| `supplier_name` | `eb:Biller/eb:Address/eb:Name` | Nombre de la empresa facturadora |
| `supplier_tax_id` | `eb:Biller/eb:VATIdentificationNumber` | UID austriaco (p. ej. ATU12345678) |
| `supplier_street` | `eb:Biller/eb:Address/eb:Street` | Dirección de calle del facturador |
| `supplier_city` | `eb:Biller/eb:Address/eb:Town` | Ciudad del facturador |
| `supplier_postal_code` | `eb:Biller/eb:Address/eb:ZIP` | Código postal del facturador |
| `supplier_country` | `eb:Biller/eb:Address/eb:Country/@eb:CountryCode` | Código de país ISO |
| `supplier_email` | `eb:Biller/eb:Address/eb:Email` | Correo electrónico del facturador |
| `supplier_iban` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:IBAN` | IBAN del facturador |
| `customer_name` | `eb:InvoiceRecipient/eb:Address/eb:Name` | Nombre de la empresa destinataria |
| `customer_tax_id` | `eb:InvoiceRecipient/eb:VATIdentificationNumber` | UID del destinatario |
| `customer_street` | `eb:InvoiceRecipient/eb:Address/eb:Street` | Dirección de calle del destinatario |
| `customer_city` | `eb:InvoiceRecipient/eb:Address/eb:Town` | Ciudad del destinatario |
| `customer_postal_code` | `eb:InvoiceRecipient/eb:Address/eb:ZIP` | Código postal del destinatario |
| `customer_country` | `eb:InvoiceRecipient/eb:Address/eb:Country/@eb:CountryCode` | Código de país ISO |
| `iban` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:IBAN` | IBAN de pago |
| `bic` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:BIC` | BIC de pago |

### Tabla de líneas (`INVOICE_TABLE`)
Ruta de fila: `eb:Details/eb:ItemList/eb:ListLineItem`
| Columna | Elemento XML de origen | Notas |
|---|---|---|
| `POSITION` | Índice secuencial | Número de línea basado en 1 |
| `DESCRIPTION` | `eb:Description` | Descripción del producto/servicio |
| `QUANTITY` | `eb:Quantity` | Cantidad numérica |
| `UNIT` | `eb:Quantity/@eb:Unit` | Código de unidad (p. ej. `STK` = pieza) |
| `UNIT_PRICE` | `eb:UnitPrice` | Precio unitario sin IVA |
| `VAT_RATE` | `eb:VAT/eb:VATItem/eb:VATRate` | Tipo de IVA en % |
| `VAT` | `eb:VAT/eb:VATItem/eb:TaxedAmount` | Importe del IVA por línea |
| `NET_AMOUNT` | `eb:LineItemAmount` | Total de línea sin IVA |

## Regla de clasificación
| Versión | Espacio de nombres |
|---------|--------------------|
| ebInterface 4.3 | `http://www.ebinterface.at/schema/4p3/` |
| ebInterface 5.0 | `http://www.ebinterface.at/schema/5p0/` |
| ebInterface 6.0 | `http://www.ebinterface.at/schema/6p0/` |
| ebInterface 6.1 | `http://www.ebinterface.at/schema/6p1/` |

Todas las versiones comparten el elemento raíz `<eb:Invoice>` con el URI de espacio de nombres correspondiente.

## Relacionados
- [Austria ebInterface 6.0](austria-ebinterface-6-0.md)
- [Austria ebInterface 6.1](austria-ebinterface-6-1.md)
- [Documentos electrónicos compatibles](./)
