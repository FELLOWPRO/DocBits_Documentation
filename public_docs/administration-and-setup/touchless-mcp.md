# Explicar y mejorar Touchless con MCP

<!-- touchless-admin-video-v2-20261104:start -->
**Capítulo del vídeo (versión de revisión):** [Consultar indicadores con MCP](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/es.html#chapter=12).
<!-- touchless-admin-video-v2-20261104:end -->

Estos procedimientos usan herramientas realmente ofrecidas por DocBits MCP. Distinga lectura y explicación de las operaciones que escriben. Compruebe organización, rol, tipo, período y fecha de datos; no invente evidencia ausente.

<figure><img src="../.gitbook/assets/touchless-owned-po-price-es.png" alt="Vista real en español de un pedido ficticio propio en Dev: 10 × 9 = 90. Es una comparación de origen para el diagnóstico por MCP, no una captura de un cliente MCP ni prueba de extracción o procesamiento correctos."><figcaption><p>Vista real en español de un pedido ficticio propio en Dev: 10 × 9 = 90. Es una comparación de origen para el diagnóstico por MCP, no una captura de un cliente MCP ni prueba de extracción o procesamiento correctos.</p></figcaption></figure>

## Explicar Touchless mediante MCP

> Explica para las facturas de los últimos 30 días Pure Touchless, las aprobaciones y la tasa AP combinada. Indica numerador, denominador, documentos en curso, exclusiones, filtros y fecha de los datos. Separa precisión de extracción y automatización.

Utilice `touchless_get_summary` con `period: "30d"` y `doc_type: "INVOICE"`. Para un subproceso, use los campos y valores realmente devueltos por `touchless_list_segments`. Compare siempre la misma organización, tipo, período y segmento; lea `data_as_of`.

**Contraejemplo verificado en Dev:** Tres facturas recién cargadas seguían `IN_PROGRESS`: `population.total: 3`, `population.in_progress: 3`, `population.eligible: 0`, `official_touchless_rate.ap_pct: null`. Todavía no había tasa calculable. No significa 0 % de precisión ni 100 % Touchless. El `eligible` del resumen se refiere aquí a la población KPI finalizada; una traza individual puede tener `eligible: true` y `bucket_final: false`.

Los ejemplos emplean herramientas MCP reales comprobadas en Dev. Se aplican la organización y los permisos de la cuenta conectada. No prueban la disponibilidad en otra interfaz o lista adicional de herramientas permitidas. Los identificadores técnicos se mantienen sin traducir.

## Investigar discrepancias mediante MCP

> Comprueba pedido, importación y reglas activas. Separa extracción, copia antigua, fuente incorrecta y configuración ausente. Todavía no cambies nada.

1. Compare original, `get_extracted_fields` y `get_extracted_tables` antes de afirmar que la extracción es correcta.
2. Use `get_po_sync_status`, por ejemplo `po_number: "TL20261104X1-PO02"`, `language: "en"`. Este resumen admite `de` o `en`; explique su respuesta en español. El test confirmó importación procesada y pedido presente, no exactitud de negocio ni el estado actual de Infor.
3. Use `touchless_get_document_trace` y `touchless_explain_po_match` con el mismo `doc_id`. Lea motor, versión activa, columnas y tolerancias efectivas. Para un clúster realmente devuelto, use su `issue_signature` en `touchless_get_po_match_evidence`.
4. Preserve lo que falta: el tipo de prueba devolvió `state: "none_published"`, `parse_error: "no published rule set"` y campos vacíos. No se acreditó un bloqueo de precio/cantidad ni un resultado correcto. El flujo genérico no sustituye esas pruebas.
5. Corrija la causa confirmada y revise facturas nuevas. Una corrección o relanzamiento humano persiste tras el éxito; un error ERP definitivo prevalece como excepción. Un documento en curso queda fuera del denominador.

Para acreditar el caso completo hacen falta original, extracción anterior a correcciones, datos importados/actuales y fecha, reglas realmente aplicadas, acción AP y resultado final. La evidencia ausente permanece abierta.

## Leer la evidencia con MCP

> Revisa esta factura sin modificarla. Compara original, campos y tablas actuales. Explica las ejecuciones registradas y señala qué evidencia histórica falta.

| Herramienta con el mismo `doc_id` | Evidencia y límite |
| --- | --- |
| `get_extracted_fields` | Valores actuales y confianza; no una instantánea histórica |
| `get_extracted_tables` | Tablas y filas existentes; no su coincidencia con el original |
| `touchless_get_document_trace` | Resultados, intervenciones, etapas y ejecuciones registradas |
| `touchless_explain_pipeline` | Explicación del proceso acreditado; no completa pruebas ausentes |

**Comprobación negativa real:** La factura de prueba tenía `header_extraction: passed`, pero `extracted_field_count: 0`, ocho campos obligatorios vacíos y ninguna tabla. La validación bloqueó con `REQUIRED_FIELD_MISSING`. Hay que revisar la extracción/configuración; una etapa verde no acredita extracción correcta ni un bloqueo de precio de pedido.

### ¿Una acción MCP es intervención humana?

Leer no cambia la factura. Otras herramientas pueden escribir, validar o reiniciar. La clasificación depende del evento y del autor registrado: una clave API puede actuar como cuenta de sistema. «Ejecutado por MCP» no demuestra ni intervención humana ni Pure Touchless. No utilice una cuenta de sistema para ocultar trabajo humano.

Compruebe `human_touched`, `human_touch_source`, `human_restart_count`, `business_approval_touched`, estado final y ejecuciones. Solo aprobación no equivale a corrección guardada, validación manual o reinicio humano.

## Priorizar proveedores y comprobar mejoras con MCP

> Ordena los proveedores que pierden más documentos Touchless. Separa errores de extracción, discrepancias de datos importados y reglas del proceso. Propón una acción y una comprobación por causa confirmada; todavía no cambies nada.

1. Use `touchless_rank_supplier_opportunities` con `period: "30d"`, `doc_type: "INVOICE"`, `order_by_field: "lost_docs"`, `order_by_direction: "desc"`. `search` busca nombre o número; `limit` y `offset` permiten paginar.
2. Pase el `supplier_key` devuelto a `touchless_diagnose_supplier`. Use `window: 30` para la situación actual o 90 para investigar recurrencias.
3. Pase un `issue_signature` real a `touchless_get_issue_cluster`. Revise documentos y evidencia ausente antes de confirmar la causa. No invente identificadores.
4. `touchless_get_recommendations` explica medidas compatibles. La mejora esperada es estimada; no sume clústeres solapados.
5. Compruebe nuevas facturas comparables y la medición posterior. Las facturas ya intervenidas no se vuelven Pure retroactivamente.

Si la extracción es correcta y los pedidos están desactualizados, corrija fuente/importación. Si el original difiere de la extracción, investigue la configuración de extracción. Una aprobación de negocio exigida sigue siendo AP Touchless tras el éxito. Una clasificación vacía no demuestra ausencia de problemas: las tres facturas de prueba en curso todavía no producían resultados de proveedor finalizados. Revise filtros, fecha, identificación del proveedor y volumen finalizado.

## Previsualizar, aplicar y medir mediante MCP

> Explica la causa confirmada y enumera propuestas compatibles. Previsualiza el cambio seleccionado y sus riesgos. Aplica solo ese cambio elegido; comprueba después el valor guardado, el historial y el efecto medible.

| Paso | Herramienta e identificadores reales | Resultado |
| --- | --- | --- |
| Enumerar | `touchless_list_change_proposals`, opcional `issue_signature`, `window: "30d"`, `lang: "es"` | Propuestas existentes; no guarda configuración |
| Previsualizar | `touchless_preview_change` con `proposal_id` e `issue_signature` devueltos | Alcance concreto y, si está permitido, `preview_token` vinculado |
| Aplicar el cambio elegido | `touchless_apply_change` con los mismos IDs, token, `overrides` y `window` | **Escribe** el ajuste compatible; si tiene éxito devuelve `change_id` |
| Leer el efecto | `touchless_verify_change` con ese `change_id` y el mismo `window` | Antes/después; siguen siendo necesarios al menos 20 documentos finalizados elegibles por período |

Copie IDs y token de respuestas reales. Una vista previa de un valor no permite aplicar otro. Una vista expirada, prohibida o incompleta no acredita aplicación. La tabla explica la secuencia; no afirma que el caso de demostración aplicara una propuesta o midiera una mejora.

Tras una corrección de configuración confirmada, compruebe el ajuste y nuevas facturas. Pasar del 52 al 61 % son 9 puntos porcentuales observados, no prueba de una causa única. Una orden incorrecta en Infor requiere corrección de negocio e importación verificada: `touchless_apply_change` no es una herramienta general de escritura en Infor. No amplíe tolerancias para ocultar datos incorrectos.

El informe muestra estimaciones, no aplicación ni devolución. Una aplicación necesita respuesta correcta y entrada de historial. Deshacer solo está disponible si la propuesta lo permite; verifique el ajuste restablecido. Recargar el historial no aplica cambios; deshacer no borra las intervenciones pasadas.

## Páginas relacionadas

* [Touchless Intelligence](touchless-intelligence.md)
* [Métricas y cálculo](touchless-metrics.md)
* [Usar el panel](touchless-dashboard.md)
* [Ejemplos: precio y cantidad](touchless-examples.md)
* [Touchless Intelligence: Diagnóstico de proveedores y clústeres de problemas](touchless-supplier-diagnosis.md)
* [Touchless Intelligence: Diagnóstico de la coincidencia con la OC](touchless-po-matching-diagnosis.md)
* [Touchless Intelligence: Seguimiento del documento](touchless-document-trace.md)
* [Touchless Intelligence: Propuestas de cambio e informes](touchless-change-proposals.md)

<!-- Source notes (not shown): screenshots come from the dev test organisation with synthetic demo data (seed script) and fictional supplier names; the PO matching decision flow has no screenshot yet. facts read from the doc2app code (TouchlessIntelligence pages and components) and the dev UI on 14 Oct 2026; NOVA gates the tab with its own organisation flag, VESTA with the Analytics module. Consulting report export format not verified, so no export is described.
-->
<!-- Touchless documentation alignment 2026-11-04: extraction quality is distinct from process automation. KPI definition checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4; existing native screenshots and video sources preserved except unsafe historical list images. -->
<!-- Completion 2026-11-04: localized MCP examples, AP actions, original-value evidence and owned synthetic PO cards. -->
