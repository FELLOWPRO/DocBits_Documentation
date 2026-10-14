# Task Management Pattern

**Tipo di pattern:** Gestione dei workflow
**Complessità:** Bassa-Media
**Configurazione stimata:** 30-45 minuti
**Casi d'uso comuni:** Workflow di approvazione, task di revisione, gestione delle eccezioni, escalation

---

Costruisci questo pattern nel **Workflow Builder** (Workflow Dashboard → Workflow List → Add Workflow). Clicca **Add Card** per aprire la libreria delle card e scegli le card usate da questo pattern — `tasks_create`, `ACTION_ASSIGN_TO_USER`, `ACTION_SEND_EMAIL_TO_GROUPS` e `CONDITION_TASK_STATUS` (la categoria **Assignee** contiene le card di task e assegnazione):

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Libreria Add Card nel Workflow Builder, raggruppata per categoria"><figcaption><p>La libreria <strong>Add Card</strong> — le card di task, assegnazione e notifica si trovano nelle categorie <strong>Assignee</strong> e <strong>Status</strong>.</p></figcaption></figure>

---

## Panoramica del pattern

Questo pattern mostra come creare, assegnare, monitorare e gestire i task all'interno dei workflow di DocBits. I task sono elementi di lavoro azionabili assegnati a utenti o gruppi che richiedono il completamento prima che il workflow del documento possa proseguire.

**Cosa fa questo pattern:**
1. Crea task in base alle condizioni del workflow
2. Assegna i task agli utenti o ai gruppi appropriati
3. Imposta le proprietà del task (priorità, scadenza, descrizione)
4. Invia notifiche quando i task vengono creati
5. Monitora lo stato e il completamento dei task
6. Instrada i documenti in base agli esiti dei task

---

## Quando usare questo pattern

Usa questo pattern quando devi:
- ✅ Creare workflow di approvazione
- ✅ Assegnare task di revisione agli utenti
- ✅ Gestire le eccezioni che richiedono intervento umano
- ✅ Inoltrare i problemi ai manager
- ✅ Creare catene di approvazione multi-livello
- ✅ Monitorare chi deve fare cosa
- ✅ Impostare scadenze per le azioni

