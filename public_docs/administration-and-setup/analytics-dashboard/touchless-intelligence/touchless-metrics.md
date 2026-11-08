# Métricas y cálculo

<!-- touchless-admin-video-v2-20261104:start -->
**Capítulo del vídeo (versión de revisión):** [Calcular las tasas](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/es.html#chapter=03).
<!-- touchless-admin-video-v2-20261104:end -->

### Extracción correcta y proceso touchless son cosas distintas

**DocBits puede leer correctamente todos los valores de una factura y la factura puede necesitar aun así la atención de AP porque los datos del sistema de origen difieren.** AP significa Accounts Payable, el equipo que procesa las facturas de proveedor. Compruebe estas dos preguntas por separado:

| Pregunta | Qué comparar | Qué le dice el resultado |
| --- | --- | --- |
| **¿DocBits leyó el documento correctamente?** | La factura original frente a los campos de cabecera y las líneas de tabla extraídos, antes de cualquier corrección manual | Calidad de la extracción: ¿coincide el valor extraído con lo que realmente dice la factura? |
| **¿Pudo terminar el proceso sin una intervención?** | La factura extraída correctamente frente al pedido y a los datos maestros suministrados por Infor ERP, junto con el historial de procesamiento registrado | Automatización del proceso: ¿pudieron completarse las comprobaciones, la coincidencia y la exportación configuradas sin una corrección ni un reinicio? |

Un valor distinto en Infor no le dice por sí mismo qué lado es el equivocado. Compruebe la factura, el pedido acordado y los datos realmente importados en DocBits. El origen puede ser incorrecto, la importación puede estar desactualizada o el proveedor puede haber facturado un valor distinto.

{% hint style="info" %}
**La tasa touchless mide el proceso, no la precisión de la extracción.** Un documento AP assisted no demuestra un error de extracción de DocBits. A la inversa, una etapa de extracción superada o una puntuación de confianza alta no demuestran que todos los valores sean correctos. Para establecerlo, compare el documento original con los valores extraídos.
{% endhint %}

Cada documento termina en exactamente **un** resultado:

| Resultado | Significado | ¿Cuenta en la tasa |
| --- | --- | --- |
| **Pure touchless** | Procesado desde la importación hasta la exportación **sin ninguna intervención humana** | Sí, como éxito |
| **AP touchless** | Se ejecutó automáticamente y una persona solo dio la **aprobación de negocio**. No se necesitó ninguna corrección | Sí, como éxito |
| **AP assisted** | Terminó con éxito, pero una persona tuvo que **corregir un campo, reiniciar el documento** o intervenir de otro modo; esto puede ser necesario incluso cuando la extracción fue correcta | Sí, fuera del numerador touchless; no identifica por sí mismo la causa |
| **Excepción de proceso** | Terminó en **error**, fue **rechazado**, fue **rechazado por el ERP** o se **estancó** en el pipeline | Sí, como fallo |
| **In progress** | Todavía no ha terminado | **No**. Aún no tiene resultado |
| **Not eligible** | Eliminado, archivado, un documento de prueba o un tipo de documento excluido | **No** |

La **tasa AP touchless**, que incluye los documentos con solo aprobación, es:

```
rate = (Pure touchless + AP touchless)
       ÷ (Pure touchless + AP touchless + AP assisted + Process exception)
```

Aquí **AP touchless** en el numerador es el resultado de documento «solo aprobación». El **porcentaje AP touchless** del dashboard es la tasa combinada: documentos pure más documentos con solo aprobación. **No sume los dos porcentajes mostrados.** La tasa pure utiliza solo documentos pure en el numerador, con el mismo denominador.

Los documentos que siguen **in progress** o que son **not eligible** nunca entran en el cálculo. Esto protege la tasa: un documento que llegó hace cinco minutos no puede bajarla.

{% hint style="info" %}
**Un toque cuenta para siempre.** Una vez que una persona ha tocado un documento, este sigue contando como tocado, aunque una ejecución automática posterior no hubiera necesitado a nadie. **Reiniciar un documento no lo vuelve touchless.** La tasa refleja el trabajo que se ha realizado.
{% endhint %}

### Ejemplo de cálculo (cifras ilustrativas)

En 30 días llegaron 200 documentos:

| Resultado | Documentos |
| --- | --- |
| Pure touchless | 120 |
| AP touchless | 30 |
| AP assisted | 30 |
| Excepción de proceso | 10 |
| In progress | 8 |
| Not eligible (documentos de prueba) | 2 |

* Denominador: 120 + 30 + 30 + 10 = **190**. Los 8 documentos in progress y los 2 not eligible quedan fuera.
* **Pure touchless**: 120 ÷ 190 = **63.2 %**
* Cuota con **solo aprobación**: 30 ÷ 190 = **15.8 %**. Es la cuota de ese resultado, no la tasa AP touchless combinada.
* **Tasa AP touchless**: (120 + 30) ÷ 190 = **78.9 %**

La pestaña muestra un **objetivo** (70 % salvo que su organización utilice otro). En este ejemplo la tasa AP combinada está por encima del 70 %, mientras que la tasa pure del 63.2 % está por debajo. Compare el objetivo con la tasa que indica la tarjeta o el gráfico correspondiente.

Haga clic en **How touchless is calculated**, arriba a la derecha, para abrir esta explicación dentro de DocBits, con las cifras de su propio período (documentos del período, aún in progress, excluidos, medidos).

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/touchless-report-methodology-en-20261104.png" alt="Población de formación actual: 201 facturas finalizadas y elegibles, sin ninguna aún en proceso ni excluida. Las 107 facturas totalmente automáticas dan 53.2%; añadiendo 11 facturas de solo aprobación se llega a 118 y 58.7%. Estas tasas del proceso no miden la precisión de la extracción."><figcaption><p>Población de formación actual: 201 facturas finalizadas y elegibles, sin ninguna aún en proceso ni excluida. Las 107 facturas totalmente automáticas dan 53.2%; añadiendo 11 facturas de solo aprobación se llega a 118 y 58.7%. Estas tasas del proceso no miden la precisión de la extracción.</p></figcaption></figure>
<!-- English source image: touchless-report-methodology-en-20261104.png -->

### Ejemplo: 100% de extracción correcta, 80% AP touchless

Supongamos que una revisión de las facturas originales y de sus valores extraídos confirma que **las 100 facturas finalizadas y elegibles se extrajeron correctamente**. Sus resultados de procesamiento son:

| Qué ocurrió | Documentos | Resultado |
| --- | --- | --- |
| Factura y datos de origen coincidían; todo el proceso se completó automáticamente | 70 | Pure touchless |
| Factura y datos de origen coincidían; solo se necesitó la aprobación de negocio | 10 | AP touchless (resultado solo aprobación) |
| Los datos de la factura se extrajeron correctamente, pero los datos importados de Infor diferían. AP aclaró la discrepancia y reinició manualmente los documentos en DocBits después de corregir los datos de origen; luego se completaron con éxito | 20 | AP assisted |

* **Documentos extraídos correctamente en esta muestra revisada:** 100 ÷ 100 = **100%**.
* **Tasa pure touchless:** 70 ÷ 100 = **70%**.
* **Tasa AP touchless:** (70 + 10) ÷ 100 = **80%**.

No hay contradicción: la extracción fue correcta en todas las facturas, mientras que 20 necesitaron una intervención de procesamiento debido a los datos de origen. La **cifra del 100% de extracción es un resultado ilustrativo de una revisión de documentos independiente**, no un KPI adicional que muestre este dashboard. No la calcule solo a partir de los resultados touchless.

### Ejemplos: ¿qué tuvo que hacer realmente AP?

Los casos siguientes son ilustrativos, no son los documentos individuales que hay detrás de las capturas. Los resultados exitosos presuponen que el procesamiento ha terminado, incluida la confirmación del ERP cuando sea necesaria.

| Caso | Factura original / extracción de DocBits / datos de origen | Acción de AP y resultado | Dónde investigar |
| --- | --- | --- | --- |
| **Error de extracción** | Número de pedido `45001234` / extraído incorrectamente como `45001284` / el pedido correcto `45001234` existe en Infor | AP corrige el número extraído; la factura termina como **AP assisted** | Extracción de este proveedor |
| **Discrepancia del sistema de origen** | Precio unitario 10,00 € / extraído correctamente 10,00 € / el pedido importado de Infor indica 9,00 €, fuera de la tolerancia configurada | AP confirma que 10,00 € es el precio acordado, organiza la corrección del pedido y reinicia manualmente la factura en DocBits; termina como **AP assisted** | Datos del pedido en Infor y su importación |
| **Retraso de importación** | El número de pedido es correcto en la factura y en DocBits / el pedido existe en Infor pero no ha llegado a DocBits | Si una importación y un reintento posteriores terminan automáticamente sin una intervención humana ni una aprobación registradas, el resultado puede seguir siendo **Pure touchless**. Un reinicio manual seguido de éxito da **AP assisted** | Momento de la importación e historial real de ejecuciones |
| **Rechazo del ERP** | La extracción es correcta, pero el ERP rechaza el documento exportado | **Excepción de proceso** mientras se clasifique como rechazo definitivo del ERP, incluso si alguien intervino antes | Rechazo del ERP y evidencia de la exportación |

**Incluso una pequeña corrección registrada o un reinicio manual cuentan como intervención.** AP assisted significa «una persona ayudó a procesar el documento»; no es el nombre de un asistente de IA aparte. Un problema de datos de origen y un problema de extracción pueden por tanto tener el mismo resultado y requerir correcciones distintas.

La clasificación utiliza los eventos que DocBits registra. No suponga que el trabajo realizado solo en Infor, sin un evento correspondiente registrado en DocBits, se cuenta automáticamente como intervención de AP. Mantenga también ese trabajo en el diagnóstico.

### ¿Qué acciones de AP cuentan como intervención?

Lo siguiente presupone una finalización correcta, incluida la confirmación del ERP necesaria. Importan la acción registrada y su autor, no cuánto tiempo duró el trabajo.

| Acción | Efecto en el resultado del documento |
| --- | --- |
| Abrir, leer, filtrar, comparar o previsualizar | No crea por sí misma una intervención de procesamiento; Pure Touchless sigue siendo posible |
| Dar la aprobación de negocio, incluida una segunda aprobación | AP Touchless, si no hubo una intervención de procesamiento |
| Cambiar y guardar un campo de cabecera o una celda de tabla | AP Assisted; incluso una sola corrección guardada cuenta |
| Validar y avanzar manualmente un documento, incluso sin corregir un valor | AP Assisted; la validación manual es distinta de la sola aprobación |
| Reiniciar manualmente el procesamiento o la exportación | AP Assisted; una ejecución automática posterior no elimina la intervención |
| Reintento automático del sistema o escritura automática de un workflow | No crea por sí solo una intervención humana; los toques humanos anteriores persisten |
| Corregir datos solo en Infor | El trabajo externo no es automáticamente un evento registrado en DocBits; documéntelo por separado e inspeccione la acción posterior en DocBits |
| Rechazo definitivo del ERP tras una corrección | Prevalece la excepción de proceso; la intervención permanece en el historial |

Un clic en Save sin evidencia de un valor modificado no demuestra una corrección. Compruebe si también desencadenó una validación manual o un reinicio.

### La etiqueta AP tiene dos significados

| Ubicación | Significado |
| --- | --- |
| Porcentaje de cabecera AP | Combinado Pure + solo aprobación: (120 + 30) / 190 = 78.9% |
| Recuento de documentos bajo ese porcentaje en el informe actual | Combinado Pure + solo aprobación: 150 = 120 + 30 |
| Categoría de resultado AP Touchless, como el grupo MCP `AP_TOUCHLESS` | Categoría separada de solo aprobación: 30 / 190 = 15.8% |
| Línea AP azul en la [captura actual de la tendencia del dashboard](touchless-dashboard.md) | Tasa combinada Pure + solo aprobación en cada punto, con la población de ese punto |

Las categorías de resultado final suman el 100% de la población medida. Los porcentajes de cabecera Pure y AP combinado se solapan y no deben sumarse.

### Cómo de actuales son las cifras

Los resultados se **recalculan cada 15 minutos**. El resultado de un documento aún puede cambiar después de aparecer por primera vez: el ERP puede confirmar una exportación horas más tarde. La línea **Data as of …** en la parte inferior de la pestaña muestra cuándo se calcularon las cifras por última vez.





## Páginas relacionadas

* [Touchless Intelligence](./)
* [Usar el dashboard](touchless-dashboard.md)
* [Ejemplos prácticos: precio y cantidad](touchless-examples.md)
* [Diagnóstico de proveedores y clústeres de problemas](touchless-supplier-diagnosis.md)
* [Diagnóstico de la coincidencia con la OC](touchless-po-matching-diagnosis.md)
* [Document Trace](touchless-document-trace.md)
* [Propuestas de cambio e informes](touchless-change-proposals.md)
* [Explicar y mejorar Touchless con MCP](touchless-mcp.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->
<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
