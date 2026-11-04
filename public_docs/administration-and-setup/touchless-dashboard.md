# Usar el panel

<!-- touchless-admin-video-v2-20261104:start -->
**Capítulo del vídeo (versión de revisión):** [Selección y fecha de los datos](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/es.html#chapter=01).
<!-- touchless-admin-video-v2-20261104:end -->

### Filtros

| Filtro | Qué hace |
| --- | --- |
| **7D / 30D / 90D** | El período para las cifras clave y la cola. El valor predeterminado es 30 días |
| **Document Type** | Filtra las métricas Touchless y su análisis por tipo. El apartado de reglas aprendidas tiene actualmente su propia selección; véase la nota siguiente. |
| **Segment field / Segment value** | Solo si su organización ejecuta varios procesos con un mismo tipo de documento (por ejemplo, pedidos directos, indirectos y EAM en el campo `order_type`). Elija un campo para ver el desglose y un valor para limitar todo a ese valor |
| **Document ID** | Abre el **Document Trace** de un documento |

La **suborganización** que seleccionó en la parte superior de DocBits limita las cifras clave y la cola de proveedores. Los clústeres de problemas y el análisis con IA siempre abarcan toda la organización.

### Tipo de documento y reglas aprendidas

La selección superior y la del apartado de reglas aprendidas son independientes en la implementación comprobada. Ese apartado carga sus tipos y elige inicialmente el primero. Arriba puede figurar **ORDER_CONFIRMATION** y abajo seguir **INVOICE**: esas reglas afectan a facturas, no a confirmaciones de pedido. Antes de aplicar una regla, compruebe su tipo local. Si no está disponible el tipo adecuado, no hay propuestas acreditadas para él. Su muestra de correcciones, por ejemplo de 60 días, tampoco adopta automáticamente el período de la tasa superior. Esta descripción no afirma que la sincronización esté implementada.

### Las cinco cifras clave

<figure><img src="../.gitbook/assets/touchless-report-kpi-es-20261104.png" alt="Informe actual de facturas a 30 días: 107 totalmente automáticas más 11 con solo aprobación dan 118 de 201, es decir, 58,7 % AP Touchless. Pure por separado es 53,2 %. La tarjeta AP ya incluye las 118. Historial ficticio de formación; no acredita una exportación ERP ejecutada."><figcaption><p>Informe actual de facturas a 30 días: 107 totalmente automáticas más 11 con solo aprobación dan 118 de 201, es decir, 58,7 % AP Touchless. Pure por separado es 53,2 %. La tarjeta AP ya incluye las 118. Historial ficticio de formación; no acredita una exportación ERP ejecutada.</p></figcaption></figure>

| Tarjeta | Qué incluye | Captura actual |
| --- | --- | --- |
| Pure Touchless | Finalización automática sin intervención ni aprobación | 107 · 53,2 % |
| AP Touchless | Pure más solo aprobación; porcentaje y número combinados | 118 · 58,7 % |
| AP Assisted | Finalizadas correctamente con intervención manual | 37 · 18,4 % |
| Excepciones de proceso | Resultado clasificado como excepción | 46 · 22,9 % |
| Cobertura del diagnóstico | Casos bloqueados con una causa conocida | 100 % · 0 sin causa conocida |

* Una tarjeta muestra un guion (—) en lugar de **0 %** cuando no hay nada que medir. Un guion significa "sin datos", no "cero".
* **Diagnosis coverage** = documentos con un motivo de bloqueo conocido ÷ todos los documentos bloqueados. Ejemplo: 50 documentos bloqueados, 10 con una causa desconocida → 40 ÷ 50 = **80 %**. Un valor bajo significa "todavía no entendemos por qué se detienen los documentos". Mejórelo antes de intentar corregir causas individuales.
* **Haga clic en una tarjeta** para abrir en una pestaña nueva la lista de documentos que hay detrás de la cifra ("View the documents behind this number"). Las tarjetas con 0 documentos no se pueden pulsar.

### Evolución de la tasa de procesamiento sin intervención

<figure><img src="../.gitbook/assets/touchless-report-trend-es-20261104.png" alt="Tendencia actual: rosa es Pure Touchless; azul es la tasa combinada que incluye los casos con solo aprobación. La línea discontinua marca el objetivo del 70 %. Los datos ficticios de formación no demuestran una mejora real del proceso."><figcaption><p>Tendencia actual: rosa es Pure Touchless; azul es la tasa combinada que incluye los casos con solo aprobación. La línea discontinua marca el objetivo del 70 %. Los datos ficticios de formación no demuestran una mejora real del proceso.</p></figcaption></figure>

El gráfico actual muestra Pure, AP combinado y el objetivo. Azul incluye Pure y solo aprobación, por lo que está al mismo nivel o por encima de rosa; no sume ambas tasas. Cada punto usa su propia población de documentos finalizados y elegibles: una tasa diaria no equivale automáticamente a la tasa del período completo. Los períodos cortos usan puntos diarios y los largos, semanales. La categoría separada de solo aprobación no es esta línea combinada.

**Ejemplo.** Una tasa Pure que pasa del 55 al 68 % después de un cambio muestra una asociación temporal. Compare tipo, proveedores y otros cambios: el antes/después no demuestra por sí solo una causa única.

### Dónde se interrumpe primero el procesamiento sin intervención

<figure><img src="../.gitbook/assets/touchless-blocking-stages-es.png" alt="Gráfico de barras de los documentos bloqueados por primera etapa de bloqueo y motivo"><figcaption><p>Documentos bloqueados según la etapa y el motivo en los que se detuvieron primero. Aquí <strong>Field validation: Required field missing</strong> cuesta más documentos (58), seguido de <strong>Export mapping failed</strong> (46) y <strong>PO item mismatch</strong> (27). Organización de ejemplo con datos de demostración; los nombres de proveedores son ficticios.</p></figcaption></figure>

Un gráfico de barras de **Blocked documents** por etapa del pipeline: la **primera** etapa que detuvo un documento.

**Ejemplo.** Si las barras muestran identificación del proveedor 12, validación de campos 41 y coincidencia de posiciones 7, investigue primero la validación. Un valor no extraído es una causa posible; compare original, reglas y datos de origen antes de confirmarla.

### Oportunidades por proveedor


La cola responde a **"¿Qué proveedor deberíamos corregir primero?"**. Está ordenada por documentos **Recoverable**, de mayor a menor, con 25 filas por página.

| Columna | Significado |
| --- | --- |
| **Supplier Number / Supplier** | El proveedor. Los documentos sin un proveedor reconocido aparecen como **No supplier identified (n documents)** |
| **Volume** | Documentos elegibles del proveedor en el período |
| **Pure Rate** | Proporción de documentos pure touchless. Verde si está en el objetivo o por encima, rojo si está por debajo |
| **Lost Documents** | Documentos que terminaron como AP assisted o como process exception. No siempre interviene una persona: un rechazo del ERP o un documento estancado durante siete días también cuentan |
| **Root Cause** | Quién es responsable de la corrección: Configuration, ERP integration, Export, Extraction, Master data, Measurement, PO matching, User process, Validation o Unknown |
| **Recoverable** | Documentos perdidos cuya causa DocBits puede corregir: configuración, datos maestros o plantilla del proveedor |
| **Expected Lift** | Cuántos **puntos porcentuales** ganaría la tasa de su organización si cada documento recuperable de este proveedor se procesara touchless (**+x pp**) |
| **Confidence** | **High**, **Medium** o **Low**: cuán seguro es el diagnóstico |
| **Status** | New, Open, Investigating, In progress, Confirmed, Resolved, Dismissed. Un proveedor con muy pocos documentos muestra **NEEDS_DIAGNOSIS** |

**Ejemplo.** Su organización tiene 1,000 documentos elegibles en el período. El proveedor A tiene 40 documentos recuperables; el proveedor B tiene 90 documentos perdidos, pero solo 10 recuperables (su problema está de su lado).

* Proveedor A: 40 ÷ 1,000 = **+4.0 pp de mejora esperada**
* Proveedor B: 10 ÷ 1,000 = **+1.0 pp**, aunque B tiene más documentos perdidos

La cola clasifica a A por encima de B porque la **mejora esperada** se mide con respecto a toda su organización, no con respecto al proveedor. Un proveedor con cuatro documentos malos no puede superar a uno con cuatrocientos.

Utilice el cuadro de búsqueda ("Search supplier number or name") para encontrar un proveedor. Haga clic en una fila para abrir el **Supplier Diagnosis**.

### Comparar proveedores


Haga clic en **Compare suppliers**, marque **de dos a cinco** proveedores (cada uno aparece con su número de documentos bloqueados) y haga clic en **Compare**.

La comparación muestra los proveedores lado a lado: **Pure rate**, **Lost documents**, **Recoverable**, **Root cause**, **Expected lift**, un gráfico de barras de los resultados y un enlace al **Supplier Diagnosis** de cada uno.

**Ejemplo.** A y B usan el mismo diseño; B tiene 80 % Pure y A 35 %. Si el diagnóstico sugiere datos maestros, compare originales, extracción y registros importados. La diferencia de tasas no demuestra por sí sola que el diseño sea correcto ni que los datos de A estén incompletos.

### Analizar con IA

El botón **Analyse n clusters with AI** analiza los clústeres de problemas con mayor potencial touchless (como mínimo un número mínimo de documentos cada uno). Tarda unos 13 segundos por clúster y abarca **toda la organización**. Solo los administradores pueden iniciarlo.

Mientras se ejecuta, verá **Queued**, **Running**, **Done**, **Already analysed** o **Error** para cada clúster, con un enlace **Open cluster**. Si la IA está desactivada o no está configurada en el entorno, el botón aparece desactivado con el motivo, y **todo lo demás en la página sigue funcionando**.

## Trabajar con Touchless Intelligence: una rutina

1. **Cada semana**: abra la pestaña y compare la **tasa** y la **tendencia** con el objetivo.
2. Revise **Diagnosis coverage**. Si está por debajo de aproximadamente el 80 %, averigüe primero por qué se detienen los documentos.
3. Lea **Where touchless is lost first** y elija la etapa más grande.
4. Abra **Supplier opportunities**. Ordene por **Expected lift** y tome el primer proveedor con el estado **RECOVERABLE**.
5. Lea los **issue clusters**, revise **Missing evidence** y siga después **What to change**.
6. Corrija una causa confirmada. Para una propuesta compatible de DocBits use vista previa e historial. Para una corrección en Infor, documente fuente e importación por separado; no crea automáticamente una modificación de configuración en ese historial.
7. Transcurridas dos semanas, revise el resultado de **antes/después**.

## Quién puede verla

* La pestaña forma parte del Panel de Análisis. Su administrador la habilita para la organización. Si falta la pestaña, consulte a su administrador.
* Los **administradores de la organización** siempre la ven.
* Los demás usuarios la ven cuando un administrador ha concedido a su rol la pestaña **Analytics dashboard** (**Settings → Roles**). Sin esa concesión, solo los administradores tienen acceso.
* Algunas acciones son solo para administradores: **AI analysis**, **aplicar y deshacer un cambio**, **learned rule proposals** y el **Consulting report**.

Si no tiene permiso, la página muestra *Action not allowed, please contact the administrator* (acción no permitida, póngase en contacto con el administrador).

## Páginas relacionadas

* [Touchless Intelligence](touchless-intelligence.md)
* [Métricas y cálculo](touchless-metrics.md)
* [Ejemplos: precio y cantidad](touchless-examples.md)
* [Touchless Intelligence: Diagnóstico de proveedores y clústeres de problemas](touchless-supplier-diagnosis.md)
* [Touchless Intelligence: Diagnóstico de la coincidencia con la OC](touchless-po-matching-diagnosis.md)
* [Touchless Intelligence: Seguimiento del documento](touchless-document-trace.md)
* [Touchless Intelligence: Propuestas de cambio e informes](touchless-change-proposals.md)
* [Explicar y mejorar Touchless con MCP](touchless-mcp.md)

<!-- Source notes (not shown): screenshots come from the dev test organisation with synthetic demo data (seed script) and fictional supplier names; the PO matching decision flow has no screenshot yet. facts read from the doc2app code (TouchlessIntelligence pages and components) and the dev UI on 14 Oct 2026; NOVA gates the tab with its own organisation flag, VESTA with the Analytics module. Consulting report export format not verified, so no export is described.
-->
<!-- Touchless documentation alignment 2026-11-04: extraction quality is distinct from process automation. KPI definition checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4; existing native screenshots and video sources preserved except unsafe historical list images. -->
<!-- Completion 2026-11-04: localized MCP examples, AP actions, original-value evidence and owned synthetic PO cards. -->
