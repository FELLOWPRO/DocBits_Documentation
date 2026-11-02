# Schede di assegnazione e creazione di compiti

## Schede di assegnazione e creazione di attività - Guida completa

**Copertine:** 12 carte relative ai compiti

***

Le schede attività in questa pagina vanno nel gruppo **Allora** del Workflow Builder: le azioni che vengono eseguite una volta che le condizioni Quando/E corrispondono:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-it.png" alt="Esempio non salvato con schede Quando, E e Allora. Configurare tutti i campi prima dell’esecuzione. Alcune etichette dell’interfaccia di questa versione sono ancora in inglese o tradotte in modo non corretto. Le spiegazioni di questa pagina sono tradotte; l’immagine mostra l’interfaccia reale."><figcaption><p>Esempio non salvato con schede Quando, E e Allora. Configurare tutti i campi prima dell’esecuzione. Alcune etichette dell’interfaccia di questa versione sono ancora in inglese o tradotte in modo non corretto. Le spiegazioni di questa pagina sono tradotte; l’immagine mostra l’interfaccia reale.</p></figcaption></figure>

***

### 📌 Informazioni sulla versione

**Carta più evoluta:** tasks\_create (4 versioni, v4 più recente) **Altre carte multiversione:** ACTION\_TASK\_FOR\_GROUP (v4), ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP (v3), ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK (v3), ACTION\_DECISION\_TREE\_CREATE\_TASKS (v3)

**Modifiche chiave:**

* **v3 → v4 Evoluzione:** Rimosso l'approccio dell'albero decisionale, aggiunti tipi di elementi di lavoro generici (Attività, Ticket, Problema)
* **v2 → Migrazione v3:** Aggiunto supporto per l'albero decisionale (ora per lo più deprecato)

📖 [Cronologia completa delle versioni](../../release.md) | [Versioni e comportamento delle carte](../../cards-overview/card-versions-guide.md)

***

### Panoramica

Le schede attività creano incarichi di lavoro per i membri del team. Quando una fattura necessita di approvazione, puoi creare automaticamente un'attività e assegnarla alla persona giusta.

***

## Creazione di attività di base

### Scheda: tasks\_create / Crea attività e assegna all'utente

#### Scopo

Crea un'attività e la assegna a una persona specifica

#### Quando usarlo

* La fattura necessita della revisione di una persona specifica
* È richiesta l'approvazione della persona nominata
* Trasferimento a un membro specifico del team

#### Parametri

**Titolo** Il nome/oggetto dell'attività

```
Example: "Review Invoice #INV-2025-001 for approval"
```

**Descrizione** Dettagli sull'attività

```
Example: "Invoice from Supplier ABC needs review.
Amount: €5000
Deadline: 2025-10-30
Please verify pricing and quality."
```

**Priorità**

* 🔴 **High**: Urgente, fallo subito
* 🟡 **Medio**: priorità normale
* 🟢 **Low**: può essere fatto più tardi

**Utente assegnato** Chi ottiene l'attività

```
Example: John Smith (Finance Manager)
```

**Notifica e-mail** Inviare un avviso e-mail alla persona assegnata?

```
✅ Yes: Person gets email
❌ No: Task only in system
```

#### Esempio

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

### Scheda: ACTION\_TASK\_FOR\_GROUP / Crea attività per gruppo

#### Scopo

Crea un'attività e la assegna a un gruppo (tutti i membri possono vederla)

#### Quando usarlo

* Più persone possono svolgere l'attività
* Compito di squadra, non individuale
* La prima persona disponibile dovrebbe occuparsene

#### Differenza dal compito individuale

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

#### Esempio di flusso di lavoro

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

### Carta: ACTION\_DECISION\_TREE\_CREATE\_TASKS

#### Scopo

Crea attività in base alla logica della tabella decisionale

#### Come funziona

```
Decision Table Returns:
  If invoice from Supplier A → Assign to Procurement
  If invoice from Supplier B → Assign to Quality Team
  If invoice from Supplier C → Assign to Finance

Task is automatically created and assigned
based on which condition is true
```

#### Quando usarlo

* Fornitori diversi necessitano di approvazioni diverse
* Routing complesso basato su molteplici fattori
* Team diversi in base al tipo di documento

#### Esempio

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

