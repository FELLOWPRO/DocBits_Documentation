# Entscheidungslogik-Pattern

**Pattern-Typ:** Bedingtes Routing & Logik
**Komplexität:** Mittel
**Geschätzte Einrichtung:** 30–45 Minuten
**Typische Anwendungsfälle:** Mehrpfad-Routing, bedingte Verarbeitung, Entscheidungsbäume, Umsetzung von Geschäftsregeln

---

Dieses Pattern bauen Sie im **Workflow-Builder** (Workflow Dashboard → Workflow List → Add Workflow). Klicken Sie auf **Add Card** und öffnen Sie die Kategorie **Logic** — sie enthält die Bedingungs- und Verzweigungskarten, die den Entscheidungsbaum steuern und die Sie mit der **And**-Gruppe kombinieren, um mehrere Bedingungen auszuwerten:

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Add Card-Bibliothek im Workflow-Builder, nach Kategorie gruppiert"><figcaption><p>Die <strong>Add Card</strong>-Bibliothek — Bedingungs- und Verzweigungskarten finden Sie unter der Kategorie <strong>Logic</strong>.</p></figcaption></figure>

---

## Pattern-Überblick

Dieses Pattern zeigt, wie Sie in DocBits-Workflows komplexe Entscheidungslogik umsetzen. Mit Bedingungskarten leiten Sie Dokumente anhand von Dokumentattributen, Feldwerten und Geschäftsregeln über verschiedene Verarbeitungspfade.

**Was dieses Pattern macht:**
1. Wertet mehrere Bedingungen nacheinander oder parallel aus
2. Leitet Dokumente anhand von Bedingungen über verschiedene Pfade
3. Setzt Geschäftsregeln und Richtlinien um
4. Behandelt komplexe Entscheidungsbäume
5. Kombiniert mehrere Kriterien für Routing-Entscheidungen

---

## Wann dieses Pattern verwenden

Verwenden Sie dieses Pattern, wenn Sie Folgendes benötigen:
- ✅ Dokumente nach Betragsschwellen leiten
- ✅ Unterschiedliche Regeln für unterschiedliche Dokumenttypen anwenden
- ✅ Mehrstufige Freigabelogik umsetzen
- ✅ Komplexe Geschäftsrichtlinien abbilden
- ✅ Dynamisches Routing anhand mehrerer Kriterien erstellen
- ✅ Logik zur Ausnahmebehandlung umsetzen
- ✅ Freigabematrizen erstellen

**Verwenden Sie dieses Pattern nicht, wenn:**
- ❌ ein einfacher linearer Workflow genügt
- ❌ alle Dokumente denselben Pfad durchlaufen
- ❌ keine bedingte Verarbeitung erforderlich ist

---

## Typen von Entscheidungslogik

### 1. Einfache IF-THEN-Logik

```
IF condition:
  → Action A
ELSE:
  → Action B
```

**Beispiel:**
```
IF Amount > €10,000:
  → Assign to Director
ELSE:
  → Assign to Manager
```

### 2. Mehrere Kriterien (UND-Logik)

```
IF condition1 AND condition2 AND condition3:
  → Action A
ELSE:
  → Action B
```

**Beispiel:**
```
IF Amount > €10,000 AND Supplier = "New" AND Department = "IT":
  → Assign to IT Director + CFO (dual approval)
ELSE:
  → Standard approval workflow
```

### 3. Alternative Kriterien (ODER-Logik)

```
IF condition1 OR condition2 OR condition3:
  → Action A
ELSE:
  → Action B
```

**Beispiel:**
```
IF Amount > €50,000 OR Supplier is "Blocked" OR Document has "Urgent" flag:
  → Escalate immediately
ELSE:
  → Standard processing
```

### 4. Verschachtelter Entscheidungsbaum

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

**Beispiel:**
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

## Vollständiges Workflow-Beispiel

### Szenario: Freigabematrix für Rechnungen

