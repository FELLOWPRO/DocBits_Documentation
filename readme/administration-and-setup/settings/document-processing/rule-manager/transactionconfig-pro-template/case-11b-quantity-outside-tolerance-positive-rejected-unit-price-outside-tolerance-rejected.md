# Caso 11b: exceso de cantidad y precio fuera de tolerancia rechazados

El siguiente escenario es un ejemplo de asignación configurada, no una plantilla predeterminada cuyo despliegue se haya verificado. La salida real, los importes, los signos y los tipos de documento dependen de las reglas y expresiones `conflict_resolution` activas, de la asignación de exportación y de las decisiones de aprobación. Cualquier nota de débito o crédito descrita está condicionada a esa configuración; el ejemplo no garantiza su emisión automática ni el cumplimiento legal.

## Escenario:

La cantidad excede el rango aceptable (positivo) y se rechaza, y el precio unitario también está fuera de tolerancia y se rechaza.

## Acción:

El sistema ajusta la cantidad y el precio unitario para que coincidan con los niveles aprobados de la orden de compra, rechaza cualquier exceso y procesa la transacción.

## Ejemplo:

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Precio unitario: $50.00 por unidad
  * Total Amount: $10,000.00
* **Invoice Received:**
  * Cantidad: 220 unidades (fuera de tolerancia del 10%, rechazadas)
  * Precio unitario: $55.00 por unidad (fuera de la tolerancia del 10%, rechazado)
  * Total Amount: $12,100.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Tolerancia del precio unitario: ±2%

Dado que tanto la cantidad (220 unidades) como el precio unitario ($55.00) exceden los límites de tolerancia aceptables y ninguno ha sido aprobado, el sistema:

1. **Rechazar la cantidad en exceso:** El sistema no acepta la cantidad facturada de 220 unidades y la ajusta para que coincida con la orden de compra original.
   * Cantidad ajustada = 200 unidades (desde PO)
2. **Rechazar el precio unitario de la factura:** El sistema no acepta el precio unitario facturado de $55.00 y lo ajusta para que coincida con la orden de compra original.
   * Precio unitario ajustado = $50.00 por unidad (desde PO)
3. **Recalcular el monto total:** El sistema calcula el monto total utilizando la cantidad ajustada y el precio unitario:
   * **Monto total corregido = Cantidad ajustada × Precio unitario ajustado**
   * **Monto total corregido = 200 unidades × $50.00 por unidad = $10,000.00**
4. **Procesar la Factura:** El sistema procesa la factura con el monto total corregido de $10,000.00, rechazando la cantidad excedente y el precio unitario mayor.

Este enfoque garantiza que la transacción se alinee con los términos originales de la orden de compra, manteniendo controles consistentes de precios y cantidades al tiempo que rechaza variaciones no aprobadas.
