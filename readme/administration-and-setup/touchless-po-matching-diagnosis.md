# Touchless Intelligence: Diagnóstico de la coincidencia con la OC

## Descripción general

Muchas facturas se detienen en la orden de compra. La factura dice una cosa, la orden de compra (OC) dice otra, y DocBits no puede decidir por sí solo si corresponden entre sí. Cada documento de este tipo necesita a una persona, por lo que **no es touchless**.

Touchless Intelligence le muestra **por qué** falló una coincidencia con la OC y **cómo** intentó DocBits hacerla. Esta página explica las dos etapas del pipeline implicadas, los motivos que verá y el **flujo de decisión de la coincidencia con la OC**, un diagrama que muestra los pasos de la coincidencia uno tras otro.

### Dónde ve la coincidencia con la OC en Touchless Intelligence

| Dónde | Qué ve |
| --- | --- |
| **Where touchless is lost first** (pestaña de resumen) | Una barra como *PO line match: PO item mismatch*. Le indica cuántos documentos se detuvieron ahí |
| **Supplier opportunities** | Un proveedor con la causa raíz **PO matching** |
| **Supplier Diagnosis**, sección **How this organisation matches** y el **issue cluster** | El flujo de decisión con el conjunto de reglas de su organización |
| **Document Trace** | La etapa **PO Line Match** con el estado **blocked** y el motivo |
| **Settings → Document Types → More Settings → Purchase Order** | Las reglas de coincidencia en sí. Véase [Reglas de Coincidencia de Órdenes de Compra](settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) |

## Las dos etapas de la OC

| Etapa | Pregunta | Se detiene con |
| --- | --- | --- |
| **9 · PO Lookup** | ¿Existe una orden de compra para esta factura? | *Purchase order not found* |
| **10 · PO Line Match** | ¿Coincide cada línea de la factura con una línea de la OC? | *PO item mismatch*, *PO line identifier mismatch*, *Unit price outside PO tolerance*, *Quantity outside PO tolerance* |

Un documento que se detiene en la etapa 9 o 10 aparece en la cola de proveedores con el primer bloqueo **PO matching**.

## Motivos por los que falla una coincidencia con la OC

| Motivo que ve | Qué significa | Causa habitual | Qué cambiar |
| --- | --- | --- | --- |
| **Purchase order not found** | DocBits no encontró ninguna orden de compra para el número de OC de la factura | El número de OC se lee mal o falta; la OC todavía no se importó; la OC pertenece a otro proveedor | Revise la extracción del número de OC para este proveedor, la importación de datos maestros de OC y el vínculo con el proveedor |
| **PO item mismatch** | Las líneas de la factura no coincidieron con las líneas de la OC | El proveedor usa sus propios números de artículo; la descripción difiere; las líneas se fusionaron o se dividieron | Revise la asignación de números de artículo y las **rule priorities** en las reglas de coincidencia; añada una regla para la forma en que el proveedor identifica las líneas |
| **PO line identifier mismatch** | El número o identificador de línea de la factura no coincide con la OC | El proveedor vuelve a numerar las líneas | Haga la coincidencia por artículo y cantidad en lugar de por número de línea |
| **Unit price outside PO tolerance** | El precio difiere más de la tolerancia permitida | Un cambio de precio real, una diferencia de redondeo o una unidad de precio distinta | Revise la **Unit price tolerance** en el conjunto de reglas; corrija la OC o consulte al proveedor |
| **Quantity outside PO tolerance** | La cantidad difiere más de la tolerancia permitida | Entrega parcial, entrega excesiva | Revise **Match quantity on** y la **Quantity tolerance** |
| **PO matching service error** | El servicio de coincidencia no pudo responder | Un problema técnico temporal | Reinicie los documentos; póngase en contacto con el soporte si se repite |
| **Automatic PO export disabled** | El ajuste **Auto export if PO matched 100%** está desactivado, por lo que los documentos coincidentes no se exportan automáticamente | El ajuste está desactivado | Active el ajuste si desea la exportación automática. Véase [Auto Export if PO Matched 100%](settings/document-processing/module/auto-export-if-po-matched-100.md) |

