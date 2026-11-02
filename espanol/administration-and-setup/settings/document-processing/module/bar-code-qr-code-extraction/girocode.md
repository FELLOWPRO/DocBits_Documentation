# GiroCode (EPC069-12)

## Descripción general

**GiroCode** es el código QR de pago SEPA definido por el European Payments Council en la especificación **EPC069-12**. Es el estándar de facto en las facturas de bancos alemanes y austríacos (Sparkasse, VR-Banken, Deutsche Bank, Commerzbank, PSA Austria) y también se utiliza en Países Bajos, Bélgica y Finlandia. DocBits decodifica ambas revisiones (**v001** y **v002**) y entrega el payload completo de pago SEPA en la respuesta de la API del documento.

### Resumen de la funcionalidad

Un GiroCode contiene todo lo necesario para iniciar una transferencia SEPA: BIC e IBAN del beneficiario, nombre, importe, propósito y una referencia de acreedor estructurada o un texto libre de concepto. DocBits normaliza el payload de modo que **los importes con `.` o `,` como separador decimal** — una desviación frecuente de la especificación por parte de generadores alemanes — se aceptan sin errores.

#### Beneficios principales

* **Amplia cobertura en DE / AT**: todos los grandes bancos minoristas imprimen GiroCodes en las facturas.
* **Ambas revisiones soportadas**: v001 (BIC obligatorio) y v002 (BIC opcional en el EEE).
* **Tolerante a separadores decimales**: acepta `227.01` y `227,01` indistintamente.

***

### Detección

- Prefijo mágico: `BCD\n001` (v001) o `BCD\n002` (v002)
- Payload estructurado por líneas según la especificación EPC069-12
- **v002** hace opcional el BIC cuando el IBAN pertenece al Espacio Único de Pagos en Euros

### Campos extraídos

Todos los campos usan el prefijo `girocode_`:

| Campo | Descripción |
|-------|-------------|
| `girocode_bic` | BIC del beneficiario (obligatorio en v001, opcional en v002 para el EEE) |
| `girocode_creditor_name` | Nombre del beneficiario |
| `girocode_iban` | IBAN del beneficiario |
| `girocode_amount` | Importe (decimal) — `.` y `,` aceptados |
| `girocode_currency` | Divisa (habitualmente `EUR`) |
| `girocode_purpose` | Código SEPA de propósito |
| `girocode_structured_reference` | Referencia estructurada del acreedor (ISO 11649 RF) |
| `girocode_unstructured_remittance` | Concepto libre |
| `girocode_version` | `001` o `002` |

### Ejemplo de respuesta de la API

Ejemplo real (factura de Dr. Meindl u. Partner):

```json
{
  "girocode_bic": "DAAEDEDDXXX",
  "girocode_creditor_name": "Dr. Meindl u. Partner",
  "girocode_iban": "DE69300606010006343686",
  "girocode_amount": 227.01,
  "girocode_currency": "EUR",
  "girocode_unstructured_remittance": "38710498001705 - QR",
  "girocode_version": "002"
}
```

***

### Cómo habilitar la función

El parsing de GiroCode está cubierto por el conmutador general de **Extracción de Códigos de Barras / QR** — no se requiere ninguna configuración específica del estándar.

1. **Abra Ajustes**:
   * Desde el panel, vaya a **Ajustes**.
   * Seleccione **Procesamiento de documentos** y después **Módulo**.
2. **Habilite la función**:
   * Desplácese hasta la opción **Extracción de Códigos de Barras / QR**.
   * Mueva el interruptor para activarla.

Para la lista completa de estándares de códigos QR de pago, consulte la [página de Descripción general](./README.md).