### Carta: ACTION\_DECISION\_TREE\_TASKS\_SEQUENTIAL

#### Scopo

Crea attività in sequenza in base alla tabella decisionale. Le attività vengono assegnate una alla volta in ordine di priorità

#### Quando usarlo

* Sono necessarie più approvazioni in sequenza
* Catena di approvazione del flusso di lavoro
* Ogni persona esamina e poi passa alla successiva

#### Come funziona

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

#### Sistema di priorità

```
Priority 1 → Assign to: Person A
Priority 2 → Assign to: Person B
Priority 3 → Assign to: Person C

They must complete in order (1→2→3)
```

#### Configurazione di esempio

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

### Carta: ACTION\_CREATE\_TASK\_FOR\_USER\_SEQUENTIAL

#### Scopo

Assegna il documento a un utente E crea attività sequenziali

#### Quando usarlo

* Assegna il documento E crea un'attività allo stesso tempo
* Il documento deve essere esaminato da una persona specifica
* Tieni traccia sia dell'assegnazione che della creazione dell'attività

#### Come funziona

```
Two things happen:
1. Document is assigned to: Person A
2. Task is created for: Person A

Both in one action
```

#### Esempio

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

### Carta: ACTION\_CREATE\_TASK\_FOR\_GROUP\_SEQUENTIAL

#### Scopo

Assegna il documento al gruppo E crea l'attività

#### Quando usarlo

* Il documento richiede l'attenzione del gruppo
* Vuoi tenere traccia della creazione dell'attività
* Creare l'attività iniziale e quindi documentare l'assegnazione

#### Esempio

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

## Creazione avanzata di attività

### Carta: ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP

#### Scopo

Crea un'attività per un gruppo di strutture specifico

#### Quando usarlo

* Compito per il team del magazzino/struttura
* Operazioni specifiche dell'impianto
* La posizione fisica conta

#### Esempio

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

### Carta: ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP\_SEQUENTIAL

#### Scopo

Assegnazione sequenziale delle attività tra le strutture

#### Quando usarlo

* Operazioni multi-impianto
* I compiti passano da una struttura all'altra
* Elaborazione sequenziale della struttura

#### Come funziona

```
Factory A (Step 1): Production
    ↓
Quality Check (Step 2): Verification
    ↓
Warehouse (Step 3): Packaging
    ↓
Shipping (Step 4): Dispatch
```

#### Esempio

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

### Carta: ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP

#### Scopo

Crea un compito per il dipartimento appalti

#### Quando usarlo

* Compito del team acquisti
* Compiti di gestione dei fornitori
* Lavoro correlato all'acquisto

#### Esempio

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

### Carta: ACTION\_ASSIGN\_TASK\_PROCUREMENT\_GROUP\_SEQUENTIAL

#### Scopo

Instradamento sequenziale delle attività all'interno dell'approvvigionamento

#### Quando usarlo

* Processi di approvvigionamento in più fasi
* Catena di approvazione negli appalti
* Percorso di escalation

#### Esempio

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

### Carta: ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK

#### Scopo

Ottieni utente dal campo documento, assegna attività Se l'utente non viene trovato, utilizza l'utente fallback

#### Quando usarlo

* Utente memorizzato nel campo documento
* Il documento specifica chi dovrebbe effettuare la revisione
* Avere una persona di backup se l'utente specificato non è disponibile

#### Come funziona

```
Document has field: "Approver Name: John Smith"

Card checks: Is John in system?
    If YES → Assign task to John
    If NO → Assign to Fallback User (Sarah)
```

#### Esempio

```
Invoice field: "Contact: Mike Johnson"

Try to assign task to Mike Johnson
    ↓
If Mike doesn't exist in system:
    ↓
Use Fallback: Team Lead (Robert Brown)
```

#### Parametri

```
- Field to Read: "Approver Name"
- Fallback User: Robert Brown
- Task Details: Title, Description, Priority
```

***

## Parametri delle attività comuni

Tutte le schede attività utilizzano questi parametri:

#### Titolo

```
Good: "Review Invoice #INV-12345 - €5000 - Supplier ABC"
Bad: "Approve something"
```

#### Descrizione

```
Should include:
✅ What to do
✅ Deadline
✅ Any special requirements
✅ Who to contact
✅ Link to document
```

#### Livelli di priorità

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

