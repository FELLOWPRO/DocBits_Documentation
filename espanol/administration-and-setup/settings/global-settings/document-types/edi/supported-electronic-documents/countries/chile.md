---
description: "Chile DTE tiene entradas de facturas, notas de crédito y guías de despacho."
---

# Chile

Utilice esta guía para identificar la familia configurada y el alcance de versiones antes de probar un archivo de origen.

[Todos los países y alcance de la compatibilidad](../README.md)

## Variantes y límites de versión

Chile DTE tiene entradas de facturas, notas de crédito y guías de despacho.

**Sintaxis:** XML

Seleccione el tipo de documento de negocio antes de comprobar los campos. Las facturas, las notas de crédito y la información de entrega utilizan asignaciones diferentes.

Las tablas recogen una comprobación del catálogo de desarrollo realizada el 17 de octubre de 2026 y del código de procesamiento correspondiente. Describen las reglas y los componentes de configuración disponibles; no certifican todos los archivos, los requisitos legales ni el despliegue en producción. Su organización puede sobrescribir los valores predeterminados.

## Matriz de reglas y componentes inspeccionados

| Etiqueta de formato exacta | Clave de documento de la regla | Componentes disponibles |
| --- | --- | --- |
| `CHILE DTE FACTURA` | `INVOICE` | C / T / P / E |
| `CHILE DTE GUIA DESPACHO` | `DELIVERY_NOTE` | C / T / P / E |
| `CHILE DTE NOTA CREDITO` | `CREDIT_NOTE` | C / T / P / E |

C = clasificación, T = Transformation, P = Preview, E = Extraction Paths. La clave de documento se utiliza para buscar la regla o configuración; no garantiza el valor final almacenado de invoice_type. Una transformación puede clasificar una nota de crédito mediante una asignación INVOICE.

Un guion indica que la comprobación de estado no informó de un componente dedicado para esa combinación exacta de formato y clave de documento. No descarta una asignación compartida o alternativa. Verifique la lógica de resolución que se está utilizando y un archivo representativo antes de depender de esa ruta.

### Etiquetas de configuración adicionales

Estas etiquetas tienen entradas de configuración, pero no una regla de clasificación independiente en el catálogo inspeccionado. Una familia genérica o una identificación más precisa pueden permitir seleccionar una ruta compatible. Su presencia por sí sola no demuestra la detección automática de esa publicación o perfil.

- `CHILE DTE`
- `CHILE FACTURA ELECTRONICA`

## Encuentre la asignación en DocBits

<figure><img src="../../../../../../../.gitbook/assets/edocs-support-chile-es.png" alt="Chile: CHILE DTE FACTURA"><figcaption><p>Interfaz real de desarrollo: el formato representativo y sus componentes de configuración disponibles. Las demás versiones figuran en la matriz.</p></figcaption></figure>

## Vídeo explicativo del país

La narración y los subtítulos WebVTT en el idioma correspondiente explican la selección del formato, la configuración y las pruebas de aceptación.

Este recorrido de solo lectura muestra la configuración existente del país en DocBits. Compruebe la fuente utilizada y la versión activa y valide facturas, notas de crédito y exportaciones representativas en su organización.

{% file src="../../../../../../../.gitbook/assets/edocs-support-chile-es-v2.mp4" %}
Chile — Vídeo explicativo del país
{% endfile %}

{% file src="../../../../../../../.gitbook/assets/edocs-support-chile-es-v2.vtt" %}
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

- [🇨🇱 CHILE DTE](../chile-dte.md)
