# PagoPA

## Descripción general

**PagoPA** es el estándar de QR de pago de la administración pública italiana. Cada factura emitida por un organismo de la PA italiana (municipios, universidades, sanidad, autoridades tributarias) lleva un código QR PagoPA. DocBits decodifica el payload y devuelve los cuatro campos de pago obligatorios en la respuesta de la API del documento.

### Resumen de la funcionalidad

Los payloads PagoPA son compactos y estrictamente estructurados: exactamente **cinco campos separados por pipe** en una sola línea. Los importes están codificados en **céntimos** (entero) y el extractor los convierte automáticamente en euros decimales. Los ceros iniciales del `codice_avviso` (aviso de pago de 18 dígitos) se preservan — no debe analizarse nunca como entero, puesto que se trata de un identificador de ancho fijo.

#### Beneficios principales

* **Cobertura obligatoria** para facturas de la PA italiana: `codice_avviso` y código fiscal del acreedor extraídos a campos con nombre.
* **Tratamiento numérico seguro**: el `codice_avviso` de 18 dígitos conserva los ceros iniciales; el importe en céntimos también se expone como euro decimal.

***

### Detección

- Prefijo mágico: `PAGOPA|002|`
- Exactamente **5 campos separados por pipe** tras el prefijo: `PAGOPA|002|<codice_avviso>|<fiscal_code_creditor>|<amount_cents>|<auth>`
- **Solo EUR** — ninguna otra divisa es válida según la especificación

### Campos extraídos

Todos los campos usan el prefijo `pagopa_`:

| Campo | Descripción |
|-------|-------------|
| `pagopa_codice_avviso` | Aviso de pago de 18 dígitos — ceros iniciales preservados (cadena) |
| `pagopa_fiscal_code_creditor` | Código fiscal del acreedor, 11 dígitos (cadena) |
| `pagopa_amount_cents` | Importe en céntimos (entero) |
| `pagopa_amount` | Importe en euros (decimal, derivado de `pagopa_amount_cents`) |
| `pagopa_auth` | Indicador opcional de auth/versión del payload |

### Ejemplo de respuesta de la API

```json
{
  "pagopa_codice_avviso": "301234567890123456",
  "pagopa_fiscal_code_creditor": "80012345678",
  "pagopa_amount_cents": 12050,
  "pagopa_amount": 120.50
}
```

***

### Cómo habilitar la función

El parsing de PagoPA está cubierto por el conmutador general de **Extracción de Códigos de Barras / QR** — no se requiere ninguna configuración específica del estándar.

1. **Abra Ajustes**:
   * Desde el panel, vaya a **Ajustes**.
   * Seleccione **Procesamiento de documentos** y después **Módulo**.
2. **Habilite la función**:
   * Desplácese hasta la opción **Extracción de Códigos de Barras / QR**.
   * Mueva el interruptor para activarla.

Para la lista completa de estándares de códigos QR de pago, consulte la [página de Descripción general](./README.md).