#### Data di scadenza (se disponibile)

```
When should task be completed by?
Example: 2025-10-30 (5 days from now)
```

***

## Scenari del flusso di lavoro delle attività

### Scenario 1: approvazione semplice

```
Invoice Arrives (€2000)
    ↓
Condition: Amount between €1000-€5000?
    ↓
YES: Create Task for Finance Manager
    ↓
Finance Manager reviews and approves
```

### Scenario 2: approvazione multilivello

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

### Scenario 3: attività parallele

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

### Scenario 4: routing condizionale

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

## Migliori pratiche per l'assegnazione delle attività

✅ **Fai:**

* Includi dettagli specifici nel titolo dell'attività
* Impostare livelli di priorità appropriati
* Stabilisci scadenze realistiche
* Avvisare gli assegnatari
* Includere il collegamento al documento
* Utilizza descrizioni chiare e utilizzabili

❌ **Non farlo:**

* Creare titoli di attività vaghi ("Rivedi questo")
* Imposta tutto come priorità alta
* Dimentica di avvisare la persona assegnata
* Crea più attività per lo stesso lavoro
* Assegna a persone non disponibili

***

## Attività di risoluzione dei problemi

### "Compito non assegnato a nessuno"

**Causa:** L'utente non esiste o il gruppo è vuoto

**Soluzione:**

* Verificare l'ortografia del nome utente
* Verificare che l'utente sia attivo nel sistema
* Verifica che il gruppo abbia membri
* Se necessario, utilizzare il fallback

### "La persona dice di non aver ricevuto la notifica"

**Causa:** Notifica e-mail disabilitata o e-mail errata

**Soluzione:**

* Seleziona la casella di controllo "Invia email" che sia abilitata
* Verifica l'indirizzo email del destinatario
* Controlla la cartella spam
* Invia nuovamente la notifica manualmente

### "La persona sbagliata ha ricevuto il compito"

**Causa:** Logica di instradamento errata

**Soluzione:**

* Controllare le condizioni della tabella decisionale
* Verificare le impostazioni di fallback
* Prova con il documento di esempio
* Verificare la presenza di errori di battitura nei nomi utente

### "Troppe attività create"

**Causa:** La carta viene attivata più volte

**Soluzione:**

* Le condizioni di controllo sono sufficientemente specifiche
* La verifica della carta viene eseguita solo una volta per documento
* Esamina le condizioni "E".
* Aggiungi ulteriori filtri

***

## Tabella di confronto delle schede attività

| Carta                                                        | Crea attività | Assegna a            | When        |
| ----------------------------------------------------------- | ------------ | --------------------- | ----------- |
| tasks\_create                                               | Sì          | Individuale            | Sempre      |
| ACTION\_TASK\_FOR\_GROUP                                    | Sì          | Gruppo                 | Sempre      |
| ACTION\_DECISION\_TREE\_CREATE\_TASKS                       | Sì          | Risultato della tabella decisionale | Condizionale |
| ACTION\_DECISION\_TREE\_TASKS\_SEQUENTIAL                   | Sì          | Multiplo (sequenziale) | Condizionale |
| ACTION\_CREATE\_TASK\_FOR\_USER\_SEQUENTIAL                 | Sì          | Utente + Documento       | Condizionale |
| ACTION\_CREATE\_TASK\_FOR\_GROUP\_SEQUENTIAL                | Sì          | Gruppo + Documento      | Condizionale |
| ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP                   | Sì          | Gruppo di strutture        | Condizionale |
| ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP\_SEQUENTIAL       | Sì          | Strutture multiple   | Condizionale |
| ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP                | Sì          | Gruppo Acquisti      | Condizionale |
| ACTION\_ASSIGN\_TASK\_PROCUREMENT\_GROUP\_SEQUENTIAL        | Sì          | Multiplo (sequenziale) | Condizionale |
| ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK | Sì          | Campo/Ripiego        | Condizionale |

***

## Carte correlate

* **ACTION\_ASSIGN\_DOCUMENT\_TO\_USER** - Assegna documento senza creare attività
* **ACTION\_SEND\_EMAIL** - Avvisa direttamente le persone
* **STAUS\_CHANGE** - Modifica lo stato invece di creare un'attività
* **RUN\_WORKFLOW** - Attiva invece un flusso di lavoro diverso
