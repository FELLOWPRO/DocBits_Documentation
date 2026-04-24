# ZATCA Fatoora (Arabia Saudita)

## Descripción general

**ZATCA Fatoora** es el código QR de facturación electrónica exigido por la Autoridad de Zakat, Impuestos y Aduanas de Arabia Saudita. Desde **diciembre de 2021 (Fase 1)**, toda factura B2C emitida en el Reino debe incluir un QR Fatoora con los cinco campos básicos de la factura; y desde **enero de 2023 (Fase 2)**, el QR lleva además un sobre de firma criptográfica. DocBits decodifica ambas fases y devuelve cada campo de pago de la Fase 1 como propiedad con nombre en la respuesta de la API del documento.

### Resumen de la funcionalidad

ZATCA Fatoora usa un formato **TLV binario** (1 byte de ID de tag, 1 byte de longitud, valor) envuelto en **Base64**. Todo el texto es UTF-8, así que los nombres de vendedor en árabe se decodifican correctamente. El extractor expone los tags 1–5 de la Fase 1 como campos estructurados y — cuando están presentes — los tags 6–9 de la Fase 2 como cadenas Base64 para herramientas de compliance posteriores. **La verificación de firma y hash está deliberadamente fuera del alcance**; corresponde a los stacks dedicados de compliance de facturación electrónica.

#### Beneficios principales

* **Cobertura obligatoria**: todas las facturas B2C saudíes se analizan.
* **Soporte árabe**: los nombres UTF-8 del vendedor viajan sin re-codificación.
* **Fase 1 y Fase 2**: ambas fases se detectan; la fase se expone en la salida.
* **Sobre de la Fase 2 preservado**: hash, firma, clave pública y firma de certificado se retienen como cadenas Base64 para herramientas de compliance.

***

### Detección

- TLV binario envuelto en Base64 (tags 1–9, 1 byte de ID de tag + 1 byte de longitud + valor)
- Detección de fase: `zatca_phase = 1` cuando solo están presentes los tags 1–5; `zatca_phase = 2` cuando también están los tags 6–9

### Estructura de tags TLV

| Tag | Fase | Contenido |
|-----|------|-----------|
| 1 | 1 | Nombre del vendedor (UTF-8, soporta árabe) |
| 2 | 1 | Número de registro de IVA |
| 3 | 1 | Marca de tiempo de la factura (ISO 8601) |
| 4 | 1 | Total de la factura |
| 5 | 1 | Total de IVA |
| 6 | 2 | Hash de la factura XML (Base64) |
| 7 | 2 | Firma digital (Base64) |
| 8 | 2 | Clave pública (Base64) |
| 9 | 2 | Firma del certificado (Base64) |

### Campos extraídos

Todos los campos usan el prefijo `zatca_`:

| Campo | Descripción |
|-------|-------------|
| `zatca_seller_name` | Nombre del vendedor (UTF-8) |
| `zatca_vat_number` | Número de registro de IVA |
| `zatca_invoice_timestamp` | Fecha/hora de la factura |
| `zatca_invoice_total` | Total de la factura (decimal) |
| `zatca_vat_total` | Total de IVA (decimal) |
| `zatca_phase` | `1` (Fase 1) o `2` (Fase 2) |
| `zatca_invoice_hash` | Hash de la factura XML — solo Fase 2, Base64 |
| `zatca_signature` | Firma digital — solo Fase 2, Base64 |
| `zatca_public_key` | Clave pública — solo Fase 2, Base64 |
| `zatca_certificate_signature` | Firma del certificado — solo Fase 2, Base64 |

{% hint style="info" %}
**Fuera de alcance**: DocBits no verifica la firma criptográfica, el hash ni la cadena de certificados. Esa verificación es una responsabilidad de compliance específica y debe gestionarse con un stack de facturación electrónica certificado por ZATCA.
{% endhint %}

### Ejemplo de respuesta de la API (Fase 1)

```json
{
  "zatca_seller_name": "شركة أكمي التجارية",
  "zatca_vat_number": "300123456700003",
  "zatca_invoice_timestamp": "2026-04-24T10:00:00",
  "zatca_invoice_total": 115.00,
  "zatca_vat_total": 15.00,
  "zatca_phase": 1
}
```

***

### Cómo habilitar la función

El parsing de ZATCA Fatoora está cubierto por el conmutador general de **Extracción de Códigos de Barras / QR** — no se requiere ninguna configuración específica del estándar.

1. **Abra Ajustes**:
   * Desde el panel, vaya a **Ajustes**.
   * Seleccione **Procesamiento de documentos** y después **Módulo**.
2. **Habilite la función**:
   * Desplácese hasta la opción **Extracción de Códigos de Barras / QR**.
   * Mueva el interruptor para activarla.

Para la lista completa de estándares de códigos QR de pago, consulte la [página de Descripción general](./README.md).
