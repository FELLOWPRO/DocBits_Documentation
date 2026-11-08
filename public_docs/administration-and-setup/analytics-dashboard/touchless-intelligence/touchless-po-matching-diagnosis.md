# Diagnóstico de la coincidencia con la OC

<!-- touchless-admin-video-v2-20261104:start -->
**Capítulo del vídeo (versión de revisión):** [Seguir un documento](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/es.html#chapter=07).
<!-- touchless-admin-video-v2-20261104:end -->

## Descripción general

Muchas facturas se detienen en el pedido. La factura dice una cosa, el pedido (PO) dice otra, y las comprobaciones configuradas no pueden resolver la diferencia automáticamente. **Una extracción correcta puede aun así llevar a una coincidencia con la OC bloqueada cuando los datos del sistema de origen difieren.** Una parada temporal todavía no es un resultado final: un procesamiento automático posterior puede tener éxito, mientras que una corrección manual o un reinicio registrados impiden que un documento exitoso sea touchless.

Touchless Intelligence le muestra **por qué** falló una coincidencia con la OC y **cómo** intentó DocBits hacer la coincidencia. Esta página explica las dos etapas del pipeline implicadas, los motivos que verá y el **flujo de decisión de la coincidencia con la OC**, un diagrama que muestra los pasos de la coincidencia uno tras otro.

### Dónde ve la coincidencia con la OC en Touchless Intelligence

| Dónde | Qué ve |
| --- | --- |
| **Where touchless is lost first** (pestaña de descripción general) | Una barra como _PO line match: PO item mismatch_. Le indica cuántos documentos se detuvieron ahí |
| **Supplier opportunities** | Un proveedor con la causa raíz **PO matching** |
| **Supplier Diagnosis**, sección **How this organisation matches** y el **issue cluster** | El flujo de decisión con el conjunto de reglas de su organización |
| **Document Trace** | La etapa **PO Line Match** con el estado **blocked** y el motivo |
| **Settings → Document Types → More Settings → Purchase Order** | Las propias reglas de coincidencia. Véase [Purchase Order Matching Rules](../../settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) |

## Las dos etapas de la OC

| Etapa | Pregunta | Se detiene con |
| --- | --- | --- |
| **9 · PO Lookup** | ¿Existe un pedido para esta factura? | _Purchase order not found_ |
| **10 · PO Line Match** | ¿Coincide cada línea de la factura con una línea del pedido? | _PO item mismatch_, _PO line identifier mismatch_, _Unit price outside PO tolerance_, _Quantity outside PO tolerance_ |

Un documento que se detiene en la etapa 9 o 10 aparece con el primer bloqueo **PO matching** en la cola de proveedores.

## Motivos por los que falla una coincidencia con la OC

| Motivo que ve | Qué significa | Causa típica | Qué cambiar |
| --- | --- | --- | --- |
| **Purchase order not found** | DocBits no encontró ningún pedido para el número de pedido de la factura | El número de pedido se lee mal o falta; el pedido aún no se ha importado; el pedido pertenece a otro proveedor | Compruebe la extracción del número de pedido de este proveedor, la importación de datos maestros de pedidos y la vinculación con el proveedor |
| **PO item mismatch** | Las líneas de la factura no coincidieron con las líneas del pedido | El proveedor utiliza sus propios números de artículo; la descripción difiere; las líneas se fusionaron o se dividieron | Compruebe el mapeo de números de artículo y las **rule priorities** de las reglas de coincidencia; añada una regla para la forma en que el proveedor identifica las líneas |
| **PO line identifier mismatch** | El número de línea o el identificador de la factura no coincide con el pedido | El proveedor renumera las líneas | Haga la coincidencia por artículo y cantidad en lugar de por número de línea |
| **Unit price outside PO tolerance** | El precio difiere más que la tolerancia permitida | Un cambio de precio real, una diferencia de redondeo o una unidad de precio distinta | Compruebe la **Unit price tolerance** del conjunto de reglas; corrija el pedido o consulte con el proveedor |
| **Quantity outside PO tolerance** | La cantidad difiere más que la tolerancia permitida | Entrega parcial, entrega en exceso | Compruebe **Match quantity on** y la **Quantity tolerance** |
| **PO matching service error** | El servicio de coincidencia no pudo responder | Un problema técnico temporal | Reinicie los documentos; contacte con el soporte si se repite |
| **Automatic PO export disabled** | El ajuste **Auto export if PO matched 100%** está desactivado, por lo que los documentos coincidentes no se exportan automáticamente | El ajuste está desactivado | Active el ajuste si desea la exportación automática. Véase [Auto Export if PO Matched 100%](../../settings/document-processing/module/auto-export-if-po-matched-100.md) |

{% hint style="info" %}
No todos los motivos de coincidencia con la OC se pueden corregir en DocBits. Si el proveedor envía un número de pedido incorrecto, la tarjeta indica **Supplier action only**: el proveedor tiene que corregir el documento y enviarlo de nuevo.
{% endhint %}

Los casos separados de precio y cantidad y su evidencia se encuentran en [Ejemplos prácticos](touchless-examples.md).


## El flujo de decisión de la coincidencia con la OC

El flujo de decisión muestra cómo intenta DocBits hacer coincidir una línea de factura con una línea de pedido. Tiene **cinco etapas**, y gana la primera coincidencia:

1. **Single match validation**: aplica las reglas por orden de prioridad. Es el caso normal, una línea de factura y una línea de pedido
2. **Multi match validation**: después de una coincidencia única, cuando hay varias líneas implicadas en un lado
3. **Total match validation**: solo cuando nada coincidió en absoluto. El total de la línea de pedido se compara con la suma de sus líneas de tabla
4. **Single mismatch validation**: se ignora el precio unitario, de modo que una línea puede coincidir por artículo y cantidad aunque el precio difiera
5. **Fallback logic**: quedan una línea de pedido y una línea de tabla, por lo que se emparejan

Dentro de las etapas, DocBits intenta, en este orden:

* **Exact match for all rules**: todos los valores comparados son idénticos
* **Tolerance-based match**: los valores numéricos pueden desviarse dentro de la tolerancia
* **Package criteria**: la última pasada, basada en los criterios relacionados con el paquete del conjunto de reglas

Cada paso pregunta **Match found?** La respuesta **Yes** (verde) lleva a **Match found** y el documento continúa. La respuesta **No match** (rojo) pasa al siguiente paso, y después del último paso el resultado es **No match found**: el documento se detiene y necesita a una persona.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/touchless-po-matching-flow.png" alt="El flujo de decisión de la coincidencia con la OC: cabecera del conjunto de reglas, cinco etapas de coincidencia numeradas con sus pasadas y los puntos finales Match found y No match found"><figcaption><p>El flujo de decisión de la coincidencia con la OC, abierto desde <strong>How this organisation matches</strong> en la página Supplier Diagnosis. La cabecera muestra el conjunto de reglas (versión 7, propiedad de esta organización) y las tolerancias. Debajo, las cinco etapas con sus pasadas se ejecutan de arriba abajo. El verde lleva a <strong>Match found</strong>, el rojo pasa al siguiente paso y termina en <strong>No match found</strong>. Organización de ejemplo con datos de demostración.</p></figcaption></figure>

### Qué le dice la cabecera del diagrama

| Campo | Significado |
| --- | --- |
| **Document type** | El tipo de documento al que pertenece el conjunto de reglas, por ejemplo INVOICE |
| **Rule set version** | La versión de las reglas de coincidencia, por ejemplo v3 |
| **Rule set owner** | **This organisation** (sus propias reglas) o **Shipped default rule set** (las reglas estándar de DocBits) |
| **Published** | Cuándo se publicó la versión |
| **Match quantity on** | Qué cantidad se compara (cantidad pedida, cantidad abierta) |
| **Tolerance amount** | Si las tolerancias proceden de los atributos del tipo de documento o del conjunto de reglas |
| **Unit price tolerance** / **Quantity tolerance** | Cuánto puede desviarse un precio o una cantidad |
| **Default tolerance** | La tolerancia para todos los demás valores numéricos |

En el ejemplo anterior, las tolerancias muestran **not configured** y **not in force: attribute decides**. Eso significa: el conjunto de reglas no tiene tolerancia propia y la línea **Tolerance amount** indica que las tolerancias proceden de los **atributos del tipo de documento**. Una tolerancia solo decide cuando está en vigor. Lea esta línea primero cuando una diferencia de precio o cantidad bloquee documentos: le indica **dónde** cambiar la tolerancia.

El estado del conjunto de reglas se muestra como una nota: **Active version** (estas reglas deciden), **Approved, not active**, **Draft, not yet in force** o **Version state unknown**. Solo decide la versión activa.

Si las reglas de transformación modificaron un documento antes de la coincidencia, el diagrama lo indica, por ejemplo _2 applied: (names)_ o _"rule" rebuilt (table): the PO match was lost here_. Es una causa oculta frecuente: una regla que reformatea una tabla puede romper una coincidencia que antes funcionaba.

## Ejemplos

Las cifras de los ejemplos son ilustrativas.

### Ejemplo 1: Precio dentro de la tolerancia

Una línea de factura tiene un precio unitario de **10.40**. La línea de pedido indica **10.00**. La tolerancia de precio unitario es del **5 %**.

* **Exact match** falla (10.40 no es 10.00).
* **Tolerance-based match** tiene éxito: la diferencia es del **4 %**, que está dentro del 5 %.
* La línea coincide. **Match found.**

Con una tolerancia del **3 %** también falla la coincidencia por tolerancia. Después de todas las etapas el documento se detiene con **Unit price outside PO tolerance**. El diagrama muestra exactamente este camino, y la solución es la tolerancia (si un 4 % es aceptable para su negocio) o una corrección en el proveedor.

### Ejemplo 2: Los números de artículo del proveedor difieren de los suyos

Un proveedor factura el artículo **"A-4711-X"**, su pedido indica **"4711"**. Ninguna regla compara ambos, así que no se encuentra coincidencia, y Touchless Intelligence agrupa todas las facturas de este proveedor en un clúster: **PO line match, PO item mismatch**, 27 documentos.

* En el clúster se lee _27 affected, 27 recoverable_, con un aumento esperado por ejemplo de **+8.7 pp**.
* La solución está de su lado: añada o reordene una regla que haga coincidir por el número de artículo del proveedor o por la descripción, o mantenga los números de artículo del proveedor en los datos maestros.
* Después de cambiar la regla, aplique el cambio con una [propuesta de cambio](touchless-change-proposals.md) y lea el **Change history** dos semanas más tarde: tasa AP touchless antes y después.

### Ejemplo 3: El pedido todavía no está

Las facturas llegan antes de que se importe el pedido. Se detienen en **PO Lookup** con **Purchase order not found**. El clúster muestra un pico breve. La solución es el orden de sus procesos, o la planificación de la importación de pedidos, no las reglas de coincidencia. Compruebe **Where touchless is lost first**: una barra _PO lookup: Purchase order not found_ que crece tras cada hueco de importación apunta a esta causa.

### Ejemplo 4: Una regla reconstruyó la tabla

Después de activar una regla de transformación para la tabla de un proveedor, la tasa de coincidencia de ese proveedor cayó bruscamente. El diagrama de un documento afectado indica _"rule" rebuilt (table): the PO match was lost here_. La solución es ajustar o deshacer la regla de transformación, no las reglas de coincidencia.

## Una rutina para problemas de coincidencia con la OC

1. Abra **Where touchless is lost first**. ¿Está una etapa de coincidencia con la OC entre las tres primeras?
2. Abra **Supplier opportunities** y ordene por **Expected lift**. Tome el proveedor con la causa raíz **PO matching** y el estado **RECOVERABLE**.
3. Abra el **Supplier Diagnosis** y lea el clúster: motivo, documentos afectados, **What to change**, **Missing evidence**.
4. Abra **How this organisation matches** y compruebe el conjunto de reglas: versión, propietario y tolerancias.
5. Abra un **documento de muestra** y su [Document Trace](touchless-document-trace.md): ¿qué etapa, qué motivo?
6. Cambie **una** cosa (orden de las reglas, tolerancia, mapeo de artículos) con una vista previa, para que el **Change history** pueda medirlo.

## Páginas relacionadas

* [Touchless Intelligence](./)
* [Diagnóstico de proveedores y clústeres de problemas](touchless-supplier-diagnosis.md)
* [Document Trace](touchless-document-trace.md)
* [Propuestas de cambio e informes](touchless-change-proposals.md)
* [Purchase Order Matching Rules](../../settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md)
* [PO Matching Cards: Complete Guide](../../workflow/cards-overview/po-matching-complete-guide.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->

<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
