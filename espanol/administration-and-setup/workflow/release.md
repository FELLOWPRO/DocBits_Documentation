---
hidden: true
---

# Workflow Card Release & Version History

## Principios de control de versiones

<figure><img src="../../.gitbook/assets/docbits_workflow_version_control.png" alt="Docbits Workflow Version Control"><figcaption>Workflow Version Control System</figcaption></figure>

### Versión 8.5.2024 - Funciones básicas de versionado

El Motor de Flujo de Trabajo DocBits implementa un control de versiones robusto para todas las tarjetas de flujo de trabajo:

1. **Version Control**: Cada tarjeta puede tener varias versiones, cada una de las cuales representa un conjunto diferente de condiciones o acciones. Esto le permite experimentar o ajustar las reglas sin afectar al flujo de trabajo actualmente activo.
2. **Seamless Upgrades**: Cuando necesite actualizar una regla o condición debido a cambios en los requisitos de procesamiento de documentos, puede crear una nueva versión de la tarjeta. Este enfoque garantiza que cualquier modificación sea deliberada y se pruebe antes de reemplazar la versión actual. Minimiza los errores y las posibles interrupciones en el procesamiento de documentos.
3. **Maintaining Consistency**: Mantener la versión original de la tarjeta sin cambios hasta que decida actualizarla garantiza que los procesos en curso no se vean afectados. Puede ejecutar pruebas y validaciones en la nueva versión sin afectar a los datos o flujos de trabajo en producción.
4. **Flexibility and Testing**: Varias versiones permiten probar diferentes escenarios en un entorno controlado. Puede ver los efectos de las nuevas reglas o cambios en su flujo de trabajo de procesamiento de documentos sin realizar cambios permanentes. Una vez que esté satisfecho con los resultados, puede optar por aplicar la nueva versión.

---

## Resumen del versionado de tarjetas

### Estadísticas

| Métrica | Valor |
|--------|-------|
| **Tarjetas con varias versiones** | 30+ |
| **Total de registros de versiones** | 90+ |
| **Versiones activas actuales** | 81+ |
| **Versiones obsoletas** | 9 |
| **Tarjetas totalmente deshabilitadas** | 2 |
| **Última versión (máx.)** | 5 (CONDITION_DOC_TO_PO_UNIT_PRICE) |

### Rango de versiones
- **Mínima:** v1
- **Máxima:** v5
- **Promedio de versiones por tarjeta:** 3

---

## Cambios detallados de versión por tarjeta

### 🔧 ACTION CARDS - Integración y ejecución externas

#### 1. CALL_API
**Versiones:** v1, v2 (Actual: v2)

📖 **Guía:** [Call External API Guide](../then/action/call-api-guide.md)

| Versión | Traducción | Estado | Cambios clave |
|---------|-------------|--------|-------------|
| v1 | No | Activa | Llamada API básica sin claves de traducción |
| v2 | Sí | ✅ Actual | Se añadió `trnsl_%call_api` para soporte multilingüe |

**Qué cambió:** Se añadió soporte de internacionalización (i18n) con claves de traducción. La funcionalidad permanece idéntica.

**Antes (v1):**
```
Call Api: [endpoint] with method: [method], params: [params], data: [data]
```

**Después (v2):**
```
trnsl_%call_api trnsl_be_% Call Api: [endpoint] with method: [method], params: [params], data: [data]
```

**Recomendación:** Use v2 para todos los flujos de trabajo nuevos (incluye soporte de idiomas)
**Compatibilidad con versiones anteriores:** ✅ v1 sigue funcionando

---

#### 2. HTTPS Request (HTTPS_REQUEST)
**Versiones:** v1, v2 (Actual: v2)

| Versión | Traducción | Estado | Cambios clave |
|---------|-------------|--------|-------------|
| v1 | No | Activa | Solicitud HTTP simple |
| v2 | Sí | ✅ Actual | Se añadieron las claves de traducción `trnsl_%send_https_request` |

