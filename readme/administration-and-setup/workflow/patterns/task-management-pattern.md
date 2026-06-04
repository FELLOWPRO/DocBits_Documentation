# Patrón de gestión de tareas

**Tipo de patrón:** Gestión de flujos de trabajo
**Complejidad:** Baja-Media
**Configuración estimada:** 30-45 minutos
**Casos de uso habituales:** Flujos de aprobación, tareas de revisión, gestión de excepciones, escalado

---

Este patrón se monta en el **Workflow Builder** (Workflow Dashboard → Workflow List → Add Workflow). Haga clic en **Add Card** para abrir la biblioteca de tarjetas y elija las tarjetas que usa este patrón: `tasks_create`, `ACTION_ASSIGN_TO_USER`, `ACTION_SEND_EMAIL_TO_GROUPS` y `CONDITION_TASK_STATUS` (la categoría **Assignee** contiene las tarjetas de tarea y asignación):

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Biblioteca Add Card del Workflow Builder, agrupada por categoría"><figcaption><p>La biblioteca <strong>Add Card</strong>: las tarjetas de tarea, asignación y notificación se encuentran en las categorías <strong>Assignee</strong> y <strong>Status</strong>.</p></figcaption></figure>

---

## Resumen del patrón

Este patrón muestra cómo crear, asignar, seguir y gestionar tareas dentro de los flujos de trabajo de DocBits. Las tareas son elementos de trabajo accionables asignados a usuarios o grupos que deben completarse antes de que el flujo de trabajo del documento pueda continuar.

**Qué hace este patrón:**
1. Crea tareas según las condiciones del flujo de trabajo
2. Asigna tareas a los usuarios o grupos adecuados
3. Establece las propiedades de la tarea (prioridad, fecha límite, descripción)
4. Envía notificaciones cuando se crean tareas
5. Hace seguimiento del estado y la finalización de las tareas
6. Enruta los documentos según los resultados de las tareas

---

## Cuándo usar este patrón

Use este patrón cuando necesite:
- ✅ Crear flujos de aprobación
- ✅ Asignar tareas de revisión a usuarios
- ✅ Gestionar excepciones que requieren intervención humana
- ✅ Escalar incidencias a los responsables
- ✅ Crear cadenas de aprobación multinivel
- ✅ Hacer seguimiento de quién debe hacer qué
- ✅ Establecer fechas límite para las acciones

**No use este patrón cuando:**
- ❌ No se requiera acción humana (use el procesamiento automático en su lugar)
- ❌ Solo necesite notificar (use el correo electrónico en su lugar)
- ❌ Se trate de un simple enrutamiento de documentos (use la asignación en su lugar)

---

## Ejemplo de flujo de trabajo completo

### Escenario: Aprobación de facturas con enrutamiento basado en el importe

**Requisito de negocio:**
- Facturas < 1.000 €: Aprobación automática (no se necesita tarea)
- Facturas de 1.000 €-10.000 €: Tarea de aprobación para el Manager
- Facturas > 10.000 €: Doble aprobación (Manager + Director)
- Todos los aprobadores reciben una notificación por correo electrónico
- Las tareas tienen una fecha límite de 3 días

**Tarjetas de flujo de trabajo utilizadas:**
1. CONDITION_DOC_FIELD_AMOUNT - Comprueba el importe de la factura
2. tasks_create - Crea la tarea de aprobación
3. ACTION_ASSIGN_TO_USER - Asigna la tarea al aprobador
4. ACTION_SEND_EMAIL_TO_GROUPS - Envía la notificación
5. CONDITION_TASK_STATUS - Comprueba si la tarea se ha completado
6. ACTION_APPROVE_DOCUMENT - Aprueba tras la finalización de la tarea

---

## Implementación paso a paso

### Paso 1: Comprobar el umbral del importe

**Tarjeta:** CONDITION_DOC_FIELD_AMOUNT o una condición de campo similar

**Configuración para la ruta 1 (< 1.000 €):**
```
Field: Total_Amount
Operator: IS LESS THAN
Value: 1000
Currency: EUR
```

**Configuración para la ruta 2 (1.000 €-10.000 €):**
```
Field: Total_Amount
Operator: IS BETWEEN
Value Min: 1000
Value Max: 10000
Currency: EUR
```

**Configuración para la ruta 3 (> 10.000 €):**
```
Field: Total_Amount
Operator: IS GREATER THAN
Value: 10000
Currency: EUR
```