**Geschäftsregeln:**
1. Betrag < 1.000 €: Automatisch freigeben
2. Betrag 1.000–10.000 €: Freigabe durch die Führungskraft
3. Betrag > 10.000 € UND neuer Lieferant: Freigabe durch Direktor + CFO
4. Betrag > 10.000 € UND bestehender Lieferant: Nur Freigabe durch Direktor
5. Jeder Betrag mit PO-Abweichung: Zuerst Freigabe durch den Einkauf
6. Dringende Rechnungen (markiert): Beschleunigter Workflow

**Umsetzung:**

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

## Schritt-für-Schritt-Umsetzung

### Schritt 1: Bedingungskarten definieren

**Bedingung 1: Betragsschwelle**
```
Card: CONDITION_DOC_FIELD_AMOUNT
Field: Total_Amount
Operator: IS LESS THAN
Value: 1000
Currency: EUR
```

**Bedingung 2: Dokumenttyp-Prüfung**
```
Card: CONDITION_DOC_TYPE_IS_ISNOT
Document Type: IS
Type: Invoice
```

**Bedingung 3: Lieferantenstatus**
```
Card: CONDITION_SUPPLIER_STATUS_IS_ISNOT
Supplier Status: IS
Status: ACTIVE
```

**Bedingung 4: Prüfung auf neuen Lieferanten**
```
Card: CONDITION_DOC_FIELD_DATE
Field: Supplier_First_Transaction_Date
Operator: IS AFTER
Value: {{TODAY_MINUS_180_DAYS}}
```

**Leitfaden-Referenz:** [Leitfaden Bedingungskarten (komplett)](../and/condition-cards-complete-guide.md)

---

### Schritt 2: Entscheidungsbaum aufbauen

**Ebene 1: Dokumenttyp**
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

**Ebene 2: Betragsschwellen (für Rechnungen)**
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

**Ebene 3: Lieferantenanalyse (für hochwertige Rechnungen)**
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

### Schritt 3: Routing-Aktionen erstellen

**Pfad A: Automatische Freigabe (Betrag < 1.000 €)**
```
Actions:
1. Set field "Approval_Type" = "AUTO"
2. Set field "Approval_Level" = "0"
3. ACTION_APPROVE_DOCUMENT
4. Export to ERP
5. Send confirmation email (optional)
```

**Pfad B: Freigabe durch die Führungskraft (1.000–10.000 €)**
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

**Pfad C: Freigabe durch den Direktor (10.000–50.000 €)**
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

**Pfad D: Freigabe durch die Geschäftsleitung (≥ 50.000 €)**
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

## Erweiterte Entscheidungslogik-Patterns

### Pattern 1: Punktzahlbasiertes Routing

**Eine Risikobewertung berechnen und entsprechend routen:**

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

**Umsetzung:**
```
1. ACTION_CALCULATE_FIELD: Calculate risk score
2. ACTION_SET_FIELD_TO_NUMBER: Store score
3. CONDITION_DOC_FIELD_NUMBER: Check score thresholds
4. Route based on score
```

---

### Pattern 2: Abteilungsbasierte Matrix

**Unterschiedliche Freigaberegeln je Abteilung:**

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

**Umsetzung:**
```
1. Check Department field
2. Based on department, check amount threshold
3. Route to appropriate approver
4. Different thresholds per department
```

---

### Pattern 3: Zeitbasierte Logik

**Unterschiedliche Regeln je nach Zeitpunkt:**

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

### Pattern 4: Ausnahmebasiertes Routing

**Ausnahmen separat leiten:**

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

## Vollständiges Entscheidungslogik-Diagramm

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

## Best Practices für die Konfiguration

### 1. Logik klar und wartbar halten

✅ **Gut:**
```
IF Amount > 10000:
  → High value path
ELSE:
  → Standard path
```

❌ **Schlecht (zu komplex):**
```
IF (Amount > 10000 AND (Supplier = "A" OR Supplier = "B") AND NOT (Status = "X" OR Status = "Y") AND Department IN [1,2,3]):
  → Complex path
```

