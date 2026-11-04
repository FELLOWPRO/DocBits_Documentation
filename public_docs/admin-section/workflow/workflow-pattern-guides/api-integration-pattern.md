# Wzorzec integracji API

**Typ wzorca:** Integracja
**Złożoność:** Średnia
**Szacowany czas konfiguracji:** 45-60 minut
**Typowe przypadki użycia:** Pobieranie danych zewnętrznych, walidacja cen, wyszukiwanie danych podstawowych

---

## Przegląd wzorca

Ten wzorzec pokazuje, jak zintegrować DocBits z zewnętrznymi interfejsami API, aby pobierać, walidować i przechowywać dane z systemów zewnętrznych. Jest to jeden z najczęstszych wzorców przepływu pracy służący do łączenia DocBits z systemami wyceny, usługami walidacji, systemami ERP i innymi zewnętrznymi źródłami danych.

**Co robi ten wzorzec:**
1. Wywołuje zewnętrzne API w celu pobrania danych
2. Waliduje odpowiedź API
3. Przechowuje dane odpowiedzi w polach dokumentu
4. Podejmuje decyzje na podstawie pobranych danych
5. Odpowiednio kieruje dokumenty

---

## Kiedy używać tego wzorca

Użyj tego wzorca, gdy musisz:
- ✅ Pobierać ceny w czasie rzeczywistym z systemów zewnętrznych
- ✅ Walidować informacje o dostawcy względem głównej bazy danych
- ✅ Wyszukiwać szczegóły produktu w systemach katalogowych
- ✅ Pobierać kursy wymiany walut z usług walutowych
- ✅ Weryfikować adresy za pomocą usług geokodowania
- ✅ Sprawdzać poziomy zapasów w systemach magazynowych
- ✅ Walidować stawki podatkowe w usługach podatkowych

**Nie używaj tego wzorca, gdy:**
- ❌ Dane znajdują się już w danych podstawowych DocBits (użyj zamiast tego wyszukiwania danych podstawowych)
- ❌ System zewnętrzny nie posiada API
- ❌ Dane nie zmieniają się często (rozważ import ręczny)

---

## Kompletny przykład przepływu pracy

### Scenariusz: Walidacja ceny faktury względem API aktualnych cen

**Wymagania biznesowe:**
- Dostawca przesyła fakturę
- Faktura wykazuje cenę jednostkową 52,00 EUR
- Musimy zweryfikować, czy jest ona zgodna z aktualnym cennikiem dostawcy
- Jeśli cena różni się o więcej niż 5%, przekaż do przeglądu

**Użyte karty przepływu pracy:**
1. CALL_API - Pobierz aktualną cenę z API dostawcy
2. CONDITION_HTTPS_REQUEST_STATUS - Sprawdź, czy wywołanie API powiodło się
3. ACTION_SET_FIELD_TO_TEXT - Zapisz cenę z API w polu dokumentu
4. CONDITION_COMPARE_TWO_DOCFIELD_VALUES - Porównaj cenę z faktury z ceną z API
5. ACTION_ASSIGN_TO_USER - Kieruj na podstawie wyniku porównania
6. tasks_create - Utwórz zadanie przeglądu w razie potrzeby

---

## Wdrażanie krok po kroku

### Krok 1: Wywołaj zewnętrzne API

**Karta:** CALL_API lub ACTION_CALL_EXTERNAL_API

**Konfiguracja:**
```json
{
  "api_endpoint": "https://api.supplier-system.com/v1/pricing",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer TWÓJ_KLUCZ_API",
    "Content-Type": "application/json"
  },
  "request_body": {
    "product_id": "{{DOCUMENT_FIELD:Kod_produktu}}",
    "supplier_id": "{{DOCUMENT_FIELD:Kod_dostawcy}}",
    "quantity": "{{DOCUMENT_FIELD:Ilosc}}",
    "currency": "EUR"
  }
}
```

---

### Krok 2: Waliduj odpowiedź API

**Karta:** CONDITION_HTTPS_REQUEST_STATUS

