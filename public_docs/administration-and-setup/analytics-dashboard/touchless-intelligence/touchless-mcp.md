# Explicar y mejorar Touchless con MCP

<!-- touchless-admin-video-v2-20261104:start -->
**Capítulo del vídeo (versión de revisión):** [Consultar cifras con MCP](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/es.html#chapter=12).
<!-- touchless-admin-video-v2-20261104:end -->

Los siguientes procedimientos usan herramientas que DocBits MCP ofrece realmente. Distinga la lectura y la explicación de la escritura. Compruebe la organización, el rol, el tipo de documento, el período y la fecha de los datos; no invente pruebas ausentes.

<figure><img src="../../../.gitbook/assets/touchless-owned-po-price-es.png" alt="Vista real en inglés de Dev de un pedido ficticio propio: 10 × 9 = 90. Es una comparación de origen para el diagnóstico con MCP, no una captura de un cliente MCP ni una prueba de extracción o procesamiento correctos."><figcaption><p>Vista real en inglés de Dev de un pedido ficticio propio: 10 × 9 = 90. Es una comparación de origen para el diagnóstico con MCP, no una captura de un cliente MCP ni una prueba de extracción o procesamiento correctos.</p></figcaption></figure>

## Explicar Touchless mediante MCP

> Explica Pure Touchless, los resultados de solo aprobación y la tasa AP combinada de las facturas de los últimos 30 días. Indica el numerador, el denominador, los documentos en curso y excluidos, el alcance y la fecha de los datos. Mantén separada la corrección de la extracción.

Utilice `touchless_get_summary` con `period: "30d"` y `doc_type: "INVOICE"`. Para un subproceso, use únicamente los campos y valores de segmento que devuelva realmente `touchless_list_segments`. Compare el panel y MCP con la misma organización, tipo de documento, segmento y período; lea `data_as_of`.

**Contraejemplo verificado en Dev:** tres facturas de prueba recién cargadas seguían `IN_PROGRESS`. El resumen devolvió `population.total: 3`, `population.in_progress: 3`, `population.eligible: 0` y `official_touchless_rate.ap_pct: null`. Todavía no se podía medir ninguna tasa. Esto no es ni un 0 % de precisión de extracción ni un 100 % Touchless. La elegibilidad del resumen se refiere aquí a la población KPI finalizada; un seguimiento individual puede mostrar a la vez `eligible: true` y `bucket_final: false`.

Los ejemplos MCP de estas cinco páginas usan herramientas DocBits MCP directas comprobadas en Dev. Se aplican la organización y el rol de su cuenta conectada; esa prueba no establece la disponibilidad en otra interfaz ni en una lista adicional de herramientas permitidas.

## Preguntas frecuentes

**DocBits extrajo todo correctamente. ¿Por qué la factura es AP assisted?**
Touchless mide todo el proceso. Unos datos de Infor incorrectos o desactualizados pueden exigir una corrección registrada o un reinicio manual aunque la extracción sea correcta. Compruebe por separado la factura original, los valores que extrajo DocBits y los datos de origen importados.

**¿AP assisted me dice si el trabajo lo causó DocBits o Infor?**
No. Registra la intervención, no la responsabilidad. Utilice el seguimiento del documento y los datos del documento y de origen subyacentes para confirmar la causa.

**Las tasas muestran un guion (—).** Ningún documento ha alcanzado un resultado final en el período, o se han medido menos documentos que el mínimo. Los documentos que siguen en curso no se cuentan.

**Falta la pestaña.** Pida a su administrador que active el módulo y que conceda a su rol la pestaña **Analytics dashboard**.

**Un documento se cuenta como intervenido, pero esta vez pasó sin que nadie lo tocara.** Se intervino en una ejecución anterior (una corrección o un reinicio). La tasa cuenta el trabajo que se realizó.

**¿Por qué cambia la cifra al cabo de unas horas?** El ERP puede confirmar una exportación horas después de enviarla. El resultado se recalcula cada 15 minutos.

**¿La IA cambia algo por su cuenta?** No. La IA solo escribe explicaciones. Un ajuste cambia únicamente después de que un administrador lo previsualice y lo aplique.

## Investigar discrepancias mediante MCP

> Comprueba el número de pedido de esta factura, el estado de la importación y las reglas de coincidencia realmente activas. Separa la extracción, una importación desactualizada, unos datos de origen incorrectos y una configuración ausente. Todavía no cambies nada.

1. Compare el original, `get_extracted_fields` y `get_extracted_tables` antes de afirmar que la extracción es correcta.
2. Use `get_po_sync_status` con `po_number: "TL20261104X1-PO02"` y `language: "en"`. La prueba en Dev confirmó una importación procesada y un pedido existente. Esto demuestra la llegada, no la corrección de negocio ni el registro actual de Infor.
3. Use `touchless_get_document_trace` y `touchless_explain_po_match` con el mismo `doc_id`. Lea el motor real, la versión de regla activa, las columnas y las tolerancias efectivas. Para un clúster realmente devuelto, use su `issue_signature` en `touchless_get_po_match_evidence`.
4. Conserve las pruebas ausentes: nuestro nuevo tipo de prueba devolvió `state: "none_published"` y `parse_error: "no published rule set"`, así como campos de extracción vacíos. No se demostró ningún bloqueo de precio o cantidad ni una coincidencia correcta. Un flujo de decisión genérico no puede sustituir esas comprobaciones ausentes.
5. Corrija la causa confirmada y compruebe las facturas nuevas. La corrección o el reinicio humano siguen siendo relevantes después del éxito; un error definitivo del ERP tiene prioridad como excepción, y un documento sin terminar queda fuera del denominador de la tasa.

Para un caso completo, conserve el original, la extracción anterior a la corrección, los valores de origen importados y actuales con el momento de la importación, las reglas reales, la acción de AP y el resultado final. La evidencia ausente permanece abierta.

## Leer las pruebas mediante MCP

> Inspecciona esta factura sin modificarla. Compara el original con los campos y las tablas actuales. Explica las etapas y ejecuciones registradas e identifica qué pruebas históricas de extracción faltan.

| Herramienta, con el mismo `doc_id` | Prueba y límite |
| --- | --- |
| `get_extracted_fields` | Valores de cabecera y confianza actuales; no una instantánea histórica |
| `get_extracted_tables` | Tablas y filas reales; no la prueba de que coincidan con el original |
| `touchless_get_document_trace` | Resultados, intervenciones, etapas y ejecuciones registradas |
| `touchless_explain_pipeline` | Explicación de la ruta de procesamiento acreditada; no completa las pruebas ausentes |

**Comprobación negativa observada:** nuestra factura de prueba nueva tenía una etapa de extracción de cabecera `passed`, pero `extracted_field_count: 0`, ocho campos obligatorios vacíos y ninguna tabla. La validación de campos se bloqueó con `REQUIRED_FIELD_MISSING`. El asistente debe investigar la extracción o la configuración ausentes, en lugar de afirmar una extracción correcta a partir de una etapa en verde o un bloqueo de precio de pedido demostrado a partir de valores de origen distintos.

### ¿Una acción MCP cuenta como intervención humana?

La inspección de solo lectura no cambia una factura. Otras herramientas MCP pueden escribir campos, validar o reiniciar. La clasificación depende del evento registrado y de si su autor es una persona o una cuenta de sistema. Una clave API puede actuar como cuenta de sistema; "ejecutado mediante MCP" por sí solo no demuestra ni una intervención humana ni Pure Touchless. Nunca use credenciales de sistema para ocultar trabajo humano repetido.

Después de una acción sobre un documento, inspeccione `human_touched`, `human_touch_source`, `human_restart_count`, `business_approval_touched`, el estado final y las ejecuciones. Solo una aprobación de negocio es distinto de una corrección guardada, una validación manual o un reinicio humano.

## Priorizar proveedores y verificar una mejora duradera mediante MCP

> Clasifica los proveedores que pierden más facturas Touchless. Separa los errores de extracción, las discrepancias de origen importado y los ajustes del proceso. Propón una acción y una comprobación de éxito verificable para cada causa confirmada; todavía no cambies nada.

1. Use `touchless_rank_supplier_opportunities` con `period: "30d"`, `doc_type: "INVOICE"`, `order_by_field: "lost_docs"`, `order_by_direction: "desc"`. Use `search` para un número o nombre de proveedor; `limit` y `offset` paginan los resultados.
2. Pase el `supplier_key` devuelto sin cambios a `touchless_diagnose_supplier`. Use `window: 30` para los problemas actuales o 90 para investigar problemas recurrentes.
3. Pase un `issue_signature` realmente devuelto a `touchless_get_issue_cluster`. Revise los documentos de ejemplo y las pruebas ausentes antes de confirmar la causa. No invente identificadores.
4. Use `touchless_get_recommendations` para explicar una acción compatible. La mejora esperada es una estimación; los clústeres solapados no deben sumarse sin más.
5. Compruebe las facturas nuevas comparables después de la corrección y la [medición del cambio](touchless-change-proposals.md). Las facturas ya intervenidas no pasan a ser Pure Touchless de forma retroactiva.

Para una extracción correcta y pedidos desactualizados, corrija los datos de origen o de importación. Para una discrepancia entre el original y la extracción, investigue la configuración de la extracción. Una aprobación exigida por política es un resultado AP Touchless correcto distinto. Una clasificación vacía no es prueba de que no haya problemas: nuestras tres facturas de prueba en curso todavía no producían ningún resultado de proveedor clasificado. Compruebe el alcance, la fecha de los datos, la identificación del proveedor y el volumen finalizado.

## Previsualizar, aplicar y medir mediante MCP

> Explica la causa confirmada y enumera las propuestas compatibles. Previsualiza el cambio seleccionado, su alcance y sus riesgos. Aplica solo ese cambio elegido y verifica después el ajuste guardado, el historial de cambios y el efecto medible.

| Paso | Herramienta e identificadores devueltos reales | Qué demuestra |
| --- | --- | --- |
| Enumerar | `touchless_list_change_proposals`, opcional `issue_signature`, `window: "30d"`, `lang: "en"` | Propuestas disponibles; no se guarda ningún ajuste |
| Previsualizar | `touchless_preview_change` con el `proposal_id` devuelto y el `issue_signature` correspondiente | Alcance concreto y un `preview_token` vinculado cuando está permitido |
| Aplicar el cambio seleccionado | `touchless_apply_change` con los mismos IDs, `preview_token`, `overrides` y `window` | **Escribe** el ajuste compatible; una respuesta correcta devuelve un `change_id` |
| Leer el efecto | `touchless_verify_change` con ese `change_id` y el mismo `window` | Medición antes/después; siguen siendo necesarios al menos 20 documentos finalizados elegibles por período |

Copie los IDs y tokens de respuestas reales. Un token que previsualiza un valor no puede aplicar otro valor. Una vista previa caducada, prohibida o incompleta no acredita un cambio aplicado. Las herramientas de solo lectura y la aplicación no deben describirse como equivalentes. Esta tabla explica la secuencia de herramientas; no afirma que la demostración ejecutara una propuesta ni midiera una ganancia.

**Ejemplo de configuración:** tras una corrección de configuración confirmada, inspeccione el valor guardado real y las facturas nuevas. Pasar del 52 % al 61 % es una diferencia observada de 9 puntos porcentuales, no la prueba de que este cambio por sí solo la causara. **Ejemplo de datos de origen:** un pedido de Infor incorrecto necesita una corrección de negocio y una importación verificada. `touchless_apply_change` no es una herramienta general de escritura en Infor. No amplíe las tolerancias para ocultar datos de origen incorrectos.

La captura del informe muestra recomendaciones e impacto estimado, no la aplicación ni la reversión. Una aplicación correcta necesita una respuesta de éxito y una entrada en el historial. Undo solo está disponible cuando la propuesta seleccionada lo admite; verifique el ajuste realmente restablecido. Volver a cargar el historial no aplica ningún ajuste, y la reversión no elimina las intervenciones pasadas sobre documentos.

## Páginas relacionadas

* [Touchless Intelligence](./)
* [Métricas y cálculo](touchless-metrics.md)
* [Usar el panel](touchless-dashboard.md)
* [Ejemplos: precio y cantidad](touchless-examples.md)
* [Touchless Intelligence: Diagnóstico de proveedores y clústeres de problemas](touchless-supplier-diagnosis.md)
* [Touchless Intelligence: Diagnóstico de la coincidencia con la OC](touchless-po-matching-diagnosis.md)
* [Touchless Intelligence: Seguimiento del documento](touchless-document-trace.md)
* [Touchless Intelligence: Propuestas de cambio e informes](touchless-change-proposals.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->
<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