**Referencia de guía:** [Guía de tarjetas de condición](../and/condition-cards-complete-guide.md)

---

### Paso 2A: Aprobar automáticamente las facturas pequeñas (< 1.000 €)

**No se necesita ninguna tarea para importes pequeños**

**Tarjetas:**
- ACTION_SET_FIELD_TO_TEXT
  - Establecer "Approval_Type" = "AUTO"
  - Establecer "Approval_Reason" = "Amount below threshold"
- ACTION_APPROVE_DOCUMENT

**Resultado:** Documento aprobado automáticamente, no se crea ninguna tarea

---

### Paso 2B: Crear la tarea de aprobación del Manager (1.000 €-10.000 €)

**Tarjeta:** tasks_create (se recomienda la v4)

**Configuración:**
```json
{
  "task_type": "Approval",
  "task_title": "Approve Invoice {{DOCUMENT_NUMBER}} - €{{Total_Amount}}",
  "task_description": "Please approve invoice from {{Supplier_Name}}\n\nAmount: €{{Total_Amount}}\nInvoice Number: {{Invoice_Number}}\nInvoice Date: {{Invoice_Date}}\n\nReview and approve within 3 business days.",
  "priority": "Medium",
  "deadline_days": 3,
  "assign_to": "{{DOCUMENT_FIELD:Approving_Manager}}",
  "task_category": "Invoice Approval",
  "required_action": "Approve or Reject"
}
```

**Asignación de campos:**
- `{{DOCUMENT_NUMBER}}` - ID de documento automático
- `{{Total_Amount}}` - Campo: Total_Amount
- `{{Supplier_Name}}` - Campo: Supplier_Name
- `{{Invoice_Number}}` - Campo: Invoice_Number
- `{{Invoice_Date}}` - Campo: Invoice_Date
- `{{Approving_Manager}}` - Campo o usuario fijo

**Referencia de guía:** [Guía de asignación de tareas](../then/task/task-assignment-guide.md)

---

### Paso 2C: Crear tareas de doble aprobación (> 10.000 €)

**Dos tareas secuenciales para facturas de alto valor**

**Tarea 1: Aprobación del Manager**
```json
{
  "task_type": "First Approval",
  "task_title": "URGENT: Approve High-Value Invoice {{DOCUMENT_NUMBER}} - €{{Total_Amount}}",
  "task_description": "HIGH VALUE INVOICE REQUIRES APPROVAL\n\nSupplier: {{Supplier_Name}}\nAmount: €{{Total_Amount}}\n\nThis invoice exceeds €10,000 and requires dual approval.\nYour approval is required before Director review.",
  "priority": "High",
  "deadline_days": 2,
  "assign_to": "Finance_Manager",
  "task_category": "High-Value Approval",
  "next_task": "Director_Approval"
}
```

**Tarea 2: Aprobación del Director (creada tras finalizar la Tarea 1)**
```json
{
  "task_type": "Second Approval",
  "task_title": "Final Approval: Invoice {{DOCUMENT_NUMBER}} - €{{Total_Amount}}",
  "task_description": "FINAL APPROVAL REQUIRED\n\nSupplier: {{Supplier_Name}}\nAmount: €{{Total_Amount}}\n\nFirst approval: Completed by {{Task1_Approver}} on {{Task1_Date}}\n\nYour final approval required.",
  "priority": "High",
  "deadline_days": 1,
  "assign_to": "Finance_Director",
  "task_category": "Final Approval",
  "prerequisite_task": "Manager_Approval"
}
```

---

### Paso 3: Asignar la tarea a un usuario/grupo

**Tarjeta:** ACTION_ASSIGN_TO_USER o ACTION_ASSIGN_TO_GROUP

**Opción 1: Asignar a un usuario específico**
```
User: John.Smith@company.com
OR
User Field: {{DOCUMENT_FIELD:Approving_Manager}}
```

**Opción 2: Asignar a un grupo**
```
Group: Finance Managers
Assignment Mode: First Available
OR
Assignment Mode: Round Robin
OR
Assignment Mode: All (everyone in group gets task)
```

**Opción 3: Asignación secuencial**
```
Card: ACTION_ASSIGN_SEQUENTIALLY_TO_USER

User 1: Finance_Manager
User 2: Finance_Director (only if User 1 approves)
User 3: CFO (only if User 2 approves)
```

**Referencia de guía:** [Guía de asignación a usuario](../then/assignee/assignment-user-guide.md)

---

### Paso 4: Enviar la notificación por correo electrónico

