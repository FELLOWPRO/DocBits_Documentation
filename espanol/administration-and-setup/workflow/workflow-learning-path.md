---
description: "Aprendizaje desde principiante hasta experto"
---

# Aprendizaje desde principiante hasta experto

Recorra los niveles en orden. Leer no basta: cada nivel termina con una configuración propia, una expectativa verificable y pruebas. P0 evita errores básicos de ejecución; P1 profundiza en datos, decisiones de negocio e integraciones.

1. [Orientación y modelo de ejecución](#level-1)
2. [Primera regla propia](#level-2)
3. [Campos, tipos y límites](#level-3)
4. [Reglas de negocio y aprobaciones](#level-4)
5. [Control Advanced y subworkflows](#level-5)
6. [Cálculo, integración y exportación](#level-6)
7. [Cambios y operación experta](#level-7)

## Requisitos

Use una organización propia de prueba y un documento sintético. Compruebe organización, rol, licencia workflow y autorización Advanced. Mantenga inactivos los ejercicios importados. Los JSON completos son para Advanced Test → Custom Data. Las aprobaciones e integraciones reales necesitan usuarios y destinos de prueba específicos.

## 1. Orientación y modelo de ejecución <a id="level-1"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/es.mp4" %}

[Abrir el vídeo con subtítulos en español y transcripción](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/es.html).

**Ejercicio:** Explique organización, acceso, When–And–Then y la diferencia entre regla lineal y grafo Advanced. Distinga filtro documental, evento, guardado y activación.

**Criterio de finalización:** Puede explicar cuándo se considera la regla y qué prueba diferencia simulación de ejecución documental.

Leer y construir: [¿Cuándo se ejecuta mi workflow?](workflow-execution-model.md) · [P0: Cambiar el estado y limitar nuevas ejecuciones](masterclass/status-and-reentry.md).

## 2. Primera regla propia <a id="level-2"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/es.mp4" %}

[Abrir el vídeo con subtítulos en español y transcripción](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/es.html).

**Ejercicio:** Construya When Invoice → And invoice_id = WF-TRAINING-001 → And total_amount > 1000 → Then wf_training_route = REVIEW. Manténgala inactiva. Pruebe datos completos para 999, 1000 y 1000.01. Esta regla lineal todavía no necesita nodo de control.

**Criterio de finalización:** REVIEW solo se alcanza por encima de 1000. Registre tipo, operador y salida elegida. Trate la entrada ausente por separado.

Leer y construir: [Caso Advanced: enrutamiento de facturas](advanced-workflow-case-study.md) · [Paquete de formación de workflows](workflow-training-kit.md).

## 3. Campos, tipos y límites <a id="level-3"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/es.mp4" %}

[Abrir el vídeo con subtítulos en español y transcripción](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/es.html).

**Ejercicio:** Compruebe ausente, null, texto vacío, espacios, false, 0 y números como texto. Calcule tolerancia con referencia al pedido y al documento. Compare una y todas las líneas realmente asociadas.

**Criterio de finalización:** Explique verdadero, falso y error con valor, tipo, referencia y datos. Ninguna línea comparable no equivale a aprobación correcta.

Leer y construir: [P1: Elegir Field is, Docfield is o Compare two Fields](masterclass/field-conditions.md) · [P1: Definir la referencia de tolerancias y comparación PO](masterclass/tolerances-and-po.md).

## 4. Reglas de negocio y aprobaciones <a id="level-4"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/es.mp4" %}

[Abrir el vídeo con subtítulos en español y transcripción](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/es.html).

**Ejercicio:** Configure dos reglas de importe sin solapamiento en una tabla de decisión. Siga el resultado de usuario guardado hasta la asignación. Planifique A con orden 10 y B con 20, rechazo y alternativa.

**Criterio de finalización:** Distinga responsabilidad, tarea, notificación y aprobación. Acepte un traspaso real a B solo después de una decisión de A procesada.

Leer y construir: [P1: Seguir la tabla de decisión hasta la asignación](masterclass/decision-table-routing.md) · [P1: Diferenciar asignación, tarea y aprobación secuencial](masterclass/assignment-task-sequential.md).

## 5. Control Advanced y subworkflows <a id="level-5"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/es.mp4" %}

[Abrir el vídeo con subtítulos en español y transcripción](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/es.html).

**Ejercicio:** Compare ALL, ANY y OR con dos controles alcanzados. Examine una rama no elegida. Ejecute los siete casos v2 y pruebe Run Workflow con un destino propio inactivo.

**Criterio de finalización:** Explique diferencias test/planificador, conteo de orígenes y errores. V2 completa sin OR bloqueado; compruebe en destino una llamada verde.

Leer y construir: [P0: Conectar Wait ALL, Wait ANY y OR correctamente](masterclass/control-nodes.md) · [P0: Entender Run Workflow, las condiciones y los errores](masterclass/run-workflow.md) · [Caso Advanced: enrutamiento de facturas](advanced-workflow-case-study.md).

## 6. Cálculo, integración y exportación <a id="level-6"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/es.mp4" %}

[Abrir el vídeo con subtítulos en español y transcripción](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/es.html).

**Ejercicio:** Compare la tabla completa antes/después, incluyendo regex sin coincidencia y división por cero. Defina la escritura real de respuestas de integración. Planifique exportación tras aprobación con configuración propia de prueba.

**Criterio de finalización:** Demuestre valores posteriores, recepción y procesamiento ERP por separado. No registre simulación ni solicitud de exportación como entrega.

Leer y construir: [P1: Calcular columnas y comprobar dependencias regex](masterclass/table-calculations.md) · [P1: Comprobar llamadas API y uso posterior de respuestas](masterclass/api-response-contract.md) · [P1: Elegir exportación, tareas abiertas y estado final](masterclass/export-lifecycle.md).

## 7. Cambios y operación experta <a id="level-7"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/es.mp4" %}

[Abrir el vídeo con subtítulos en español y transcripción](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/es.html).

**Ejercicio:** Guarde una exportación del workflow y versiones de tarjetas antes de cambiarlo. Repita positivos, negativos, errores, límites y una segunda ejecución. Relacione el primer fallo con entrada y configuración concretas.

**Criterio de finalización:** Puede aceptar cambios, restaurar la configuración y comparar un nuevo documento con sus efectos. Registre causa, corrección y límites.

Leer y construir: [Diagnosticar problemas de workflow sistemáticamente](workflow-troubleshooting.md) · [Comprender y configurar tarjetas de workflow](card-reference-standard.md).

## Compruebe lo aprendido

| Pregunta | Respuesta |
| --- | --- |
| ¿false está vacío en Field is v2? | Sí; 0 y el texto "false" no lo están. |
| ¿Un OR verde garantiza la ejecución documental? | No. Los predecesores no alcanzados se tratan distinto en test y en el planificador revisado. |
| ¿Run Workflow puede llamar un destino inactivo? | Sí, en la llamada explícita revisada. Compruebe condiciones y resultado del destino. |
| ¿HTTP 200 proporciona automáticamente api.response.cost_center? | No. Las acciones revisadas no ofrecen ese contrato automático de salida JSON. |
| ¿Una prueba verde demuestra recepción de exportación? | No. Ejecución documental, recepción y procesamiento ERP necesitan pruebas propias. |

## Las cinco guías complementarias

Use durante los ejercicios: modelo de ejecución → caso reproducible → paquete → diagnóstico → referencia de tarjetas. Son materiales de los niveles, no cinco tareas adicionales sin comprobar.

1. [¿Cuándo se ejecuta mi workflow?](workflow-execution-model.md)
2. [Caso Advanced: enrutamiento de facturas](advanced-workflow-case-study.md)
3. [Paquete de formación de workflows](workflow-training-kit.md)
4. [Diagnosticar problemas de workflow sistemáticamente](workflow-troubleshooting.md)
5. [Comprender y configurar tarjetas de workflow](card-reference-standard.md)

## Registro de finalización

Use acceptance-record-template.json del paquete. Registre escenario, revisión, expectativa, observación y tipo de prueba. Distinga test Dev, comprobación aislada de código, ejecución documental real, recepción y procesamiento ERP. Deje abiertos explícitamente los pasos no comprobados.
