# Task Assignment & Creation Cards - Complete Guide

Te karty trafiają do grupy **Then** w Kreatorze przepływów — akcje uruchamiane po spełnieniu warunków When/And:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Karty dodaje się do grupy <strong>Then</strong> za pomocą <strong>Add Card</strong>.</p></figcaption></figure>

**Obejmuje:** 12 kart związanych z zadaniami

---

## Przegląd

Karty zadań tworzą przydziały pracy dla członków zespołu. Gdy faktura wymaga zatwierdzenia, możesz automatycznie utworzyć zadanie i przypisać je do właściwej osoby.

---

# Podstawowe tworzenie zadań

## Karta: tasks_create / Create Task and Assign to User

### Cel
Tworzy zadanie i przypisuje je do konkretnej osoby

### Kiedy używać
- Faktura wymaga przeglądu przez konkretną osobę
- Wymagane zatwierdzenie od imiennie wskazanej osoby
- Przekazanie konkretnemu członkowi zespołu

### Parametry

**Title**
Nazwa/temat zadania
```
Example: "Review Invoice #INV-2025-001 for approval"
```

**Description**
Szczegóły zadania
```
Example: "Invoice from Supplier ABC needs review.
Amount: €5000
Deadline: 2025-10-30
Please verify pricing and quality."
```

**Priority**
- 🔴 **High**: Pilne, wykonaj natychmiast
- 🟡 **Medium**: Normalny priorytet
- 🟢 **Low**: Może być wykonane później

**Assigned User**
Kto otrzymuje zadanie
```
Example: John Smith (Finance Manager)
```

**Email Notification**
Wysłać alert e-mail do przypisanej osoby?
```
✅ Yes: Person gets email
❌ No: Task only in system
```

### Przykład
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

## Karta: ACTION_TASK_FOR_GROUP / Create Task for Group

### Cel
Tworzy zadanie i przypisuje je do grupy (wszyscy członkowie mogą je zobaczyć)

### Kiedy używać
- Wiele osób może wykonać zadanie
- Zadanie dla zespołu, nie dla osoby indywidualnej
- Pierwsza dostępna osoba powinna je obsłużyć

### Różnica względem zadania indywidualnego
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

### Przykładowy przepływ pracy
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

## Karta: ACTION_DECISION_TREE_CREATE_TASKS

### Cel
Tworzy zadania na podstawie logiki tabeli decyzyjnej

### Jak to działa
```
Decision Table Returns:
  If invoice from Supplier A → Assign to Procurement
  If invoice from Supplier B → Assign to Quality Team
  If invoice from Supplier C → Assign to Finance

Task is automatically created and assigned
based on which condition is true
```

### Kiedy używać
- Różni dostawcy wymagają różnego zatwierdzenia
- Złożony routing na podstawie wielu czynników
- Różny zespół na podstawie typu dokumentu

### Przykład
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

## Karta: ACTION_DECISION_TREE_TASKS_SEQUENTIAL

### Cel
Tworzy zadania sekwencyjnie na podstawie tabeli decyzyjnej
Zadania są przypisywane pojedynczo z kolejnością priorytetów

### Kiedy używać
- Potrzeba wielu zatwierdzeń w sekwencji
- Łańcuch zatwierdzania przepływu pracy
- Każda osoba przegląda, a następnie przekazuje dalej

### Jak to działa
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

### System priorytetów
```
Priority 1 → Assign to: Person A
Priority 2 → Assign to: Person B
Priority 3 → Assign to: Person C

They must complete in order (1→2→3)
```

### Przykładowa konfiguracja
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

## Karta: ACTION_CREATE_TASK_FOR_USER_SEQUENTIAL

### Cel
Przypisuje dokument do jednego użytkownika ORAZ tworzy zadanie sekwencyjne

### Kiedy używać
- Przypisz dokument ORAZ utwórz zadanie jednocześnie
- Dokument wymaga przeglądu przez konkretną osobę
- Śledzenie zarówno przypisania, jak i tworzenia zadania