**Qué cambió:** Se añadió soporte de traducción. La funcionalidad principal de webhook/solicitud no cambió.
**Recomendación:** Use v2 (soporte multilingüe)

---

#### 3. ACTION_RUN_DOCOPERATOR_SCRIPT ⚠️
**Versiones:** v2 (Actual), v3, v4 (Obsoletas y deshabilitadas)

| Versión | Traducción | Estado | Cambios clave |
|---------|-------------|--------|-------------|
| v2 | Sí | Activa | Implementación original de DocOperator |
| v3 | Sí | Activa | Se añadió el parámetro "Execute the prompt" para mayor control |
| v4 | Sí | ❌ OBSOLETA Y DESHABILITADA | Se eliminó el parámetro "Execute" (revertido) |

**Ruta de evolución:** v2 → v3 (parámetro añadido) → v4 (revertido - no recomendada)

**Qué cambió:**
- v2 → v3: Se añadió un parámetro opcional de control de ejecución para mayor flexibilidad
- v3 → v4: Se eliminó el parámetro tras un análisis posterior (obsoleta)

**Recomendación:** Use v3 para flujos de trabajo nuevos (última versión activa con todas las funciones)
**Migración:** Si usa v4, cambie a v3 ⚠️

---

#### 4. ACTION_TASK_FOR_GROUP
**Versiones:** v2, v3 (Obsoleta), v4 (Actual)

📖 **Guía:** [Task Assignment Guide](../then/task/task-assignment-guide.md)

| Versión | Cambios | Estado | Parámetro de tipo |
|---------|---------|--------|-----------------|
| v2 | Implementación original | Activa | "Task" (fijo) |
| v3 | + Soporte de árbol de decisión | ❌ OBSOLETA | "Task" (fijo) |
| v4 | - Árbol de decisión, + Tipo genérico | ✅ Actual | Tipo genérico (flexible) |

**Evolución:** v2 → v3 (experimento con árbol de decisión) → v4 (tipos genéricos, árbol de decisión eliminado)

**Cambio v2 → v3 (experimento con árbol de decisión):**
```
Before: "Create a new Task with the title: [param] ... and assign to group [param]"
After:  "Create a new Task with the title: [param] ... and assign to group [param].
         Use decision tree, if available: [param]"
```

**Cambio v3 → v4 (tipos genéricos + eliminación del árbol de decisión):**
```
Before (v3): "Create a new Task with the title: [param] ... "
After (v4):  "Create a new [param] with the title: [param] ... "
```

**Qué cambió:**
- v2 → v3: Se añadió el parámetro `decision tree, if available: [param]`
- v3 → v4:
  - ❌ Se eliminó el parámetro de árbol de decisión
  - ✅ Se cambió "Task" → `[param]` genérico (admite Task, Ticket, Issue, etc.)
  - Se añadió la clave de traducción `trnsl_%task_for_group_v4`

**Por qué:** El enfoque de árbol de decisión de v3 era experimental. v4 ofrece mayor flexibilidad con tipos genéricos de elementos de trabajo.
**Recomendación:** Use v4 (actual, más flexible)

---

#### 5. ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP
**Versiones:** v2, v3 (Actual)

| Versión | Tipo de tarea | Estado | Diferencia clave |
|---------|-----------|--------|-----------------|
| v2 | "task" (fijo) | Activa | Versión original |
| v3 | Tipo genérico | ✅ Actual | Cambiado a `[param]` flexible |

**Qué cambió:** v2 → v3: "Create a new task" → "Create a new [param]" (admite cualquier tipo de elemento de trabajo)
**Recomendación:** Use v3

---

#### 6. RUN_WORKFLOW
**Versiones:** v1, v2 (Actual)

**Qué cambió:** v1 → v2: Se añadieron las claves de traducción `trnsl_%run_workflow`
**Recomendación:** Use v2

---

### 📊 TARJETAS DE COMPARACIÓN Y VALIDACIÓN DE PO

#### 1. CONDITION_DOC_TO_PO_UNIT_PRICE ⭐ (La más evolucionada - 5 versiones)
**Versiones:** v2, v3, v4, v5 (Actual)

