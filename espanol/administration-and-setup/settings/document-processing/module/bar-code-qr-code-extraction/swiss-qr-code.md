# Swiss QR Bill

## Descripción general

La **Swiss QR Bill** es el estándar nacional de comprobantes de pago que, desde el 30 de junio de 2020, ha reemplazado a las tradicionales boletas naranjas y rojas suizas. Toda factura nacional suiza — de proveedores de servicios públicos, aseguradoras o socios comerciales — lleva hoy un código Swiss QR Bill. DocBits lo decodifica automáticamente y expone cada campo de pago en la respuesta de la API.

### Resumen de la funcionalidad

Las Swiss QR Bills siguen el estándar de pagos **ISO 20022** y se emiten en dos versiones: **v1.0** (despliegue inicial) y **v2.0** (actual). El extractor de DocBits soporta ambas. Los payloads reconocidos se decodifican en un conjunto completo de campos — acreedor, deudor, IBAN / QR-IBAN, importe, divisa, tipo de referencia (QRR, SCOR o NON), mensajes estructurados y libres, y esquemas de pago alternativos.

<figure><img src="../../../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Beneficios principales

* **Cero entrada manual** para facturas suizas: IBAN, importe, referencia y acreedor fluyen directamente al documento.
* **Ambas versiones cubiertas**: v1.0 y v2.0 se detectan automáticamente.
* **Tipos de referencia preservados**: QRR, SCOR y NON se conservan exactamente como aparecen impresos, lo que mantiene el proceso de conciliación funcionando.

***

### Detección

- Prefijo mágico: `SPC\n0100` (v1.0) o `SPC\n0200` (v2.0)
- Compatible con ISO 20022
- El parser también expone `alt-schemes` (esquemas de pago alternativos) cuando están presentes

### Campos extraídos

Todos los campos usan el prefijo `swissqr_`:

| Campo | Descripción |
|-------|-------------|
| `swissqr_account` | IBAN o QR-IBAN del acreedor |
| `swissqr_creditor_name` | Nombre del acreedor |
| `swissqr_creditor_street` | Calle / línea de dirección del acreedor |
| `swissqr_creditor_city` | Ciudad del acreedor |
| `swissqr_creditor_postal_code` | Código postal del acreedor |
| `swissqr_creditor_country` | País del acreedor (ISO 3166 alpha-2) |
| `swissqr_debtor_name` | Nombre del deudor (si está impreso) |
| `swissqr_debtor_street`, `swissqr_debtor_city`, `swissqr_debtor_postal_code`, `swissqr_debtor_country` | Dirección del deudor |
| `swissqr_amount` | Importe (decimal) |
| `swissqr_currency` | Divisa (ISO 4217) — normalmente `CHF` o `EUR` |
| `swissqr_reference` | Referencia estructurada (QRR o SCOR) |
| `swissqr_reference_type` | `QRR`, `SCOR` o `NON` |
| `swissqr_unstructured_message` | Texto libre de concepto |
| `swissqr_bill_information` | Información estructurada de facturación (S1 / Swico) |
| `swissqr_alt_schemes` | Procedimientos alternativos (si están presentes) |

### Ejemplo de respuesta de la API

```json
{
  "swissqr_account": "CH4431999123000889012",
  "swissqr_creditor_name": "Robert Schneider AG",
  "swissqr_creditor_street": "Rue du Lac 1268",
  "swissqr_creditor_city": "Biel",
  "swissqr_creditor_postal_code": "2501",
  "swissqr_creditor_country": "CH",
  "swissqr_amount": 1949.75,
  "swissqr_currency": "CHF",
  "swissqr_reference": "210000000003139471430009017",
  "swissqr_reference_type": "QRR",
  "swissqr_unstructured_message": "Bill No. 3139 for services 2026"
}
```

***

### Cómo habilitar la función

El parsing de Swiss QR Bill está cubierto por el conmutador general de **Extracción de Códigos de Barras / QR** — no se requiere ninguna configuración específica del estándar.

1. **Abra Ajustes**:
   * Desde el panel, vaya a **Ajustes**.
   * Seleccione **Procesamiento de documentos** y después **Módulo**.
2. **Habilite la función**:
   * Desplácese hasta la opción **Extracción de Códigos de Barras / QR**.
   * Mueva el interruptor para activarla.

<figure><img src="../../../../../.gitbook/assets/image (444).png" alt=""><figcaption></figcaption></figure>

Para la lista completa de estándares de códigos QR de pago, consulte la [página de Descripción general](./README.md).
