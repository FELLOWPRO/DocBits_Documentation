---
hidden: true
---

# Historia wydań i wersji kart przepływu pracy

## Zasady kontroli wersji

<figure><img src="../../.gitbook/assets/docbits_workflow_version_control.png" alt="Docbits Workflow Version Control"><figcaption>System kontroli wersji przepływu pracy</figcaption></figure>

### Wersja 8.5.2024 - Podstawowe funkcje wersjonowania

Silnik przepływów pracy DocBits wdraża solidną kontrolę wersji dla wszystkich kart przepływu pracy:

1. **Kontrola wersji**: Każda karta może mieć wiele wersji, z których każda reprezentuje inny zestaw warunków lub akcji. Pozwala to eksperymentować z regułami lub je modyfikować bez wpływu na aktualnie aktywny przepływ pracy.
2. **Płynne aktualizacje**: Gdy musisz zaktualizować regułę lub warunek z powodu zmian w wymaganiach dotyczących przetwarzania dokumentów, możesz utworzyć nową wersję karty. To podejście zapewnia, że wszelkie modyfikacje są celowe i przetestowane, zanim zastąpią bieżącą wersję. Minimalizuje błędy i potencjalne zakłócenia w przetwarzaniu dokumentów.
3. **Utrzymanie spójności**: Pozostawienie oryginalnej wersji karty bez zmian, dopóki nie zdecydujesz się na aktualizację, zapewnia, że trwające procesy nie są naruszone. Możesz uruchamiać testy i walidacje nowej wersji bez wpływu na dane lub przepływy pracy na żywo.
4. **Elastyczność i testowanie**: Wiele wersji umożliwia testowanie różnych scenariuszy w kontrolowanym środowisku. Możesz zobaczyć skutki nowych reguł lub zmian w przepływie pracy przetwarzania dokumentów bez wprowadzania trwałych zmian. Gdy jesteś zadowolony z wyników, możesz wybrać zastosowanie nowej wersji.

---

## Przegląd wersjonowania kart

### Statystyki

| Metryka | Wartość |
|--------|-------|
| **Karty z wieloma wersjami** | 30+ |
| **Łączna liczba zapisów wersji** | 90+ |
| **Bieżące aktywne wersje** | 81+ |
| **Wycofane wersje** | 9 |
| **Całkowicie wyłączone karty** | 2 |
| **Najnowsza wersja (maks.)** | 5 (CONDITION_DOC_TO_PO_UNIT_PRICE) |

### Zakres wersji
- **Minimum:** v1
- **Maksimum:** v5
- **Średnia liczba wersji na kartę:** 3

---

## Szczegółowe zmiany wersji kart

### 🔧 ACTION CARDS - Integracja zewnętrzna i wykonywanie

#### 1. CALL_API
**Wersje:** v1, v2 (Bieżąca: v2)

📖 **Przewodnik:** [Przewodnik Call External API](../then/action/call-api-guide.md)

| Wersja | Tłumaczenie | Status | Kluczowe zmiany |
|---------|-------------|--------|-------------|
| v1 | Nie | Aktywna | Podstawowe wywołanie API bez kluczy tłumaczeń |
| v2 | Tak | ✅ Bieżąca | Dodano `trnsl_%call_api` dla obsługi wielu języków |

**Co się zmieniło:** Dodano obsługę internacjonalizacji (i18n) z kluczami tłumaczeń. Funkcjonalność pozostaje identyczna.

**Przed (v1):**
```
Call Api: [endpoint] with method: [method], params: [params], data: [data]
```

**Po (v2):**
```
trnsl_%call_api trnsl_be_% Call Api: [endpoint] with method: [method], params: [params], data: [data]
```

**Zalecenie:** Użyj v2 dla wszystkich nowych przepływów pracy (zawiera obsługę języków)
**Zgodność wsteczna:** ✅ v1 nadal działa

---

#### 2. HTTPS Request (HTTPS_REQUEST)
**Wersje:** v1, v2 (Bieżąca: v2)

| Wersja | Tłumaczenie | Status | Kluczowe zmiany |
|---------|-------------|--------|-------------|
| v1 | Nie | Aktywna | Proste żądanie HTTP |
| v2 | Tak | ✅ Bieżąca | Dodano klucze tłumaczeń `trnsl_%send_https_request` |

