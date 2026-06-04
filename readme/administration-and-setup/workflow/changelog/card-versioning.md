# System wersjonowania kart - Aktualizacja z października 2025

**Dokument:** Przegląd wersjonowania kart przepływu pracy
**Ostatnia aktualizacja:** 23 października 2025
**Status:** Ukończono

---

## Przegląd

Silnik przepływów pracy DocBits wykorzystuje **wersjonowanie oparte na liczbach całkowitych** do zarządzania ewolucją kart przy zachowaniu zgodności wstecznej. Ten dokument zawiera przegląd systemu wersjonowania.

---

## Czym jest wersjonowanie kart?

### Koncepcja
Każda karta przepływu pracy może mieć wiele wersji, co umożliwia systemowi:
- Dodawanie nowych funkcji bez przerywania istniejących przepływów pracy
- Obsługę wycofanej funkcjonalności podczas jej stopniowego wygaszania
- Ewolucję możliwości kart w czasie
- Zachowanie zgodności wstecznej

### Struktura wersji
- **Format:** Wartości całkowite (1, 2, 3, 4, 5...)
- **Identyfikacja:** Klucz złożony (card_type, card_version)
- **Status:** Każda wersja ma flagi deprecated/enabled

### Przykład
Karta `tasks_create` ewoluowała przez 4 wersje:
- **v1:** Oryginalne tworzenie zadań (wycofane)
- **v2:** Dodano obsługę tłumaczeń (wycofane)
- **v3:** Eksperymentalna obsługa drzewa decyzyjnego (wycofane)
- **v4:** Obsługa generycznego typu pozycji roboczej (obecnie aktywna)

---

## Kluczowe statystyki

### Przegląd wersjonowania
| Metryka | Wartość |
|--------|-------|
| **Karty z wieloma wersjami** | 30+ |
| **Łączna liczba zapisów wersji** | 90+ |
| **Wersje na kartę (średnio)** | 3 |
| **Maksymalna liczba wersji** | 5 (CONDITION_DOC_TO_PO_UNIT_PRICE) |
| **Wycofane wersje** | 9 |
| **Całkowicie wyłączone karty** | 2 |

### Rozkład wersji
- **2 wersje:** 14 kart (prostsza ewolucja)
- **3 wersje:** 11 kart (umiarkowana ewolucja)
- **4 wersje:** 4 karty (znacząca ewolucja)
- **5 wersji:** 1 karta (najbardziej ewoluowana: CONDITION_DOC_TO_PO_UNIT_PRICE)

---

## Typowe wzorce wersji

### Wzorzec 1: Przyjęcie kluczy tłumaczeń (v1 → v2)

**Dotyczy:** ponad 15 kart

**Zmiana:**
```
v1: Plain text: "Call Api: [param] with method: [param]"
v2: With i18n: "trnsl_%call_api trnsl_be_% Call Api: [param]..."
```

**Cel:** Umożliwienie obsługi wielu języków

**Karty:** CALL_API, RUN_WORKFLOW, APPROVE, REJECT, CALC_COLUMNS i inne

**Migracja:** Bezpieczna - brak zmian funkcjonalnych

---

### Wzorzec 2: Integracja drzewa decyzyjnego (v2 → v3)

**Dotyczy:** 5 kart

**Zmiana:** Dodanie parametru drzewa decyzyjnego

```
v2: Create a new Task with title: [param], description: [param]...
v3: (same as v2) + "Use decision tree, if available: [param]"
```

**Cel:** Obsługa wyników tabeli decyzyjnej

**Karty:**
- tasks_create (v3 wycofane)
- ACTION_TASK_FOR_GROUP (v3 wycofane)
- DOC_USER_ASSIGN (v3 wycofane)
- DOC_GROUP_ASSIGN (v3 wycofane)
- ACTION_DECISION_TREE_CREATE_TASKS

**Status:** Wycofane - podejście z drzewem decyzyjnym było eksperymentalne

---

### Wzorzec 3: Ewolucja typów generycznych (v3 → v4)

**Dotyczy:** 4 karty

