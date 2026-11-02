# EMVCo MPM (QR presentado por el comercio)

## Descripción general

**EMVCo MPM** (Merchant-Presented Mode) es la especificación global de códigos QR mantenida por EMVCo — el mismo organismo detrás de los estándares de tarjetas con chip y pagos sin contacto. Un único envoltorio TLV (Tag-Length-Value) se comparte entre más de una docena de sistemas nacionales de pagos instantáneos, de forma que un solo parser habilita **Pix** (Brasil), **UPI** (India), **PayNow** (Singapur), **PromptPay** (Tailandia), **QRIS** (Indonesia), **QR Ph** (Filipinas), **VietQR** (Vietnam), **FPS** (Hong Kong), **DuitNow** (Malasia), **NETS** (Singapur) y muchos más.

### Resumen de la funcionalidad

Todo payload EMVCo MPM comparte el mismo envoltorio: comienza con `000201` (Payload Format Indicator = 01) y termina con `6304<CRC>`, donde `<CRC>` es una suma CRC16-CCITT-FALSE en 4 hex. Dentro, los tags codificados en TLV 26–51 transportan plantillas de **Merchant Account Info** identificadas por un **subtag GUI** — ese tag GUI es la clave con la que DocBits detecta a qué esquema nacional pertenece el QR. El CRC se valida y el resultado se expone como booleano, de modo que los comercios puedan detectar códigos manipulados.

#### Beneficios principales

* **Un extractor, muchos esquemas**: un único parser genérico TLV gestiona toda la familia EMVCo MPM.
* **Esquemas nacionales identificados**: la salida incluye un esquema nombrado (p. ej. `pix`, `upi`, `paynow`) para que la lógica posterior ramifique con claridad.
* **Validez de CRC expuesta**: `emvmpm_crc16_valid` revela los QR manipulados o corruptos.
* **Normalización de divisa**: los códigos numéricos ISO 4217 se mapean automáticamente a alpha-3 (20+ divisas; los códigos no mapeados pasan tal cual).

***

### Detección

- Forma mágica: comienza con `000201` y termina con `6304<4-hex CRC16-CCITT-FALSE>`
- Un decodificador TLV genérico recorre cada tag
- Los esquemas nacionales se identifican por el **subtag GUI** dentro de las plantillas de Merchant Account Info (tags 26–51)

### Esquemas nacionales reconocidos

| Subtag GUI | Esquema | País |
|------------|---------|------|
| `br.gov.bcb.pix` | **Pix** | Brasil |
| `UPI` | **UPI** | India |
| `SG.PAYNOW` | **PayNow / SGQR** | Singapur |
| `SG.COM.NETS` | **NETS** | Singapur |
| `HK.COM.HKICL.FPS` | **FPS** | Hong Kong |
| `ID.CO.QRIS.WWW` | **QRIS** | Indonesia |
| `COM.BDO.QRPH` / `COM.BPI.QRPH` / `PH.PPMI.P2MEMV` | **QR Ph** | Filipinas |
| `COM.QRCODE.TELLUSBANGKOK` + AID `A000000677010111` | **PromptPay** | Tailandia |
| `A000000727` | **VietQR** | Vietnam |

Los valores GUI/AID no reconocidos siguen analizándose — el extractor recurre al conjunto de campos genéricos EMVCo MPM.

### Campos extraídos

Todos los campos usan el prefijo `emvmpm_`:

| Campo | Descripción |
|-------|-------------|
| `emvmpm_scheme` | Esquema nacional detectado (p. ej. `pix`, `upi`, `paynow`, `qris`, `promptpay`, `vietqr`, `fps`, `qrph`, `nets`) o `generic` |
| `emvmpm_merchant_name` | Nombre del comercio (tag 59) |
| `emvmpm_merchant_city` | Ciudad del comercio (tag 60) |
| `emvmpm_country_code` | Código de país ISO 3166 alpha-2 (tag 58) |
| `emvmpm_amount` | Importe de la transacción (decimal, tag 54) |
| `emvmpm_currency` | Divisa alpha-3 (convertida del código numérico del tag 53) |
| `emvmpm_additional_data` | Objeto anidado: número de factura, etiqueta de referencia, etiqueta de terminal, propósito de la transacción (subtags del tag 62) |
| `emvmpm_crc16_valid` | Booleano — `true` si la suma CRC16 coincide |

### Ejemplo de respuesta de la API (Pix)

```json
{
  "emvmpm_scheme": "pix",
  "emvmpm_merchant_name": "ACME COMERCIO LTDA",
  "emvmpm_merchant_city": "SAO PAULO",
  "emvmpm_country_code": "BR",
  "emvmpm_amount": 125.00,
  "emvmpm_currency": "BRL",
  "emvmpm_additional_data": {
    "reference_label": "PEDIDO-2026-0427"
  },
  "emvmpm_crc16_valid": true
}
```

***

### Cómo habilitar la función

El parsing de EMVCo MPM está cubierto por el conmutador general de **Extracción de Códigos de Barras / QR** — no se requiere ninguna configuración específica del estándar.

1. **Abra Ajustes**:
   * Desde el panel, vaya a **Ajustes**.
   * Seleccione **Procesamiento de documentos** y después **Módulo**.
2. **Habilite la función**:
   * Desplácese hasta la opción **Extracción de Códigos de Barras / QR**.
   * Mueva el interruptor para activarla.

Para la lista completa de estándares de códigos QR de pago, consulte la [página de Descripción general](./README.md).
