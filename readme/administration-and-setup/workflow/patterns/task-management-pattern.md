# Task Management Pattern

**Tip obrasca:** Upravljanje tokom rada
**Složenost:** Niska-srednja
**Procenjeno podešavanje:** 30-45 minuta
**Uobičajeni slučajevi upotrebe:** Tokovi rada za odobravanje, zadaci pregleda, rukovanje izuzecima, eskalacija

---

Ovaj obrazac gradite u **Workflow Builder**-u (Workflow Dashboard → Workflow List → Add Workflow). Kliknite na **Add Card** da otvorite biblioteku kartica i izaberete kartice koje ovaj obrazac koristi — `tasks_create`, `ACTION_ASSIGN_TO_USER`, `ACTION_SEND_EMAIL_TO_GROUPS` i `CONDITION_TASK_STATUS` (kategorija **Assignee** sadrži kartice za zadatke i dodeljivanje):

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Biblioteka Add Card u Workflow Builder-u, grupisana po kategoriji"><figcaption><p>Biblioteka <strong>Add Card</strong> — kartice za zadatke, dodeljivanje i obaveštenja nalaze se pod kategorijama <strong>Assignee</strong> i <strong>Status</strong>.</p></figcaption></figure>

---

## Pregled obrasca

Ovaj obrazac pokazuje kako da kreirate, dodeljujete, pratite i upravljate zadacima u okviru DocBits tokova rada. Zadaci su radne stavke koje se mogu izvršiti, dodeljene korisnicima ili grupama, koje zahtevaju završetak pre nego što tok rada dokumenta može da se nastavi.

**Šta ovaj obrazac radi:**
1. Kreira zadatke na osnovu uslova toka rada
2. Dodeljuje zadatke odgovarajućim korisnicima ili grupama
3. Postavlja svojstva zadatka (prioritet, rok, opis)
4. Šalje obaveštenja kada se kreiraju zadaci
5. Prati status i završetak zadatka
6. Rutira dokumente na osnovu ishoda zadatka

---

## Kada koristiti ovaj obrazac

Koristite ovaj obrazac kada treba da:
- ✅ Kreirate tokove rada za odobravanje
- ✅ Dodelite zadatke pregleda korisnicima
- ✅ Rukujete izuzecima koji zahtevaju ljudsku intervenciju
- ✅ Eskalirate probleme menadžerima
- ✅ Kreirate višenivovske lance odobravanja
- ✅ Pratite ko treba šta da uradi
- ✅ Postavite rokove za akcije

**Nemojte koristiti ovaj obrazac kada:**
- ❌ Nije potrebna ljudska akcija (umesto toga koristite automatsku obradu)
- ❌ Potrebno je samo obavestiti (umesto toga koristite e-poštu)
- ❌ Jednostavno rutiranje dokumenta (umesto toga koristite dodeljivanje)

---

## Kompletan primer toka rada

### Scenario: Odobravanje fakture sa rutiranjem zasnovanim na iznosu

**Poslovni zahtev:**
- Fakture < €1.000: Automatsko odobravanje (zadatak nije potreban)
- Fakture €1.000-€10.000: Zadatak odobravanja menadžeru
- Fakture > €10.000: Dvostruko odobravanje (Menadžer + Direktor)
- Svi odobravaoci primaju obaveštenje e-poštom
- Zadaci imaju rok od 3 dana

**Korišćene kartice toka rada:**
1. CONDITION_DOC_FIELD_AMOUNT - Provera iznosa fakture
2. tasks_create - Kreiranje zadatka odobravanja
3. ACTION_ASSIGN_TO_USER - Dodeljivanje zadatka odobravaocu
4. ACTION_SEND_EMAIL_TO_GROUPS - Slanje obaveštenja
5. CONDITION_TASK_STATUS - Provera da li je zadatak završen
6. ACTION_APPROVE_DOCUMENT - Odobravanje nakon završetka zadatka

---

## Implementacija korak po korak

### Korak 1: Proverite prag iznosa

