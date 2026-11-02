# SPAYD / Short Payment Descriptor (Checo)

## Descripción general

**SPAYD** (Short Payment Descriptor), también conocido como **SPD**, es el estándar de código QR de pago definido por la Asociación Bancaria Checa. Se imprime prácticamente en todas las facturas empresariales checas y se utiliza parcialmente en Eslovaquia. DocBits decodifica los payloads SPAYD y devuelve la instrucción de pago completa — incluyendo los símbolos específicos checos (variable, specific, constant) — en la respuesta de la API del documento.

### Resumen de la funcionalidad

Un payload SPAYD es una lista de pares clave:valor separados por asteriscos. Los valores están codificados en porcentaje, de modo que los nombres de destinatario y los mensajes en UTF-8 se preservan. DocBits soporta la variante habitual `ACC` (IBAN más BIC opcional, separados por `+`), `ALT-ACC` (IBANs alternativos, separados por comas) y preserva cualquier clave desconocida específica del proveedor en un campo dedicado (`spayd_raw_pairs`), garantizando que los consumidores posteriores no pierdan datos.

#### Beneficios principales

* **Cobertura completa de pagos checos**: IBAN/BIC más los símbolos VS/SS/KS se extraen a campos con nombre.
* **Seguro con Unicode**: los nombres y mensajes UTF-8 codificados en porcentaje viajan íntegros.
* **Compatible hacia adelante**: las claves desconocidas se preservan en `spayd_raw_pairs`.

***

### Detección

- Prefijo mágico: `SPD*1.0*`
- El payload es una lista separada por `*` de pares `KEY:value`, p. ej. `SPD*1.0*ACC:CZ5508000000001234567899*AM:480.55*CC:CZK`
- Los valores están **codificados en porcentaje** (RFC 3986)
- `ACC` puede contener `IBAN+BIC` (separados por `+`); `ALT-ACC` contiene IBANs alternativos separados por comas

### Campos extraídos

Todos los campos usan el prefijo `spayd_`:

| Campo | Descripción |
|-------|-------------|
| `spayd_iban` | IBAN principal (de `ACC`) |
| `spayd_bic` | BIC (de `ACC`, si está presente) |
| `spayd_alt_ibans` | Lista de IBANs alternativos (de `ALT-ACC`) |
| `spayd_amount` | Importe (decimal, de `AM`) |
| `spayd_currency` | Divisa (de `CC`, normalmente `CZK`) |
| `spayd_variable_symbol` | Símbolo variable (`VS`) — número de factura/referencia |
| `spayd_specific_symbol` | Símbolo específico (`SS`) |
| `spayd_constant_symbol` | Símbolo constante (`KS`) |
| `spayd_recipient_name` | Nombre del destinatario (de `RN`) |
| `spayd_due_date` | Fecha de vencimiento (de `DT`, `YYYYMMDD`) |
| `spayd_message` | Mensaje libre (de `MSG`) |
| `spayd_raw_pairs` | Pares `KEY:value` desconocidos o específicos del proveedor, preservados sin cambios |

### Ejemplo de respuesta de la API

```json
{
  "spayd_iban": "CZ5508000000001234567899",
  "spayd_amount": 480.55,
  "spayd_currency": "CZK",
  "spayd_variable_symbol": "2026041720",
  "spayd_constant_symbol": "0308",
  "spayd_recipient_name": "Moje firma, s.r.o.",
  "spayd_due_date": "20260507",
  "spayd_message": "Platba za fakturu 2026041720"
}
```

***

### Cómo habilitar la función

El parsing de SPAYD está cubierto por el conmutador general de **Extracción de Códigos de Barras / QR** — no se requiere ninguna configuración específica del estándar.

1. **Abra Ajustes**:
   * Desde el panel, vaya a **Ajustes**.
   * Seleccione **Procesamiento de documentos** y después **Módulo**.
2. **Habilite la función**:
   * Desplácese hasta la opción **Extracción de Códigos de Barras / QR**.
   * Mueva el interruptor para activarla.

Para la lista completa de estándares de códigos QR de pago, consulte la [página de Descripción general](./README.md).
