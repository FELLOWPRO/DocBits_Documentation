# Tarjetas de creación y asignación de tareas

## Tarjetas de creación y asignación de tareas: guía completa

**Cubiertas:** 12 tarjetas relacionadas con tareas

***

Las tarjetas de tareas en esta página van en el grupo **Entonces** del Generador de flujo de trabajo: las acciones que se ejecutan una vez que coinciden las condiciones Cuándo/Y:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-es.png" alt="Ejemplo sin guardar con tarjetas Cuando, Y y Entonces. Configure todos los campos antes de ejecutarlo. Algunas etiquetas de esta versión de la tarjeta todavía tienen una traducción incompleta o incorrecta en la interfaz. Las explicaciones de esta página utilizan los términos correctos."><figcaption><p>Ejemplo sin guardar con tarjetas Cuando, Y y Entonces. Configure todos los campos antes de ejecutarlo. Algunas etiquetas de esta versión de la tarjeta todavía tienen una traducción incompleta o incorrecta en la interfaz. Las explicaciones de esta página utilizan los términos correctos.</p></figcaption></figure>

***

### 📌 Información de versión

**Tarjeta más evolucionada:** tasks\_create (4 versiones, v4 más reciente) **Otras tarjetas multiversión:** ACTION\_TASK\_FOR\_GROUP (v4), ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP (v3), ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK (v3), ACTION\_DECISION\_TREE\_CREATE\_TASKS (v3)

**Cambios clave:**

* **v3 → v4 Evolución:** Se eliminó el enfoque de árbol de decisión, se agregaron tipos de elementos de trabajo genéricos (tarea, ticket, problema)
* **v2 → v3 Migración:** Se agregó soporte para árbol de decisiones (ahora en su mayoría obsoleto)

📖 [Historial de versiones completo](../../release.md) | [Versiones de tarjetas y comportamiento](../../cards-overview/card-versions-guide.md)

***

### Descripción general

Las tarjetas de tareas crean asignaciones de trabajo para los miembros del equipo. Cuando una factura necesita aprobación, puede crear automáticamente una tarea y asignarla a la persona adecuada.

***

## Creación de tareas básicas

### Tarjeta: tasks\_create / Crear tarea y asignar a usuario

#### Propósito

Crea una tarea y la asigna a una persona específica

#### Cuando usar

* La factura necesita la revisión de una persona específica
* Se requiere aprobación de la persona designada
* Traspaso a un miembro específico del equipo

#### Parámetros

**Título** El nombre/asunto de la tarea

```
Example: "Review Invoice #INV-2025-001 for approval"
```

**Descripción** Detalles sobre la tarea

```
Example: "Invoice from Supplier ABC needs review.
Amount: €5000
Deadline: 2025-10-30
Please verify pricing and quality."
```

**Prioridad**

* 🔴 **Alto**: Urgente, hazlo inmediatamente
* 🟡 **Media**: Prioridad normal
* 🟢 **Bajo**: Se puede hacer más tarde

**Usuario asignado** Quién recibe la tarea

```
Example: John Smith (Finance Manager)
```

**Notificación por correo electrónico** ¿Enviar alerta por correo electrónico a la persona asignada?

```
✅ Yes: Person gets email
❌ No: Task only in system
```

#### Ejemplo

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

***

### Tarjeta: ACTION\_TASK\_FOR\_GROUP / Crear Tarea para Grupo

#### Propósito

Crea una tarea y la asigna a un grupo (todos los miembros pueden verla)

#### Cuando usar

* Varias personas pueden realizar la tarea.
* Tarea para equipo, no individual.
* La primera persona disponible debe encargarse

#### Diferencia de la tarea individual

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

#### Flujo de trabajo de ejemplo

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

***

### Tarjeta: ACTION\_DECISION\_TREE\_CREATE\_TASKS

#### Propósito

Crea tareas basadas en la lógica de la tabla de decisiones.

#### Cómo funciona

```
Decision Table Returns:
  If invoice from Supplier A → Assign to Procurement
  If invoice from Supplier B → Assign to Quality Team
  If invoice from Supplier C → Assign to Finance

Task is automatically created and assigned
based on which condition is true
```

#### Cuando usar

* Diferentes proveedores necesitan diferentes aprobaciones
* Enrutamiento complejo basado en múltiples factores
* Equipo diferente según el tipo de documento

#### Ejemplo

