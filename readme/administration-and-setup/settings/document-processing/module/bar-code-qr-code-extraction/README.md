# Extracción de Códigos de Barras / QR

## **Descripción general**

Esta función permite extraer automáticamente información de **códigos de barras y códigos QR** incrustados en los documentos. Se trata de un ajuste todo o nada — activarla habilita la extracción de ambos tipos de código.

## Cómo habilitar la Extracción de Códigos de Barras / QR

Siga estos pasos para activar la función:

1. **Abra Ajustes**:
   * Desde el panel, vaya a **Ajustes**.
   * Seleccione **Procesamiento de documentos** y después **Módulo**.
2. **Habilite la función**:
   * Desplácese hasta la opción **Extracción de Códigos de Barras / QR**.
   *   Mueva el interruptor para activar la extracción.\
       \


       <figure><img src="../../../../../.gitbook/assets/image (445).png" alt=""><figcaption></figcaption></figure>

## **Tipos de código admitidos**

DocBits admite la extracción de los siguientes tipos de código:

* **QR-CODE**
* **EAN-2**, **EAN-5**, **EAN-8**, **EAN-13**
* **UPC-A**, **UPC-E**
* **ISBN-10**, **ISBN-13**
* **COMPOSITE**
* **I25**&#x20;
* **DATABAR**, **DATABAR-EXP**
* **CODABAR**
* **CODE-39**, **CODE-93**, **CODE-128**
* **PDF-417**
* **SQ-CODE**

## Estándares de Pagos mediante QR

Además de la decodificación genérica de QR, DocBits reconoce **siete estándares distintos de códigos QR de pago** y extrae automáticamente sus campos de pago a la respuesta de la API del documento. Los clientes ya no necesitan decodificar manualmente estas cadenas — cada estándar incluye su propio prefijo de campo (p. ej. `swissqr_*`, `girocode_*`) para que los valores fluyan directamente al matching, validación y exportación.

| # | Estándar | Región | Prefijo de campo | Uso típico |
|---|----------|--------|------------------|------------|
| 1 | [Swiss QR Bill](swiss-qr-code.md) | Suiza | `swissqr_*` | Toda factura suiza desde 2020 |
| 2 | [GiroCode (EPC069-12)](girocode.md) | DE, AT, NL, BE, FI | `girocode_*` | Pagos SEPA |
| 3 | [SPAYD / SPD](spayd.md) | CZ, parcialmente SK | `spayd_*` | Estándar de la Asociación Bancaria Checa |
| 4 | [PagoPA](pagopa.md) | IT (administración pública) | `pagopa_*` | Obligatorio en facturas de la PA italiana |
| 5 | [URIs de pagos cripto](crypto-uris.md) | Global (cripto) | `crypto_*` | Bitcoin, Lightning, Ethereum, Zcash, Litecoin |
| 6 | [EMVCo MPM](emvco-mpm.md) | BR, IN, SG, TH, MY, ID, PH, VN, HK y más | `emvmpm_*` | Pix, UPI, PayNow, PromptPay, QRIS, QR Ph, VietQR, FPS |
| 7 | [ZATCA Fatoora](zatca-fatoora.md) | Arabia Saudita | `zatca_*` | Obligatorio en toda factura del KSA |

**La detección es automática.** Cada cadena QR decodificada se inspecciona por su prefijo mágico (p. ej. `SPC\n0200` para Swiss QR Bill v2.0 o `PAGOPA|002|` para PagoPA) y solo los estándares reconocidos se analizan en campos estructurados.

### **Páginas relacionadas**

[Detalles de Extracción de Códigos de Barras](bar-code-extractions.md)
