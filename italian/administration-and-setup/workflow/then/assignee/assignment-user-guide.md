# Document Assignment & User Cards - Complete Guide

Queste schede vanno nel gruppo **Then** del Generatore di workflow — le azioni eseguite una volta soddisfatte le condizioni When/And:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Le schede vengono aggiunte al gruppo <strong>Then</strong> tramite <strong>Add Card</strong>.</p></figcaption></figure>

**Copre:** 13 card di assegnazione e relative agli utenti

---

## 📌 Informazioni sulla Versione

**Card Multi-Versione:** DOC_USER_ASSIGN (v2 la più recente, v3 deprecata), DOC_GROUP_ASSIGN (v2 la più recente, v3 deprecata), OC_ASSIGN_DOC (v2)

**Importante:** le versioni v3 hanno aggiunto il supporto al decision tree ma sono ora deprecate
**Raccomandazione:** usa v2 sia per DOC_USER_ASSIGN che per DOC_GROUP_ASSIGN

📖 [Cronologia Completa delle Versioni](../../../changelog/release.md#-assignment--routing-cards) | [Database delle Versioni delle Card](../../../../DocFlow/docs/card_version.md)

---

# Assegnazione di Base del Documento

## Card: DOC_USER_ASSIGN / Assign Document to User

### Scopo
Assegna il documento a una persona specifica per la sua azione

### Quando Usarla
- Il documento necessita della revisione di una persona specifica
- Passaggio di consegne a un singolo membro del team
- Tracciamento della responsabilità
- Assegnare il lavoro a una persona indicata

### Come Funziona
```
Document is "assigned to" = John Smith
Only John can see it as assigned to him
John is responsible for this document
```

### Esempio
```
Invoice arrives
    ↓
Assign Document to: John Smith (Finance Manager)
    ↓
Only John sees "Assigned to Me"
John must take action on it
```

### Parametri
```
User: [Select which person]
```

### Nota
Assegnare significa:
- Il documento appare come "assigned to me" per quella persona
- Quella persona è responsabile
- Gli altri possono comunque vedere il documento (ma non come assegnato a loro)
- Un'unica assegnazione alla volta per documento

---

## Card: DOC_GROUP_ASSIGN / Assign Document to Group

### Scopo
Assegna il documento a un gruppo (tutti i membri lo vedono come assegnato a loro)

### Quando Usarla
- Documento per un team, non per un singolo
- Più persone possono gestirlo
- Responsabilità condivisa
- Distribuzione del carico di lavoro del team

### Come Funziona
```
Document is "assigned to" = Finance Team (10 people)
All 10 team members see "Assigned to My Group"
Any team member can take action
```

### Esempio
```
New vendor invoice
    ↓
Assign Document to: Procurement Team
    ↓
All procurement team members see it
First available person handles it
```

### Parametri
```
Group: [Select which group]
```

### Differenza
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

## Card: ACTION_ASSIGN_DOC_BASED_ON_DECISION_TABLE

### Scopo
Assegna il documento in base alla logica della decision table

### Quando Usarla
- Fornitori diversi necessitano di responsabili diversi
- Assegnazione basata sull'importo
- Logica di instradamento complessa
- Più condizioni per l'assegnazione

### Come Funziona
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

### Esempio: Assegnazione Basata sull'Importo
```
Invoice: €2000 from ABC Corp

Decision Table checks:
  Is amount > €10000? NO
  Is amount > €5000? NO
  Is amount > €1000? YES

Result: Assign to: Finance Manager
```

### Esempio: Assegnazione Basata sul Fornitore
```
Invoice from: Preferred Supplier

Decision Table:
  If preferred supplier → Finance Team
  If new supplier → Procurement Manager
  If blacklisted → Director Review

Result: Assign to: Finance Team
```

### Parametri
```
Decision Table: [Select decision table]
(Decision table contains assignment logic)
```

---

## Card: ACTION_ASSIGN_DOC_DECISION_TABLE_SEQUENTIAL

### Scopo
Assegna il documento in sequenza in base alla decision table con priorità

### Quando Usarla
- Più approvazioni sequenziali
- Persone diverse a livelli diversi
- Catena di approvazione basata sull'importo
- Percorso di escalation

### Come Funziona
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

### Sistema di Priorità
```
Priority 1: First assignment
Priority 2: Second assignment
Priority 3: Third assignment
(etc.)

Each must complete before next begins
```

### Esempio: Approvazione a Più Livelli
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

### Parametri
```
Decision Table: [Select]
Priority Order: [Determined by decision table]
```

---

## Card: ACTION_ASSIGN_DOC_TO_USER_SEQUENTIAL

### Scopo
Assegna il documento a un utente con priorità sequenziale

### Quando Usarla
- Il documento necessita di una persona specifica
- Elaborazione sequenziale chiara
- Assegnazione singola con un ordine

### Come Funziona
```
Assign Document to: User A (Priority 1)
    ↓
User A processes
    ↓
Then: Assign to User B (Priority 2)
    ↓
User B processes
```

### Esempio
```
Invoice processing:
1. Assign to: Accounts Payable Clerk
2. Then: Assign to: Finance Manager
3. Then: Assign to: Director

Each person has their turn
```

---

## Card: ACTION_ASSIGN_DOC_TO_GROUP_SEQUENTIAL

### Scopo
Assegna il documento in sequenza a gruppi

### Quando Usarla
- Più approvazioni di gruppo
- Reparti diversi a ciascuna fase
- Elaborazione sequenziale basata sui team

### Come Funziona
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

### Esempio
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

## Card: ACTION_ASSIGN_DOC_TO_FACILITY_GROUP

### Scopo
Assegna il documento a uno specifico gruppo di sede

### Quando Usarla
- Documento per un magazzino/sede specifici
- Operazioni basate sulla sede
- Elaborazione specifica per posizione

### Esempio
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

## Card: ACTION_ASSIGN_DOC_TO_FACILITY_GROUP_SEQUENTIAL

### Scopo
Assegna in sequenza tra le sedi

### Quando Usarla
- Elaborazione multi-sede
- La spedizione attraversa più sedi
- Workflow basato sulla posizione

### Esempio
```
Manufacturing Order:

Step 1: Factory A (Manufacturing) - Build product
Step 2: Quality Center (Testing) - Test product
Step 3: Distribution Center (Packing) - Package
Step 4: Warehouse (Storage) - Store

Document/shipment passes through each
```

---

## Card: ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP

### Scopo
Assegna il documento al reparto di approvvigionamento

### Quando Usarla
- Gestione da parte del team di approvvigionamento
- Lavoro relativo ai fornitori
- Relativo agli ordini di acquisto

### Esempio
```
Vendor evaluation document
    ↓
Assign to: Procurement Group
    ↓
Procurement team evaluates vendor
```

---

## Card: ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP_SEQUENTIAL

### Scopo
Assegnazione sequenziale all'interno dell'approvvigionamento

### Quando Usarla
- Processo di approvvigionamento a più fasi
- Catena di approvazione nell'approvvigionamento

### Esempio
```
Purchase Requisition:

Step 1: Buyer (Creates PO)
Step 2: Approver (Reviews)
Step 3: Director (Final sign-off)

Each step in sequence
```

---

## Card: ACTION_CHANGE_DOC_SUBORG / Change Document Sub-Organization

### Scopo
Assegna il documento a una sotto-organizzazione diversa

### Quando Usarla
- Organizzazione errata selezionata
- Necessità di spostarlo al reparto corretto
- Ristrutturazione organizzativa

### Come Funziona
```
Current Sub-Org: Finance Department
    ↓
Change to: Accounting Department
    ↓
Document now belongs to Accounting
```

### Esempio
```
Document for: Berlin Office
    ↓
Realize should be: Munich Office
    ↓
Change Sub-Organization to: Munich Office
```

---

## Card: ACTION_CHANGE_DOC_SUBORG_BY_FIELD_TEXT

### Scopo
Cambia la sotto-organizzazione in base al valore di un campo del documento

### Quando Usarla
- Sotto-organizzazione memorizzata in un campo
- Abbinare la posizione del documento al campo
- Assegnazione automatica dell'organizzazione

### Come Funziona
```
Document Field: "Delivery_Location" = "Berlin"
    ↓
Decision Table:
  If location = "Berlin" → Assign to: Berlin Sub-Org
  If location = "Munich" → Assign to: Munich Sub-Org

    ↓
Document assigned to: Berlin Sub-Org
```

### Esempio
```
Invoice field: "Cost Center: CC-Berlin-001"
    ↓
System recognizes: Berlin location
    ↓
Change document to: Berlin Sub-Organization
```

---

## Card: ACTION_ASSIGN_USER_FROM_FIELD_WITH_FALLBACK

### Scopo
Assegna il documento a un utente ricavato da un campo, con fallback se l'utente non viene trovato

### Quando Usarla
- Il nome utente è memorizzato in un campo del documento
- Potrebbe non esistere nel sistema
- Serve una riserva nel caso l'utente non sia disponibile

### Come Funziona
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

### Parametri
```
Source Field: [Field containing user name]
Fallback User: [If source user not found]
```

### Esempio
```
Invoice has field: "Contact Person: Mike Johnson"

Try to assign to: Mike Johnson
    ↓
If Mike not in system:
    ↓
Fallback to: Finance Manager (Robert)
```

---

## Card: ACTION_ASSIGN_USER_TO_SUPPLIER

### Scopo
Assegna il documento all'utente che gestisce quel fornitore

### Quando Usarla
- Utente collegato a un fornitore
- Account manager del fornitore
- Responsabile della relazione con il fornitore

### Come Funziona
```
Document Supplier: ABC Corp
    ↓
System checks: Who manages ABC Corp?
    ↓
Assign to: John Smith (ABC Corp Account Manager)
```

---

# Decision Tree di Assegnazione

## Esempio di Decision Table 1: Basato sull'Importo
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

## Esempio di Decision Table 2: Basato sul Fornitore
```
Supplier Type = "Preferred"
  → Assign to: Account Manager

Supplier Type = "New"
  → Assign to: Procurement Manager

Supplier Type = "Problem"
  → Assign to: Procurement Director
```

## Esempio di Decision Table 3: Basato sul Tipo di Documento
```
Document Type = "Invoice"
  → Assign to: Accounts Payable Team

Document Type = "Credit Memo"
  → Assign to: Finance Manager

Document Type = "PO"
  → Assign to: Procurement Team
```

---

# Esempi di Workflow di Assegnazione

## Esempio 1: Instradamento Semplice
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

## Esempio 2: Approvazione Sequenziale
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

## Esempio 3: Instradamento Basato sull'Importo
```
Invoice: €50,000
    ↓
Decision Table: Amount > €20k?
    ↓
YES → Assign to: CFO
    ↓
CFO approves directly
```

## Esempio 4: Basato sulla Sede
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

# Best Practice per l'Assegnazione

✅ **Fai:**
- Mantieni semplici le decision table
- Testa la logica di instradamento con dati di esempio
- Assicurati che tutti i percorsi portino da qualche parte
- Predisponi un fallback per gli utenti mancanti
- Documenta le decisioni di instradamento

❌ **Non Fare:**
- Creare assegnazioni circolari (A→B→A)
- Assegnare a utenti inesistenti (senza fallback)
- Rendere l'instradamento troppo complesso
- Dimenticare di testare l'instradamento
- Assegnare a persone non disponibili

---

# Risoluzione dei Problemi di Assegnazione

## "Document not assigned"
**Causa:** condizione non soddisfatta o l'utente non esiste

**Soluzione:**
- Verifica che la condizione sia vera
- Verifica che l'utente esista nel sistema
- Controlla le impostazioni di fallback
- Rivedi la logica della decision table

## "Wrong person assigned"
**Causa:** decision table o logica di instradamento errata

**Soluzione:**
- Testa la decision table
- Controlla le condizioni
- Verifica la mappatura degli utenti
- Rivedi i valori dei campi

## "Assignment seems to skip someone"
**Causa:** ordine sequenziale errato

**Soluzione:**
- Controlla i numeri di priorità
- Verifica che la sequenza sia corretta
- Testa con un documento di esempio
- Rivedi l'ordinamento della decision table

---

# Confronto tra le Card di Assegnazione

| Card | Assegna a | Tipo di Instradamento | Caso d'Uso |
|------|-----------|-----------|----------|
| DOC_USER_ASSIGN | Individual | Direct | Simple assignment |
| DOC_GROUP_ASSIGN | Group | Direct | Team assignment |
| ACTION_ASSIGN_DOC_BASED_ON_DECISION_TABLE | Decision Result | Conditional | Complex routing |
| ACTION_ASSIGN_DOC_DECISION_TABLE_SEQUENTIAL | Multiple (Sequential) | Conditional | Approval chain |
| ACTION_ASSIGN_DOC_TO_USER_SEQUENTIAL | User (Sequential) | Ordered | Sequential user steps |
| ACTION_ASSIGN_DOC_TO_GROUP_SEQUENTIAL | Groups (Sequential) | Ordered | Sequential group steps |
| ACTION_ASSIGN_DOC_TO_FACILITY_GROUP | Facility Group | Direct | Facility-specific |
| ACTION_ASSIGN_DOC_TO_FACILITY_GROUP_SEQUENTIAL | Facilities (Sequential) | Ordered | Multi-facility |
| ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP | Procurement | Direct | Procurement workflow |
| ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP_SEQUENTIAL | Procurement (Sequential) | Ordered | Procurement approval chain |
| ACTION_CHANGE_DOC_SUBORG | Sub-Organization | Direct | Department change |
| ACTION_CHANGE_DOC_SUBORG_BY_FIELD_TEXT | Sub-Org by Field | Conditional | Field-based assignment |
| ACTION_ASSIGN_USER_FROM_FIELD_WITH_FALLBACK | Field/Fallback | Conditional | Dynamic user assignment |

---

# Card Correlate

- **ACTION_CREATE_TASK_FOR_USER** - Assegna un'attività alla stessa persona
- **ACTION_SEND_EMAIL** - Notifica la persona assegnata
- **CONDITION_USER_IS_ISNOT** - Verifica se è assegnata la persona corretta
- **CONDITION_GROUP_IS_ISNOT** - Verifica se è assegnato il gruppo corretto