**Tarjeta:** ACTION_SEND_EMAIL_TO_GROUPS

**Configuración:**
```json
{
  "recipients": [
    "{{TASK_ASSIGNEE_EMAIL}}",
    "finance-notifications@company.com"
  ],
  "subject": "New Task Assigned: Approve Invoice {{DOCUMENT_NUMBER}}",
  "body": "Dear {{TASK_ASSIGNEE_NAME}},\n\nA new approval task has been assigned to you:\n\nTask: Approve Invoice {{DOCUMENT_NUMBER}}\nSupplier: {{Supplier_Name}}\nAmount: €{{Total_Amount}}\nDeadline: {{TASK_DEADLINE}}\nPriority: {{TASK_PRIORITY}}\n\nPlease log in to DocBits to review and approve:\n{{DOCUMENT_LINK}}\n\nBest regards,\nDocBits Automation"
}
```

**Variables de correo electrónico:**
- `{{TASK_ASSIGNEE_EMAIL}}` - Correo electrónico del responsable de la tarea
- `{{TASK_ASSIGNEE_NAME}}` - Nombre del responsable de la tarea
- `{{DOCUMENT_NUMBER}}` - ID de documento
- `{{TASK_DEADLINE}}` - Fecha de vencimiento de la tarea
- `{{TASK_PRIORITY}}` - Nivel de prioridad de la tarea
- `{{DOCUMENT_LINK}}` - Enlace directo al documento

**Referencia de guía:** [Guía de envío de correo a grupos](../then/action/send-email-groups-guide.md)

---

### Paso 5: Hacer seguimiento del estado de la tarea

**Tarjeta:** CONDITION_TASK_STATUS o un comprobador de estado de tarea similar

**Configuración:**
```
Task ID: {{CREATED_TASK_ID}}
Status Check: IS COMPLETED
```

**Opciones de estado:**
- CREATED - Tarea recién creada
- ASSIGNED - Tarea asignada a un usuario
- IN_PROGRESS - El usuario ha empezado a trabajar en la tarea
- COMPLETED - Tarea finalizada
- APPROVED - Tarea aprobada
- REJECTED - Tarea rechazada
- CANCELLED - Tarea cancelada
- OVERDUE - Tarea vencida

**Lógica:**
```
IF TASK_STATUS = COMPLETED AND TASK_RESULT = APPROVED:
  → Continue to next step (or next approval level)
  → Update document status
  → Log approval

IF TASK_STATUS = COMPLETED AND TASK_RESULT = REJECTED:
  → Stop workflow
  → Send rejection notification
  → Create review task for corrections

IF TASK_STATUS = OVERDUE:
  → Escalate to manager
  → Send reminder email
  → Create escalation task
```

---

### Paso 6: Completar el flujo de trabajo según el resultado de la tarea

**Tras finalizar la tarea:**

**Escenario A: Tarea aprobada**
```
1. Set field "Approval_Status" = "APPROVED"
2. Set field "Approved_By" = {{TASK_COMPLETED_BY}}
3. Set field "Approval_Date" = {{TASK_COMPLETED_DATE}}
4. ACTION_APPROVE_DOCUMENT
5. Export document (if configured)
```

**Escenario B: Tarea rechazada**
```
1. Set field "Approval_Status" = "REJECTED"
2. Set field "Rejected_By" = {{TASK_COMPLETED_BY}}
3. Set field "Rejection_Reason" = {{TASK_REJECTION_REASON}}
4. ACTION_REJECT_DOCUMENT
5. Send rejection notification to supplier
6. Create "Correction Needed" task
```

**Escenario C: Tarea vencida**
```
1. Set field "Task_Status" = "OVERDUE"
2. Create escalation task for manager
3. Send reminder email to original assignee
4. Send escalation email to manager
5. Log overdue event
```

---

## Diagrama del flujo de trabajo completo

