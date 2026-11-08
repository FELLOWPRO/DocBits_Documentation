# Touchless Intelligence

Touchless Intelligence responde a dos preguntas distintas: **¿DocBits extrajo correctamente la factura?** Y **¿terminó todo el proceso sin una intervención de procesamiento?** Una extracción correcta todavía puede necesitar trabajo cuando los datos de Infor difieren. AP es el equipo humano de cuentas por pagar.

## Vídeo: funciones del informe Touchless

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/es.mp4" %}

Esta versión de revisión de 5:00 muestra un informe con datos: filtros, cifras clave y cálculo, tendencias, primeros bloqueos, pruebas registradas, historial del documento, comparación de ejecuciones, reglas aprendidas, mejoras e historial, informes de consultoría y resultados MCP reales.

[Abrir el vídeo con subtítulos en español y 16 capítulos](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/es.html). La revisión auditiva de esta nueva versión sigue pendiente.

Estos casos didácticos explican funciones del informe. Una recomendación o una vista previa no demuestra un ajuste aplicado ni una mejora medida. La propuesta de cambio MCP mostrada sigue necesitando una configuración de destino concreta; la vista previa y la aplicación no están disponibles para esa propuesta. Algunos textos nativos del producto pueden conservar su idioma original.

<figure><img src="../../../.gitbook/assets/anatomy-touchless-es.svg" alt="Línea de clasificación isométrica: una cinta transportadora con 14 compuertas, un empujador que desvía un documento a una bandeja de revisión, un contenedor de exportación con una pila de documentos y un indicador que marca 78,9 %"><figcaption><p>Touchless como línea de clasificación, con las cifras ilustrativas del ejemplo de cálculo: las 14 compuertas son las etapas del Pipeline Path, las hojas que aún están en la cinta están en proceso y no cuentan, un documento que se detiene en una compuerta se empuja a la bandeja de revisión junto con los documentos AP assisted (30) y de excepción de proceso (10), y los documentos Pure touchless (120) y de solo aprobación (30) del contenedor de exportación dan los 150 de 190 del indicador, o 78,9 %, por encima de la marca objetivo del 70 %.</p></figcaption></figure>

## Encontrar la guía adecuada

| Guía | Qué cubre |
| --- | --- |
| [Métricas y cálculo](../../touchless-metrics.md) | Categorías de resultado, numerador y denominador, acciones de AP y cálculos |
| [Usar el panel](touchless-dashboard.md) | Filtros, tarjetas KPI, tendencias, primeros bloqueos y controles |
| [Ejemplos: precio y cantidad](touchless-examples.md) | Facturas ficticias y vistas reales de pedidos en Dev con diferencias de precio y cantidad |
| [Touchless Intelligence: Diagnóstico de proveedores y clústeres de problemas](../../touchless-supplier-diagnosis.md) | Priorizar proveedores y causas recurrentes |
| [Touchless Intelligence: Diagnóstico de la coincidencia con la OC](../../touchless-po-matching-diagnosis.md) | Entender reglas activas, tolerancias y el flujo de decisión |
| [Touchless Intelligence: Seguimiento del documento](touchless-document-trace.md) | Inspeccionar valores originales, ejecuciones, bloqueos e intervenciones |
| [Touchless Intelligence: Propuestas de cambio e informes](touchless-change-proposals.md) | Distinguir vista previa, aplicación, medición del efecto y reversión |
| [Explicar y mejorar Touchless con MCP](touchless-mcp.md) | Explicar, diagnosticar y aplicar mejoras controladas mediante MCP |

<figure><img src="../../../.gitbook/assets/touchless-overview-es.png" alt="La pestaña Touchless Intelligence con cinco cifras clave, sugerencias de mejora y el gráfico de la tasa touchless"><figcaption><p>La pestaña Touchless Intelligence: cifras clave, mejoras, la tasa a lo largo del tiempo y el gráfico de dónde se pierde primero el touchless. Organización de ejemplo con datos de demostración; los nombres de proveedores son ficticios.</p></figcaption></figure>

## Ajustes del informe

El informe lee cuatro ajustes de organización que un administrador mantiene en **Settings → Module → Dashboards & Analytics**. Definen el objetivo y la vista de costes; un campo vacío significa que DocBits usa el valor predeterminado.

| Ajuste | Valor predeterminado | Qué controla |
| --- | --- | --- |
| Touchless target | 70 % | La proporción de documentos que debería pasar sin una intervención de procesamiento. El informe lo usa como marca objetivo en el gráfico de la tasa. |
| Minutes per AP intervention | 6 min | El tiempo que un empleado de AP necesita para corregir y liberar un documento. |
| Hourly cost | 40 | El coste de una hora de trabajo de AP en la moneda indicada abajo. |
| Currency | EUR | La moneda de la vista de costes, como código ISO 4217 de tres letras, por ejemplo `EUR`, `CHF` o `USD`. DocBits guarda el código en mayúsculas y rechaza un valor que no sea un código de moneda, de modo que una errata no puede llegar al informe. |

La API vuelve a comprobar los valores guardados y usa el valor predeterminado para un valor con el que no puede trabajar.

## Acceso

Este apartado pertenece al [Panel de Análisis](../). Los administradores tienen acceso; los demás usuarios necesitan la concesión de rol correspondiente. El análisis con IA, los cambios compatibles y los informes de consultoría pueden requerir derechos de administrador.

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->
<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
