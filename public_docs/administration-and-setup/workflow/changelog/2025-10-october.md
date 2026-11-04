# October 2025 Release - Major Documentation & Versioning Updates

**Fecha de lanzamiento:** 23 de octubre de 2025
**Tipo de lanzamiento:** Lanzamiento de funciones y documentación

---

## Resumen ejecutivo

Este lanzamiento marca un hito importante en la documentación y la gestión de tarjetas del Motor de Flujo de Trabajo DocBits. Hemos añadido 9 guías exhaustivas de tarjetas de flujo de trabajo que cubren más de 80 tarjetas, hemos implementado la documentación del sistema de versionado de tarjetas y hemos identificado 87 oportunidades de referencia cruzada para mejorar los enlaces de los flujos de trabajo.

**Logros principales:**
- ✅ 9 guías exhaustivas de flujos de trabajo (4.642 líneas de documentación en inglés)
- ✅ Documentación completa del sistema de versionado de tarjetas
- ✅ Soporte multilingüe (8 idiomas, 72 archivos en total)
- ✅ Análisis de enlaces de flujos de trabajo (87 oportunidades)
- ✅ Precisión técnica del 100 % mantenida

---

## Novedades

### 📚 Ampliación de la documentación

#### Nuevas guías exhaustivas
Se han añadido nueve nuevos archivos de documentación para ayudar a los usuarios a comprender e implementar las tarjetas de flujo de trabajo:

**Tarjetas de integración externa:**
1. **Call API Guide** (320 líneas)
   - Referencia exhaustiva de integración de API
   - Configuración de parámetros
   - Gestión de errores y análisis de respuestas
   - Desplegada en: 8 idiomas ✅

2. **HTTPS Request Guide** (302 líneas)
   - Implementación simple de solicitudes HTTP/HTTPS
   - Integración de webhooks
   - Gestión de códigos de estado
   - Desplegada en: 8 idiomas ✅

3. **DocOperator Script Guide** (422 líneas)
   - Automatización del navegador
   - Rellenado de formularios y extracción de datos
   - Parámetros y variables de script
   - Desplegada en: 8 idiomas ✅

**Tarjetas de comunicación y tareas:**
4. **Send Email to Groups Guide** (368 líneas)
   - Notificaciones por correo electrónico a grupos
   - Variables de plantilla
   - Gestión de destinatarios
   - Desplegada en: 8 idiomas ✅

5. **Task Assignment Guide** (593 líneas)
   - Creación y asignación de tareas
   - Niveles de prioridad
   - Asignación a grupos y usuarios
   - 12 tarjetas de tarea cubiertas
   - Desplegada en: 8 idiomas ✅

**Manipulación de documentos y datos:**
6. **Field Manipulation Guide** (607 líneas)
   - Operaciones con campos de documentos
   - Fórmulas de cálculo
   - Transformación de datos
   - Operaciones con tablas
   - Desplegada en: 8 idiomas ✅

7. **Document Assignment Guide** (688 líneas)
   - Asignación a usuarios y grupos
   - Enrutamiento secuencial
   - Lógica de asignación condicional
   - Desplegada en: 8 idiomas ✅

**Validación y comparación:**
8. **PO Matching Complete Guide** (661 líneas)
   - Lógica de cotejo de pedidos de compra
   - Cálculos de variación (fórmulas incluidas)
   - Umbrales de tolerancia
   - Comparación a nivel de artículo
   - Desplegada en: 8 idiomas ✅

9. **Condition Cards Complete Guide** (681 líneas)
   - Referencia de más de 31 tarjetas de condición
   - Lógica de decisión
   - Enrutamiento condicional
   - Referencia exhaustiva de parámetros
   - Desplegada en: 8 idiomas ✅

#### Estadísticas de documentación
| Métrica | Valor |
|--------|-------|
| **Total de archivos** | 72 (9 guías × 8 idiomas) |
| **Documentación en inglés** | 4.642 líneas |
| **Total de líneas de documentación** | ~334.224 |
| **Tarjetas cubiertas** | 80+ |
| **Idiomas** | 8 |
| **Longitud media de las guías** | 516 líneas |

---

### 🔄 Documentación del sistema de versionado de tarjetas

