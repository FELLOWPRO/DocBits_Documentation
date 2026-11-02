---
description: "P1: Elegir exportación, tareas abiertas y estado final"
---

# P1: Elegir exportación, tareas abiertas y estado final

**Start Export** usa la vía de exportación configurada. **Export with Export Configuration** ejecuta una configuración elegida. Su variante diferida la pone en cola para el final de la ejecución actual. Encolar no significa envío automático después de futuras aprobaciones humanas.

Las versiones nuevas revisadas ofrecen `status=finished` o `status=exported`: finished cierra el documento; exported permite seguir editándolo. Start Export ofrece la selección desde v4; exportación configurada y diferida desde v3. Las anteriores usan finished. En las nuevas, una opción ausente también toma finished; un valor inválido es un error de configuración.

Con `ignore_pending_tasks=false`, se comprueban tareas abiertas. El servicio puede rechazar por ello la exportación configurada inmediata. La tarjeta no acredita reanudación automática tras completar tareas más tarde. Defina un nuevo evento y compruebe registros existentes en destino antes de reenviar. Ignorar tareas no sustituye la aprobación.

Conecte exportación solo después de verificar una condición de aprobación explícita. La aceptación incluye tarea abierta, completada, aprobación ausente, recepción en destino de prueba y repetición. Diferencie solicitud, recepción y procesamiento ERP. El paquete no contiene destinos reales y sus pruebas no demuestran entrega.

## Tarjetas y parámetros de ejemplo

Los valores describen parámetros de tarjetas, no un workflow completo importable. Sustituya YOUR_* por selecciones propias de prueba. El diseñador gestiona el ID oculto del llamante. Catálogo: Dev, DocFlow 2.10.38, 21 de octubre de 2026; compruebe versiones y permisos de su organización.

### `export` · v4

Identidad: `757f30ca-ed60-4e04-8131-2779df17f019`

| Parámetro | Tipo / opciones | Ejemplo |
| --- | --- | --- |
| `boolean` | `boolean:bool` | `true` |
| `status` | `finished / exported` | `"finished"` |

### `action_export_with` · v3

Identidad: `ebcd854d-68b3-4b5f-8d45-1bcf8c675b21`

| Parámetro | Tipo / opciones | Ejemplo |
| --- | --- | --- |
| `export_configuration` | `export_configuration:int` | `"YOUR_TEST_EXPORT_CONFIGURATION_ID"` |
| `ignore_pending_tasks` | `ignore_pending_tasks:bool` | `false` |
| `status` | `finished / exported` | `"exported"` |

### `action_export_with_config_deferred` · v3

Identidad: `060ef4c8-625f-447c-83c9-2ca3f680d88d`

| Parámetro | Tipo / opciones | Ejemplo |
| --- | --- | --- |
| `export_configuration` | `export_configuration:int` | `"YOUR_TEST_EXPORT_CONFIGURATION_ID"` |
| `ignore_pending_tasks` | `ignore_pending_tasks:bool` | `false` |
| `status` | `finished / exported` | `"finished"` |

## Casos de prueba de negocio

| Caso | Entrada / configuración | Resultado esperado |
| --- | --- | --- |
| EXPORT-01 | status=finished | cerrado |
| EXPORT-02 | status=exported | editable |
| EXPORT-03 | ignore_pending_tasks=false; pending_tasks>0 | posible rechazo; reanudación automática no demostrada |
| EXPORT-04 | action_export_with_config_deferred | encolado ≠ recibido |
| EXPORT-05 | RUN-1 → RUN-2 | destination_records=1 |

## Pruebas y límites

Parámetros y comportamiento se contrastaron con el catálogo Dev y el código revisado. Los casos de negocio son instrucciones de aceptación. No se realizaron aprobaciones personales, cambios reales ni entregas para este capítulo.

[Continuar aprendiendo](../workflow-learning-path.md) · [Paquete de formación](../workflow-training-kit.md)
