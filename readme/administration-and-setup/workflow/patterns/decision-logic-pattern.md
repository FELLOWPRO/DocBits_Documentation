# Decision Logic Pattern

**Tip obrasca:** Uslovno rutiranje i logika
**Složenost:** Srednja
**Procenjeno podešavanje:** 30-45 minuta
**Uobičajeni slučajevi upotrebe:** Rutiranje sa više putanja, uslovna obrada, stabla odlučivanja, implementacija poslovnih pravila

---

Ovaj obrazac gradite u **Workflow Builder**-u (Workflow Dashboard → Workflow List → Add Workflow). Kliknite na **Add Card** i otvorite kategoriju **Logic** — ona sadrži uslovne kartice i kartice grananja koje pokreću stablo odlučivanja, a koje kombinujete sa grupom **And** za procenu više uslova:

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Biblioteka Add Card u Workflow Builder-u, grupisana po kategoriji"><figcaption><p>Biblioteka <strong>Add Card</strong> — uslovne kartice i kartice grananja nalaze se pod kategorijom <strong>Logic</strong>.</p></figcaption></figure>

---

## Pregled obrasca

Ovaj obrazac pokazuje kako da implementirate složenu logiku odlučivanja u DocBits tokovima rada koristeći uslovne kartice za rutiranje dokumenata kroz različite putanje obrade na osnovu atributa dokumenta, vrednosti polja i poslovnih pravila.

**Šta ovaj obrazac radi:**
1. Procenjuje više uslova sekvencijalno ili paralelno
2. Rutira dokumente ka različitim putanjama na osnovu uslova
3. Implementira poslovna pravila i politike
4. Rukuje složenim stablima odlučivanja
5. Kombinuje više kriterijuma za odluke o rutiranju

---

## Kada koristiti ovaj obrazac

Koristite ovaj obrazac kada treba da:
- ✅ Rutirate dokumente po pragovima iznosa
- ✅ Primenite različita pravila za različite tipove dokumenata
- ✅ Implementirate logiku višenivovskog odobravanja
- ✅ Rukujete složenim poslovnim politikama
- ✅ Kreirate dinamičko rutiranje na osnovu više kriterijuma
- ✅ Implementirate logiku rukovanja izuzecima
- ✅ Kreirate matrice odobravanja

**Nemojte koristiti ovaj obrazac kada:**
- ❌ Jednostavan linearni tok rada je dovoljan
- ❌ Svi dokumenti prate istu putanju
- ❌ Nije potrebna uslovna obrada

---

## Tipovi logike odlučivanja

### 1. Jednostavna IF-THEN logika

```
IF condition:
  → Action A
ELSE:
  → Action B
```

**Primer:**
```
IF Amount > €10,000:
  → Assign to Director
ELSE:
  → Assign to Manager
```

### 2. Više kriterijuma (AND logika)

```
IF condition1 AND condition2 AND condition3:
  → Action A
ELSE:
  → Action B
```

**Primer:**
```
IF Amount > €10,000 AND Supplier = "New" AND Department = "IT":
  → Assign to IT Director + CFO (dual approval)
ELSE:
  → Standard approval workflow
```

### 3. Alternativni kriterijumi (OR logika)

```
IF condition1 OR condition2 OR condition3:
  → Action A
ELSE:
  → Action B
```

**Primer:**
```
IF Amount > €50,000 OR Supplier is "Blocked" OR Document has "Urgent" flag:
  → Escalate immediately
ELSE:
  → Standard processing
```

### 4. Ugnežđeno stablo odlučivanja

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

**Primer:**
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

## Kompletan primer toka rada

### Scenario: Matrica odobravanja faktura

**Poslovna pravila:**
1. Iznos < €1.000: Automatsko odobravanje
2. Iznos €1.000-€10.000: Odobravanje menadžera
3. Iznos > €10.000 AND Novi dobavljač: Odobravanje direktora + CFO
4. Iznos > €10.000 AND Postojeći dobavljač: Samo odobravanje direktora
5. Bilo koji iznos sa neslaganjem PO: Prvo odobravanje nabavke
6. Hitne fakture (označene): Ubrzani tok rada

**Implementacija:**

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

## Implementacija korak po korak

### Korak 1: Definišite uslovne kartice

**Uslov 1: Prag iznosa**
```
Card: CONDITION_DOC_FIELD_AMOUNT
Field: Total_Amount
Operator: IS LESS THAN
Value: 1000
Currency: EUR
```

**Uslov 2: Provera tipa dokumenta**
```
Card: CONDITION_DOC_TYPE_IS_ISNOT
Document Type: IS
Type: Invoice
```

**Uslov 3: Status dobavljača**
```
Card: CONDITION_SUPPLIER_STATUS_IS_ISNOT
Supplier Status: IS
Status: ACTIVE
```

**Uslov 4: Provera novog dobavljača**
```
Card: CONDITION_DOC_FIELD_DATE
Field: Supplier_First_Transaction_Date
Operator: IS AFTER
Value: {{TODAY_MINUS_180_DAYS}}
```

**Referenca vodiča:** [Condition Cards Complete Guide](../and/condition-cards-complete-guide.md)

---

### Korak 2: Izgradite stablo odlučivanja

**Nivo 1: Tip dokumenta**
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

**Nivo 2: Pragovi iznosa (za fakture)**
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

**Nivo 3: Analiza dobavljača (za fakture velike vrednosti)**
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

### Korak 3: Kreirajte akcije rutiranja

