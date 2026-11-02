---
description: Compatibilidad de DocBits con el documento electrónico ZUGFERD 1.0
---

# 🇩🇪 ZUGFERD 1.0

<!-- edocs-country-scope -->

{% hint style="info" %}
Consulte la guía del país para conocer los límites de versión, la configuración que se está utilizando y el vídeo explicativo del país. [Alemania](countries/germany.md). La sintaxis, la versión de publicación y el perfil son opciones diferentes. No deduzca una publicación de Factur-X a partir del marcador compartido 1p0.
{% endhint %}

| Propiedad                | Valor                              |
| ------------------------ | ---------------------------------- |
| **País / Región**        | Alemania                           |
| **Tipos de documento**   | Factura, Nota de crédito           |
| **Formato**              | CII (incrustado en PDF/A-3)        |
| **Estándar**             | ZUGFeRD 1.0                        |
| **Basado en**            | Especificación ZUGFeRD 1.0         |

ZUGFeRD 1.0 fue el estándar híbrido alemán de facturación original, publicado en 2014. Incrusta un archivo XML CII (ZUGFeRD-invoice.xml) dentro de un documento PDF/A-3. Esta versión es anterior a la norma europea EN 16931 y utiliza su propio sistema de perfiles.

## Estado de compatibilidad

| Componente                 | Estado        |
| -------------------------- | ------------- |
| Vista previa               | ✅ Compatible |
| Extracción de campos       | ✅ Compatible |
| Transformación             | ✅ Compatible |

## Vista previa predeterminada

<figure><img src="../../../../../../.gitbook/assets/zugferd-preview.png" alt="Vista previa de una factura ZUGFeRD 1.0 en DocBits"><figcaption><p>Vista previa predeterminada de DocBits para una factura ZUGFeRD 1.0 de Alemania</p></figcaption></figure>

## Relacionado

* [Configuración de ZUGFeRD](../zugferd/)
* [Asignación de campos de ZUGFeRD](../zugferd/README.md)
* [Documentos electrónicos compatibles](./)