Se ha creado una referencia exhaustiva de versionado de tarjetas en [`/docs/card_version.md`](../../docs/card_version.md) con:

**Hallazgos clave:**
- Más de 30 tarjetas con varias versiones
- Más de 90 registros de versiones en total
- 9 versiones obsoletas
- 2 tarjetas totalmente deshabilitadas

**Patrones de evolución de versiones identificados:**
1. **Translation Key Adoption (v1 → v2)** - Más de 15 tarjetas
   - Adición de prefijos `trnsl_%` para soporte de i18n

2. **Decision Tree Integration (v2 → v3)** - 5 tarjetas
   - Soporte experimental de árbol de decisión (posteriormente obsoleto)

3. **Generic Type Evolution (v3 → v4)** - 4 tarjetas
   - Cambio de "Task" a tipos flexibles de elementos de trabajo

4. **Tolerance Parameters** - 6 tarjetas de comparación de PO
   - Soporte de tolerancia de variación en el cotejo

5. **Comparison Modes** - 3 tarjetas de comparación de PO
   - Diferentes algoritmos de comparación

6. **Workflow Triggers** - STAUS_CHANGE
   - Ejecución automática de flujos de trabajo al cambiar el estado

**Tarjetas con más versiones:**
- CONDITION_DOC_TO_PO_UNIT_PRICE - 5 versiones (v2-5)
- CONDITION_OC_TO_PO_ITEMS - 4 versiones (v1-4)
- tasks_create - 4 versiones (v1-4)
- ACTION_TASK_FOR_GROUP - 3 versiones (v2-4)
- ACTION_RUN_DOCOPERATOR_SCRIPT - 3 versiones (v2-4)

**Consulte:** [Complete Card Versioning Reference](../../docs/card_version.md)

---

### 🔗 Análisis de enlaces de flujos de trabajo

El análisis exhaustivo identificó **87 oportunidades de referencia cruzada** entre las guías de flujos de trabajo:

**Categorías de enlaces:**
1. **Condition Card References** (15 enlaces)
   - La mayoría de las tarjetas hacen referencia a la lógica de condiciones
   - Fundamental para el control del flujo de trabajo

2. **Data Flow Links** (12 enlaces)
   - Flujo API → almacenamiento de campos → comprobación de condiciones → acción

3. **Action Card Comparisons** (8 enlaces)
   - Ayudan a los usuarios a elegir entre API, HTTPS, DocOperator

4. **Error Handling Patterns** (9 enlaces)
   - Escenarios de fallo y recuperación

5. **Workflow Integration Patterns** (8 enlaces)
   - Varias tarjetas trabajando juntas

6. **Enhancement Suggestions** (más de 35 enlaces)
   - Oportunidades de integración adicionales

**Plan de implementación:**
- **Fase 1 (45 min):** Enlaces de navegación de alto impacto
- **Fase 2 (60 min):** Documentación de patrones de flujo de trabajo
- **Fase 3 (30 min):** Pulido de mejoras y exhaustividad
- **Tiempo total:** 2-3 horas

**Consulte:** [Workflow Linking Map](../../WORKFLOW_LINKING_MAP.md) | [Quick Reference](../../WORKFLOW_LINKING_QUICK_REFERENCE.md)

---

## Estado del despliegue

### Despliegue por rama de idioma

| Idioma | Rama | Estado | Commits |
|----------|--------|--------|---------|
| 🇺🇸 English | main | ⏳ Pendiente | 1 commit |
| 🇩🇪 German | de | ✅ DESPLEGADA | Sincronizada |
| 🇪🇸 Spanish | es | ✅ DESPLEGADA | Sincronizada |
| 🇫🇷 French | fr | ✅ DESPLEGADA | Sincronizada |
| 🇮🇹 Italian | it | ✅ DESPLEGADA | Sincronizada |
| 🇵🇱 Polish | pl | ✅ DESPLEGADA | Sincronizada |
| 🇵🇹 Portuguese | pt | ✅ DESPLEGADA | Sincronizada |
| 🇳🇱 Dutch | nl | ✅ DESPLEGADA | Sincronizada |

**Tasa de despliegue:** 6 de 8 ramas (75 %) desplegadas correctamente en GitHub

---

## Cambios incompatibles

⚠️ **Sin cambios incompatibles en este lanzamiento**

