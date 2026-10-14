# Wzorzec logiki decyzyjnej

**Typ wzorca:** Routing warunkowy i logika
**Złożoność:** Średnia
**Szacowana konfiguracja:** 30–45 minut
**Typowe przypadki użycia:** Routing wielościeżkowy, przetwarzanie warunkowe, drzewa decyzyjne, wdrażanie reguł biznesowych

---

Ten wzorzec budujesz w **Workflow Builder** (Workflow Dashboard → Workflow List → Add Workflow). Kliknij **Add Card** i otwórz kategorię **Logic** — zawiera ona karty warunków i rozgałęzień, które sterują drzewem decyzyjnym i które łączysz z grupą **And**, aby ocenić wiele warunków:

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Biblioteka Add Card w Workflow Builder, pogrupowana według kategorii"><figcaption><p>Biblioteka <strong>Add Card</strong> — karty warunków i rozgałęzień znajdziesz w kategorii <strong>Logic</strong>.</p></figcaption></figure>

---

## Przegląd wzorca

Ten wzorzec pokazuje, jak wdrożyć złożoną logikę decyzyjną w workflow DocBits. Za pomocą kart warunków routujesz dokumenty różnymi ścieżkami przetwarzania w oparciu o atrybuty dokumentu, wartości pól i reguły biznesowe.

**Co robi ten wzorzec:**
1. Ocenia wiele warunków kolejno lub równolegle
2. Routuje dokumenty różnymi ścieżkami na podstawie warunków
3. Wdraża reguły biznesowe i polityki
4. Obsługuje złożone drzewa decyzyjne
5. Łączy wiele kryteriów w decyzje routingu

---

## Kiedy stosować ten wzorzec

Stosuj ten wzorzec, gdy potrzebujesz:
- ✅ Routować dokumenty według progów kwotowych
- ✅ Stosować różne reguły dla różnych typów dokumentów
- ✅ Wdrażać wielopoziomową logikę zatwierdzania
- ✅ Obsługiwać złożone polityki biznesowe
- ✅ Tworzyć dynamiczny routing w oparciu o wiele kryteriów
- ✅ Wdrażać logikę obsługi wyjątków
- ✅ Tworzyć macierze zatwierdzania

**Nie stosuj tego wzorca, gdy:**
- ❌ wystarcza prosty liniowy workflow
- ❌ wszystkie dokumenty przechodzą tą samą ścieżką
- ❌ przetwarzanie warunkowe nie jest wymagane

---

## Typy logiki decyzyjnej

### 1. Prosta logika IF-THEN

```
IF condition:
  → Action A
ELSE:
  → Action B
```

**Przykład:**
```
IF Amount > €10,000:
  → Assign to Director
ELSE:
  → Assign to Manager
```

### 2. Wiele kryteriów (logika AND)

```
IF condition1 AND condition2 AND condition3:
  → Action A
ELSE:
  → Action B
```

**Przykład:**
```
IF Amount > €10,000 AND Supplier = "New" AND Department = "IT":
  → Assign to IT Director + CFO (dual approval)
ELSE:
  → Standard approval workflow
```

### 3. Alternatywne kryteria (logika OR)

```
IF condition1 OR condition2 OR condition3:
  → Action A
ELSE:
  → Action B
```

**Przykład:**
```
IF Amount > €50,000 OR Supplier is "Blocked" OR Document has "Urgent" flag:
  → Escalate immediately
ELSE:
  → Standard processing
```

### 4. Zagnieżdżone drzewo decyzyjne

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

**Przykład:**
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

## Kompletny przykład workflow

### Scenariusz: Macierz zatwierdzania faktur

**Reguły biznesowe:**
1. Kwota < 1 000 €: Zatwierdzaj automatycznie
2. Kwota 1 000–10 000 €: Zatwierdzenie przez kierownika
3. Kwota > 10 000 € ORAZ nowy dostawca: Zatwierdzenie przez dyrektora + CFO
4. Kwota > 10 000 € ORAZ istniejący dostawca: Tylko zatwierdzenie przez dyrektora
5. Dowolna kwota z odchyleniem PO: Najpierw zatwierdzenie przez zakupy
6. Pilne faktury (oznaczone): Przyspieszony workflow