```
Document: Invoice from ABC Corp (Supplier A)
    ↓
Decision Table checks: Which supplier?
    ↓
Result: Supplier A → Procurement Team
    ↓
Create and assign task to Procurement Team
```

***

### Tarjeta: ACTION\_DECISION\_TREE\_TASKS\_SEQUENTIAL

#### Propósito

Crea tareas secuencialmente según la tabla de decisiones. Las tareas se asignan una a la vez con orden de prioridad.

#### Cuando usar

* Se necesitan varias aprobaciones en secuencia
* Cadena de aprobación del flujo de trabajo
* Cada persona revisa y luego pasa al siguiente.

#### Cómo funciona

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

#### Sistema de Prioridad

```
Priority 1 → Assign to: Person A
Priority 2 → Assign to: Person B
Priority 3 → Assign to: Person C

They must complete in order (1→2→3)
```

#### Configuración de ejemplo

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

***

### Tarjeta: ACTION\_CREATE\_TASK\_FOR\_USER\_SEQUENTIAL

#### Propósito

Asigna un documento a un usuario Y crea una tarea secuencial

#### Cuando usar

* Asignar documento Y crear tarea al mismo tiempo
* El documento debe ser revisado por una persona específica.
* Realice un seguimiento tanto de la asignación como de la creación de tareas

#### Cómo funciona

```
Two things happen:
1. Document is assigned to: Person A
2. Task is created for: Person A

Both in one action
```

#### Ejemplo

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

***

### Tarjeta: ACTION\_CREATE\_TASK\_FOR\_GROUP\_SEQUENTIAL

#### Propósito

Asigna documento al grupo Y crea tarea

#### Cuando usar

* El documento necesita atención grupal.
* Quiere realizar un seguimiento de la creación de tareas
* Crear tarea inicial y luego documentar la asignación

#### Ejemplo

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

***

## Creación avanzada de tareas

### Tarjeta: ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP

#### Propósito

Crea una tarea para un grupo de instalaciones específico

#### Cuando usar

* Tarea para el equipo de almacén/instalación
* Operaciones específicas de la instalación
* La ubicación física importa

#### Ejemplo

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

***

### Tarjeta: ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP\_SEQUENTIAL

#### Propósito

Asignación secuencial de tareas entre instalaciones

#### Cuando usar

* Operaciones de múltiples instalaciones
* Las tareas pasan de una instalación a otra.
* Procesamiento secuencial de instalaciones

#### Cómo funciona

```
Factory A (Step 1): Production
    ↓
Quality Check (Step 2): Verification
    ↓
Warehouse (Step 3): Packaging
    ↓
Shipping (Step 4): Dispatch
```

#### Ejemplo

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

***

### Tarjeta: ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP

#### Propósito

Crea una tarea para el departamento de adquisiciones.

#### Cuando usar

* Tarea para el equipo de adquisiciones
* Tareas de gestión de proveedores.
* Trabajo relacionado con compras

#### Ejemplo

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

***

### Tarjeta: ACTION\_ASSIGN\_TASK\_PROCUREMENT\_GROUP\_SEQUENTIAL

#### Propósito

Enrutamiento secuencial de tareas dentro de adquisiciones

#### Cuando usar

* Procesos de adquisición de varios pasos
* Cadena de aprobación en adquisiciones
* Ruta de escalada

#### Ejemplo

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

***

### Tarjeta: ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK

#### Propósito

Obtenga el usuario del campo del documento, asigne la tarea. Si no se encuentra el usuario, utilice el usuario alternativo.

#### Cuando usar

* Usuario almacenado en el campo del documento
* El documento especifica quién debe revisar
* Tener una persona de respaldo si el usuario especificado no está disponible

#### Cómo funciona

```
Document has field: "Approver Name: John Smith"

Card checks: Is John in system?
    If YES → Assign task to John
    If NO → Assign to Fallback User (Sarah)
```

#### Ejemplo

```
Invoice field: "Contact: Mike Johnson"

Try to assign task to Mike Johnson
    ↓
If Mike doesn't exist in system:
    ↓
Use Fallback: Team Lead (Robert Brown)
```

#### Parámetros

```
- Field to Read: "Approver Name"
- Fallback User: Robert Brown
- Task Details: Title, Description, Priority
```

***

## Parámetros de tareas comunes

Todas las tarjetas de tareas utilizan estos parámetros:

#### Título

```
Good: "Review Invoice #INV-12345 - €5000 - Supplier ABC"
Bad: "Approve something"
```

#### Descripción

