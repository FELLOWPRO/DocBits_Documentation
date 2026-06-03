# Guías de patrones de flujo de trabajo

**Versión:** 1.0
**Última actualización:** 23 de octubre de 2025

---

## Resumen

Esta sección contiene guías completas de patrones de flujo de trabajo que muestran cómo combinar varias tarjetas de flujo de trabajo para resolver escenarios de negocio habituales. Cada patrón ofrece instrucciones de implementación paso a paso, ejemplos completos y buenas prácticas.

**¿Qué son los patrones de flujo de trabajo?**

Los patrones de flujo de trabajo son soluciones probadas y reutilizables para los retos habituales del procesamiento de documentos. En lugar de empezar desde cero, puede usar estos patrones como plantillas y adaptarlos a sus necesidades.

---

## El Workflow Builder de un vistazo

Todos los patrones de esta página se montan en el **Workflow Builder**. Se accede desde **Workflow Dashboard → Workflow List → Add Workflow** (o abriendo un flujo de trabajo existente). El panel muestra el historial de ejecuciones y las tasas de éxito/fallo de todos sus flujos de trabajo:

<figure><img src="../../../.gitbook/assets/workflow_dashboard.png" alt="Workflow Dashboard con totales de ejecuciones, tasas de éxito y fallo, el gráfico de ejecuciones y la actividad reciente"><figcaption><p>El Workflow Dashboard: totales de ejecuciones, tasas de éxito/fallo y actividad reciente de cada flujo de trabajo.</p></figcaption></figure>

La pestaña **Workflow List** enumera cada flujo de trabajo con su tipo, orden de ejecución y disparador. Use **Add Workflow** para crear uno nuevo, o haga clic en un flujo de trabajo para abrirlo en el editor:

<figure><img src="../../../.gitbook/assets/workflow_list.png" alt="Pestaña Workflow List con los flujos de trabajo por tipo, orden de ejecución y disparador"><figcaption><p>La Workflow List: cada fila es un flujo de trabajo que puede abrir, activar/desactivar o editar.</p></figcaption></figure>

Un flujo de trabajo se compone de tres grupos de tarjetas: **When** (el disparador), **And** (condiciones adicionales) y **Then** (las acciones a ejecutar). El ejemplo siguiente se activa con facturas que pertenecen a una suborganización y las asigna a un usuario:

<figure><img src="../../../.gitbook/assets/workflow_designer_cards.png" alt="Lienzo del Workflow Builder con tarjetas When, And y Then"><figcaption><p>El lienzo del Workflow Builder. Cada patrón de abajo es solo una combinación distinta de tarjetas When / And / Then.</p></figcaption></figure>