**Co się zmieniło:** Dodano obsługę tłumaczeń. Podstawowa funkcjonalność webhooków/żądań niezmieniona.
**Zalecenie:** Użyj v2 (obsługa wielu języków)

---

#### 3. ACTION_RUN_DOCOPERATOR_SCRIPT ⚠️
**Wersje:** v2 (Bieżąca), v3, v4 (Wycofane i wyłączone)

| Wersja | Tłumaczenie | Status | Kluczowe zmiany |
|---------|-------------|--------|-------------|
| v2 | Tak | Aktywna | Oryginalna implementacja DocOperator |
| v3 | Tak | Aktywna | Dodano parametr "Execute the prompt" dla dodatkowej kontroli |
| v4 | Tak | ❌ WYCOFANA I WYŁĄCZONA | Usunięto parametr "Execute" (cofnięto) |

**Ścieżka ewolucji:** v2 → v3 (dodano parametr) → v4 (cofnięto - niezalecane)

**Co się zmieniło:**
- v2 → v3: Dodano opcjonalny parametr kontroli wykonania dla większej elastyczności
- v3 → v4: Usunięto parametr po dalszej analizie (wycofane)

**Zalecenie:** Użyj v3 dla nowych przepływów pracy (najnowsza aktywna wersja ze wszystkimi funkcjami)
**Migracja:** Jeśli używasz v4, przełącz się na v3 ⚠️

---

#### 4. ACTION_TASK_FOR_GROUP
**Wersje:** v2, v3 (Wycofana), v4 (Bieżąca)

📖 **Przewodnik:** [Przewodnik Task Assignment](../then/task/task-assignment-guide.md)

| Wersja | Zmiany | Status | Parametr typu |
|---------|---------|--------|-----------------|
| v2 | Oryginalna implementacja | Aktywna | "Task" (stały) |
| v3 | + Obsługa drzewa decyzyjnego | ❌ WYCOFANA | "Task" (stały) |
| v4 | - Drzewo decyzyjne, + Typ generyczny | ✅ Bieżąca | Typ generyczny (elastyczny) |

**Ewolucja:** v2 → v3 (eksperyment z drzewem decyzyjnym) → v4 (typy generyczne, drzewo decyzyjne usunięte)

**Zmiana v2 → v3 (eksperyment z drzewem decyzyjnym):**
```
Before: "Create a new Task with the title: [param] ... and assign to group [param]"
After:  "Create a new Task with the title: [param] ... and assign to group [param].
         Use decision tree, if available: [param]"
```

**Zmiana v3 → v4 (typy generyczne + usunięcie drzewa decyzyjnego):**
```
Before (v3): "Create a new Task with the title: [param] ... "
After (v4):  "Create a new [param] with the title: [param] ... "
```

**Co się zmieniło:**
- v2 → v3: Dodano parametr `decision tree, if available: [param]`
- v3 → v4:
  - ❌ Usunięto parametr drzewa decyzyjnego
  - ✅ Zmieniono "Task" → generyczny `[param]` (obsługuje Task, Ticket, Issue itp.)
  - Dodano klucz tłumaczenia `trnsl_%task_for_group_v4`

**Dlaczego:** Podejście z drzewem decyzyjnym v3 było eksperymentalne. v4 zapewnia lepszą elastyczność dzięki generycznym typom pozycji roboczych.
**Zalecenie:** Użyj v4 (bieżąca, najbardziej elastyczna)

---

#### 5. ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP
**Wersje:** v2, v3 (Bieżąca)

| Wersja | Typ zadania | Status | Kluczowa różnica |
|---------|-----------|--------|-----------------|
| v2 | "task" (stały) | Aktywna | Oryginalna wersja |
| v3 | Typ generyczny | ✅ Bieżąca | Zmieniono na elastyczny `[param]` |

**Co się zmieniło:** v2 → v3: "Create a new task" → "Create a new [param]" (obsługuje dowolny typ pozycji roboczej)
**Zalecenie:** Użyj v3

---

#### 6. RUN_WORKFLOW
**Wersje:** v1, v2 (Bieżąca)

**Co się zmieniło:** v1 → v2: Dodano klucze tłumaczeń `trnsl_%run_workflow`
**Zalecenie:** Użyj v2

---

### 📊 KARTY PORÓWNANIA I WALIDACJI PO

#### 1. CONDITION_DOC_TO_PO_UNIT_PRICE ⭐ (Najbardziej ewoluowana - 5 wersji)
**Wersje:** v2, v3, v4, v5 (Bieżąca)

