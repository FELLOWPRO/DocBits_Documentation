# Patrón de lógica de decisión

**Tipo de patrón:** Enrutamiento condicional y lógica
**Complejidad:** Media
**Configuración estimada:** 30-45 minutos
**Casos de uso habituales:** Enrutamiento multirruta, procesamiento condicional, árboles de decisión, implementación de reglas de negocio

---

Este patrón se monta en el **Workflow Builder** (Workflow Dashboard → Workflow List → Add Workflow). Haga clic en **Add Card** y abra la categoría **Logic**: contiene las tarjetas de condición y ramificación que impulsan el árbol de decisión, que combina con el grupo **And** para evaluar varias condiciones:

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Biblioteca Add Card del Workflow Builder, agrupada por categoría"><figcaption><p>La biblioteca <strong>Add Card</strong>: las tarjetas de condición y ramificación se encuentran en la categoría <strong>Logic</strong>.</p></figcaption></figure>

---

## Resumen del patrón

Este patrón muestra cómo implementar lógica de decisión compleja en los flujos de trabajo de DocBits usando tarjetas de condición para enrutar documentos por distintas rutas de procesamiento según los atributos del documento, los valores de los campos y las reglas de negocio.

**Qué hace este patrón:**
1. Evalúa varias condiciones en secuencia o en paralelo
2. Enruta los documentos por distintas rutas según las condiciones
3. Implementa reglas y políticas de negocio
4. Gestiona árboles de decisión complejos
5. Combina varios criterios para las decisiones de enrutamiento

---

## Cuándo usar este patrón

Use este patrón cuando necesite:
- ✅ Enrutar documentos por umbrales de importe
- ✅ Aplicar distintas reglas para distintos tipos de documento
- ✅ Implementar lógica de aprobación multinivel
- ✅ Gestionar políticas de negocio complejas
- ✅ Crear enrutamiento dinámico basado en varios criterios
- ✅ Implementar lógica de gestión de excepciones
- ✅ Crear matrices de aprobación

**No use este patrón cuando:**
- ❌ Un flujo de trabajo lineal simple sea suficiente
- ❌ Todos los documentos sigan la misma ruta
- ❌ No se necesite procesamiento condicional

---

## Tipos de lógica de decisión

### 1. Lógica IF-THEN simple

```
IF condition:
  → Action A
ELSE:
  → Action B
```

**Ejemplo:**
```
IF Amount > €10,000:
  → Assign to Director
ELSE:
  → Assign to Manager
```

### 2. Varios criterios (lógica AND)

```
IF condition1 AND condition2 AND condition3:
  → Action A
ELSE:
  → Action B
```

**Ejemplo:**
```
IF Amount > €10,000 AND Supplier = "New" AND Department = "IT":
  → Assign to IT Director + CFO (dual approval)
ELSE:
  → Standard approval workflow
```

### 3. Criterios alternativos (lógica OR)

```
IF condition1 OR condition2 OR condition3:
  → Action A
ELSE:
  → Action B
```

**Ejemplo:**
```
IF Amount > €50,000 OR Supplier is "Blocked" OR Document has "Urgent" flag:
  → Escalate immediately
ELSE:
  → Standard processing
```

### 4. Árbol de decisión anidado

```
IF condition1:
  IF condition2:
    → Action A
  ELSE:
    → Action B
ELSE:
  IF condition3:
    → Action C
  ELSE:
    → Action D
```

**Ejemplo:**
```
IF Document_Type = "Invoice":
  IF Amount > €10,000:
    → High-value invoice workflow
  ELSE:
    → Standard invoice workflow
ELSE IF Document_Type = "Credit Note":
  IF Amount > €5,000:
    → High-value credit workflow
  ELSE:
    → Standard credit workflow
```

---

## Ejemplo de flujo de trabajo completo

### Escenario: Matriz de aprobación de facturas

**Reglas de negocio:**
1. Importe < 1.000 €: Aprobación automática
2. Importe 1.000 €-10.000 €: Aprobación del Manager
3. Importe > 10.000 € Y proveedor nuevo: Aprobación de Director + CFO
4. Importe > 10.000 € Y proveedor existente: Aprobación solo de Director
5. Cualquier importe con discrepancia de PO: Aprobación de Procurement primero
6. Facturas urgentes (marcadas): Flujo de trabajo acelerado

**Implementación:**

