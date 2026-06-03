# Wzorzec zarządzania zadaniami

**Typ wzorca:** Zarządzanie workflow
**Złożoność:** Niska-Średnia
**Szacowana konfiguracja:** 30–45 minut
**Typowe przypadki użycia:** Workflow zatwierdzania, zadania przeglądu, obsługa wyjątków, eskalacja

---

Ten wzorzec budujesz w **Workflow Builder** (Workflow Dashboard → Workflow List → Add Workflow). Kliknij **Add Card**, aby otworzyć bibliotekę kart, i wybierz karty używane przez ten wzorzec — `tasks_create`, `ACTION_ASSIGN_TO_USER`, `ACTION_SEND_EMAIL_TO_GROUPS` oraz `CONDITION_TASK_STATUS` (kategoria **Assignee** zawiera karty zadań i przypisań):

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Biblioteka Add Card w Workflow Builder, pogrupowana według kategorii"><figcaption><p>Biblioteka <strong>Add Card</strong> — karty zadań, przypisań i powiadomień znajdziesz w kategoriach <strong>Assignee</strong> i <strong>Status</strong>.</p></figcaption></figure>

---

## Przegląd wzorca

Ten wzorzec pokazuje, jak tworzyć, przypisywać, śledzić i zarządzać zadaniami w workflow DocBits. Zadania to wykonalne kroki pracy przypisywane użytkownikom lub grupom, które muszą zostać ukończone, zanim workflow dokumentu będzie mógł być kontynuowany.

**Co robi ten wzorzec:**
1. Tworzy zadania na podstawie warunków workflow
2. Przypisuje zadania odpowiednim użytkownikom lub grupom
3. Ustawia właściwości zadań (priorytet, termin, opis)
4. Wysyła powiadomienia, gdy zadania są tworzone
5. Śledzi status i ukończenie zadań
6. Routuje dokumenty na podstawie wyników zadań

---

## Kiedy stosować ten wzorzec

Stosuj ten wzorzec, gdy potrzebujesz:
- ✅ Tworzyć workflow zatwierdzania
- ✅ Przypisywać zadania przeglądu użytkownikom
- ✅ Obsługiwać wyjątki wymagające interwencji człowieka
- ✅ Eskalować problemy do przełożonych
- ✅ Tworzyć wielopoziomowe łańcuchy zatwierdzania
- ✅ Śledzić, kto co musi zrobić
- ✅ Ustawiać terminy dla działań

**Nie stosuj tego wzorca, gdy:**
- ❌ żadne działanie ręczne nie jest wymagane (zamiast tego użyj przetwarzania automatycznego)
- ❌ chcesz jedynie powiadomić (zamiast tego użyj e-maila)
- ❌ wystarcza proste routowanie dokumentów (zamiast tego użyj przypisania)

---

## Kompletny przykład workflow

### Scenariusz: Zatwierdzanie faktur z routingiem opartym na kwocie

**Wymaganie biznesowe:**
- Faktury < 1 000 €: Zatwierdzaj automatycznie (zadanie niepotrzebne)
- Faktury 1 000–10 000 €: Zadanie zatwierdzenia do kierownika
- Faktury > 10 000 €: Podwójne zatwierdzenie (kierownik + dyrektor)
- Wszyscy zatwierdzający otrzymują powiadomienie e-mail
- Zadania mają termin 3 dni

**Użyte karty workflow:**
1. CONDITION_DOC_FIELD_AMOUNT – Sprawdź kwotę faktury
2. tasks_create – Utwórz zadanie zatwierdzenia
3. ACTION_ASSIGN_TO_USER – Przypisz zadanie zatwierdzającemu
4. ACTION_SEND_EMAIL_TO_GROUPS – Wyślij powiadomienie
5. CONDITION_TASK_STATUS – Sprawdź, czy zadanie zostało ukończone
6. ACTION_APPROVE_DOCUMENT – Zatwierdź po ukończeniu zadania

---

## Wdrożenie krok po kroku

### Krok 1: Sprawdź próg kwotowy

**Karta:** CONDITION_DOC_FIELD_AMOUNT lub podobny warunek pola

