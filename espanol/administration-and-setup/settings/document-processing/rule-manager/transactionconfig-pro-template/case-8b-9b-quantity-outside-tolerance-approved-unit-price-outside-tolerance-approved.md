# Casos 8b y 9b: cantidad y precio fuera de tolerancia, aprobados

El siguiente escenario es un ejemplo de asignación configurada, no una plantilla predeterminada cuyo despliegue se haya verificado. La salida real, los importes, los signos y los tipos de documento dependen de las reglas y expresiones `conflict_resolution` activas, de la asignación de exportación y de las decisiones de aprobación. Cualquier nota de débito o crédito descrita está condicionada a esa configuración; el ejemplo no garantiza su emisión automática ni el cumplimiento legal.

## Escenario:

Tanto la cantidad como el precio unitario están fuera del rango de tolerancia pero han sido aprobados.

## Acción:

El sistema procesa la transacción utilizando los valores de la factura tanto para la cantidad como para el precio unitario, aplicando los ajustes o cargos de línea necesarios.

## Ejemplo:

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Precio unitario: $25.00 por unidad
  * Total Amount: $5,000.00
* **Invoice Received:**
  * Cantidad: 220 unidades (fuera de tolerancia del 10%, aprobada)
  * Precio unitario: $27.00 por unidad (fuera de la tolerancia del 8%, aprobado)
  * Total Amount: $5,940.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Tolerancia del precio unitario: ±2%

Dado que tanto la cantidad (220 unidades) como el precio unitario ($27.00) están fuera de los límites de tolerancia aceptables pero han sido aprobados, el sistema:

1. **Aceptar la Cantidad Aprobada:** El sistema acepta la cantidad facturada de 220 unidades ya que ha sido aprobada a pesar de estar fuera del rango de tolerancia.
2. **Aceptar el precio unitario aprobado:** El sistema acepta el precio unitario facturado de $27.00 por unidad ya que ha sido aprobado a pesar de estar fuera del rango de tolerancia.
3. **Calcular el monto total:** El sistema calcula el monto total en función de los valores de factura aprobados:
   * **Monto total = Cantidad × Precio unitario**
   * **Monto total = 220 unidades × $27.00 por unidad = $5,940.00**
4. **Aplicar ajustes o cargos de línea necesarios:** Si corresponde, el sistema puede aplicar cualquier cargo o ajuste de línea adicional según las políticas de la organización para el manejo de las variaciones aprobadas.
5. **Procesar la factura:** El sistema procesa la factura utilizando los valores aprobados tanto para cantidad como para precio unitario, finalizando la transacción por un monto total de $5,940.00.

Este enfoque garantiza que la transacción se procese de acuerdo con las variaciones aprobadas, lo que permite flexibilidad y al mismo tiempo mantiene registros financieros precisos.