```
STEP 1: Check for PO Mismatch
  IF PO_Match_Status = "FAIL":
    → Route to Procurement for PO resolution
    → After resolution, continue below

STEP 2: Check Urgent Flag
  IF Urgent_Flag = TRUE:
    → Skip amount checks
    → Direct to highest approver
    → Set priority = HIGH
    → 1-day deadline

STEP 3: Amount-Based Routing (if not urgent)
  IF Amount < €1,000:
    → Auto-approve
    → Export immediately

  ELSE IF Amount < €10,000:
    → Create task for Manager
    → Priority: Medium
    → Deadline: 3 days

  ELSE IF Amount ≥ €10,000:
    CHECK Supplier Status:
      IF Supplier_Age < 180 days (New):
        → Create task for Director (Task 1)
        → After approval, create task for CFO (Task 2)
        → Priority: High
        → Deadline: 2 days each

      ELSE (Existing Supplier):
        → Create task for Director only
        → Priority: High
        → Deadline: 2 days
```

---

## Implementación paso a paso

### Paso 1: Definir las tarjetas de condición

**Condición 1: Umbral de importe**
```
Card: CONDITION_DOC_FIELD_AMOUNT
Field: Total_Amount
Operator: IS LESS THAN
Value: 1000
Currency: EUR
```

**Condición 2: Comprobación del tipo de documento**
```
Card: CONDITION_DOC_TYPE_IS_ISNOT
Document Type: IS
Type: Invoice
```

**Condición 3: Estado del proveedor**
```
Card: CONDITION_SUPPLIER_STATUS_IS_ISNOT
Supplier Status: IS
Status: ACTIVE
```

**Condición 4: Comprobación de proveedor nuevo**
```
Card: CONDITION_DOC_FIELD_DATE
Field: Supplier_First_Transaction_Date
Operator: IS AFTER
Value: {{TODAY_MINUS_180_DAYS}}
```

**Referencia de guía:** [Guía completa de tarjetas de condición](../and/condition-cards-complete-guide.md)

---

### Paso 2: Construir el árbol de decisión

**Nivel 1: Tipo de documento**
```
Workflow: "Invoice Processing"

IF Document_Type = "Invoice":
  → Continue to Level 2

ELSE IF Document_Type = "Credit Note":
  → Branch to "Credit Note Processing"

ELSE IF Document_Type = "Receipt":
  → Branch to "Receipt Processing"

ELSE:
  → Route to "Unknown Document Type" handling
```

**Nivel 2: Umbrales de importe (para facturas)**
```
IF Amount < €1,000:
  → Branch to "Auto-Approve Path"

ELSE IF Amount < €10,000:
  → Branch to "Manager Approval Path"

ELSE IF Amount < €50,000:
  → Branch to "Director Approval Path"
  → Check Level 3 conditions

ELSE (Amount ≥ €50,000):
  → Branch to "Executive Approval Path"
  → Dual or triple approval required
```

**Nivel 3: Análisis del proveedor (para facturas de alto valor)**
```
IF Supplier_Status = "BLOCKED":
  → STOP processing
  → Create urgent escalation task
  → Notify procurement and finance

ELSE IF Supplier_Age < 180 days (New):
  → Additional approval required
  → Add CFO to approval chain
  → Enhanced verification

ELSE IF Supplier_Risk_Rating = "HIGH":
  → Additional checks required
  → Fraud detection review
  → Manager pre-approval

ELSE:
  → Standard high-value workflow
```

---

### Paso 3: Crear las acciones de enrutamiento

**Ruta A: Aprobación automática (importe < 1.000 €)**
```
Actions:
1. Set field "Approval_Type" = "AUTO"
2. Set field "Approval_Level" = "0"
3. ACTION_APPROVE_DOCUMENT
4. Export to ERP
5. Send confirmation email (optional)
```

**Ruta B: Aprobación del Manager (1.000 €-10.000 €)**
```
Actions:
1. Set field "Approval_Type" = "MANUAL"
2. Set field "Approval_Level" = "1"
3. tasks_create:
   - Title: "Approve Invoice {{DOCUMENT_NUMBER}}"
   - Assign to: Department_Manager
   - Priority: Medium
   - Deadline: 3 days
4. Send email notification to manager
5. Wait for task completion
6. If approved: Export to ERP
7. If rejected: Return to supplier
```

**Ruta C: Aprobación del Director (10.000 €-50.000 €)**
```
Actions:
1. Set field "Approval_Type" = "MANUAL"
2. Set field "Approval_Level" = "2"
3. Check Supplier_Age:
   IF New (< 180 days):
     - Create Task 1: Director approval
     - After Task 1: Create Task 2: CFO approval
     - Dual approval required
   ELSE:
     - Create Task: Director approval only
4. Priority: High
5. Deadline: 2 days
6. Send email notifications
7. Wait for completion
8. If all approved: Export
9. If any rejected: Return to supplier
```

