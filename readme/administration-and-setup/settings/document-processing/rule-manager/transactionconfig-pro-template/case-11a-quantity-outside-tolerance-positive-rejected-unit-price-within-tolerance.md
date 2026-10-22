# Caso 11a: exceso de cantidad rechazado; precio dentro de tolerancia

El siguiente escenario es un ejemplo de asignación configurada, no una plantilla predeterminada cuyo despliegue se haya verificado. La salida real, los importes, los signos y los tipos de documento dependen de las reglas y expresiones `conflict_resolution` activas, de la asignación de exportación y de las decisiones de aprobación. Cualquier nota de débito o crédito descrita está condicionada a esa configuración; el ejemplo no garantiza su emisión automática ni el cumplimiento legal.

## Escenario:

La cantidad en la factura excede el rango aceptable (positivo) y se rechaza, pero el precio unitario está dentro de la tolerancia.

## Acción:

El sistema ajusta la cantidad al nivel aprobado, mantiene el precio unitario y procesa la transacción. Cualquier exceso de cantidad se rechaza y no se factura.

## Ejemplo:

* **Purchase Order (PO):**
  * Quantity: 100 units
  * Precio unitario: $8.00 por unidad
  * Total Amount: $800.00
* **Invoice Received:**
  * Cantidad: 110 unidades (fuera de tolerancia del 10%, rechazadas)
  * Precio unitario: $8.00 por unidad (dentro de la tolerancia)
  * Total Amount: $880.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Tolerancia del precio unitario: ±2%

Dado que la cantidad (110 unidades) excede el límite de tolerancia aceptable (variación positiva del 10%) y no está aprobada, pero el precio unitario ($8.00) está dentro de la tolerancia, el sistema:

1. **Rechazar la cantidad en exceso:** El sistema rechaza la cantidad que excede el nivel de tolerancia aprobado.
2. **Ajustar la cantidad:** El sistema ajusta la cantidad para que coincida con el nivel aprobado especificado en la orden de compra.
   * Cantidad aprobada = 100 unidades (desde PO)
3. **Mantener el precio unitario:** El precio unitario de $8.00 por unidad está dentro de la tolerancia y permanece sin cambios.
4. **Recalcular el monto total:** El sistema calcula el monto total utilizando la cantidad aprobada y el precio unitario aceptado:
   * **Monto total = Cantidad aprobada × Precio unitario**
   * **Monto total = 100 unidades × $8.00 por unidad = $800.00**
5. **Procesar la factura:** El sistema procesa la factura con el monto total ajustado de $800.00, reflejando solo la cantidad aprobada y el precio unitario. La cantidad sobrante de 10 unidades se rechaza y no se factura.

Este enfoque garantiza que el importe facturado se alinee con los términos acordados en la orden de compra, incluso cuando el proveedor intenta facturar una cantidad excesiva.
