# Card Versioning System - October 2025 Update

**Documento:** Resumen del versionado de tarjetas de flujo de trabajo
**Última actualización:** 23 de octubre de 2025
**Estado:** Completo

---

## Resumen

El Motor de Flujo de Trabajo DocBits utiliza un **versionado basado en enteros** para gestionar la evolución de las tarjetas manteniendo la compatibilidad con versiones anteriores. Este documento ofrece una visión general del sistema de versionado.

---

## ¿Qué es el versionado de tarjetas?

### Concepto
Cada tarjeta de flujo de trabajo puede tener varias versiones, lo que permite al sistema:
- Añadir nuevas funciones sin romper los flujos de trabajo existentes
- Admitir funcionalidad obsoleta mientras se elimina gradualmente
- Hacer evolucionar las capacidades de las tarjetas con el tiempo
- Mantener la compatibilidad con versiones anteriores

### Estructura de versiones
- **Formato:** Valores enteros (1, 2, 3, 4, 5...)
- **Identificación:** Clave compuesta de (card_type, card_version)
- **Estado:** Cada versión tiene indicadores de obsolescencia/habilitación

### Ejemplo
La tarjeta `tasks_create` ha evolucionado a través de 4 versiones:
- **v1:** Creación de tareas original (obsoleta)
- **v2:** Se añadió soporte de traducción (obsoleta)
- **v3:** Soporte experimental de árbol de decisión (obsoleta)
- **v4:** Soporte de tipos genéricos de elementos de trabajo (activa actual)

---

## Estadísticas clave

### Resumen del versionado
| Métrica | Valor |
|--------|-------|
| **Tarjetas con varias versiones** | 30+ |
| **Total de registros de versiones** | 90+ |
| **Versiones por tarjeta (promedio)** | 3 |
| **Máximo de versiones** | 5 (CONDITION_DOC_TO_PO_UNIT_PRICE) |
| **Versiones obsoletas** | 9 |
| **Tarjetas totalmente deshabilitadas** | 2 |

### Distribución de versiones
- **2 versiones:** 14 tarjetas (evolución más simple)
- **3 versiones:** 11 tarjetas (evolución moderada)
- **4 versiones:** 4 tarjetas (evolución significativa)
- **5 versiones:** 1 tarjeta (la más evolucionada: CONDITION_DOC_TO_PO_UNIT_PRICE)

---

## Patrones comunes de versión

### Patrón 1: Adopción de claves de traducción (v1 → v2)

**Afectadas:** Más de 15 tarjetas

**Cambio:**
```
v1: Plain text: "Call Api: [param] with method: [param]"
v2: With i18n: "trnsl_%call_api trnsl_be_% Call Api: [param]..."
```

**Propósito:** Habilitar el soporte multilingüe

**Tarjetas:** CALL_API, RUN_WORKFLOW, APPROVE, REJECT, CALC_COLUMNS, y más

**Migración:** Segura - sin cambios funcionales

---

### Patrón 2: Integración de árbol de decisión (v2 → v3)

**Afectadas:** 5 tarjetas

**Cambio:** Adición del parámetro de árbol de decisión

```
v2: Create a new Task with title: [param], description: [param]...
v3: (same as v2) + "Use decision tree, if available: [param]"
```

**Propósito:** Admitir los resultados de las tablas de decisión

**Tarjetas:**
- tasks_create (v3 obsoleta)
- ACTION_TASK_FOR_GROUP (v3 obsoleta)
- DOC_USER_ASSIGN (v3 obsoleta)
- DOC_GROUP_ASSIGN (v3 obsoleta)
- ACTION_DECISION_TREE_CREATE_TASKS

**Estado:** Obsoleto - el enfoque de árbol de decisión era experimental

---

### Patrón 3: Evolución a tipo genérico (v3 → v4)

**Afectadas:** 4 tarjetas

**Cambio:** "Task" se convierte en un tipo flexible de elemento de trabajo

```
v3: Create a new Task with the title: [param]
v4: Create a new [param] with the title: [param]
```

**Propósito:** Admitir Tasks, Tickets, Issues y otros tipos de elementos de trabajo

**Tarjetas:**
- tasks_create (v4 actual)
- ACTION_TASK_FOR_GROUP (v4 actual)
- ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP (v3 actual)
- ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK (v3 actual)

**Estado actual:** Activa y recomendada

---

### Patrón 4: Parámetros de tolerancia (tarjetas de PO)

**Afectadas:** 6 tarjetas de comparación de PO

**Cambio:** Adición de soporte de tolerancia/variación

```
v2: Document value [operator] Purchase Order value
v3+: Document value [operator] PO value with tolerance [amount] [unit]
```

**Propósito:** Permitir una variación aceptable en el cotejo (por ejemplo, una diferencia de precio del 2 % es aceptable)

**Tarjetas clave:**
- CONDITION_DOC_TO_PO_UNIT_PRICE (evolucionó a v5 con tolerancia)
- CONDITION_DATES_OPERATOR_OC_LINE_ITEMS (v2 → v3)
- CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY

