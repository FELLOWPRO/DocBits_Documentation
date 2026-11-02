# Caso 14: Recargo de cabecera - Recargo por unidad fuera de la tolerancia (Aprobado)

El siguiente escenario es un ejemplo de asignación configurada, no una plantilla predeterminada cuyo despliegue se haya verificado. La salida real, los importes, los signos y los tipos de documento dependen de las reglas y expresiones `conflict_resolution` activas, de la asignación de exportación y de las decisiones de aprobación. Cualquier nota de débito o crédito descrita está condicionada a esa configuración; el ejemplo no garantiza su emisión automática ni el cumplimiento legal.

## Escenario:

El recargo de cabecera por unidad está fuera de la tolerancia pero ha sido aprobado.

## Acción:

El sistema procesa el cargo aprobado por unidad, aplicándolo a la transacción.

## Ejemplo:

* **Purchase Order (PO):**
  * Recargo de cabecera por unidad: $2.50
  * Quantity: 2,000 units
  * Monto total del recargo de cabecera: $5,000.00
* **Invoice Received:**
  * Recargo de cabecera por unidad: $3.00 (fuera de la tolerancia del 20%, aprobado)
  * Quantity: 2,000 units
  * Monto total del recargo de cabecera: $6,000.00
* **Tolerance Levels:**
  * Tolerancia del recargo por unidad del encabezado: ±5%

Dado que el cargo por unidad ($3.00) excede el rango de tolerancia aceptable del 5% pero ha sido aprobado, el sistema:

1. **Aceptar el recargo de cabecera aprobado por unidad:** El sistema acepta el recargo de cabecera facturado por unidad de $3.00 ya que ha sido aprobado a pesar de exceder el límite de tolerancia.
2. **Procesar el Cargo de Cabecera:** El sistema procesa la factura utilizando el cargo aprobado por unidad y la cantidad:
   * **Monto total del recargo de cabecera = Cantidad × Recargo de cabecera aprobado por unidad**
   * **Monto total del recargo de cabecera = 2,000 unidades × $3.00 = $6,000.00**
3. **Finalizar Factura:** El sistema procesa la transacción con los cargos aprobados, reflejando el monto total de $6,000.00.

Este enfoque permite que el sistema se adapte a las variaciones aprobadas en los cargos de encabezado, lo que garantiza que la transacción se procese de acuerdo con la aprobación y al mismo tiempo se mantengan registros financieros precisos.