### Jak to działa
```
Two things happen:
1. Document is assigned to: Person A
2. Task is created for: Person A

Both in one action
```

### Przykład
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

## Karta: ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL

### Cel
Przypisuje dokument do grupy ORAZ tworzy zadanie

### Kiedy używać
- Dokument wymaga uwagi grupy
- Chcesz śledzić tworzenie zadania
- Utwórz początkowe zadanie, a następnie przypisanie dokumentu

### Przykład
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

# Zaawansowane tworzenie zadań

## Karta: ACTION_ASSIGN_TASK_TO_FACILITY_GROUP

### Cel
Tworzy zadanie dla określonej grupy obiektu

### Kiedy używać
- Zadanie dla zespołu magazynu/obiektu
- Operacje specyficzne dla obiektu
- Liczy się fizyczna lokalizacja

### Przykład
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

## Karta: ACTION_ASSIGN_TASK_TO_FACILITY_GROUP_SEQUENTIAL

### Cel
Sekwencyjne przypisanie zadań między obiektami

### Kiedy używać
- Operacje wieloobiektowe
- Zadania przechodzą z obiektu do obiektu
- Sekwencyjne przetwarzanie obiektów

### Jak to działa
```
Factory A (Step 1): Production
    ↓
Quality Check (Step 2): Verification
    ↓
Warehouse (Step 3): Packaging
    ↓
Shipping (Step 4): Dispatch
```

### Przykład
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

## Karta: ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP

### Cel
Tworzy zadanie dla działu zakupów

### Kiedy używać
- Zadanie dla zespołu zakupowego
- Zadania zarządzania dostawcami
- Praca związana z zakupami

### Przykład
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

## Karta: ACTION_ASSIGN_TASK_PROCUREMENT_GROUP_SEQUENTIAL

### Cel
Sekwencyjny routing zadań w ramach zakupów

### Kiedy używać
- Wieloetapowe procesy zakupowe
- Łańcuch zatwierdzania w zakupach
- Ścieżka eskalacji

### Przykład
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

## Karta: ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK

### Cel
Pobierz użytkownika z pola dokumentu, przypisz zadanie
Jeśli użytkownik nie zostanie znaleziony, użyj użytkownika zapasowego

### Kiedy używać
- Użytkownik przechowywany w polu dokumentu
- Dokument określa, kto powinien przeprowadzić przegląd
- Miej osobę zapasową, jeśli określony użytkownik jest niedostępny

### Jak to działa
```
Document has field: "Approver Name: John Smith"

Card checks: Is John in system?
    If YES → Assign task to John
    If NO → Assign to Fallback User (Sarah)
```

### Przykład
```
Invoice field: "Contact: Mike Johnson"

Try to assign task to Mike Johnson
    ↓
If Mike doesn't exist in system:
    ↓
Use Fallback: Team Lead (Robert Brown)
```

### Parametry
```
- Field to Read: "Approver Name"
- Fallback User: Robert Brown
- Task Details: Title, Description, Priority
```

---

# Typowe parametry zadań

Wszystkie karty zadań używają tych parametrów:

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

### Poziomy priorytetu
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

### Due Date (jeśli dostępne)
```
When should task be completed by?
Example: 2025-10-30 (5 days from now)
```

---

# Scenariusze przepływu pracy zadań

## Scenariusz 1: Proste zatwierdzenie
```
Invoice Arrives (€2000)
    ↓
Condition: Amount between €1000-€5000?
    ↓
YES: Create Task for Finance Manager
    ↓
Finance Manager reviews and approves
```

## Scenariusz 2: Zatwierdzenie wielopoziomowe
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

## Scenariusz 3: Zadania równoległe
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

## Scenariusz 4: Routing warunkowy
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

# Najlepsze praktyki przypisywania zadań

