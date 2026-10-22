---
description: "Distinguir eventos, condiciones, orden de ejecución, pruebas y activación de workflows."
---

# ¿Cuándo se ejecuta mi workflow?

Un workflow necesita un motivo de ejecución y condiciones coincidentes. **El tipo de documento es Factura** selecciona documentos; no significa que cualquier cambio de una factura inicie otra ejecución automáticamente.

## Del evento a la acción

1. Compruebe la organización, los permisos y el módulo Workflow, además de la habilitación Advanced cuando corresponda.
2. Identifique el motivo: procesamiento documental, ejecución manual explícita o un disparador de evento compatible. Utilice únicamente disparadores disponibles en el catálogo de su versión.
3. En Standard Workflow deben cumplirse When y todas las condiciones And. Una condición falsa detiene esa secuencia lineal.
4. En Advanced Workflow, la entrada y las salidas de resultado conectadas determinan la ruta. Una condición And falsa puede continuar por naranja; rojo trata un error de evaluación.
5. Compruebe el resultado donde corresponda: respuesta de prueba, ejecución persistida, documento o sistema receptor.

**Start** es una entrada manual. El paquete utiliza una entrada When para Factura y una limitación al número exacto de formación para cumplir los requisitos de la interfaz actual. Impórtelo desactivado y pruébelo manualmente. Una prueba manual correcta no demuestra la activación automática por eventos del documento.

## Guardar, probar y activar

| Estado | Significado |
| --- | --- |
| Borrador local | La copia del navegador no sustituye el guardado en el servidor. |
| Guardado | La configuración existe. Compruebe la activación por separado: guardar una regla nueva puede activarla. |
| Prueba Advanced | Evalúa el gráfico actual, incluidos cambios sin guardar. Las acciones documentales se simulan. |
| Activado | La regla puede participar en el evento correspondiente. Compruebe ese evento por separado. |

Test Manager y el diálogo de prueba Advanced son superficies de ejecución diferentes. Comparar solo el estado no confirma una asignación, notificación o entrega de exportación. Compruebe los posibles efectos de la superficie elegida antes de usar documentos reales.

## Varios workflows y ejecuciones repetidas

Los valores menores del **orden de ejecución** se procesan primero. Por ejemplo, el workflow 100 prepara un campo y el 200 lo comprueba. Utilice valores distintos y confirme los datos realmente leídos en una ejecución nueva. La posición de una tarjeta Advanced en el lienzo no determina el orden.

**Change Status to → Trigger Workflows** puede iniciar otra ejecución. **Run Workflow** invoca un workflow seleccionado. Ambos necesitan condiciones deliberadas; ninguno garantiza una única ejecución. Limite tareas y exportaciones mediante el estado del proceso y pruebe expresamente una segunda ejecución. Una marca de finalización por sí sola no evita en general duplicados simultáneos.

Continúe con el [caso Advanced](advanced-workflow-case-study.md), el [paquete de formación](workflow-training-kit.md) y la [guía de diagnóstico](workflow-troubleshooting.md).

## WF-01: Ejercicio y aceptación

Registre evento, filtro, activación y versión de tarjeta. Compruebe dos ejecuciones y el orden 100/200 con un campo posterior realmente leído. Distinga solicitud esperada y ejecución observada.

[Ruta de aprendizaje](workflow-learning-path.md)
