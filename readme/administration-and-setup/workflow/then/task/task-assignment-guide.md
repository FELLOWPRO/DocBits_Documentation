# Task Assignment & Creation Cards - Complete Guide

Estas tarjetas van en el grupo **Then** del Generador de flujos de trabajo: las acciones que se ejecutan cuando se cumplen las condiciones When/And:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Las tarjetas se añaden al grupo <strong>Then</strong> mediante <strong>Add Card</strong>.</p></figcaption></figure>

**Cubre:** 12 tarjetas relacionadas con tareas

---

## 📌 Información de versión

**Tarjeta más evolucionada:** tasks_create (4 versiones, v4 la más reciente)
**Otras tarjetas con varias versiones:** ACTION_TASK_FOR_GROUP (v4), ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP (v3), ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK (v3), ACTION_DECISION_TREE_CREATE_TASKS (v3)

**Cambios clave:**
- **Evolución v3 → v4:** Se eliminó el enfoque de árbol de decisión y se añadieron tipos genéricos de elementos de trabajo (Task, Ticket, Issue)
- **Migración v2 → v3:** Se añadió soporte de árbol de decisión (ahora mayormente obsoleto)

📖 [Complete Version History](../../../changelog/release.md#-task-management-cards) | [Card Version Database](../../../../DocFlow/docs/card_version.md)

---

## Resumen

Las tarjetas de tarea crean asignaciones de trabajo para los miembros del equipo. Cuando una factura necesita aprobación, puede crear automáticamente una tarea y asignarla a la persona adecuada.

---

# Creación básica de tareas

## Tarjeta: tasks_create / Create Task and Assign to User

### Propósito
Crea una tarea y la asigna a una persona específica

### Cuándo usar
- La factura necesita la revisión de una persona específica
- Se requiere la aprobación de una persona designada
- Traspaso a un miembro específico del equipo

### Parámetros

**Title**
El nombre/asunto de la tarea
```
Example: "Review Invoice #INV-2025-001 for approval"
```

**Description**
Detalles sobre la tarea
```
Example: "Invoice from Supplier ABC needs review.
Amount: €5000
Deadline: 2025-10-30
Please verify pricing and quality."
```

**Priority**
- 🔴 **High**: Urgente, hacer de inmediato
- 🟡 **Medium**: Prioridad normal
- 🟢 **Low**: Puede hacerse más tarde

**Assigned User**
Quién recibe la tarea
```
Example: John Smith (Finance Manager)
```

**Email Notification**
¿Enviar una alerta por correo electrónico a la persona asignada?
```
✅ Yes: Person gets email
❌ No: Task only in system
```

### Ejemplo
```
Condition: "Invoice amount > €10,000"
    ↓
Create Task:
- Title: "High-Value Invoice Review Required"
- Description: "Invoice #INV-2025-789 for €15,000 needs approval"
- Priority: High
- Assigned to: Sarah Johnson (Finance Approver)
- Send Email: Yes
    ↓
Sarah receives task and email notification
```

---

## Tarjeta: ACTION_TASK_FOR_GROUP / Create Task for Group

### Propósito
Crea una tarea y la asigna a un grupo (todos los miembros pueden verla)

### Cuándo usar
- Varias personas pueden realizar la tarea
- Tarea para un equipo, no para un individuo
- La primera persona disponible debe encargarse

### Diferencia con la tarea individual
```
Individual Task:
- Only John sees it
- John must do it
- Others can't see it

Group Task:
- Everyone in group sees it
- Any group member can claim it
- Distributed workload
```

### Ejemplo de flujo de trabajo
```
Document arrives
    ↓
Condition: "Is supplier new?"
    ↓
Create Task for Procurement Team:
- Title: "Verify New Supplier Details"
- Description: "Please validate supplier information"
- Priority: Medium
- Group: Procurement Team (10 members)
- Notify: Yes
    ↓
All 10 procurement team members see task
First person available takes it
```

---

## Tarjeta: ACTION_DECISION_TREE_CREATE_TASKS

### Propósito
Crea tareas según la lógica de una tabla de decisión

### Cómo funciona
```
Decision Table Returns:
  If invoice from Supplier A → Assign to Procurement
  If invoice from Supplier B → Assign to Quality Team
  If invoice from Supplier C → Assign to Finance

Task is automatically created and assigned
based on which condition is true
```

### Cuándo usar
- Diferentes proveedores necesitan diferentes aprobaciones
- Enrutamiento complejo basado en múltiples factores
- Diferente equipo según el tipo de documento

### Ejemplo
```
Document: Invoice from ABC Corp (Supplier A)
    ↓
Decision Table checks: Which supplier?
    ↓
Result: Supplier A → Procurement Team
    ↓
Create and assign task to Procurement Team
```

---

## Tarjeta: ACTION_DECISION_TREE_TASKS_SEQUENTIAL

### Propósito
Crea tareas de forma secuencial según una tabla de decisión
Las tareas se asignan de una en una con orden de prioridad

### Cuándo usar
- Se necesitan varias aprobaciones en secuencia
- Cadena de aprobación del flujo de trabajo
- Cada persona revisa y luego pasa a la siguiente

### Cómo funciona
```
Step 1: Create Task for Procurement Manager
        (Priority 1)
    ↓
Step 2: Procurement Manager approves
    ↓
Step 3: Create Task for Finance Manager
        (Priority 2)
    ↓
Step 4: Finance Manager approves
    ↓
Step 5: Export
```

### Sistema de prioridades
```
Priority 1 → Assign to: Person A
Priority 2 → Assign to: Person B
Priority 3 → Assign to: Person C

They must complete in order (1→2→3)
```

### Ejemplo de configuración
```
Decision Table Returns:
  Level 1: Sarah Johnson (Finance)
  Level 2: Mike Smith (Manager)
  Level 3: Director (for approval)

Task Flow:
1. Sarah reviews → Comments
2. Passes to Mike → He reviews
3. Passes to Director → Final approval
4. All complete → Export
```

---

## Tarjeta: ACTION_CREATE_TASK_FOR_USER_SEQUENTIAL

### Propósito
Asigna el documento a un usuario Y crea una tarea secuencial

### Cuándo usar
- Asignar el documento Y crear una tarea al mismo tiempo
- El documento debe ser revisado por una persona específica
- Hacer un seguimiento tanto de la asignación como de la creación de la tarea

### Cómo funciona
```
Two things happen:
1. Document is assigned to: Person A
2. Task is created for: Person A

Both in one action
```

### Ejemplo
```
High-value invoice arrives
    ↓
ACTION_CREATE_TASK_FOR_USER_SEQUENTIAL:
- Assign Document to: Finance Manager
- Create Task: "Review & Approve High Value Invoice"
- Priority: High
    ↓
Document AND task both go to Finance Manager
```

---

## Tarjeta: ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL

### Propósito
Asigna el documento a un grupo Y crea una tarea

### Cuándo usar
- El documento necesita la atención de un grupo
- Desea hacer un seguimiento de la creación de la tarea
- Crear una tarea inicial y luego la asignación del documento

### Ejemplo
```
New supplier evaluation
    ↓
ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL:
- Document assigned to: Supplier Management Group
- Create Task: "Evaluate New Supplier Credentials"
- Assign Task to: Same group
- Priority: Medium
    ↓
Group members see document and task
```

---

# Creación avanzada de tareas

## Tarjeta: ACTION_ASSIGN_TASK_TO_FACILITY_GROUP

### Propósito
Crea una tarea para un grupo de instalación específico

### Cuándo usar
- Tarea para el equipo de un almacén/instalación
- Operaciones específicas de instalación
- La ubicación física es importante

### Ejemplo
```
Document: Shipment notification
    ↓
Create Task for Facility Group:
- Group: Berlin Warehouse Team
- Task: "Prepare items for shipment"
- Items: From document
    ↓
Berlin warehouse team gets task
```

---

## Tarjeta: ACTION_ASSIGN_TASK_TO_FACILITY_GROUP_SEQUENTIAL

### Propósito
Asignación secuencial de tareas entre instalaciones

### Cuándo usar
- Operaciones en varias instalaciones
- Las tareas pasan de una instalación a otra
- Procesamiento secuencial por instalación

### Cómo funciona
```
Factory A (Step 1): Production
    ↓
Quality Check (Step 2): Verification
    ↓
Warehouse (Step 3): Packaging
    ↓
Shipping (Step 4): Dispatch
```

### Ejemplo
```
Manufacturing Document
    ↓
Create Sequential Tasks:
- Task 1: Factory A (Manufacturing) - Priority 1
- Task 2: Quality Team (Testing) - Priority 2
- Task 3: Warehouse (Packing) - Priority 3
- Task 4: Shipping (Dispatch) - Priority 4
    ↓
Each team completes → Passes to next
```

---

## Tarjeta: ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP

### Propósito
Crea una tarea para el departamento de compras

### Cuándo usar
- Tarea para el equipo de compras
- Tareas de gestión de proveedores
- Trabajo relacionado con compras

### Ejemplo
```
Supplier status change notification
    ↓
Create Task for Procurement Group:
- Task: "Update supplier records"
- Supplier: ABC Corp
- Action: Change status to 'On Hold'
- Priority: High
    ↓
Procurement team is notified
```

---

## Tarjeta: ACTION_ASSIGN_TASK_PROCUREMENT_GROUP_SEQUENTIAL

### Propósito
Enrutamiento secuencial de tareas dentro del departamento de compras

### Cuándo usar
- Procesos de compras de varios pasos
- Cadena de aprobación en compras
- Ruta de escalamiento

### Ejemplo
```
Purchase Requisition received
    ↓
Step 1: Buyer verifies (Priority 1)
    ↓
Step 2: Approver approves (Priority 2)
    ↓
Step 3: Director signs off (Priority 3)
    ↓
All sign-offs complete → Release to supplier
```

---

## Tarjeta: ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK

### Propósito
Obtiene el usuario de un campo del documento y asigna la tarea
Si no se encuentra el usuario, usa un usuario de respaldo

### Cuándo usar
- El usuario está almacenado en un campo del documento
- El documento especifica quién debe revisarlo
- Tener una persona de respaldo si el usuario especificado no está disponible

### Cómo funciona
```
Document has field: "Approver Name: John Smith"

Card checks: Is John in system?
    If YES → Assign task to John
    If NO → Assign to Fallback User (Sarah)
```

### Ejemplo
```
Invoice field: "Contact: Mike Johnson"

Try to assign task to Mike Johnson
    ↓
If Mike doesn't exist in system:
    ↓
Use Fallback: Team Lead (Robert Brown)
```

### Parámetros
```
- Field to Read: "Approver Name"
- Fallback User: Robert Brown
- Task Details: Title, Description, Priority
```

---

# Parámetros comunes de las tareas

Todas las tarjetas de tarea utilizan estos parámetros:

### Title
```
Good: "Review Invoice #INV-12345 - €5000 - Supplier ABC"
Bad: "Approve something"
```

### Description
```
Should include:
✅ What to do
✅ Deadline
✅ Any special requirements
✅ Who to contact
✅ Link to document
```

### Niveles de prioridad
```
🔴 HIGH
   - Action needed within hours
   - Blocks other processes
   - Example: Supply missing, urgent approval

🟡 MEDIUM
   - Standard processing
   - Normal timeline
   - Example: Regular invoice review

🟢 LOW
   - Can wait days/weeks
   - Non-urgent
   - Example: Archive old documents
```

### Fecha de vencimiento (si está disponible)
```
When should task be completed by?
Example: 2025-10-30 (5 days from now)
```

---

# Escenarios de flujo de trabajo de tareas

## Escenario 1: Aprobación simple
```
Invoice Arrives (€2000)
    ↓
Condition: Amount between €1000-€5000?
    ↓
YES: Create Task for Finance Manager
    ↓
Finance Manager reviews and approves
```

## Escenario 2: Aprobación multinivel
```
Invoice Arrives (€50,000 - High Value)
    ↓
Create Sequential Tasks:
1. Finance Team (Initial review)
2. Finance Manager (Approval)
3. Director (Final sign-off)
    ↓
Each level completes → Next begins
```

## Escenario 3: Tareas en paralelo
```
Invoice Arrives (From New Supplier)
    ↓
Create Task 1: Quality Team (verify supplier)
Create Task 2: Finance Team (check prices)
Create Task 3: Procurement (check contract)
    ↓
All teams work simultaneously
All must complete before proceeding
```

## Escenario 4: Enrutamiento condicional
```
Invoice Arrives
    ↓
Decision Table:
  If amount > €10k → Assign to Director
  If amount €1k-€10k → Assign to Manager
  If amount < €1k → Assign to Team Lead
    ↓
Task created for correct person
```

---

# Buenas prácticas de asignación de tareas

✅ **Haga:**
- Incluya detalles específicos en el título de la tarea
- Establezca niveles de prioridad adecuados
- Establezca plazos realistas
- Notifique a las personas asignadas
- Incluya un enlace al documento
- Use descripciones claras y orientadas a la acción

❌ **No haga:**
- Crear títulos de tarea vagos ("Review this")
- Establecer todo como prioridad High
- Olvidar notificar a la persona asignada
- Crear varias tareas para el mismo trabajo
- Asignar a personas no disponibles

---

# Resolución de problemas de tareas

## "Task not assigned to anyone"
**Causa:** El usuario no existe o el grupo está vacío

**Solución:**
- Verifique la ortografía del nombre del usuario
- Compruebe que el usuario está activo en el sistema
- Verifique que el grupo tiene miembros
- Use un respaldo si es necesario

## "Person says they didn't get notification"
**Causa:** La notificación por correo electrónico está deshabilitada o el correo es incorrecto

**Solución:**
- Compruebe que la casilla "Send Email" está habilitada
- Verifique la dirección de correo electrónico del destinatario
- Compruebe la carpeta de spam
- Reenvíe la notificación manualmente

## "Wrong person got task"
**Causa:** La lógica de enrutamiento es incorrecta

**Solución:**
- Compruebe las condiciones de la tabla de decisión
- Verifique la configuración del respaldo
- Pruebe con un documento de muestra
- Compruebe si hay errores tipográficos en los nombres de usuario

## "Too many tasks created"
**Causa:** La tarjeta se dispara varias veces

**Solución:**
- Compruebe que las condiciones son lo suficientemente específicas
- Verifique que la tarjeta solo se ejecuta una vez por documento
- Revise las condiciones "And"
- Añada filtrado adicional

---

# Tabla comparativa de tarjetas de tarea

| Tarjeta | Crea tarea | Asigna a | Cuándo |
|------|-------------|-----------|------|
| tasks_create | Sí | Individuo | Siempre |
| ACTION_TASK_FOR_GROUP | Sí | Grupo | Siempre |
| ACTION_DECISION_TREE_CREATE_TASKS | Sí | Resultado de tabla de decisión | Condicional |
| ACTION_DECISION_TREE_TASKS_SEQUENTIAL | Sí | Múltiple (secuencial) | Condicional |
| ACTION_CREATE_TASK_FOR_USER_SEQUENTIAL | Sí | Usuario + Documento | Condicional |
| ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL | Sí | Grupo + Documento | Condicional |
| ACTION_ASSIGN_TASK_TO_FACILITY_GROUP | Sí | Grupo de instalación | Condicional |
| ACTION_ASSIGN_TASK_TO_FACILITY_GROUP_SEQUENTIAL | Sí | Varias instalaciones | Condicional |
| ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP | Sí | Equipo de compras | Condicional |
| ACTION_ASSIGN_TASK_PROCUREMENT_GROUP_SEQUENTIAL | Sí | Múltiple (secuencial) | Condicional |
| ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK | Sí | Campo/respaldo | Condicional |

---

# Tarjetas relacionadas

- **ACTION_ASSIGN_DOCUMENT_TO_USER** - Asignar el documento sin crear una tarea
- **ACTION_SEND_EMAIL** - Notificar directamente a las personas
- **STAUS_CHANGE** - Cambiar el estado en lugar de crear una tarea
- **RUN_WORKFLOW** - Activar un flujo de trabajo diferente en su lugar
