---
description: Compatibilidad de DocBits con el documento electrónico FACTURX
---

# 🇫🇷 FACTURX

| Propiedad                | Valor                         |
| ------------------------ | ----------------------------- |
| **País / Región**        | Francia / Alemania            |
| **Tipos de documento**   | Factura, Nota de crédito      |
| **Formato**              | CII (incrustado en PDF/A-3)   |
| **Estándar**             | Factur-X                      |
| **Basado en**            | EN 16931                      |

Factur-X es la implementación francesa del estándar híbrido de facturación franco-alemán. Incrusta datos XML CII estructurados dentro de un documento PDF/A-3, lo que permite una facturación legible por personas y procesable por máquinas. DocBits detecta automáticamente la versión y el perfil de Factur-X a partir del XML incrustado.

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
* [Asignación de campos de ZUGFeRD](../zugferd/versions/)
* [Documentos electrónicos compatibles](./)
