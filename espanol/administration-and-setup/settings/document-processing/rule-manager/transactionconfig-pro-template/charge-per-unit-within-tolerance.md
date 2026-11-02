# Recargo por unidad dentro de la tolerancia

El siguiente escenario es un ejemplo de asignación configurada, no una plantilla predeterminada cuyo despliegue se haya verificado. La salida real, los importes, los signos y los tipos de documento dependen de las reglas y expresiones `conflict_resolution` activas, de la asignación de exportación y de las decisiones de aprobación. Cualquier nota de débito o crédito descrita está condicionada a esa configuración; el ejemplo no garantiza su emisión automática ni el cumplimiento legal.

## Escenario:

El cargo por unidad en la factura está dentro del rango de tolerancia aceptable en comparación con la orden de compra.

## Acción:

El sistema acepta el cargo por unidad como facturado y procesa la transacción sin ajustes.

## Ejemplo:

* **Purchase Order (PO):**
  * Cargo por unidad: $5.00
  * Quantity: 500 units
  * Total Charge Amount: $2,500.00
* **Invoice Received:**
  * Cargo por unidad: $5.10 (dentro de la tolerancia del 2%)
  * Quantity: 500 units
  * Total Charge Amount: $2,550.00
* **Tolerance Levels:**
  * Tolerancia del recargo por unidad: ±3%

Dado que el cargo por unidad ($5.10) está dentro del rango de tolerancia aceptable del 3% en comparación con la orden de compra, el sistema:

1. **Aceptar el cargo por unidad:** El sistema acepta el cargo facturado por unidad de $5.10 ya que se encuentra dentro del límite de tolerancia definido.
2. **Procesar la transacción:** El sistema procesa la factura con el monto total del cargo en función del cargo facturado por unidad y cantidad:
   * **Monto total del cargo = Cantidad × Cargo por unidad**
   * **Monto total del cargo = 500 unidades × $5.10 = $2,550.00**
3. **Finalizar Factura:** El sistema procesa la transacción sin ningún ajuste, aceptando la factura tal como está.

Este enfoque permite que el sistema se adapte a variaciones menores aceptables en los cargos, lo que garantiza un procesamiento fluido y eficiente de las transacciones sin rechazos ni demoras innecesarias.
