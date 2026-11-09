# Recargo por unidad fuera de la tolerancia (Rechazado)

El siguiente escenario es un ejemplo de asignación configurada, no una plantilla predeterminada cuyo despliegue se haya verificado. La salida real, los importes, los signos y los tipos de documento dependen de las reglas y expresiones `conflict_resolution` activas, de la asignación de exportación y de las decisiones de aprobación. Cualquier nota de débito o crédito descrita está condicionada a esa configuración; el ejemplo no garantiza su emisión automática ni el cumplimiento legal.

## Escenario:

El cargo por unidad está fuera de tolerancia y no ha sido aprobado.

## Acción:

El sistema ajusta el cargo por unidad para que coincida con la orden de compra o los niveles aprobados, generando las notas de débito o crédito necesarias.

## Ejemplo:

* **Purchase Order (PO):**
  * Charge Per Unit: $6.00
  * Quantity: 800 units
  * Total Charge Amount: $4,800.00
* **Invoice Received:**
  * Charge Per Unit: $7.00 (variance 16.67%, outside the ±5% tolerance, rejected)
  * Quantity: 800 units
  * Total Charge Amount: $5,600.00
* **Tolerance Levels:**
  * Charge Per Unit Tolerance: ±5%

Dado que Charge Per Unit ($7.00) excede el rango de tolerancia aceptable del 5% y no ha sido aprobado, el sistema:

1. **Reject the Invoiced Charge Per Unit:** El sistema no acepta el valor de Charge Per Unit de $7.00 debido a que la variación excede el límite de tolerancia.
2. **Adjust the Charge Per Unit:** El sistema ajusta Charge Per Unit para que coincida con la orden de compra o el valor aprobado de Charge Per Unit:
   * Adjusted Charge Per Unit = $6.00 (from PO)
3. **Recalculate the Total Charge Amount:** El sistema vuelve a calcular el Total Charge Amount en función del Charge Per Unit ajustado:
   * **Corrected Total Charge Amount = Quantity × Adjusted Charge Per Unit**
   * **Corrected Total Charge Amount = 800 units × $6.00 = $4,800.00**
4. **Generate a Debit Note:** Dado que el total de la factura original era mayor que el total corregido, el sistema genera una nota de débito por el monto cobrado de más:
   * **Debit Note Amount = Original Invoice Total - Corrected Total Charge Amount**
   * **Debit Note Amount = $5,600.00 - $4,800.00 = $800.00**
5. **Process the Invoice:** El sistema procesa la factura con el Total Charge Amount corregido de $4,800.00 y emite una nota de débito por $800.00 para contabilizar el monto cobrado de más.

Este enfoque garantiza que las transacciones financieras sean coherentes con los términos de la orden de compra, rechazando variaciones no aprobadas y manteniendo prácticas de facturación precisas.
