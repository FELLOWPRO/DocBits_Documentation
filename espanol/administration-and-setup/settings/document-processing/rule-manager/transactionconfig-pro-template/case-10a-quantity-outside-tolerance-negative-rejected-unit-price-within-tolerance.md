# Caso 10a: desviación negativa de cantidad rechazada; precio dentro de tolerancia

El siguiente escenario es un ejemplo de asignación configurada, no una plantilla predeterminada cuyo despliegue se haya verificado. La salida real, los importes, los signos y los tipos de documento dependen de las reglas y expresiones `conflict_resolution` activas, de la asignación de exportación y de las decisiones de aprobación. Cualquier nota de débito o crédito descrita está condicionada a esa configuración; el ejemplo no garantiza su emisión automática ni el cumplimiento legal.

## Escenario:

La cantidad está por debajo del rango aceptable (tolerancia negativa) y no está aprobada, aunque el precio unitario está dentro de la tolerancia.

## Acción:

El sistema ajusta la cantidad para que coincida con el nivel aprobado, manteniendo constante el precio unitario. La transacción se procesa en consecuencia.

## Ejemplo:

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Precio unitario: $20.00 por unidad
  * Total Amount: $3,000.00
* **Invoice Received:**
  * Cantidad: 140 unidades (fuera de tolerancia del -6.67%, rechazada)
  * Precio unitario: $20.00 por unidad (dentro de la tolerancia)
  * Total Amount: $2,800.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Tolerancia del precio unitario: ±2%

Dado que la cantidad (140 unidades) está por debajo del límite de tolerancia aceptable (variación negativa de -6.67%) y no está aprobada, pero el precio unitario ($20.00) está dentro de la tolerancia, el sistema:

1. **Rechazar la cantidad inferior:** El sistema no acepta la cantidad inferior porque está fuera del rango de tolerancia aprobado.
2. **Ajustar la cantidad:** El sistema ajusta la cantidad para que coincida con el nivel aprobado especificado en la orden de compra.
   * Cantidad aprobada = 150 unidades (desde PO)
3. **Mantener el precio unitario:** El precio unitario de $20.00 por unidad está dentro de la tolerancia y permanece sin cambios.
4. **Recalcular el monto total:** El sistema calcula el monto total utilizando la cantidad aprobada y el precio unitario aceptado:
   * **Monto total = Cantidad aprobada × Precio unitario**
   * **Monto total = 150 unidades × $20.00 por unidad = $3,000.00**
5. **Procesar la factura:** El sistema procesa la factura con el monto total ajustado de $3,000.00, reflejando la cantidad aprobada y el precio unitario. Se espera que el proveedor facture la cantidad total aprobada.

Este enfoque garantiza que la transacción financiera se alinee con los términos de la orden de compra y evita la subfacturación mientras se mantienen registros financieros precisos.
