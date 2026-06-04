# Kartice za dodeljivanje i kreiranje zadataka - Kompletan vodič

**Pokriva:** 12 kartica povezanih sa zadacima

---

Kartice za zadatke na ovoj stranici idu u grupu **Then** u Workflow Builder-u — akcije koje se pokreću kada se When/And uslovi poklope:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder platno sa grupama kartica When, And i Then"><figcaption><p>Kartice za zadatke i kreiranje se dodaju u grupu <strong>Then</strong> preko <strong>Add Card</strong>.</p></figcaption></figure>

---

## 📌 Version Information

**Najrazvijenija kartica:** tasks_create (4 verzije, v4 najnovija)
**Druge kartice sa više verzija:** ACTION_TASK_FOR_GROUP (v4), ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP (v3), ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK (v3), ACTION_DECISION_TREE_CREATE_TASKS (v3)

**Ključne promene:**
- **v3 → v4 evolucija:** Uklonjen pristup stabla odlučivanja, dodati generički tipovi radnih stavki (Task, Ticket, Issue)
- **v2 → v3 migracija:** Dodata podrška za stablo odlučivanja (sada uglavnom zastarela)

📖 [Kompletna istorija verzija](../../../changelog/release.md#-task-management-cards) | [Baza podataka verzija kartica](../../../../DocFlow/docs/card_version.md)

---

## Pregled

Kartice za zadatke kreiraju radna dodeljivanja za članove tima. Kada faktura zahteva odobravanje, možete automatski kreirati zadatak i dodeliti ga pravoj osobi.

---

# Osnovno kreiranje zadataka

## Kartica: tasks_create / Kreiraj zadatak i dodeli korisniku

### Svrha
Kreira zadatak i dodeljuje ga određenoj osobi

### Kada koristiti
- Faktura zahteva pregled određene osobe
- Potrebno odobravanje od imenovane osobe
- Predaja određenom članu tima

### Parametri

**Title**
Naziv/predmet zadatka
```
Example: "Review Invoice #INV-2025-001 for approval"
```

**Description**
Detalji o zadatku
```
Example: "Invoice from Supplier ABC needs review.
Amount: €5000
Deadline: 2025-10-30
Please verify pricing and quality."
```

**Priority**
- 🔴 **High**: Hitno, uradite odmah
- 🟡 **Medium**: Normalan prioritet
- 🟢 **Low**: Može se uraditi kasnije

**Assigned User**
Ko dobija zadatak
```
Example: John Smith (Finance Manager)
```

**Email Notification**
Poslati upozorenje e-poštom dodeljenoj osobi?
```
✅ Yes: Person gets email
❌ No: Task only in system
```

### Primer
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

## Kartica: ACTION_TASK_FOR_GROUP / Kreiraj zadatak za grupu

### Svrha
Kreira zadatak i dodeljuje ga grupi (svi članovi mogu da ga vide)

### Kada koristiti
- Više ljudi može da uradi zadatak
- Zadatak za tim, ne za pojedinca
- Prva dostupna osoba treba da rukuje

### Razlika u odnosu na pojedinačni zadatak
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

### Primer toka rada
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

## Kartica: ACTION_DECISION_TREE_CREATE_TASKS

### Svrha
Kreira zadatke na osnovu logike tabele odlučivanja

### Kako funkcioniše
```
Decision Table Returns:
  If invoice from Supplier A → Assign to Procurement
  If invoice from Supplier B → Assign to Quality Team
  If invoice from Supplier C → Assign to Finance

Task is automatically created and assigned
based on which condition is true
```

### Kada koristiti
- Različiti dobavljači zahtevaju različito odobravanje
- Složeno rutiranje na osnovu više faktora
- Različit tim na osnovu tipa dokumenta

### Primer
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

## Kartica: ACTION_DECISION_TREE_TASKS_SEQUENTIAL

### Svrha
Kreira zadatke sekvencijalno na osnovu tabele odlučivanja
Zadaci se dodeljuju jedan po jedan sa redosledom prioriteta

### Kada koristiti
- Potrebno više odobravanja u nizu
- Lanac odobravanja toka rada
- Svaka osoba pregleda pa prosleđuje sledećoj

### Kako funkcioniše
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

### Sistem prioriteta
```
Priority 1 → Assign to: Person A
Priority 2 → Assign to: Person B
Priority 3 → Assign to: Person C

They must complete in order (1→2→3)
```

### Primer konfiguracije
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

## Kartica: ACTION_CREATE_TASK_FOR_USER_SEQUENTIAL

### Svrha
Dodeljuje dokument jednom korisniku I kreira sekvencijalni zadatak

### Kada koristiti
- Dodeljivanje dokumenta I kreiranje zadatka istovremeno
- Dokument treba da pregleda određena osoba
- Praćenje i dodeljivanja i kreiranja zadatka

### Kako funkcioniše
```
Two things happen:
1. Document is assigned to: Person A
2. Task is created for: Person A

Both in one action
```

### Primer
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

## Kartica: ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL

### Svrha
Dodeljuje dokument grupi I kreira zadatak

### Kada koristiti
- Dokument zahteva pažnju grupe
- Želite da pratite kreiranje zadatka
- Kreiranje početnog zadatka pa dodeljivanje dokumenta

### Primer
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

# Napredno kreiranje zadataka

## Kartica: ACTION_ASSIGN_TASK_TO_FACILITY_GROUP

### Svrha
Kreira zadatak za određenu grupu objekta

### Kada koristiti
- Zadatak za tim skladišta/objekta
- Operacije specifične za objekat
- Fizička lokacija je važna

### Primer
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

## Kartica: ACTION_ASSIGN_TASK_TO_FACILITY_GROUP_SEQUENTIAL

### Svrha
Sekvencijalno dodeljivanje zadataka kroz objekte

### Kada koristiti
- Operacije na više objekata
- Zadaci prelaze sa objekta na objekat
- Sekvencijalna obrada po objektu

### Kako funkcioniše
```
Factory A (Step 1): Production
    ↓
Quality Check (Step 2): Verification
    ↓
Warehouse (Step 3): Packaging
    ↓
Shipping (Step 4): Dispatch
```

### Primer
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

## Kartica: ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP

### Svrha
Kreira zadatak za odeljenje nabavke

### Kada koristiti
- Zadatak za tim nabavke
- Zadaci upravljanja dobavljačima
- Posao povezan sa kupovinom

### Primer
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

## Kartica: ACTION_ASSIGN_TASK_PROCUREMENT_GROUP_SEQUENTIAL

### Svrha
Sekvencijalno rutiranje zadataka unutar nabavke

### Kada koristiti
- Višekoračni procesi nabavke
- Lanac odobravanja u nabavci
- Putanja eskalacije

### Primer
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

## Kartica: ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK

### Svrha
Dobija korisnika iz polja dokumenta, dodeljuje zadatak
Ako korisnik nije pronađen, koristi rezervnog korisnika

### Kada koristiti
- Korisnik sačuvan u polju dokumenta
- Dokument navodi ko treba da pregleda
- Imate rezervnu osobu ako navedeni korisnik nije dostupan

### Kako funkcioniše
```
Document has field: "Approver Name: John Smith"

Card checks: Is John in system?
    If YES → Assign task to John
    If NO → Assign to Fallback User (Sarah)
```

### Primer
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

# Uobičajeni parametri zadataka

Sve kartice za zadatke koriste ove parametre:

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

### Nivoi prioriteta
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

### Due Date (ako je dostupno)
```
When should task be completed by?
Example: 2025-10-30 (5 days from now)
```

---

# Scenariji tokova rada zadataka

## Scenario 1: Jednostavno odobravanje
```
Invoice Arrives (€2000)
    ↓
Condition: Amount between €1000-€5000?
    ↓
YES: Create Task for Finance Manager
    ↓
Finance Manager reviews and approves
```

## Scenario 2: Višenivovsko odobravanje
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

## Scenario 3: Paralelni zadaci
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

## Scenario 4: Uslovno rutiranje
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

# Najbolje prakse za dodeljivanje zadataka

✅ **Radite:**
- Uključite specifične detalje u naslov zadatka
- Postavite odgovarajuće nivoe prioriteta
- Postavite realne rokove
- Obavestite osobe kojima je dodeljeno
- Uključite vezu ka dokumentu
- Koristite jasne opise sa jasnom akcijom

❌ **Ne radite:**
- Ne kreirajte nejasne naslove zadataka („Review this")
- Ne postavljajte sve kao visok prioritet
- Ne zaboravljajte da obavestite dodeljenu osobu
- Ne kreirajte više zadataka za isti posao
- Ne dodeljujte nedostupnim osobama

---

# Rešavanje problema sa zadacima

## „Task not assigned to anyone"
**Uzrok:** Korisnik ne postoji ili je grupa prazna

**Rešenje:**
- Verifikujte ispravnost imena korisnika
- Proverite da je korisnik aktivan u sistemu
- Verifikujte da grupa ima članove
- Koristite rezervu ako je potrebno

## „Person says they didn't get notification"
**Uzrok:** Obaveštenje e-poštom onemogućeno ili e-pošta pogrešna

**Rešenje:**
- Proverite da je polje za potvrdu „Send Email" omogućeno
- Verifikujte adresu e-pošte primaoca
- Proverite folder neželjene pošte
- Ručno ponovo pošaljite obaveštenje

## „Wrong person got task"
**Uzrok:** Logika rutiranja nije ispravna

**Rešenje:**
- Proverite uslove tabele odlučivanja
- Verifikujte podešavanja rezerve
- Testirajte sa uzorkom dokumenta
- Proverite greške u kucanju imena korisnika

## „Too many tasks created"
**Uzrok:** Kartica se okida više puta

**Rešenje:**
- Proverite da su uslovi dovoljno specifični
- Verifikujte da se kartica pokreće samo jednom po dokumentu
- Pregledajte „And" uslove
- Dodajte dodatno filtriranje

---

# Tabela poređenja kartica za zadatke

| Kartica | Kreira zadatak | Dodeljuje | Kada |
|------|-------------|-----------|------|
| tasks_create | Da | Pojedincu | Uvek |
| ACTION_TASK_FOR_GROUP | Da | Grupi | Uvek |
| ACTION_DECISION_TREE_CREATE_TASKS | Da | Rezultatu tabele odlučivanja | Uslovno |
| ACTION_DECISION_TREE_TASKS_SEQUENTIAL | Da | Više (sekvencijalno) | Uslovno |
| ACTION_CREATE_TASK_FOR_USER_SEQUENTIAL | Da | Korisnik + Dokument | Uslovno |
| ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL | Da | Grupa + Dokument | Uslovno |
| ACTION_ASSIGN_TASK_TO_FACILITY_GROUP | Da | Grupi objekta | Uslovno |
| ACTION_ASSIGN_TASK_TO_FACILITY_GROUP_SEQUENTIAL | Da | Više objekata | Uslovno |
| ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP | Da | Timu nabavke | Uslovno |
| ACTION_ASSIGN_TASK_PROCUREMENT_GROUP_SEQUENTIAL | Da | Više (sekvencijalno) | Uslovno |
| ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK | Da | Polje/Rezerva | Uslovno |

---

# Povezane kartice

- **ACTION_ASSIGN_DOCUMENT_TO_USER** - Dodeli dokument bez kreiranja zadatka
- **ACTION_SEND_EMAIL** - Obavesti osobe direktno
- **STAUS_CHANGE** - Promeni status umesto kreiranja zadatka
- **RUN_WORKFLOW** - Pokreni drugi tok rada umesto toga
