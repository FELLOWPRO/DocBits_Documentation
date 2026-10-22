---
description: "P0: Cambiar el estado y limitar nuevas ejecuciones"
---

# P0: Cambiar el estado y limitar nuevas ejecuciones

**Change Status to** actualiza el estado documental. En la versión 3, `trigger_docflow` controla si se solicita más procesamiento de workflows. Defínalo explícitamente. El código usa `true` cuando falta; las versiones 1/2 no leen ese interruptor por la misma ruta de ejecución. Compruebe la versión guardada.

Empiece con `validated_pending_approval` y `trigger_docflow=false`. El estado es una opción técnica: inventar `pending_approval` no es equivalente. Advanced Test simula el cambio. No demuestra ni su persistencia ni el procesamiento de otra ejecución solicitada.

Un proceso limitado comprueba el estado inicial y un marcador de procesamiento, realiza la acción y pasa al siguiente estado. Un evento repetido ya no debe cumplir la condición inicial. Sin embargo, dos ejecuciones concurrentes pueden leer el mismo marcador antiguo: tareas y destinos de exportación necesitan controles adicionales de duplicados.

Para la aceptación, compare la primera y segunda ejecuciones reales: estado, procesamiento solicitado y número de tareas o registros de destino. No alterne entre dos estados solo para experimentar. Cambiar el estado no concede una aprobación cuya condición de negocio sigue sin cumplirse.

## Tarjetas y parámetros de ejemplo

Los valores describen parámetros de tarjetas, no un workflow completo importable. Sustituya YOUR_* por selecciones propias de prueba. El diseñador gestiona el ID oculto del llamante. Catálogo: Dev, DocFlow 2.10.38, 21 de octubre de 2026; compruebe versiones y permisos de su organización.

### `staus_change` · v3

Identidad: `4e0d38a2-a0af-4c1c-b0c2-2f380d70d910`

| Parámetro | Tipo / opciones | Ejemplo |
| --- | --- | --- |
| `trigger_docflow` | `trigger_docflow:bool` | `false` |
| `status` | `error / rejected / ready_for_validation / validated_pending_approval / approved_pending_second_approval / archived / finished / exported` | `"validated_pending_approval"` |

## Casos de prueba de negocio

| Caso | Entrada / configuración | Resultado esperado |
| --- | --- | --- |
| STATUS-01 | v3; trigger_docflow=false | validated_pending_approval; trigger=false |
| STATUS-02 | v3; trigger_docflow=true | ejecución posterior solicitada ≠ completada |
| STATUS-03 | v3; trigger_docflow: — | default=true |
| STATUS-04 | RUN-1 → RUN-2 | tasks=1; destination_records=1 |

## Pruebas y límites

Se comprobaron resultados seleccionados de tarjetas y nodos con datos sintéticos en Advanced Test. Las respuestas están en el paquete. Las acciones documentales son simuladas; no prueban una ejecución persistida ni una entrega externa.

[Continuar aprendiendo](../workflow-learning-path.md) · [Paquete de formación](../workflow-training-kit.md)
