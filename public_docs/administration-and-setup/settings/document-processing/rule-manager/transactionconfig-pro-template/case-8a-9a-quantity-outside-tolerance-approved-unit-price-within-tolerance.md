# Caso 8a, 9a: Cantidad fuera de la tolerancia (Aprobado), Precio unitario dentro de la tolerancia

El siguiente escenario es un ejemplo de asignación configurada, no una plantilla predeterminada cuyo despliegue se haya verificado. La salida real, los importes, los signos y los tipos de documento dependen de las reglas y expresiones `conflict_resolution` activas, de la asignación de exportación y de las decisiones de aprobación. Cualquier nota de débito o crédito descrita está condicionada a esa configuración; el ejemplo no garantiza su emisión automática ni el cumplimiento legal.

## Escenario:

La cantidad en la factura está fuera de la tolerancia aceptable pero ha sido aprobada, mientras que el precio unitario permanece dentro de la tolerancia.

## Acción:

El sistema acepta la cantidad aprobada y el precio unitario según la factura y procesa la transacción en consecuencia.

## Ejemplo:

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Unit Price: $12.00 per unit
  * Total Amount: $1,800.00
* **Invoice Received:**
  * Quantity: 160 units — 6.67% above the PO value, outside the configured ±5% tolerance; approved.
  * Unit Price: $12.00 per unit (within tolerance)
  * Total Amount: $1,920.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Dado que la cantidad (160 unidades) excede el límite de tolerancia aceptable pero ha sido aprobada, y el precio unitario ($12.00) está dentro del rango aceptable, el sistema:

1. **Aceptar la cantidad aprobada:** El sistema reconoce que la cantidad ha sido aprobada a pesar de estar fuera del rango de tolerancia normal.
2. **Aceptar el Precio Unitario:** El precio unitario de $12.00 por unidad está dentro de la tolerancia aceptable, por lo que se acepta como facturado.
3. **Procesar la transacción:** El sistema calcula el monto total utilizando la cantidad aprobada y el precio unitario:
   * **Total Amount = Quantity × Unit Price**
   * **Total Amount = 160 units × $12.00 per unit = $1,920.00**
4. **Finalizar la factura:** El sistema procesa la factura con el monto total de $1,920.00, reflejando la cantidad aprobada y el precio unitario aceptado.

Este enfoque permite que el sistema se adapte a las variaciones de cantidad aprobadas y, al mismo tiempo, garantiza que el precio unitario se mantenga dentro del rango esperado, lo que facilita el procesamiento de transacciones sin problemas.
