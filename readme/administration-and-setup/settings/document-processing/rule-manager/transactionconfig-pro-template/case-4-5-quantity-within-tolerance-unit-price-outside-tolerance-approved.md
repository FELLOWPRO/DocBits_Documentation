# Caso 4, 5: Cantidad dentro de la tolerancia, Precio unitario fuera de la tolerancia (Aprobado)

El siguiente escenario es un ejemplo de asignación configurada, no una plantilla predeterminada cuyo despliegue se haya verificado. La salida real, los importes, los signos y los tipos de documento dependen de las reglas y expresiones `conflict_resolution` activas, de la asignación de exportación y de las decisiones de aprobación. Cualquier nota de débito o crédito descrita está condicionada a esa configuración; el ejemplo no garantiza su emisión automática ni el cumplimiento legal.

## Escenario:

La cantidad en la factura está dentro de la tolerancia, pero el precio unitario está fuera del rango de tolerancia aceptable. Sin embargo, esta variación en el precio unitario ha sido revisada y aprobada por las autoridades correspondientes.

## Acción:

El sistema ajusta el precio unitario para que coincida con la orden de compra y aplica los cargos de línea necesarios para contabilizar la diferencia.

## Ejemplo:

**Purchase Order (PO):**

Quantity: <mark style="color:green;">100</mark> units

Precio unitario: $10.00 por unidad

Total Amount: <mark style="color:purple;">$1,000.00</mark>

**Invoice Received:**

Cantidad: <mark style="color:green;">100</mark> unidades (dentro de la tolerancia)

Precio unitario: <mark style="color:red;">$11.00</mark> por unidad (fuera de la tolerancia de ±5%)

Total Amount: <mark style="color:red;">$1,100.00</mark>

**Tolerance Levels:**

Quantity Tolerance: ±2%

Tolerancia del precio unitario: ±5 % (rango esperado: $9.50 a $10.50)

**Approval:**

• El precio unitario de $11.00 está fuera del rango de tolerancia pero ha sido aprobado manualmente por el departamento correspondiente.

Dado que la cantidad está dentro de la tolerancia pero el precio unitario está fuera de la tolerancia (aún aprobado), el sistema:

1\. **Ajustar el precio unitario**: el sistema vuelve a ajustar el precio unitario al precio unitario de PO porque se aprobó la variación:

• **Precio unitario ajustado = $10.00 por unidad**

• **Monto total ajustado = 100 unidades × $10.00 por unidad = $1,000.00**

2\. **Aplicar un cargo de línea por la diferencia**: Dado que el precio unitario aprobado de $11.00 es mayor que el precio unitario de la orden de compra de $10.00, el sistema aplica un cargo de línea para contabilizar esta diferencia:

• **Monto del cargo de línea = (Precio unitario de la factura aprobada - precio unitario de la orden de compra) × Cantidad**

• **Monto del cargo de línea = ($11.00 - $10.00) × 100 unidades = $100.00**

3\. **Procesar la Factura**: El sistema procesa la factura con:

• **Base Amount:** $1,000.00

• **Line Charge:** $100.00

• **Monto total procesado:** $1,100.00

Esto garantiza que, si bien los valores de la orden de compra se mantienen para mantener la coherencia, la variación aprobada en el precio unitario se contabiliza mediante un cargo de línea adicional, lo que da como resultado un procesamiento financiero y un mantenimiento de registros precisos.
