# URIs de pagos cripto (BIP21 / BIP321)

## Descripción general

Las URIs de pagos cripto son el estándar informal pero ampliamente adoptado para codificar solicitudes de pago en criptomonedas dentro de códigos QR. DocBits reconoce tanto **BIP21** (la URI original de Bitcoin) como **BIP321** (la extensión modernizada de 2024) en las cinco blockchains más utilizadas: **Bitcoin**, **Lightning Network**, **Zcash**, **Ethereum** y **Litecoin**.

### Resumen de la funcionalidad

El payload QR cripto es una URI con un esquema (`bitcoin:`, `lightning:`, `zcash:`, `ethereum:`, `litecoin:`), una dirección de destinatario y un conjunto de parámetros estilo URL. DocBits extrae todos los parámetros estándar de BIP21 (`amount`, `label`, `message`) y las extensiones más recientes de BIP321 (`lightning=` como fallback, `pj=` / `pjos=` para payjoin). Según la especificación BIP21, los parámetros con prefijo `req-` pueden ser rechazados por los consumidores si no se soportan — DocBits los mantiene, por lo tanto, en un campo separado (`crypto_required_params`) para que los clientes decidan cómo manejarlos.

#### Beneficios principales

* **Soporte multi-cadena**: Bitcoin, Lightning, Zcash, Ethereum y Litecoin con un solo extractor.
* **BIP21 + BIP321**: ambas versiones se reconocen; la versión se expone en la salida.
* **Esquema case-insensitive**: `BITCOIN:` y `bitcoin:` se tratan igual.

***

### Detección

- Detección basada en esquema (insensible a mayúsculas/minúsculas): `bitcoin:`, `lightning:`, `zcash:`, `ethereum:`, `litecoin:`
- Formato URI estándar: `<scheme>:<address>?<param>=<value>&<param>=<value>`

### Parámetros soportados

**Parámetros base de BIP21:**
- `amount` — importe solicitado en la unidad nativa
- `label` — etiqueta legible del destinatario
- `message` — texto libre

**Extensiones BIP321:**
- `lightning=<BOLT11>` — factura Lightning como fallback
- `pj=<endpoint>` / `pjos=<endpoint>` — endpoints de payjoin
- `req-*` — parámetros obligatorios (preservados en `crypto_required_params`)

### Campos extraídos

Todos los campos usan el prefijo `crypto_`:

| Campo | Descripción |
|-------|-------------|
| `crypto_scheme` | `bitcoin`, `lightning`, `zcash`, `ethereum` o `litecoin` |
| `crypto_address` | Dirección del destinatario |
| `crypto_amount` | Importe solicitado (decimal) |
| `crypto_currency` | Símbolo de la divisa nativa (`BTC`, `ETH`, `LTC`, `ZEC`) |
| `crypto_label` | Etiqueta del destinatario (si está definida) |
| `crypto_message` | Texto libre (si está definido) |
| `crypto_lightning_fallback` | Factura BOLT11 Lightning (desde `lightning=` de BIP321) |
| `crypto_payjoin_endpoint` | Endpoint de payjoin (desde `pj=` / `pjos=`) |
| `crypto_required_params` | Parámetros `req-*`, preservados para que el cliente decida |
| `crypto_uri_version` | `bip21` o `bip321` |

### Ejemplo de respuesta de la API

```json
{
  "crypto_scheme": "bitcoin",
  "crypto_address": "bc1q9h6mksxrsfnd4ymr8mu2w2v3v0sylgkfghxwzm",
  "crypto_amount": 0.00254,
  "crypto_currency": "BTC",
  "crypto_label": "Acme Invoice 2026-042",
  "crypto_message": "Payment for invoice 2026-042",
  "crypto_uri_version": "bip21"
}
```

***

### Cómo habilitar la función

El parsing de URIs cripto está cubierto por el conmutador general de **Extracción de Códigos de Barras / QR** — no se requiere ninguna configuración específica del estándar.

1. **Abra Ajustes**:
   * Desde el panel, vaya a **Ajustes**.
   * Seleccione **Procesamiento de documentos** y después **Módulo**.
2. **Habilite la función**:
   * Desplácese hasta la opción **Extracción de Códigos de Barras / QR**.
   * Mueva el interruptor para activarla.

Para la lista completa de estándares de códigos QR de pago, consulte la [página de Descripción general](./README.md).