Haga clic en **Add Card** en cualquier grupo para abrir la biblioteca de tarjetas. Las tarjetas están organizadas por categoría (Compare with Purchase Order, Partner Cards, Document Field, Date &#x26; Time, Document, Logic, Status, Table, Assignee, …) para que encuentre el bloque que necesita cada patrón:

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Diálogo Add Card con las categorías de tarjetas y las tarjetas disponibles"><figcaption><p>La biblioteca <strong>Add Card</strong>: cada tarjeta mencionada en los patrones de abajo se elige aquí.</p></figcaption></figure>

---

## Patrones disponibles

### 1. [Patrón de integración de API](api-integration-pattern.md)

**Complejidad:** Media | **Tiempo de configuración:** 45-60 minutos

Aprenda a integrar DocBits con API externas para obtener, validar y almacenar datos de sistemas externos.

**Casos de uso:**
- Obtener precios en tiempo real de sistemas externos
- Validar información de proveedores con bases de datos maestras
- Buscar detalles de productos en sistemas de catálogo
- Obtener tipos de cambio de servicios de divisas
- Verificar direcciones con servicios de geocodificación

**Tarjetas utilizadas:** CALL_API, CONDITION_HTTPS_REQUEST_STATUS, ACTION_SET_FIELD_TO_TEXT, CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**[Ver patrón completo →](api-integration-pattern.md)**

---

### 2. [Patrón de gestión de tareas](task-management-pattern.md)

**Complejidad:** Baja-Media | **Tiempo de configuración:** 30-45 minutos

Domine la creación, asignación, seguimiento y gestión de tareas en los flujos de trabajo de DocBits para procesos de aprobación y revisión.

**Casos de uso:**
- Crear flujos de aprobación
- Asignar tareas de revisión a usuarios
- Gestionar excepciones que requieren intervención humana
- Escalar incidencias a responsables
- Crear cadenas de aprobación de varios niveles
- Hacer seguimiento de la finalización y los plazos de las tareas

**Tarjetas utilizadas:** tasks_create, ACTION_ASSIGN_TO_USER, ACTION_SEND_EMAIL_TO_GROUPS, CONDITION_TASK_STATUS

**[Ver patrón completo →](task-management-pattern.md)**

---

### 3. [Patrón de conciliación de pedidos (PO Matching)](po-matching-pattern.md)

**Complejidad:** Media-Alta | **Tiempo de configuración:** 60-90 minutos

Implemente flujos completos de conciliación de pedidos para validar facturas frente a pedidos con enrutamiento basado en tolerancias.

**Casos de uso:**
- Validar facturas frente a pedidos
- Detectar errores de precio antes del pago
- Identificar discrepancias de cantidad
- Aplicar controles de compras
- Evitar pagos duplicados
- Automatizar la conciliación a tres bandas

**Tarjetas utilizadas:** PURCHASE_ORDER_FULL_MATCH, CONDITION_DOC_TO_PO_UNIT_PRICE, CONDITION_DOC_TO_PO_QUANTITY, CONDITION_DOC_TO_PO_TAX_LINES

**[Ver patrón completo →](po-matching-pattern.md)**

---

### 4. [Patrón de lógica de decisión](decision-logic-pattern.md)

**Complejidad:** Media | **Tiempo de configuración:** 30-45 minutos

Implemente árboles de decisión complejos y lógica de enrutamiento condicional para procesar documentos por distintas rutas según reglas de negocio.

**Casos de uso:**
- Enrutar documentos por umbrales de importe
- Aplicar reglas distintas para distintos tipos de documento
- Implementar lógica de aprobación de varios niveles
- Gestionar políticas de negocio complejas
- Crear enrutamiento dinámico basado en varios criterios
- Implementar matrices de aprobación

**Tarjetas utilizadas:** CONDITION_DOC_FIELD_AMOUNT, CONDITION_DOC_TYPE_IS_ISNOT, CONDITION_SUPPLIER_STATUS_IS_ISNOT, ACTION_ASSIGN_TO_USER

**[Ver patrón completo →](decision-logic-pattern.md)**

---

### 5. [Patrón de transformación de datos](data-transformation-pattern.md)

**Complejidad:** Media | **Tiempo de configuración:** 30-45 minutos

Transforme, calcule, formatee y enriquezca los datos de los documentos para prepararlos para la exportación, realizar cálculos y estandarizar formatos.

**Casos de uso:**
- Calcular totales, subtotales e impuestos
- Convertir divisas o unidades
- Formatear fechas, números y texto
- Derivar valores de campos existentes
- Enriquecer datos desde fuentes externas
- Estandarizar formatos de datos
- Validar cálculos

**Tarjetas utilizadas:** ACTION_CALCULATE_FIELD, ACTION_SET_FIELD_TO_TEXT, ACTION_COPY_FIELD_VALUE, CALL_API, CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**[Ver patrón completo →](data-transformation-pattern.md)**

---

## Guía de selección de patrones

### Por complejidad

| Complejidad | Patrones | Ideal para |
|------------|----------|----------|
| **Baja-Media** | [Gestión de tareas](task-management-pattern.md) | Principiantes, flujos sencillos |
| **Media** | [Integración de API](api-integration-pattern.md)<br>[Lógica de decisión](decision-logic-pattern.md)<br>[Transformación de datos](data-transformation-pattern.md) | Usuarios intermedios, flujos estándar |
| **Media-Alta** | [PO Matching](po-matching-pattern.md) | Usuarios avanzados, validación compleja |

---

### Por caso de uso

| Necesito… | Usar este patrón |
|--------------|------------------|
| Integrar con sistemas externos | [Patrón de integración de API](api-integration-pattern.md) |
| Crear flujos de aprobación | [Patrón de gestión de tareas](task-management-pattern.md) |
| Validar frente a pedidos | [Patrón de PO Matching](po-matching-pattern.md) |
| Enrutar según condiciones | [Patrón de lógica de decisión](decision-logic-pattern.md) |
| Calcular y transformar datos | [Patrón de transformación de datos](data-transformation-pattern.md) |

---

### Por sector/departamento

| Sector/Departamento | Patrones recomendados |
|---------------------|---------------------|
| **Finanzas/Contabilidad** | [PO Matching](po-matching-pattern.md), [Gestión de tareas](task-management-pattern.md), [Transformación de datos](data-transformation-pattern.md) |
| **Compras** | [PO Matching](po-matching-pattern.md), [Lógica de decisión](decision-logic-pattern.md), [Integración de API](api-integration-pattern.md) |
| **Operaciones** | [Gestión de tareas](task-management-pattern.md), [Lógica de decisión](decision-logic-pattern.md) |
| **TI/Integración** | [Integración de API](api-integration-pattern.md), [Transformación de datos](data-transformation-pattern.md) |
| **Todos los departamentos** | [Lógica de decisión](decision-logic-pattern.md), [Gestión de tareas](task-management-pattern.md) |

---

## Cómo usar estos patrones

### Paso 1: Elegir un patrón

1. Revise las descripciones de los patrones de arriba
2. Identifique qué patrón se ajusta a su caso de uso
3. Compruebe la complejidad y el tiempo estimado de configuración
4. Lea la sección «Cuándo usarlo» de la guía del patrón

### Paso 2: Revisar los requisitos previos

Cada guía de patrón enumera:
- Conocimientos necesarios
- Guías relacionadas que conviene leer antes
- Tarjetas que se utilizarán
- Requisitos de configuración

### Paso 3: Seguir las instrucciones paso a paso

Cada patrón ofrece:
- Un ejemplo completo de flujo de trabajo
- Una guía de implementación paso a paso
- Plantillas de configuración
- Ejemplos reales
- Consejos para la resolución de problemas

### Paso 4: Adaptar a sus necesidades

- Adapte el ejemplo a sus reglas de negocio
- Ajuste umbrales y tolerancias
- Modifique la lógica de enrutamiento
- Añada o elimine pasos según sea necesario
- Pruebe a fondo antes del uso en producción

### Paso 5: Supervisar y optimizar

- Haga seguimiento del rendimiento del flujo de trabajo
- Supervise las tasas de éxito
- Recopile comentarios de los usuarios
- Afine la configuración
- Documente las personalizaciones

---

## Combinaciones de patrones

Muchos escenarios reales requieren combinar varios patrones:

### Ejemplo 1: Procesamiento completo de facturas

```
1. API Integration Pattern → Fetch current pricing
2. Data Transformation Pattern → Calculate totals
3. PO Matching Pattern → Validate against PO
4. Decision Logic Pattern → Route based on variance
5. Task Management Pattern → Create approval tasks
```

### Ejemplo 2: Aprobación de facturas de alto importe

```
1. Data Transformation Pattern → Calculate amounts
2. Decision Logic Pattern → Check thresholds
3. Task Management Pattern → Multi-level approval
4. API Integration Pattern → Notify external systems
```

### Ejemplo 3: Gestión de excepciones

```
1. PO Matching Pattern → Detect variances
2. Decision Logic Pattern → Classify exception severity
3. Task Management Pattern → Create review tasks
4. Data Transformation Pattern → Calculate impact
```

---

## Plantillas de patrón

Cada patrón incluye estas secciones estandarizadas:

1. **Resumen**: qué hace el patrón
2. **Cuándo usarlo**: casos de uso adecuados
3. **Ejemplo completo**: escenario real
4. **Paso a paso**: instrucciones de implementación
5. **Configuración**: plantillas de configuración de tarjetas
6. **Diagrama de flujo**: representación visual
7. **Variantes avanzadas**: implementaciones alternativas
8. **Gestión de errores**: problemas habituales y soluciones
9. **Lista de pruebas**: pasos de validación
10. **Patrones relacionados**: patrones complementarios
11. **Guías relacionadas**: documentación de referencia

---

## Obtener ayuda

### Recursos de soporte para patrones

**Documentación:**
- [Índice completo de la guía de flujos de trabajo](../README.md)
- [Guías de tarjetas individuales](../then/action/)
- [Referencia de tarjetas de condición](../and/condition-cards-complete-guide.md)

**Contacto:**
- Comentarios sobre patrones: docs@docbits.com
- Soporte técnico: support@docbits.com
- Ayuda con la implementación: consulting@docbits.com

---

## Próximos pasos

**¿Es nuevo en los patrones de flujo de trabajo?**
1. Empiece por el [Patrón de gestión de tareas](task-management-pattern.md): el más fácil de entender
2. Revise el [Patrón de lógica de decisión](decision-logic-pattern.md): fundamental para todos los flujos
3. Explore el [Patrón de integración de API](api-integration-pattern.md): una necesidad de integración habitual

**¿Listo para implementar?**
1. Elija su patrón de la lista de arriba
2. Lea la guía completa del patrón
3. Revise los requisitos previos y las guías relacionadas
4. Siga las instrucciones paso a paso
5. Pruebe con documentos de muestra
6. Despliegue en producción
7. Supervise y optimice

---

**Última actualización:** 23 de octubre de 2025
**Mantenido por:** Equipo de documentación
**Versión:** 1.0