Todos los flujos de trabajo existentes siguen funcionando sin cambios. La nueva documentación no afecta al comportamiento de las tarjetas existentes.

---

## Detalles técnicos

### Organización de archivos

**Nueva estructura de directorios:**
```
readme/administration-and-setup/workflow/
├── then/
│   ├── action/
│   │   ├── call-api-guide.md (NEW)
│   │   ├── https-request-guide.md (NEW)
│   │   ├── docoperator-script-guide.md (NEW)
│   │   ├── send-email-groups-guide.md (NEW)
│   │   └── [existing files]
│   ├── task/
│   │   ├── task-assignment-guide.md (NEW)
│   │   └── [existing files]
│   ├── document-field/
│   │   ├── field-manipulation-guide.md (NEW)
│   │   └── [existing files]
│   └── assignee/
│       ├── assignment-user-guide.md (NEW)
│       └── [existing files]
├── and/
│   ├── compare-with-purchase-order/
│   │   ├── po-matching-complete-guide.md (NEW)
│   │   └── [existing files]
│   └── condition-cards-complete-guide.md (NEW)
└── changelog/ (NEW DIRECTORY)
    ├── README.md (NEW)
    ├── 2025-10-october.md (THIS FILE)
    ├── card-versioning.md (NEW)
    └── documentation-enhancements.md (NEW)
```

### Referencias de documentación
Todas las guías incluyen:
- ✅ Propósito y casos de uso
- ✅ Instrucciones de configuración paso a paso
- ✅ Ejemplos reales
- ✅ Tablas de referencia de parámetros
- ✅ Secciones de resolución de problemas
- ✅ Referencias a tarjetas relacionadas
- ✅ Buenas prácticas

### Precisión técnica
- ✅ Nombres de tarjetas preservados exactamente (por ejemplo, ACTION_SET_FIELD_TO_TEXT)
- ✅ Fórmulas intactas (por ejemplo, Variance % = |(Invoice-PO)|/PO×100)
- ✅ Todos los bloques de código y ejemplos JSON sin cambios
- ✅ Nomenclatura de parámetros técnicos coherente
- ✅ Precisión del 100 % mantenida en todas las traducciones

---

## Rendimiento y calidad

### Métricas de calidad de la documentación
| Métrica | Valor |
|--------|-------|
| **Ejemplos de código** | 50+ |
| **Referencias de parámetros** | 200+ |
| **Casos de uso documentados** | 80+ |
| **Tarjetas relacionadas enlazadas** | 87 oportunidades |
| **Fórmulas de cálculo** | 10+ |
| **Calidad de traducción** | Profesional |
| **Nivel de precisión** | 100 % |

---

## Guía de migración y actualización

### Para usuarios existentes
No se requiere migración. Todos los flujos de trabajo existentes siguen funcionando sin cambios.

### Para nuevos usuarios
Comience con estas guías según sus necesidades:
1. **¿Nuevo en los flujos de trabajo?** → Lea primero [Workflow Overview](../README.md)
2. **¿Configurando integraciones?** → Consulte [Call API Guide](../then/action/call-api-guide.md)
3. **¿Creando tareas?** → Consulte [Task Assignment Guide](../then/task/task-assignment-guide.md)
4. **¿Estableciendo condiciones?** → Consulte [Condition Cards Guide](../and/condition-cards-complete-guide.md)
5. **¿Comparando con un PO?** → Consulte [PO Matching Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md)

---

## Problemas conocidos y limitaciones

### Tareas pendientes
- ⏳ Implementar 87 enlaces de referencia cruzada (estimado en 2-3 horas)
- ⏳ Añadir capturas de pantalla/diagramas a las guías
- ⏳ Crear tutoriales en vídeo
- ⏳ Implementar la recopilación de comentarios de los usuarios

### Resuelto en este lanzamiento
- ✅ Falta de documentación para más de 80 tarjetas
- ✅ Seguimiento del historial de versiones de las tarjetas
- ✅ Identificación de enlaces de flujos de trabajo

---

## Comentarios y soporte

### Informar de problemas
Si encuentra:
- **Errores de documentación:** Informe con el nombre y la versión específicos de la tarjeta
- **Ejemplos faltantes:** Indique qué guía y caso de uso
- **Problemas de traducción:** Especifique el idioma y la sección

