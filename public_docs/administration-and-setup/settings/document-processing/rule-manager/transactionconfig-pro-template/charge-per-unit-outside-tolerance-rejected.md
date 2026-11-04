# Caso 15: Cargo de línea por unidad fuera de tolerancia (rechazado)

El siguiente escenario es un ejemplo de asignación configurada, no una plantilla predeterminada cuyo despliegue se haya verificado. La salida real, los importes, los signos y los tipos de documento dependen de las reglas y expresiones `conflict_resolution` activas, de la asignación de exportación y de las decisiones de aprobación. Cualquier nota de débito o crédito descrita está condicionada a esa configuración; el ejemplo no garantiza su emisión automática ni el cumplimiento legal.

## Escenario

El cargo por unidad de una línea está fuera de tolerancia y la desviación no se ha aprobado. Este caso trata de un cargo de línea, no de un cargo de cabecera.

## Acción ilustrativa

Una asignación configurada para utilizar el cargo del PO tras el rechazo sustituiría el cargo unitario de la factura por el del PO. Cualquier ajuste o nota de débito o crédito depende de la asignación de exportación y de las decisiones de aprobación.

## Ejemplo

* **Pedido de compra (PO):**
  * Cargo de línea por unidad: $4.00
  * Cantidad: 1,500 unidades
  * Cargo de línea total: $6,000.00
* **Factura recibida:**
  * Cargo de línea por unidad: $5.00 — un 25% superior al PO, fuera de la tolerancia configurada de ±5%; rechazado.
  * Cantidad: 1,500 unidades
  * Cargo de línea total: $7,500.00
* **Tolerancia configurada:** Cargo por unidad ±5%.

En esta asignación ilustrativa:

1. Se rechaza el cargo facturado de $5.00 por unidad porque la desviación del 25% supera ±5% y no está aprobada.
2. Se utiliza el cargo del PO de $4.00 por unidad.
3. Se recalcula el cargo de línea total: **1,500 unidades × $4.00 = $6,000.00**.
4. Se calcula el exceso facturado: **$7,500.00 - $6,000.00 = $1,500.00**.
5. Se aplica el tratamiento configurado para la diferencia. Una nota de crédito de $1,500.00 es un resultado posible de la asignación, no una acción garantizada. Su importe, signo, tipo de documento y emisión dependen de las reglas activas, de la asignación de exportación y de las aprobaciones.

Valide la asignación de cargos de línea y los documentos contables resultantes antes de utilizar este escenario en producción.