**Putanja A: Automatsko odobravanje (Iznos < €1.000)**
```
Actions:
1. Set field "Approval_Type" = "AUTO"
2. Set field "Approval_Level" = "0"
3. ACTION_APPROVE_DOCUMENT
4. Export to ERP
5. Send confirmation email (optional)
```

**Putanja B: Odobravanje menadžera (€1.000-€10.000)**
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

**Putanja C: Odobravanje direktora (€10.000-€50.000)**
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

**Putanja D: Izvršno odobravanje (≥ €50.000)**
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

## Napredni obrasci logike odlučivanja

### Obrazac 1: Rutiranje zasnovano na skoru

**Izračunajte skor rizika i rutirajte u skladu sa tim:**

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

**Implementacija:**
```
1. ACTION_CALCULATE_FIELD: Calculate risk score
2. ACTION_SET_FIELD_TO_NUMBER: Store score
3. CONDITION_DOC_FIELD_NUMBER: Check score thresholds
4. Route based on score
```

---

### Obrazac 2: Matrica zasnovana na odeljenju

**Različita pravila odobravanja po odeljenju:**

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

**Implementacija:**
```
1. Check Department field
2. Based on department, check amount threshold
3. Route to appropriate approver
4. Different thresholds per department
```

---

### Obrazac 3: Logika zasnovana na vremenu

**Različita pravila na osnovu vremena:**

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

### Obrazac 4: Rutiranje zasnovano na izuzecima

**Rutirajte izuzetke odvojeno:**

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

## Kompletan dijagram logike odlučivanja

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

## Najbolje prakse za konfiguraciju

### 1. Održavajte logiku jasnom i lakom za održavanje

✅ **Dobro:**
```
IF Amount > 10000:
  → High value path
ELSE:
  → Standard path
```

❌ **Loše (Previše složeno):**
```
IF (Amount > 10000 AND (Supplier = "A" OR Supplier = "B") AND NOT (Status = "X" OR Status = "Y") AND Department IN [1,2,3]):
  → Complex path
```

**Bolje: Razbijte na korake:**
```
Step 1: IF Amount > 10000: Continue, ELSE: Standard path
Step 2: IF Supplier in allowed list: Continue, ELSE: Review
Step 3: IF Status valid: Continue, ELSE: Reject
Step 4: IF Department authorized: Approve, ELSE: Escalate
```

---

### 2. Dokumentujte logiku odlučivanja

**Uvek uključite:**
- Svrhu svake tačke odlučivanja
- Poslovno pravilo koje se implementira
- Očekivane ishode
- Rukovanje izuzecima

**Primer dokumentacije:**
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

### 3. Testirajte sve putanje

**Matrica testiranja:**

| Test slučaj | Iznos | Tip | Dobavljač | Očekivana putanja | Status |
|-----------|--------|------|----------|---------------|--------|
| TC1 | €500 | Invoice | Postojeći | Auto-approve | ✅ |
| TC2 | €5,000 | Invoice | Postojeći | Manager | ✅ |
| TC3 | €15,000 | Invoice | Novi | Director+CFO | ✅ |
| TC4 | €60,000 | Invoice | Postojeći | Executive | ✅ |
| TC5 | €2,000 | Credit Note | Postojeći | Credit workflow | ✅ |
| TC6 | €100,000 | Invoice | Blokiran | Stop & Escalate | ✅ |

---

### 4. Pratite metrike odlučivanja

**Pratite:**
- Distribuciju kroz putanje odlučivanja
- Stopu automatskog odobravanja
- Stopu ručnog pregleda
- Prosečno vreme obrade po putanji
- Stope izuzetaka
- Iskorišćenost putanja

**Primer metrika:**
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

## Povezani obrasci

### Obrasci koji dobro funkcionišu zajedno:

- **[Task Management Pattern](task-management-pattern.md)** - Kreirajte zadatke na osnovu odluka
- **[API Integration Pattern](api-integration-pattern.md)** - Preuzmite podatke za donošenje odluka
- **[PO Matching Pattern](po-matching-pattern.md)** - Koristite PO rezultate u odlukama
- **[Data Transformation Pattern](data-transformation-pattern.md)** - Transformišite podatke pre odluka

---

## Povezani vodiči

### Preduslovi
- [Condition Cards Complete Guide](../and/condition-cards-complete-guide.md) - Sve uslovne kartice
- [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md) - Operacije nad poljima
- [Assignment User Guide](../then/assignee/assignment-user-guide.md) - Logika rutiranja

### Povezane kartice
- **CONDITION_DOC_FIELD_AMOUNT** - [Condition Cards Guide](../and/condition-cards-complete-guide.md#field-conditions)
- **CONDITION_DOC_TYPE_IS_ISNOT** - [Condition Cards Guide](../and/condition-cards-complete-guide.md#condition-doc-type-is-isnot)
- **CONDITION_SUPPLIER_STATUS_IS_ISNOT** - [Condition Cards Guide](../and/condition-cards-complete-guide.md#condition-supplier-status-is-isnot)
- **ACTION_ASSIGN_TO_USER** - [Assignment Guide](../then/assignee/assignment-user-guide.md)
- **tasks_create** - [Task Assignment Guide](../then/task/task-assignment-guide.md)

### Sledeći koraci
- Kreirajte zadatke: [Task Management Pattern](task-management-pattern.md)
- Dodajte složeno uparivanje: [PO Matching Pattern](po-matching-pattern.md)
- Integrišite API-je: [API Integration Pattern](api-integration-pattern.md)

---

**Verzija obrasca:** 1.0
**Poslednje ažuriranje:** 23. oktobar 2025.
**Težina:** Srednja
**Procenjeno vreme:** 30-45 minuta
**Stopa uspeha:** Visoka
