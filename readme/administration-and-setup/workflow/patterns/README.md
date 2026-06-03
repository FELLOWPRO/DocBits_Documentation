# Przewodniki po wzorcach workflow

**Wersja:** 1.0
**Ostatnia aktualizacja:** 23 października 2025

---

## Przegląd

Ten katalog zawiera obszerne przewodniki po wzorcach workflow, które pokazują, jak łączyć wiele kart workflow, aby rozwiązywać typowe scenariusze biznesowe. Każdy wzorzec zawiera instrukcje wdrożenia krok po kroku, kompletne przykłady oraz najlepsze praktyki.

**Czym są wzorce workflow?**

Wzorce workflow to sprawdzone, wielokrotnego użytku rozwiązania typowych wyzwań w przetwarzaniu dokumentów. Zamiast zaczynać od zera, możesz wykorzystać te wzorce jako szablony i dostosować je do swoich potrzeb.

---

## Workflow Builder w skrócie

Każdy wzorzec na tej stronie składa się w **Workflow Builder**. Dotrzesz do niego przez **Workflow Dashboard → Workflow List → Add Workflow** (lub otwierając istniejący workflow). Dashboard pokazuje historię uruchomień oraz wskaźniki sukcesu/niepowodzeń dla wszystkich Twoich workflow:

<figure><img src="../../../.gitbook/assets/workflow_dashboard.png" alt="Workflow Dashboard z sumami uruchomień, wskaźnikami sukcesu i niepowodzeń, wykresem uruchomień oraz ostatnią aktywnością"><figcaption><p>Workflow Dashboard — sumy uruchomień, wskaźniki sukcesu/niepowodzeń oraz ostatnia aktywność dla każdego workflow.</p></figcaption></figure>

Zakładka **Workflow List** wymienia każdy workflow wraz z jego typem, kolejnością wykonania i wyzwalaczem. Użyj **Add Workflow**, aby utworzyć nowy, lub kliknij workflow, aby otworzyć go w builderze:

<figure><img src="../../../.gitbook/assets/workflow_list.png" alt="Zakładka Workflow List z workflow według typu, kolejności wykonania i wyzwalacza"><figcaption><p>Workflow List — każdy wiersz to workflow, który możesz otworzyć, włączyć/wyłączyć lub edytować.</p></figcaption></figure>

Workflow składa się z trzech grup kart — **When** (wyzwalacz), **And** (dodatkowe warunki) oraz **Then** (akcje do wykonania). Poniższy przykład jest wyzwalany dla faktur należących do podorganizacji i przypisuje je użytkownikowi:

<figure><img src="../../../.gitbook/assets/workflow_designer_cards.png" alt="Canvas Workflow Builder z kartami When, And i Then"><figcaption><p>Canvas Workflow Builder. Każdy z poniższych wzorców to po prostu inna kombinacja kart When / And / Then.</p></figcaption></figure>

