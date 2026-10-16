# Decision Logic Pattern

**Patroontype:** Voorwaardelijke routering en logica **Complexiteit:** Gemiddeld **Geschatte insteltijd:** 30-45 minuten **Veelvoorkomende toepassingen:** Routering via meerdere paden, voorwaardelijke verwerking, beslissingsbomen, implementatie van bedrijfsregels

***

U bouwt dit patroon in de **Workflow Builder** (Workflow Dashboard → Workflow List → Add Workflow). Klik op **Add Card** en open de categorie **Logic**. Deze bevat de voorwaarde- en vertakkingskaarten die de beslissingsboom aansturen en die u combineert met de groep **And** om meerdere voorwaarden te evalueren:

<figure><img src="../../../../.gitbook/assets/workflow_add_card_picker.png" alt="Add Card-bibliotheek in de Workflow Builder, gegroepeerd per categorie"><figcaption><p>De <strong>Add Card</strong>-bibliotheek: voorwaarde- en vertakkingskaarten vindt u onder de categorie <strong>Logic</strong>.</p></figcaption></figure>

***

## Patroonoverzicht

Dit patroon laat zien hoe u complexe beslissingslogica implementeert in DocBits-workflows. Met voorwaardekaarten routeert u documenten via verschillende verwerkingspaden op basis van documentkenmerken, veldwaarden en bedrijfsregels.

**Wat dit patroon doet:**

1. Evalueert meerdere voorwaarden achtereenvolgens of parallel
2. Routeert documenten naar verschillende paden op basis van voorwaarden
3. Implementeert bedrijfsregels en beleid
4. Verwerkt complexe beslissingsbomen
5. Combineert meerdere criteria voor routeringsbeslissingen

***

## Wanneer dit patroon te gebruiken

Gebruik dit patroon wanneer u het volgende moet doen:

* ✅ Documenten routeren op basis van bedragsdrempels
* ✅ Verschillende regels toepassen voor verschillende documenttypes
* ✅ Goedkeuringslogica op meerdere niveaus implementeren
* ✅ Complex bedrijfsbeleid verwerken
* ✅ Dynamische routering creëren op basis van meerdere criteria
* ✅ Logica voor uitzonderingsafhandeling implementeren
* ✅ Goedkeuringsmatrices opstellen

**Gebruik dit patroon niet wanneer:**

* ❌ Een eenvoudige lineaire workflow volstaat
* ❌ Alle documenten hetzelfde pad volgen
* ❌ Er geen voorwaardelijke verwerking nodig is

***

## Soorten beslissingslogica

### 1. Eenvoudige IF-THEN-logica

```
IF condition:
  → Action A
ELSE:
  → Action B
```

**Voorbeeld:**

```
IF Amount > €10,000:
  → Assign to Director
ELSE:
  → Assign to Manager
```

### 2. Meerdere criteria (AND-logica)

```
IF condition1 AND condition2 AND condition3:
  → Action A
ELSE:
  → Action B
```

**Voorbeeld:**

```
IF Amount > €10,000 AND Supplier = "New" AND Department = "IT":
  → Assign to IT Director + CFO (dual approval)
ELSE:
  → Standard approval workflow
```

### 3. Alternatieve criteria (OR-logica)

```
IF condition1 OR condition2 OR condition3:
  → Action A
ELSE:
  → Action B
```

**Voorbeeld:**

```
IF Amount > €50,000 OR Supplier is "Blocked" OR Document has "Urgent" flag:
  → Escalate immediately
ELSE:
  → Standard processing
```

### 4. Geneste beslissingsboom

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

**Voorbeeld:**

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

***

## Volledig workflowvoorbeeld

### Scenario: factuurgoedkeuringsmatrix

**Bedrijfsregels:**

1. Bedrag < €1.000: automatisch goedkeuren
2. Bedrag €1.000-€10.000: goedkeuring door de manager
3. Bedrag > €10.000 EN nieuwe leverancier: goedkeuring door directeur + CFO
4. Bedrag > €10.000 EN bestaande leverancier: alleen goedkeuring door de directeur
5. Elk bedrag met een afwijking ten opzichte van de inkooporder: eerst goedkeuring door Inkoop
6. Urgente facturen (gemarkeerd): versnelde workflow

**Implementatie:**

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

***

## Stapsgewijze implementatie

### Stap 1: Voorwaardekaarten definiëren

**Voorwaarde 1: bedragsdrempel**

```
Card: CONDITION_DOC_FIELD_AMOUNT
Field: Total_Amount
Operator: IS LESS THAN
Value: 1000
Currency: EUR
```

**Voorwaarde 2: controle van het documenttype**

```
Card: CONDITION_DOC_TYPE_IS_ISNOT
Document Type: IS
Type: Invoice
```

**Voorwaarde 3: leveranciersstatus**

```
Card: CONDITION_SUPPLIER_STATUS_IS_ISNOT
Supplier Status: IS
Status: ACTIVE
```

**Voorwaarde 4: controle op nieuwe leverancier**

```
Card: CONDITION_DOC_FIELD_DATE
Field: Supplier_First_Transaction_Date
Operator: IS AFTER
Value: {{TODAY_MINUS_180_DAYS}}
```

**Verwijzing naar de handleiding:** [Condition Cards Complete Guide](../condition-cards-complete-guide.md)

***

### Stap 2: Beslissingsboom opbouwen

**Niveau 1: documenttype**

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

**Niveau 2: bedragsdrempels (voor facturen)**

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

**Niveau 3: leveranciersanalyse (voor facturen met hoge waarde)**

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

***

### Stap 3: Routeringsacties aanmaken

**Pad A: automatisch goedkeuren (bedrag < €1.000)**

