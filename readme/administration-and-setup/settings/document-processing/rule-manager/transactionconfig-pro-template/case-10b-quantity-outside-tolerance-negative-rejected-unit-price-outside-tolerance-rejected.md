# Caso 10b: desviación negativa de cantidad y precio fuera de tolerancia rechazados

El siguiente escenario es un ejemplo de asignación configurada, no una plantilla predeterminada cuyo despliegue se haya verificado. La salida real, los importes, los signos y los tipos de documento dependen de las reglas y expresiones `conflict_resolution` activas, de la asignación de exportación y de las decisiones de aprobación. Cualquier nota de débito o crédito descrita está condicionada a esa configuración; el ejemplo no garantiza su emisión automática ni el cumplimiento legal.

## Escenario:

Tanto la cantidad como el precio unitario están fuera de tolerancia y ninguno de los dos ha sido aprobado.

## Acción:

El sistema rechaza los datos de la factura, ajusta los valores para que coincidan con la orden de compra y genera las notas de débito o crédito necesarias.

## Ejemplo:

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Precio unitario: $30.00 por unidad
  * Total Amount: $4,500.00
* **Invoice Received:**
  * Cantidad: 140 unidades (fuera de tolerancia del -6.67%, rechazada)
  * Precio unitario: $33.00 por unidad (fuera de la tolerancia del 10%, rechazado)
  * Total Amount: $4,620.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Tolerancia del precio unitario: ±2%

Dado que tanto la cantidad (140 unidades) como el precio unitario ($33.00) están fuera de los límites de tolerancia aceptables y ninguno ha sido aprobado, el sistema:

1. **Rechazar los datos de la factura:** El sistema no acepta la cantidad facturada o el precio unitario debido a su desviación de los límites de tolerancia.
2. **Ajustar la cantidad:** El sistema ajusta la cantidad para que coincida con la cantidad de la orden de compra original.
   * Cantidad ajustada = 150 unidades (desde PO)
3. **Ajustar el precio unitario:** El sistema ajusta el precio unitario para que coincida con el precio unitario de la orden de compra original.
   * Precio unitario ajustado = $30.00 por unidad (desde PO)
4. **Recalcular el monto total:** El sistema vuelve a calcular el monto total utilizando la cantidad ajustada y el precio unitario:
   * **Monto total corregido = Cantidad ajustada × Precio unitario ajustado**
   * **Monto total corregido = 150 unidades × $30.00 por unidad = $4,500.00**
5. **Generar una nota de débito:** Dado que el total de la factura original era mayor que el total corregido, el sistema genera una nota de débito por el monto cobrado de más.
   * **Monto de la nota de débito = Total de la factura original - Monto total corregido**
   * **Monto de la Nota de Débito = $4,620.00 - $4,500.00 = $120.00**
6. **Procesar la Factura:** El sistema procesa la factura con el monto total corregido de $4,500.00 y emite una nota de débito por $120.00 para compensar el monto cobrado de más.

Este enfoque garantiza que la transacción financiera se corrija para que coincida con los términos de la orden de compra, manteniendo prácticas de facturación precisas y justas.