```
Should include:
✅ What to do
✅ Deadline
✅ Any special requirements
✅ Who to contact
✅ Link to document
```

#### Niveles de prioridad

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

#### Fecha de vencimiento (si está disponible)

```
When should task be completed by?
Example: 2025-10-30 (5 days from now)
```

***

## Escenarios de flujo de trabajo de tareas

### Escenario 1: Aprobación simple

```
Invoice Arrives (€2000)
    ↓
Condition: Amount between €1000-€5000?
    ↓
YES: Create Task for Finance Manager
    ↓
Finance Manager reviews and approves
```

### Escenario 2: Aprobación multinivel

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

### Escenario 3: Tareas paralelas

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

### Escenario 4: enrutamiento condicional

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

***

## Mejores prácticas de asignación de tareas

✅ **Hacer:**

* Incluir detalles específicos en el título de la tarea.
* Establecer niveles de prioridad apropiados
* Establecer plazos realistas
* Notificar a los responsables
* Incluir enlace al documento
* Utilice descripciones claras y prácticas

❌ **No:**

* Cree títulos de tareas vagos ("Revisar esto")
* Establecer todo como prioridad alta
* Olvídate de avisar a la persona asignada
* Crea múltiples tareas para el mismo trabajo
* Asignar a personas no disponibles

***

## Tareas de solución de problemas

### "Tarea no asignada a nadie"

**Causa:** El usuario no existe o el grupo está vacío

**Solución:**

* Verificar la ortografía del nombre de usuario
* Verificar que el usuario esté activo en el sistema
* Verificar que el grupo tenga miembros
* Utilice respaldo si es necesario

### "La persona dice que no recibió la notificación"

**Causa:** Notificación por correo electrónico deshabilitada o correo electrónico incorrecto

**Solución:**

* Marque la casilla de verificación "Enviar correo electrónico" que esté habilitada
* Verificar la dirección de correo electrónico del destinatario
* Revisar la carpeta de spam
* Reenviar notificación manualmente

### "La persona equivocada consiguió la tarea"

**Causa:** Lógica de enrutamiento incorrecta

**Solución:**

* Consultar las condiciones de la tabla de decisiones.
* Verificar la configuración alternativa
* Prueba con documento de muestra
* Compruebe si hay errores tipográficos en los nombres de usuario

### "Se crearon demasiadas tareas"

**Causa:** Tarjeta disparada varias veces

**Solución:**

* Las condiciones de verificación son lo suficientemente específicas.
* Verificar tarjeta solo se ejecuta una vez por documento
* Revisar las condiciones "Y"
* Agregar filtrado adicional

***

## Tabla de comparación de tarjetas de tareas

| tarjeta                                                        | Crea tarea | Asigna a            | When        |
| ----------------------------------------------------------- | ------------ | --------------------- | ----------- |
| tasks\_create                                               | Sí          | individuo            | siempre      |
| ACTION\_TASK\_FOR\_GROUP                                    | Sí          | grupo                 | siempre      |
| ACTION\_DECISION\_TREE\_CREATE\_TASKS                       | Sí          | Resultado de la tabla de decisión | Condicional |
| ACTION\_DECISION\_TREE\_TASKS\_SEQUENTIAL                   | Sí          | Múltiple (Secuencial) | Condicional |
| ACTION\_CREATE\_TASK\_FOR\_USER\_SEQUENTIAL                 | Sí          | Usuario + Documento       | Condicional |
| ACTION\_CREATE\_TASK\_FOR\_GROUP\_SEQUENTIAL                | Sí          | Grupo + Documento      | Condicional |
| ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP                   | Sí          | Grupo de instalaciones        | Condicional |
| ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP\_SEQUENTIAL       | Sí          | Múltiples instalaciones   | Condicional |
| ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP                | Sí          | Equipo de adquisiciones      | Condicional |
| ACTION\_ASSIGN\_TASK\_PROCUREMENT\_GROUP\_SEQUENTIAL        | Sí          | Múltiple (Secuencial) | Condicional |
| ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK | Sí          | Campo/Reserva        | Condicional |

***

## Tarjetas relacionadas

* **ACTION\_ASSIGN\_DOCUMENT\_TO\_USER** - Asignar documento sin crear tarea
* **ACTION\_SEND\_EMAIL** - Notificar a las personas directamente
* **STAUS\_CHANGE**: cambiar el estado en lugar de crear una tarea
* **RUN\_WORKFLOW**: en su lugar, activa un flujo de trabajo diferente
