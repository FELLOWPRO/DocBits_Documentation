# Caso 7: cantidad dentro de tolerancia; aumento de precio rechazado

El siguiente escenario es un ejemplo de asignación configurada, no una plantilla predeterminada cuyo despliegue se haya verificado. La salida real, los importes, los signos y los tipos de documento dependen de las reglas y expresiones `conflict_resolution` activas, de la asignación de exportación y de las decisiones de aprobación. Cualquier nota de débito o crédito descrita está condicionada a esa configuración; el ejemplo no garantiza su emisión automática ni el cumplimiento legal.

## Escenario:

La cantidad está dentro de la tolerancia, pero el precio unitario excede el rango aceptable (tolerancia positiva) y no se aprueba.

## Acción:

El sistema rechaza el precio unitario de la factura, lo ajusta para que coincida con la orden de compra y puede generar una nota de débito para contabilizar el monto cobrado de más.

## Ejemplo:

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Precio unitario: $15.00 por unidad
  * Total Amount: $3,000.00
* **Invoice Received:**
  * Cantidad: 198 unidades (dentro de una tolerancia del 1%)
  * Precio unitario: $17.00 por unidad (fuera de la tolerancia positiva del 13.33%)
  * Total Amount: $3,366.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±2%
  * Tolerancia del precio unitario: ±1%

Dado que la cantidad (198 unidades) está dentro del rango de tolerancia aceptable pero el precio unitario ($17.00) excede la tolerancia aceptable y no está aprobado, el sistema:

1. **Rechazar el precio unitario facturado:** El sistema no acepta el precio unitario facturado de $17.00.
2. **Ajustar el precio unitario:** El sistema ajusta el precio unitario para que coincida con el precio unitario de la orden de compra original.
   * Precio unitario ajustado = $15.00 (desde PO)
3. **Calcular el monto total corregido:** Utilizando el precio unitario ajustado, el sistema vuelve a calcular el monto total.
   * **Monto total corregido = Cantidad × Precio unitario ajustado**
   * **Monto total corregido = 198 unidades × $15.00 por unidad = $2,970.00**
4. **Generar Nota de Débito:** El sistema genera una nota de débito para contabilizar la diferencia por el sobrecargo.
   * **Monto de la nota de débito = Total de la factura original - Monto total corregido**
   * **Monto de la nota de débito = $3,366.00 - $2,970.00 = $396.00**
   * Esta nota de débito representa el monto cobrado de más por el proveedor.
5. **Procesar la Factura:** El sistema procesa la factura con el monto total corregido de $2,970.00 y emite una nota de débito por $396.00 para compensar el sobrecargo.

Este enfoque garantiza que se corrija cualquier sobrecoste, alineando la transacción con los términos de la orden de compra y protegiendo los intereses financieros de la empresa.
