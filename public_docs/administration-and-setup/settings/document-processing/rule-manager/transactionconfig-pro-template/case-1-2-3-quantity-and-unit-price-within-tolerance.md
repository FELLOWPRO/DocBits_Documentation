# Caso 1, 2, 3: Cantidad y precio unitario dentro de la tolerancia

El siguiente escenario es un ejemplo de asignación configurada, no una plantilla predeterminada cuyo despliegue se haya verificado. La salida real, los importes, los signos y los tipos de documento dependen de las reglas y expresiones `conflict_resolution` activas, de la asignación de exportación y de las decisiones de aprobación. Cualquier nota de débito o crédito descrita está condicionada a esa configuración; el ejemplo no garantiza su emisión automática ni el cumplimiento legal.

## Escenario:

Tanto la cantidad como el precio unitario en la factura están dentro de un rango de tolerancia aceptable en comparación con la orden de compra.

## Acción:

El sistema acepta los valores de la factura y calcula el monto total en función de la cantidad proporcionada y el precio unitario.

## Ejemplo:

**Purchase Order (PO):**

Quantity: 100 units

Unit Price: $10.00 per unit

Total Amount: $1,000.00

**Invoice Received:**

Quantity: 101 units — 1% above the PO value, within the configured ±2% tolerance.

Unit Price: $10.05 per unit — 0.5% above the PO value, within the configured ±1% tolerance.

Total Amount: $1,015.05

**Tolerance Levels:**

Quantity Tolerance: ±2%

Unit Price Tolerance: ±1%


Dado que la cantidad (101 unidades) y el precio unitario ($10.05) están dentro de los niveles de tolerancia aceptables en comparación con la orden de compra, el sistema:


1\. **Aceptar los valores de la factura:** La cantidad y el precio unitario de la factura se aceptan como válidos porque se encuentran dentro de los límites de tolerancia definidos.

2\. **Calcular el monto total:** El monto total se calcula utilizando los valores aceptados:

• Total Amount = Quantity × Unit Price

• Total Amount = 101 units × $10.05 per unit = $1,015.05

3\. **Procesar la factura:** La factura se procesa por un monto total de $1,015.05 y los registros financieros se actualizan en consecuencia.

Este enfoque garantiza que las discrepancias menores que se encuentran dentro de los niveles de tolerancia aceptables no provoquen rechazos de facturas ni retrasos en los pagos, lo que agiliza el proceso financiero.
