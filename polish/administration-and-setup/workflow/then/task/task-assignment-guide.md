# Karty przydzielania zadań i tworzenia

## Karty przydziału zadań i tworzenia — kompletny przewodnik

**Okładki:** 12 kart związanych z zadaniami

***

Karty zadań na tej stronie znajdują się w grupie **Wtedy** Konstruktora przepływu pracy — akcje, które są uruchamiane po spełnieniu warunków Kiedy/I:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-pl.png" alt="Niezapisany przykład z kartami Kiedy, I oraz Wtedy. Uzupełnij wszystkie pola przed uruchomieniem. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs."><figcaption><p>Niezapisany przykład z kartami Kiedy, I oraz Wtedy. Uzupełnij wszystkie pola przed uruchomieniem. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs.</p></figcaption></figure>

***

### 📌 Informacje o wersji

**Najbardziej rozwinięta karta:** tasks\_create (4 wersje, najnowsza wersja 4) **Inne karty z wieloma wersjami:** ACTION\_TASK\_FOR\_GROUP (v4), ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP (v3), ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK (v3), ACTION\_DECISION\_TREE\_CREATE\_TASKS (v3)

**Kluczowe zmiany:**

* **v3 → v4 Ewolucja:** Usunięto podejście oparte na drzewie decyzyjnym, dodano ogólne typy elementów pracy (Zadanie, Zgłoszenie, Problem)
* **v2 → v3 Migracja:** Dodano obsługę drzew decyzyjnych (obecnie w większości przestarzałe)

📖 [Pełna historia wersji](../../release.md) | [Wersje kart i zachowanie](../../cards-overview/card-versions-guide.md)

***

### Przegląd

Karty zadań tworzą przydziały pracy dla członków zespołu. Gdy faktura wymaga zatwierdzenia, możesz automatycznie utworzyć zadanie i przypisać je odpowiedniej osobie.

***

## Podstawowe tworzenie zadań

### Karta: tasks\_create / Utwórz zadanie i przypisz użytkownikowi

#### Cel

Tworzy zadanie i przydziela je konkretnej osobie

#### Kiedy stosować

* Faktura wymaga sprawdzenia przez konkretną osobę
* Wymagana zgoda od wskazanej osoby
* Przekazanie konkretnemu członkowi zespołu

#### Parametry

**Tytuł** Nazwa/temat zadania

```
Example: "Review Invoice #INV-2025-001 for approval"
```

**Opis** Szczegóły dotyczące zadania

```
Example: "Invoice from Supplier ABC needs review.
Amount: €5000
Deadline: 2025-10-30
Please verify pricing and quality."
```

**Priorytet**

* 🔴 **Wysoki**: Pilne, wykonaj natychmiast
* 🟡 **Średni**: Normalny priorytet
* 🟢 **Niski**: Można to zrobić później

**Przypisany użytkownik** Kto otrzymuje zadanie

```
Example: John Smith (Finance Manager)
```

**Powiadomienie e-mail** Wysłać powiadomienie e-mailem do przypisanej osoby?

```
✅ Yes: Person gets email
❌ No: Task only in system
```

#### Przykład

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

### Karta: ACTION\_TASK\_FOR\_GROUP / Utwórz zadanie dla grupy

#### Cel

Tworzy zadanie i przypisuje je do grupy (wszyscy członkowie mogą je zobaczyć)

#### Kiedy stosować

* Zadanie może wykonać wiele osób
* Zadanie dla zespołu, a nie indywidualnego
* Pierwsza dostępna osoba powinna sobie poradzić

#### Różnica w stosunku do zadania indywidualnego

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

#### Przykładowy przepływ pracy

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

### Karta: ACTION\_DECISION\_TREE\_CREATE\_TASKS

#### Cel

Tworzy zadania w oparciu o logikę tabeli decyzyjnej

#### Jak to działa

```
Decision Table Returns:
  If invoice from Supplier A → Assign to Procurement
  If invoice from Supplier B → Assign to Quality Team
  If invoice from Supplier C → Assign to Finance

Task is automatically created and assigned
based on which condition is true
```

#### Kiedy stosować

* Różni dostawcy potrzebują różnych zezwoleń
* Złożone wyznaczanie tras w oparciu o wiele czynników
* Inny zespół w zależności od typu dokumentu

#### Przykład

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

### Karta: ACTION\_DECISION\_TREE\_TASKS\_SEQUENTIAL

#### Cel

Tworzy zadania sekwencyjnie w oparciu o tabelę decyzyjną. Zadania są przydzielane pojedynczo z zachowaniem kolejności priorytetów

