# Przewodniki po wzorcach przepływu pracy

**Wersja:** 1.0
**Ostatnia aktualizacja:** 23 października 2025 r.

---

## Przegląd

Niniejszy katalog zawiera kompleksowe przewodniki po wzorcach przepływu pracy, które pokazują, jak łączyć wiele kart przepływu pracy, aby rozwiązać typowe scenariusze biznesowe. Każdy wzorzec zawiera instrukcje wdrażania krok po kroku, kompletne przykłady i najlepsze praktyki.

**Czym są wzorce przepływu pracy?**

Wzorce przepływu pracy to sprawdzone, wielokrotnego użytku rozwiązania typowych wyzwań związanych z przetwarzaniem dokumentacji. Zamiast zaczynać od zera, możesz użyć tych wzorców jako szablonów i dostosować je do swoich konkretnych potrzeb.

---

## Dostępne wzorce

### 1. [Wzorzec integracji API](api-integration-pattern.md)

**Złożoność:** Średnia | **Czas konfiguracji:** 45-60 minut

Dowiedz się, jak zintegrować DocBits z zewnętrznymi interfejsami API, aby pobierać, walidować i przechowywać dane z systemów zewnętrznych.

**Przypadki użycia:**
- Pobieranie cen w czasie rzeczywistym z systemów zewnętrznych
- Walidacja danych dostawcy względem głównych baz danych
- Wyszukiwanie szczegółów produktu w systemach katalogowych
- Pobieranie kursów wymiany walut
- Weryfikacja adresów za pomocą usług geokodowania

**Użyte karty:** CALL_API, CONDITION_HTTPS_REQUEST_STATUS, ACTION_SET_FIELD_TO_TEXT, CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**[Zobacz pełny wzorzec →](api-integration-pattern.md)**

---

### 2. [Wzorzec zarządzania zadaniami](task-management-pattern.md)

**Złożoność:** Niska-Średnia | **Czas konfiguracji:** 30-45 minut

Opanuj sztukę tworzenia, przypisywania, śledzenia i zarządzania zadaniami w ramach przepływów pracy DocBits w procesach zatwierdzania i przeglądu.

**Przypadki użycia:**
- Tworzenie przepływów pracy zatwierdzania
- Przypisywanie zadań przeglądu użytkownikom
- Obsługa wyjątków wymagających interwencji człowieka
- Eskalacja problemów do menedżerów
- Tworzenie wielopoziomowych łańcuchów zatwierdzania
- Śledzenie realizacji zadań i terminów

**Użyte karty:** tasks_create, ACTION_ASSIGN_TO_USER, ACTION_SEND_EMAIL_TO_GROUPS, CONDITION_TASK_STATUS

**[Zobacz pełny wzorzec →](task-management-pattern.md)**

---

### 3. [Wzorzec dopasowania zamówienia zakupu (PO)](po-matching-pattern.md)

**Złożoność:** Średnia-Wysoka | **Czas konfiguracji:** 60-90 minut

Wdrażaj kompleksowe przepływy pracy dopasowywania zamówień zakupu, aby walidować faktury względem zamówień zakupu z routingiem opartym na tolerancji.

**Przypadki użycia:**
- Walidacja faktur względem zamówień zakupu
- Wykrywanie błędów cenowych przed płatnością
- Identyfikacja rozbieżności w ilościach
- Egzekwowanie kontroli zamówień
- Zapobieganie powielaniu płatności
- Automatyzacja trójdrożnego dopasowania

**Użyte karty:** PURCHASE_ORDER_FULL_MATCH, CONDITION_DOC_TO_PO_UNIT_PRICE, CONDITION_DOC_TO_PO_QUANTITY, CONDITION_DOC_TO_PO_TAX_LINES

**[Zobacz pełny wzorzec →](po-matching-pattern.md)**

---

### 4. [Wzorzec logiki decyzyjnej](decision-logic-pattern.md)

**Złożoność:** Średnia | **Czas konfiguracji:** 30-45 minut

Wdrażaj złożone drzewa decyzyjne i warunkową logikę routingu, aby przetwarzać dokumenty różnymi ścieżkami w oparciu o zasady biznesowe.

**Przypadki użycia:**
- Routing dokumentów według progów kwotowych
- Stosowanie różnych zasad dla różnych typów dokumentów
- Wdrażanie wielopoziomowej logiki zatwierdzania
- Obsługa złożonych polityk biznesowych
- Tworzenie dynamicznego routingu opartego na wielu kryteriach
- Wdrażanie macierzy zatwierdzania

**Użyte karty:** CONDITION_DOC_FIELD_AMOUNT, CONDITION_DOC_TYPE_IS_ISNOT, CONDITION_SUPPLIER_STATUS_IS_ISNOT, ACTION_ASSIGN_TO_USER

**[Zobacz pełny wzorzec →](decision-logic-pattern.md)**

---

### 5. [Wzorzec transformacji danych](data-transformation-pattern.md)

**Złożoność:** Średnia | **Czas konfiguracji:** 30-45 minut

Transformuj, obliczaj, formatuj i wzbogacaj dane dokumentów, aby przygotować je do eksportu, wykonywać obliczenia i standaryzować formaty.

**Przypadki użycia:**
- Obliczanie sum, sum częściowych, podatków
- Konwersja walut lub jednostek
- Formatowanie dat, liczb, tekstu
- Wyliczanie wartości z istniejących pól
- Wzbogacanie danych z zewnętrznych źródeł
- Standaryzacja formatów danych
- Walidacja obliczeń

