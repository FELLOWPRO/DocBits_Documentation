# Scripts de Ejemplo

Scripts de ejemplo listos para producción para casos de uso comunes de automatización en DocBits. Cada ejemplo incluye el script completo, una explicación paso a paso y enlaces a las funciones utilizadas.

## Ejemplos por Caso de Uso

### Validación de Datos
- [Validación de Proveedor por Lookup](lookup-supplier-validation.md) — Validar proveedor contra datos maestros
- [Validación de Suma de Tabla](table-sum-validation.md) — Verificar que los totales de línea coincidan con el importe neto

### Automatización
- [Coincidencia Automática de OC](auto-po-matching.md) — Activar coincidencia automática de OC
- [Auto-Exportación por Condiciones](status-auto-export.md) — Saltar validación para facturas de bajo riesgo
- [Cálculo de Fecha de Vencimiento](due-date-calculation.md) — Calcular condiciones de pago con salto de fines de semana

### Reglas de Negocio
- [Detección de Código Fiscal](tax-code-detection.md) — Determinar código fiscal a partir del texto completo y montos
- [Tarea para Monto Elevado](task-high-amount.md) — Crear tarea de aprobación para facturas grandes
- [Campos Obligatorios Dinámicos](dynamic-required-fields.md) — Ajustar campos obligatorios según la moneda

### Fulltext & Vector Search
- [Detección de Facturas Duplicadas](duplicate-invoice-detection.md) — Encontrar duplicados de facturas mediante búsqueda fulltext
- [Detección de Documentos Similares](similar-document-detection.md) — Marcar documentos similares mediante búsqueda vectorial
- [Búsqueda de Texto de Cumplimiento](compliance-text-search.md) — Buscar palabras clave de cumplimiento (ej. Reverse Charge)
- [Validación de Proveedor ERP](erp-vendor-validation.md) — Validar proveedor contra datos maestros ERP
- [Completar Campos desde el Historial](fill-missing-fields-from-history.md) — Completar campos automáticamente desde documentos anteriores

### Ejemplos Legacy
- [Cálculo de Cargos Totales](calculating-total-charges-script-for-docbits-1.md) — Sumar montos de flete y embalaje
- [Eliminar Líneas Vacías](delete-lines-with-empty-quantity-and-amount.md) — Eliminar filas con cantidad/monto cero
- [Números de Certificado de Exportación](formatting-export-certificate-reference-numbers-script-for-docbits.md) — Rellenar números de referencia con ceros a la izquierda
- [Números de Factura Extendidos](generating-extended-invoice-numbers-script-for-docbits-1.md) — Concatenar ID de factura y número de OC
- [USD como Moneda Predeterminada](usd-as-default-currency.md) — Establecer USD como moneda predeterminada
