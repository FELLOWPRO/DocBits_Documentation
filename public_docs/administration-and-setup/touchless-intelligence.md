# Touchless Intelligence

Touchless Intelligence responde a dos preguntas distintas: **¿DocBits extrajo correctamente la factura?** y **¿Terminó todo el proceso sin intervención de procesamiento?** Una extracción correcta todavía puede requerir trabajo cuando los datos de Infor difieren. AP es el equipo humano de cuentas por pagar.

## Vídeo: funciones del informe Touchless

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/es.mp4" %}

Esta versión de revisión de 5:00 muestra un informe con datos: filtros, indicadores y cálculo, evolución, primeros bloqueos, pruebas registradas, historial del documento, ejecuciones, reglas aprendidas, mejoras e historial, consultoría y resultados MCP reales.

[Abrir el vídeo con subtítulos en español y 16 capítulos](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/es.html). La revisión auditiva de esta nueva versión sigue pendiente.

Estos casos didácticos explican funciones del informe. Una recomendación o vista previa no demuestra un cambio aplicado ni una mejora medida. La propuesta MCP mostrada aún necesita una configuración de destino concreta; no admite vista previa ni aplicación. Algunos textos nativos del producto pueden conservar su idioma original. En las reglas aprendidas, «20 de 21» indica a cuántos casos se aplica la regla. El contraejemplo muestra un valor ya aceptado que la regla sustituiría; algunos rótulos nativos lo traducen de forma imprecisa.

<figure><img src="../.gitbook/assets/anatomy-touchless-es.svg" alt="Línea de clasificación isométrica: una cinta transportadora con 14 compuertas, un empujador que desvía un documento a una bandeja de revisión, un contenedor de exportación con una pila de documentos y un indicador que marca 78,9 %"><figcaption><p>Touchless como línea de clasificación, con las cifras ilustrativas del ejemplo de cálculo: las 14 compuertas son las etapas del Pipeline Path, las hojas que aún están en la cinta están en proceso y no cuentan, un documento que se detiene en una compuerta se empuja a la bandeja de revisión junto con los documentos AP assisted (30) y de excepción de proceso (10), y los documentos Pure touchless (120) y de solo aprobación (30) del contenedor de exportación dan los 150 de 190 del indicador, o 78,9 %, por encima de la marca objetivo del 70 %.</p></figcaption></figure>

## Encontrar la guía adecuada

| Guía | Contenido |
| --- | --- |
| [Métricas y cálculo](touchless-metrics.md) | Categorías, numerador y denominador, intervenciones y cálculos |
| [Usar el panel](touchless-dashboard.md) | Filtros, indicadores, tendencias y primeros bloqueos |
| [Ejemplos: precio y cantidad](touchless-examples.md) | Facturas ficticias y capturas reales en Dev con diferencias de precio y cantidad |
| [Touchless Intelligence: Diagnóstico de proveedores y clústeres de problemas](touchless-supplier-diagnosis.md) | Priorizar proveedores y causas recurrentes |
| [Touchless Intelligence: Diagnóstico de la coincidencia con la OC](touchless-po-matching-diagnosis.md) | Entender reglas activas, tolerancias y decisiones |
| [Touchless Intelligence: Seguimiento del documento](touchless-document-trace.md) | Comprobar originales, ejecuciones, bloqueos e intervenciones |
| [Touchless Intelligence: Propuestas de cambio e informes](touchless-change-proposals.md) | Separar vista previa, aplicación, medición y reversión |
| [Explicar y mejorar Touchless con MCP](touchless-mcp.md) | Explicar, diagnosticar y mejorar de forma controlada con MCP |

<figure><img src="../.gitbook/assets/touchless-overview-es.png" alt="La pestaña Touchless Intelligence con cinco cifras clave, sugerencias de mejora y el gráfico de la tasa touchless"><figcaption><p>La pestaña Touchless Intelligence: cifras clave, mejoras, la tasa a lo largo del tiempo y el gráfico de dónde se pierde primero el touchless. Organización de ejemplo con datos de demostración; los nombres de proveedores son ficticios.</p></figcaption></figure>

## Acceso

Este apartado pertenece al [Panel de Análisis](analytics-dashboard.md). Los administradores tienen acceso; otros usuarios necesitan el permiso de rol correspondiente. El análisis con IA, los cambios compatibles y los informes pueden requerir derechos de administrador.

<!-- Source notes (not shown): screenshots come from the dev test organisation with synthetic demo data (seed script) and fictional supplier names; the PO matching decision flow has no screenshot yet. facts read from the doc2app code (TouchlessIntelligence pages and components) and the dev UI on 14 Oct 2026; NOVA gates the tab with its own organisation flag, VESTA with the Analytics module. Consulting report export format not verified, so no export is described.
-->
<!-- Touchless documentation alignment 2026-11-04: extraction quality is distinct from process automation. KPI definition checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4; existing native screenshots and video sources preserved except unsafe historical list images. -->
<!-- Completion 2026-11-04: localized MCP examples, AP actions, original-value evidence and owned synthetic PO cards. -->
