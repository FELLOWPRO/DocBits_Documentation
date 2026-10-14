# Wzorzec integracji API

**Typ wzorca:** Integracja
**Złożoność:** Średnia
**Szacowana konfiguracja:** 45–60 minut
**Typowe przypadki użycia:** Pobieranie danych zewnętrznych, walidacja cen, wyszukiwanie danych podstawowych

---

Ten wzorzec budujesz w **Workflow Builder** (Workflow Dashboard → Workflow List → Add Workflow). Kliknij **Add Card**, aby otworzyć bibliotekę kart, i wybierz karty używane przez ten wzorzec — `CALL_API`, `CONDITION_HTTPS_REQUEST_STATUS`, `ACTION_SET_FIELD_TO_TEXT` oraz `CONDITION_COMPARE_TWO_DOCFIELD_VALUES`:

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Biblioteka Add Card w Workflow Builder, pogrupowana według kategorii"><figcaption><p>Biblioteka <strong>Add Card</strong> — wybierz karty API, warunków i pól używane przez ten wzorzec z tych kategorii.</p></figcaption></figure>

---

## Przegląd wzorca

Ten wzorzec pokazuje, jak zintegrować DocBits z zewnętrznymi API, aby pobierać, walidować i zapisywać dane z systemów zewnętrznych. Jest to jeden z najczęstszych wzorców workflow służących do łączenia DocBits z systemami cenowymi, usługami walidacji, systemami ERP i innymi zewnętrznymi źródłami danych.

**Co robi ten wzorzec:**
1. Wywołuje zewnętrzne API w celu pobrania danych
2. Waliduje odpowiedź API
3. Zapisuje dane z odpowiedzi w polach dokumentu
4. Podejmuje decyzje na podstawie pobranych danych
5. Routuje dokumenty odpowiednio

---

## Kiedy stosować ten wzorzec

Stosuj ten wzorzec, gdy potrzebujesz:
- ✅ Pobierać ceny w czasie rzeczywistym z systemów zewnętrznych
- ✅ Walidować informacje o dostawcach względem bazy danych podstawowych
- ✅ Wyszukiwać szczegóły produktów w systemach katalogowych
- ✅ Pobierać kursy wymiany z usług walutowych
- ✅ Weryfikować adresy za pomocą usługi geokodowania
- ✅ Sprawdzać stany magazynowe w systemach magazynowych
- ✅ Walidować stawki podatkowe z usług podatkowych

**Nie stosuj tego wzorca, gdy:**
- ❌ dane są już dostępne w danych podstawowych DocBits (zamiast tego użyj wyszukiwania danych podstawowych)
- ❌ system zewnętrzny nie posiada API (zamiast tego użyj wzorca skryptu DocOperator)
- ❌ dane rzadko się zmieniają (rozważ import ręczny)

---

## Kompletny przykład workflow

### Scenariusz: Walidacja ceny faktury względem aktualnego API cenowego

**Wymaganie biznesowe:**
- Dostawca przesyła fakturę
- Faktura wykazuje cenę jednostkową 52,00 €
- Musimy sprawdzić, czy zgadza się to z aktualnym cennikiem dostawcy
- Jeśli cena odbiega o więcej niż 5%, eskaluj do przeglądu

**Użyte karty workflow:**
1. CALL_API – Pobierz aktualną cenę z API dostawcy
2. CONDITION_HTTPS_REQUEST_STATUS – Sprawdź, czy wywołanie API powiodło się
3. ACTION_SET_FIELD_TO_TEXT – Zapisz cenę z API w polu dokumentu
4. CONDITION_COMPARE_TWO_DOCFIELD_VALUES – Porównaj cenę faktury z ceną z API
5. ACTION_ASSIGN_TO_USER – Routuj na podstawie wyniku porównania
6. tasks_create – W razie potrzeby utwórz zadanie przeglądu

---

## Wdrożenie krok po kroku

### Krok 1: Wywołaj zewnętrzne API

**Karta:** CALL_API lub ACTION_CALL_EXTERNAL_API

**Konfiguracja:**
```json
{
  "api_endpoint": "https://api.supplier-system.com/v1/pricing",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
  },
  "request_body": {
    "product_id": "{{DOCUMENT_FIELD:Product_Code}}",
    "supplier_id": "{{DOCUMENT_FIELD:Supplier_Code}}",
    "quantity": "{{DOCUMENT_FIELD:Quantity}}",
    "currency": "EUR"
  }
}
```