**Beneficio:** Criterios de coincidencia más realistas

---

### Patrón 5: Parámetros de modo de comparación

**Afectadas:** 3 tarjetas de comparación de PO

**Cambio:** Soporte de diferentes algoritmos de comparación

```
v3: Standard comparison logic
v4: Same logic + "Compare as [param]" parameter
```

**Propósito:** Métodos de comparación flexibles

**Tarjetas:**
- COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE (v2-4)
- CONDITION_OC_TO_PO_ITEMS (v3-4)
- CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY (v3-4)

---

### Patrón 6: Disparadores de flujo de trabajo

**Afectadas:** Solo STAUS_CHANGE

**Cambio:** Activación automática de flujos de trabajo al cambiar el estado

```
v2: Change Status to [param]
v3: Change Status to [param], trigger Workflows [param]
```

**Propósito:** Propagar en cascada los cambios de estado entre flujos de trabajo

---

## Tarjetas más evolucionadas

### 1. CONDITION_DOC_TO_PO_UNIT_PRICE (5 versiones)

**Ruta de evolución:** v2 → v3 → v4 → v5

- **v2:** Comparación básica de precio unitario
- **v3:** Misma clave de traducción (v2)
- **v4:** Se añadió el parámetro de modo de comparación
- **v5:** Se añadió el parámetro de umbral de tolerancia

**Actual:** v5 (con soporte de tolerancia)

---

### 2. CONDITION_OC_TO_PO_ITEMS (4 versiones)

**Ruta de evolución:** v1 → v2 → v3 → v4

- **v1:** Coincidencia básica de artículos (obsoleta)
- **v2:** Se añadió el parámetro de método de comparación
- **v3:** Mejorada con claves de traducción
- **v4:** Se añadió el parámetro de modo de comparación

**Actual:** v4

**Evite:** v1 (obsoleta)

---

### 3. tasks_create (4 versiones)

**Ruta de evolución:** v1 → v2 → v3 → v4

- **v1:** Implementación original (obsoleta)
- **v2:** Se añadió soporte de traducción (obsoleta)
- **v3:** Se añadió el árbol de decisión (obsoleta)
- **v4:** Tipos genéricos de elementos de trabajo (actual)

**Actual:** v4 (recomendada)

**Cronología:**
```
v1 → deprecated (old)
  → v2 → deprecated (translation added)
    → v3 → deprecated (decision tree experiment)
      → v4 → CURRENT & ACTIVE
```

---

## Estado de obsolescencia

### Versiones totalmente obsoletas (No usar)

| Tarjeta | Versión | Motivo | Alternativa |
|------|---------|--------|-------------|
| tasks_create | v1 | Muy antigua | Use v4 |
| tasks_create | v3 | Árbol de decisión obsoleto | Use v4 |
| ACTION_TASK_FOR_GROUP | v3 | Árbol de decisión obsoleto | Use v4 |
| DOC_USER_ASSIGN | v3 | Árbol de decisión obsoleto | Use v2 |
| DOC_GROUP_ASSIGN | v3 | Árbol de decisión obsoleto | Use v2 |
| CONDITION_DOC_TYPE_IS_ISNOT | v1 | Muy antigua | Use v2 |
| CONDITION_OC_TO_PO_ITEMS | v1 | Muy antigua | Use v4 |
| ACTION_RUN_DOCOPERATOR_SCRIPT | v4 | Funciones revertidas | Use v3 |

### Tarjetas totalmente deshabilitadas (No se pueden usar)

| Tarjeta | Versiones | Notas |
|------|----------|-------|
| DOC_SUBORG_CHANGE | v1, v2 | Funcionalidad no admitida |
| RUN_SCRIPT | v2, v3 | Reemplazada por ACTION_RUN_DOCOPERATOR_SCRIPT |

---

## Recomendaciones de versión

### Por caso de uso

**Creación de un nuevo flujo de trabajo:**
- Use siempre el **número de versión habilitada más alto**
- Proporciona las últimas funciones y mejoras
- Compatible y documentada

**Mantenimiento de un flujo de trabajo existente:**
- Continúe usando la versión actual si funciona
- Planifique la migración cuando sea factible
- No hay necesidad urgente de actualizar

**Migración de un flujo de trabajo heredado:**
- Identifique la versión actualmente en uso
- Planifique la ruta de actualización
- Pruebe exhaustivamente antes de desplegar

---

## Cómo funcionan las versiones

### Selección de versión
Al crear un flujo de trabajo, usted selecciona qué versión de una tarjeta utilizar. Ejemplo:
- Use `tasks_create v4` para crear nuevas tareas (recomendado)
- Use `tasks_create v2` si los sistemas heredados lo requieren (más antigua pero funciona)
- NO use `tasks_create v1` (obsoleta)

### Compatibilidad con versiones anteriores
- Las versiones más nuevas no rompen los flujos de trabajo más antiguos
- Los flujos de trabajo antiguos siguen funcionando con su versión original
- Puede actualizar los flujos de trabajo gradualmente

