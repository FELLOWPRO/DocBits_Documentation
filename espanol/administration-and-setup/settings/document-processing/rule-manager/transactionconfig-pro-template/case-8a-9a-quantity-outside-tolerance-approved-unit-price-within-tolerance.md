# Caso 8a, 9a: Cantidad fuera de la tolerancia (Aprobado), Precio unitario dentro de la tolerancia

El siguiente escenario es un ejemplo de asignación configurada, no una plantilla predeterminada cuyo despliegue se haya verificado. La salida real, los importes, los signos y los tipos de documento dependen de las reglas y expresiones `conflict_resolution` activas, de la asignación de exportación y de las decisiones de aprobación. Cualquier nota de débito o crédito descrita está condicionada a esa configuración; el ejemplo no garantiza su emisión automática ni el cumplimiento legal.

## Escenario:

La cantidad en la factura está fuera de la tolerancia aceptable pero ha sido aprobada, mientras que el precio unitario permanece dentro de la tolerancia.

## Acción:

El sistema acepta la cantidad aprobada y el precio unitario según la factura y procesa la transacción en consecuencia.

## Ejemplo:

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Precio unitario: $12.00 por unidad
  * Total Amount: $1,800.00
* **Invoice Received:**
  * Cantidad: 160 unidades (fuera de tolerancia del 6.67% pero aprobada)
  * Precio unitario: $12.00 por unidad (dentro de la tolerancia)
  * Total Amount: $1,920.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Tolerancia del precio unitario: ±2%

Dado que la cantidad (160 unidades) excede el límite de tolerancia aceptable pero ha sido aprobada, y el precio unitario ($12.00) está dentro del rango aceptable, el sistema:

1. **Aceptar la cantidad aprobada:** El sistema reconoce que la cantidad ha sido aprobada a pesar de estar fuera del rango de tolerancia normal.
2. **Aceptar el Precio Unitario:** El precio unitario de $12.00 por unidad está dentro de la tolerancia aceptable, por lo que se acepta como facturado.
3. **Procesar la transacción:** El sistema calcula el monto total utilizando la cantidad aprobada y el precio unitario:
   * **Monto total = Cantidad × Precio unitario**
   * **Monto total = 160 unidades × $12.00 por unidad = $1,920.00**
4. **Finalizar la factura:** El sistema procesa la factura con el monto total de $1,920.00, reflejando la cantidad aprobada y el precio unitario aceptado.

Este enfoque permite que el sistema se adapte a las variaciones de cantidad aprobadas y, al mismo tiempo, garantiza que el precio unitario se mantenga dentro del rango esperado, lo que facilita el procesamiento de transacciones sin problemas.