**Użyte karty:** ACTION_CALCULATE_FIELD, ACTION_SET_FIELD_TO_TEXT, ACTION_COPY_FIELD_VALUE, CALL_API, CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**[Zobacz pełny wzorzec →](data-transformation-pattern.md)**

---

## Przewodnik wyboru wzorca

### Według złożoności

| Złożoność | Wzorce | Najlepsze dla |
|------------|----------|----------|
| **Niska-Średnia** | [Zarządzanie zadaniami](task-management-pattern.md) | Początkujący, proste przepływy pracy |
| **Średnia** | [Integracja API](api-integration-pattern.md)<br>[Logika decyzyjna](decision-logic-pattern.md)<br>[Transformacja danych](data-transformation-pattern.md) | Średniozaawansowani, standardowe przepływy pracy |
| **Średnia-Wysoka** | [Dopasowanie PO](po-matching-pattern.md) | Zaawansowani, złożona walidacja |

---

### Według przypadku użycia

| Muszę... | Użyj tego wzorca |
|--------------|------------------|
| Zintegrować się z systemami zewnętrznymi | [Wzorzec integracji API](api-integration-pattern.md) |
| Utworzyć przepływy pracy zatwierdzania | [Wzorzec zarządzania zadaniami](task-management-pattern.md) |
| Zweryfikować względem zamówień zakupu | [Wzorzec dopasowania PO](po-matching-pattern.md) |
| Kierować na podstawie warunków | [Wzorzec logiki decyzyjnej](decision-logic-pattern.md) |
| Obliczać i przekształcać dane | [Wzorzec transformacji danych](data-transformation-pattern.md) |

---

### Według branży/działu

| Branża/Dział | Zalecane wzorce |
|---------------------|---------------------|
| **Finanse/Księgowość** | [Dopasowanie PO](po-matching-pattern.md), [Zarządzanie zadaniami](task-management-pattern.md), [Transformacja danych](data-transformation-pattern.md) |
| **Zakupy** | [Dopasowanie PO](po-matching-pattern.md), [Logika decyzyjna](decision-logic-pattern.md), [Integracja API](api-integration-pattern.md) |
| **Operacje** | [Zarządzanie zadaniami](task-management-pattern.md), [Logika decyzyjna](decision-logic-pattern.md) |
| **IT/Integracja** | [Integracja API](api-integration-pattern.md), [Transformacja danych](data-transformation-pattern.md) |
| **Wszystkie działy** | [Logika decyzyjna](decision-logic-pattern.md), [Zarządzanie zadaniami](task-management-pattern.md) |

---

## Jak korzystać z tych wzorców

### Krok 1: Wybierz wzorzec

1. Przejrzyj opisy wzorców powyżej.
2. Zidentyfikuj, który wzorzec pasuje do Twojego przypadku użycia.
3. Sprawdź złożoność i szacowany czas konfiguracji.
4. Przejrzyj sekcję „Kiedy używać” w przewodniku po wzorcach.

### Krok 2: Przejrzyj wymagania wstępne

Każdy przewodnik po wzorcach wymienia:
- Wymaganą wiedzę
- Powiązane przewodniki do przeczytania w pierwszej kolejności
- Karty, które zostaną użyte
- Wymagania konfiguracyjne

### Krok 3: Postępuj zgodnie z instrukcjami krok po kroku

Każdy wzorzec zapewnia:
- Kompletny przykład przepływu pracy
- Przewodnik wdrażania krok po kroku
- Szablony konfiguracji
- Przykłady z życia wzięte
- Wskazówki dotyczące rozwiązywania problemów

### Krok 4: Dostosuj do swoich potrzeb

- Dostosuj przykład do swoich zasad biznesowych.
- Dostosuj progi i tolerancje.
- Zmodyfikuj logikę routingu.
- Dodaj/usuń kroki według potrzeb.
- Przetestuj dokładnie przed użyciem produkcyjnym.

### Krok 5: Monitoruj i optymalizuj

- Śledź wydajność przepływu pracy.
- Monitoruj wskaźniki sukcesu.
- Zbieraj opinie użytkowników.
- Udoskonalaj konfigurację.
- Dokumentuj dostosowania.

---

## Kombinacje wzorców

Wiele rzeczywistych scenariuszy wymaga połączenia wielu wzorców:

### Przykład 1: Pełne przetwarzanie faktur

```
1. Wzorzec integracji API → Pobierz aktualne ceny
2. Wzorzec transformacji danych → Oblicz sumy
3. Wzorzec dopasowania PO → Waliduj względem zamówienia zakupu
4. Wzorzec logiki decyzyjnej → Kieruj na podstawie odchyleń
5. Wzorzec zarządzania zadaniami → Utwórz zadania zatwierdzania
```

---

## Uzyskiwanie pomocy

### Zasoby wsparcia wzorców

**Dokumentacja:**
- [Pełny indeks przewodnika po przepływie pracy](../README.md)
- [Przewodniki po poszczególnych kartach](../then/action/)
- [Odniesienie do kart warunkowych](../and/condition-cards-complete-guide.md)

**Kontakt:**
- Opinie o wzorcach: docs@docbits.com
- Wsparcie techniczne: support@docbits.com
- Pomoc we wdrożeniu: consulting@docbits.com

---

**Ostatnia aktualizacja:** 23 października 2025 r.
**Utrzymywane przez:** Zespół ds. Dokumentacji
**Wersja:** 1.0
