---
description: Compatibilidad de DocBits con el documento electrónico ARGENTINA AFIP
---

# 🇦🇷 ARGENTINA AFIP

<!-- edocs-country-scope -->

{% hint style="info" %}
Consulte la guía del país para conocer los límites de versión, la configuración que se está utilizando y el vídeo explicativo del país. [Argentina](countries/argentina.md). La entrada de clasificación de notas de crédito no tiene un paquete de extracción dedicado en el estado inspeccionado. Verifique la asignación utilizada y pruebe un ejemplo real de nota de crédito.
{% endhint %}

| Propiedad            | Valor                                                                      |
| -------------------- | -------------------------------------------------------------------------- |
| **País / Región**    | Argentina                                                                  |
| **Tipos de documento** | Invoice                                                                  |
| **Formato**          | XML                                                                        |
| **Estándar**         | AFIP Comprobante Electrónico (Administración Federal de Ingresos Públicos) |
| **Configuración regional** | `es_AR`                                                              |

El estándar ARGENTINA AFIP es el formato de factura electrónica de la autoridad tributaria federal argentina (AFIP). Los documentos se identifican mediante `<tipoComprobante>`; por ejemplo, el tipo `001` = Factura A. Cada factura incluye un número CAE (Código de Autorización Electrónica) y un código de barras para la validación de la AFIP.

## Estado de compatibilidad

| Componente                | Estado        |
| ------------------------- | ------------- |
| Vista previa              | ✅ Compatible |
| Extracción de campos      | ✅ Compatible |
| Transformación            | ✅ Compatible |

## Vista previa predeterminada

<figure><img src="../../../../../../.gitbook/assets/argentina-afip-preview.png" alt="Vista previa de una factura ARGENTINA AFIP en DocBits"><figcaption><p>Vista previa predeterminada de DocBits para una factura Factura A de ARGENTINA AFIP</p></figcaption></figure>

## Mapeo de campos

### Campos de cabecera

| Campo de DocBits       | Elemento XML de origen                               | Notas                                                          |
| ---------------------- | ---------------------------------------------------- | -------------------------------------------------------------- |
| `invoice_id`           | `<puntoVenta>` + `<numeroComprobante>`               | Con el formato `PPPP-NNNNNNNN`                                 |
| `invoice_date`         | `<cabecera>/<fechaEmision>`                          |                                                                |
| `due_date`             | `<cabecera>/<fechaVencimiento>`                      |                                                                |
| `currency`             | Fijo: `ARS`                                          | Siempre peso argentino                                         |
| `total_amount`         | `<totales>/<total>`                                  |                                                                |
| `net_amount`           | `<totales>/<netoGravado>` o `<subtotal>`             |                                                                |
| `tax_amount`           | `<totales>/<totalIVA>`                               |                                                                |
| `supplier_name`        | `<emisor>/<razonSocial>`                             |                                                                |
| `supplier_id`          | `<emisor>/<CUIT>` o `<cabecera>/<CUIT>`              | CUIT = identificación fiscal argentina                         |
| `supplier_address`     | `<emisor>/<domicilioComercial>/<calle>` + `<numero>` |                                                                |
| `supplier_postal_code` | `<emisor>/<domicilioComercial>/<codigoPostal>`       |                                                                |
| `supplier_city`        | `<emisor>/<domicilioComercial>/<localidad>`          |                                                                |
| `supplier_country`     | Fijo: `AR`                                           |                                                                |
| `buyer_name`           | `<receptor>/<razonSocial>`                           |                                                                |
| `buyer_id`             | `<receptor>/<CUIT>`                                  |                                                                |
| `buyer_address`        | `<receptor>/<domicilio>/<calle>` + `<numero>`        |                                                                |
| `buyer_postal_code`    | `<receptor>/<domicilio>/<codigoPostal>`              |                                                                |
| `buyer_city`           | `<receptor>/<domicilio>/<localidad>`                 |                                                                |
| `buyer_country`        | Fijo: `AR`                                           |                                                                |
| `iban`                 | `<PAYMENT/IBAN>`                                     | Normalmente vacío: los documentos de la AFIP rara vez contienen datos bancarios |
| `bic`                  | `<PAYMENT/BIC>`                                      | Normalmente vacío                                              |
| `payment_terms`        | `<PAYMENT_TERMS>`                                    | Normalmente vacío                                              |
| `purchase_order`       | `<PURCHASE_ORDER>`                                   | Normalmente vacío                                              |

### Tabla de posiciones (`INVOICE_TABLE`)

Ruta de fila: `<items>/<item>`

| Columna       | Atributo / elemento de origen | Notas                                        |
| ------------- | ----------------------------- | -------------------------------------------- |
| `POSITION`    | atributo `@numero`            | Número de secuencia de la posición           |
| `DESCRIPTION` | `<descripcion>`               |                                              |
| `QUANTITY`    | `<cantidad>`                  |                                              |
| `UNIT`        | `<unidadMedida>`              | Código de unidad de la AFIP (p. ej., `7` = unidad) |
| `UNIT_PRICE`  | `<precioUnitario>`            |                                              |
| `VAT_RATE`    | `<alicuotaIVA>`               | p. ej., `21.00` para el IVA estándar argentino |
| `VAT`         | `<importeIVA>`                |                                              |
| `NET_AMOUNT`  | `<subtotal>`                  | Total de la línea antes de impuestos         |

## Regla de clasificación

DocBits detecta los documentos ARGENTINA AFIP mediante el patrón de expresión regular:

```
<tipoComprobante>001\s*</tipoComprobante>
```

El tipo `001` corresponde a **Factura A** (factura a compradores registrados en el IVA). Los demás tipos de comprobante son gestionados por el estándar ARGENTINA FACTURA ELECTRONICA.

## Documentos relacionados

* [ARGENTINA FACTURA ELECTRONICA](argentina-factura-electronica.md)
* [Documentos electrónicos compatibles](./)
