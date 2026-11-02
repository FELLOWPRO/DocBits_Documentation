# Caso 6: Cantidad dentro de tolerancia y precio inferior al permitido (rechazado)

El siguiente escenario es un ejemplo de asignación configurada, no una plantilla predeterminada cuyo despliegue se haya verificado. La salida real, los importes, los signos y los tipos de documento dependen de las reglas y expresiones `conflict_resolution` activas, de la asignación de exportación y de las decisiones de aprobación. Cualquier nota de débito o crédito descrita está condicionada a esa configuración; el ejemplo no garantiza su emisión automática ni el cumplimiento legal.

## Escenario

La cantidad está dentro de tolerancia, pero el precio unitario de la factura está por debajo del intervalo permitido y la desviación de precio no se ha aprobado.

## Acción ilustrativa

Una asignación configurada para utilizar el precio del PO tras el rechazo conservaría la cantidad y sustituiría el precio unitario de la factura por el del PO. Que la diferencia origine un ajuste, una nota de débito, una nota de crédito o ningún documento separado depende de la asignación activa y de las aprobaciones. Los cargos de cabecera adicionales solo se aplican si están configurados expresamente.

## Ejemplo

* **Pedido de compra (PO):**
  * Cantidad: 100 unidades
  * Precio unitario: $10.00 por unidad
  * Total: $1,000.00
* **Factura recibida:**
  * Cantidad: 100 unidades — desviación real del 0%, dentro de la tolerancia configurada de ±2%.
  * Precio unitario: $9.00 — desviación real del -10%, fuera de la tolerancia configurada de ±1%; rechazada.
  * Total: $900.00
* **Tolerancias configuradas:**
  * Cantidad: ±2%
  * Precio unitario: ±1%

En esta asignación ilustrativa:

1. Se rechaza el precio unitario facturado de $9.00 porque la desviación supera la tolerancia y no está aprobada.
2. Se utiliza el precio unitario del PO de $10.00.
3. Se recalcula el total del ejemplo: **100 unidades × $10.00 = $1,000.00**.
4. Se calcula la diferencia con signo como total facturado menos total recalculado: **$900.00 - $1,000.00 = -$100.00**.
5. Se aplica la asignación de exportación y la decisión de aprobación configuradas. El valor -$100.00 es una diferencia con signo, no una instrucción incondicional de emitir una nota de crédito. La asignación determina el importe, el signo y el tipo de documento de cualquier ajuste.

Este ejemplo no significa que una nota de crédito revierta automáticamente un importe cobrado de menos. Confirme el tratamiento contable previsto en la asignación de exportación activa antes de utilizar la regla.
