# Decision Logic Pattern

**Tipo di pattern:** Instradamento condizionale e logica
**Complessità:** Media
**Configurazione stimata:** 30-45 minuti
**Casi d'uso comuni:** Instradamento multi-percorso, elaborazione condizionale, alberi decisionali, implementazione di regole aziendali

---

Costruisci questo pattern nel **Workflow Builder** (Workflow Dashboard → Workflow List → Add Workflow). Clicca **Add Card** e apri la categoria **Logic** — contiene le card di condizione e di ramificazione che guidano l'albero decisionale, che combini con il gruppo **And** per valutare più condizioni:

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Libreria Add Card nel Workflow Builder, raggruppata per categoria"><figcaption><p>La libreria <strong>Add Card</strong> — le card di condizione e di ramificazione si trovano nella categoria <strong>Logic</strong>.</p></figcaption></figure>

---

## Panoramica del pattern

Questo pattern mostra come implementare una logica decisionale complessa nei workflow di DocBits usando le card di condizione per instradare i documenti attraverso percorsi di elaborazione diversi in base agli attributi del documento, ai valori dei campi e alle regole aziendali.

**Cosa fa questo pattern:**
1. Valuta più condizioni in sequenza o in parallelo
2. Instrada i documenti verso percorsi diversi in base alle condizioni
3. Implementa regole e policy aziendali
4. Gestisce alberi decisionali complessi
5. Combina più criteri per le decisioni di instradamento

---

## Quando usare questo pattern

Usa questo pattern quando devi:
- ✅ Instradare i documenti per soglie di importo
- ✅ Applicare regole diverse per tipi di documento diversi
- ✅ Implementare logica di approvazione multi-livello
- ✅ Gestire policy aziendali complesse
- ✅ Creare instradamento dinamico basato su più criteri
- ✅ Implementare la logica di gestione delle eccezioni
- ✅ Creare matrici di approvazione

**Non usare questo pattern quando:**
- ❌ Un semplice workflow lineare è sufficiente
- ❌ Tutti i documenti seguono lo stesso percorso
- ❌ Non è necessaria alcuna elaborazione condizionale

---

## Tipi di logica decisionale

### 1. Logica IF-THEN semplice

```
IF condition:
  → Action A
ELSE:
  → Action B
```

**Esempio:**
```
IF Amount > €10,000:
  → Assign to Director
ELSE:
  → Assign to Manager
```

### 2. Criteri multipli (logica AND)

```
IF condition1 AND condition2 AND condition3:
  → Action A
ELSE:
  → Action B
```

**Esempio:**
```
IF Amount > €10,000 AND Supplier = "New" AND Department = "IT":
  → Assign to IT Director + CFO (dual approval)
ELSE:
  → Standard approval workflow
```

### 3. Criteri alternativi (logica OR)

```
IF condition1 OR condition2 OR condition3:
  → Action A
ELSE:
  → Action B
```

**Esempio:**
```
IF Amount > €50,000 OR Supplier is "Blocked" OR Document has "Urgent" flag:
  → Escalate immediately
ELSE:
  → Standard processing
```

### 4. Albero decisionale annidato

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

**Esempio:**
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

## Esempio completo di workflow

### Scenario: Matrice di approvazione delle fatture

**Regole aziendali:**
1. Importo < €1.000: Approvazione automatica
2. Importo €1.000-€10.000: Approvazione del Manager
3. Importo > €10.000 E nuovo fornitore: Approvazione del Director + CFO
4. Importo > €10.000 E fornitore esistente: Solo approvazione del Director
5. Qualsiasi importo con mancata corrispondenza del PO: Prima approvazione degli approvvigionamenti
6. Fatture urgenti (contrassegnate): Workflow accelerato

**Implementazione:**

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

## Implementazione passo passo

### Passo 1: Definisci le card di condizione

**Condizione 1: Soglia di importo**
```
Card: CONDITION_DOC_FIELD_AMOUNT
Field: Total_Amount
Operator: IS LESS THAN
Value: 1000
Currency: EUR
```

**Condizione 2: Verifica del tipo di documento**
```
Card: CONDITION_DOC_TYPE_IS_ISNOT
Document Type: IS
Type: Invoice
```

**Condizione 3: Stato del fornitore**
```
Card: CONDITION_SUPPLIER_STATUS_IS_ISNOT
Supplier Status: IS
Status: ACTIVE
```

**Condizione 4: Verifica del nuovo fornitore**
```
Card: CONDITION_DOC_FIELD_DATE
Field: Supplier_First_Transaction_Date
Operator: IS AFTER
Value: {{TODAY_MINUS_180_DAYS}}
```

**Riferimento alla guida:** [Condition Cards Complete Guide](../and/condition-cards-complete-guide.md)

---

### Passo 2: Costruisci l'albero decisionale

**Livello 1: Tipo di documento**
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

**Livello 2: Soglie di importo (per le fatture)**
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

**Livello 3: Analisi del fornitore (per le fatture di valore elevato)**
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

### Passo 3: Crea le azioni di instradamento

**Percorso A: Approvazione automatica (Importo < €1.000)**
```
Actions:
1. Set field "Approval_Type" = "AUTO"
2. Set field "Approval_Level" = "0"
3. ACTION_APPROVE_DOCUMENT
4. Export to ERP
5. Send confirmation email (optional)
```

