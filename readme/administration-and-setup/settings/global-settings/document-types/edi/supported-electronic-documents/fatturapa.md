---
description: Compatibilidad de DocBits con el documento electrónico FATTURAPA
---

# 🇮🇹 FATTURAPA

<!-- edocs-country-scope -->

{% hint style="info" %}
Consulte la guía del país para conocer los límites de versión, la configuración que se está utilizando y el vídeo explicativo del país. [Italia](countries/italy.md). La etiqueta de familia no certifica todas las publicaciones de FatturaPA ni la transmisión por SDI. Compruebe el esquema de origen y los requisitos del receptor.
{% endhint %}

| Propiedad              | Valor                                    |
| ---------------------- | ---------------------------------------- |
| **País / Región**      | Italia                                   |
| **Tipos de documento** | Factura, Nota de crédito, Factura simplificada |
| **Formato**            | XML (FatturaPA 1.2.x)                    |
| **Estándar**           | FatturaPA (SDI)                          |

FatturaPA es el estándar italiano de facturación electrónica impuesto por la Agenzia delle Entrate. Desde enero de 2019, todas las facturas entre empresas italianas deben transmitirse a través del Sistema di Interscambio (SDI). DocBits procesa los documentos XML de FatturaPA y extrae todos los campos de cabecera y de línea.

## Estado de compatibilidad

| Componente             | Estado          |
| ---------------------- | --------------- |
| Vista previa           | ✅ Compatible    |
| Extracción de campos   | ✅ Compatible    |
| Transformación         | ✅ Compatible    |

## Vista previa predeterminada

<figure><img src="../../../../../../.gitbook/assets/fatturapa-preview.png" alt="Vista previa de la factura FatturaPA en DocBits"><figcaption><p>Vista previa predeterminada de DocBits para una factura FatturaPA de Italia</p></figcaption></figure>

## Relacionado

* [Documentos electrónicos compatibles](./)