**Ruta D: Aprobación ejecutiva (≥ 50.000 €)**
```
Actions:
1. Set field "Approval_Type" = "EXECUTIVE"
2. Set field "Approval_Level" = "3"
3. Sequential approvals:
   - Task 1: Finance Director
   - Task 2: CFO
   - Task 3: CEO (if > €100,000)
4. Priority: Urgent
5. Deadline: 1 day each
6. Send urgent notifications
7. Executive dashboard update
8. Wait for all approvals
9. If all approved: Export
10. If any rejected: Executive review meeting
```

---

## Patrones avanzados de lógica de decisión

### Patrón 1: Enrutamiento basado en puntuación

**Calcule una puntuación de riesgo y enrute en consecuencia:**

```
Risk Score Calculation:
  Score = 0

  IF Amount > €50,000: Score += 30
  IF Supplier_Age < 180 days: Score += 25
  IF PO_Variance > 10%: Score += 20
  IF Supplier_Country = "High Risk Country": Score += 15
  IF Payment_Terms < 30 days: Score += 10

  Total Score Range: 0-100

Routing:
  IF Score < 20: Auto-approve
  IF Score 20-50: Manager approval
  IF Score 51-75: Director approval
  IF Score > 75: Executive approval + fraud check
```

**Implementación:**
```
1. ACTION_CALCULATE_FIELD: Calculate risk score
2. ACTION_SET_FIELD_TO_NUMBER: Store score
3. CONDITION_DOC_FIELD_NUMBER: Check score thresholds
4. Route based on score
```

---

### Patrón 2: Matriz basada en departamentos

**Distintas reglas de aprobación por departamento:**

```
Department Matrix:

  IT Department:
    Amount < €5,000: IT Manager
    Amount ≥ €5,000: IT Director + CIO

  Finance Department:
    Amount < €10,000: Finance Manager
    Amount ≥ €10,000: CFO

  Operations Department:
    Amount < €3,000: Operations Manager
    Amount ≥ €3,000: COO

  General:
    Amount < €2,000: Department Manager
    Amount ≥ €2,000: Department Director
```

**Implementación:**
```
1. Check Department field
2. Based on department, check amount threshold
3. Route to appropriate approver
4. Different thresholds per department
```

---

### Patrón 3: Lógica basada en el tiempo

**Distintas reglas según el momento:**

```
Month-End Processing (Last 3 days of month):
  IF Today in last 3 days of month:
    - Priority: URGENT
    - Deadline: 1 day
    - Approver: On-duty finance manager
    - Expedited workflow
  ELSE:
    - Standard priority
    - Standard deadline
    - Standard workflow

Business Hours vs After Hours:
  IF Time between 9 AM - 5 PM:
    - Assign to current shift
  ELSE:
    - Queue for next business day
    - OR route to on-call approver

Fiscal Period:
  IF Document_Date in Current_Fiscal_Period:
    - Standard processing
  ELSE:
    - Flag as "Prior Period"
    - Require accounting approval
    - Additional checks
```

---

### Patrón 4: Enrutamiento basado en excepciones

**Enrute las excepciones por separado:**

```
Exception Detection:

  No Exception:
    → Standard workflow

  Minor Exception (Auto-fixable):
    → Auto-correct
    → Log correction
    → Continue standard workflow

  Medium Exception (Needs review):
    → Create review task
    → Flag document
    → After fix: Continue workflow

  Major Exception (Requires escalation):
    → Stop processing
    → Create urgent task
    → Notify multiple levels
    → Manual intervention required

Exception Types:
  - Missing required field
  - Invalid field value
  - PO mismatch
  - Duplicate invoice
  - Supplier mismatch
  - Amount discrepancy
```

---

## Diagrama completo de lógica de decisión

