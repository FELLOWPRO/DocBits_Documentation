# Caso 15: Recargo de cabecera - Recargo por unidad fuera de la tolerancia (Rechazado)

El siguiente escenario es un ejemplo de asignación configurada, no una plantilla predeterminada cuyo despliegue se haya verificado. La salida real, los importes, los signos y los tipos de documento dependen de las reglas y expresiones `conflict_resolution` activas, de la asignación de exportación y de las decisiones de aprobación. Cualquier nota de débito o crédito descrita está condicionada a esa configuración; el ejemplo no garantiza su emisión automática ni el cumplimiento legal.

## Escenario:

El recargo de cabecera por unidad está fuera de tolerancia y no ha sido aprobado.

## Acción:

El sistema ajusta el recargo de cabecera para que coincida con la orden de compra, procesa la transacción en consecuencia y genera las notas necesarias.

## Ejemplo:

* **Purchase Order (PO):**
  * Recargo de cabecera por unidad: $4.00
  * Quantity: 1,500 units
  * Monto total del recargo de cabecera: $6,000.00
* **Invoice Received:**
  * Recargo de cabecera por unidad: $5.00 (fuera de la tolerancia del 25%, rechazado)
  * Quantity: 1,500 units
  * Monto total del recargo de cabecera: $7,500.00
* **Tolerance Levels:**
  * Tolerancia del recargo por unidad del encabezado: ±5%

Dado que el cargo por unidad ($5.00) excede el rango de tolerancia aceptable del 5% y no ha sido aprobado, el sistema:

1. **Rechazar el recargo de cabecera facturado por unidad:** El sistema no acepta el recargo de cabecera facturado por unidad de $5.00 debido a que la variación excede el límite de tolerancia.
2. **Ajustar el recargo de cabecera por unidad:** El sistema ajusta el cargo por unidad para que coincida con la orden de compra original o el cargo aprobado por unidad:
   * Recargo de cabecera ajustado por unidad = $4.00 (desde PO)
3. **Recalcular el monto total del recargo de cabecera:** El sistema vuelve a calcular el monto total del cargo en función del cargo ajustado por unidad:
   * **Monto total corregido del recargo de cabecera = Cantidad × Recargo de cabecera ajustado por unidad**
   * **Monto total corregido del recargo de cabecera = 1,500 unidades × $4.00 = $6,000.00**
4. **Generar una nota de crédito:** Dado que el total de la factura original era mayor que el total corregido, el sistema genera una nota de crédito por el monto cobrado de más:
   * **Monto de la nota de crédito = Total de la factura original - Monto total corregido del recargo de cabecera**
   * **Monto de la nota de crédito = $7,500.00 - $6,000.00 = $1,500.00**
5. **Procesar la factura:** El sistema procesa la factura con el monto de cargo total corregido de $6,000.00 y emite una nota de crédito por $1,500.00 para contabilizar el monto cobrado de más.

Este enfoque garantiza que la transacción esté alineada con los términos originales de la orden de compra, manteniendo un procesamiento financiero preciso y corrigiendo cualquier sobrecargo.