### Implementación técnica
Las versiones se gestionan a nivel de base de datos:
```
card_templates table (PostgreSQL)
- card_type: Identifies the card (e.g., "tasks_create")
- card_version: Version number (e.g., 2, 3, 4)
- deprecated: Boolean flag
- enabled: Boolean flag
- text: Card description/parameters
```

---

## A efectos de documentación

### Comprensión de la información de versión
Cuando vea "Card v3" en la documentación:
- Se refiere a la versión 3 de esa tarjeta específica
- Consulte la [Full Versioning Reference](../../docs/card_version.md) para obtener más detalles
- Verifique qué versión se recomienda

### Comprobación de su versión
Para saber qué versión está usando:
1. Abra la tarjeta en su flujo de trabajo
2. Compruebe el número de versión mostrado
3. Compárelo con las recomendaciones de las guías

### Cronología de evolución de las versiones
- **2024-2025:** Evolución continua
- **Octubre de 2025:** Documentación completa del versionado
- **Futuro:** Mejoras continuas

---

## Documentación relacionada

### Referencia exhaustiva
→ [Full Card Versioning Reference](../../docs/card_version.md)

Incluye:
- Las más de 30 tarjetas con sus versiones
- Evolución detallada del texto de cada una
- Cambios específicos de parámetros
- Consultas SQL para la búsqueda de versiones

### Guías específicas de cada tarjeta
→ [Workflow Guides](../)

Documentación de cada tarjeta con recomendaciones de versión

### Detalles del historial de versiones
Cada guía incluye información de versión y notas de migración

---

## Referencia rápida

### Tarjetas con más versiones
1. CONDITION_DOC_TO_PO_UNIT_PRICE - 5 versiones
2. CONDITION_OC_TO_PO_ITEMS - 4 versiones
3. tasks_create - 4 versiones
4. COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE - 3 versiones
5. CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY - 4 versiones

### Patrón de evolución más común
**Adopción de claves de traducción (v1 → v2)** - Más de 15 tarjetas

### Cambio más significativo
**Evolución a tipo genérico (v3 → v4)** - Cambio de "Task" a un tipo flexible de elemento de trabajo

### Totalmente deshabilitadas
- DOC_SUBORG_CHANGE
- RUN_SCRIPT

---

## Preguntas frecuentes

### P: ¿Qué versión debo usar?
R: Use la **versión habilitada más alta** a menos que tenga un motivo específico para usar una versión más antigua.

### P: ¿Puedo actualizar mi flujo de trabajo a una versión más nueva?
R: Sí, pero pruebe exhaustivamente. Algunas versiones tienen requisitos de parámetros diferentes.

### P: ¿Qué ocurre si uso una versión obsoleta?
R: Sigue funcionando, pero no obtendrá nuevas funciones. Se recomienda la migración.

### P: ¿Puedo usar una tarjeta deshabilitada?
R: No, las tarjetas deshabilitadas no se pueden usar. Use la alternativa recomendada en su lugar.

### P: ¿Cómo sé si mi tarjeta necesita actualizarse?
R: Consulte la [Full Versioning Reference](../../docs/card_version.md) para su tipo de tarjeta y siga las recomendaciones.

---

## Buenas prácticas

1. **New Workflows:** Use la última versión estable
2. **Updates:** Compruebe periódicamente si hay nuevas versiones
3. **Testing:** Pruebe primero las actualizaciones de versión en el sandbox
4. **Documentation:** Consulte las guías específicas de cada tarjeta para obtener detalles de versión
5. **Migration:** Planifique las actualizaciones de forma incremental
6. **Support:** Contacte con el soporte si surgen dudas sobre la compatibilidad de versiones

---

## Tabla resumen

| Tipo de tarjeta | Versión actual | Total de versiones | Estado | Notas |
|-----------|-----------------|----------------|--------|-------|
| tasks_create | 4 | 4 | Activa | La más evolucionada; v3 obsoleta |
| CONDITION_DOC_TO_PO_UNIT_PRICE | 5 | 4 | Activa | Mayor número de versiones |
| CONDITION_OC_TO_PO_ITEMS | 4 | 4 | Activa | v1 obsoleta |
| ACTION_TASK_FOR_GROUP | 4 | 3 | Activa | v3 obsoleta |
| ACTION_RUN_DOCOPERATOR_SCRIPT | 3 | 3 | Activa | v4 obsoleta/deshabilitada |
| La mayoría de las tarjetas | 2 | 2 | Activa | Patrón v1 → v2 |

---

## Consulte también

- 📖 [Full Card Versioning Reference](../../docs/card_version.md)
- 🔗 [Workflow Guides](../)
- 📋 [October 2025 Release Notes](./2025-10-october.md)
- 🔄 [Workflow Linking Analysis](../../WORKFLOW_LINKING_MAP.md)

---

**Última actualización:** 23 de octubre de 2025
**Origen:** base de datos postgres-dev-docflow
**Estado:** Referencia completa
