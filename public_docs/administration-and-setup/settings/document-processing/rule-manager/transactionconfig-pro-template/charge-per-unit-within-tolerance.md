# Recargo por unidad dentro de la tolerancia

El siguiente escenario es un ejemplo de asignación configurada, no una plantilla predeterminada cuyo despliegue se haya verificado. La salida real, los importes, los signos y los tipos de documento dependen de las reglas y expresiones `conflict_resolution` activas, de la asignación de exportación y de las decisiones de aprobación. Cualquier nota de débito o crédito descrita está condicionada a esa configuración; el ejemplo no garantiza su emisión automática ni el cumplimiento legal.

## Escenario:

El Charge Per Unit de la factura está dentro del rango de tolerancia aceptable en comparación con la orden de compra.

## Acción:

El sistema acepta el Charge Per Unit como facturado y procesa la transacción sin ajustes.

## Ejemplo:

* **Purchase Order (PO):**
  * Charge Per Unit: $5.00
  * Quantity: 500 units
  * Total Charge Amount: $2,500.00
* **Invoice Received:**
  * Charge Per Unit: $5.10 (variación 2%, dentro de la tolerancia de ±3%)
  * Quantity: 500 units
  * Total Charge Amount: $2,550.00
* **Tolerance Levels:**
  * Charge Per Unit Tolerance: ±3%

Dado que el Charge Per Unit ($5.10) está dentro del rango de tolerancia aceptable del 3% en comparación con la orden de compra, el sistema:

1. **Accept the Charge Per Unit:** El sistema acepta el Charge Per Unit facturado de $5.10 ya que se encuentra dentro del límite de tolerancia definido.
2. **Process the Transaction:** El sistema procesa la factura con el Total Charge Amount en función del Charge Per Unit facturado y de la Quantity:
   * **Total Charge Amount = Quantity × Charge Per Unit**
   * **Total Charge Amount = 500 units × $5.10 = $2,550.00**
3. **Finalize the Invoice:** El sistema procesa la transacción sin ningún ajuste, aceptando la factura tal como está.

Este enfoque permite que el sistema se adapte a variaciones menores aceptables en los cargos, lo que garantiza un procesamiento fluido y eficiente de las transacciones sin rechazos ni demoras innecesarias.
