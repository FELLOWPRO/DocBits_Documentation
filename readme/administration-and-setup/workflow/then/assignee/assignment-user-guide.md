# Document Assignment & User Cards - Complete Guide

Te karty trafiają do grupy **Then** w Kreatorze przepływów — akcje uruchamiane po spełnieniu warunków When/And:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Karty dodaje się do grupy <strong>Then</strong> za pomocą <strong>Add Card</strong>.</p></figcaption></figure>

**Obejmuje:** 13 kart związanych z przypisaniem i użytkownikami

---

## 📌 Informacje o wersji

**Karty wielowersyjne:** DOC_USER_ASSIGN (v2 najnowsza, v3 wycofana), DOC_GROUP_ASSIGN (v2 najnowsza, v3 wycofana), OC_ASSIGN_DOC (v2)

**Ważne:** Wersje v3 dodały obsługę drzewa decyzyjnego, ale są teraz wycofane
**Zalecenie:** Użyj v2 zarówno dla DOC_USER_ASSIGN, jak i DOC_GROUP_ASSIGN

📖 [Pełna historia wersji](../../../changelog/release.md#-assignment--routing-cards) | [Baza danych wersji kart](../../../../DocFlow/docs/card_version.md)

---

# Podstawowe przypisanie dokumentu

## Karta: DOC_USER_ASSIGN / Assign Document to User

### Cel
Przypisuje dokument do konkretnej osoby w celu podjęcia przez nią działania

### Kiedy używać
- Dokument wymaga przeglądu przez konkretną osobę
- Przekazanie indywidualnemu członkowi zespołu
- Śledzenie odpowiedzialności
- Przypisanie pracy do imiennie wskazanej osoby

### Jak to działa
```
Document is "assigned to" = John Smith
Only John can see it as assigned to him
John is responsible for this document
```

### Przykład
```
Invoice arrives
    ↓
Assign Document to: John Smith (Finance Manager)
    ↓
Only John sees "Assigned to Me"
John must take action on it
```

### Parametry
```
User: [Select which person]
```

### Uwaga
Przypisanie oznacza:
- Dokument pokazuje się jako "assigned to me" dla tej osoby
- Ta osoba jest odpowiedzialna
- Inni nadal mogą widzieć dokument (ale nie jako przypisany do nich)
- Jedno przypisanie na raz na dokument

---

## Karta: DOC_GROUP_ASSIGN / Assign Document to Group

### Cel
Przypisuje dokument do grupy (wszyscy członkowie widzą go jako przypisany do nich)

### Kiedy używać
- Dokument dla zespołu, nie dla osoby indywidualnej
- Wiele osób może go obsłużyć
- Współdzielona odpowiedzialność
- Dystrybucja obciążenia zespołu

### Jak to działa
```
Document is "assigned to" = Finance Team (10 people)
All 10 team members see "Assigned to My Group"
Any team member can take action
```

### Przykład
```
New vendor invoice
    ↓
Assign Document to: Procurement Team
    ↓
All procurement team members see it
First available person handles it
```

### Parametry
```
Group: [Select which group]
```

### Różnica
```
Individual Assignment:
- One person responsible
- That person sees "Assigned to Me"
- Others don't see assignment

Group Assignment:
- Team responsible
- All members see "Assigned to My Group"
- Anyone can claim/process
```

---

## Karta: ACTION_ASSIGN_DOC_BASED_ON_DECISION_TABLE

### Cel
Przypisuje dokument na podstawie logiki tabeli decyzyjnej

### Kiedy używać
- Różni dostawcy wymagają różnych osób obsługujących
- Przypisanie na podstawie kwoty
- Złożona logika routingu
- Wiele warunków przypisania

### Jak to działa
```
Decision Table Logic:
  If Supplier = "ABC Corp" → Assign to: Procurement Team
  If Supplier = "XYZ Inc" → Assign to: Direct Manager
  If Amount > €10000 → Assign to: Finance Director

Document arrives
    ↓
Check: Which condition matches?
    ↓
Assign accordingly
```

### Przykład: Przypisanie na podstawie kwoty
```
Invoice: €2000 from ABC Corp

Decision Table checks:
  Is amount > €10000? NO
  Is amount > €5000? NO
  Is amount > €1000? YES

Result: Assign to: Finance Manager
```

### Przykład: Przypisanie na podstawie dostawcy
```
Invoice from: Preferred Supplier

Decision Table:
  If preferred supplier → Finance Team
  If new supplier → Procurement Manager
  If blacklisted → Director Review

Result: Assign to: Finance Team
```

### Parametry
```
Decision Table: [Select decision table]
(Decision table contains assignment logic)
```

---

## Karta: ACTION_ASSIGN_DOC_DECISION_TABLE_SEQUENTIAL

### Cel
Przypisuje dokument sekwencyjnie na podstawie tabeli decyzyjnej z priorytetami

### Kiedy używać
- Wiele kolejnych zatwierdzeń
- Różne osoby na różnych poziomach
- Łańcuch zatwierdzania na podstawie kwoty
- Ścieżka eskalacji

### Jak to działa
```
First Decision: Who approves first?
    ↓
Assign to: Person 1
    ↓
Person 1 approves
    ↓
Second Decision: Who approves next?
    ↓
Assign to: Person 2
    ↓
Person 2 approves (final)
    ↓
Document Complete
```

### System priorytetów
```
Priority 1: First assignment
Priority 2: Second assignment
Priority 3: Third assignment
(etc.)

Each must complete before next begins
```

### Przykład: Zatwierdzenie wielopoziomowe
```
Invoice: €50,000

Decision Table:
  €1k-€5k → Assign to: Finance Manager (Priority 1)
  €5k-€20k → Then: Assign to: Finance Director (Priority 2)
  €20k+ → Then: Assign to: CFO (Priority 3)

Invoice Flow:
1. Finance Manager reviews → approves
2. Finance Director reviews → approves
3. CFO reviews → approves final

Each step depends on previous completion
```

### Parametry
```
Decision Table: [Select]
Priority Order: [Determined by decision table]
```

---

## Karta: ACTION_ASSIGN_DOC_TO_USER_SEQUENTIAL

### Cel
Przypisuje dokument do użytkownika z priorytetem sekwencyjnym

### Kiedy używać
- Dokument wymaga konkretnej osoby
- Wyraźne przetwarzanie sekwencyjne
- Pojedyncze przypisanie z kolejnością

### Jak to działa
```
Assign Document to: User A (Priority 1)
    ↓
User A processes
    ↓
Then: Assign to User B (Priority 2)
    ↓
User B processes
```

### Przykład
```
Invoice processing:
1. Assign to: Accounts Payable Clerk
2. Then: Assign to: Finance Manager
3. Then: Assign to: Director

Each person has their turn
```

---

## Karta: ACTION_ASSIGN_DOC_TO_GROUP_SEQUENTIAL

### Cel
Przypisuje dokument sekwencyjnie do grup

### Kiedy używać
- Wiele zatwierdzeń grupowych
- Różne działy na każdym etapie
- Przetwarzanie sekwencyjne oparte na zespołach

### Jak to działa
```
Step 1: Assign to Group A (Quality Team)
        Quality verifies
    ↓
Step 2: Assign to Group B (Finance Team)
        Finance reviews
    ↓
Step 3: Assign to Group C (Procurement)
        Procurement approves
```

### Przykład
```
New Supplier Onboarding:

Step 1: Quality Team
  - Evaluate supplier capability
  - Check certifications

Step 2: Finance Team
  - Check payment terms
  - Verify pricing

Step 3: Procurement Team
  - Approve supplier
  - Set up in system

Document passes through all three
```

---

## Karta: ACTION_ASSIGN_DOC_TO_FACILITY_GROUP

### Cel
Przypisuje dokument do określonej grupy obiektu

### Kiedy używać
- Dokument dla konkretnego magazynu/obiektu
- Operacje oparte na obiekcie
- Przetwarzanie specyficzne dla lokalizacji

### Przykład
```
Shipment notification

Assign to: Berlin Warehouse Team
    ↓
Berlin warehouse processes shipment
    ↓
Or

Assign to: Munich Warehouse Team
    ↓
Munich warehouse processes shipment
```

---

## Karta: ACTION_ASSIGN_DOC_TO_FACILITY_GROUP_SEQUENTIAL

### Cel
Przypisuje sekwencyjnie między obiektami

### Kiedy używać
- Przetwarzanie wielolokalizacyjne
- Wysyłka przechodzi przez obiekty
- Przepływ pracy oparty na lokalizacji

### Przykład
```
Manufacturing Order:

Step 1: Factory A (Manufacturing) - Build product
Step 2: Quality Center (Testing) - Test product
Step 3: Distribution Center (Packing) - Package
Step 4: Warehouse (Storage) - Store

Document/shipment passes through each
```

---

## Karta: ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP

### Cel
Przypisuje dokument do działu zakupów

### Kiedy używać
- Obsługa przez zespół zakupowy
- Praca związana z dostawcami
- Związane z zamówieniem zakupu

### Przykład
```
Vendor evaluation document
    ↓
Assign to: Procurement Group
    ↓
Procurement team evaluates vendor
```

---

## Karta: ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP_SEQUENTIAL

### Cel
Przypisanie sekwencyjne w ramach zakupów

### Kiedy używać
- Wieloetapowy proces zakupowy
- Łańcuch zatwierdzania w zakupach

### Przykład
```
Purchase Requisition:

Step 1: Buyer (Creates PO)
Step 2: Approver (Reviews)
Step 3: Director (Final sign-off)

Each step in sequence
```

---

## Karta: ACTION_CHANGE_DOC_SUBORG / Change Document Sub-Organization

### Cel
Przypisuje dokument do innej sub-organizacji

### Kiedy używać
- Wybrano niewłaściwą organizację
- Trzeba przenieść do właściwego działu
- Restrukturyzacja organizacyjna

### Jak to działa
```
Current Sub-Org: Finance Department
    ↓
Change to: Accounting Department
    ↓
Document now belongs to Accounting
```

### Przykład
```
Document for: Berlin Office
    ↓
Realize should be: Munich Office
    ↓
Change Sub-Organization to: Munich Office
```

---

## Karta: ACTION_CHANGE_DOC_SUBORG_BY_FIELD_TEXT

### Cel
Zmienia sub-organizację na podstawie wartości pola dokumentu

### Kiedy używać
- Sub-organizacja przechowywana w polu
- Dopasowanie lokalizacji dokumentu do pola
- Automatyczne przypisanie organizacji

### Jak to działa
```
Document Field: "Delivery_Location" = "Berlin"
    ↓
Decision Table:
  If location = "Berlin" → Assign to: Berlin Sub-Org
  If location = "Munich" → Assign to: Munich Sub-Org

    ↓
Document assigned to: Berlin Sub-Org
```

### Przykład
```
Invoice field: "Cost Center: CC-Berlin-001"
    ↓
System recognizes: Berlin location
    ↓
Change document to: Berlin Sub-Organization
```

---

## Karta: ACTION_ASSIGN_USER_FROM_FIELD_WITH_FALLBACK

### Cel
Przypisuje dokument do użytkownika z pola, z rozwiązaniem zapasowym, jeśli użytkownik nie zostanie znaleziony

### Kiedy używać
- Nazwa użytkownika przechowywana w polu dokumentu
- Może nie istnieć w systemie
- Potrzebne rozwiązanie zapasowe, jeśli użytkownik jest niedostępny

### Jak to działa
```
Document Field: "Approver: John Smith"
    ↓
Try to assign to: John Smith
    ↓
If John doesn't exist:
    ↓
Use Fallback: Sarah Johnson (Manager)
    ↓
Document assigned to: Sarah Johnson
```

### Parametry
```
Source Field: [Field containing user name]
Fallback User: [If source user not found]
```

### Przykład
```
Invoice has field: "Contact Person: Mike Johnson"

Try to assign to: Mike Johnson
    ↓
If Mike not in system:
    ↓
Fallback to: Finance Manager (Robert)
```

---

## Karta: ACTION_ASSIGN_USER_TO_SUPPLIER

### Cel
Przypisuje dokument do użytkownika, który zarządza tym dostawcą

### Kiedy używać
- Użytkownik powiązany z dostawcą
- Opiekun konta dostawcy
- Właściciel relacji z dostawcą

### Jak to działa
```
Document Supplier: ABC Corp
    ↓
System checks: Who manages ABC Corp?
    ↓
Assign to: John Smith (ABC Corp Account Manager)
```

---

# Drzewa decyzyjne przypisania

## Przykład tabeli decyzyjnej 1: Na podstawie kwoty
```
Amount ≤ €1000
  → Assign to: Finance Team

Amount €1000-€5000
  → Assign to: Finance Manager

Amount €5000-€20000
  → Assign to: Finance Director

Amount > €20000
  → Assign to: CFO
```

## Przykład tabeli decyzyjnej 2: Na podstawie dostawcy
```
Supplier Type = "Preferred"
  → Assign to: Account Manager

Supplier Type = "New"
  → Assign to: Procurement Manager

Supplier Type = "Problem"
  → Assign to: Procurement Director
```

## Przykład tabeli decyzyjnej 3: Na podstawie typu dokumentu
```
Document Type = "Invoice"
  → Assign to: Accounts Payable Team

Document Type = "Credit Memo"
  → Assign to: Finance Manager

Document Type = "PO"
  → Assign to: Procurement Team
```

---

# Przykłady przepływów pracy przypisania

## Przykład 1: Prosty routing
```
Document Arrives
    ↓
Check: Supplier = "ABC Corp"? YES
    ↓
Assign to: John Smith
(John handles ABC Corp)
    ↓
John reviews and approves
```

## Przykład 2: Zatwierdzenie sekwencyjne
```
Document Arrives
    ↓
Assign to: Finance Manager (Step 1)
    ↓
Manager reviews
    ↓
Passes to: Finance Director (Step 2)
    ↓
Director reviews
    ↓
Passes to: CFO (Step 3)
    ↓
CFO approves final
```

## Przykład 3: Routing na podstawie kwoty
```
Invoice: €50,000
    ↓
Decision Table: Amount > €20k?
    ↓
YES → Assign to: CFO
    ↓
CFO approves directly
```

## Przykład 4: Na podstawie obiektu
```
Shipment for: Berlin Office
    ↓
Assign to: Berlin Warehouse Team
    ↓
Then assign to: Berlin Distribution Team
    ↓
Both teams process in sequence
```

---

# Najlepsze praktyki przypisania

✅ **Rób:**
- Utrzymuj tabele decyzyjne proste
- Testuj logikę routingu z próbkami
- Zapewnij, że wszystkie ścieżki prowadzą gdzieś
- Miej rozwiązanie zapasowe dla brakujących użytkowników
- Dokumentuj decyzje dotyczące routingu

❌ **Nie rób:**
- Nie twórz przypisań cyklicznych (A→B→A)
- Nie przypisuj do nieistniejących użytkowników (bez rozwiązania zapasowego)
- Nie czyń routingu zbyt złożonym
- Nie zapominaj o przetestowaniu routingu
- Nie przypisuj do niedostępnych osób

---

# Rozwiązywanie problemów z przypisaniem

## "Document not assigned"
**Przyczyna:** Warunek niespełniony lub użytkownik nie istnieje

**Rozwiązanie:**
- Sprawdź, czy warunek jest prawdziwy
- Zweryfikuj, czy użytkownik istnieje w systemie
- Sprawdź ustawienia rozwiązania zapasowego
- Przejrzyj logikę tabeli decyzyjnej

## "Wrong person assigned"
**Przyczyna:** Nieprawidłowa tabela decyzyjna lub logika routingu

**Rozwiązanie:**
- Przetestuj tabelę decyzyjną
- Sprawdź warunki
- Zweryfikuj mapowanie użytkowników
- Przejrzyj wartości pól

## "Assignment seems to skip someone"
**Przyczyna:** Nieprawidłowa kolejność sekwencyjna

**Rozwiązanie:**
- Sprawdź numery priorytetów
- Zweryfikuj, czy sekwencja jest poprawna
- Przetestuj z próbką
- Przejrzyj uporządkowanie tabeli decyzyjnej

---

# Porównanie kart przypisania

| Karta | Przypisuje do | Typ routingu | Przypadek użycia |
|------|-----------|-----------|----------|
| DOC_USER_ASSIGN | Osoba indywidualna | Bezpośredni | Proste przypisanie |
| DOC_GROUP_ASSIGN | Grupa | Bezpośredni | Przypisanie do zespołu |
| ACTION_ASSIGN_DOC_BASED_ON_DECISION_TABLE | Wynik decyzji | Warunkowy | Złożony routing |
| ACTION_ASSIGN_DOC_DECISION_TABLE_SEQUENTIAL | Wiele (sekwencyjnie) | Warunkowy | Łańcuch zatwierdzania |
| ACTION_ASSIGN_DOC_TO_USER_SEQUENTIAL | Użytkownik (sekwencyjnie) | Uporządkowany | Sekwencyjne kroki użytkownika |
| ACTION_ASSIGN_DOC_TO_GROUP_SEQUENTIAL | Grupy (sekwencyjnie) | Uporządkowany | Sekwencyjne kroki grupy |
| ACTION_ASSIGN_DOC_TO_FACILITY_GROUP | Grupa obiektu | Bezpośredni | Specyficzne dla obiektu |
| ACTION_ASSIGN_DOC_TO_FACILITY_GROUP_SEQUENTIAL | Obiekty (sekwencyjnie) | Uporządkowany | Wieloobiektowy |
| ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP | Zakupy | Bezpośredni | Przepływ pracy zakupów |
| ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP_SEQUENTIAL | Zakupy (sekwencyjnie) | Uporządkowany | Łańcuch zatwierdzania zakupów |
| ACTION_CHANGE_DOC_SUBORG | Sub-organizacja | Bezpośredni | Zmiana działu |
| ACTION_CHANGE_DOC_SUBORG_BY_FIELD_TEXT | Sub-org według pola | Warunkowy | Przypisanie na podstawie pola |
| ACTION_ASSIGN_USER_FROM_FIELD_WITH_FALLBACK | Pole/Rozwiązanie zapasowe | Warunkowy | Dynamiczne przypisanie użytkownika |

---

# Powiązane karty

- **ACTION_CREATE_TASK_FOR_USER** - Przypisz zadanie tej samej osobie
- **ACTION_SEND_EMAIL** - Powiadom przypisaną osobę
- **CONDITION_USER_IS_ISNOT** - Sprawdź, czy przypisano właściwą osobę
- **CONDITION_GROUP_IS_ISNOT** - Sprawdź, czy przypisano właściwą grupę
