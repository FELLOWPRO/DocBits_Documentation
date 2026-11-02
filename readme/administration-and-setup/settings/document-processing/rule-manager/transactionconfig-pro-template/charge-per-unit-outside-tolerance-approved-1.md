# Caso 14: Línea de recargo - Recargo por unidad fuera de la tolerancia (Aprobado)

El siguiente escenario es un ejemplo de asignación configurada, no una plantilla predeterminada cuyo despliegue se haya verificado. La salida real, los importes, los signos y los tipos de documento dependen de las reglas y expresiones `conflict_resolution` activas, de la asignación de exportación y de las decisiones de aprobación. Cualquier nota de débito o crédito descrita está condicionada a esa configuración; el ejemplo no garantiza su emisión automática ni el cumplimiento legal.

## Escenario:

El cargo por unidad está fuera de tolerancia pero ha sido aprobado.

## Acción:

El sistema acepta el cargo por unidad y aplica los cargos aprobados, procesando la transacción en consecuencia.

## Ejemplo:

* **Purchase Order (PO):**
  * Cargo por unidad: $4.50
  * Quantity: 1,000 units
  * Total Charge Amount: $4,500.00
* **Invoice Received:**
  * Cargo por unidad: $5.00 (fuera de la tolerancia del 11.11%, aprobada)
  * Quantity: 1,000 units
  * Total Charge Amount: $5,000.00
* **Tolerance Levels:**
  * Tolerancia del recargo por unidad: ±5%

Dado que el cargo por unidad ($5.00) está fuera del rango de tolerancia aceptable del 5 % pero ha sido aprobado, el sistema:

1. **Aceptar el cargo aprobado por unidad:** El sistema acepta el cargo facturado por unidad de $5.00 ya que ha sido aprobado a pesar de exceder el límite de tolerancia.
2. **Procesar la Transacción:** El sistema procesa la factura utilizando el cargo aprobado por unidad y la cantidad:
   * **Monto total del cargo = Cantidad × Cargo aprobado por unidad**
   * **Monto total del cargo = 1,000 unidades × $5.00 = $5,000.00**
3. **Finalizar Factura:** El sistema procesa la transacción con los cargos aprobados, reflejando el monto total de $5,000.00.

Este enfoque garantiza que el sistema pueda adaptarse a las variaciones aprobadas en los cargos, lo que permite flexibilidad y al mismo tiempo mantiene registros financieros precisos.
