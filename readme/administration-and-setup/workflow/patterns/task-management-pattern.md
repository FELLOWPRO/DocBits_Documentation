# Aufgabenverwaltungs-Pattern

**Pattern-Typ:** Workflow-Management
**Komplexität:** Niedrig-Mittel
**Geschätzte Einrichtung:** 30–45 Minuten
**Typische Anwendungsfälle:** Freigabe-Workflows, Prüfaufgaben, Ausnahmebehandlung, Eskalation

---

Dieses Pattern bauen Sie im **Workflow-Builder** (Workflow Dashboard → Workflow List → Add Workflow). Klicken Sie auf **Add Card**, um die Kartenbibliothek zu öffnen, und wählen Sie die von diesem Pattern verwendeten Karten — `tasks_create`, `ACTION_ASSIGN_TO_USER`, `ACTION_SEND_EMAIL_TO_GROUPS` und `CONDITION_TASK_STATUS` (die Kategorie **Assignee** enthält die Aufgaben- und Zuweisungskarten):

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Add Card-Bibliothek im Workflow-Builder, nach Kategorie gruppiert"><figcaption><p>Die <strong>Add Card</strong>-Bibliothek — die Aufgaben-, Zuweisungs- und Benachrichtigungskarten finden Sie unter den Kategorien <strong>Assignee</strong> und <strong>Status</strong>.</p></figcaption></figure>

---

## Pattern-Überblick

Dieses Pattern zeigt, wie Sie Aufgaben in DocBits-Workflows erstellen, zuweisen, verfolgen und verwalten. Aufgaben sind umsetzbare Arbeitsschritte, die Benutzern oder Gruppen zugewiesen werden und abgeschlossen sein müssen, bevor der Dokument-Workflow fortgesetzt werden kann.

**Was dieses Pattern macht:**
1. Erstellt Aufgaben anhand von Workflow-Bedingungen
2. Weist Aufgaben passenden Benutzern oder Gruppen zu
3. Setzt Aufgabeneigenschaften (Priorität, Frist, Beschreibung)
4. Sendet Benachrichtigungen, wenn Aufgaben erstellt werden
5. Verfolgt Status und Abschluss der Aufgaben
6. Leitet Dokumente anhand der Aufgabenergebnisse weiter

---

## Wann dieses Pattern verwenden

Verwenden Sie dieses Pattern, wenn Sie Folgendes benötigen:
- ✅ Freigabe-Workflows erstellen
- ✅ Prüfaufgaben Benutzern zuweisen
- ✅ Ausnahmen behandeln, die manuelles Eingreifen erfordern
- ✅ Probleme an Vorgesetzte eskalieren
- ✅ Mehrstufige Freigabeketten erstellen
- ✅ Verfolgen, wer was tun muss
- ✅ Fristen für Aktionen setzen

**Verwenden Sie dieses Pattern nicht, wenn:**
- ❌ keine manuelle Aktion erforderlich ist (verwenden Sie stattdessen die automatische Verarbeitung)
- ❌ nur benachrichtigt werden soll (verwenden Sie stattdessen E-Mail)
- ❌ einfaches Dokument-Routing genügt (verwenden Sie stattdessen die Zuweisung)

---

## Vollständiges Workflow-Beispiel

### Szenario: Rechnungsfreigabe mit betragsbasiertem Routing

**Geschäftliche Anforderung:**
- Rechnungen < 1.000 €: Automatisch freigeben (keine Aufgabe nötig)
- Rechnungen 1.000–10.000 €: Freigabeaufgabe an die Führungskraft
- Rechnungen > 10.000 €: Doppelfreigabe (Führungskraft + Direktor)
- Alle Freigeber erhalten eine E-Mail-Benachrichtigung
- Aufgaben haben eine Frist von 3 Tagen

**Verwendete Workflow-Karten:**
1. CONDITION_DOC_FIELD_AMOUNT – Rechnungsbetrag prüfen
2. tasks_create – Freigabeaufgabe erstellen
3. ACTION_ASSIGN_TO_USER – Aufgabe dem Freigeber zuweisen
4. ACTION_SEND_EMAIL_TO_GROUPS – Benachrichtigung senden
5. CONDITION_TASK_STATUS – Prüfen, ob die Aufgabe abgeschlossen ist
6. ACTION_APPROVE_DOCUMENT – Nach Aufgabenabschluss freigeben