**Konfiguracja dla ścieżki 1 (< 1 000 €):**
```
Field: Total_Amount
Operator: IS LESS THAN
Value: 1000
Currency: EUR
```

**Konfiguracja dla ścieżki 2 (1 000–10 000 €):**
```
Field: Total_Amount
Operator: IS BETWEEN
Value Min: 1000
Value Max: 10000
Currency: EUR
```

**Konfiguracja dla ścieżki 3 (> 10 000 €):**
```
Field: Total_Amount
Operator: IS GREATER THAN
Value: 10000
Currency: EUR
```

**Referencja przewodnika:** [Przewodnik po kartach warunków](../and/condition-cards-complete-guide.md)

---

### Krok 2A: Automatycznie zatwierdzaj małe faktury (< 1 000 €)

**Dla małych kwot zadanie nie jest potrzebne**

**Karty:**
- ACTION_SET_FIELD_TO_TEXT
  - Ustaw „Approval_Type" = „AUTO"
  - Ustaw „Approval_Reason" = „Amount below threshold"
- ACTION_APPROVE_DOCUMENT

**Wynik:** Dokument zatwierdzony automatycznie, zadanie nie zostało utworzone

---

### Krok 2B: Utwórz zadanie zatwierdzenia dla kierownika (1 000–10 000 €)

**Karta:** tasks_create (zalecana v4)

**Konfiguracja:**
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

**Mapowanie pól:**
- `{{DOCUMENT_NUMBER}}` – Automatyczny identyfikator dokumentu
- `{{Total_Amount}}` – Pole: Total_Amount
- `{{Supplier_Name}}` – Pole: Supplier_Name
- `{{Invoice_Number}}` – Pole: Invoice_Number
- `{{Invoice_Date}}` – Pole: Invoice_Date
- `{{Approving_Manager}}` – Pole lub stały użytkownik

**Referencja przewodnika:** [Przewodnik po przypisywaniu zadań](../then/task/task-assignment-guide.md)

---

### Krok 2C: Utwórz zadania podwójnego zatwierdzenia (> 10 000 €)

**Dwa kolejne zadania dla faktur o wysokiej wartości**

**Zadanie 1: Zatwierdzenie przez kierownika**
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

**Zadanie 2: Zatwierdzenie przez dyrektora (tworzone po ukończeniu zadania 1)**
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

### Krok 3: Przypisz zadanie użytkownikowi/grupie

**Karta:** ACTION_ASSIGN_TO_USER lub ACTION_ASSIGN_TO_GROUP

**Opcja 1: Przypisz do konkretnego użytkownika**
```
User: John.Smith@company.com
OR
User Field: {{DOCUMENT_FIELD:Approving_Manager}}
```

**Opcja 2: Przypisz do grupy**
```
Group: Finance Managers
Assignment Mode: First Available
OR
Assignment Mode: Round Robin
OR
Assignment Mode: All (everyone in group gets task)
```

**Opcja 3: Przypisanie sekwencyjne**
```
Card: ACTION_ASSIGN_SEQUENTIALLY_TO_USER

User 1: Finance_Manager
User 2: Finance_Director (only if User 1 approves)
User 3: CFO (only if User 2 approves)
```

**Referencja przewodnika:** [Przewodnik po przypisaniu](../then/assignee/assignment-user-guide.md)

---

### Krok 4: Wyślij powiadomienie e-mail

**Karta:** ACTION_SEND_EMAIL_TO_GROUPS

**Konfiguracja:**
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

**Zmienne e-mail:**
- `{{TASK_ASSIGNEE_EMAIL}}` – E-mail odbiorcy zadania
- `{{TASK_ASSIGNEE_NAME}}` – Nazwa odbiorcy zadania
- `{{DOCUMENT_NUMBER}}` – Identyfikator dokumentu
- `{{TASK_DEADLINE}}` – Termin zadania
- `{{TASK_PRIORITY}}` – Poziom priorytetu zadania
- `{{DOCUMENT_LINK}}` – Bezpośredni link do dokumentu

**Referencja przewodnika:** [Przewodnik po wysyłaniu e-maili do grup](../then/action/send-email-groups-guide.md)

---

### Krok 5: Śledź status zadania

