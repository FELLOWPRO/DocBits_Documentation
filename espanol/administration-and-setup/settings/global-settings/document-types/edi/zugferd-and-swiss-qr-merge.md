# Mapeo de campos ZUGFeRD + Swiss QR Code

## Visión general

Al procesar facturas en PDF que contienen tanto datos XML ZUGFeRD como un Swiss QR Code, DocBits extrae datos de ambas fuentes y los fusiona de manera inteligente.

## Cómo funciona

1. **Extracción ZUGFeRD XML** - DocBits primero extrae campos del ZUGFeRD XML incrustado
2. **Detección de Swiss QR Code** - El barcode detecta y analiza los códigos Swiss QR
3. **Fusión Inteligente (Smart Merge)** - Los campos vacíos se llenan con datos de Swiss QR (los campos con valores se conservan)
4. **Audit Trail** - Los datos completos del código QR se almacenan en `qr_code_data` para verificación

## Tabla de Mapeo de Campos

### Mapeo de Campos Swiss QR Code → DocBits

| Campo Swiss QR | Campo DocBits | Descripción |
| :--- | :--- | :--- |
| IBAN | `supplier_iban` | IBAN del acreedor (p. ej., CH9300762011...) |
| Amount | `total_amount` | Importe del pago (p. ej., 1234.56) |
| Currency | `currency` | Código de moneda (CHF o EUR) |
| Reference | `payment_reference` / `esr_reference` | Referencia QR o número ESR |
| Creditor.Name | `supplier_name` | Nombre de la empresa proveedora |
| Creditor.AddressLine1 | `supplier_address` | Dirección (calle) |
| Creditor.PostalCode | `supplier_plz` | Código postal |
| Creditor.City | `supplier_city` | Ciudad |
| Creditor.Country | `supplier_country` | Código de país (CH) |
| Debtor.Name | `company_name` | Nombre de la empresa receptora |
| Debtor.AddressLine1 | `company_street` | Dirección del receptor |
| Debtor.PostalCode | `company_plz` | Código postal del receptor |
| Debtor.City | `company_city` | Ciudad del receptor |

## Ejemplo: Procesamiento de Factura de Muestra

### Documento de Entrada

*   **PDF**: Factura con ZUGFeRD 1.0 XML incrustado + código de barras Swiss QR Code

### Datos Extraídos del Swiss QR Code

```json
{
  "supplier_iban": "CH9300762011623852957",
  "amount_to_pay": 1234.56,
  "currency": "CHF",
  "esr_reference": "210000000003139471430009017",
  "supplier_name": "Sample Company GmbH",
  "supplier": {
    "name": "Sample Company GmbH",
    "address_line_1": "Musterstrasse",
    "address_line_2": "123",
    "postal_code": "8000",
    "city": "Zürich",
    "country": "CH"
  },
  "recipient": {
    "name": "Demo Customer AG",
    "address_line_1": "Beispielweg 45",
    "postal_code": "3000",
    "city": "Bern",
    "country": "CH"
  }
}
```

### Resultados de Extracción de Campos

| Campo | Valor | Fuente | Método |
| :--- | :--- | :--- | :--- |
| `supplier_iban` | CH9300762011623852957 | ZUGFeRD XML | ED |
| `total_amount` | 1234.56 | ZUGFeRD XML | ED |
| `currency` | CHF | ZUGFeRD XML | ED |
| `supplier_name` | Sample Company GmbH | ZUGFeRD XML | ED |
| `supplier_address` | Musterstrasse 123 | ZUGFeRD XML | ED |
| `payment_reference` | 210000000003139471430009017 | Swiss QR | SWISS_QR |
| `supplier_plz` | 8000 | Swiss QR | SWISS_QR |
| `supplier_city` | Zürich | Swiss QR | SWISS_QR |

## Métodos de Extracción

| Código de Método | Descripción |
| :--- | :--- |
| **ED** | Documento Electrónico (ZUGFeRD/XRechnung/PEPPOL XML) |
| **SWISS_QR** | Extracción de código de barras Swiss QR Code |
| **OCR** | Reconocimiento Óptico de Caracteres |
| **ML** | Extracción por Machine Learning |

## Prioridad de Fusión (Merge)

1.  **ZUGFeRD XML** tiene la mayor prioridad (datos estructurados y fiables)
2.  **Swiss QR Code** rellena campos vacíos (garantizado preciso para datos de pago)
3.  **OCR/ML** usado para campos no presentes en fuentes electrónicas

## Versiones de Swiss QR Code Soportadas

*   Formato Swiss QR Bill (ISO 20022)
*   Formato QR-IBAN (comienza con 30, 31)
*   Formato IBAN Estándar
*   Con/sin referencia estructurada (QRR, SCOR)

## Requisito de Versión

Esta función requiere **api versión 10.95.6** y **barcode versión 1.0.5** o superior.

### Versiones de Componentes (Entorno Dev)

| Componente | Versión | Descripción |
| :--- | :--- | :--- |
| `api` | 10.95.6 | API central con soporte de extracción ZUGFeRD 1.0 |
| `barcode` | 1.0.5 | Detección y análisis de Swiss QR Code |
| `Auth` | 1.48.8 | Servicio de autenticación |