**Kartica:** CONDITION_DOC_FIELD_AMOUNT ili slični uslov polja

**Konfiguracija za putanju 1 (< €1.000):**
```
Field: Total_Amount
Operator: IS LESS THAN
Value: 1000
Currency: EUR
```

**Konfiguracija za putanju 2 (€1.000-€10.000):**
```
Field: Total_Amount
Operator: IS BETWEEN
Value Min: 1000
Value Max: 10000
Currency: EUR
```

**Konfiguracija za putanju 3 (> €10.000):**
```
Field: Total_Amount
Operator: IS GREATER THAN
Value: 10000
Currency: EUR
```

**Referenca vodiča:** [Condition Cards Guide](../and/condition-cards-complete-guide.md)

---

### Korak 2A: Automatsko odobravanje malih faktura (< €1.000)

**Zadatak nije potreban za male iznose**

**Kartice:**
- ACTION_SET_FIELD_TO_TEXT
  - Postavite "Approval_Type" = "AUTO"
  - Postavite "Approval_Reason" = "Amount below threshold"
- ACTION_APPROVE_DOCUMENT

**Rezultat:** Dokument je automatski odobren, nijedan zadatak nije kreiran

---

### Korak 2B: Kreirajte zadatak odobravanja menadžeru (€1.000-€10.000)

**Kartica:** tasks_create (v4 preporučeno)

**Konfiguracija:**
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

**Mapiranje polja:**
- `{{DOCUMENT_NUMBER}}` - Automatski ID dokumenta
- `{{Total_Amount}}` - Polje: Total_Amount
- `{{Supplier_Name}}` - Polje: Supplier_Name
- `{{Invoice_Number}}` - Polje: Invoice_Number
- `{{Invoice_Date}}` - Polje: Invoice_Date
- `{{Approving_Manager}}` - Polje ili fiksni korisnik

**Referenca vodiča:** [Task Assignment Guide](../then/task/task-assignment-guide.md)

---

### Korak 2C: Kreirajte zadatke dvostrukog odobravanja (> €10.000)

**Dva sekvencijalna zadatka za fakture velike vrednosti**

**Zadatak 1: Odobravanje menadžera**
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

**Zadatak 2: Odobravanje direktora (Kreiran nakon završetka Zadatka 1)**
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

### Korak 3: Dodelite zadatak korisniku/grupi

**Kartica:** ACTION_ASSIGN_TO_USER ili ACTION_ASSIGN_TO_GROUP

**Opcija 1: Dodelite određenom korisniku**
```
User: John.Smith@company.com
OR
User Field: {{DOCUMENT_FIELD:Approving_Manager}}
```

**Opcija 2: Dodelite grupi**
```
Group: Finance Managers
Assignment Mode: First Available
OR
Assignment Mode: Round Robin
OR
Assignment Mode: All (everyone in group gets task)
```

**Opcija 3: Sekvencijalno dodeljivanje**
```
Card: ACTION_ASSIGN_SEQUENTIALLY_TO_USER

User 1: Finance_Manager
User 2: Finance_Director (only if User 1 approves)
User 3: CFO (only if User 2 approves)
```

**Referenca vodiča:** [Assignment User Guide](../then/assignee/assignment-user-guide.md)

---

### Korak 4: Pošaljite obaveštenje e-poštom

**Kartica:** ACTION_SEND_EMAIL_TO_GROUPS

**Konfiguracija:**
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

**Promenljive e-pošte:**
- `{{TASK_ASSIGNEE_EMAIL}}` - E-pošta osobe kojoj je zadatak dodeljen
- `{{TASK_ASSIGNEE_NAME}}` - Ime osobe kojoj je zadatak dodeljen
- `{{DOCUMENT_NUMBER}}` - ID dokumenta
- `{{TASK_DEADLINE}}` - Rok zadatka
- `{{TASK_PRIORITY}}` - Nivo prioriteta zadatka
- `{{DOCUMENT_LINK}}` - Direktna veza ka dokumentu

**Referenca vodiča:** [Send Email Groups Guide](../then/action/send-email-groups-guide.md)

