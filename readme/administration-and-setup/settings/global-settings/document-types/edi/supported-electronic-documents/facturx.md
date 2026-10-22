---
description: Compatibilidad de DocBits con el documento electrónico FACTURX
---

# 🇫🇷 FACTURX

<!-- edocs-country-scope -->

{% hint style="info" %}
Consulte la guía del país para conocer los límites de versión, la configuración que se está utilizando y el vídeo explicativo del país. [Francia](countries/france.md). El marcador XML 1p0 y Factur-X XMP Version 1.0 no identifican una versión de publicación. Mantenga la etiqueta genérica cuando se desconozca la publicación.
{% endhint %}

| Propiedad                | Valor                         |
| ------------------------ | ----------------------------- |
| **País / Región**        | Francia / Alemania            |
| **Tipos de documento**   | Factura, Nota de crédito      |
| **Formato**              | CII (incrustado en PDF/A-3)   |
| **Estándar**             | Factur-X                      |
| **Basado en**            | EN 16931                      |

Un CII Guideline ID armonizado puede identificar una familia y un perfil aunque varias publicaciones compartan el mismo marcador 1p0. Factur-X XMP Version 1.0 es un marcador de esquema, no una publicación como 1.08 o 1.09. El XMP de ZUGFeRD puede declarar su versión. Si no se dispone de metadatos de una fuente autorizada, mantenga el resultado de familia genérica y confirme el archivo original con el remitente.

## Estado de compatibilidad

| Componente                 | Estado        |
| -------------------------- | ------------- |
| Vista previa               | ✅ Compatible |
| Extracción de campos       | ✅ Compatible |
| Transformación             | ✅ Compatible |

## Vista previa predeterminada

<figure><img src="../../../../../../.gitbook/assets/facturx-preview.png" alt="Vista previa de una factura Factur-X en DocBits"><figcaption><p>Vista previa predeterminada de DocBits para una factura Factur-X de Francia</p></figcaption></figure>

## Relacionado

* [Configuración de ZUGFeRD](../zugferd/)
* [Asignación de campos de ZUGFeRD](../zugferd/README.md)
* [Documentos electrónicos compatibles](./)