#### Kiedy stosować

* Wymaganych jest wiele zatwierdzeń w kolejności
* Łańcuch zatwierdzania przepływu pracy
* Każda osoba recenzuje, a następnie przechodzi do następnej

#### Jak to działa

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

#### System priorytetowy

```
Priority 1 → Assign to: Person A
Priority 2 → Assign to: Person B
Priority 3 → Assign to: Person C

They must complete in order (1→2→3)
```

#### Przykładowa konfiguracja

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

### Karta: ACTION\_CREATE\_TASK\_FOR\_USER\_SEQUENTIAL

#### Cel

Przypisuje dokument do jednego użytkownika ORAZ tworzy zadanie sekwencyjne

#### Kiedy stosować

* Przypisz dokument ORAZ utwórz zadanie w tym samym czasie
* Dokument wymaga sprawdzenia przez konkretną osobę
* Śledź zarówno przydział, jak i tworzenie zadań

#### Jak to działa

```
Two things happen:
1. Document is assigned to: Person A
2. Task is created for: Person A

Both in one action
```

#### Przykład

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

### Karta: ACTION\_CREATE\_TASK\_FOR\_GROUP\_SEQUENTIAL

#### Cel

Przypisuje dokument do grupy ORAZ tworzy zadanie

#### Kiedy stosować

* Dokument wymaga uwagi grupy
* Chcesz śledzić tworzenie zadań
* Utwórz początkowe zadanie, a następnie przypisz dokument

#### Przykład

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

## Zaawansowane tworzenie zadań

### Karta: ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP

#### Cel

Tworzy zadanie dla określonej grupy obiektów

#### Kiedy stosować

* Zadanie dla zespołu magazynu/obiektu
* Operacje specyficzne dla obiektu
* Lokalizacja fizyczna ma znaczenie

#### Przykład

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

### Karta: ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP\_SEQUENTIAL

#### Cel

Sekwencyjne przydzielanie zadań pomiędzy obiektami

#### Kiedy stosować

* Operacje wieloobiektowe
* Zadania przechodzą z placówki do placówki
* Sekwencyjne przetwarzanie obiektów

#### Jak to działa

```
Factory A (Step 1): Production
    ↓
Quality Check (Step 2): Verification
    ↓
Warehouse (Step 3): Packaging
    ↓
Shipping (Step 4): Dispatch
```

#### Przykład

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

### Karta: ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP

#### Cel

Tworzy zadanie dla działu zakupów

#### Kiedy stosować

* Zadanie dla zespołu zakupowego
* Zadania związane z zarządzaniem dostawcami
* Praca związana z zakupami

#### Przykład

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

### Karta: ACTION\_ASSIGN\_TASK\_PROCUREMENT\_GROUP\_SEQUENTIAL

#### Cel

Sekwencyjne kierowanie zadań w ramach zaopatrzenia

#### Kiedy stosować

* Wieloetapowe procesy zakupowe
* Łańcuch akceptacji w zakupach
* Ścieżka eskalacji

#### Przykład

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

### Karta: ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK

#### Cel

Pobierz użytkownika z pola dokumentu, przypisz zadanie. Jeśli użytkownik nie zostanie znaleziony, użyj użytkownika zastępczego

#### Kiedy stosować

* Użytkownik zapisany w polu dokumentu
* Dokument określa, kto powinien dokonać przeglądu
* Miej osobę zastępczą, jeśli określony użytkownik jest niedostępny

#### Jak to działa

```
Document has field: "Approver Name: John Smith"

Card checks: Is John in system?
    If YES → Assign task to John
    If NO → Assign to Fallback User (Sarah)
```

#### Przykład

```
Invoice field: "Contact: Mike Johnson"

Try to assign task to Mike Johnson
    ↓
If Mike doesn't exist in system:
    ↓
Use Fallback: Team Lead (Robert Brown)
```

#### Parametry

```
- Field to Read: "Approver Name"
- Fallback User: Robert Brown
- Task Details: Title, Description, Priority
```

***

## Typowe parametry zadania

Wszystkie karty zadań korzystają z tych parametrów:

#### Tytuł

```
Good: "Review Invoice #INV-12345 - €5000 - Supplier ABC"
Bad: "Approve something"
```

#### Opis

```
Should include:
✅ What to do
✅ Deadline
✅ Any special requirements
✅ Who to contact
✅ Link to document
```

#### Poziomy priorytetów

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

#### Termin płatności (jeśli jest dostępny)

```
When should task be completed by?
Example: 2025-10-30 (5 days from now)
```

***

## Scenariusze przepływu zadań

### Scenariusz 1: Proste zatwierdzenie