**Percorso B: Approvazione del Manager (€1.000-€10.000)**
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

**Percorso C: Approvazione del Director (€10.000-€50.000)**
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

**Percorso D: Approvazione esecutiva (≥ €50.000)**
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

## Pattern avanzati di logica decisionale

### Pattern 1: Instradamento basato sul punteggio

**Calcola un punteggio di rischio e instrada di conseguenza:**

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

**Implementazione:**
```
1. ACTION_CALCULATE_FIELD: Calculate risk score
2. ACTION_SET_FIELD_TO_NUMBER: Store score
3. CONDITION_DOC_FIELD_NUMBER: Check score thresholds
4. Route based on score
```

---

### Pattern 2: Matrice basata sul reparto

**Regole di approvazione diverse per reparto:**

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

**Implementazione:**
```
1. Check Department field
2. Based on department, check amount threshold
3. Route to appropriate approver
4. Different thresholds per department
```

---

### Pattern 3: Logica basata sul tempo

**Regole diverse in base alla tempistica:**

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

### Pattern 4: Instradamento basato sulle eccezioni

**Instrada le eccezioni separatamente:**

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

## Diagramma completo della logica decisionale

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

## Best practice di configurazione

### 1. Mantieni la logica chiara e manutenibile

✅ **Buono:**
```
IF Amount > 10000:
  → High value path
ELSE:
  → Standard path
```

❌ **Cattivo (troppo complesso):**
```
IF (Amount > 10000 AND (Supplier = "A" OR Supplier = "B") AND NOT (Status = "X" OR Status = "Y") AND Department IN [1,2,3]):
  → Complex path
```

**Meglio: suddividi in passaggi:**
```
Step 1: IF Amount > 10000: Continue, ELSE: Standard path
Step 2: IF Supplier in allowed list: Continue, ELSE: Review
Step 3: IF Status valid: Continue, ELSE: Reject
Step 4: IF Department authorized: Approve, ELSE: Escalate
```

---

### 2. Documenta la logica decisionale

**Includi sempre:**
- Lo scopo di ogni punto decisionale
- La regola aziendale implementata
- Gli esiti attesi
- La gestione delle eccezioni

**Esempio di documentazione:**
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

### 3. Testa tutti i percorsi

**Matrice di test:**

| Caso di test | Importo | Tipo | Fornitore | Percorso atteso | Stato |
|-----------|--------|------|----------|---------------|--------|
| TC1 | €500 | Fattura | Esistente | Approvazione automatica | ✅ |
| TC2 | €5.000 | Fattura | Esistente | Manager | ✅ |
| TC3 | €15.000 | Fattura | Nuovo | Director+CFO | ✅ |
| TC4 | €60.000 | Fattura | Esistente | Esecutivo | ✅ |
| TC5 | €2.000 | Nota di credito | Esistente | Workflow note di credito | ✅ |
| TC6 | €100.000 | Fattura | Bloccato | Stop & Escalate | ✅ |

---

### 4. Monitora le metriche decisionali

**Monitora:**
- Distribuzione tra i percorsi decisionali
- Tasso di approvazione automatica
- Tasso di revisione manuale
- Tempo medio di elaborazione per percorso
- Tassi di eccezione
- Utilizzo dei percorsi

**Esempio di metriche:**
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

## Pattern correlati

### Pattern che funzionano bene insieme:

- **[Task Management Pattern](task-management-pattern.md)** - Crea task in base alle decisioni
- **[API Integration Pattern](api-integration-pattern.md)** - Recupera dati per il processo decisionale
- **[PO Matching Pattern](po-matching-pattern.md)** - Usa i risultati del PO nelle decisioni
- **[Data Transformation Pattern](data-transformation-pattern.md)** - Trasforma i dati prima delle decisioni

---

## Guide correlate

### Prerequisiti
- [Condition Cards Complete Guide](../and/condition-cards-complete-guide.md) - Tutte le card di condizione
- [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md) - Operazioni sui campi
- [Assignment User Guide](../then/assignee/assignment-user-guide.md) - Logica di instradamento

### Card correlate
- **CONDITION_DOC_FIELD_AMOUNT** - [Condition Cards Guide](../and/condition-cards-complete-guide.md#field-conditions)
- **CONDITION_DOC_TYPE_IS_ISNOT** - [Condition Cards Guide](../and/condition-cards-complete-guide.md#condition-doc-type-is-isnot)
- **CONDITION_SUPPLIER_STATUS_IS_ISNOT** - [Condition Cards Guide](../and/condition-cards-complete-guide.md#condition-supplier-status-is-isnot)
- **ACTION_ASSIGN_TO_USER** - [Assignment Guide](../then/assignee/assignment-user-guide.md)
- **tasks_create** - [Task Assignment Guide](../then/task/task-assignment-guide.md)

### Prossimi passi
- Crea task: [Task Management Pattern](task-management-pattern.md)
- Aggiungi matching complesso: [PO Matching Pattern](po-matching-pattern.md)
- Integra le API: [API Integration Pattern](api-integration-pattern.md)

---

**Versione del pattern:** 1.0
**Ultimo aggiornamento:** 23 ottobre 2025
**Difficoltà:** Media
**Tempo stimato:** 30-45 minuti
**Tasso di successo:** Alto
