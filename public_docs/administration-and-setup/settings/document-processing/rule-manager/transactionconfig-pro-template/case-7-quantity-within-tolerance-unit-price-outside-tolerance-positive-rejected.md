# Caso 7: cantidad dentro de la tolerancia, precio unitario fuera de la tolerancia (rechazo positivo)

El siguiente escenario es un ejemplo ilustrativo de una asignación configurada, no una plantilla predeterminada desplegada y verificada. La salida real, los importes, los signos y los tipos de documento dependen de las reglas y expresiones `conflict_resolution` activas, de la asignación de exportación y de las decisiones de aprobación. Cualquier nota de débito o de crédito descrita a continuación está condicionada por esa configuración; el ejemplo no garantiza su emisión automática ni el cumplimiento legal.

## Escenario:

La cantidad está dentro de la tolerancia, pero el precio unitario supera el rango aceptable (tolerancia positiva) y no está aprobado.

## Acción:

El sistema rechaza el precio unitario de la factura, lo ajusta para que coincida con la orden de compra y puede generar una nota de débito para contabilizar el importe cobrado en exceso.

## Ejemplo:

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Unit Price: $15.00 per unit
  * Total Amount: $3,000.00
* **Invoice Received:**
  * Quantity: 198 units — 1% below the PO value, within the configured ±2% tolerance.
  * Unit Price: $17.00 per unit — 13.33% above the PO value, outside the configured ±1% tolerance; rejected.
  * Total Amount: $3,366.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±2%
  * Unit Price Tolerance: ±1%

Dado que la cantidad (198 unidades) está dentro del rango de tolerancia aceptable pero el precio unitario ($17.00) supera la tolerancia aceptable y no está aprobado, el sistema:

1. **Rechazar el precio unitario de la factura:** el sistema no acepta el precio unitario facturado de $17.00.
2. **Ajustar el precio unitario:** el sistema ajusta el precio unitario para que coincida con el precio unitario de la orden de compra original.
   * Adjusted Unit Price = $15.00 (de la PO)
3. **Calcular el importe total corregido:** con el precio unitario ajustado, el sistema recalcula el importe total.
   * **Corrected Total Amount = Quantity × Adjusted Unit Price**
   * **Corrected Total Amount = 198 units × $15.00 per unit = $2,970.00**
4. **Generar una nota de débito:** el sistema genera una nota de débito para contabilizar la diferencia debida al cobro excesivo.
   * **Debit Note Amount = Original Invoice Total - Corrected Total Amount**
   * **Debit Note Amount = $3,366.00 - $2,970.00 = $396.00**
   * Esta nota de débito representa el importe cobrado en exceso por el proveedor.
5. **Procesar la factura:** el sistema procesa la factura con el importe total corregido de $2,970.00 y emite una nota de débito por $396.00 para compensar el cobro excesivo.

Este enfoque garantiza que se corrija cualquier cobro excesivo, alinea la transacción con las condiciones de la orden de compra y protege los intereses financieros de la empresa.
