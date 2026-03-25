# Scripts de Ejemplo

Ejemplos de scripts listos para produccion para casos de uso comunes de automatizacion en DocBits. Cada ejemplo incluye el script completo, una explicacion paso a paso y enlaces a las funciones utilizadas.

## Ejemplos por Caso de Uso

### Validacion de Datos
- [Validacion de Proveedor por Lookup](lookup-supplier-validation.md) — Validar proveedor contra datos maestros
- [Validacion de Suma de Tabla](table-sum-validation.md) — Verificar que los totales de partidas coincidan con el monto neto

### Automatizacion
- [Coincidencia Automatica de OC](auto-po-matching.md) — Activar coincidencia automatica de ordenes de compra
- [Auto-Exportacion por Condiciones](status-auto-export.md) — Omitir validacion para facturas de bajo riesgo
- [Calculo de Fecha de Vencimiento](due-date-calculation.md) — Calcular terminos de pago con omision de fines de semana

### Reglas de Negocio
- [Deteccion de Codigo Fiscal](tax-code-detection.md) — Determinar codigo fiscal a partir de texto completo y montos
- [Tarea por Monto Elevado](task-high-amount.md) — Crear tarea de aprobacion para facturas grandes
- [Campos Obligatorios Dinamicos](dynamic-required-fields.md) — Ajustar campos obligatorios segun la moneda

### Ejemplos Heredados
- [Calculo de Cargos Totales](calculating-total-charges-script-for-docbits-1.md) — Sumar montos de flete y embalaje
- [Eliminar Lineas Vacias](delete-lines-with-empty-quantity-and-amount.md) — Eliminar filas con cantidad/monto cero
- [Numeros de Certificado de Exportacion](formatting-export-certificate-reference-numbers-script-for-docbits.md) — Rellenar numeros de referencia con ceros a la izquierda
- [Numeros de Factura Extendidos](generating-extended-invoice-numbers-script-for-docbits-1.md) — Concatenar ID de factura y numero de OC
- [USD como Moneda Predeterminada](usd-as-default-currency.md) — Establecer USD como moneda predeterminada