Kliknij **Add Card** w dowolnej grupie, aby otworzyć bibliotekę kart. Karty są uporządkowane według kategorii (Compare with Purchase Order, Partner Cards, Document Field, Date &#x26; Time, Document, Logic, Status, Table, Assignee, …), dzięki czemu znajdziesz element, którego wymaga dany wzorzec:

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Okno dialogowe Add Card pokazujące kategorie kart oraz dostępne karty"><figcaption><p>Biblioteka <strong>Add Card</strong> — każda karta wymieniona w poniższych wzorcach jest wybierana stąd.</p></figcaption></figure>

---

## Dostępne wzorce

### 1. [Wzorzec integracji API](api-integration-pattern.md)

**Złożoność:** Średnia | **Czas konfiguracji:** 45–60 minut

Naucz się, jak integrować DocBits z zewnętrznymi API, aby pobierać, walidować i zapisywać dane z systemów zewnętrznych.

**Przypadki użycia:**
- Pobieranie cen w czasie rzeczywistym z systemów zewnętrznych
- Walidacja informacji o dostawcach względem baz danych podstawowych
- Wyszukiwanie szczegółów produktów w systemach katalogowych
- Pobieranie kursów wymiany z usług walutowych
- Weryfikacja adresów za pomocą usług geokodowania

**Użyte karty:** CALL_API, CONDITION_HTTPS_REQUEST_STATUS, ACTION_SET_FIELD_TO_TEXT, CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**[Zobacz pełny wzorzec →](api-integration-pattern.md)**

---

### 2. [Wzorzec zarządzania zadaniami](task-management-pattern.md)

**Złożoność:** Niska-Średnia | **Czas konfiguracji:** 30–45 minut

Opanuj sztukę tworzenia, przypisywania, śledzenia i zarządzania zadaniami w workflow DocBits dla procesów zatwierdzania i przeglądu.

**Przypadki użycia:**
- Tworzenie workflow zatwierdzania
- Przypisywanie zadań przeglądu użytkownikom
- Obsługa wyjątków wymagających interwencji człowieka
- Eskalacja problemów do przełożonych
- Tworzenie wielopoziomowych łańcuchów zatwierdzania
- Śledzenie ukończenia zadań i terminów

**Użyte karty:** tasks_create, ACTION_ASSIGN_TO_USER, ACTION_SEND_EMAIL_TO_GROUPS, CONDITION_TASK_STATUS

**[Zobacz pełny wzorzec →](task-management-pattern.md)**

---

### 3. [Wzorzec dopasowania zamówień (PO Matching)](po-matching-pattern.md)

**Złożoność:** Średnia-Wysoka | **Czas konfiguracji:** 60–90 minut

Wdróż kompleksowe workflow dopasowania zamówień zakupu, aby walidować faktury względem zamówień z routingiem opartym na tolerancjach.

**Przypadki użycia:**
- Walidacja faktur względem zamówień zakupu
- Wykrywanie błędów cenowych przed płatnością
- Identyfikacja rozbieżności ilościowych
- Egzekwowanie kontroli zakupowych
- Zapobieganie podwójnym płatnościom
- Automatyzacja dopasowania trójstronnego

**Użyte karty:** PURCHASE_ORDER_FULL_MATCH, CONDITION_DOC_TO_PO_UNIT_PRICE, CONDITION_DOC_TO_PO_QUANTITY, CONDITION_DOC_TO_PO_TAX_LINES

**[Zobacz pełny wzorzec →](po-matching-pattern.md)**

---

### 4. [Wzorzec logiki decyzyjnej](decision-logic-pattern.md)

**Złożoność:** Średnia | **Czas konfiguracji:** 30–45 minut

Wdróż złożone drzewa decyzyjne i logikę warunkowego routingu, aby przetwarzać dokumenty różnymi ścieżkami w oparciu o reguły biznesowe.

**Przypadki użycia:**
- Routing dokumentów według progów kwotowych
- Stosowanie różnych reguł dla różnych typów dokumentów
- Wdrażanie wielopoziomowej logiki zatwierdzania
- Obsługa złożonych polityk biznesowych
- Tworzenie dynamicznego routingu w oparciu o wiele kryteriów
- Wdrażanie macierzy zatwierdzania

**Użyte karty:** CONDITION_DOC_FIELD_AMOUNT, CONDITION_DOC_TYPE_IS_ISNOT, CONDITION_SUPPLIER_STATUS_IS_ISNOT, ACTION_ASSIGN_TO_USER

**[Zobacz pełny wzorzec →](decision-logic-pattern.md)**

---

### 5. [Wzorzec transformacji danych](data-transformation-pattern.md)

**Złożoność:** Średnia | **Czas konfiguracji:** 30–45 minut

Transformuj, obliczaj, formatuj i wzbogacaj dane dokumentu, aby przygotować je do eksportu, wykonywać obliczenia i standaryzować formaty.

**Przypadki użycia:**
- Obliczanie sum, sum częściowych, podatków
- Przeliczanie walut lub jednostek
- Formatowanie dat, liczb, tekstu
- Wyprowadzanie wartości z istniejących pól
- Wzbogacanie danych ze źródeł zewnętrznych
- Standaryzacja formatów danych
- Walidacja obliczeń

**Użyte karty:** ACTION_CALCULATE_FIELD, ACTION_SET_FIELD_TO_TEXT, ACTION_COPY_FIELD_VALUE, CALL_API, CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**[Zobacz pełny wzorzec →](data-transformation-pattern.md)**

---

## Pomoc w wyborze wzorca

### Według złożoności

| Złożoność | Wzorce | Najlepsze dla |
|------------|----------|----------|
| **Niska-Średnia** | [Zarządzanie zadaniami](task-management-pattern.md) | Początkujący, proste workflow |
| **Średnia** | [Integracja API](api-integration-pattern.md)<br>[Logika decyzyjna](decision-logic-pattern.md)<br>[Transformacja danych](data-transformation-pattern.md) | Zaawansowani użytkownicy, standardowe workflow |
| **Średnia-Wysoka** | [PO Matching](po-matching-pattern.md) | Profesjonaliści, złożona walidacja |

---

### Według przypadku użycia

| Chcę… | Użyj tego wzorca |
|--------------|------------------|
| Zintegrować się z systemami zewnętrznymi | [Wzorzec integracji API](api-integration-pattern.md) |
| Tworzyć workflow zatwierdzania | [Wzorzec zarządzania zadaniami](task-management-pattern.md) |
| Walidować względem zamówień zakupu | [Wzorzec dopasowania zamówień (PO Matching)](po-matching-pattern.md) |
| Routować w oparciu o warunki | [Wzorzec logiki decyzyjnej](decision-logic-pattern.md) |
| Obliczać i transformować dane | [Wzorzec transformacji danych](data-transformation-pattern.md) |

---

### Według branży/działu

| Branża/Dział | Zalecane wzorce |
|---------------------|---------------------|
| **Finanse/Księgowość** | [PO Matching](po-matching-pattern.md), [Zarządzanie zadaniami](task-management-pattern.md), [Transformacja danych](data-transformation-pattern.md) |
| **Zakupy** | [PO Matching](po-matching-pattern.md), [Logika decyzyjna](decision-logic-pattern.md), [Integracja API](api-integration-pattern.md) |
| **Operacje** | [Zarządzanie zadaniami](task-management-pattern.md), [Logika decyzyjna](decision-logic-pattern.md) |
| **IT/Integracja** | [Integracja API](api-integration-pattern.md), [Transformacja danych](data-transformation-pattern.md) |
| **Wszystkie działy** | [Logika decyzyjna](decision-logic-pattern.md), [Zarządzanie zadaniami](task-management-pattern.md) |

---

## Jak korzystać z tych wzorców

### Krok 1: Wybierz wzorzec

1. Przejrzyj powyższe opisy wzorców
2. Określ, który wzorzec pasuje do Twojego przypadku użycia
3. Sprawdź złożoność i szacowany czas konfiguracji
4. Przeczytaj sekcję „Kiedy stosować" w przewodniku po wzorcu

### Krok 2: Sprawdź wymagania wstępne

Każdy przewodnik po wzorcu wymienia:
- Wymaganą wiedzę
- Powiązane przewodniki do przeczytania najpierw
- Użyte karty
- Wymagania konfiguracyjne

### Krok 3: Postępuj zgodnie z instrukcjami krok po kroku

Każdy wzorzec zawiera:
- Kompletny przykład workflow
- Przewodnik wdrożenia krok po kroku
- Szablony konfiguracji
- Przykłady z praktyki
- Wskazówki dotyczące rozwiązywania problemów

### Krok 4: Dostosuj do swoich potrzeb

- Dostosuj przykład do swoich reguł biznesowych
- Wyreguluj progi i tolerancje
- Zmień logikę routingu
- Dodawaj lub usuwaj kroki według potrzeb
- Przetestuj gruntownie przed wdrożeniem produkcyjnym

### Krok 5: Monitoruj i optymalizuj

- Śledź wydajność workflow
- Monitoruj wskaźniki sukcesu
- Zbieraj opinie użytkowników
- Udoskonalaj konfigurację
- Dokumentuj dostosowania

---

## Kombinacje wzorców

Wiele rzeczywistych scenariuszy wymaga łączenia wielu wzorców:

### Przykład 1: Kompletne przetwarzanie faktur

```
1. Wzorzec integracji API → Pobierz aktualne ceny
2. Wzorzec transformacji danych → Oblicz sumy
3. Wzorzec PO Matching → Waliduj względem zamówienia
4. Wzorzec logiki decyzyjnej → Routuj na podstawie odchylenia
5. Wzorzec zarządzania zadaniami → Utwórz zadania zatwierdzania
```

### Przykład 2: Zatwierdzanie faktur o wysokiej wartości

```
1. Wzorzec transformacji danych → Oblicz kwoty
2. Wzorzec logiki decyzyjnej → Sprawdź progi
3. Wzorzec zarządzania zadaniami → Wielopoziomowe zatwierdzanie
4. Wzorzec integracji API → Powiadom systemy zewnętrzne
```

### Przykład 3: Obsługa wyjątków

```
1. Wzorzec PO Matching → Wykryj odchylenia
2. Wzorzec logiki decyzyjnej → Sklasyfikuj wagę wyjątku
3. Wzorzec zarządzania zadaniami → Utwórz zadania przeglądu
4. Wzorzec transformacji danych → Oblicz wpływ
```

---

## Szablony wzorców

Każdy wzorzec zawiera następujące ustandaryzowane sekcje:

1. **Przegląd** – Co robi wzorzec
2. **Kiedy stosować** – Odpowiednie przypadki użycia
3. **Kompletny przykład** – Rzeczywisty scenariusz
4. **Krok po kroku** – Instrukcja wdrożenia
5. **Konfiguracja** – Szablony konfiguracji kart
6. **Diagram workflow** – Reprezentacja wizualna
7. **Zaawansowane warianty** – Alternatywne wdrożenia
8. **Obsługa błędów** – Typowe problemy i rozwiązania
9. **Lista kontrolna testów** – Kroki walidacji
10. **Powiązane wzorce** – Uzupełniające wzorce
11. **Powiązane przewodniki** – Dokumentacja referencyjna

---

## Uzyskiwanie pomocy

### Zasoby wsparcia dla wzorców

**Dokumentacja:**
- [Pełny indeks przewodników po workflow](../README.md)
- [Przewodniki po poszczególnych kartach](../then/action/)
- [Referencja kart warunków](../and/condition-cards-complete-guide.md)

**Kontakt:**
- Opinie o wzorcach: docs@docbits.com
- Wsparcie techniczne: support@docbits.com
- Pomoc we wdrożeniu: consulting@docbits.com

---

## Następne kroki

**Nowy w temacie wzorców workflow?**
1. Zacznij od [Wzorca zarządzania zadaniami](task-management-pattern.md) – najłatwiejszy do zrozumienia
2. Przejrzyj [Wzorzec logiki decyzyjnej](decision-logic-pattern.md) – podstawowy dla wszystkich workflow
3. Poznaj [Wzorzec integracji API](api-integration-pattern.md) – częsta potrzeba integracyjna

**Gotowy do wdrożenia?**
1. Wybierz swój wzorzec z powyższej listy
2. Przeczytaj pełny przewodnik po wzorcu
3. Sprawdź wymagania wstępne i powiązane przewodniki
4. Postępuj zgodnie z instrukcją krok po kroku
5. Przetestuj na przykładowych dokumentach
6. Wdróż na produkcję
7. Monitoruj i optymalizuj

---

**Ostatnia aktualizacja:** 23 października 2025
**Opiekun:** Zespół Dokumentacji
**Wersja:** 1.0