**Karta:** CONDITION_TASK_STATUS lub podobny weryfikator statusu zadania

**Konfiguracja:**
```
Task ID: {{CREATED_TASK_ID}}
Status Check: IS COMPLETED
```

**Opcje statusu:**
- CREATED – Zadanie właśnie utworzone
- ASSIGNED – Zadanie przypisane użytkownikowi
- IN_PROGRESS – Użytkownik rozpoczął zadanie
- COMPLETED – Zadanie ukończone
- APPROVED – Zadanie zatwierdzone
- REJECTED – Zadanie odrzucone
- CANCELLED – Zadanie anulowane
- OVERDUE – Zadanie przeterminowane

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

### Krok 6: Zakończ workflow na podstawie wyniku zadania

**Po ukończeniu zadania:**

**Scenariusz A: Zadanie zatwierdzone**
```
1. Set field "Approval_Status" = "APPROVED"
2. Set field "Approved_By" = {{TASK_COMPLETED_BY}}
3. Set field "Approval_Date" = {{TASK_COMPLETED_DATE}}
4. ACTION_APPROVE_DOCUMENT
5. Export document (if configured)
```

**Scenariusz B: Zadanie odrzucone**
```
1. Set field "Approval_Status" = "REJECTED"
2. Set field "Rejected_By" = {{TASK_COMPLETED_BY}}
3. Set field "Rejection_Reason" = {{TASK_REJECTION_REASON}}
4. ACTION_REJECT_DOCUMENT
5. Send rejection notification to supplier
6. Create "Correction Needed" task
```

**Scenariusz C: Zadanie przeterminowane**
```
1. Set field "Task_Status" = "OVERDUE"
2. Create escalation task for manager
3. Send reminder email to original assignee
4. Send escalation email to manager
5. Log overdue event
```

---

## Kompletny diagram workflow

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

## Szablony konfiguracji

### Szablon 1: Proste zadanie zatwierdzenia

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

### Szablon 2: Zadanie przeglądu ze szczegółami

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

### Szablon 3: Zadanie eskalacji

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

## Zaawansowane wzorce

### Wzorzec 1: Sekwencyjne wielopoziomowe zatwierdzanie

**Zastosowanie:** Faktury muszą przejść przez kilku zatwierdzających kolejno

```
Level 1: Accounts Clerk (verify data)
  → IF APPROVED:
    Level 2: Accounts Manager (approve amount)
      → IF APPROVED:
        Level 3: Finance Director (final sign-off)
          → IF APPROVED:
            Document Approved ✅
```

**Wdrożenie:**
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

### Wzorzec 2: Równoległe zatwierdzanie przez wiele osób

**Zastosowanie:** Wiele osób musi zatwierdzić jednocześnie

```
Send to ALL approvers at once:
- Finance Manager
- Procurement Manager
- Quality Manager

Document approved only when ALL approve
```

**Wdrożenie:**
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

### Wzorzec 3: Warunkowe tworzenie zadań

**Zastosowanie:** Tworzenie różnych zadań na podstawie warunków

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

### Wzorzec 4: Eskalacja oparta na terminie

**Zastosowanie:** Automatyczna eskalacja, gdy zadanie nie zostanie ukończone w terminie

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

## Obsługa błędów

### Scenariusz 1: Nie znaleziono odbiorcy

**Problem:** Użytkownik nie istnieje lub jest nieaktywny

**Rozwiązanie:**
```
1. Check user status with CONDITION_USER_IS_ISNOT
2. IF User = INACTIVE:
     → Assign to backup user
     → OR Assign to user's group
     → Log warning
3. Send notification to admin
```

---

### Scenariusz 2: Tworzenie zadania nie powiodło się

**Problem:** Błąd systemowy podczas tworzenia zadania

**Rozwiązanie:**
```
1. Check task creation status
2. IF Failed:
     → Retry task creation
     → Send email notification instead
     → Create admin alert task
     → Log error details
```

---

### Scenariusz 3: Brak reakcji na zadanie

**Problem:** Użytkownik nie ukończy zadania w terminie

**Rozwiązanie:**
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

## Lista kontrolna testów