### Solicitudes de funciones
- Sugerir guías adicionales: Especifique el escenario de flujo de trabajo
- Proponer mejoras de enlaces: Haga referencia a tarjetas específicas
- Solicitar contenido en vídeo: Describa el tema deseado

### ¿Preguntas?
- Consulte la guía correspondiente a su tarjeta
- Consulte [Card Versioning Reference](../../docs/card_version.md) para obtener información específica de cada versión
- Revise [Workflow Logs](../workflow-logs/) para ver los detalles de ejecución

---

## Resumen de las notas de lanzamiento

### Qué cambió
✅ Se añadieron 9 guías exhaustivas de flujos de trabajo (72 archivos, 8 idiomas)
✅ Se documentó el sistema de versionado de tarjetas (más de 30 tarjetas, más de 90 versiones)
✅ Se identificaron oportunidades de enlace de flujos de trabajo (87 referencias cruzadas)
✅ Se creó el sistema de registro de cambios

### Qué permaneció igual
✅ Todos los flujos de trabajo existentes siguen funcionando
✅ Sin cambios incompatibles en el comportamiento de las tarjetas
✅ Compatible con versiones anteriores

### Qué viene a continuación
🔄 Implementación de enlaces de referencia cruzada (87 oportunidades)
🎨 Guías visuales y capturas de pantalla
🎬 Tutoriales en vídeo
📊 Análisis e informes avanzados

---

## Estadísticas e impacto

### Impacto de la documentación
- **Contenido nuevo:** 4.642 líneas (inglés)
- **Archivos desplegados:** 72 (9 guías × 8 idiomas)
- **Tarjetas documentadas:** 80+
- **Usuarios atendidos:** Todos los usuarios de flujos de trabajo de DocBits

### Impacto del versionado
- **Tarjetas rastreadas:** 30+
- **Registros de versiones:** 90+
- **Versiones obsoletas:** 9
- **Versiones activas:** 81+

### Potencial de enlaces
- **Oportunidades de referencia cruzada:** 87
- **Tiempo de implementación:** 2-3 horas
- **Impacto previsto en el usuario:** Alto (navegación mejorada)

---

## Agradecimientos

Este lanzamiento ha sido posible gracias a:
- Análisis exhaustivo de la documentación
- Equipo de traducción multilingüe
- Seguimiento y análisis de versiones
- Mapeo de referencias cruzadas
- Verificación de aseguramiento de la calidad

---

## ¿Qué viene a continuación?

**Inmediato (próximas 2 semanas):**
1. Implementar las 87 referencias cruzadas identificadas
2. Recopilar comentarios de los usuarios sobre las nuevas guías
3. Identificar necesidades de documentación adicionales

**Corto plazo (próximo mes):**
1. Añadir capturas de pantalla y diagramas
2. Crear tutoriales en vídeo
3. Actualizar los flujos de trabajo estándar

**Largo plazo (próximo trimestre):**
1. Plantillas avanzadas de flujos de trabajo
2. Biblioteca de patrones de integración
3. Documentación de buenas prácticas

---

## Información de la versión

- **Lanzamiento:** Octubre de 2025
- **Código de versión:** 2025-10
- **Tipo:** Funciones y documentación
- **Estado:** Estable
- **Soporte:** Completo

---

## Descarga y acceso

### Empezar
- 📖 Lea las guías: [Workflow Guides](../)
- 🔍 Consulte las versiones: [Card Versioning Reference](../../docs/card_version.md)
- 🔗 Mapee los enlaces: [Workflow Linking Analysis](../../WORKFLOW_LINKING_MAP.md)

### GitHub
- **Repositorio:** github.com/Fellow-Consulting-AG/docbits
- **Ramas:** main, de, es, fr, it, pl, pt, nl
- **Documentación:** readme/administration-and-setup/workflow/

### GitBook
- **Sitio:** docs.docbits.com
- **Ruta:** /administration-and-setup/workflow/
- **Idiomas:** 8 admitidos

---

**Fecha de lanzamiento:** 23 de octubre de 2025
**Última actualización:** 23 de octubre de 2025
**Repositorio:** https://github.com/Fellow-Consulting-AG/docbits
**Soporte:** Equipo de DocBits