---

## Schritt-für-Schritt-Umsetzung

### Schritt 1: Betragsschwelle prüfen

**Karte:** CONDITION_DOC_FIELD_AMOUNT oder eine ähnliche Feldbedingung

**Konfiguration für Pfad 1 (< 1.000 €):**
```
Field: Total_Amount
Operator: IS LESS THAN
Value: 1000
Currency: EUR
```

**Konfiguration für Pfad 2 (1.000–10.000 €):**
```
Field: Total_Amount
Operator: IS BETWEEN
Value Min: 1000
Value Max: 10000
Currency: EUR
```

**Konfiguration für Pfad 3 (> 10.000 €):**
```
Field: Total_Amount
Operator: IS GREATER THAN
Value: 10000
Currency: EUR
```

**Leitfaden-Referenz:** [Leitfaden Bedingungskarten](../and/condition-cards-complete-guide.md)

---

### Schritt 2A: Kleine Rechnungen automatisch freigeben (< 1.000 €)

**Für kleine Beträge ist keine Aufgabe nötig**

**Karten:**
- ACTION_SET_FIELD_TO_TEXT
  - „Approval_Type" = „AUTO" setzen
  - „Approval_Reason" = „Amount below threshold" setzen
- ACTION_APPROVE_DOCUMENT

**Ergebnis:** Dokument automatisch freigegeben, keine Aufgabe erstellt

---

### Schritt 2B: Freigabeaufgabe für die Führungskraft erstellen (1.000–10.000 €)

**Karte:** tasks_create (v4 empfohlen)

**Konfiguration:**
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

**Feldzuordnung:**
- `{{DOCUMENT_NUMBER}}` – Automatische Dokument-ID
- `{{Total_Amount}}` – Feld: Total_Amount
- `{{Supplier_Name}}` – Feld: Supplier_Name
- `{{Invoice_Number}}` – Feld: Invoice_Number
- `{{Invoice_Date}}` – Feld: Invoice_Date
- `{{Approving_Manager}}` – Feld oder fester Benutzer

**Leitfaden-Referenz:** [Leitfaden Aufgabenzuweisung](../then/task/task-assignment-guide.md)

---

### Schritt 2C: Doppelfreigabe-Aufgaben erstellen (> 10.000 €)

**Zwei aufeinanderfolgende Aufgaben für hochwertige Rechnungen**

**Aufgabe 1: Freigabe durch die Führungskraft**
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

**Aufgabe 2: Freigabe durch den Direktor (wird nach Abschluss von Aufgabe 1 erstellt)**
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

### Schritt 3: Aufgabe einem Benutzer/einer Gruppe zuweisen

**Karte:** ACTION_ASSIGN_TO_USER oder ACTION_ASSIGN_TO_GROUP

**Option 1: Einem bestimmten Benutzer zuweisen**
```
User: John.Smith@company.com
OR
User Field: {{DOCUMENT_FIELD:Approving_Manager}}
```

**Option 2: Einer Gruppe zuweisen**
```
Group: Finance Managers
Assignment Mode: First Available
OR
Assignment Mode: Round Robin
OR
Assignment Mode: All (everyone in group gets task)
```

**Option 3: Sequenzielle Zuweisung**
```
Card: ACTION_ASSIGN_SEQUENTIALLY_TO_USER

User 1: Finance_Manager
User 2: Finance_Director (only if User 1 approves)
User 3: CFO (only if User 2 approves)
```

**Leitfaden-Referenz:** [Zuweisungs-Leitfaden](../then/assignee/assignment-user-guide.md)

---

### Schritt 4: E-Mail-Benachrichtigung senden

**Karte:** ACTION_SEND_EMAIL_TO_GROUPS

**Konfiguration:**
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

**E-Mail-Variablen:**
- `{{TASK_ASSIGNEE_EMAIL}}` – E-Mail des Aufgaben-Empfängers
- `{{TASK_ASSIGNEE_NAME}}` – Name des Aufgaben-Empfängers
- `{{DOCUMENT_NUMBER}}` – Dokument-ID
- `{{TASK_DEADLINE}}` – Fälligkeitsdatum der Aufgabe
- `{{TASK_PRIORITY}}` – Prioritätsstufe der Aufgabe
- `{{DOCUMENT_LINK}}` – Direktlink zum Dokument

