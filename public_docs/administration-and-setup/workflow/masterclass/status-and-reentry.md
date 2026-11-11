---
description: >-
  Use la tarjeta Cambiar estado a de forma que un cambio de estado no vuelva a
  iniciar el mismo Workflow.
---

# Cambiar el estado sin volver a iniciar su Workflow

Cuando un documento recibe un nuevo estado, DocBits inicia los Workflows previstos para ese estado. Entre ellos puede estar el Workflow que acaba de cambiar el estado. Si sus condiciones se siguen cumpliendo, se ejecuta de nuevo y crea una segunda tarea o exportación.

Esta página muestra cómo configurar su Workflow para que cada documento pase por él una sola vez.

## El ajuste decisivo

La tarjeta [Cambiar estado a](../then/status/change-status-to.md) asigna el nuevo estado. Su ajuste **Desencadenar flujos de trabajo** decide si este cambio de estado puede iniciar Workflows:

* **Falso:** no se inicia ningún Workflow. Use este valor, salvo que otro Workflow deba continuar con el documento.
* **Verdadero:** DocBits inicia los Workflows cuyas condiciones coinciden con el documento en su nuevo estado. Entre ellos puede estar el Workflow que hizo el cambio.

La página de la tarjeta describe todos los estados y las versiones de la tarjeta.

## Qué Workflows se inician después de un cambio de estado

Con **Desencadenar flujos de trabajo** en **Verdadero**, DocBits revisa cada Workflow activo y comprueba sus condiciones sobre el tipo de documento y el estado, por ejemplo una tarjeta **El estado del documento**. Un Workflow se inicia si el documento, con su nuevo estado, cumple las condiciones.

Un Workflow que no comprueba el estado coincide con **cualquier** estado. Por eso, cuando cambia el estado él mismo, el nuevo estado lo vuelve a iniciar.

Cambiar un documento al estado que ya tiene no hace nada: el estado se mantiene y no se inicia ningún Workflow.

## Ejemplo: una ejecución o dos

La regla: cuando su Workflow ha hecho su trabajo, sus propias condiciones ya no deben cumplirse.

<figure><img src="../../../.gitbook/assets/status-change-runs-once-vs-twice-es.png" alt="Dos Workflows, ambos con Desencadenar flujos de trabajo en Verdadero. Izquierda: la condición comprueba que el tipo es Factura y el estado es Listo para la validación. Tras el cambio a Aprobación pendiente, la condición ya no se cumple y el Workflow no se vuelve a iniciar; resultado: 1 tarea. Derecha: la condición solo comprueba que el tipo es Factura. El nuevo estado inicia el Workflow por segunda vez; crea una segunda tarea y vuelve a asignar Aprobación pendiente, lo que no cambia nada. Resultado: 2 tareas." width="800"><figcaption><p>El mismo Workflow con y sin condición de estado</p></figcaption></figure>

A la derecha, el Workflow se ejecuta una segunda vez y crea una tarea duplicada. Solo se detiene ahí porque el segundo cambio de estado asigna un estado que el documento ya tiene.

**Dos Workflows pueden iniciarse mutuamente.** Si un Workflow asigna **Aprobación pendiente** y otro devuelve el documento a **Listo para la validación**, ambos con **Verdadero**, se inician el uno al otro una y otra vez. Dé a cada Workflow una condición sobre el estado del que parte y use **Verdadero** solo donde sea necesario.

## Configuración paso a paso

1. **Use la versión 3 de Cambiar estado a.** Las versiones anteriores no tienen el ajuste **Desencadenar flujos de trabajo** (consulte [Versiones de la tarjeta](../then/status/change-status-to.md#versiones-de-la-tarjeta)).
2. **Compruebe el estado de partida.** Añada la tarjeta **Y** **El estado del documento** (en **Y → Estado**) y ajústela a **Es** **Listo para la validación**. Consulte [Condición de estado de documento único](../and/status/single-document-status-condition.md). Si el estado por sí solo no indica si el paso ya está hecho, compruebe también un campo que su Workflow rellene al terminar.
3. **Añada la acción**, por ejemplo crear una tarea o exportar el documento.
4. **Añada Cambiar estado a** y elija el siguiente estado, por ejemplo **Aprobación pendiente**.
5. **Elija el valor de Desencadenar flujos de trabajo.** Empiece con **Falso**. Elija **Verdadero** solo si otro Workflow debe continuar con el nuevo estado.
6. **Pruébelo con un documento real.** Compruebe que se ha creado exactamente una tarea o exportación y que el documento tiene el nuevo estado.

{% hint style="info" %}
Las pruebas en el diseñador de Workflows solo simulan el cambio de estado. El estado no se guarda y no se inicia ningún otro Workflow. Para ver el comportamiento real, use un documento real.
{% endhint %}

## Protección integrada

DocBits limita los daños cuando varios Workflows se inician unos a otros una y otra vez:

* **Una ejecución de Workflow a la vez por documento.** Las ejecuciones para el mismo documento se esperan entre sí, y cada ejecución ve el documento tal como lo dejó la anterior.
* **Límite de ejecuciones.** De forma predeterminada, el mismo Workflow se ejecuta como máximo 50 veces sobre un documento. A partir de ahí, DocBits deja de iniciarlo para ese documento.

Estos límites acaban deteniendo la repetición, pero para entonces ya pueden existir muchas tareas o exportaciones. Lo que la evita es una condición sobre el estado. Si un duplicado supondría un problema real, compruébelo también antes de actuar, por ejemplo si ya existe una tarea abierta para el documento.

## Relacionado

* [Cambiar estado a](../then/status/change-status-to.md): la tarjeta, sus estados y versiones
* [Condición de estado de documento único](../and/status/single-document-status-condition.md): comprobar el estado del documento en una condición
* [¿Cuándo se ejecuta mi workflow?](../workflow-execution-model.md)
* [Resumen de la ruta de aprendizaje](../workflow-learning-path.md)