✅ **Rób:**
- Uwzględnij konkretne szczegóły w tytule zadania
- Ustaw odpowiednie poziomy priorytetu
- Ustaw realistyczne terminy
- Powiadom osoby przypisane
- Dołącz łącze do dokumentu
- Używaj jasnych, gotowych do działania opisów

❌ **Nie rób:**
- Nie twórz niejasnych tytułów zadań ("Review this")
- Nie ustawiaj wszystkiego jako wysoki priorytet
- Nie zapominaj o powiadomieniu przypisanej osoby
- Nie twórz wielu zadań dla tej samej pracy
- Nie przypisuj do niedostępnych osób

---

# Rozwiązywanie problemów z zadaniami

## "Task not assigned to anyone"
**Przyczyna:** Użytkownik nie istnieje lub grupa jest pusta

**Rozwiązanie:**
- Zweryfikuj pisownię nazwy użytkownika
- Sprawdź, czy użytkownik jest aktywny w systemie
- Zweryfikuj, czy grupa ma członków
- W razie potrzeby użyj rozwiązania zapasowego

## "Person says they didn't get notification"
**Przyczyna:** Powiadomienie e-mail wyłączone lub nieprawidłowy e-mail

**Rozwiązanie:**
- Sprawdź, czy pole wyboru "Send Email" jest włączone
- Zweryfikuj adres e-mail odbiorcy
- Sprawdź folder spamu
- Wyślij powiadomienie ponownie ręcznie

## "Wrong person got task"
**Przyczyna:** Nieprawidłowa logika routingu

**Rozwiązanie:**
- Sprawdź warunki tabeli decyzyjnej
- Zweryfikuj ustawienia rozwiązania zapasowego
- Przetestuj z przykładowym dokumentem
- Sprawdź literówki w nazwach użytkowników

## "Too many tasks created"
**Przyczyna:** Karta uruchamia się wielokrotnie

**Rozwiązanie:**
- Sprawdź, czy warunki są wystarczająco konkretne
- Zweryfikuj, czy karta uruchamia się tylko raz na dokument
- Przejrzyj warunki "And"
- Dodaj dodatkowe filtrowanie

---

# Tabela porównawcza kart zadań

| Karta | Tworzy zadanie | Przypisuje do | Kiedy |
|------|-------------|-----------|------|
| tasks_create | Tak | Osoba indywidualna | Zawsze |
| ACTION_TASK_FOR_GROUP | Tak | Grupa | Zawsze |
| ACTION_DECISION_TREE_CREATE_TASKS | Tak | Wynik tabeli decyzyjnej | Warunkowo |
| ACTION_DECISION_TREE_TASKS_SEQUENTIAL | Tak | Wiele (sekwencyjnie) | Warunkowo |
| ACTION_CREATE_TASK_FOR_USER_SEQUENTIAL | Tak | Użytkownik + dokument | Warunkowo |
| ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL | Tak | Grupa + dokument | Warunkowo |
| ACTION_ASSIGN_TASK_TO_FACILITY_GROUP | Tak | Grupa obiektu | Warunkowo |
| ACTION_ASSIGN_TASK_TO_FACILITY_GROUP_SEQUENTIAL | Tak | Wiele obiektów | Warunkowo |
| ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP | Tak | Zespół zakupowy | Warunkowo |
| ACTION_ASSIGN_TASK_PROCUREMENT_GROUP_SEQUENTIAL | Tak | Wiele (sekwencyjnie) | Warunkowo |
| ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK | Tak | Pole/Rozwiązanie zapasowe | Warunkowo |

---

# Powiązane karty

- **ACTION_ASSIGN_DOCUMENT_TO_USER** - Przypisz dokument bez tworzenia zadania
- **ACTION_SEND_EMAIL** - Powiadom osoby bezpośrednio
- **STAUS_CHANGE** - Zmień status zamiast tworzyć zadanie
- **RUN_WORKFLOW** - Uruchom inny przepływ pracy zamiast tego
