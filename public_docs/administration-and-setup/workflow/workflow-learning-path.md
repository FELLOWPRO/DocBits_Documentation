---
description: "Aprendizaje desde principiante hasta experto"
---

# Aprendizaje desde principiante hasta experto

Siete niveles le llevan de la primera mirada al diseñador de workflows hasta la responsabilidad de un cambio en un workflow en producción. Cada nivel indica un objetivo, los pasos que realiza en su propia organización de prueba y un resultado que puede comprobar. Recórralos en orden y construya cada ejercicio usted mismo: cada nivel se apoya en la configuración del anterior.

1. [Orientación y modelo de ejecución](./#level-1)
2. [Primera regla propia](./#level-2)
3. [Campos, tipos y límites](./#level-3)
4. [Reglas de negocio y aprobaciones](./#level-4)
5. [Control Advanced y subworkflows](./#level-5)
6. [Cálculo, integración y exportación](./#level-6)
7. [Cambios y operación experta](./#level-7)

## Antes de empezar

* Una organización de prueba propia con una factura sintética dentro. Nunca practique con documentos de clientes.
* Su rol, la licencia de workflow y el permiso Advanced, comprobados antes del nivel 1.
* Los ejercicios importados permanecen inactivos hasta que los haya probado.
* Los datos JSON completos van en **Advanced Test → Custom Data**.
* Las aprobaciones e integraciones reales necesitan sus propios usuarios y destinos de prueba; una prueba en el diseñador no los sustituye.

## 1. Orientación y modelo de ejecución <a href="#level-1" id="level-1"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/es.mp4" %}

[Abrir el vídeo con subtítulos y transcripción en español](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/es.html).

**Objetivo:** Saber qué inicia un workflow y qué puede afirmar un resultado de prueba sobre una ejecución real, y qué no.

1. Compruebe la organización, su acceso, el módulo de workflow y el permiso Advanced.
2. Diga When–And–Then con sus propias palabras y explique después dónde termina una regla lineal y cómo un grafo Advanced sigue en cambio sus salidas conectadas.
3. Mantenga separadas cuatro cosas que en el diseñador se parecen: el filtro de tipo de documento, el evento de ejecución, el guardado y la activación.

**Criterio de finalización:** Puede decir cuándo se considera una regla y qué prueba separa una simulación de una ejecución sobre un documento real.

**Detalle:** [¿Cuándo se ejecuta mi workflow?](workflow-execution-model.md) · [Cambiar el estado sin reiniciar el workflow](masterclass/status-and-reentry.md)

## 2. Primera regla propia <a href="#level-2" id="level-2"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/es.mp4" %}

[Abrir el vídeo con subtítulos y transcripción en español](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/es.html).

**Objetivo:** Llevar una regla del diseñador a un resultado comprobado sin tocar un documento.

1. Créela en el Advanced Builder: When Invoice → And invoice\_id = WF-TRAINING-001 → And total\_amount > 1000 → Then wf\_training\_route = REVIEW. Una regla lineal de este tamaño no necesita nodo de control.
2. Guárdela y compruebe en la lista de reglas que sigue inactiva, porque guardar una regla nueva ya puede activarla. Advanced Test es una superficie de ejecución aparte: evalúa el grafo del constructor, no la regla activada.
3. Ejecute Advanced Test con datos completos para 999, 1000 y 1000.01. Anote por caso el tipo de campo, el operador y la salida elegida, y añada un caso en el que falte el importe por completo.

**Criterio de finalización:** REVIEW solo se alcanza con 1000.01, un importe ausente aparece como error y no como resultado normal por debajo del umbral, y la regla vuelve a estar desactivada al final.

**Detalle:** [Caso de negocio Advanced: enrutado de facturas](advanced-workflow-case-study.md) · [Kit de ejercicios de workflow](workflow-training-kit.md)

## 3. Campos, tipos y límites <a href="#level-3" id="level-3"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/es.mp4" %}

[Abrir el vídeo con subtítulos y transcripción en español](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/es.html).

**Objetivo:** Saber qué compara realmente una condición antes de fiarse de su resultado.

1. Pruebe la comprobación de vacío contra un campo ausente, `null`, texto vacío, espacios, `false`, `0`, `"0"` y `"false"`, y anote cuáles cuentan como vacíos.
2. Calcule dos veces la misma tolerancia del 2 por ciento: una con el pedido como referencia (pedido 100, documento 102.02) y otra con el documento como referencia.
3. Alterne entre Any y All en la tarjeta de pedido y cuente cuántas líneas se compararon realmente.

**Criterio de finalización:** Explica verdadero, falso y error a partir del valor, el tipo, la referencia y los datos disponibles. En la versión 5 de la tarjeta de pedido, un documento sin línea comparable es un error de datos y no una aprobación correcta.

**Detalle:** [P1: Field is, Docfield is y comparar dos campos](masterclass/field-conditions.md) · [P1: Fijar tolerancias y referencia de pedido sin ambigüedad](masterclass/tolerances-and-po.md)

## 4. Reglas de negocio y aprobaciones <a href="#level-4" id="level-4"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/es.mp4" %}

[Abrir el vídeo con subtítulos y transcripción en español](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/es.html).

**Objetivo:** Enviar una factura a la persona correcta mediante una tabla de decisión y, después, ejecutar una cadena de aprobación que espere a la primera persona revisora.

**Ejercicio 1: tabla de decisión con asignación directa**

1. Cree una tabla de decisión con dos reglas que no puedan coincidir a la vez: revisora A hasta 1000, revisora B por encima de 1000, usando `cost_center=4711` y `total_amount`.
2. En **Decision Table has Returns** versión 3, defina `store_data=wf_store_data`. Asigne el documento con **Assign document based on decision table** y `assignee_type=user`, con usuarios reales de su organización de prueba.
3. Pruebe una coincidencia, ninguna, varias y un ID de usuario no válido, y lleve las no coincidencias y los errores de asignación a un repliegue explícito. Acepte la asignación en el propio documento.

**Ejercicio 2: aprobación secuencial sin asignación directa**

1. Cree una segunda regla separada con las tarjetas secuenciales: la tarjeta de asignación secuencial en la posición 10 para la revisora A y después la tarjeta de tarea secuencial en la posición 20 para la revisora B. Deje fuera la asignación directa en esta ejecución, porque la finalización revisada puede saltarse el primer destinatario secuencial si el documento ya se asignó directamente en la misma ejecución.
2. Apruebe como A y compruebe que B recibe el documento solo después de la decisión procesada de A; apruebe después como B.
3. Rechace como A en una ejecución nueva y confirme que el export no se produce. Pruebe a continuación qué ocurre cuando no se puede resolver ningún destinatario.

**Criterio de finalización:** Distingue responsabilidad, tarea, notificación y aprobación efectiva; A → aprobación → B → aprobación ocurrió en ese orden; un rechazo de A impidió el export; y un destinatario ausente no contó como aprobación cerrada.

**Detalle:** [P1: Seguir la tabla de decisión hasta la asignación](masterclass/decision-table-routing.md) · [P1: Distinguir asignación, tarea y aprobación secuencial](masterclass/assignment-task-sequential.md)

## 5. Control Advanced y subworkflows <a href="#level-5" id="level-5"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/es.mp4" %}

[Abrir el vídeo con subtítulos y transcripción en español](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/es.html).

**Objetivo:** Unir correctamente rutas paralelas y entregar trabajo a otro workflow.

1. Compare ALL, ANY y OR con dos comprobaciones realmente alcanzadas: ALL necesita una salida coincidente de cada origen, ANY y OR necesitan una, y verde más naranja del mismo origen siguen contando como un solo origen.
2. Mire una rama que la ejecución no tomó, como en el caso MERGE-04: Advanced Test sigue evaluando la unión en espera, mientras que la ejecución normal la omite en cuanto un predecesor no llega nunca.
3. Ejecute los siete casos del caso práctico v2 (por encima, por debajo, límite, justo por encima, ausente, número no válido, otra factura). Después llame con Run Workflow a un workflow propio inactivo y abra la ruta en el destino mismo.

**Criterio de finalización:** Explica la diferencia del caso MERGE-04 entre prueba y ejecución del paso 2, cómo se cuentan los orígenes y adónde va un error. Una llamada verde a Run Workflow sigue necesitando una comprobación en el destino. V2 se refiere aquí a la segunda versión del grafo del caso práctico: la tarjeta de estado de cada ruta lleva directamente a la tarjeta de cierre común, sin nodo OR en espera.

**Detalle:** [P0: Conectar bien Wait ALL, Wait ANY y OR](masterclass/control-nodes.md) · [P0: Entender Run Workflow, las condiciones de destino y los errores](masterclass/run-workflow.md) · [Caso de negocio Advanced: enrutado de facturas](advanced-workflow-case-study.md)

## 6. Cálculo, integración y exportación <a href="#level-6" id="level-6"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/es.mp4" %}

[Abrir el vídeo con subtítulos y transcripción en español](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/es.html).

**Objetivo:** Calcular valores, recuperar un resultado de un sistema externo y exportar solo después de una aprobación real.

1. Calcule una columna y compare toda la tabla antes y después, incluida una fila en la que la expresión regular no coincide y una división por cero.
2. Escriba el contrato de reescritura con el sistema externo: qué campo del documento recoge el resultado, qué tarjeta o extensión lo escribe ahí y cómo comprueba después el valor guardado. Un HTTP 200 por sí solo no es un resultado.
3. Planifique el export tras la aprobación con su propia configuración y anote qué va a revisar en el destinatario.

**Criterio de finalización:** Los valores posteriores en el campo, la recepción en el destinatario y el procesamiento en el ERP tienen cada uno su propia prueba. Una simulación o un export encolado no es una entrega.

**Detalle:** [P1: Calcular tablas y comprobar la dependencia de regex](masterclass/table-calculations.md) · [P1: Comprobar la llamada a la API y el uso de la respuesta](masterclass/api-response-contract.md) · [P1: Variantes de export, tareas abiertas y estado de cierre](masterclass/export-lifecycle.md)

## 7. Cambios y operación experta <a href="#level-7" id="level-7"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/es.mp4" %}

[Abrir el vídeo con subtítulos y transcripción en español](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/es.html).

**Objetivo:** Modificar un workflow que no construyó y poder revertir el cambio.

1. Exporte el workflow y anote las versiones de las tarjetas antes de tocar nada.
2. Repita tras el cambio los casos positivos, negativos, de error y de límite, más una segunda ejecución del mismo caso.
3. Remonte el primer fallo a una entrada y una configuración concretas y mantenga el export guardado como camino de vuelta.

**Criterio de finalización:** Puede aceptar el cambio, restaurar la configuración guardada y comparar una nueva ejecución documental con pruebas. Anote la causa, la corrección y los límites que permanecen.

**Detalle:** [Diagnosticar errores de workflow de forma sistemática](workflow-troubleshooting.md) · [Entender las tarjetas y configurarlas con fiabilidad](card-reference-standard.md)

## Compruebe lo aprendido

| Pregunta | Respuesta |
| --- | --- |
| ¿`false` cuenta como vacío en Field is v2? | Sí. El número 0 y el texto "false" no están vacíos. |
| ¿Una prueba OR en verde garantiza la ejecución documental? | No. En el caso revisado MERGE-04, una prueba evalúa la unión que una ejecución documental omite cuando un predecesor no llega nunca. |
| ¿Puede Run Workflow llamar a un destino inactivo? | Sí, en la llamada explícita revisada. Compruebe igualmente las condiciones del destino y el resultado. |
| ¿Un HTTP 200 expone automáticamente api.response.cost\_center? | No. Las acciones revisadas no ofrecen ese contrato de salida JSON automático. |
| ¿Una prueba en verde demuestra la recepción del export? | No. La ejecución documental, la recepción en el destinatario y el procesamiento en el ERP necesitan pruebas separadas. |

## Registrar lo que ha aceptado

Descargue `workflow-training-kit-v2.zip` del [kit de ejercicios de workflow](workflow-training-kit.md), descomprímalo y abra `acceptance-record-template.json`. Es un registro vacío y no algo que se importe; el mismo ZIP contiene también los datos, las expectativas y las respuestas de prueba guardadas a las que se refieren los niveles.

Anote qué ha probado y cómo lo sabe: el escenario, la configuración (hash del export del workflow, versiones de las tarjetas), lo que esperaba, lo que observó y qué tipo de prueba tiene. Mantenga separados una prueba en Advanced Test, una comprobación aislada del origen, una ejecución con documento real, la recepción en el destinatario y el procesamiento en el ERP, y deje marcados como abiertos los pasos que no ha probado.