```
INVOICE ARRIVES
│
├─ LEVEL 1: EXCEPTION CHECK
│  │
│  ├─ Has Critical Exception? (Missing PO, Duplicate, etc.)
│  │  │
│  │  ├─ YES → Stop & Escalate
│  │  │        Create urgent task
│  │  │        Notify admin
│  │  │        → END (Exception Handling)
│  │  │
│  │  └─ NO → Continue to Level 2
│
├─ LEVEL 2: DOCUMENT TYPE
│  │
│  ├─ Type = Invoice?
│  │  └─ YES → Continue to Level 3
│  │
│  ├─ Type = Credit Note?
│  │  └─ YES → Branch to Credit Note workflow
│  │           → END (Credit Note Path)
│  │
│  └─ Other Type?
│     └─ YES → Branch to appropriate workflow
│              → END (Other Type Path)
│
├─ LEVEL 3: URGENCY CHECK (for Invoices)
│  │
│  ├─ Urgent Flag = TRUE?
│  │  │
│  │  ├─ YES → Expedited Workflow
│  │  │        Priority: URGENT
│  │  │        Deadline: 1 day
│  │  │        Assign to: Senior Approver
│  │  │        → END (Expedited Path)
│  │  │
│  │  └─ NO → Continue to Level 4
│
├─ LEVEL 4: AMOUNT THRESHOLDS
│  │
│  ├─ Amount < €1,000?
│  │  │
│  │  ├─ YES → AUTO-APPROVE PATH
│  │  │        Set Approval_Type = "AUTO"
│  │  │        Approve immediately
│  │  │        Export to ERP
│  │  │        → END (Auto-Approved)
│  │  │
│  │  └─ NO → Continue
│  │
│  ├─ Amount < €10,000?
│  │  │
│  │  ├─ YES → MANAGER APPROVAL PATH
│  │  │        Create task for Manager
│  │  │        Priority: Medium
│  │  │        Deadline: 3 days
│  │  │        → WAIT for approval
│  │  │           → END (Manager Path)
│  │  │
│  │  └─ NO → Continue
│  │
│  ├─ Amount < €50,000?
│  │  │
│  │  ├─ YES → DIRECTOR APPROVAL PATH
│  │  │        Continue to Level 5 (Supplier Check)
│  │  │
│  │  └─ NO → Continue
│  │
│  └─ Amount ≥ €50,000?
│     │
│     └─ YES → EXECUTIVE APPROVAL PATH
│              Create sequential tasks:
│              - Finance Director
│              - CFO
│              - CEO (if > €100,000)
│              Priority: URGENT
│              Deadline: 1 day each
│              → WAIT for all approvals
│                 → END (Executive Path)
│
├─ LEVEL 5: SUPPLIER ANALYSIS (for €10k-€50k range)
│  │
│  ├─ Supplier Status = "BLOCKED"?
│  │  │
│  │  ├─ YES → BLOCK & ESCALATE
│  │  │        Stop processing
│  │  │        Create urgent task
│  │  │        Notify procurement & finance
│  │  │        → END (Blocked Supplier)
│  │  │
│  │  └─ NO → Continue
│  │
│  ├─ Supplier Age < 180 days (New)?
│  │  │
│  │  ├─ YES → DUAL APPROVAL REQUIRED
│  │  │        Task 1: Director (2 days)
│  │  │        → WAIT for Task 1
│  │  │           IF Task 1 Approved:
│  │  │             Task 2: CFO (2 days)
│  │  │             → WAIT for Task 2
│  │  │                → END (Dual Approved)
│  │  │           IF Task 1 Rejected:
│  │  │             → END (Rejected at Level 1)
│  │  │
│  │  └─ NO → Continue
│  │
│  ├─ Supplier Risk Rating = "HIGH"?
│  │  │
│  │  ├─ YES → ENHANCED APPROVAL
│  │  │        Additional fraud checks
│  │  │        Director approval required
│  │  │        Extended deadline
│  │  │        → END (Enhanced Path)
│  │  │
│  │  └─ NO → STANDARD DIRECTOR APPROVAL
│  │           Create task for Director
│  │           Priority: High
│  │           Deadline: 2 days
│  │           → WAIT for approval
│  │              → END (Standard High-Value)
│  │
│  └─ [Supplier analysis complete]
│
└─ [All decision levels processed]
```

---

## Buenas prácticas de configuración

### 1. Mantenga la lógica clara y mantenible

✅ **Bien:**
```
IF Amount > 10000:
  → High value path
ELSE:
  → Standard path
```

❌ **Mal (demasiado complejo):**
```
IF (Amount > 10000 AND (Supplier = "A" OR Supplier = "B") AND NOT (Status = "X" OR Status = "Y") AND Department IN [1,2,3]):
  → Complex path
```

**Mejor: divídalo en pasos:**
```
Step 1: IF Amount > 10000: Continue, ELSE: Standard path
Step 2: IF Supplier in allowed list: Continue, ELSE: Review
Step 3: IF Status valid: Continue, ELSE: Reject
Step 4: IF Department authorized: Approve, ELSE: Escalate
```

