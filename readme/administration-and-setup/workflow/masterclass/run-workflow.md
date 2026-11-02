---
description: "P0: Entender Run Workflow, las condiciones y los errores"
---

# P0: Entender Run Workflow, las condiciones y los errores

**Run Workflow** llama a un workflow por ID y espera su ejecución. El nombre no basta. El diseñador gestiona el ID oculto del workflow llamante; no lo cambie como parámetro de negocio. El documento actual pasa al destino, donde se vuelven a evaluar entrada y condiciones.

La llamada explícita revisada también alcanza un destino **inactivo**. Inactivo no significa inaccesible mediante Run Workflow. Las pruebas Dev cubrieron un destino propio inactivo, una llamada a sí mismo y un ID desconocido. Las dos últimas tomaron Error. Los límites incorporados de recursión y cadena no sustituyen las reglas que limitan llamadas repetidas.

Distinga variables de organización y campos documentales de los resultados de una ejecución. La llamada no transfiere automáticamente todos los resultados de tablas de decisión o HTTP del proceso padre. Acuerde los campos necesarios y compruebe su valor real en la tarjeta siguiente.

Una llamada en verde no confirma todas las condiciones del destino: un resultado Advanced sin error técnico se considera llamada correcta y puede incluir `failed_condition`. Examine la ruta elegida y su efecto. Gestione el error expresamente en el llamante; evite A→B→A y llamadas reiteradas al mismo destino.

## Tarjetas y parámetros de ejemplo

Los valores describen parámetros de tarjetas, no un workflow completo importable. Sustituya YOUR_* por selecciones propias de prueba. El diseñador gestiona el ID oculto del llamante. Catálogo: Dev, DocFlow 2.10.38, 21 de octubre de 2026; compruebe versiones y permisos de su organización.

### `run_workflow` · v2

Identidad: `bb773bc7-b258-49b9-b0e9-b1c28ac227cb`

| Parámetro | Tipo / opciones | Ejemplo |
| --- | --- | --- |
| `hidden_workflow_id` | `hidden_workflow_id` | `"MANAGED_BY_DESIGNER"` |
| `workflow` | `workflow:str` | `"YOUR_TARGET_WORKFLOW_ID"` |

## Casos de prueba de negocio

| Caso | Entrada / configuración | Resultado esperado |
| --- | --- | --- |
| CHILD-01 | enabled=false; workflow=VALID_ID | call=success |
| CHILD-02 | caller_id=target_id | error |
| CHILD-03 | workflow=UNKNOWN_ID | error |
| CHILD-04 | Advanced target=failed_condition | la llamada puede tener éxito; compruebe destino |

## Pruebas y límites

Se comprobaron resultados seleccionados de tarjetas y nodos con datos sintéticos en Advanced Test. Las respuestas están en el paquete. Las acciones documentales son simuladas; no prueban una ejecución persistida ni una entrega externa.

[Continuar aprendiendo](../workflow-learning-path.md) · [Paquete de formación](../workflow-training-kit.md)