- [ ] Zadanie utworzone pomyślnie
- [ ] Zadanie przypisane właściwemu użytkownikowi/grupie
- [ ] Powiadomienie e-mail wysłane
- [ ] Zadanie pojawia się na liście zadań użytkownika
- [ ] Właściwości zadania poprawne (tytuł, opis, priorytet, termin)
- [ ] Użytkownik może ukończyć zadanie
- [ ] Workflow jest kontynuowany po ukończeniu zadania
- [ ] Workflow zatwierdzania działa poprawnie
- [ ] Workflow odrzucenia działa poprawnie
- [ ] Eskalacja jest wyzwalana we właściwym momencie
- [ ] Obsługa przeterminowania działa
- [ ] Wszystkie powiadomienia e-mail wysłane
- [ ] Aktualizacje pól działają poprawnie

---

## Przykłady z praktyki

### Przykład 1: Wyjątek w trójstronnym dopasowaniu PO

**Scenariusz:** Faktura nie zgadza się z zamówieniem, wymagany przegląd

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

### Przykład 2: Zatwierdzanie faktury dostawcy

**Scenariusz:** Faktura od nowego dostawcy wymaga specjalnego zatwierdzenia

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

### Przykład 3: Przetwarzanie na zamknięcie miesiąca

**Scenariusz:** Faktury z końca miesiąca wymagają pilnego przetwarzania

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

## Wskazówki dotyczące wydajności

✅ **Najlepsze praktyki:**
- Ustawiaj realistyczne terminy
- Używaj jasnych tytułów i opisów zadań
- Umieszczaj w zadaniu wszystkie niezbędne informacje
- Powiadamiaj na czas
- Monitoruj wskaźniki ukończenia zadań
- Automatycznie eskaluj przeterminowane zadania
- Rejestruj wszystkie aktywności zadań
- Przeglądaj wzorce zadań co miesiąc

❌ **Unikaj:**
- Tworzenia zadań do wszystkiego
- Niejasnych opisów zadań
- Nierealistycznych terminów
- Zbyt wielu e-maili powiadomień
- Braku ścieżki eskalacji
- Ignorowania przeterminowanych zadań
- Nieśledzenia wskaźników zadań

---

## Powiązane wzorce

### Wzorce, które dobrze ze sobą współgrają:

- **[Wzorzec integracji API](api-integration-pattern.md)** – Tworzenie zadań dla błędów API
- **[Wzorzec PO Matching](po-matching-pattern.md)** – Tworzenie zadań przy odchyleniach PO
- **[Wzorzec logiki decyzyjnej](decision-logic-pattern.md)** – Routing do odpowiedniego typu zadania
- **[Wzorzec transformacji danych](data-transformation-pattern.md)** – Transformacja danych przed utworzeniem zadania

---

## Powiązane przewodniki

### Wymagania wstępne
- [Przewodnik po przypisywaniu zadań](../then/task/task-assignment-guide.md) – Dokumentacja karty zadania
- [Przewodnik po przypisaniu](../then/assignee/assignment-user-guide.md) – Przypisanie użytkownika
- [Przewodnik po wysyłaniu e-maili do grup](../then/action/send-email-groups-guide.md) – Powiadomienia e-mail

### Powiązane karty
- **tasks_create** – [Przewodnik po przypisywaniu zadań](../then/task/task-assignment-guide.md)
- **ACTION_ASSIGN_TO_USER** – [Przewodnik po przypisaniu](../then/assignee/assignment-user-guide.md)
- **ACTION_SEND_EMAIL_TO_GROUPS** – [Przewodnik po e-mailach](../then/action/send-email-groups-guide.md)
- **CONDITION_TASK_STATUS** – [Przewodnik po kartach warunków](../and/condition-cards-complete-guide.md)

### Następne kroki
- Dodaj powiadomienia e-mail: [Przewodnik po e-mailach](../then/action/send-email-groups-guide.md)
- Wdróż złożony routing: [Wzorzec logiki decyzyjnej](decision-logic-pattern.md)

---

**Wersja wzorca:** 1.0
**Ostatnia aktualizacja:** 23 października 2025
**Trudność:** Niska-Średnia
**Szacowany czas:** 30–45 minut
**Wskaźnik sukcesu:** Bardzo wysoki
