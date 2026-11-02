# Recargo por unidad fuera de la tolerancia (Rechazado)

El siguiente escenario es un ejemplo de asignación configurada, no una plantilla predeterminada cuyo despliegue se haya verificado. La salida real, los importes, los signos y los tipos de documento dependen de las reglas y expresiones `conflict_resolution` activas, de la asignación de exportación y de las decisiones de aprobación. Cualquier nota de débito o crédito descrita está condicionada a esa configuración; el ejemplo no garantiza su emisión automática ni el cumplimiento legal.

## Escenario:

El cargo por unidad está fuera de tolerancia y no ha sido aprobado.

## Acción:

El sistema ajusta el cargo por unidad para que coincida con la orden de compra o los niveles aprobados, generando las notas de débito o crédito necesarias.

## Ejemplo:

* **Purchase Order (PO):**
  * Cargo por unidad: $6.00
  * Quantity: 800 units
  * Total Charge Amount: $4,800.00
* **Invoice Received:**
  * Cargo por unidad: $7.00 (fuera de la tolerancia del 16.67%, rechazado)
  * Quantity: 800 units
  * Total Charge Amount: $5,600.00
* **Tolerance Levels:**
  * Tolerancia del recargo por unidad: ±5%

Dado que el cargo por unidad ($7.00) excede el rango de tolerancia aceptable del 5% y no ha sido aprobado, el sistema:

1. **Rechazar el cargo facturado por unidad:** El sistema no acepta el cargo facturado por unidad de $7.00 debido a que la variación excede el límite de tolerancia.
2. **Ajustar el cargo por unidad:** El sistema ajusta el cargo por unidad para que coincida con la orden de compra o el cargo por unidad aprobado:
   * Cargo ajustado por unidad = $6.00 (desde PO)
3. **Recalcular el monto total del cargo:** El sistema vuelve a calcular el monto total del cargo en función del cargo ajustado por unidad:
   * **Monto de cargo total corregido = Cantidad × Cargo ajustado por unidad**
   * **Monto de cargo total corregido = 800 unidades × $6.00 = $4,800.00**
4. **Generar una Nota de Débito:** Dado que el total de la factura original era mayor que el total corregido, el sistema genera una nota de débito por el monto cobrado de más:
   * **Monto de la nota de débito = Total de la factura original - Monto total del cargo corregido**
   * **Monto de la Nota de Débito = $5,600.00 - $4,800.00 = $800.00**
5. **Procesar la factura:** El sistema procesa la factura con el monto de cargo total corregido de $4,800.00 y emite una nota de débito por $800.00 para contabilizar el monto cobrado de más.

Este enfoque garantiza que las transacciones financieras sean coherentes con los términos de la orden de compra, rechazando variaciones no aprobadas y manteniendo prácticas de facturación precisas.