**Wdrożenie:**

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

## Wdrożenie krok po kroku

### Krok 1: Zdefiniuj karty warunków

**Warunek 1: Próg kwotowy**
```
Card: CONDITION_DOC_FIELD_AMOUNT
Field: Total_Amount
Operator: IS LESS THAN
Value: 1000
Currency: EUR
```

**Warunek 2: Sprawdzenie typu dokumentu**
```
Card: CONDITION_DOC_TYPE_IS_ISNOT
Document Type: IS
Type: Invoice
```

**Warunek 3: Status dostawcy**
```
Card: CONDITION_SUPPLIER_STATUS_IS_ISNOT
Supplier Status: IS
Status: ACTIVE
```

**Warunek 4: Sprawdzenie nowego dostawcy**
```
Card: CONDITION_DOC_FIELD_DATE
Field: Supplier_First_Transaction_Date
Operator: IS AFTER
Value: {{TODAY_MINUS_180_DAYS}}
```

**Referencja przewodnika:** [Przewodnik po kartach warunków (kompletny)](../and/condition-cards-complete-guide.md)

---

### Krok 2: Zbuduj drzewo decyzyjne

**Poziom 1: Typ dokumentu**
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

**Poziom 2: Progi kwotowe (dla faktur)**
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

**Poziom 3: Analiza dostawcy (dla faktur o wysokiej wartości)**
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

### Krok 3: Utwórz akcje routingu

**Ścieżka A: Automatyczne zatwierdzenie (kwota < 1 000 €)**
```
Actions:
1. Set field "Approval_Type" = "AUTO"
2. Set field "Approval_Level" = "0"
3. ACTION_APPROVE_DOCUMENT
4. Export to ERP
5. Send confirmation email (optional)
```

**Ścieżka B: Zatwierdzenie przez kierownika (1 000–10 000 €)**
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

**Ścieżka C: Zatwierdzenie przez dyrektora (10 000–50 000 €)**
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

**Ścieżka D: Zatwierdzenie przez zarząd (≥ 50 000 €)**
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

## Zaawansowane wzorce logiki decyzyjnej

### Wzorzec 1: Routing oparty na punktacji

**Oblicz ocenę ryzyka i routuj odpowiednio:**

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

**Wdrożenie:**
```
1. ACTION_CALCULATE_FIELD: Calculate risk score
2. ACTION_SET_FIELD_TO_NUMBER: Store score
3. CONDITION_DOC_FIELD_NUMBER: Check score thresholds
4. Route based on score
```

---

### Wzorzec 2: Macierz oparta na dziale

**Różne reguły zatwierdzania w zależności od działu:**

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

**Wdrożenie:**
```
1. Check Department field
2. Based on department, check amount threshold
3. Route to appropriate approver
4. Different thresholds per department
```

---

### Wzorzec 3: Logika oparta na czasie

**Różne reguły w zależności od momentu:**

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

### Wzorzec 4: Routing oparty na wyjątkach

**Routowanie wyjątków osobno:**

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

## Kompletny diagram logiki decyzyjnej

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

## Najlepsze praktyki konfiguracji

### 1. Utrzymuj logikę jasną i łatwą w utrzymaniu

✅ **Dobrze:**
```
IF Amount > 10000:
  → High value path
ELSE:
  → Standard path
```

❌ **Źle (zbyt złożone):**
```
IF (Amount > 10000 AND (Supplier = "A" OR Supplier = "B") AND NOT (Status = "X" OR Status = "Y") AND Department IN [1,2,3]):
  → Complex path
```