```
Invoice Arrives (€2000)
    ↓
Condition: Amount between €1000-€5000?
    ↓
YES: Create Task for Finance Manager
    ↓
Finance Manager reviews and approves
```

### Scenariusz 2: Zatwierdzenie wielopoziomowe

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

### Scenariusz 3: Zadania równoległe

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

### Scenariusz 4: Routing warunkowy

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

## Najlepsze praktyki w zakresie przydzielania zadań

✅ **Wykonaj:**

* Uwzględnij szczegółowe informacje w tytule zadania
* Ustaw odpowiednie poziomy priorytetów
* Ustal realistyczne terminy
* Powiadom cesjonariuszy
* Dołącz link do dokumentu
* Używaj jasnych, praktycznych opisów

❌ **Nie:**

* Twórz niejasne tytuły zadań („Przejrzyj to”)
* Ustaw wszystko jako Wysoki priorytet
* Zapomnij powiadomić wyznaczoną osobę
* Utwórz wiele zadań dla tej samej pracy
* Przypisz do niedostępnych osób

***

## Zadania rozwiązywania problemów

### „Zadanie nie przydzielone nikomu”

**Przyczyna:** Użytkownik nie istnieje lub grupa jest pusta

**Rozwiązanie:**

* Sprawdź pisownię nazwy użytkownika
* Sprawdź, czy użytkownik jest aktywny w systemie
* Sprawdź, czy grupa ma członków
* W razie potrzeby użyj opcji zastępczej

### „Osoba twierdzi, że nie otrzymała powiadomienia”

**Przyczyna:** Powiadomienia e-mail wyłączone lub nieprawidłowy e-mail

**Rozwiązanie:**

* Sprawdź, czy pole wyboru „Wyślij e-mail” jest włączone
* Zweryfikuj adres e-mail odbiorcy
* Sprawdź folder spamu
* Wyślij ponownie powiadomienie ręcznie

### „Niewłaściwa osoba dostała zadanie”

**Przyczyna:** Nieprawidłowa logika routingu

**Rozwiązanie:**

* Sprawdź warunki tabeli decyzyjnej
* Sprawdź ustawienia awaryjne
* Przetestuj na przykładowym dokumencie
* Sprawdź literówki w nazwach użytkowników

### „Utworzono zbyt wiele zadań”

**Przyczyna:** Wielokrotne uruchomienie karty

**Rozwiązanie:**

* Sprawdź, czy warunki są wystarczająco szczegółowe
* Sprawdź, czy karta działa tylko raz na dokument
* Przejrzyj warunki „i”.
* Dodaj dodatkowe filtrowanie

***

## Tabela porównawcza kart zadań

| Karta                                                        | Tworzy zadanie | Przypisuje do            | When        |
| ----------------------------------------------------------- | ------------ | --------------------- | ----------- |
| tasks\_create                                               | Tak          | Indywidualny            | Zawsze      |
| ACTION\_TASK\_FOR\_GROUP                                    | Tak          | Grupa                 | Zawsze      |
| ACTION\_DECISION\_TREE\_CREATE\_TASKS                       | Tak          | Wynik tabeli decyzyjnej | Warunkowe |
| ACTION\_DECISION\_TREE\_TASKS\_SEQUENTIAL                   | Tak          | Wiele (sekwencyjne) | Warunkowe |
| ACTION\_CREATE\_TASK\_FOR\_USER\_SEQUENTIAL                 | Tak          | Użytkownik + dokument       | Warunkowe |
| ACTION\_CREATE\_TASK\_FOR\_GROUP\_SEQUENTIAL                | Tak          | Grupa + dokument      | Warunkowe |
| ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP                   | Tak          | Grupa Obiektów        | Warunkowe |
| ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP\_SEQUENTIAL       | Tak          | Wiele obiektów   | Warunkowe |
| ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP                | Tak          | Zespół ds. zakupów      | Warunkowe |
| ACTION\_ASSIGN\_TASK\_PROCUREMENT\_GROUP\_SEQUENTIAL        | Tak          | Wiele (sekwencyjne) | Warunkowe |
| ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK | Tak          | Pole/awaria        | Warunkowe |

***

## Powiązane karty

* **ACTION\_ASSIGN\_DOCUMENT\_TO\_USER** – Przypisz dokument bez tworzenia zadania
* **ACTION\_SEND\_EMAIL** — Powiadom osoby bezpośrednio
* **STAUS\_CHANGE** – Zmień status zamiast tworzyć zadanie
* **RUN\_WORKFLOW** – Zamiast tego wyzwalaj inny przepływ pracy
