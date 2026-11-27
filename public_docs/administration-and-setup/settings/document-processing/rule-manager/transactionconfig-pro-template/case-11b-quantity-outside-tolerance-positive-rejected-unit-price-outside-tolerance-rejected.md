# Caso 11b: exceso de cantidad y precio fuera de tolerancia rechazados

El siguiente escenario es un ejemplo de asignación configurada, no una plantilla predeterminada cuyo despliegue se haya verificado. La salida real, los importes, los signos y los tipos de documento dependen de las reglas y expresiones `conflict_resolution` activas, de la asignación de exportación y de las decisiones de aprobación. Cualquier nota de débito o crédito descrita está condicionada a esa configuración; el ejemplo no garantiza su emisión automática ni el cumplimiento legal.

## Escenario:

La cantidad excede el rango aceptable (positivo) y se rechaza, y el precio unitario también está fuera de tolerancia y se rechaza.

## Acción:

El sistema ajusta la cantidad y el precio unitario para que coincidan con los niveles aprobados de la orden de compra, rechaza cualquier exceso y procesa la transacción.

## Ejemplo:

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Unit Price: $50.00 per unit
  * Total Amount: $10,000.00
* **Invoice Received:**
  * Quantity: 220 units — 10% above the PO value, outside the configured ±5% tolerance; rejected.
  * Unit Price: $55.00 per unit — 10% above the PO value, outside the configured ±2% tolerance; rejected.
  * Total Amount: $12,100.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Dado que tanto la cantidad (220 unidades) como el precio unitario ($55.00) exceden los límites de tolerancia aceptables y ninguno ha sido aprobado, el sistema:

1. **Reject the Excess Quantity:** El sistema no acepta la cantidad facturada de 220 unidades y la ajusta para que coincida con la orden de compra original.
   * Adjusted Quantity = 200 units (from PO)
2. **Reject the Invoice Unit Price:** El sistema no acepta el precio unitario facturado de $55.00 y lo ajusta para que coincida con la orden de compra original.
   * Adjusted Unit Price = $50.00 per unit (from PO)
3. **Recalculate the Total Amount:** El sistema calcula el monto total utilizando la cantidad ajustada y el precio unitario:
   * **Corrected Total Amount = Adjusted Quantity × Adjusted Unit Price**
   * **Corrected Total Amount = 200 units × $50.00 per unit = $10,000.00**
4. **Process the Invoice:** El sistema procesa la factura con el monto total corregido de $10,000.00, rechazando la cantidad excedente y el precio unitario mayor.

Este enfoque garantiza que la transacción se alinee con los términos originales de la orden de compra, manteniendo controles consistentes de precios y cantidades al tiempo que rechaza variaciones no aprobadas.