{% hint style="info" %}
No todos los motivos de coincidencia con la OC se pueden corregir en DocBits. Si el proveedor envía un número de OC incorrecto, la tarjeta indica **Supplier action only**: el proveedor tiene que corregir el documento y volver a enviarlo.
{% endhint %}

## El flujo de decisión de la coincidencia con la OC

El flujo de decisión muestra cómo intenta DocBits hacer coincidir una línea de factura con una línea de la OC. Tiene **cinco etapas** y gana la primera coincidencia:

1. **Single match validation**: aplicar las reglas por orden de prioridad. Es el caso normal, una línea de factura y una línea de la OC
2. **Multi match validation**: después de una coincidencia simple, cuando hay varias líneas implicadas en uno de los lados
3. **Total match validation**: solo cuando no coincidió nada. El total de la línea de la OC se compara con la suma de sus líneas de tabla
4. **Single mismatch validation**: se ignora el precio unitario, de modo que una línea puede coincidir por artículo y cantidad aunque el precio difiera
5. **Fallback logic**: quedan una línea de la OC y una línea de tabla, por lo que se emparejan

Dentro de las etapas, DocBits prueba, en este orden:

* **Exact match for all rules**: todos los valores comparados son idénticos
* **Tolerance-based match**: los valores numéricos pueden desviarse dentro de la tolerancia
* **Package criteria**: la última pasada, basada en los criterios relacionados con el paquete del conjunto de reglas

Cada paso pregunta **Match found?** La respuesta **Yes** (verde) lleva a **Match found** y el documento continúa. La respuesta **No match** (rojo) pasa al siguiente paso y, tras el último paso, el resultado es **No match found**: el documento se detiene y necesita a una persona.

<figure><img src="../.gitbook/assets/touchless-po-matching-flow.png" alt="El flujo de decisión de la coincidencia con la OC: encabezado del conjunto de reglas, cinco etapas de coincidencia numeradas con sus pasadas y los puntos finales Match found y No match found"><figcaption><p>El flujo de decisión de la coincidencia con la OC, abierto desde <strong>How this organisation matches</strong> en la página Supplier Diagnosis. El encabezado muestra el conjunto de reglas (versión 7, propiedad de esta organización) y las tolerancias. Debajo, las cinco etapas con sus pasadas van de arriba abajo. El verde lleva a <strong>Match found</strong>, el rojo pasa al siguiente paso y termina en <strong>No match found</strong>. Organización de ejemplo con datos de demostración.</p></figcaption></figure>

### Qué le dice el encabezado del diagrama

| Campo | Significado |
| --- | --- |
| **Document type** | El tipo de documento al que pertenece el conjunto de reglas, por ejemplo INVOICE |
| **Rule set version** | La versión de las reglas de coincidencia, por ejemplo v3 |
| **Rule set owner** | **This organisation** (sus propias reglas) o **Shipped default rule set** (las reglas estándar de DocBits) |
| **Published** | Cuándo se publicó la versión |
| **Match quantity on** | Qué cantidad se compara (cantidad pedida, cantidad abierta) |
| **Tolerance amount** | Si las tolerancias provienen de los atributos del tipo de documento o del conjunto de reglas |
| **Unit price tolerance** / **Quantity tolerance** | Cuánto puede desviarse un precio o una cantidad |
| **Default tolerance** | La tolerancia para todos los demás valores numéricos |

En el ejemplo anterior, las tolerancias muestran **not configured** y **not in force: attribute decides**. Eso significa que el propio conjunto de reglas no tiene tolerancia propia, y la línea **Tolerance amount** indica que las tolerancias provienen de los **atributos del tipo de documento**. Una tolerancia solo decide cuando está en vigor. Lea esta línea primero cuando una diferencia de precio o de cantidad bloquee documentos: le dice **dónde** cambiar la tolerancia.

El estado del conjunto de reglas se muestra como una nota: **Active version** (estas reglas deciden), **Approved, not active**, **Draft, not yet in force** o **Version state unknown**. Solo la versión activa decide.