```
INVOICE ARRIVES
│
├─ CHECK AMOUNT
│  │
│  ├─ Amount < €1,000 ✅
│  │  │
│  │  ├─ Set Approval_Type = "AUTO"
│  │  └─ Auto-Approve Document
│  │     → END (Approved)
│  │
│  ├─ Amount €1,000-€10,000 ⚠️
│  │  │
│  │  ├─ CREATE TASK: Manager Approval
│  │  │  - Title: "Approve Invoice"
│  │  │  - Priority: Medium
│  │  │  - Deadline: 3 days
│  │  │  │
│  │  │  ├─ ASSIGN TO: Finance Manager
│  │  │  │
│  │  │  ├─ SEND EMAIL: Notification
│  │  │  │
│  │  │  ├─ WAIT FOR TASK COMPLETION
│  │  │  │  │
│  │  │  │  ├─ TASK APPROVED ✅
│  │  │  │  │  │
│  │  │  │  │  ├─ Set Approval_Status = "APPROVED"
│  │  │  │  │  └─ Approve Document
│  │  │  │  │     → END (Approved)
│  │  │  │  │
│  │  │  │  ├─ TASK REJECTED ❌
│  │  │  │  │  │
│  │  │  │  │  ├─ Set Approval_Status = "REJECTED"
│  │  │  │  │  ├─ Reject Document
│  │  │  │  │  └─ Create Correction Task
│  │  │  │  │     → END (Rejected)
│  │  │  │  │
│  │  │  │  └─ TASK OVERDUE ⏰
│  │  │  │     │
│  │  │  │     ├─ Send Reminder Email
│  │  │  │     ├─ Escalate to Director
│  │  │  │     └─ Create Escalation Task
│  │  │  │        → WAIT (Escalated)
│  │  │  │
│  │  │  └─ [Task tracking active]
│  │  │
│  │  └─ [Manager approval path]
│  │
│  └─ Amount > €10,000 🚨
│     │
│     ├─ CREATE TASK 1: Manager First Approval
│     │  - Title: "URGENT: First Approval"
│     │  - Priority: High
│     │  - Deadline: 2 days
│     │  │
│     │  ├─ ASSIGN TO: Finance Manager
│     │  ├─ SEND EMAIL: High Priority Notification
│     │  │
│     │  ├─ WAIT FOR TASK 1 COMPLETION
│     │  │  │
│     │  │  ├─ TASK 1 APPROVED ✅
│     │  │  │  │
│     │  │  │  ├─ CREATE TASK 2: Director Final Approval
│     │  │  │  │  - Title: "Final Approval Required"
│     │  │  │  │  - Priority: High
│     │  │  │  │  - Deadline: 1 day
│     │  │  │  │  │
│     │  │  │  │  ├─ ASSIGN TO: Finance Director
│     │  │  │  │  ├─ SEND EMAIL: Final Approval Notification
│     │  │  │  │  │
│     │  │  │  │  ├─ WAIT FOR TASK 2 COMPLETION
│     │  │  │  │  │  │
│     │  │  │  │  │  ├─ TASK 2 APPROVED ✅
│     │  │  │  │  │  │  │
│     │  │  │  │  │  │  ├─ Set Dual_Approval = "COMPLETE"
│     │  │  │  │  │  │  └─ Approve Document
│     │  │  │  │  │  │     → END (Dual Approved)
│     │  │  │  │  │  │
│     │  │  │  │  │  └─ TASK 2 REJECTED ❌
│     │  │  │  │  │     │
│     │  │  │  │  │     ├─ Reject Document
│     │  │  │  │  │     └─ Notify All Parties
│     │  │  │  │  │        → END (Final Rejected)
│     │  │  │  │  │
│     │  │  │  │  └─ [Task 2 tracking]
│     │  │  │  │
│     │  │  │  └─ [Task 2 created]
│     │  │  │
│     │  │  └─ TASK 1 REJECTED ❌
│     │  │     │
│     │  │     ├─ Reject Document (No Task 2 created)
│     │  │     └─ Notify Supplier
│     │  │        → END (First Rejected)
│     │  │
│     │  └─ [Task 1 tracking]
│     │
│     └─ [Dual approval path]
│
└─ [Amount check complete]
```

---

## Plantillas de configuración

### Plantilla 1: Tarea de aprobación simple

```json
{
  "card": "tasks_create",
  "task_title": "Approve {{DOCUMENT_TYPE}} {{DOCUMENT_NUMBER}}",
  "task_description": "Please review and approve this document.",
  "priority": "Medium",
  "deadline_days": 3,
  "assign_to": "approver@company.com",
  "category": "Approval"
}
```

---

### Plantilla 2: Tarea de revisión con detalles

```json
{
  "card": "tasks_create",
  "task_title": "Review Exception: {{EXCEPTION_TYPE}}",
  "task_description": "Document: {{DOCUMENT_NUMBER}}\nException: {{EXCEPTION_REASON}}\n\nDetails:\n- Supplier: {{Supplier_Name}}\n- Amount: €{{Total_Amount}}\n- Date: {{Document_Date}}\n\nAction Required: Review and resolve exception",
  "priority": "High",
  "deadline_days": 1,
  "assign_to_group": "Exceptions Team",
  "category": "Exception Handling"
}
```

