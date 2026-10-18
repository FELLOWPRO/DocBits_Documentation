---
description: Compatibilidad de DocBits con el documento electrónico INVOIC02
---

# INVOIC02

<!-- edocs-country-scope -->

{% hint style="info" %}
Consulte la guía del país para conocer los límites de versión, la configuración que se está utilizando y el vídeo explicativo del país. [Internacional](countries/international.md). Las asignaciones de facturas, pedidos, respuestas y avisos de expedición son diferentes. El procesamiento de archivos no proporciona por sí mismo un punto de acceso Peppol ni conectividad con socios comerciales.
{% endhint %}

| Propiedad              | Valor                   |
| ---------------------- | ----------------------- |
| **País / Región**      | Internacional           |
| **Tipos de documento** | Factura                 |
| **Formato**            | EDIFACT                 |
| **Estándar**           | UN/EDIFACT INVOIC D.02B |

INVOIC02 es un mensaje de factura UN/EDIFACT basado en la versión de directorio D.02B. EDIFACT (Electronic Data Interchange for Administration, Commerce and Transport) es un estándar EDI muy utilizado en logística, comercio minorista y fabricación. DocBits analiza la estructura de segmentos de EDIFACT y extrae los campos de cabecera, de línea y de resumen.

## Estado de compatibilidad

| Componente             | Estado          |
| ---------------------- | --------------- |
| Vista previa           | ✅ Compatible    |
| Extracción de campos   | ✅ Compatible    |
| Transformación         | ✅ Compatible    |

## Vista previa predeterminada

<figure><img src="../../../../../../.gitbook/assets/invoic02-preview.png" alt="Vista previa de la factura INVOIC02 en DocBits"><figcaption><p>Vista previa predeterminada de DocBits para una factura INVOIC02</p></figcaption></figure>

## Relacionado

* [Documentos electrónicos compatibles](./)
