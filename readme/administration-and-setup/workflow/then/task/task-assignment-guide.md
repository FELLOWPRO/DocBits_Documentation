# Task Assignment & Creation Cards - Complete Guide

Queste schede vanno nel gruppo **Then** del Generatore di workflow — le azioni eseguite una volta soddisfatte le condizioni When/And:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Le schede vengono aggiunte al gruppo <strong>Then</strong> tramite <strong>Add Card</strong>.</p></figcaption></figure>

**Copre:** 12 card relative alle attività

---

## Panoramica

Le task card creano assegnazioni di lavoro per i membri del team. Quando una fattura necessita di approvazione, puoi creare automaticamente un'attività e assegnarla alla persona giusta.

---

# Creazione di Attività di Base

## Card: tasks_create / Create Task and Assign to User

### Scopo
Crea un'attività e la assegna a una persona specifica

### Quando Usarla
- La fattura necessita della revisione di una persona specifica
- È richiesta l'approvazione da parte di una persona indicata
- Passaggio di consegne a un membro specifico del team

### Parametri

**Title**
Il nome/oggetto dell'attività
```
Example: "Review Invoice #INV-2025-001 for approval"
```

**Description**
Dettagli sull'attività
```
Example: "Invoice from Supplier ABC needs review.
Amount: €5000
Deadline: 2025-10-30
Please verify pricing and quality."
```

**Priority**
- 🔴 **High**: urgente, da fare immediatamente
- 🟡 **Medium**: priorità normale
- 🟢 **Low**: può essere fatto in seguito

**Assigned User**
Chi riceve l'attività
```
Example: John Smith (Finance Manager)
```

**Email Notification**
Inviare un avviso email alla persona assegnata?
```
✅ Yes: Person gets email
❌ No: Task only in system
```

### Esempio
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

## Card: ACTION_TASK_FOR_GROUP / Create Task for Group

### Scopo
Crea un'attività e la assegna a un gruppo (tutti i membri possono vederla)

### Quando Usarla
- Più persone possono svolgere l'attività
- Attività per un team, non per un singolo
- La prima persona disponibile deve occuparsene

### Differenza dall'Attività Individuale
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

### Esempio di Workflow
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

## Card: ACTION_DECISION_TREE_CREATE_TASKS

### Scopo
Crea attività in base alla logica della decision table

### Come Funziona
```
Decision Table Returns:
  If invoice from Supplier A → Assign to Procurement
  If invoice from Supplier B → Assign to Quality Team
  If invoice from Supplier C → Assign to Finance

Task is automatically created and assigned
based on which condition is true
```

### Quando Usarla
- Fornitori diversi necessitano di approvazioni diverse
- Instradamento complesso basato su più fattori
- Team diverso in base al tipo di documento

### Esempio
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

## Card: ACTION_DECISION_TREE_TASKS_SEQUENTIAL

### Scopo
Crea attività in sequenza in base alla decision table
Le attività vengono assegnate una alla volta con un ordine di priorità

### Quando Usarla
- Sono necessarie più approvazioni in sequenza
- Catena di approvazione del workflow
- Ogni persona esamina e poi passa alla successiva

### Come Funziona
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

### Sistema di Priorità
```
Priority 1 → Assign to: Person A
Priority 2 → Assign to: Person B
Priority 3 → Assign to: Person C

They must complete in order (1→2→3)
```

### Esempio di Configurazione
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

## Card: ACTION_CREATE_TASK_FOR_USER_SEQUENTIAL

### Scopo
Assegna il documento a un utente E crea un'attività sequenziale

### Quando Usarla
- Assegnare il documento E creare un'attività contemporaneamente
- Il documento deve essere esaminato da una persona specifica
- Tracciare sia l'assegnazione che la creazione dell'attività

### Come Funziona
```
Two things happen:
1. Document is assigned to: Person A
2. Task is created for: Person A

Both in one action
```

### Esempio
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

## Card: ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL

### Scopo
Assegna il documento a un gruppo E crea un'attività

### Quando Usarla
- Il documento necessita dell'attenzione di un gruppo
- Vuoi tracciare la creazione dell'attività
- Creare un'attività iniziale e poi l'assegnazione del documento

### Esempio
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

# Creazione di Attività Avanzata

## Card: ACTION_ASSIGN_TASK_TO_FACILITY_GROUP

### Scopo
Crea un'attività per uno specifico gruppo di sede

### Quando Usarla
- Attività per il team di magazzino/sede
- Operazioni specifiche per sede
- Quando la posizione fisica è rilevante

### Esempio
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

## Card: ACTION_ASSIGN_TASK_TO_FACILITY_GROUP_SEQUENTIAL

### Scopo
Assegnazione sequenziale delle attività tra le sedi

### Quando Usarla
- Operazioni multi-sede
- Attività che passano da sede a sede
- Elaborazione sequenziale tra le sedi

### Come Funziona
```
Factory A (Step 1): Production
    ↓
Quality Check (Step 2): Verification
    ↓
Warehouse (Step 3): Packaging
    ↓
Shipping (Step 4): Dispatch
```

### Esempio
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

## Card: ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP

### Scopo
Crea un'attività per il reparto di approvvigionamento

### Quando Usarla
- Attività per il team di approvvigionamento
- Attività di gestione dei fornitori
- Lavoro relativo agli acquisti