**Zmiana:** "Task" staje się elastycznym typem pozycji roboczej

```
v3: Create a new Task with the title: [param]
v4: Create a new [param] with the title: [param]
```

**Cel:** Obsługa Tasks, Tickets, Issues i innych typów pozycji roboczych

**Karty:**
- tasks_create (v4 bieżąca)
- ACTION_TASK_FOR_GROUP (v4 bieżąca)
- ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP (v3 bieżąca)
- ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK (v3 bieżąca)

**Bieżący status:** Aktywna i zalecana

---

### Wzorzec 4: Parametry tolerancji (karty PO)

**Dotyczy:** 6 kart porównania PO

**Zmiana:** Dodanie obsługi tolerancji/odchyleń

```
v2: Document value [operator] Purchase Order value
v3+: Document value [operator] PO value with tolerance [amount] [unit]
```

**Cel:** Dopuszczenie akceptowalnego odchylenia w dopasowywaniu (np. różnica ceny 2% jest OK)

**Kluczowe karty:**
- CONDITION_DOC_TO_PO_UNIT_PRICE (ewoluowała do v5 z tolerancją)
- CONDITION_DATES_OPERATOR_OC_LINE_ITEMS (v2 → v3)
- CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY

**Korzyść:** Bardziej realistyczne kryteria dopasowania

---

### Wzorzec 5: Parametry trybu porównania

**Dotyczy:** 3 karty porównania PO

**Zmiana:** Obsługa różnych algorytmów porównania

```
v3: Standard comparison logic
v4: Same logic + "Compare as [param]" parameter
```

**Cel:** Elastyczne metody porównania

**Karty:**
- COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE (v2-4)
- CONDITION_OC_TO_PO_ITEMS (v3-4)
- CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY (v3-4)

---

### Wzorzec 6: Wyzwalacze przepływu pracy

**Dotyczy:** tylko STAUS_CHANGE

**Zmiana:** Automatyczne wyzwalanie przepływów pracy przy zmianie statusu

```
v2: Change Status to [param]
v3: Change Status to [param], trigger Workflows [param]
```

**Cel:** Kaskadowanie zmian statusu między przepływami pracy

---

## Najbardziej ewoluowane karty

### 1. CONDITION_DOC_TO_PO_UNIT_PRICE (5 wersji)

**Ścieżka ewolucji:** v2 → v3 → v4 → v5

- **v2:** Podstawowe porównanie ceny jednostkowej
- **v3:** Ten sam klucz tłumaczenia (v2)
- **v4:** Dodano parametr trybu porównania
- **v5:** Dodano parametr progu tolerancji

**Bieżąca:** v5 (z obsługą tolerancji)

---

### 2. CONDITION_OC_TO_PO_ITEMS (4 wersje)

**Ścieżka ewolucji:** v1 → v2 → v3 → v4

- **v1:** Podstawowe dopasowanie pozycji (wycofane)
- **v2:** Dodano parametr metody porównania
- **v3:** Wzbogacono o klucze tłumaczeń
- **v4:** Dodano parametr trybu porównania

**Bieżąca:** v4

**Unikaj:** v1 (wycofane)

---

### 3. tasks_create (4 wersje)

**Ścieżka ewolucji:** v1 → v2 → v3 → v4

- **v1:** Oryginalna implementacja (wycofane)
- **v2:** Dodano obsługę tłumaczeń (wycofane)
- **v3:** Dodano drzewo decyzyjne (wycofane)
- **v4:** Generyczne typy pozycji roboczych (bieżąca)

**Bieżąca:** v4 (zalecana)

**Oś czasu:**
```
v1 → deprecated (old)
  → v2 → deprecated (translation added)
    → v3 → deprecated (decision tree experiment)
      → v4 → CURRENT & ACTIVE
```

---

## Status wycofania

### Całkowicie wycofane wersje (nie używać)