Si las reglas de transformación modificaron un documento antes de la coincidencia, el diagrama lo indica, por ejemplo *2 applied: (names)* o *"(rule)" rebuilt (table): the PO match was lost here*. Es una causa oculta frecuente: una regla que reformatea una tabla puede romper una coincidencia que antes funcionaba.

## Ejemplos

Las cifras de los ejemplos son ilustrativas.

### Ejemplo 1: Precio dentro de la tolerancia

Una línea de factura tiene un precio unitario de **10.40**. La línea de la OC dice **10.00**. La tolerancia del precio unitario es del **5 %**.

* **Exact match** falla (10.40 no es 10.00).
* **Tolerance-based match** tiene éxito: la diferencia es del **4 %**, que está dentro del 5 %.
* La línea coincide. **Match found.**

Con una tolerancia del **3 %**, la tolerance-based match también falla. Después de todas las etapas, el documento se detiene con **Unit price outside PO tolerance**. El diagrama muestra exactamente este recorrido, y la solución es la tolerancia (si el 4 % es aceptable para su negocio) o una corrección por parte del proveedor.

### Ejemplo 2: Los números de artículo del proveedor difieren de los suyos

Un proveedor factura el artículo **"A-4711-X"**, su OC dice **"4711"**. Ninguna regla compara ambos, por lo que no se encuentra coincidencia, y Touchless Intelligence agrupa todas las facturas de este proveedor en un clúster: **PO line match, PO item mismatch**, 27 documentos.

* En el clúster lee *27 affected, 27 recoverable*, con una mejora esperada de, por ejemplo, **+8.7 pp**.
* La solución está de su lado: añada o reordene una regla que haga la coincidencia por el número de artículo del proveedor o por la descripción, o mantenga los números de artículo del proveedor en los datos maestros.
* Después de cambiar la regla, aplique el cambio con una [propuesta de cambio](touchless-change-proposals.md) y lea el **Change history** dos semanas más tarde: tasa pura antes y después.

### Ejemplo 3: La orden de compra todavía no está

Las facturas llegan antes de que se importara la OC. Se detienen en **PO Lookup** con **Purchase order not found**. El clúster muestra un pico breve. La solución es el orden de sus procesos, o el calendario de la importación de OC, no las reglas de coincidencia. Revise **Where touchless is lost first**: una barra *PO lookup: Purchase order not found* que crece después de cada hueco en la importación apunta a esta causa.

### Ejemplo 4: Una regla reconstruyó la tabla

Después de que entrara en vigor una regla de transformación para la tabla de un proveedor, la tasa de coincidencia de este proveedor cayó bruscamente. El diagrama de un documento afectado dice *"(rule)" rebuilt (table): the PO match was lost here*. La solución es ajustar o deshacer la regla de transformación, no las reglas de coincidencia.

## Una rutina para los problemas de coincidencia con la OC

1. Abra **Where touchless is lost first**. ¿Está una etapa de coincidencia con la OC entre las tres primeras?
2. Abra **Supplier opportunities** y ordene por **Expected lift**. Tome el proveedor con la causa raíz **PO matching** y el estado **RECOVERABLE**.
3. Abra el **Supplier Diagnosis** y lea el clúster: motivo, documentos afectados, **What to change**, **Missing evidence**.
4. Abra **How this organisation matches** y revise el conjunto de reglas: versión, propietario y tolerancias.
5. Abra un **documento de muestra** y su [Seguimiento del documento](touchless-document-trace.md): ¿qué etapa, qué motivo?
6. Cambie **una** cosa (orden de las reglas, tolerancia, asignación de artículos) con una vista previa, para que el **Change history** pueda medirla.

## Páginas relacionadas

* [Touchless Intelligence](touchless-intelligence.md)
* [Diagnóstico de proveedores y clústeres de problemas](touchless-supplier-diagnosis.md)
* [Seguimiento del documento](touchless-document-trace.md)
* [Propuestas de cambio e informes](touchless-change-proposals.md)
* [Reglas de Coincidencia de Órdenes de Compra](settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md)
* [PO Matching Cards - Complete Guide](workflow/and/compare-with-purchase-order/po-matching-complete-guide.md)