📖 **Przewodnik:** [Pełny przewodnik PO Matching](../and/compare-with-purchase-order/po-matching-complete-guide.md#2-unit-price-comparison-document-vs-po)

| Wersja | Zmiany | Status | Tolerancja | Porównanie |
|---------|---------|--------|-----------|------------|
| v2 | Podstawowe porównanie cen | Aktywna | ❌ Nie | Podstawowe |
| v3 | Tak samo jak v2 | Aktywna | ❌ Nie | Podstawowe |
| v4 | + Parametr trybu porównania | Aktywna | ❌ Nie | ✅ Tak |
| v5 | + Parametry tolerancji | ✅ Bieżąca | ✅ Tak (kwota + jednostka) | ✅ Tak |

**Ścieżka ewolucji:** v2 → v3 (bez zmian) → v4 (tryby porównania) → v5 (progi tolerancji)

**v2 → v3:** Brak zmiany funkcjonalnej (ten sam klucz tłumaczenia)

**Zmiana v3 → v4 (dodano tryb porównania):**
```
Before: "[document] unit price is [operator] to purchase order"
After:  "[document] unit price is [operator] to purchase order. Compare as [mode]"
```

**Zmiana v4 → v5 (dodano parametry tolerancji):**
```
Before: "[document] unit price is [operator] to purchase order. Compare as [mode]"
After:  "[document] unit price is [operator] to purchase order, with tolerance of [amount] [unit].
         Compare as [mode]"
```

**Co się zmieniło:**
- **v2 → v3:** Brak zmiany funkcjonalnej
- **v3 → v4:** Dodano `Compare as [param]` - obsługa różnych operatorów porównania
- **v4 → v5:** Dodano parametry tolerancji:
  - `with tolerance of [amount] [unit]`
  - Przykład: "with tolerance of 2 %" lub "with tolerance of 100 EUR"
  - Obsługuje: %, EUR, $ i inne waluty

**Przypadki użycia:**
- v2/v3: Ścisłe dopasowanie (tylko dokładne ceny)
- v4: Różne metody porównania
- v5: Elastyczna akceptacja odchyleń (np. akceptacja różnic cen 2%) ✅ ZALECANE

**Zalecenie:** Użyj v5 dla nowoczesnych przepływów pracy dopasowania PO

---

#### 2. CONDITION_OC_TO_PO_ITEMS
**Wersje:** v1 (Wycofana), v2, v3, v4 (Bieżąca)

| Wersja | Zmiany | Status | Funkcja porównania |
|---------|---------|--------|-----------------|
| v1 | Brak tłumaczenia, brak metody | ❌ WYCOFANA | Podstawowa |
| v2 | + Klucze tłumaczeń, + metoda | Aktywna | Podstawowa metoda |
| v3 | Tak samo jak v2 | Aktywna | Podstawowa metoda |
| v4 | + Parametry trybu porównania | ✅ Bieżąca | ✅ Elastyczna |

**Co się zmieniło:**
- **v1 → v2:** Dodano `trnsl_%in_order_confirmations_matches_purchase_order` + parametr metody porównania
- **v2 → v3:** Brak zmiany
- **v3 → v4:** Dodano `Compare as [param1] [param2]` dla elastycznych trybów porównania

**Zalecenie:** Użyj v4 (unikaj v1, która jest wycofana)

---

#### 3. CONDITION_DATES_OPERATOR_OC_LINE_ITEMS
**Wersje:** v2, v3 (Bieżąca)

| Wersja | Dni tolerancji | Akceptowane dni tolerancji | Status |
|---------|-----------------|------------------------|--------|
| v2 | ❌ Nie | ❌ Nie | Aktywna |
| v3 | ✅ Tak | ✅ Tak | ✅ Bieżąca |

**Co się zmieniło:** v2 → v3: Dodano parametry tolerancji:
- `with [param] days as tolerance`
- `and [param] as accepted tolerance days`

**Przykład:** Akceptuj daty dostawy w ciągu 5 dni od obiecanej daty
**Zalecenie:** Użyj v3

---

#### 4. CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY
**Wersje:** v2, v3, v4 (Bieżąca)

| Wersja | Tryb porównania | Status |
|---------|-----------------|--------|
| v2 | Podstawowy | Aktywna |
| v3 | Podstawowy (bez zmian) | Aktywna |
| v4 | ✅ Elastyczny wybór trybu | ✅ Bieżąca |

**Co się zmieniło:** v3 → v4: Dodano `compare [param]` dla różnych podejść do porównania
**Zalecenie:** Użyj v4

---

#### 5. COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE
**Wersje:** v2, v3, v4 (Bieżąca)

| Wersja | Tryb porównania | Status |
|---------|-----------------|--------|
| v2 | Standardowy | Aktywna |
| v3 | Standardowy (bez zmian) | Aktywna |
| v4 | ✅ Elastyczny | ✅ Bieżąca |

**Co się zmieniło:** v3 → v4: Dodano parametr `compare [param]`
**Zalecenie:** Użyj v4

---

#### 6. CONDITION_CONFIRMED_DELIVERY_ACCEPTED_DATE_IN_CALENDAR_MASTER_DATA
**Wersje:** v2, v3 (Bieżąca)

| Wersja | Typ dostawy | Tabela danych podstawowych | Status |
|---------|---------------|-------------------|--------|
| v2 | "Confirmed" (stały) | Stałe odniesienie | Aktywna |
| v3 | [Konfigurowalny param] | Dynamiczny [param] | ✅ Bieżąca |

**Co się zmieniło:** v2 → v3:
- Zmieniono "Confirmed delivery" → `[param] delivery` (elastyczny typ dostawy)
- Zmieniono stałe odniesienie do tabeli → `stored in [param]` (dynamiczny wybór tabeli)

**Elastyczność:** v3 umożliwia różne typy dat dostawy i tabele dostawców
**Zalecenie:** Użyj v3

---

#### 7. CONDIITON_UNIT_OF_MEASURE_EQUAL
**Wersje:** v2, v3 (Bieżąca)

| Wersja | Odniesienie do tabeli dostawcy | Status |
|---------|--------------------------|--------|
| v2 | "supplier item price table" (stały) | Aktywna |
| v3 | [Dynamiczny param] | ✅ Bieżąca |

**Co się zmieniło:** v2 → v3: Stałe odniesienie do tabeli → `stored in [param]` (umożliwia dynamiczny wybór tabeli)
**Zalecenie:** Użyj v3

---

### 👥 KARTY PRZYPISANIA I ROUTINGU

#### 1. DOC_USER_ASSIGN
**Wersje:** v1, v2, v3 (Wycofana)

| Wersja | Tłumaczenie | Drzewo decyzyjne | Status |
|---------|-------------|---------------|--------|
| v1 | Nie | ❌ Nie | Aktywna |
| v2 | Tak | ❌ Nie | ✅ Bieżąca |
| v3 | Tak | ✅ Tak | ❌ WYCOFANA |

**Ewolucja:** v1 (bez i18n) → v2 (z i18n) → v3 (+ eksperyment z drzewem decyzyjnym, teraz wycofana)

**Co się zmieniło:**
- v1 → v2: Dodano klucze tłumaczeń
- v2 → v3: Dodano obsługę drzewa decyzyjnego (eksperymentalna, wycofana)

**Zalecenie:** Użyj v2 (stabilna z obsługą i18n)

---

#### 2. DOC_GROUP_ASSIGN
**Wersje:** v2, v3 (Wycofana)

| Wersja | Drzewo decyzyjne | Status |
|---------|---------------|--------|
| v2 | ❌ Nie | ✅ Bieżąca |
| v3 | ✅ Tak | ❌ WYCOFANA |

**Co się zmieniło:** v2 → v3: Dodano `Use decision tree, if available [param]` (później wycofane)
**Zalecenie:** Użyj v2

---

#### 3. OC_ASSIGN_DOC
**Wersje:** v1, v2 (Bieżąca)

**Co się zmieniło:** v1 → v2: Dodano klucze tłumaczeń `trnsl_%oc_assign_doc`
**Zalecenie:** Użyj v2

---

### 📋 KARTY ZARZĄDZANIA ZADANIAMI

#### 1. tasks_create ⭐ (Najbardziej ewoluowana karta zadań - 4 wersje)
**Wersje:** v1 (Wycofana), v2 (Wycofana), v3 (Wycofana), v4 (Bieżąca)

📖 **Przewodnik:** [Przewodnik Task Assignment](../then/task/task-assignment-guide.md#card-tasks_create--create-task-and-assign-to-user)

| Wersja | Tłumaczenie | Drzewo decyzyjne | Typ pozycji roboczej | Status |
|---------|-------------|---------------|-----------------|--------|
| v1 | Nie | Nie | "Task" (stały) | ❌ WYCOFANA |
| v2 | Tak | Nie | "Task" (stały) | ❌ WYCOFANA |
| v3 | Tak | Tak | "Task" (stały) | ❌ WYCOFANA |
| v4 | Tak | Nie | [Generyczny param] | ✅ Bieżąca |

**Oś czasu ewolucji:**
```
v1 (original)
  ↓ (add translation)
v2 (with i18n)
  ↓ (experiment with decision tree)
v3 (+ decision tree, BUT deprecated after this)
  ↓ (remove decision tree, add generic types)
v4 (CURRENT - flexible work items)
```

**Zmiana v1 → v2 (dodano klucze tłumaczeń):**
```
Before: "Create a new Task with the title: [param] ... and assign to user [param]"
After:  "trnsl_%tasks_create trnsl_be_% Create a new Task with the title: [param] ... and assign to user [param]"
```

**Zmiana v2 → v3 (eksperyment z drzewem decyzyjnym):**
```
Before: "Create a new Task with the title: [param] ... and assign to user [param]"
After:  "Create a new Task with the title: [param] ... and assign it to the user [param].
         Use decision tree, if available: [param]"
```

**Zmiana v3 → v4 (typy generyczne + usunięcie drzewa decyzyjnego):**
```
Before: "Create a new Task with the title: [param] ... "
After:  "Create a new [param] with the title: [param] ... "
```

**Co się zmieniło:**
- **v1 → v2:** Dodano klucze tłumaczeń `trnsl_%tasks_create`
- **v2 → v3:**
  - Dodano obsługę drzewa decyzyjnego: `Use decision tree, if available: [param]`
  - Zmieniono "assign to user" → "assign it to the user"
- **v3 → v4:**
  - ❌ Usunięto parametr drzewa decyzyjnego
  - ✅ Zmieniono "Task" → generyczny `[param]` (obsługuje Task, Ticket, Issue itp.)
  - Zaktualizowano klucz tłumaczenia do `trnsl_%tasks_create_v4`

**Uwaga o drzewie decyzyjnym:** v3 wykorzystywała drzewa decyzyjne do dynamicznego przypisywania zadań. To podejście było eksperymentalne i zostało wycofane w v4 na rzecz bezpośredniego, opartego na parametrach wyboru typu pozycji roboczej.

**Zalecenie:** Używaj wyłącznie v4 dla nowych przepływów pracy
**Migracja:** Jeśli używasz v1, v2 lub v3, zaktualizuj do v4 ✅

---

#### 2. OC_TASK
**Wersje:** v1, v2 (Bieżąca)

**Co się zmieniło:** v1 → v2: Dodano klucze tłumaczeń `trnsl_%oc_task`
**Zalecenie:** Użyj v2

---

#### 3. ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK
**Wersje:** v1, v3 (Bieżąca - v2 pominięta)

| Wersja | Typ pozycji roboczej | Status |
|---------|-----------------|--------|
| v1 | "Task" (stały) | Aktywna |
| v3 | [Generyczny param] | ✅ Bieżąca |

**Co się zmieniło:** v1 → v3: Ewolucja typu generycznego (v2 została pominięta w produkcji)
**Zalecenie:** Użyj v3

---

#### 4. ACTION_DECISION_TREE_CREATE_TASKS
**Wersje:** v2, v3 (Bieżąca)

| Wersja | Tekst przypisania | Status |
|---------|-----------------|--------|
| v2 | "Assign task with title" | Aktywna |
| v3 | "Assign [generic] with title" | ✅ Bieżąca |

**Co się zmieniło:** v2 → v3:
- Zmieniono "Assign task" → "Assign [generic param]"
- Zmieniono "return of decision" → "return of decision table" (jaśniejsza terminologia)

**Zalecenie:** Użyj v3

---

### 🔄 KARTY KONTROLI DOKUMENTU

#### APPROVE
**Wersje:** v1, v2 (Bieżąca)
**Zmiana:** Dodano klucze tłumaczeń `trnsl_%approve_doc`
**Zalecenie:** Użyj v2

---

#### REJECT
**Wersje:** v1, v2 (Bieżąca)
**Zmiana:** Dodano klucze tłumaczeń `trnsl_%reject_doc`
**Zalecenie:** Użyj v2

---

#### STAUS_CHANGE (Status Change)
**Wersje:** v1, v2, v3 (Bieżąca)

| Wersja | Wyzwalacz przepływu pracy | Status |
|---------|-----------------|--------|
| v1 | ❌ Nie | Aktywna |
| v2 | ❌ Nie | Aktywna |
| v3 | ✅ Tak | ✅ Bieżąca |

**Co się zmieniło:** v2 → v3: Dodano `trigger Workflows [param]` - automatyczne wyzwalanie przepływów pracy przy zmianie statusu
**Zalecenie:** Użyj v3

---

#### EXPORT
**Wersje:** v1, v2, v3 (Bieżąca)

| Wersja | Walidacja | Status |
|---------|------------|--------|
| v1 | ❌ Nie | Aktywna |
| v2 | ❌ Nie | Aktywna |
| v3 | ✅ Tak | ✅ Bieżąca |

**Co się zmieniło:** v2 → v3: Dodano `Start Export with Validation: [param]`
**Zalecenie:** Użyj v3

---

### 🧮 KARTY MANIPULACJI DANYMI

#### CALC_COLUMNS, CALC_COLUMNS_REGEX, EDIT_COLUMN, AI_CALC_MTZ_ETZ
**Wzorzec:** v1 → v2 (dodano klucze tłumaczeń)
**Zalecenie:** Użyj v2 dla wszystkich

---

#### CONDITION_DECISION_TREE_DATA
**Wersje:** v2, v3 (Bieżąca)

| Wersja | Wykorzystanie danych | Status |
|---------|------------|--------|
| v2 | "Use return data in later cards" | Aktywna |
| v3 | "[Explicit param] returned data for use in subsequent cards" | ✅ Bieżąca |

**Co się zmieniło:** v2 → v3: Bardziej jednoznaczna kontrola nad ekstrakcją danych drzewa decyzyjnego
**Zalecenie:** Użyj v3

---

### ❌ KARTY WYŁĄCZONE (nie używać)

#### DOC_SUBORG_CHANGE
**Wersje:** v1, v2 (obie wyłączone)
**Status:** Już nieobsługiwana
**Alternatywa:** Użyj funkcji przypisania dokumentów

---

#### RUN_SCRIPT
**Wersje:** v2, v3 (obie wyłączone)
**Status:** Zastąpiona przez ACTION_RUN_DOCOPERATOR_SCRIPT
**Alternatywa:** Użyj ACTION_RUN_DOCOPERATOR_SCRIPT v3

---

## 🎯 Typowe wzorce wersji

### Wzorzec 1: Przyjęcie kluczy tłumaczeń (v1 → v2)
**Dotyczy:** ponad 15 kart

**Zmiana:** Dodano klucze tłumaczeń `trnsl_%[card_name]`
```
v1: Plain text (no i18n)
v2: trnsl_%[key] trnsl_be_% Plain text (with i18n)
```

**Karty:** CALL_API, RUN_WORKFLOW, APPROVE, REJECT, CALC_COLUMNS i inne
**Wpływ:** Umożliwia obsługę wielu języków

---

### Wzorzec 2: Integracja drzewa decyzyjnego (v2 → v3) - WYCOFANE
**Dotyczy:** 5 kart (ACTION_TASK_FOR_GROUP, tasks_create, DOC_USER_ASSIGN, DOC_GROUP_ASSIGN, ACTION_DECISION_TREE_CREATE_TASKS)

**Zmiana:** Dodano opcjonalny parametr drzewa decyzyjnego
```
v2: Standard task/assignment logic
v3: + "Use decision tree, if available: [param]"
```

**Status:** ❌ W większości wycofane (z wyjątkiem ACTION_DECISION_TREE_CREATE_TASKS)
**Powód:** Preferowane jest prostsze podejście oparte na bezpośrednich parametrach

---

### Wzorzec 3: Ewolucja typów generycznych (v3 → v4)
**Dotyczy:** 4 karty (tasks_create, ACTION_TASK_FOR_GROUP, ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP, ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK)

**Zmiana:** "Task" → generyczny parametr typu
```
v3: Create a new Task with title: [param]
v4: Create a new [param] with title: [param]
```

**Wpływ:** Obsługuje Task, Ticket, Issue i inne typy pozycji roboczych
**Korzyść:** Większa elastyczność i możliwość ponownego użycia

---

### Wzorzec 4: Parametry tolerancji (karty PO)
**Dotyczy:** 6 kart (CONDITION_DOC_TO_PO_UNIT_PRICE, CONDITION_DATES_OPERATOR_OC_LINE_ITEMS, CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY itp.)

**Zmiana:** Dodano obsługę tolerancji/odchyleń
```
v2: Value [operator] Reference Value
v3+: Value [operator] Reference with tolerance [amount] [unit]
```

**Przykłady:**
- "with tolerance of 2 %"
- "with tolerance of 100 EUR"
- "with 5 days as tolerance"

**Wpływ:** Realistyczne kryteria dopasowania (nie wszystkie wartości muszą się dokładnie zgadzać)

---

### Wzorzec 5: Parametry trybu porównania
**Dotyczy:** 3 karty (COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE, CONDITION_OC_TO_PO_ITEMS, CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY)

**Zmiana:** Dodano elastyczny wybór metody porównania
```
v3: Standard comparison
v4: + "Compare as [param1] [param2]"
```

**Wpływ:** Obsługa różnych algorytmów porównania

---

## ✅ Zalecenia dotyczące wersji

### Dla nowych przepływów pracy
**Reguła:** Zawsze używaj najwyższego włączonego numeru wersji
- Zapewnia najnowsze funkcje
- Najlepsze wsparcie
- Najlepiej przetestowana
- Zalecane podejście

### Dla istniejących przepływów pracy
**Bezpieczne podejście:**
- Kontynuuj korzystanie z bieżącej wersji, jeśli działa
- Zaplanuj stopniową migrację do nowszych wersji
- Najpierw przetestuj aktualizacje w środowisku testowym

### Priorytet migracji

| Priorytet | Karty | Działanie |
|----------|-------|--------|
| **Wysoki** | tasks_create v1/v2/v3, ACTION_TASK_FOR_GROUP v3, CONDITION_DOC_TO_PO_UNIT_PRICE v2/v3/v4 | Zaktualizuj do bieżącej wersji |
| **Średni** | Inne aktualizacje tłumaczeń v1/v2, karty PO v2/v3 | Rozważ aktualizację |
| **Niski** | Karty bez zmian funkcjonalnych | Opcjonalnie |

---

## ⚠️ Wycofane wersje - nie używać

| Karta | Wersja | Powód | Użyj zamiast tego |
|------|---------|--------|-------------|
| tasks_create | v1, v2, v3 | Bardzo stara lub drzewo decyzyjne wycofane | v4 |
| ACTION_TASK_FOR_GROUP | v3 | Podejście z drzewem decyzyjnym wycofane | v4 |
| DOC_USER_ASSIGN | v3 | Podejście z drzewem decyzyjnym wycofane | v2 |
| DOC_GROUP_ASSIGN | v3 | Podejście z drzewem decyzyjnym wycofane | v2 |
| CONDITION_DOC_TYPE_IS_ISNOT | v1 | Bardzo stara | v2 |
| CONDITION_OC_TO_PO_ITEMS | v1 | Bardzo stara | v4 |
| ACTION_RUN_DOCOPERATOR_SCRIPT | v4 | Funkcje cofnięte | v3 |

---

## 🔄 Całkowicie wyłączone karty - nie można używać

| Karta | Wersje | Powód | Alternatywa |
|------|----------|--------|-------------|
| DOC_SUBORG_CHANGE | v1, v2 | Już nieobsługiwana | Karty przypisania dokumentów |
| RUN_SCRIPT | v2, v3 | Zastąpiona przez DocOperator | ACTION_RUN_DOCOPERATOR_SCRIPT v3 |

---

## Powiązana dokumentacja

- 📖 [Odniesienie do wersjonowania kart](../changelog/card-versioning.md) - Szczegółowe informacje o wersjach
- 📚 [Przewodniki po przepływach pracy](../) - Korzystanie z kart krok po kroku
- 🔄 [Baza danych wersji kart](../docs/card_version.md) - Pełna historia wersji
- 📋 [Dzienniki przepływu](../workflow-logs/) - Wykonanie i debugowanie

---

**Ostatnia aktualizacja:** 23 października 2025
**Status:** Pełna historia wersji
**Źródło bazy danych:** postgres-dev-docflow