| Karta | Wersja | Powód | Alternatywa |
|------|---------|--------|-------------|
| tasks_create | v1 | Bardzo stara | Użyj v4 |
| tasks_create | v3 | Drzewo decyzyjne wycofane | Użyj v4 |
| ACTION_TASK_FOR_GROUP | v3 | Drzewo decyzyjne wycofane | Użyj v4 |
| DOC_USER_ASSIGN | v3 | Drzewo decyzyjne wycofane | Użyj v2 |
| DOC_GROUP_ASSIGN | v3 | Drzewo decyzyjne wycofane | Użyj v2 |
| CONDITION_DOC_TYPE_IS_ISNOT | v1 | Bardzo stara | Użyj v2 |
| CONDITION_OC_TO_PO_ITEMS | v1 | Bardzo stara | Użyj v4 |
| ACTION_RUN_DOCOPERATOR_SCRIPT | v4 | Funkcje wycofane | Użyj v3 |

### Całkowicie wyłączone karty (nie można używać)

| Karta | Wersje | Uwagi |
|------|----------|-------|
| DOC_SUBORG_CHANGE | v1, v2 | Nieobsługiwana funkcjonalność |
| RUN_SCRIPT | v2, v3 | Zastąpiona przez ACTION_RUN_DOCOPERATOR_SCRIPT |

---

## Zalecenia dotyczące wersji

### Według przypadku użycia

**Tworzenie nowego przepływu pracy:**
- Zawsze używaj **najwyższego włączonego numeru wersji**
- Zapewnia najnowsze funkcje i ulepszenia
- Obsługiwana i udokumentowana

**Konserwacja istniejącego przepływu pracy:**
- Kontynuuj korzystanie z bieżącej wersji, jeśli działa
- Zaplanuj migrację, gdy będzie to wykonalne
- Brak pilnej potrzeby aktualizacji

**Migracja starszego przepływu pracy:**
- Zidentyfikuj aktualnie używaną wersję
- Zaplanuj ścieżkę aktualizacji
- Przetestuj dokładnie przed wdrożeniem

---

## Jak działają wersje

### Wybór wersji
Podczas tworzenia przepływu pracy wybierasz, której wersji karty użyć. Przykład:
- Użyj `tasks_create v4` do tworzenia nowych zadań (zalecane)
- Użyj `tasks_create v2`, jeśli starsze systemy tego wymagają (starsza, ale działa)
- NIE używaj `tasks_create v1` (wycofane)

### Zgodność wsteczna
- Nowsze wersje nie przerywają starszych przepływów pracy
- Stare przepływy pracy nadal działają ze swoją oryginalną wersją
- Można stopniowo aktualizować przepływy pracy

### Implementacja techniczna
Wersje są zarządzane na poziomie bazy danych:
```
card_templates table (PostgreSQL)
- card_type: Identifies the card (e.g., "tasks_create")
- card_version: Version number (e.g., 2, 3, 4)
- deprecated: Boolean flag
- enabled: Boolean flag
- text: Card description/parameters
```

---

## Na potrzeby dokumentacji

### Zrozumienie informacji o wersji
Gdy widzisz "Card v3" w dokumentacji:
- Odnosi się to do wersji 3 tej konkretnej karty
- Sprawdź [Pełne odniesienie do wersjonowania](../../docs/card_version.md), aby uzyskać szczegóły
- Zweryfikuj, która wersja jest zalecana

### Sprawdzanie swojej wersji
Aby dowiedzieć się, której wersji używasz:
1. Otwórz kartę w swoim przepływie pracy
2. Sprawdź wyświetlany numer wersji
3. Porównaj z zaleceniami w przewodnikach

### Oś czasu ewolucji wersji
- **2024-2025:** Ciągła ewolucja
- **Październik 2025:** Pełna dokumentacja wersjonowania
- **Przyszłość:** Kontynuowane ulepszenia

---

## Powiązana dokumentacja

### Kompleksowe odniesienie
→ [Pełne odniesienie do wersjonowania kart](../../docs/card_version.md)

Zawiera:
- Wszystkie ponad 30 kart z wersjami
- Szczegółową ewolucję tekstu dla każdej
- Konkretne zmiany parametrów
- Zapytania SQL do wyszukiwania wersji