**Besser: In Schritte aufteilen:**
```
Step 1: IF Amount > 10000: Continue, ELSE: Standard path
Step 2: IF Supplier in allowed list: Continue, ELSE: Review
Step 3: IF Status valid: Continue, ELSE: Reject
Step 4: IF Department authorized: Approve, ELSE: Escalate
```

---

### 2. Entscheidungslogik dokumentieren

**Immer aufnehmen:**
- Zweck jedes Entscheidungspunkts
- Umgesetzte Geschäftsregel
- Erwartete Ergebnisse
- Ausnahmebehandlung

**Beispiel-Dokumentation:**
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

### 3. Alle Pfade testen

**Test-Matrix:**

| Testfall | Betrag | Typ | Lieferant | Erwarteter Pfad | Status |
|-----------|--------|------|----------|---------------|--------|
| TC1 | €500 | Invoice | Existing | Auto-approve | ✅ |
| TC2 | €5,000 | Invoice | Existing | Manager | ✅ |
| TC3 | €15,000 | Invoice | New | Director+CFO | ✅ |
| TC4 | €60,000 | Invoice | Existing | Executive | ✅ |
| TC5 | €2,000 | Credit Note | Existing | Credit workflow | ✅ |
| TC6 | €100,000 | Invoice | Blocked | Stop & Escalate | ✅ |

---

### 4. Entscheidungskennzahlen überwachen

**Verfolgen:**
- Verteilung auf die Entscheidungspfade
- Automatische Freigabequote
- Manuelle Prüfquote
- Durchschnittliche Verarbeitungszeit pro Pfad
- Ausnahmequoten
- Pfad-Auslastung

**Beispiel-Kennzahlen:**
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

## Verwandte Patterns

### Patterns, die gut zusammenpassen:

- **[Aufgabenverwaltungs-Pattern](task-management-pattern.md)** – Aufgaben anhand von Entscheidungen erstellen
- **[API-Integrations-Pattern](api-integration-pattern.md)** – Daten für die Entscheidungsfindung abrufen
- **[PO-Matching-Pattern](po-matching-pattern.md)** – PO-Ergebnisse in Entscheidungen verwenden
- **[Datentransformations-Pattern](data-transformation-pattern.md)** – Daten vor Entscheidungen transformieren

---

## Verwandte Leitfäden

### Voraussetzungen
- [Leitfaden Bedingungskarten (komplett)](../and/condition-cards-complete-guide.md) – Alle Bedingungskarten
- [Leitfaden Feldmanipulation](../then/document-field/field-manipulation-guide.md) – Feldoperationen
- [Zuweisungs-Leitfaden](../then/assignee/assignment-user-guide.md) – Routing-Logik

### Verwandte Karten
- **CONDITION_DOC_FIELD_AMOUNT** – [Leitfaden Bedingungskarten](../and/condition-cards-complete-guide.md#field-conditions)
- **CONDITION_DOC_TYPE_IS_ISNOT** – [Leitfaden Bedingungskarten](../and/condition-cards-complete-guide.md#condition-doc-type-is-isnot)
- **CONDITION_SUPPLIER_STATUS_IS_ISNOT** – [Leitfaden Bedingungskarten](../and/condition-cards-complete-guide.md#condition-supplier-status-is-isnot)
- **ACTION_ASSIGN_TO_USER** – [Zuweisungs-Leitfaden](../then/assignee/assignment-user-guide.md)
- **tasks_create** – [Leitfaden Aufgabenzuweisung](../then/task/task-assignment-guide.md)

### Nächste Schritte
- Aufgaben erstellen: [Aufgabenverwaltungs-Pattern](task-management-pattern.md)
- Komplexen Abgleich hinzufügen: [PO-Matching-Pattern](po-matching-pattern.md)
- APIs integrieren: [API-Integrations-Pattern](api-integration-pattern.md)

---

**Pattern-Version:** 1.0
**Zuletzt aktualisiert:** 23. Oktober 2025
**Schwierigkeit:** Mittel
**Geschätzte Zeit:** 30–45 Minuten
**Erfolgsquote:** Hoch
