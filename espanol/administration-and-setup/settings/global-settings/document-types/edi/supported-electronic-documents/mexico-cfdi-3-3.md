---
description: Compatibilidad de DocBits con el documento electrónico MEXICO CFDI 3.3
---

# 🇲🇽 MEXICO CFDI 3.3

<!-- edocs-country-scope -->

{% hint style="info" %}
Consulte la guía del país para conocer los límites de versión, la configuración que se está utilizando y el vídeo explicativo del país. [México](countries/mexico.md). Compruebe el espacio de nombres, la versión y TipoDeComprobante. Un importe negativo por sí solo no identifica una nota de crédito. Analizar el archivo no certifica la autorización del SAT.
{% endhint %}

| Propiedad              | Valor                                              |
| ---------------------- | -------------------------------------------------- |
| **País / Región**      | México                                             |
| **Tipos de documento** | Factura, Nota de crédito, Recibo de pago           |
| **Formato**            | XML                                                |
| **Estándar**           | CFDI 3.3 (Comprobante Fiscal Digital por Internet) |

CFDI 3.3 es la generación anterior del estándar mexicano de comprobante fiscal digital emitido por el SAT (Servicio de Administración Tributaria). Aunque fue sustituida por CFDI 4.0, muchas facturas históricas siguen utilizando esta versión. Incluye el UUID (folio fiscal), los identificadores RFC y los cálculos de impuestos IEPS/IVA.

## Estado de compatibilidad

| Componente             | Estado          |
| ---------------------- | --------------- |
| Vista previa           | ✅ Compatible    |
| Extracción de campos   | ✅ Compatible    |
| Transformación         | ✅ Compatible    |

## Vista previa predeterminada

<figure><img src="../../../../../../.gitbook/assets/mexico-cfdi-3-3-preview.png" alt="Vista previa de la factura México CFDI 3.3 en DocBits"><figcaption><p>Vista previa predeterminada de DocBits para una factura CFDI 3.3 de México</p></figcaption></figure>

## Relacionado

* [Documentos electrónicos compatibles](./)