**Leitfaden-Referenz:** [Leitfaden E-Mail an Gruppen](../then/action/send-email-groups-guide.md)

---

### Schritt 5: Aufgabenstatus verfolgen

**Karte:** CONDITION_TASK_STATUS oder ein ähnlicher Aufgabenstatus-Prüfer

**Konfiguration:**
```
Task ID: {{CREATED_TASK_ID}}
Status Check: IS COMPLETED
```

**Status-Optionen:**
- CREATED – Aufgabe gerade erstellt
- ASSIGNED – Aufgabe einem Benutzer zugewiesen
- IN_PROGRESS – Benutzer hat mit der Aufgabe begonnen
- COMPLETED – Aufgabe abgeschlossen
- APPROVED – Aufgabe freigegeben
- REJECTED – Aufgabe abgelehnt
- CANCELLED – Aufgabe storniert
- OVERDUE – Aufgabe überfällig

**Logik:**
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

### Schritt 6: Workflow anhand des Aufgabenergebnisses abschließen

**Nach Aufgabenabschluss:**

**Szenario A: Aufgabe freigegeben**
```
1. Set field "Approval_Status" = "APPROVED"
2. Set field "Approved_By" = {{TASK_COMPLETED_BY}}
3. Set field "Approval_Date" = {{TASK_COMPLETED_DATE}}
4. ACTION_APPROVE_DOCUMENT
5. Export document (if configured)
```

**Szenario B: Aufgabe abgelehnt**
```
1. Set field "Approval_Status" = "REJECTED"
2. Set field "Rejected_By" = {{TASK_COMPLETED_BY}}
3. Set field "Rejection_Reason" = {{TASK_REJECTION_REASON}}
4. ACTION_REJECT_DOCUMENT
5. Send rejection notification to supplier
6. Create "Correction Needed" task
```

**Szenario C: Aufgabe überfällig**
```
1. Set field "Task_Status" = "OVERDUE"
2. Create escalation task for manager
3. Send reminder email to original assignee
4. Send escalation email to manager
5. Log overdue event
```

---

## Vollständiges Workflow-Diagramm

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

## Konfigurationsvorlagen

### Vorlage 1: Einfache Freigabeaufgabe

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

### Vorlage 2: Prüfaufgabe mit Details

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

### Vorlage 3: Eskalationsaufgabe

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

## Erweiterte Patterns

### Pattern 1: Sequenzielle mehrstufige Freigabe

**Verwendung:** Rechnungen müssen mehrere Freigeber nacheinander durchlaufen

```
Level 1: Accounts Clerk (verify data)
  → IF APPROVED:
    Level 2: Accounts Manager (approve amount)
      → IF APPROVED:
        Level 3: Finance Director (final sign-off)
          → IF APPROVED:
            Document Approved ✅
```

**Umsetzung:**
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

### Pattern 2: Parallele Freigabe durch mehrere Personen

**Verwendung:** Mehrere Personen müssen gleichzeitig freigeben

```
Send to ALL approvers at once:
- Finance Manager
- Procurement Manager
- Quality Manager

Document approved only when ALL approve
```

**Umsetzung:**
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

### Pattern 3: Bedingte Aufgabenerstellung

**Verwendung:** Unterschiedliche Aufgaben anhand von Bedingungen erstellen

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

### Pattern 4: Fristbasierte Eskalation

**Verwendung:** Automatisch eskalieren, wenn die Aufgabe nicht rechtzeitig abgeschlossen wird

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

## Fehlerbehandlung

### Szenario 1: Empfänger nicht gefunden

**Problem:** Benutzer existiert nicht oder ist inaktiv

**Lösung:**
```
1. Check user status with CONDITION_USER_IS_ISNOT
2. IF User = INACTIVE:
     → Assign to backup user
     → OR Assign to user's group
     → Log warning
3. Send notification to admin
```

---

### Szenario 2: Aufgabenerstellung fehlgeschlagen

**Problem:** Systemfehler beim Erstellen der Aufgabe

**Lösung:**
```
1. Check task creation status
2. IF Failed:
     → Retry task creation
     → Send email notification instead
     → Create admin alert task
     → Log error details
```

---

### Szenario 3: Keine Reaktion auf die Aufgabe

**Problem:** Benutzer schließt die Aufgabe nicht fristgerecht ab

**Lösung:**
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

## Test-Checkliste