---

### Korak 5: Pratite status zadatka

**Kartica:** CONDITION_TASK_STATUS ili sličan proveravač statusa zadatka

**Konfiguracija:**
```
Task ID: {{CREATED_TASK_ID}}
Status Check: IS COMPLETED
```

**Opcije statusa:**
- CREATED - Zadatak upravo kreiran
- ASSIGNED - Zadatak dodeljen korisniku
- IN_PROGRESS - Korisnik je počeo rad na zadatku
- COMPLETED - Zadatak završen
- APPROVED - Zadatak odobren
- REJECTED - Zadatak odbijen
- CANCELLED - Zadatak otkazan
- OVERDUE - Zadatak prekoračio rok

**Logika:**
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

### Korak 6: Završite tok rada na osnovu rezultata zadatka

**Nakon završetka zadatka:**

**Scenario A: Zadatak odobren**
```
1. Set field "Approval_Status" = "APPROVED"
2. Set field "Approved_By" = {{TASK_COMPLETED_BY}}
3. Set field "Approval_Date" = {{TASK_COMPLETED_DATE}}
4. ACTION_APPROVE_DOCUMENT
5. Export document (if configured)
```

**Scenario B: Zadatak odbijen**
```
1. Set field "Approval_Status" = "REJECTED"
2. Set field "Rejected_By" = {{TASK_COMPLETED_BY}}
3. Set field "Rejection_Reason" = {{TASK_REJECTION_REASON}}
4. ACTION_REJECT_DOCUMENT
5. Send rejection notification to supplier
6. Create "Correction Needed" task
```

**Scenario C: Zadatak prekoračio rok**
```
1. Set field "Task_Status" = "OVERDUE"
2. Create escalation task for manager
3. Send reminder email to original assignee
4. Send escalation email to manager
5. Log overdue event
```

---

## Kompletan dijagram toka rada

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

## Šabloni za konfiguraciju

### Šablon 1: Jednostavan zadatak odobravanja

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

### Šablon 2: Zadatak pregleda sa detaljima

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

### Šablon 3: Zadatak eskalacije

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

## Napredni obrasci

### Obrazac 1: Sekvencijalno višenivovsko odobravanje

**Upotreba:** Fakture moraju proći kroz više odobravaoca redom

```
Level 1: Accounts Clerk (verify data)
  → IF APPROVED:
    Level 2: Accounts Manager (approve amount)
      → IF APPROVED:
        Level 3: Finance Director (final sign-off)
          → IF APPROVED:
            Document Approved ✅
```

**Implementacija:**
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

### Obrazac 2: Paralelno odobravanje od strane više odobravaoca

**Upotreba:** Više ljudi mora istovremeno da odobri

```
Send to ALL approvers at once:
- Finance Manager
- Procurement Manager
- Quality Manager

Document approved only when ALL approve
```

**Implementacija:**
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

### Obrazac 3: Uslovno kreiranje zadataka

**Upotreba:** Kreirajte različite zadatke na osnovu uslova

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

### Obrazac 4: Eskalacija zasnovana na roku

**Upotreba:** Automatska eskalacija ako zadatak nije završen na vreme

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

## Rukovanje greškama

### Scenario 1: Osoba za dodeljivanje nije pronađena

**Problem:** Korisnik ne postoji ili je neaktivan

**Rešenje:**
```
1. Check user status with CONDITION_USER_IS_ISNOT
2. IF User = INACTIVE:
     → Assign to backup user
     → OR Assign to user's group
     → Log warning
3. Send notification to admin
```

---

### Scenario 2: Kreiranje zadatka nije uspelo

**Problem:** Sistemska greška pri kreiranju zadatka

**Rešenje:**
```
1. Check task creation status
2. IF Failed:
     → Retry task creation
     → Send email notification instead
     → Create admin alert task
     → Log error details
```

---

### Scenario 3: Nema odgovora na zadatak

**Problem:** Korisnik ne završava zadatak do roka

**Rešenje:**
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

## Lista za proveru testiranja