📖 **Guía:** [PO Matching Complete Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md#2-unit-price-comparison-document-vs-po)

| Versión | Cambios | Estado | Tolerancia | Comparación |
|---------|---------|--------|-----------|------------|
| v2 | Comparación de precios básica | Activa | ❌ No | Básica |
| v3 | Igual que v2 | Activa | ❌ No | Básica |
| v4 | + Parámetro de modo de comparación | Activa | ❌ No | ✅ Sí |
| v5 | + Parámetros de tolerancia | ✅ Actual | ✅ Sí (importe + unidad) | ✅ Sí |

**Ruta de evolución:** v2 → v3 (sin cambios) → v4 (modos de comparación) → v5 (umbrales de tolerancia)

**v2 → v3:** Sin cambios funcionales (misma clave de traducción)

**Cambio v3 → v4 (modo de comparación añadido):**
```
Before: "[document] unit price is [operator] to purchase order"
After:  "[document] unit price is [operator] to purchase order. Compare as [mode]"
```

**Cambio v4 → v5 (parámetros de tolerancia añadidos):**
```
Before: "[document] unit price is [operator] to purchase order. Compare as [mode]"
After:  "[document] unit price is [operator] to purchase order, with tolerance of [amount] [unit].
         Compare as [mode]"
```

**Qué cambió:**
- **v2 → v3:** Sin cambios funcionales
- **v3 → v4:** Se añadió `Compare as [param]` - Admite diferentes operadores de comparación
- **v4 → v5:** Se añadieron parámetros de tolerancia:
  - `with tolerance of [amount] [unit]`
  - Ejemplo: "with tolerance of 2 %" o "with tolerance of 100 EUR"
  - Admite: %, EUR, $ y otras monedas

**Casos de uso:**
- v2/v3: Coincidencia estricta (solo precios exactos)
- v4: Diferentes métodos de comparación
- v5: Aceptación flexible de variaciones (por ejemplo, aceptar diferencias de precio del 2 %) ✅ RECOMENDADA

**Recomendación:** Use v5 para flujos de trabajo modernos de comparación de PO

---

#### 2. CONDITION_OC_TO_PO_ITEMS
**Versiones:** v1 (Obsoleta), v2, v3, v4 (Actual)

| Versión | Cambios | Estado | Función de comparación |
|---------|---------|--------|-----------------|
| v1 | Sin traducción, sin método | ❌ OBSOLETA | Básica |
| v2 | + Claves de traducción, + método | Activa | Método básico |
| v3 | Igual que v2 | Activa | Método básico |
| v4 | + Parámetros de modo de comparación | ✅ Actual | ✅ Flexible |

**Qué cambió:**
- **v1 → v2:** Se añadió `trnsl_%in_order_confirmations_matches_purchase_order` + parámetro de método de comparación
- **v2 → v3:** Sin cambios
- **v3 → v4:** Se añadió `Compare as [param1] [param2]` para modos de comparación flexibles

**Recomendación:** Use v4 (evite v1, que es obsoleta)

---

#### 3. CONDITION_DATES_OPERATOR_OC_LINE_ITEMS
**Versiones:** v2, v3 (Actual)

| Versión | Días de tolerancia | Días de tolerancia aceptados | Estado |
|---------|-----------------|------------------------|--------|
| v2 | ❌ No | ❌ No | Activa |
| v3 | ✅ Sí | ✅ Sí | ✅ Actual |

**Qué cambió:** v2 → v3: Se añadieron parámetros de tolerancia:
- `with [param] days as tolerance`
- `and [param] as accepted tolerance days`

**Ejemplo:** Aceptar fechas de entrega dentro de los 5 días de la fecha prometida
**Recomendación:** Use v3

---

#### 4. CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY
**Versiones:** v2, v3, v4 (Actual)

| Versión | Modo de comparación | Estado |
|---------|-----------------|--------|
| v2 | Básico | Activa |
| v3 | Básico (sin cambios) | Activa |
| v4 | ✅ Selección de modo flexible | ✅ Actual |

**Qué cambió:** v3 → v4: Se añadió `compare [param]` para diferentes enfoques de comparación
**Recomendación:** Use v4

---

#### 5. COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE
**Versiones:** v2, v3, v4 (Actual)

| Versión | Modo de comparación | Estado |
|---------|-----------------|--------|
| v2 | Estándar | Activa |
| v3 | Estándar (sin cambios) | Activa |
| v4 | ✅ Flexible | ✅ Actual |

**Qué cambió:** v3 → v4: Se añadió el parámetro `compare [param]`
**Recomendación:** Use v4

---

#### 6. CONDITION_CONFIRMED_DELIVERY_ACCEPTED_DATE_IN_CALENDAR_MASTER_DATA
**Versiones:** v2, v3 (Actual)

| Versión | Tipo de entrega | Tabla de datos maestros | Estado |
|---------|---------------|-------------------|--------|
| v2 | "Confirmed" (fijo) | Referencia fija | Activa |
| v3 | [Parámetro configurable] | [param] dinámico | ✅ Actual |

**Qué cambió:** v2 → v3:
- Se cambió "Confirmed delivery" → `[param] delivery` (tipo de entrega flexible)
- Se cambió la referencia de tabla fija → `stored in [param]` (selección dinámica de tabla)

**Flexibilidad:** v3 permite diferentes tipos de fecha de entrega y tablas de proveedores
**Recomendación:** Use v3

---

#### 7. CONDIITON_UNIT_OF_MEASURE_EQUAL
**Versiones:** v2, v3 (Actual)

| Versión | Referencia de tabla de proveedores | Estado |
|---------|--------------------------|--------|
| v2 | "supplier item price table" (fija) | Activa |
| v3 | [param dinámico] | ✅ Actual |

**Qué cambió:** v2 → v3: Referencia de tabla fija → `stored in [param]` (permite selección dinámica de tabla)
**Recomendación:** Use v3

---

### 👥 TARJETAS DE ASIGNACIÓN Y ENRUTAMIENTO

#### 1. DOC_USER_ASSIGN
**Versiones:** v1, v2, v3 (Obsoleta)

| Versión | Traducción | Árbol de decisión | Estado |
|---------|-------------|---------------|--------|
| v1 | No | ❌ No | Activa |
| v2 | Sí | ❌ No | ✅ Actual |
| v3 | Sí | ✅ Sí | ❌ OBSOLETA |

**Evolución:** v1 (sin i18n) → v2 (con i18n) → v3 (+ experimento con árbol de decisión, ahora obsoleta)

**Qué cambió:**
- v1 → v2: Se añadieron claves de traducción
- v2 → v3: Se añadió soporte de árbol de decisión (experimental, obsoleta)

**Recomendación:** Use v2 (estable con soporte de i18n)

---

#### 2. DOC_GROUP_ASSIGN
**Versiones:** v2, v3 (Obsoleta)

| Versión | Árbol de decisión | Estado |
|---------|---------------|--------|
| v2 | ❌ No | ✅ Actual |
| v3 | ✅ Sí | ❌ OBSOLETA |

**Qué cambió:** v2 → v3: Se añadió `Use decision tree, if available [param]` (posteriormente obsoleta)
**Recomendación:** Use v2

---

#### 3. OC_ASSIGN_DOC
**Versiones:** v1, v2 (Actual)

**Qué cambió:** v1 → v2: Se añadieron las claves de traducción `trnsl_%oc_assign_doc`
**Recomendación:** Use v2

---

### 📋 TARJETAS DE GESTIÓN DE TAREAS

#### 1. tasks_create ⭐ (Tarjeta de tarea más evolucionada - 4 versiones)
**Versiones:** v1 (Obsoleta), v2 (Obsoleta), v3 (Obsoleta), v4 (Actual)

📖 **Guía:** [Task Assignment Guide](../then/task/task-assignment-guide.md#card-tasks_create--create-task-and-assign-to-user)

| Versión | Traducción | Árbol de decisión | Tipo de elemento de trabajo | Estado |
|---------|-------------|---------------|-----------------|--------|
| v1 | No | No | "Task" (fijo) | ❌ OBSOLETA |
| v2 | Sí | No | "Task" (fijo) | ❌ OBSOLETA |
| v3 | Sí | Sí | "Task" (fijo) | ❌ OBSOLETA |
| v4 | Sí | No | [param genérico] | ✅ Actual |

**Cronología de evolución:**
```
v1 (original)
  ↓ (add translation)
v2 (with i18n)
  ↓ (experiment with decision tree)
v3 (+ decision tree, BUT deprecated after this)
  ↓ (remove decision tree, add generic types)
v4 (CURRENT - flexible work items)
```

**Cambio v1 → v2 (claves de traducción añadidas):**
```
Before: "Create a new Task with the title: [param] ... and assign to user [param]"
After:  "trnsl_%tasks_create trnsl_be_% Create a new Task with the title: [param] ... and assign to user [param]"
```

**Cambio v2 → v3 (experimento con árbol de decisión):**
```
Before: "Create a new Task with the title: [param] ... and assign to user [param]"
After:  "Create a new Task with the title: [param] ... and assign it to the user [param].
         Use decision tree, if available: [param]"
```

**Cambio v3 → v4 (tipos genéricos + eliminación del árbol de decisión):**
```
Before: "Create a new Task with the title: [param] ... "
After:  "Create a new [param] with the title: [param] ... "
```

**Qué cambió:**
- **v1 → v2:** Se añadieron las claves de traducción `trnsl_%tasks_create`
- **v2 → v3:**
  - Se añadió soporte de árbol de decisión: `Use decision tree, if available: [param]`
  - Se cambió "assign to user" → "assign it to the user"
- **v3 → v4:**
  - ❌ Se eliminó el parámetro de árbol de decisión
  - ✅ Se cambió "Task" → `[param]` genérico (admite Task, Ticket, Issue, etc.)
  - Se actualizó la clave de traducción a `trnsl_%tasks_create_v4`

**Nota sobre el árbol de decisión:** v3 usaba árboles de decisión para asignar tareas dinámicamente. Este enfoque era experimental y quedó obsoleto en v4 en favor de la selección directa del tipo de elemento de trabajo basada en parámetros.

**Recomendación:** Use v4 exclusivamente para flujos de trabajo nuevos
**Migración:** Si usa v1, v2 o v3, actualice a v4 ✅

---

#### 2. OC_TASK
**Versiones:** v1, v2 (Actual)

**Qué cambió:** v1 → v2: Se añadieron las claves de traducción `trnsl_%oc_task`
**Recomendación:** Use v2

---

#### 3. ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK
**Versiones:** v1, v3 (Actual - v2 omitida)

| Versión | Tipo de elemento de trabajo | Estado |
|---------|-----------------|--------|
| v1 | "Task" (fijo) | Activa |
| v3 | [param genérico] | ✅ Actual |

**Qué cambió:** v1 → v3: Evolución a tipo genérico (v2 se omitió en producción)
**Recomendación:** Use v3

---

#### 4. ACTION_DECISION_TREE_CREATE_TASKS
**Versiones:** v2, v3 (Actual)

| Versión | Texto de asignación | Estado |
|---------|-----------------|--------|
| v2 | "Assign task with title" | Activa |
| v3 | "Assign [generic] with title" | ✅ Actual |

**Qué cambió:** v2 → v3:
- Se cambió "Assign task" → "Assign [generic param]"
- Se cambió "return of decision" → "return of decision table" (terminología más clara)

**Recomendación:** Use v3

---

### 🔄 TARJETAS DE CONTROL DE DOCUMENTOS

#### APPROVE
**Versiones:** v1, v2 (Actual)
**Cambio:** Se añadieron las claves de traducción `trnsl_%approve_doc`
**Recomendación:** Use v2

---

#### REJECT
**Versiones:** v1, v2 (Actual)
**Cambio:** Se añadieron las claves de traducción `trnsl_%reject_doc`
**Recomendación:** Use v2

---

#### STAUS_CHANGE (Status Change)
**Versiones:** v1, v2, v3 (Actual)

| Versión | Disparador de flujo de trabajo | Estado |
|---------|-----------------|--------|
| v1 | ❌ No | Activa |
| v2 | ❌ No | Activa |
| v3 | ✅ Sí | ✅ Actual |

**Qué cambió:** v2 → v3: Se añadió `trigger Workflows [param]` - Activación automática de flujos de trabajo al cambiar el estado
**Recomendación:** Use v3

---

#### EXPORT
**Versiones:** v1, v2, v3 (Actual)

| Versión | Validación | Estado |
|---------|------------|--------|
| v1 | ❌ No | Activa |
| v2 | ❌ No | Activa |
| v3 | ✅ Sí | ✅ Actual |

**Qué cambió:** v2 → v3: Se añadió `Start Export with Validation: [param]`
**Recomendación:** Use v3

---

### 🧮 TARJETAS DE MANIPULACIÓN DE DATOS

#### CALC_COLUMNS, CALC_COLUMNS_REGEX, EDIT_COLUMN, AI_CALC_MTZ_ETZ
**Patrón:** v1 → v2 (claves de traducción añadidas)
**Recomendación:** Use v2 para todas

---

#### CONDITION_DECISION_TREE_DATA
**Versiones:** v2, v3 (Actual)

| Versión | Uso de datos | Estado |
|---------|------------|--------|
| v2 | "Use return data in later cards" | Activa |
| v3 | "[Explicit param] returned data for use in subsequent cards" | ✅ Actual |

**Qué cambió:** v2 → v3: Control más explícito sobre la extracción de datos del árbol de decisión
**Recomendación:** Use v3

---

### ❌ TARJETAS DESHABILITADAS (No usar)

#### DOC_SUBORG_CHANGE
**Versiones:** v1, v2 (ambas deshabilitadas)
**Estado:** Ya no se admite
**Alternativa:** Use las funciones de asignación de documentos

---

#### RUN_SCRIPT
**Versiones:** v2, v3 (ambas deshabilitadas)
**Estado:** Reemplazada por ACTION_RUN_DOCOPERATOR_SCRIPT
**Alternativa:** Use ACTION_RUN_DOCOPERATOR_SCRIPT v3

---

## 🎯 Patrones comunes de versión

### Patrón 1: Adopción de claves de traducción (v1 → v2)
**Afectadas:** 15+ tarjetas

**Cambio:** Se añadieron las claves de traducción `trnsl_%[card_name]`
```
v1: Plain text (no i18n)
v2: trnsl_%[key] trnsl_be_% Plain text (with i18n)
```

**Tarjetas:** CALL_API, RUN_WORKFLOW, APPROVE, REJECT, CALC_COLUMNS, y más
**Impacto:** Habilita el soporte multilingüe

---

### Patrón 2: Integración de árbol de decisión (v2 → v3) - OBSOLETO
**Afectadas:** 5 tarjetas (ACTION_TASK_FOR_GROUP, tasks_create, DOC_USER_ASSIGN, DOC_GROUP_ASSIGN, ACTION_DECISION_TREE_CREATE_TASKS)

**Cambio:** Se añadió un parámetro opcional de árbol de decisión
```
v2: Standard task/assignment logic
v3: + "Use decision tree, if available: [param]"
```

**Estado:** ❌ Mayormente obsoleto (excepto ACTION_DECISION_TREE_CREATE_TASKS)
**Motivo:** Se prefiere el enfoque más simple basado en parámetros directos

---

### Patrón 3: Evolución a tipo genérico (v3 → v4)
**Afectadas:** 4 tarjetas (tasks_create, ACTION_TASK_FOR_GROUP, ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP, ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK)

**Cambio:** "Task" → parámetro de tipo genérico
```
v3: Create a new Task with title: [param]
v4: Create a new [param] with title: [param]
```

**Impacto:** Admite Task, Ticket, Issue y otros tipos de elementos de trabajo
**Beneficio:** Mayor flexibilidad y reutilización

---

### Patrón 4: Parámetros de tolerancia (tarjetas de PO)
**Afectadas:** 6 tarjetas (CONDITION_DOC_TO_PO_UNIT_PRICE, CONDITION_DATES_OPERATOR_OC_LINE_ITEMS, CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY, etc.)

**Cambio:** Se añadió soporte de tolerancia/variación
```
v2: Value [operator] Reference Value
v3+: Value [operator] Reference with tolerance [amount] [unit]
```

**Ejemplos:**
- "with tolerance of 2 %"
- "with tolerance of 100 EUR"
- "with 5 days as tolerance"

**Impacto:** Criterios de coincidencia realistas (no es necesario que todos los valores coincidan exactamente)

---

### Patrón 5: Parámetros de modo de comparación
**Afectadas:** 3 tarjetas (COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE, CONDITION_OC_TO_PO_ITEMS, CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY)

**Cambio:** Se añadió la selección de método de comparación flexible
```
v3: Standard comparison
v4: + "Compare as [param1] [param2]"
```

**Impacto:** Admite diferentes algoritmos de comparación

---

## ✅ Recomendaciones de versión

### Para flujos de trabajo nuevos
**Regla:** Use siempre el número de versión habilitada más alto
- Proporciona las últimas funciones
- Mejor soporte
- Más probada
- Enfoque recomendado

### Para flujos de trabajo existentes
**Enfoque seguro:**
- Continúe usando la versión actual si funciona
- Planifique una migración gradual a versiones más nuevas
- Pruebe primero las actualizaciones en el sandbox

### Prioridad de migración

| Prioridad | Tarjetas | Acción |
|----------|-------|--------|
| **Alta** | tasks_create v1/v2/v3, ACTION_TASK_FOR_GROUP v3, CONDITION_DOC_TO_PO_UNIT_PRICE v2/v3/v4 | Actualizar a la versión actual |
| **Media** | Otras actualizaciones de traducción v1/v2, tarjetas de PO v2/v3 | Considerar la actualización |
| **Baja** | Tarjetas sin cambios funcionales | Opcional |

---

## ⚠️ Versiones obsoletas - No usar

| Tarjeta | Versión | Motivo | Use en su lugar |
|------|---------|--------|-------------|
| tasks_create | v1, v2, v3 | Muy antigua, o árbol de decisión obsoleto | v4 |
| ACTION_TASK_FOR_GROUP | v3 | Enfoque de árbol de decisión obsoleto | v4 |
| DOC_USER_ASSIGN | v3 | Enfoque de árbol de decisión obsoleto | v2 |
| DOC_GROUP_ASSIGN | v3 | Enfoque de árbol de decisión obsoleto | v2 |
| CONDITION_DOC_TYPE_IS_ISNOT | v1 | Muy antigua | v2 |
| CONDITION_OC_TO_PO_ITEMS | v1 | Muy antigua | v4 |
| ACTION_RUN_DOCOPERATOR_SCRIPT | v4 | Funciones revertidas | v3 |

---

## 🔄 Tarjetas totalmente deshabilitadas - No se pueden usar

| Tarjeta | Versiones | Motivo | Alternativa |
|------|----------|--------|-------------|
| DOC_SUBORG_CHANGE | v1, v2 | Ya no se admite | Tarjetas de asignación de documentos |
| RUN_SCRIPT | v2, v3 | Reemplazada por DocOperator | ACTION_RUN_DOCOPERATOR_SCRIPT v3 |

---

## Documentación relacionada

- 📖 [Card Versioning Reference](../changelog/card-versioning.md) - Información detallada de versiones
- 📚 [Workflow Guides](../) - Uso de tarjetas paso a paso
- 🔄 [Card Version Database](../docs/card_version.md) - Historial completo de versiones
- 📋 [Workflow Logs](../workflow-logs/) - Ejecución y depuración

---

**Última actualización:** 23 de octubre de 2025
**Estado:** Historial completo de versiones
**Origen de la base de datos:** postgres-dev-docflow