- [ ] Aufgabe erfolgreich erstellt
- [ ] Aufgabe dem richtigen Benutzer/der richtigen Gruppe zugewiesen
- [ ] E-Mail-Benachrichtigung gesendet
- [ ] Aufgabe erscheint in der Aufgabenliste des Benutzers
- [ ] Aufgabeneigenschaften korrekt (Titel, Beschreibung, Priorität, Frist)
- [ ] Benutzer kann die Aufgabe abschließen
- [ ] Workflow wird nach Aufgabenabschluss fortgesetzt
- [ ] Freigabe-Workflow funktioniert korrekt
- [ ] Ablehnungs-Workflow funktioniert korrekt
- [ ] Eskalation wird zum richtigen Zeitpunkt ausgelöst
- [ ] Überfälligkeitsbehandlung funktioniert
- [ ] Alle E-Mail-Benachrichtigungen gesendet
- [ ] Feldaktualisierungen funktionieren korrekt

---

## Praxisbeispiele

### Beispiel 1: Ausnahme beim Drei-Wege-PO-Abgleich

**Szenario:** Rechnung stimmt nicht mit der Bestellung überein, Prüfung nötig

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

### Beispiel 2: Freigabe einer Lieferantenrechnung

**Szenario:** Rechnung eines neuen Lieferanten benötigt eine besondere Freigabe

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

### Beispiel 3: Monatsabschluss-Verarbeitung

**Szenario:** Rechnungen zum Monatsende benötigen dringende Verarbeitung

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

## Leistungstipps

✅ **Best Practices:**
- Realistische Fristen setzen
- Klare Aufgabentitel und -beschreibungen verwenden
- Alle notwendigen Informationen in die Aufgabe aufnehmen
- Zeitnah benachrichtigen
- Abschlussquoten der Aufgaben überwachen
- Überfällige Aufgaben automatisch eskalieren
- Alle Aufgabenaktivitäten protokollieren
- Aufgabenmuster monatlich überprüfen

❌ **Vermeiden:**
- Für alles Aufgaben erstellen
- Vage Aufgabenbeschreibungen
- Unrealistische Fristen
- Zu viele Benachrichtigungs-E-Mails
- Kein Eskalationspfad
- Überfällige Aufgaben ignorieren
- Aufgabenkennzahlen nicht verfolgen

---

## Verwandte Patterns

### Patterns, die gut zusammenpassen:

- **[API-Integrations-Pattern](api-integration-pattern.md)** – Aufgaben für API-Fehler erstellen
- **[PO-Matching-Pattern](po-matching-pattern.md)** – Aufgaben bei PO-Abweichungen erstellen
- **[Entscheidungslogik-Pattern](decision-logic-pattern.md)** – Zum passenden Aufgabentyp routen
- **[Datentransformations-Pattern](data-transformation-pattern.md)** – Daten vor der Aufgabenerstellung transformieren

---

## Verwandte Leitfäden

### Voraussetzungen
- [Leitfaden Aufgabenzuweisung](../then/task/task-assignment-guide.md) – Dokumentation der Aufgabenkarte
- [Zuweisungs-Leitfaden](../then/assignee/assignment-user-guide.md) – Benutzerzuweisung
- [Leitfaden E-Mail an Gruppen](../then/action/send-email-groups-guide.md) – E-Mail-Benachrichtigungen

### Verwandte Karten
- **tasks_create** – [Leitfaden Aufgabenzuweisung](../then/task/task-assignment-guide.md)
- **ACTION_ASSIGN_TO_USER** – [Zuweisungs-Leitfaden](../then/assignee/assignment-user-guide.md)
- **ACTION_SEND_EMAIL_TO_GROUPS** – [E-Mail-Leitfaden](../then/action/send-email-groups-guide.md)
- **CONDITION_TASK_STATUS** – [Leitfaden Bedingungskarten](../and/condition-cards-complete-guide.md)

### Nächste Schritte
- E-Mail-Benachrichtigungen hinzufügen: [E-Mail-Leitfaden](../then/action/send-email-groups-guide.md)
- Komplexes Routing umsetzen: [Entscheidungslogik-Pattern](decision-logic-pattern.md)

---

**Pattern-Version:** 1.0
**Zuletzt aktualisiert:** 23. Oktober 2025
**Schwierigkeit:** Niedrig-Mittel
**Geschätzte Zeit:** 30–45 Minuten
**Erfolgsquote:** Sehr hoch
