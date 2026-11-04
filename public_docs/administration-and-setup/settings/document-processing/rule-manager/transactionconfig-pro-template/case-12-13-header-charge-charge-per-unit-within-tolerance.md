# Recargo por unidad dentro de la tolerancia

El siguiente escenario es un ejemplo de asignación configurada, no una plantilla predeterminada cuyo despliegue se haya verificado. La salida real, los importes, los signos y los tipos de documento dependen de las reglas y expresiones `conflict_resolution` activas, de la asignación de exportación y de las decisiones de aprobación. Cualquier nota de débito o crédito descrita está condicionada a esa configuración; el ejemplo no garantiza su emisión automática ni el cumplimiento legal.

## Escenario:

El recargo de cabecera por unidad está dentro del rango de tolerancia aceptable en comparación con la orden de compra.

## Acción:

El sistema procesa el cargo de cabecera tal como facturado, aplicándolo sin ajustes.

## Ejemplo:

* **Purchase Order (PO):**
  * Recargo de cabecera por unidad: $3.50
  * Quantity: 1,200 units
  * Monto total del recargo de cabecera: $4,200.00
* **Invoice Received:**
  * Recargo de cabecera por unidad: $3.55 (dentro de la tolerancia del 1.43%)
  * Quantity: 1,200 units
  * Monto total del recargo de cabecera: $4,260.00
* **Tolerance Levels:**
  * Tolerancia del recargo por unidad del encabezado: ±2%

Dado que el recargo de cabecera por unidad ($3.55) está dentro del rango de tolerancia aceptable del 2% en comparación con la orden de compra, el sistema:

1. **Aceptar el recargo de cabecera por unidad:** El sistema acepta el recargo de cabecera facturado por unidad de $3.55 ya que se encuentra dentro del límite de tolerancia definido.
2. **Procesar el recargo de cabecera:** El sistema procesa la factura con el monto total del recargo de cabecera según el cargo facturado por unidad y cantidad:
   * **Monto total del recargo de cabecera = Cantidad × Recargo de cabecera por unidad**
   * **Monto total del recargo de cabecera = 1,200 unidades × $3.55 = $4,260.00**
3. **Finalizar Factura:** El sistema procesa la transacción sin ningún ajuste, aceptando la factura tal como está.

Este enfoque garantiza un procesamiento fluido y eficiente de las transacciones cuando los cargos del encabezado se encuentran dentro del rango de tolerancia aceptable, evitando rechazos o demoras innecesarias.