---

### Plantilla 3: Tarea de escalado

```json
{
  "card": "tasks_create",
  "task_title": "ESCALATION: {{ORIGINAL_TASK_TITLE}}",
  "task_description": "ESCALATED TASK\n\nOriginal Task: {{ORIGINAL_TASK_ID}}\nOriginal Assignee: {{ORIGINAL_ASSIGNEE}}\nDeadline Passed: {{ORIGINAL_DEADLINE}}\nDays Overdue: {{DAYS_OVERDUE}}\n\nPlease review and take immediate action.",
  "priority": "Urgent",
  "deadline_days": 1,
  "assign_to": "manager@company.com",
  "category": "Escalation",
  "parent_task": "{{ORIGINAL_TASK_ID}}"
}
```

---

## Patrones avanzados

### Patrón 1: Aprobación secuencial multinivel

**Uso:** Las facturas deben pasar por varios aprobadores en secuencia

```
Level 1: Accounts Clerk (verify data)
  → IF APPROVED:
    Level 2: Accounts Manager (approve amount)
      → IF APPROVED:
        Level 3: Finance Director (final sign-off)
          → IF APPROVED:
            Document Approved ✅
```

**Implementación:**
```
1. Create Task 1 for Clerk
2. Wait for Task 1 completion
3. IF Task 1 = APPROVED:
     Create Task 2 for Manager
4. Wait for Task 2 completion
5. IF Task 2 = APPROVED:
     Create Task 3 for Director
6. Wait for Task 3 completion
7. IF Task 3 = APPROVED:
     Approve Document
```

---

### Patrón 2: Aprobación paralela con varios aprobadores

**Uso:** Varias personas deben aprobar de forma simultánea

```
Send to ALL approvers at once:
- Finance Manager
- Procurement Manager
- Quality Manager

Document approved only when ALL approve
```

**Implementación:**
```
1. Create 3 tasks simultaneously
2. Track all 3 task statuses
3. WAIT until ALL tasks completed
4. IF ALL = APPROVED:
     Approve Document
   ELSE:
     Reject Document
```

---

### Patrón 3: Creación condicional de tareas

**Uso:** Crear distintas tareas según las condiciones

```
IF Supplier = "New":
  → Create "New Supplier Review" task
ELSE IF Amount > €50,000:
  → Create "High Value Approval" task
ELSE IF Document has errors:
  → Create "Error Correction" task
ELSE:
  → Create "Standard Approval" task
```

---

### Patrón 4: Escalado basado en fechas límite

**Uso:** Escalar automáticamente si la tarea no se completa a tiempo

```
Day 0: Create task for User A (3-day deadline)
Day 3: IF not completed:
         → Send reminder to User A
Day 4: IF still not completed:
         → Create escalation task for Manager B
         → Notify both User A and Manager B
Day 5: IF still not completed:
         → Create urgent task for Director C
         → High priority notification
```

---

## Gestión de errores

### Escenario 1: No se encuentra el responsable

**Problema:** El usuario no existe o está inactivo

**Solución:**
```
1. Check user status with CONDITION_USER_IS_ISNOT
2. IF User = INACTIVE:
     → Assign to backup user
     → OR Assign to user's group
     → Log warning
3. Send notification to admin
```

---

### Escenario 2: Error al crear la tarea

**Problema:** Error del sistema al crear la tarea

**Solución:**
```
1. Check task creation status
2. IF Failed:
     → Retry task creation
     → Send email notification instead
     → Create admin alert task
     → Log error details
```

---

### Escenario 3: Sin respuesta a la tarea

**Problema:** El usuario no completa la tarea antes de la fecha límite

**Solución:**
```
1. Monitor task deadline
2. Day before deadline:
     → Send reminder email
3. On deadline day:
     → Send urgent reminder
4. After deadline:
     → Create escalation task
     → Notify manager
     → Log overdue event
```

---

## Lista de comprobación para pruebas