**Non usare questo pattern quando:**
- ❌ Non è richiesta alcuna azione umana (usa invece l'elaborazione automatica)
- ❌ Devi solo notificare (usa invece l'email)
- ❌ Semplice instradamento dei documenti (usa invece l'assegnazione)

---

## Esempio completo di workflow

### Scenario: Approvazione delle fatture con instradamento basato sull'importo

**Requisito aziendale:**
- Fatture < €1.000: Approvazione automatica (nessun task necessario)
- Fatture €1.000-€10.000: Task di approvazione al Manager
- Fatture > €10.000: Doppia approvazione (Manager + Director)
- Tutti gli approvatori ricevono una notifica via email
- I task hanno una scadenza di 3 giorni

**Card di workflow utilizzate:**
1. CONDITION_DOC_FIELD_AMOUNT - Verifica l'importo della fattura
2. tasks_create - Crea il task di approvazione
3. ACTION_ASSIGN_TO_USER - Assegna il task all'approvatore
4. ACTION_SEND_EMAIL_TO_GROUPS - Invia la notifica
5. CONDITION_TASK_STATUS - Verifica se il task è completato
6. ACTION_APPROVE_DOCUMENT - Approva dopo il completamento del task

---

## Implementazione passo passo

### Passo 1: Verifica la soglia di importo

**Card:** CONDITION_DOC_FIELD_AMOUNT o condizione di campo simile

**Configurazione per il Percorso 1 (< €1.000):**
```
Field: Total_Amount
Operator: IS LESS THAN
Value: 1000
Currency: EUR
```

**Configurazione per il Percorso 2 (€1.000-€10.000):**
```
Field: Total_Amount
Operator: IS BETWEEN
Value Min: 1000
Value Max: 10000
Currency: EUR
```

**Configurazione per il Percorso 3 (> €10.000):**
```
Field: Total_Amount
Operator: IS GREATER THAN
Value: 10000
Currency: EUR
```

**Riferimento alla guida:** [Condition Cards Guide](../and/condition-cards-complete-guide.md)

---

### Passo 2A: Approva automaticamente le fatture di piccolo importo (< €1.000)

**Nessun task necessario per gli importi piccoli**

**Card:**
- ACTION_SET_FIELD_TO_TEXT
  - Imposta "Approval_Type" = "AUTO"
  - Imposta "Approval_Reason" = "Amount below threshold"
- ACTION_APPROVE_DOCUMENT

**Risultato:** Documento approvato automaticamente, nessun task creato

---

### Passo 2B: Crea il task di approvazione del Manager (€1.000-€10.000)

**Card:** tasks_create (v4 consigliata)

**Configurazione:**
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

**Mappatura dei campi:**
- `{{DOCUMENT_NUMBER}}` - ID documento automatico
- `{{Total_Amount}}` - Campo: Total_Amount
- `{{Supplier_Name}}` - Campo: Supplier_Name
- `{{Invoice_Number}}` - Campo: Invoice_Number
- `{{Invoice_Date}}` - Campo: Invoice_Date
- `{{Approving_Manager}}` - Campo o utente fisso

**Riferimento alla guida:** [Task Assignment Guide](../then/task/task-assignment-guide.md)

---

### Passo 2C: Crea i task di doppia approvazione (> €10.000)

**Due task sequenziali per le fatture di valore elevato**

**Task 1: Approvazione del Manager**
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

**Task 2: Approvazione del Director (creato dopo il completamento del Task 1)**
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

### Passo 3: Assegna il task a un utente/gruppo

**Card:** ACTION_ASSIGN_TO_USER o ACTION_ASSIGN_TO_GROUP

**Opzione 1: Assegna a un utente specifico**
```
User: John.Smith@company.com
OR
User Field: {{DOCUMENT_FIELD:Approving_Manager}}
```

**Opzione 2: Assegna a un gruppo**
```
Group: Finance Managers
Assignment Mode: First Available
OR
Assignment Mode: Round Robin
OR
Assignment Mode: All (everyone in group gets task)
```

**Opzione 3: Assegnazione sequenziale**
```
Card: ACTION_ASSIGN_SEQUENTIALLY_TO_USER

User 1: Finance_Manager
User 2: Finance_Director (only if User 1 approves)
User 3: CFO (only if User 2 approves)
```

**Riferimento alla guida:** [Assignment User Guide](../then/assignee/assignment-user-guide.md)

---

### Passo 4: Invia la notifica via email

**Card:** ACTION_SEND_EMAIL_TO_GROUPS

**Configurazione:**
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

**Variabili dell'email:**
- `{{TASK_ASSIGNEE_EMAIL}}` - Email dell'assegnatario del task
- `{{TASK_ASSIGNEE_NAME}}` - Nome dell'assegnatario del task
- `{{DOCUMENT_NUMBER}}` - ID documento
- `{{TASK_DEADLINE}}` - Data di scadenza del task
- `{{TASK_PRIORITY}}` - Livello di priorità del task
- `{{DOCUMENT_LINK}}` - Link diretto al documento

**Riferimento alla guida:** [Send Email Groups Guide](../then/action/send-email-groups-guide.md)

---

### Passo 5: Monitora lo stato del task

**Card:** CONDITION_TASK_STATUS o controllo di stato del task simile

**Configurazione:**
```
Task ID: {{CREATED_TASK_ID}}
Status Check: IS COMPLETED
```

**Opzioni di stato:**
- CREATED - Task appena creato
- ASSIGNED - Task assegnato a un utente
- IN_PROGRESS - L'utente ha iniziato a lavorare sul task
- COMPLETED - Task terminato
- APPROVED - Task approvato
- REJECTED - Task rifiutato
- CANCELLED - Task annullato
- OVERDUE - Task oltre la scadenza

**Logica:**
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

### Passo 6: Completa il workflow in base al risultato del task

**Dopo il completamento del task:**

**Scenario A: Task approvato**
```
1. Set field "Approval_Status" = "APPROVED"
2. Set field "Approved_By" = {{TASK_COMPLETED_BY}}
3. Set field "Approval_Date" = {{TASK_COMPLETED_DATE}}
4. ACTION_APPROVE_DOCUMENT
5. Export document (if configured)
```

**Scenario B: Task rifiutato**
```
1. Set field "Approval_Status" = "REJECTED"
2. Set field "Rejected_By" = {{TASK_COMPLETED_BY}}
3. Set field "Rejection_Reason" = {{TASK_REJECTION_REASON}}
4. ACTION_REJECT_DOCUMENT
5. Send rejection notification to supplier
6. Create "Correction Needed" task
```

**Scenario C: Task in ritardo**
```
1. Set field "Task_Status" = "OVERDUE"
2. Create escalation task for manager
3. Send reminder email to original assignee
4. Send escalation email to manager
5. Log overdue event
```

---

## Diagramma completo del workflow

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

## Modelli di configurazione

### Modello 1: Task di approvazione semplice

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

### Modello 2: Task di revisione con dettagli

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

### Modello 3: Task di escalation

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

## Pattern avanzati

### Pattern 1: Approvazione sequenziale multi-livello

**Uso:** Le fatture devono passare attraverso più approvatori in sequenza

```
Level 1: Accounts Clerk (verify data)
  → IF APPROVED:
    Level 2: Accounts Manager (approve amount)
      → IF APPROVED:
        Level 3: Finance Director (final sign-off)
          → IF APPROVED:
            Document Approved ✅
```

**Implementazione:**
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

### Pattern 2: Approvazione parallela di più approvatori

**Uso:** Più persone devono approvare simultaneamente

```
Send to ALL approvers at once:
- Finance Manager
- Procurement Manager
- Quality Manager

Document approved only when ALL approve
```

**Implementazione:**
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

### Pattern 3: Creazione condizionale dei task

**Uso:** Creare task diversi in base alle condizioni

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

### Pattern 4: Escalation basata sulla scadenza

**Uso:** Escalation automatica se il task non viene completato in tempo

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

## Gestione degli errori

### Scenario 1: Assegnatario non trovato

**Problema:** L'utente non esiste o è inattivo

**Soluzione:**
```
1. Check user status with CONDITION_USER_IS_ISNOT
2. IF User = INACTIVE:
     → Assign to backup user
     → OR Assign to user's group
     → Log warning
3. Send notification to admin
```

---

### Scenario 2: Creazione del task fallita

**Problema:** Errore di sistema nella creazione del task

**Soluzione:**
```
1. Check task creation status
2. IF Failed:
     → Retry task creation
     → Send email notification instead
     → Create admin alert task
     → Log error details
```

---

### Scenario 3: Nessuna risposta al task

**Problema:** L'utente non completa il task entro la scadenza

**Soluzione:**
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

## Checklist di test

- [ ] Task creato con successo
- [ ] Task assegnato all'utente/gruppo corretto
- [ ] Notifica via email inviata
- [ ] Il task compare nell'elenco dei task dell'utente
- [ ] Proprietà del task corrette (titolo, descrizione, priorità, scadenza)
- [ ] L'utente può completare il task
- [ ] Il workflow continua dopo il completamento del task
- [ ] Il workflow di approvazione funziona correttamente
- [ ] Il workflow di rifiuto funziona correttamente
- [ ] L'escalation si attiva al momento giusto
- [ ] La gestione dei ritardi funziona
- [ ] Tutte le notifiche via email vengono inviate
- [ ] Gli aggiornamenti dei campi funzionano correttamente

---

## Esempi reali

### Esempio 1: Eccezione del matching a tre vie del PO

**Scenario:** La fattura non corrisponde al PO, necessita di revisione

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

### Esempio 2: Approvazione della fattura del fornitore

**Scenario:** La fattura di un nuovo fornitore necessita di un'approvazione speciale

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

### Esempio 3: Elaborazione di fine mese

**Scenario:** Le fatture di fine mese necessitano di elaborazione urgente

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

## Suggerimenti sulle prestazioni

✅ **Best practice:**
- Imposta scadenze realistiche
- Usa titoli e descrizioni dei task chiari
- Includi tutte le informazioni necessarie nel task
- Invia notifiche tempestive
- Monitora i tassi di completamento dei task
- Escalation automatica dei task in ritardo
- Registra tutte le attività dei task
- Esamina i pattern dei task mensilmente

❌ **Da evitare:**
- Creare task per qualsiasi cosa
- Descrizioni dei task vaghe
- Scadenze irrealistiche
- Troppe email di notifica
- Nessun percorso di escalation
- Ignorare i task in ritardo
- Non monitorare le metriche dei task

---

## Pattern correlati

### Pattern che funzionano bene insieme:

- **[API Integration Pattern](api-integration-pattern.md)** - Crea task per gli errori API
- **[PO Matching Pattern](po-matching-pattern.md)** - Crea task per le mancate corrispondenze del PO
- **[Decision Logic Pattern](decision-logic-pattern.md)** - Instrada al tipo di task appropriato
- **[Data Transformation Pattern](data-transformation-pattern.md)** - Trasforma i dati prima di creare il task

---

## Guide correlate

### Prerequisiti
- [Task Assignment Guide](../then/task/task-assignment-guide.md) - Documentazione della card di task
- [Assignment User Guide](../then/assignee/assignment-user-guide.md) - Assegnazione agli utenti
- [Send Email Groups Guide](../then/action/send-email-groups-guide.md) - Notifiche via email

### Card correlate
- **tasks_create** - [Task Assignment Guide](../then/task/task-assignment-guide.md)
- **ACTION_ASSIGN_TO_USER** - [Assignment Guide](../then/assignee/assignment-user-guide.md)
- **ACTION_SEND_EMAIL_TO_GROUPS** - [Email Guide](../then/action/send-email-groups-guide.md)
- **CONDITION_TASK_STATUS** - [Condition Cards Guide](../and/condition-cards-complete-guide.md)

### Prossimi passi
- Aggiungi le notifiche via email: [Send Email Guide](../then/action/send-email-groups-guide.md)
- Implementa l'instradamento complesso: [Decision Logic Pattern](decision-logic-pattern.md)
- Gestisci gli errori: [Error Handling Pattern](error-handling-pattern.md)

---

**Versione del pattern:** 1.0
**Ultimo aggiornamento:** 23 ottobre 2025
**Difficoltà:** Bassa-Media
**Tempo stimato:** 30-45 minuti
**Tasso di successo:** Molto alto
