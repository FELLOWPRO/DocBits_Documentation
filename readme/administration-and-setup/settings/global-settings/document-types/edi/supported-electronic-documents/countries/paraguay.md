---
description: "Paraguay DTE, SIFEN y SIFEN 150 son etiquetas configuradas."
---

# Paraguay

Utilice esta guía para identificar la familia configurada y el alcance de versiones antes de probar un archivo de origen.

[Todos los países y alcance de la compatibilidad](../README.md)

## Variantes y límites de versión

Paraguay DTE, SIFEN y SIFEN 150 son etiquetas configuradas.

**Sintaxis:** XML

Las entradas de clasificación de notas de crédito carecen de paquetes de extracción dedicados en el estado inspeccionado. Verifique la asignación utilizada y no trate las etiquetas como intercambiables.

Las tablas recogen una comprobación del catálogo de desarrollo realizada el 17 de octubre de 2026 y del código de procesamiento correspondiente. Describen las reglas y los componentes de configuración disponibles; no certifican todos los archivos, los requisitos legales ni el despliegue en producción. Su organización puede sobrescribir los valores predeterminados.

## Matriz de reglas y componentes inspeccionados

| Etiqueta de formato exacta | Clave de documento de la regla | Componentes disponibles |
| --- | --- | --- |
| `PARAGUAY DTE` | `CREDIT_NOTE` | C / — / — / — |
| `PARAGUAY SIFEN` | `CREDIT_NOTE` | C / — / — / — |
| `PARAGUAY DTE` | `INVOICE` | C / T / P / E |
| `PARAGUAY SIFEN` | `INVOICE` | C / T / P / E |
| `PARAGUAY SIFEN 150` | `INVOICE` | C / T / P / E |

C = clasificación, T = Transformation, P = Preview, E = Extraction Paths. La clave de documento se utiliza para buscar la regla o configuración; no garantiza el valor final almacenado de invoice_type. Una transformación puede clasificar una nota de crédito mediante una asignación INVOICE.

Un guion indica que la comprobación de estado no informó de un componente dedicado para esa combinación exacta de formato y clave de documento. No descarta una asignación compartida o alternativa. Verifique la lógica de resolución que se está utilizando y un archivo representativo antes de depender de esa ruta.

## Encuentre la asignación en DocBits

<figure><img src="../../../../../../../.gitbook/assets/edocs-support-paraguay-es.png" alt="Paraguay: PARAGUAY SIFEN 150"><figcaption><p>Interfaz real de desarrollo: el formato representativo y sus componentes de configuración disponibles. Las demás versiones figuran en la matriz.</p></figcaption></figure>

## Vídeo explicativo del país

La narración y los subtítulos WebVTT en el idioma correspondiente explican la selección del formato, la configuración y las pruebas de aceptación.

{% file src="../../../../../../../.gitbook/assets/edocs-support-paraguay-es.mp4" %}
Paraguay — Vídeo explicativo del país
{% endfile %}

{% file src="../../../../../../../.gitbook/assets/edocs-support-paraguay-es.vtt" %}
WebVTT
{% endfile %}

## Pruebas de aceptación

Una comprobación de componentes confirma que existe una configuración. No es una prueba de procesamiento de principio a fin para todas las versiones. Pruebe el contenido exacto y la ruta de factura o nota de crédito que necesite su integración.

## Compruebe un formato en su organización

1. Conserve el XML original o el PDF con su XML incrustado. Consulte el espacio de nombres, el identificador de esquema o de personalización y la versión y el perfil declarados.

2. Abra Configuración → Tipos de documento → E-Doc para el documento de negocio correspondiente. Busque el formato de documento electrónico exacto que aparece en la guía.

3. Compruebe el origen Default o Custom que se está utilizando y su versión de configuración activa. Revise Transformation, Preview y Extraction Paths. Guardar un borrador no lo activa.

4. Pruebe archivos de origen representativos de cada sintaxis, versión y documento de negocio que necesite. Verifique los campos clave, los importes, los impuestos, la clasificación como factura o nota de crédito y la exportación al ERP.

5. Confirme por separado la política de validación y el transporte. Conserve las asignaciones personalizadas y compruebe las aprobaciones y el historial de exportación antes de reiniciar documentos existentes.

## Referencia de formato relacionada

- [🇵🇾 PARAGUAY DTE](../paraguay-dte.md)
- [🇵🇾 PARAGUAY SIFEN](../paraguay-sifen.md)
- [🇵🇾 PARAGUAY SIFEN 150](../paraguay-sifen-150.md)