- [ ] Zadatak uspešno kreiran
- [ ] Zadatak dodeljen ispravnom korisniku/grupi
- [ ] Obaveštenje e-poštom poslato
- [ ] Zadatak se pojavljuje na listi zadataka korisnika
- [ ] Svojstva zadatka ispravna (naslov, opis, prioritet, rok)
- [ ] Korisnik može da završi zadatak
- [ ] Tok rada se nastavlja nakon završetka zadatka
- [ ] Tok rada odobravanja ispravno funkcioniše
- [ ] Tok rada odbijanja ispravno funkcioniše
- [ ] Eskalacija se aktivira u pravo vreme
- [ ] Rukovanje prekoračenim rokom funkcioniše
- [ ] Sva obaveštenja e-poštom poslata
- [ ] Ažuriranja polja ispravno funkcionišu

---

## Primeri iz stvarnog sveta

### Primer 1: Izuzetak trostrukog uparivanja PO

**Scenario:** Faktura se ne poklapa sa PO, potreban je pregled

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

### Primer 2: Odobravanje fakture dobavljača

**Scenario:** Faktura novog dobavljača zahteva posebno odobravanje

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

### Primer 3: Obrada na kraju meseca

**Scenario:** Fakture na kraju meseca zahtevaju hitnu obradu

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

## Saveti za performanse

✅ **Najbolje prakse:**
- Postavite realne rokove
- Koristite jasne naslove i opise zadataka
- Uključite sve potrebne informacije u zadatak
- Šaljite blagovremena obaveštenja
- Pratite stope završetka zadataka
- Automatski eskalirajte zadatke koji su prekoračili rok
- Beležite sve aktivnosti zadataka
- Mesečno pregledajte obrasce zadataka

❌ **Izbegavajte:**
- Kreiranje zadataka za sve
- Nejasne opise zadataka
- Nerealne rokove
- Previše e-poruka sa obaveštenjima
- Bez putanje eskalacije
- Ignorisanje zadataka koji su prekoračili rok
- Nepraćenje metrika zadataka

---

## Povezani obrasci

### Obrasci koji dobro funkcionišu zajedno:

- **[API Integration Pattern](api-integration-pattern.md)** - Kreirajte zadatke za API greške
- **[PO Matching Pattern](po-matching-pattern.md)** - Kreirajte zadatke za PO neslaganja
- **[Decision Logic Pattern](decision-logic-pattern.md)** - Rutirajte ka odgovarajućem tipu zadatka
- **[Data Transformation Pattern](data-transformation-pattern.md)** - Transformišite podatke pre kreiranja zadatka

---

## Povezani vodiči

### Preduslovi
- [Task Assignment Guide](../then/task/task-assignment-guide.md) - Dokumentacija kartice za zadatke
- [Assignment User Guide](../then/assignee/assignment-user-guide.md) - Dodeljivanje korisnika
- [Send Email Groups Guide](../then/action/send-email-groups-guide.md) - Obaveštenja e-poštom

### Povezane kartice
- **tasks_create** - [Task Assignment Guide](../then/task/task-assignment-guide.md)
- **ACTION_ASSIGN_TO_USER** - [Assignment Guide](../then/assignee/assignment-user-guide.md)
- **ACTION_SEND_EMAIL_TO_GROUPS** - [Email Guide](../then/action/send-email-groups-guide.md)
- **CONDITION_TASK_STATUS** - [Condition Cards Guide](../and/condition-cards-complete-guide.md)

### Sledeći koraci
- Dodajte obaveštenja e-poštom: [Send Email Guide](../then/action/send-email-groups-guide.md)
- Implementirajte složeno rutiranje: [Decision Logic Pattern](decision-logic-pattern.md)
- Rukujte greškama: [Error Handling Pattern](error-handling-pattern.md)

---

**Verzija obrasca:** 1.0
**Poslednje ažuriranje:** 23. oktobar 2025.
**Težina:** Niska-srednja
**Procenjeno vreme:** 30-45 minuta
**Stopa uspeha:** Vrlo visoka
