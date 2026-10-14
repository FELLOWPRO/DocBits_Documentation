# Document Assignment & User Cards - Complete Guide

Estas tarjetas van en el grupo **Then** del Generador de flujos de trabajo: las acciones que se ejecutan cuando se cumplen las condiciones When/And:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Las tarjetas se añaden al grupo <strong>Then</strong> mediante <strong>Add Card</strong>.</p></figcaption></figure>

**Cubre:** 13 tarjetas de asignación y relacionadas con usuarios

---

## 📌 Información de versión

**Tarjetas con varias versiones:** DOC_USER_ASSIGN (v2 la más reciente, v3 obsoleta), DOC_GROUP_ASSIGN (v2 la más reciente, v3 obsoleta), OC_ASSIGN_DOC (v2)

**Importante:** Las versiones v3 añadieron soporte de árbol de decisión pero ahora están obsoletas
**Recomendación:** Use v2 tanto para DOC_USER_ASSIGN como para DOC_GROUP_ASSIGN

📖 [Complete Version History](../../../changelog/release.md#-assignment--routing-cards) | [Card Version Database](../../../../DocFlow/docs/card_version.md)

---

# Asignación básica de documentos

## Tarjeta: DOC_USER_ASSIGN / Assign Document to User

### Propósito
Asigna el documento a una persona específica para que actúe

### Cuándo usar
- El documento necesita la revisión de una persona específica
- Traspaso a un miembro individual del equipo
- Seguimiento de la responsabilidad
- Asignar el trabajo a una persona designada

### Cómo funciona
```
Document is "assigned to" = John Smith
Only John can see it as assigned to him
John is responsible for this document
```

### Ejemplo
```
Invoice arrives
    ↓
Assign Document to: John Smith (Finance Manager)
    ↓
Only John sees "Assigned to Me"
John must take action on it
```

### Parámetros
```
User: [Select which person]
```

### Nota
Asignar significa:
- El documento aparece como "assigned to me" para esa persona
- Esa persona es la responsable
- Los demás pueden seguir viendo el documento (pero no como asignado a ellos)
- Una asignación a la vez por documento

---

## Tarjeta: DOC_GROUP_ASSIGN / Assign Document to Group

### Propósito
Asigna el documento a un grupo (todos los miembros lo ven como asignado a ellos)

### Cuándo usar
- Documento para un equipo, no para un individuo
- Varias personas pueden gestionarlo
- Responsabilidad compartida
- Distribución de la carga de trabajo del equipo

### Cómo funciona
```
Document is "assigned to" = Finance Team (10 people)
All 10 team members see "Assigned to My Group"
Any team member can take action
```

### Ejemplo
```
New vendor invoice
    ↓
Assign Document to: Procurement Team
    ↓
All procurement team members see it
First available person handles it
```

### Parámetros
```
Group: [Select which group]
```

### Diferencia
```
Individual Assignment:
- One person responsible
- That person sees "Assigned to Me"
- Others don't see assignment

Group Assignment:
- Team responsible
- All members see "Assigned to My Group"
- Anyone can claim/process
```

---

## Tarjeta: ACTION_ASSIGN_DOC_BASED_ON_DECISION_TABLE

### Propósito
Asigna el documento según la lógica de una tabla de decisión

### Cuándo usar
- Diferentes proveedores necesitan diferentes responsables
- Asignación basada en el importe
- Lógica de enrutamiento compleja
- Varias condiciones para la asignación

### Cómo funciona
```
Decision Table Logic:
  If Supplier = "ABC Corp" → Assign to: Procurement Team
  If Supplier = "XYZ Inc" → Assign to: Direct Manager
  If Amount > €10000 → Assign to: Finance Director

Document arrives
    ↓
Check: Which condition matches?
    ↓
Assign accordingly
```

### Ejemplo: Asignación basada en el importe
```
Invoice: €2000 from ABC Corp

Decision Table checks:
  Is amount > €10000? NO
  Is amount > €5000? NO
  Is amount > €1000? YES

Result: Assign to: Finance Manager
```

### Ejemplo: Asignación basada en el proveedor
```
Invoice from: Preferred Supplier

Decision Table:
  If preferred supplier → Finance Team
  If new supplier → Procurement Manager
  If blacklisted → Director Review

Result: Assign to: Finance Team
```

### Parámetros
```
Decision Table: [Select decision table]
(Decision table contains assignment logic)
```

---

## Tarjeta: ACTION_ASSIGN_DOC_DECISION_TABLE_SEQUENTIAL

### Propósito
Asigna el documento de forma secuencial según una tabla de decisión con prioridades

### Cuándo usar
- Varias aprobaciones secuenciales
- Diferentes personas en diferentes niveles
- Cadena de aprobación basada en el importe
- Ruta de escalamiento

### Cómo funciona
```
First Decision: Who approves first?
    ↓
Assign to: Person 1
    ↓
Person 1 approves
    ↓
Second Decision: Who approves next?
    ↓
Assign to: Person 2
    ↓
Person 2 approves (final)
    ↓
Document Complete
```

### Sistema de prioridades
```
Priority 1: First assignment
Priority 2: Second assignment
Priority 3: Third assignment
(etc.)

Each must complete before next begins
```

### Ejemplo: Aprobación multinivel
```
Invoice: €50,000

Decision Table:
  €1k-€5k → Assign to: Finance Manager (Priority 1)
  €5k-€20k → Then: Assign to: Finance Director (Priority 2)
  €20k+ → Then: Assign to: CFO (Priority 3)

Invoice Flow:
1. Finance Manager reviews → approves
2. Finance Director reviews → approves
3. CFO reviews → approves final

Each step depends on previous completion
```

### Parámetros
```
Decision Table: [Select]
Priority Order: [Determined by decision table]
```

---

## Tarjeta: ACTION_ASSIGN_DOC_TO_USER_SEQUENTIAL

### Propósito
Asigna el documento a un usuario con prioridad secuencial

### Cuándo usar
- El documento necesita una persona específica
- Procesamiento secuencial claro
- Asignación única con orden

### Cómo funciona
```
Assign Document to: User A (Priority 1)
    ↓
User A processes
    ↓
Then: Assign to User B (Priority 2)
    ↓
User B processes
```

### Ejemplo
```
Invoice processing:
1. Assign to: Accounts Payable Clerk
2. Then: Assign to: Finance Manager
3. Then: Assign to: Director

Each person has their turn
```

---

## Tarjeta: ACTION_ASSIGN_DOC_TO_GROUP_SEQUENTIAL

### Propósito
Asigna el documento de forma secuencial a grupos

### Cuándo usar
- Varias aprobaciones de grupo
- Diferentes departamentos en cada fase
- Procesamiento secuencial basado en equipos

### Cómo funciona
```
Step 1: Assign to Group A (Quality Team)
        Quality verifies
    ↓
Step 2: Assign to Group B (Finance Team)
        Finance reviews
    ↓
Step 3: Assign to Group C (Procurement)
        Procurement approves
```

### Ejemplo
```
New Supplier Onboarding:

Step 1: Quality Team
  - Evaluate supplier capability
  - Check certifications

Step 2: Finance Team
  - Check payment terms
  - Verify pricing

Step 3: Procurement Team
  - Approve supplier
  - Set up in system

Document passes through all three
```

---

## Tarjeta: ACTION_ASSIGN_DOC_TO_FACILITY_GROUP

### Propósito
Asigna el documento a un grupo de instalación específico

### Cuándo usar
- Documento para un almacén/instalación específico
- Operaciones basadas en instalaciones
- Procesamiento específico por ubicación

### Ejemplo
```
Shipment notification

Assign to: Berlin Warehouse Team
    ↓
Berlin warehouse processes shipment
    ↓
Or

Assign to: Munich Warehouse Team
    ↓
Munich warehouse processes shipment
```

---

## Tarjeta: ACTION_ASSIGN_DOC_TO_FACILITY_GROUP_SEQUENTIAL

### Propósito
Asigna de forma secuencial entre instalaciones

### Cuándo usar
- Procesamiento en varias ubicaciones
- El envío pasa por las instalaciones
- Flujo de trabajo basado en la ubicación

### Ejemplo
```
Manufacturing Order:

Step 1: Factory A (Manufacturing) - Build product
Step 2: Quality Center (Testing) - Test product
Step 3: Distribution Center (Packing) - Package
Step 4: Warehouse (Storage) - Store

Document/shipment passes through each
```

---

## Tarjeta: ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP

### Propósito
Asigna el documento al departamento de compras

### Cuándo usar
- Gestión por parte del equipo de compras
- Trabajo relacionado con proveedores
- Relacionado con pedidos de compra

### Ejemplo
```
Vendor evaluation document
    ↓
Assign to: Procurement Group
    ↓
Procurement team evaluates vendor
```

---

## Tarjeta: ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP_SEQUENTIAL

### Propósito
Asignación secuencial dentro del departamento de compras

### Cuándo usar
- Proceso de compras de varios pasos
- Cadena de aprobación en compras

### Ejemplo
```
Purchase Requisition:

Step 1: Buyer (Creates PO)
Step 2: Approver (Reviews)
Step 3: Director (Final sign-off)

Each step in sequence
```

---

## Tarjeta: ACTION_CHANGE_DOC_SUBORG / Change Document Sub-Organization

### Propósito
Asigna el documento a una suborganización diferente

### Cuándo usar
- Se seleccionó la organización incorrecta
- Es necesario moverlo al departamento correcto
- Reestructuración organizativa

### Cómo funciona
```
Current Sub-Org: Finance Department
    ↓
Change to: Accounting Department
    ↓
Document now belongs to Accounting
```

### Ejemplo
```
Document for: Berlin Office
    ↓
Realize should be: Munich Office
    ↓
Change Sub-Organization to: Munich Office
```

---

## Tarjeta: ACTION_CHANGE_DOC_SUBORG_BY_FIELD_TEXT

### Propósito
Cambia la suborganización según el valor de un campo del documento

### Cuándo usar
- La suborganización está almacenada en un campo
- Hacer coincidir la ubicación del documento con el campo
- Asignación automática de organización

### Cómo funciona
```
Document Field: "Delivery_Location" = "Berlin"
    ↓
Decision Table:
  If location = "Berlin" → Assign to: Berlin Sub-Org
  If location = "Munich" → Assign to: Munich Sub-Org

    ↓
Document assigned to: Berlin Sub-Org
```

### Ejemplo
```
Invoice field: "Cost Center: CC-Berlin-001"
    ↓
System recognizes: Berlin location
    ↓
Change document to: Berlin Sub-Organization
```

---

## Tarjeta: ACTION_ASSIGN_USER_FROM_FIELD_WITH_FALLBACK

### Propósito
Asigna el documento a un usuario obtenido de un campo, con un respaldo si no se encuentra el usuario

### Cuándo usar
- El nombre del usuario está almacenado en un campo del documento
- Puede no existir en el sistema
- Se necesita un respaldo si el usuario no está disponible

### Cómo funciona
```
Document Field: "Approver: John Smith"
    ↓
Try to assign to: John Smith
    ↓
If John doesn't exist:
    ↓
Use Fallback: Sarah Johnson (Manager)
    ↓
Document assigned to: Sarah Johnson
```

### Parámetros
```
Source Field: [Field containing user name]
Fallback User: [If source user not found]
```

### Ejemplo
```
Invoice has field: "Contact Person: Mike Johnson"

Try to assign to: Mike Johnson
    ↓
If Mike not in system:
    ↓
Fallback to: Finance Manager (Robert)
```

---

## Tarjeta: ACTION_ASSIGN_USER_TO_SUPPLIER

### Propósito
Asigna el documento al usuario que gestiona ese proveedor

### Cuándo usar
- Usuario vinculado a un proveedor
- Gestor de cuenta del proveedor
- Responsable de la relación con el proveedor

### Cómo funciona
```
Document Supplier: ABC Corp
    ↓
System checks: Who manages ABC Corp?
    ↓
Assign to: John Smith (ABC Corp Account Manager)
```

---

# Árboles de decisión de asignación

## Ejemplo de tabla de decisión 1: Basada en el importe
```
Amount ≤ €1000
  → Assign to: Finance Team

Amount €1000-€5000
  → Assign to: Finance Manager

Amount €5000-€20000
  → Assign to: Finance Director

Amount > €20000
  → Assign to: CFO
```

## Ejemplo de tabla de decisión 2: Basada en el proveedor
```
Supplier Type = "Preferred"
  → Assign to: Account Manager

Supplier Type = "New"
  → Assign to: Procurement Manager

Supplier Type = "Problem"
  → Assign to: Procurement Director
```

## Ejemplo de tabla de decisión 3: Basada en el tipo de documento
```
Document Type = "Invoice"
  → Assign to: Accounts Payable Team

Document Type = "Credit Memo"
  → Assign to: Finance Manager

Document Type = "PO"
  → Assign to: Procurement Team
```

---

# Ejemplos de flujos de trabajo de asignación

## Ejemplo 1: Enrutamiento simple
```
Document Arrives
    ↓
Check: Supplier = "ABC Corp"? YES
    ↓
Assign to: John Smith
(John handles ABC Corp)
    ↓
John reviews and approves
```

## Ejemplo 2: Aprobación secuencial
```
Document Arrives
    ↓
Assign to: Finance Manager (Step 1)
    ↓
Manager reviews
    ↓
Passes to: Finance Director (Step 2)
    ↓
Director reviews
    ↓
Passes to: CFO (Step 3)
    ↓
CFO approves final
```

## Ejemplo 3: Enrutamiento basado en el importe
```
Invoice: €50,000
    ↓
Decision Table: Amount > €20k?
    ↓
YES → Assign to: CFO
    ↓
CFO approves directly
```

## Ejemplo 4: Basado en la instalación
```
Shipment for: Berlin Office
    ↓
Assign to: Berlin Warehouse Team
    ↓
Then assign to: Berlin Distribution Team
    ↓
Both teams process in sequence
```

---

# Buenas prácticas de asignación

✅ **Haga:**
- Mantenga las tablas de decisión simples
- Pruebe la lógica de enrutamiento con muestras
- Asegúrese de que todas las rutas conduzcan a algún sitio
- Tenga un respaldo para los usuarios que falten
- Documente las decisiones de enrutamiento

❌ **No haga:**
- Crear asignaciones circulares (A→B→A)
- Asignar a usuarios inexistentes (sin respaldo)
- Hacer el enrutamiento demasiado complejo
- Olvidar probar el enrutamiento
- Asignar a personas no disponibles

---

# Resolución de problemas de asignación

## "Document not assigned"
**Causa:** No se cumple la condición o el usuario no existe

**Solución:**
- Compruebe que la condición es verdadera
- Verifique que el usuario existe en el sistema
- Compruebe la configuración del respaldo
- Revise la lógica de la tabla de decisión

## "Wrong person assigned"
**Causa:** La tabla de decisión o la lógica de enrutamiento es incorrecta

**Solución:**
- Pruebe la tabla de decisión
- Compruebe las condiciones
- Verifique la asignación de usuarios
- Revise los valores de los campos

## "Assignment seems to skip someone"
**Causa:** El orden secuencial es incorrecto

**Solución:**
- Compruebe los números de prioridad
- Verifique que la secuencia es correcta
- Pruebe con una muestra
- Revise el orden de la tabla de decisión

---

# Comparación de tarjetas de asignación

| Tarjeta | Asigna a | Tipo de ruta | Caso de uso |
|------|-----------|-----------|----------|
| DOC_USER_ASSIGN | Individuo | Directa | Asignación simple |
| DOC_GROUP_ASSIGN | Grupo | Directa | Asignación a equipo |
| ACTION_ASSIGN_DOC_BASED_ON_DECISION_TABLE | Resultado de decisión | Condicional | Enrutamiento complejo |
| ACTION_ASSIGN_DOC_DECISION_TABLE_SEQUENTIAL | Múltiple (secuencial) | Condicional | Cadena de aprobación |
| ACTION_ASSIGN_DOC_TO_USER_SEQUENTIAL | Usuario (secuencial) | Ordenada | Pasos secuenciales de usuario |
| ACTION_ASSIGN_DOC_TO_GROUP_SEQUENTIAL | Grupos (secuencial) | Ordenada | Pasos secuenciales de grupo |
| ACTION_ASSIGN_DOC_TO_FACILITY_GROUP | Grupo de instalación | Directa | Específica de instalación |
| ACTION_ASSIGN_DOC_TO_FACILITY_GROUP_SEQUENTIAL | Instalaciones (secuencial) | Ordenada | Varias instalaciones |
| ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP | Compras | Directa | Flujo de trabajo de compras |
| ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP_SEQUENTIAL | Compras (secuencial) | Ordenada | Cadena de aprobación de compras |
| ACTION_CHANGE_DOC_SUBORG | Suborganización | Directa | Cambio de departamento |
| ACTION_CHANGE_DOC_SUBORG_BY_FIELD_TEXT | Suborg. por campo | Condicional | Asignación basada en campo |
| ACTION_ASSIGN_USER_FROM_FIELD_WITH_FALLBACK | Campo/respaldo | Condicional | Asignación dinámica de usuario |

---

# Tarjetas relacionadas

- **ACTION_CREATE_TASK_FOR_USER** - Asignar una tarea a la misma persona
- **ACTION_SEND_EMAIL** - Notificar a la persona asignada
- **CONDITION_USER_IS_ISNOT** - Comprobar si se ha asignado a la persona correcta
- **CONDITION_GROUP_IS_ISNOT** - Comprobar si se ha asignado al grupo correcto