### Esempio
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

## Card: ACTION_ASSIGN_TASK_PROCUREMENT_GROUP_SEQUENTIAL

### Scopo
Instradamento sequenziale delle attività all'interno dell'approvvigionamento

### Quando Usarla
- Processi di approvvigionamento a più fasi
- Catena di approvazione nell'approvvigionamento
- Percorso di escalation

### Esempio
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

## Card: ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK

### Scopo
Recupera l'utente da un campo del documento e assegna l'attività
Se l'utente non viene trovato, usa l'utente di fallback

### Quando Usarla
- L'utente è memorizzato in un campo del documento
- Il documento specifica chi deve effettuare la revisione
- Disponi di una persona di riserva nel caso l'utente specificato non sia disponibile

### Come Funziona
```
Document has field: "Approver Name: John Smith"

Card checks: Is John in system?
    If YES → Assign task to John
    If NO → Assign to Fallback User (Sarah)
```

### Esempio
```
Invoice field: "Contact: Mike Johnson"

Try to assign task to Mike Johnson
    ↓
If Mike doesn't exist in system:
    ↓
Use Fallback: Team Lead (Robert Brown)
```

### Parametri
```
- Field to Read: "Approver Name"
- Fallback User: Robert Brown
- Task Details: Title, Description, Priority
```

---

# Parametri Comuni delle Attività

Tutte le task card utilizzano questi parametri:

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

### Livelli di Priorità
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

### Due Date (se disponibile)
```
When should task be completed by?
Example: 2025-10-30 (5 days from now)
```

---

# Scenari di Workflow delle Attività

## Scenario 1: Approvazione Semplice
```
Invoice Arrives (€2000)
    ↓
Condition: Amount between €1000-€5000?
    ↓
YES: Create Task for Finance Manager
    ↓
Finance Manager reviews and approves
```

## Scenario 2: Approvazione a Più Livelli
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

## Scenario 3: Attività Parallele
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

## Scenario 4: Instradamento Condizionale
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

# Best Practice per l'Assegnazione delle Attività

✅ **Fai:**
- Includi dettagli specifici nel titolo dell'attività
- Imposta livelli di priorità appropriati
- Imposta scadenze realistiche
- Notifica gli assegnatari
- Includi un link al documento
- Usa descrizioni chiare e orientate all'azione

❌ **Non Fare:**
- Creare titoli di attività vaghi ("Review this")
- Impostare tutto con priorità High
- Dimenticare di notificare la persona assegnata
- Creare più attività per lo stesso lavoro
- Assegnare a persone non disponibili

---

# Risoluzione dei Problemi delle Attività

## "Task not assigned to anyone"
**Causa:** l'utente non esiste o il gruppo è vuoto

**Soluzione:**
- Verifica l'ortografia del nome utente
- Controlla che l'utente sia attivo nel sistema
- Verifica che il gruppo abbia membri
- Usa il fallback se necessario

## "Person says they didn't get notification"
**Causa:** notifica email disabilitata o email errata

**Soluzione:**
- Controlla che la casella "Send Email" sia abilitata
- Verifica l'indirizzo email del destinatario
- Controlla la cartella spam
- Reinvia manualmente la notifica

## "Wrong person got task"
**Causa:** logica di instradamento errata

**Soluzione:**
- Controlla le condizioni della decision table
- Verifica le impostazioni di fallback
- Testa con un documento di esempio
- Controlla eventuali errori di battitura nei nomi utente

## "Too many tasks created"
**Causa:** la card si attiva più volte

**Soluzione:**
- Controlla che le condizioni siano abbastanza specifiche
- Verifica che la card venga eseguita una sola volta per documento
- Rivedi le condizioni "And"
- Aggiungi ulteriori filtri

---

# Tabella di Confronto delle Task Card

| Card | Crea Attività | Assegna a | Quando |
|------|-------------|-----------|------|
| tasks_create | Yes | Individual | Always |
| ACTION_TASK_FOR_GROUP | Yes | Group | Always |
| ACTION_DECISION_TREE_CREATE_TASKS | Yes | Decision Table Result | Conditional |
| ACTION_DECISION_TREE_TASKS_SEQUENTIAL | Yes | Multiple (Sequential) | Conditional |
| ACTION_CREATE_TASK_FOR_USER_SEQUENTIAL | Yes | User + Document | Conditional |
| ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL | Yes | Group + Document | Conditional |
| ACTION_ASSIGN_TASK_TO_FACILITY_GROUP | Yes | Facility Group | Conditional |
| ACTION_ASSIGN_TASK_TO_FACILITY_GROUP_SEQUENTIAL | Yes | Multiple Facilities | Conditional |
| ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP | Yes | Procurement Team | Conditional |
| ACTION_ASSIGN_TASK_PROCUREMENT_GROUP_SEQUENTIAL | Yes | Multiple (Sequential) | Conditional |
| ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK | Yes | Field/Fallback | Conditional |

---

# Card Correlate

- **ACTION_ASSIGN_DOCUMENT_TO_USER** - Assegna il documento senza creare un'attività
- **ACTION_SEND_EMAIL** - Notifica direttamente le persone
- **STAUS_CHANGE** - Cambia lo stato invece di creare un'attività
- **RUN_WORKFLOW** - Attiva invece un workflow diverso