**Konfiguracja:**
```
Operator: JEST RÓWNY
Kod statusu: 200
```

**Logika:**
```
JEŚLI API zwróci 200 (sukces):
  → Kontynuuj zapisywanie danych
W PRZECIWNYM RAZIE:
  → Kieruj do przepływu obsługi błędów API
  → Wyślij powiadomienie e-mail
  → Utwórz zadanie ręcznego przeglądu
```

---

### Krok 3: Zapisz odpowiedź API w polach dokumentu

**Karta:** ACTION_SET_FIELD_TO_TEXT (lub odpowiedni moduł ustawiania pól)

**Konfiguracja:**

**Pole 1: Aktualna_Cena_API**
```
Nazwa pola: Aktualna_Cena_API
Wartość pola: {{API_RESPONSE:data.unit_price}}
Typ pola: Liczba
```

---

### Krok 4: Porównaj cenę faktury z ceną z API

**Karta:** CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**Konfiguracja:**
```
Pole 1: Cena_Jednostkowa_Faktury (z ekstrakcji OCR)
Pole 2: Aktualna_Cena_API (z odpowiedzi API)
Operator: Oblicz procent odchylenia
Tolerancja: 5%
```

**Obliczenie:**
```
Odchylenie % = |(Cena_Faktury - Cena_API)| / Cena_API × 100

Przykład:
  Cena faktury: 52,00 EUR
  Cena API: 50,00 EUR
  Odchylenie = |52 - 50| / 50 × 100 = 4%

  Czy 4% ≤ 5% tolerancji? TAK ✅
  Wynik: POZYTYWNY
```

---

### Krok 5: Kieruj na podstawie wyniku walidacji

**Scenariusz A: Cena w granicach tolerancji (Sukces)**

**Karty:**
- ACTION_SET_FIELD_TO_TEXT
  - Ustaw pole „Status_walidacji_ceny” = „POZYTYWNY”
- ACTION_APPROVE_DOCUMENT
  - Automatycznie zatwierdź dokument

**Scenariusz B: Cena poza granicami tolerancji (Błąd)**

**Karty:**
- tasks_create
  - Tytuł zadania: „Przegląd odchylenia ceny - {{DOCUMENT_NUMBER}}”
- ACTION_ASSIGN_TO_USER
  - Przypisz do: Menedżer ds. Zakupów

---

## Szablony konfiguracji

### Szablon 1: Proste zapytanie GET (Wyszukiwanie)

```json
{
  "card": "CALL_API",
  "endpoint": "https://api.example.com/lookup",
  "method": "GET",
  "headers": {
    "Authorization": "Bearer {{API_KEY}}"
  },
  "parameters": {
    "id": "{{DOCUMENT_FIELD:Lookup_ID}}"
  }
}
```

---

## Obsługa błędów

### Typowe błędy i rozwiązania

#### Błąd 1: Przekroczenie czasu połączenia (Timeout)

**Rozwiązanie:**
```
1. Sprawdź URL punktu końcowego API
2. Zweryfikuj łączność sieciową
3. Wdróż obsługę przekroczenia czasu:
   JEŚLI CONDITION_HTTPS_REQUEST_STATUS = TIMEOUT:
     → Utwórz zadanie „API Timeout”
     → Powiadom wsparcie IT
```

---

## Lista kontrolna testów

- [ ] Przetestuj wywołanie API z prawidłowymi danymi
- [ ] Przetestuj wywołanie API z nieprawidłowymi danymi
- [ ] Przetestuj scenariusz przekroczenia czasu (co się stanie, gdy API działa wolno?)
- [ ] Przetestuj błąd uwierzytelniania
- [ ] Przetestuj nieprawidłowy format odpowiedzi
- [ ] Przetestuj zapisywanie pól (dane zapisane poprawnie?)
- [ ] Przetestuj logikę porównywania (prawidłowe obliczenia?)
- [ ] Przetestuj routing (dokumenty trafiają we właściwe miejsce?)

---

**Wersja wzorca:** 1.0
**Ostatnia aktualizacja:** 23 października 2025 r.
**Trudność:** Średnia
