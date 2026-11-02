# Líneas de impuestos

El siguiente escenario es un ejemplo de asignación configurada, no una plantilla predeterminada cuyo despliegue se haya verificado. La salida real, los importes, los signos y los tipos de documento dependen de las reglas y expresiones `conflict_resolution` activas, de la asignación de exportación y de las decisiones de aprobación. Cualquier nota de débito o crédito descrita está condicionada a esa configuración; el ejemplo no garantiza su emisión automática ni el cumplimiento legal.

## Escenario:

Maneja discrepancias en los montos de impuestos entre la factura y la orden de compra.

## Acción:

El sistema ajusta las líneas impositivas de acuerdo con las tasas y montos impositivos aprobados, asegurando el cumplimiento de las regulaciones tributarias aplicables.

## Ejemplo:

* **Purchase Order (PO):**
  * Subtotal Amount: $10,000.00
  * Tax Rate: 8%
  * Monto de impuesto esperado: $800.00
  * Monto Total con Impuesto: $10,800.00
* **Invoice Received:**
  * Subtotal Amount: $10,000.00
  * Tasa impositiva: 10% (discrepancia)
  * Monto del impuesto facturado: $1,000.00
  * Monto Total con Impuesto: $11,000.00

Dado que la tasa impositiva en la factura (10%) difiere de la tasa impositiva esperada (8%) y no se aprueba, el sistema:

1. **Rechazar la tasa impositiva facturada:** El sistema no acepta la tasa impositiva del 10% porque no coincide con la tasa aprobada en la orden de compra.
2. **Ajustar la tasa impositiva:** El sistema ajusta la tasa impositiva para que coincida con la tasa aprobada de la orden de compra.
   * Tasa impositiva ajustada = 8% (desde PO)
3. **Recalcular el monto del impuesto:** El sistema vuelve a calcular el monto del impuesto en función de la tasa impositiva ajustada:
   * **Monto de impuesto corregido = Monto subtotal × Tasa de impuesto ajustada**
   * **Monto de impuesto corregido = $10,000.00 × 8% = $800.00**
4. **Recalcular el monto total:** El sistema recalcula el monto total incluyendo impuestos:
   * **Monto Total Corregido con Impuesto = Monto Subtotal + Monto de Impuesto Corregido**
   * **Monto Total Corregido con Impuesto = $10,000.00 + $800.00 = $10,800.00**
5. **Generar una Nota de Crédito:** El sistema genera una nota de crédito para corregir el impuesto sobrecargado:
   * **Monto de la nota de crédito = Monto del impuesto de la factura original - Monto del impuesto corregido**
   * **Monto de la nota de crédito = $1,000.00 - $800.00 = $200.00**
6. **Procesar la Factura:** El sistema procesa la factura con el monto de impuesto corregido de $800.00 y el monto total de $10,800.00, emitiendo una nota de crédito por la discrepancia de impuesto de $200.00.

Este enfoque garantiza que el impuesto sobre la factura sea coherente con la orden de compra y cumpla con las normas fiscales aplicables, evitando el pago excesivo y garantizando la precisión de los registros financieros.