---

### 2. Documente la lógica de decisión

**Incluya siempre:**
- El propósito de cada punto de decisión
- La regla de negocio que se implementa
- Los resultados esperados
- La gestión de excepciones

**Ejemplo de documentación:**
```
Decision Point: Amount Threshold Check
Business Rule: BR-INV-001 (Invoice Approval Matrix)
Purpose: Route invoices based on amount thresholds per company policy
Thresholds:
  < €1,000: Auto-approve (CFO approved threshold)
  €1,000-€10,000: Manager approval (Delegation matrix)
  > €10,000: Director approval (Signature authority)
Exceptions: Urgent invoices skip to highest level
Updated: 2025-10-23
Owner: Finance Department
```

---

### 3. Pruebe todas las rutas

**Matriz de pruebas:**

| Caso de prueba | Importe | Tipo | Proveedor | Ruta esperada | Estado |
|-----------|--------|------|----------|---------------|--------|
| TC1 | 500 € | Invoice | Existing | Auto-approve | ✅ |
| TC2 | 5.000 € | Invoice | Existing | Manager | ✅ |
| TC3 | 15.000 € | Invoice | New | Director+CFO | ✅ |
| TC4 | 60.000 € | Invoice | Existing | Executive | ✅ |
| TC5 | 2.000 € | Credit Note | Existing | Credit workflow | ✅ |
| TC6 | 100.000 € | Invoice | Blocked | Stop & Escalate | ✅ |

---

### 4. Supervise las métricas de decisión

**Haga seguimiento de:**
- La distribución entre las rutas de decisión
- La tasa de aprobación automática
- La tasa de revisión manual
- El tiempo medio de procesamiento por ruta
- Las tasas de excepción
- La utilización de cada ruta

**Ejemplo de métricas:**
```
Month: October 2025
Total Invoices: 1,250

Decision Path Distribution:
- Auto-approved (< €1k): 680 (54%)
- Manager path (€1k-€10k): 420 (34%)
- Director path (€10k-€50k): 120 (10%)
- Executive path (> €50k): 30 (2%)

Processing Time:
- Auto-approve: < 1 minute
- Manager path: 2.5 days average
- Director path: 1.8 days average
- Executive path: 3.2 days average

Exceptions: 15 (1.2%)
```

---

## Patrones relacionados

### Patrones que funcionan bien juntos:

- **[Patrón de gestión de tareas](task-management-pattern.md)** - Crea tareas según las decisiones
- **[Patrón de integración de API](api-integration-pattern.md)** - Obtiene datos para la toma de decisiones
- **[Patrón de cotejo de PO](po-matching-pattern.md)** - Usa los resultados de PO en las decisiones
- **[Patrón de transformación de datos](data-transformation-pattern.md)** - Transforma los datos antes de las decisiones

---

## Guías relacionadas

### Requisitos previos
- [Guía completa de tarjetas de condición](../and/condition-cards-complete-guide.md) - Todas las tarjetas de condición
- [Guía de manipulación de campos](../then/document-field/field-manipulation-guide.md) - Operaciones con campos
- [Guía de asignación a usuario](../then/assignee/assignment-user-guide.md) - Lógica de enrutamiento

### Tarjetas relacionadas
- **CONDITION_DOC_FIELD_AMOUNT** - [Guía de tarjetas de condición](../and/condition-cards-complete-guide.md#field-conditions)
- **CONDITION_DOC_TYPE_IS_ISNOT** - [Guía de tarjetas de condición](../and/condition-cards-complete-guide.md#condition-doc-type-is-isnot)
- **CONDITION_SUPPLIER_STATUS_IS_ISNOT** - [Guía de tarjetas de condición](../and/condition-cards-complete-guide.md#condition-supplier-status-is-isnot)
- **ACTION_ASSIGN_TO_USER** - [Guía de asignación](../then/assignee/assignment-user-guide.md)
- **tasks_create** - [Guía de asignación de tareas](../then/task/task-assignment-guide.md)

### Próximos pasos
- Crear tareas: [Patrón de gestión de tareas](task-management-pattern.md)
- Añadir cotejo complejo: [Patrón de cotejo de PO](po-matching-pattern.md)
- Integrar API: [Patrón de integración de API](api-integration-pattern.md)

---

**Versión del patrón:** 1.0
**Última actualización:** 23 de octubre de 2025
**Dificultad:** Media
**Tiempo estimado:** 30-45 minutos
**Tasa de éxito:** Alta