**Oczekiwana odpowiedź:**
```json
{
  "success": true,
  "data": {
    "product_id": "ABC123",
    "unit_price": 50.00,
    "currency": "EUR",
    "valid_until": "2025-12-31",
    "discount_applicable": true
  }
}
```

**Referencja przewodnika:** [Przewodnik Call API](../then/action/call-api-guide.md)

---

### Krok 2: Waliduj odpowiedź API

**Karta:** CONDITION_HTTPS_REQUEST_STATUS

**Konfiguracja:**
```
Operator: IS EQUAL TO
Status Code: 200
```

**Logika:**
```
IF API returns 200 (success):
  → Continue to store data
ELSE:
  → Route to "API Error" handling workflow
  → Send email notification
  → Create manual review task
```

**Referencja przewodnika:** [Przewodnik po kartach warunków – status HTTP](../and/condition-cards-complete-guide.md#condition-https-request-status)

---

### Krok 3: Zapisz odpowiedź API w polach dokumentu

**Karta:** ACTION_SET_FIELD_TO_TEXT (lub równoważny seter pola)

**Konfiguracja:**

**Pole 1: Current_API_Price**
```
Field Name: Current_API_Price
Field Value: {{API_RESPONSE:data.unit_price}}
Field Type: Number
```

**Pole 2: API_Price_Valid_Until**
```
Field Name: API_Price_Valid_Until
Field Value: {{API_RESPONSE:data.valid_until}}
Field Type: Date
```

**Pole 3: API_Discount_Available**
```
Field Name: API_Discount_Available
Field Value: {{API_RESPONSE:data.discount_applicable}}
Field Type: Boolean
```

**Wynik:** Dane z API są teraz zapisane w polach dokumentu do późniejszego wykorzystania

**Referencja przewodnika:** [Przewodnik po manipulacji polami – zapisywanie danych API](../then/document-field/field-manipulation-guide.md#storing-api-data)

---

### Krok 4: Porównaj cenę faktury z ceną z API

**Karta:** CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**Konfiguracja:**
```
Field 1: Invoice_Unit_Price (from OCR extraction)
Field 2: Current_API_Price (from API response)
Operator: Calculate variance percentage
Tolerance: 5%
```

**Obliczenie:**
```
Variance % = |(Invoice_Price - API_Price)| / API_Price × 100

Example:
  Invoice Price: €52.00
  API Price: €50.00
  Variance = |52 - 50| / 50 × 100 = 4%

  Is 4% ≤ 5% tolerance? YES ✅
  Result: PASS
```

**Referencja przewodnika:** [Przewodnik po kartach warunków – porównanie pól](../and/condition-cards-complete-guide.md#field-comparison)

---

### Krok 5: Routuj na podstawie wyniku walidacji

**Scenariusz A: Cena w granicach tolerancji (Pass)**

**Karty:**
- ACTION_SET_FIELD_TO_TEXT
  - Ustaw pole „Price_Validation_Status" = „PASS"
  - Ustaw pole „Price_Variance_Percent" = „4%"
- ACTION_APPROVE_DOCUMENT
  - Automatycznie zatwierdź dokument

**Scenariusz B: Cena poza tolerancją (Fail)**

**Karty:**
- ACTION_SET_FIELD_TO_TEXT
  - Ustaw pole „Price_Validation_Status" = „FAIL"
  - Ustaw pole „Price_Variance_Percent" = „12%" (przykład)
- tasks_create
  - Tytuł zadania: „Review Price Variance - {{DOCUMENT_NUMBER}}"
  - Opis zadania: „Invoice price (€{{Invoice_Unit_Price}}) exceeds API price (€{{Current_API_Price}}) by {{Price_Variance_Percent}}"
  - Priorytet: Wysoki
- ACTION_ASSIGN_TO_USER
  - Przypisz do: Kierownika zakupów
- ACTION_SEND_EMAIL_TO_GROUPS
  - Wyślij powiadomienie do zespołu zakupów

**Referencje przewodników:**
- [Przewodnik po przypisaniu](../then/assignee/assignment-user-guide.md)
- [Przewodnik po przypisywaniu zadań](../then/task/task-assignment-guide.md)
- [Przewodnik po wysyłaniu e-maili](../then/action/send-email-groups-guide.md)

---

## Kompletny diagram workflow

```
DOCUMENT ARRIVES (Invoice with Product ABC123, Price €52)
│
├─ STEP 1: Call Pricing API
│  Card: CALL_API
│  Request: Get current price for ABC123
│  │
│  ├─ SUCCESS (200) ✅
│  │  Response: {"unit_price": 50.00}
│  │  │
│  │  ├─ STEP 2: Check API Status
│  │  │  Card: CONDITION_HTTPS_REQUEST_STATUS
│  │  │  Result: 200 = Success
│  │  │  │
│  │  │  ├─ STEP 3: Store API Data
│  │  │  │  Card: ACTION_SET_FIELD_TO_TEXT
│  │  │  │  Action: Store €50 in "Current_API_Price" field
│  │  │  │  │
│  │  │  │  ├─ STEP 4: Compare Prices
│  │  │  │  │  Card: CONDITION_COMPARE_TWO_DOCFIELD_VALUES
│  │  │  │  │  Calculate: Variance = |52-50|/50 = 4%
│  │  │  │  │  │
│  │  │  │  │  ├─ IF Variance ≤ 5% (PASS) ✅
│  │  │  │  │  │  │
│  │  │  │  │  │  ├─ Set Status Field: "PASS"
│  │  │  │  │  │  └─ Auto-Approve Document
│  │  │  │  │  │     → END (Document Approved)
│  │  │  │  │  │
│  │  │  │  │  └─ IF Variance > 5% (FAIL) ❌
│  │  │  │  │     │
│  │  │  │  │     ├─ Set Status Field: "FAIL"
│  │  │  │  │     ├─ Create Review Task
│  │  │  │  │     ├─ Assign to Procurement Manager
│  │  │  │  │     └─ Send Email Notification
│  │  │  │  │        → END (Pending Review)
│  │  │  │  │
│  │  │  │  └─ [Field storage complete]
│  │  │  │
│  │  │  └─ [Status check complete]
│  │  │
│  │  └─ [API data retrieved]
│  │
│  └─ ERROR (Non-200) ❌
│     │
│     ├─ Set Error Status
│     ├─ Create "API Error" Task
│     ├─ Assign to IT Support
│     └─ Send Email to Admin
│        → END (API Error - Manual Review)
```

---

## Szablony konfiguracji

### Szablon 1: Proste żądanie GET (wyszukiwanie)

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

**Zastosowanie:** Proste wyszukiwanie danych po ID

---

### Szablon 2: Żądanie POST z treścią (walidacja)

```json
{
  "card": "CALL_API",
  "endpoint": "https://api.example.com/validate",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer {{API_KEY}}",
    "Content-Type": "application/json"
  },
  "body": {
    "document_number": "{{DOCUMENT_NUMBER}}",
    "supplier_id": "{{DOCUMENT_FIELD:Supplier_Code}}",
    "total_amount": "{{DOCUMENT_FIELD:Total_Amount}}",
    "currency": "{{DOCUMENT_FIELD:Currency}}"
  }
}
```

**Zastosowanie:** Wysyłanie danych dokumentu do walidacji

---

### Szablon 3: Złożone żądanie z danymi zagnieżdżonymi

```json
{
  "card": "CALL_API",
  "endpoint": "https://api.example.com/process",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer {{API_KEY}}",
    "Content-Type": "application/json"
  },
  "body": {
    "document": {
      "type": "{{DOCUMENT_TYPE}}",
      "number": "{{DOCUMENT_NUMBER}}",
      "date": "{{DOCUMENT_FIELD:Invoice_Date}}"
    },
    "vendor": {
      "code": "{{DOCUMENT_FIELD:Supplier_Code}}",
      "name": "{{DOCUMENT_FIELD:Supplier_Name}}"
    },
    "items": [
      {
        "product": "{{TABLE_FIELD:Product_Code}}",
        "quantity": "{{TABLE_FIELD:Quantity}}",
        "unit_price": "{{TABLE_FIELD:Unit_Price}}"
      }
    ]
  }
}
```

**Zastosowanie:** Złożone przetwarzanie dokumentów z danymi tabelarycznymi

---

## Obsługa błędów

### Typowe błędy i rozwiązania

#### Błąd 1: Przekroczenie limitu czasu połączenia

**Objawy:**
- API nie odpowiada
- Workflow pozostaje w stanie oczekiwania

**Rozwiązanie:**
```
1. Check API endpoint URL (typo?)
2. Verify network connectivity
3. Check API service status
4. Implement timeout handling:

   IF CONDITION_HTTPS_REQUEST_STATUS = TIMEOUT:
     → Create "API Timeout" task
     → Assign to IT Support
     → Send email notification
     → Use fallback value (if available)
```

#### Błąd 2: 401 Unauthorized

**Objawy:**
- API zwraca status 401
- Uwierzytelnianie nie powiodło się

**Rozwiązanie:**
```
1. Verify API key is correct
2. Check if API key expired
3. Ensure Authorization header formatted correctly
4. Implement auth error handling:

   IF CONDITION_HTTPS_REQUEST_STATUS = 401:
     → Create "API Auth Failed" task
     → Assign to Admin
     → Log error details
     → Stop workflow execution
```

#### Błąd 3: Nieprawidłowy format odpowiedzi

**Objawy:**
- Odpowiedź otrzymana, ale niemożliwa do sparsowania
- Brakuje oczekiwanych pól

**Rozwiązanie:**
```
1. Verify API documentation
2. Check response structure matches expectations
3. Implement response validation:

   IF API_RESPONSE:data.unit_price IS NULL:
     → Set default value
     → Create "Invalid Response" task
     → Log response for debugging
```

**Referencja przewodnika:** [Call API – rozwiązywanie problemów](../then/action/call-api-guide.md#troubleshooting)

---

## Zaawansowane warianty

### Wariant 1: Łączenie wielu API w łańcuch

**Scenariusz:** Wymagane dane z wielu API

```
Step 1: Call Supplier API → Get Supplier Details
Step 2: Call Product API → Get Product Info (using Supplier ID from Step 1)
Step 3: Call Pricing API → Get Price (using Product ID from Step 2)
Step 4: Validate & Store all data
```

---

### Wariant 2: Warunkowe wywołania API

**Scenariusz:** Wywołuj API tylko pod określonymi warunkami

```
IF DOCUMENT_TYPE = "Invoice" AND AMOUNT > 10000:
  → Call Pricing Validation API
  → Verify prices
ELSE:
  → Skip API call (not needed for small amounts)
```

---

### Wariant 3: Buforowanie odpowiedzi API

**Scenariusz:** Ograniczenie liczby wywołań API poprzez buforowanie odpowiedzi

```
1. Check if "API_Last_Called" date is today
2. IF Yes:
     → Use cached value from "Cached_API_Price" field
3. IF No:
     → Call API
     → Store response in "Cached_API_Price"
     → Set "API_Last_Called" to today
```

---

## Aspekty wydajności

### Najlepsze praktyki

✅ **Zalecane:**
- Buforuj odpowiedzi API, gdy to możliwe
- Stosuj ustawienia limitu czasu (30–60 sekund)
- Wdróż logikę ponawiania dla błędów przejściowych
- Rejestruj wywołania API do diagnostyki błędów
- Monitoruj użycie/koszty API
- Najpierw testuj na przykładowych dokumentach

❌ **Niezalecane:**
- Wywoływanie API synchronicznie dla każdego dokumentu (rozważ przetwarzanie wsadowe)
- Ignorowanie błędów odpowiedzi
- Twarde kodowanie danych uwierzytelniających w workflow
- Wykonywanie zbędnych wywołań API
- Pozostawianie nieobsłużonych przekroczeń limitu czasu

---

## Lista kontrolna testów

Przed wdrożeniem tego wzorca na produkcję:

- [ ] Przetestuj wywołanie API z prawidłowymi danymi
- [ ] Przetestuj wywołanie API z nieprawidłowymi danymi
- [ ] Przetestuj scenariusz przekroczenia limitu czasu (co się dzieje, gdy API jest wolne?)
- [ ] Przetestuj błędy uwierzytelniania
- [ ] Przetestuj nieprawidłowy format odpowiedzi
- [ ] Przetestuj zapisywanie pól (czy dane zapisane poprawnie?)
- [ ] Przetestuj logikę porównania (czy obliczenia poprawne?)
- [ ] Przetestuj routing (czy dokumenty trafiają we właściwe miejsce?)
- [ ] Przetestuj obsługę błędów (czy błędy obsłużone czysto?)
- [ ] Przetestuj przy dużym wolumenie (czy wydajność akceptowalna?)

---

## Przykłady z praktyki

### Przykład 1: Wyszukiwanie kursu wymiany

**API:** https://api.exchangerate-api.com/v4/latest/USD

**Workflow:**
1. Wyodrębnij walutę faktury: „GBP"
2. Wywołaj API kursów wymiany
3. Pobierz kurs GBP→EUR
4. Oblicz równowartość w EUR
5. Zapisz w polu „Amount_EUR"
6. Kontynuuj przetwarzanie z kwotą w EUR

---

### Przykład 2: Weryfikacja zdolności kredytowej dostawcy

**API:** Wewnętrzna usługa weryfikacji zdolności kredytowej

**Workflow:**
1. Wyodrębnij kod dostawcy
2. Wywołaj API weryfikacji zdolności kredytowej
3. Pobierz status zdolności kredytowej: „APPROVED" lub „BLOCKED"
4. IF BLOCKED:
   - Zatrzymaj przetwarzanie
   - Utwórz pilne zadanie
   - Powiadom zespół finansowy
5. IF APPROVED:
   - Kontynuuj normalny workflow

---

### Przykład 3: Wzbogacanie danych podstawowych produktu

**API:** Usługa katalogu produktów

**Workflow:**
1. Wyodrębnij kod produktu z faktury
2. Wywołaj API produktów
3. Pobierz: nazwę produktu, kategorię, konto księgowe
4. Zapisz w polach dokumentu
5. Wykorzystaj do automatycznej dekretacji

---

## Powiązane wzorce

### Ten wzorzec dobrze współgra z:

- **[Wzorzec transformacji danych](data-transformation-pattern.md)** – Transformacja danych z odpowiedzi API
- **[Wzorzec logiki decyzyjnej](decision-logic-pattern.md)** – Routing na podstawie danych z API
- **[Wzorzec zarządzania zadaniami](task-management-pattern.md)** – Tworzenie zadań dla błędów API
- **[Wzorzec PO Matching](po-matching-pattern.md)** – Łączenie cen z API z walidacją PO

---

## Powiązane przewodniki

### Wymagania wstępne
- [Przewodnik Call API](../then/action/call-api-guide.md) – Dokumentacja karty API
- [Przewodnik po kartach warunków](../and/condition-cards-complete-guide.md) – Logika warunków
- [Przewodnik po manipulacji polami](../then/document-field/field-manipulation-guide.md) – Operacje na polach

### Powiązane karty
- **CALL_API** – [Przewodnik Call API](../then/action/call-api-guide.md)
- **ACTION_HTTPS_REQUEST** – [Przewodnik po żądaniu HTTPS](../then/action/https-request-guide.md)
- **CONDITION_HTTPS_REQUEST_STATUS** – [Przewodnik po kartach warunków](../and/condition-cards-complete-guide.md#condition-https-request-status)
- **ACTION_SET_FIELD_TO_TEXT** – [Przewodnik po manipulacji polami](../then/document-field/field-manipulation-guide.md#set-field)
- **CONDITION_COMPARE_TWO_DOCFIELD_VALUES** – [Przewodnik po kartach warunków](../and/condition-cards-complete-guide.md#field-comparison)

---

## Wsparcie i zasoby

**Potrzebujesz pomocy?**
- Przeczytaj [Call API – rozwiązywanie problemów](../then/action/call-api-guide.md#troubleshooting)
- Sprawdź [kody odpowiedzi API](../then/action/call-api-guide.md#response-scenarios)
- Najpierw przetestuj API za pomocą Postmana
- Skontaktuj się ze wsparciem dostawcy API

**Opinie:**
- Zgłaszaj problemy z wzorcem na: docs@docbits.com
- Proponuj usprawnienia
- Dziel się swoimi przypadkami użycia

---

**Wersja wzorca:** 1.0
**Ostatnia aktualizacja:** 23 października 2025
**Trudność:** Średnia
**Szacowany czas:** 45–60 minut
**Wskaźnik sukcesu:** Wysoki (przy stabilnym API)