### Przewodniki dla konkretnych kart
→ [Przewodniki po przepływach pracy](../)

Dokumentacja dla każdej karty z zaleceniami dotyczącymi wersji

### Szczegóły historii wersji
Każdy przewodnik zawiera informacje o wersji i uwagi dotyczące migracji

---

## Szybkie odniesienie

### Karty z największą liczbą wersji
1. CONDITION_DOC_TO_PO_UNIT_PRICE - 5 wersji
2. CONDITION_OC_TO_PO_ITEMS - 4 wersje
3. tasks_create - 4 wersje
4. COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE - 3 wersje
5. CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY - 4 wersje

### Najczęstszy wzorzec ewolucji
**Przyjęcie kluczy tłumaczeń (v1 → v2)** - ponad 15 kart

### Najbardziej znacząca zmiana
**Ewolucja typów generycznych (v3 → v4)** - Zmiana z "Task" na elastyczny typ pozycji roboczej

### Całkowicie wyłączone
- DOC_SUBORG_CHANGE
- RUN_SCRIPT

---

## Najczęściej zadawane pytania

### P: Której wersji powinienem używać?
O: Użyj **najwyższej włączonej wersji**, chyba że masz konkretny powód, aby użyć starszej wersji.

### P: Czy mogę zaktualizować mój przepływ pracy do nowszej wersji?
O: Tak, ale przetestuj dokładnie. Niektóre wersje mają różne wymagania dotyczące parametrów.

### P: Co się stanie, jeśli użyję wycofanej wersji?
O: Nadal działa, ale nie otrzymasz nowych funkcji. Zalecana migracja.

### P: Czy mogę użyć wyłączonej karty?
O: Nie, wyłączonych kart nie można używać. Zamiast tego użyj zalecanej alternatywy.

### P: Skąd mam wiedzieć, czy moja karta wymaga aktualizacji?
O: Sprawdź [Pełne odniesienie do wersjonowania](../../docs/card_version.md) dla swojego typu karty i postępuj zgodnie z zaleceniami.

---

## Najlepsze praktyki

1. **Nowe przepływy pracy:** Użyj najnowszej stabilnej wersji
2. **Aktualizacje:** Okresowo sprawdzaj nowe wersje
3. **Testowanie:** Najpierw przetestuj aktualizacje wersji w środowisku testowym
4. **Dokumentacja:** Zapoznaj się z przewodnikami dla konkretnych kart, aby uzyskać szczegóły wersji
5. **Migracja:** Planuj aktualizacje przyrostowo
6. **Wsparcie:** Skontaktuj się ze wsparciem, jeśli pojawią się pytania dotyczące zgodności wersji

---

## Tabela podsumowująca

| Typ karty | Bieżąca wersja | Łączna liczba wersji | Status | Uwagi |
|-----------|-----------------|----------------|--------|-------|
| tasks_create | 4 | 4 | Aktywna | Najbardziej ewoluowana; v3 wycofana |
| CONDITION_DOC_TO_PO_UNIT_PRICE | 5 | 4 | Aktywna | Najwyższa liczba wersji |
| CONDITION_OC_TO_PO_ITEMS | 4 | 4 | Aktywna | v1 wycofana |
| ACTION_TASK_FOR_GROUP | 4 | 3 | Aktywna | v3 wycofana |
| ACTION_RUN_DOCOPERATOR_SCRIPT | 3 | 3 | Aktywna | v4 wycofana/wyłączona |
| Większość kart | 2 | 2 | Aktywna | Wzorzec v1 → v2 |

---

## Zobacz także

- 📖 [Pełne odniesienie do wersjonowania kart](../../docs/card_version.md)
- 🔗 [Przewodniki po przepływach pracy](../)
- 📋 [Informacje o wydaniu z października 2025](./2025-10-october.md)
- 🔄 [Analiza łączenia przepływów pracy](../../WORKFLOW_LINKING_MAP.md)

---

**Ostatnia aktualizacja:** 23 października 2025
**Źródło:** baza danych postgres-dev-docflow
**Status:** Kompletne odniesienie