```
Actions:
1. Set field "Approval_Type" = "AUTO"
2. Set field "Approval_Level" = "0"
3. ACTION_APPROVE_DOCUMENT
4. Export to ERP
5. Send confirmation email (optional)
```

**Pad B: goedkeuring door de manager (€1.000-€10.000)**

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

**Pad C: goedkeuring door de directeur (€10.000-€50.000)**

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

**Pad D: goedkeuring door het topmanagement (≥ €50.000)**

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

***

## Geavanceerde patronen voor beslissingslogica

### Patroon 1: routering op basis van scores

**Bereken een risicoscore en route dienovereenkomstig:**

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

**Implementatie:**

```
1. ACTION_CALCULATE_FIELD: Calculate risk score
2. ACTION_SET_FIELD_TO_NUMBER: Store score
3. CONDITION_DOC_FIELD_NUMBER: Check score thresholds
4. Route based on score
```

***

### Patroon 2: matrix per afdeling

**Verschillende goedkeuringsregels per afdeling:**

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

**Implementatie:**

```
1. Check Department field
2. Based on department, check amount threshold
3. Route to appropriate approver
4. Different thresholds per department
```

***

### Patroon 3: tijdgebaseerde logica

**Verschillende regels op basis van het tijdstip:**

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

***

### Patroon 4: routering op basis van uitzonderingen

**Route uitzonderingen afzonderlijk:**

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

***

## Volledig beslissingslogicadiagram

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

***

## Best practices voor de configuratie

### 1. Houd de logica duidelijk en onderhoudbaar

✅ **Goed:**

```
IF Amount > 10000:
  → High value path
ELSE:
  → Standard path
```

❌ **Slecht (te complex):**

```
IF (Amount > 10000 AND (Supplier = "A" OR Supplier = "B") AND NOT (Status = "X" OR Status = "Y") AND Department IN [1,2,3]):
  → Complex path
```

**Beter: splits het op in stappen:**

```
Step 1: IF Amount > 10000: Continue, ELSE: Standard path
Step 2: IF Supplier in allowed list: Continue, ELSE: Review
Step 3: IF Status valid: Continue, ELSE: Reject
Step 4: IF Department authorized: Approve, ELSE: Escalate
```

***

### 2. Documenteer de beslissingslogica

**Neem altijd op:**

* Doel van elk beslissingspunt
* De bedrijfsregel die wordt geïmplementeerd
* Verwachte uitkomsten
* Afhandeling van uitzonderingen

**Voorbeeld van documentatie:**

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

***

### 3. Test alle paden

**Testmatrix:**

| Testgeval | Bedrag   | Type       | Leverancier | Verwacht pad           | Status |
| --------- | -------- | ---------- | ----------- | ---------------------- | ------ |
| TC1       | €500     | Factuur    | Bestaand    | Automatisch goedkeuren | ✅      |
| TC2       | €5.000   | Factuur    | Bestaand    | Manager                | ✅      |
| TC3       | €15.000  | Factuur    | Nieuw       | Directeur+CFO          | ✅      |
| TC4       | €60.000  | Factuur    | Bestaand    | Topmanagement          | ✅      |
| TC5       | €2.000   | Creditnota | Bestaand    | Creditnota-workflow    | ✅      |
| TC6       | €100.000 | Factuur    | Geblokkeerd | Stoppen en escaleren   | ✅      |

***

### 4. Bewaak beslissingsstatistieken

**Houd bij:**

* Verdeling over de beslissingspaden
* Percentage automatische goedkeuringen
* Percentage handmatige beoordelingen
* Gemiddelde verwerkingstijd per pad
* Percentage uitzonderingen
* Gebruik per pad

**Voorbeeldstatistieken:**

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

***

## Gerelateerde patronen

### Patronen die goed samenwerken:

* [**Task Management Pattern**](task-management-pattern.md) - Taken aanmaken op basis van beslissingen
* [**API Integration Pattern**](api-integration-pattern.md) - Gegevens ophalen voor besluitvorming
* [**PO Matching Pattern**](po-matching-pattern.md) - PO-resultaten gebruiken in beslissingen
* [**Data Transformation Pattern**](data-transformation-pattern.md) - Gegevens transformeren vóór beslissingen

***

## Gerelateerde handleidingen

### Vereisten

* [Condition Cards Complete Guide](../condition-cards-complete-guide.md) - Alle voorwaardekaarten
* [Field Manipulation Guide](../field-manipulation-guide.md) - Veldbewerkingen
* [Assignment User Guide](../assignment-user-guide.md) - Routeringslogica

### Gerelateerde kaarten

* **CONDITION\_DOC\_FIELD\_AMOUNT** - [Condition Cards Guide](../condition-cards-complete-guide.md#field-conditions)
* **CONDITION\_DOC\_TYPE\_IS\_ISNOT** - [Condition Cards Guide](../condition-cards-complete-guide.md#condition-doc-type-is-isnot)
* **CONDITION\_SUPPLIER\_STATUS\_IS\_ISNOT** - [Condition Cards Guide](../condition-cards-complete-guide.md#condition-supplier-status-is-isnot)
* **ACTION\_ASSIGN\_TO\_USER** - [Assignment Guide](../assignment-user-guide.md)
* **tasks\_create** - [Task Assignment Guide](../task-assignment-guide.md)

### Volgende stappen

* Taken aanmaken: [Task Management Pattern](task-management-pattern.md)
* Complexe matching toevoegen: [PO Matching Pattern](po-matching-pattern.md)
* API's integreren: [API Integration Pattern](api-integration-pattern.md)

***

**Patroonversie:** 1.0 **Laatst bijgewerkt:** 23 oktober 2025 **Moeilijkheidsgraad:** Gemiddeld **Geschatte tijd:** 30-45 minuten **Slagingspercentage:** Hoog