- [ ] Tarea creada correctamente
- [ ] Tarea asignada al usuario/grupo correcto
- [ ] Notificación por correo electrónico enviada
- [ ] La tarea aparece en la lista de tareas del usuario
- [ ] Propiedades de la tarea correctas (título, descripción, prioridad, fecha límite)
- [ ] El usuario puede completar la tarea
- [ ] El flujo de trabajo continúa tras la finalización de la tarea
- [ ] El flujo de aprobación funciona correctamente
- [ ] El flujo de rechazo funciona correctamente
- [ ] El escalado se activa en el momento adecuado
- [ ] La gestión de tareas vencidas funciona
- [ ] Todas las notificaciones por correo electrónico se envían
- [ ] Las actualizaciones de campos funcionan correctamente

---

## Ejemplos del mundo real

### Ejemplo 1: Excepción de cotejo a tres bandas de PO

**Escenario:** La factura no coincide con la PO, necesita revisión

```
1. PO Matching fails (price variance > 5%)
2. Create Task: "Review PO Mismatch"
   - Assign to: Procurement Officer
   - Priority: High
   - Description: Include variance details
3. Send email with comparison table
4. Wait for task completion
5. IF Approved: Continue processing
   IF Rejected: Return to supplier
```

---

### Ejemplo 2: Aprobación de factura de proveedor

**Escenario:** La factura de un proveedor nuevo necesita una aprobación especial

```
1. Check if supplier is new (< 6 months old)
2. IF New:
     Create Task: "New Supplier Invoice Review"
     - Assign to: Procurement Manager
     - Include supplier details
     - Require supplier verification
3. After approval:
     Add to approved supplier list
     Continue normal workflow
```

---

### Ejemplo 3: Procesamiento de fin de mes

**Escenario:** Las facturas de fin de mes necesitan un procesamiento urgente

```
1. Check if document date in last 3 days of month
2. IF Yes:
     Create Task: "URGENT: Month-End Invoice"
     - Priority: Urgent
     - Deadline: 1 day
     - Assign to: Finance Team (all members)
     - Flag for expedited processing
3. Send urgent email notification
4. Track completion
```

---

## Consejos de rendimiento

✅ **Buenas prácticas:**
- Establezca fechas límite realistas
- Use títulos y descripciones de tarea claros
- Incluya toda la información necesaria en la tarea
- Envíe notificaciones oportunas
- Supervise las tasas de finalización de tareas
- Escale automáticamente las tareas vencidas
- Registre todas las actividades de las tareas
- Revise los patrones de tareas mensualmente

❌ **Evite:**
- Crear tareas para todo
- Descripciones de tarea imprecisas
- Fechas límite poco realistas
- Demasiados correos electrónicos de notificación
- No tener una ruta de escalado
- Ignorar las tareas vencidas
- No hacer seguimiento de las métricas de tareas

---

## Patrones relacionados

### Patrones que funcionan bien juntos:

- **[Patrón de integración de API](api-integration-pattern.md)** - Crea tareas para errores de API
- **[Patrón de cotejo de PO](po-matching-pattern.md)** - Crea tareas para discrepancias de PO
- **[Patrón de lógica de decisión](decision-logic-pattern.md)** - Enruta al tipo de tarea adecuado
- **[Patrón de transformación de datos](data-transformation-pattern.md)** - Transforma los datos antes de crear la tarea

---

## Guías relacionadas

### Requisitos previos
- [Guía de asignación de tareas](../then/task/task-assignment-guide.md) - Documentación de la tarjeta de tarea
- [Guía de asignación a usuario](../then/assignee/assignment-user-guide.md) - Asignación de usuarios
- [Guía de envío de correo a grupos](../then/action/send-email-groups-guide.md) - Notificaciones por correo electrónico

### Tarjetas relacionadas
- **tasks_create** - [Guía de asignación de tareas](../then/task/task-assignment-guide.md)
- **ACTION_ASSIGN_TO_USER** - [Guía de asignación](../then/assignee/assignment-user-guide.md)
- **ACTION_SEND_EMAIL_TO_GROUPS** - [Guía de correo electrónico](../then/action/send-email-groups-guide.md)
- **CONDITION_TASK_STATUS** - [Guía de tarjetas de condición](../and/condition-cards-complete-guide.md)

### Próximos pasos
- Añadir notificaciones por correo electrónico: [Guía de envío de correo](../then/action/send-email-groups-guide.md)
- Implementar enrutamiento complejo: [Patrón de lógica de decisión](decision-logic-pattern.md)
- Gestionar errores: [Patrón de gestión de errores](error-handling-pattern.md)

---

**Versión del patrón:** 1.0
**Última actualización:** 23 de octubre de 2025
**Dificultad:** Baja-Media
**Tiempo estimado:** 30-45 minutos
**Tasa de éxito:** Muy alta