**Lepiej: Podziel na kroki:**
```
Step 1: IF Amount > 10000: Continue, ELSE: Standard path
Step 2: IF Supplier in allowed list: Continue, ELSE: Review
Step 3: IF Status valid: Continue, ELSE: Reject
Step 4: IF Department authorized: Approve, ELSE: Escalate
```

---

### 2. Dokumentuj logikę decyzyjną

**Zawsze uwzględnij:**
- Cel każdego punktu decyzyjnego
- Wdrożoną regułę biznesową
- Oczekiwane wyniki
- Obsługę wyjątków

**Przykładowa dokumentacja:**
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

### 3. Przetestuj wszystkie ścieżki

**Macierz testów:**

| Przypadek testowy | Kwota | Typ | Dostawca | Oczekiwana ścieżka | Status |
|-----------|--------|------|----------|---------------|--------|
| TC1 | €500 | Invoice | Existing | Auto-approve | ✅ |
| TC2 | €5,000 | Invoice | Existing | Manager | ✅ |
| TC3 | €15,000 | Invoice | New | Director+CFO | ✅ |
| TC4 | €60,000 | Invoice | Existing | Executive | ✅ |
| TC5 | €2,000 | Credit Note | Existing | Credit workflow | ✅ |
| TC6 | €100,000 | Invoice | Blocked | Stop & Escalate | ✅ |

---

### 4. Monitoruj wskaźniki decyzyjne

**Śledź:**
- Rozkład na ścieżki decyzyjne
- Wskaźnik automatycznego zatwierdzania
- Wskaźnik przeglądu ręcznego
- Średni czas przetwarzania na ścieżkę
- Wskaźniki wyjątków
- Wykorzystanie ścieżek

**Przykładowe wskaźniki:**
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

## Powiązane wzorce

### Wzorce, które dobrze ze sobą współgrają:

- **[Wzorzec zarządzania zadaniami](task-management-pattern.md)** – Tworzenie zadań na podstawie decyzji
- **[Wzorzec integracji API](api-integration-pattern.md)** – Pobieranie danych do podejmowania decyzji
- **[Wzorzec PO Matching](po-matching-pattern.md)** – Wykorzystanie wyników PO w decyzjach
- **[Wzorzec transformacji danych](data-transformation-pattern.md)** – Transformacja danych przed decyzjami

---

## Powiązane przewodniki

### Wymagania wstępne
- [Przewodnik po kartach warunków (kompletny)](../and/condition-cards-complete-guide.md) – Wszystkie karty warunków
- [Przewodnik po manipulacji polami](../then/document-field/field-manipulation-guide.md) – Operacje na polach
- [Przewodnik po przypisaniu](../then/assignee/assignment-user-guide.md) – Logika routingu

### Powiązane karty
- **CONDITION_DOC_FIELD_AMOUNT** – [Przewodnik po kartach warunków](../and/condition-cards-complete-guide.md#field-conditions)
- **CONDITION_DOC_TYPE_IS_ISNOT** – [Przewodnik po kartach warunków](../and/condition-cards-complete-guide.md#condition-doc-type-is-isnot)
- **CONDITION_SUPPLIER_STATUS_IS_ISNOT** – [Przewodnik po kartach warunków](../and/condition-cards-complete-guide.md#condition-supplier-status-is-isnot)
- **ACTION_ASSIGN_TO_USER** – [Przewodnik po przypisaniu](../then/assignee/assignment-user-guide.md)
- **tasks_create** – [Przewodnik po przypisywaniu zadań](../then/task/task-assignment-guide.md)

### Następne kroki
- Twórz zadania: [Wzorzec zarządzania zadaniami](task-management-pattern.md)
- Dodaj złożone dopasowanie: [Wzorzec PO Matching](po-matching-pattern.md)
- Zintegruj API: [Wzorzec integracji API](api-integration-pattern.md)

---

**Wersja wzorca:** 1.0
**Ostatnia aktualizacja:** 23 października 2025
**Trudność:** Średnia
**Szacowany czas:** 30–45 minut
**Wskaźnik sukcesu:** Wysoki
