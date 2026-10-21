# Karty operacji na polach i tabelach

## Karty manipulacji na polu i tabeli - kompletny przewodnik

**Okładki:** 9 kart do modyfikowania pól i tabel dokumentów

***

Karty pól i tabel na tej stronie znajdują się w grupie **Wtedy** Kreatora przepływu pracy — akcje wykonywane po spełnieniu warunków Kiedy/I:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-pl.png" alt="Niezapisany przykład z kartami Kiedy, I oraz Wtedy. Uzupełnij wszystkie pola przed uruchomieniem. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs."><figcaption><p>Niezapisany przykład z kartami Kiedy, I oraz Wtedy. Uzupełnij wszystkie pola przed uruchomieniem. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs.</p></figcaption></figure>

***

### 📌 Informacje o wersji

**Karty wielowersyjne:** CALC\_COLUMNS (v2), CALC\_COLUMNS\_REGEX (v2), EDIT\_COLUMN (v2), AI\_CALC\_MTZ\_ETZ (v2)

**Wzorzec wersji:** Wszystkie karty manipulacji polami są zgodne ze wzorcem v1 → v2 ** Zmiana klucza:** v2 dodaje obsługę internacjonalizacji (i18n) z kluczami translacyjnymi

📖 [Pełna historia wersji](../../release.md) | [Wersje kart i zachowanie](../../cards-overview/card-versions-guide.md)

***

## Manipulacja polem dokumentu

### Karta: ACTION\_SET\_FIELD\_TO\_TEXT / Ustaw pole na wartość tekstową

#### Cel

Automatycznie wypełnia pole dokumentu określonym tekstem

#### Kiedy stosować

* Wypełnij pole decyzją
* Ustaw wartości domyślne
* Wypełnij standardowe informacje
* Zaktualizuj pole w oparciu o warunki

#### Jak to działa

```
IF Condition is true
    THEN Set Field "Category" to Value "Premium"
```

#### Przykładowe scenariusze

**Scenariusz 1: Ustaw kategorię zatwierdzenia**

```
Condition: Invoice amount > €10,000
    ↓
Action: Set "Approval_Category" field to "High Value"
    ↓
Result: Document now shows "Approval_Category: High Value"
```

**Scenariusz 2: Ustaw kategorię dostawcy**

```
Condition: Supplier name contains "ABC"
    ↓
Action: Set "Supplier_Type" field to "Preferred Supplier"
    ↓
Result: Document marked as "Preferred Supplier"
```

**Scenariusz 3: Ustaw notatki dotyczące przetwarzania**

```
Condition: Document has been rejected
    ↓
Action: Set "Processing_Notes" to "Requires supplier revision"
    ↓
Result: Note appears for next processor
```

#### Parametry

**Nazwa pola** Które pole zaktualizować

```
Examples: Category, Type, Status, Comment, Notes
```

**Wartość tekstowa** Co wpisać w polu

```
Examples: "Approved", "Pending Review", "High Priority"
```

#### Kroki konfiguracji

1. Wybierz pole do wypełnienia
2. Wprowadź wartość tekstową
3. Ustaw warunki (kiedy wypełnić)
4. Zapisz

***

### Karta: ACTION\_SET\_BOOLEAN\_FIELD / Ustaw pole wyboru

#### Cel

Automatycznie zaznacza lub odznacza pole wyboru

#### Kiedy stosować

* Oznacz jako przetworzone
* Ustaw flagi zatwierdzenia
* Włącz/wyłącz opcje
* Oznacz do eksportu

#### Jak to działa

```
IF Condition is true
    THEN Check/Uncheck the "Approved" box
```

#### Prawda = zaznaczona, Fałsz = niezaznaczona

**Przykłady:**

**Przykład 1: Oznacz jako zweryfikowane**

```
Condition: PO matches perfectly
    ↓
Action: Check "Verified" checkbox
    ↓
Result: ✅ Verified (checked)
```

**Przykład 2: Flaga do ręcznego przeglądu**

```
Condition: Price variance > 10%
    ↓
Action: Check "Requires_Manual_Review" checkbox
    ↓
Result: ✅ Requires_Manual_Review (marked)
```

**Przykład 3: Odznacz wstępnie wypełnione pole**

```
Condition: Supplier is blacklisted
    ↓
Action: Uncheck "Approved_for_Payment" checkbox
    ↓
Result: ☐ Approved_for_Payment (unchecked - blocked)
```

#### Parametry

```
Checkbox Field: [Choose field]
Set To: ☑ Checked (✅ True)
   or: ☐ Unchecked (❌ False)
```

***

### Karta: ACTION\_INVERT\_BOOLEAN\_FIELD / Przełącz pole wyboru

#### Cel

Odwraca stan pola wyboru (zaznaczone → niezaznaczone i odwrotnie)

#### Kiedy stosować

* Przełącz stan zatwierdzenia
* Przełącz tryb przetwarzania
* Odwróć poprzedni stan
* Zaktualizuj flagi logiczne

#### Jak to działa

```
Current state: ✅ (Checked)
    ↓
ACTION_INVERT: Toggle the box
    ↓
New state: ☐ (Unchecked)

OR

Current state: ☐ (Unchecked)
    ↓
ACTION_INVERT: Toggle the box
    ↓
New state: ✅ (Checked)
```

#### Przykład

```
Invoice received with "Priority" checked
    ↓
After processing, invert "Priority" checkbox
    ↓
Checkbox now unchecked (no longer priority)
```

***

### Karta: ACTION\_COPY\_DOCFIELD\_TO\_DOCFIELD / Skopiuj wartość pola

#### Cel

Kopiuje wartość z jednego pola do innego pola

#### Kiedy stosować

* Skopiuj informacje o dostawcy do informacji rozliczeniowych
* Duplikuj dane w różnych polach
* Standaryzuj format danych
* Utwórz kopię zapasową wartości

#### Jak to działa

```
Source Field: "Invoice_Supplier"  Value: "ABC Corp"
    ↓
COPY TO
    ↓
Target Field: "Billing_Partner"  Value: "ABC Corp"

Both fields now have same value
```

#### Prawdziwe przykłady

**Przykład 1: Skopiuj adres dostawy**

```
Source: "Delivery_Address" = "123 Main St, Berlin"
    ↓
Copy to: "Billing_Address"
    ↓
Result: Both fields show "123 Main St, Berlin"
```

**Przykład 2: Skopiuj kod dostawcy**

```
Source: "Supplier_Code_External" = "SUPP-789"
    ↓
Copy to: "Supplier_Code_Internal"
    ↓
Result: Both codes match, system recognizes supplier
```

**Przykład 3: Kwota kopii do zatwierdzenia**

```
Source: "Invoice_Total" = "€5000"
    ↓
Copy to: "Amount_to_Validate"
    ↓
Result: Validation field has correct amount
```

#### Parametry

```
Source Field: [Choose field to copy FROM]
Target Field: [Choose field to copy TO]
```

#### Notatki

* Oryginalne pole bez zmian
* Pole docelowe nadpisane wartością źródłową
* Dobry do standaryzacji danych

***

## Manipulacja tabelą

### Karta: EDIT\_COLUMN / Edytuj kolumnę tabeli

#### Cel

Zmienia wartości w kolumnie tabeli na podstawie warunków

#### Kiedy stosować

* Napraw błędy cenowe w elementach zamówienia
* Aktualizuj ilości
* Prawidłowe opisy przedmiotów
* Standaryzuj wartości

#### Jak to działa

```
Table Column: "Unit_Price"
Original Values: [100, 105, 103]
    ↓
FIND: Values matching condition
REPLACE: With new value
    ↓
Updated Column: [100, 110, 110] (example)
```

#### Przykład: napraw ceny

**Scenariusz: Ceny w niewłaściwej walucie**

```
Table "Line_Items" with column "Price"

Current prices: [100, 100, 100] (in wrong currency)
    ↓
Condition: "If Price column equals 100"
    ↓
Action: Replace with 95 (corrected price)
    ↓
Result: [95, 95, 95] (prices corrected)
```

#### Parametry

```
Table: [Choose table]
Column: [Choose column to edit]
Find: [Value to find]
Replace with: [New value]
Condition: [When to apply]
```

#### Typowe zastosowania

* Ustal ceny jednostkowe
* Standaryzuj opisy
* Prawidłowe ilości
* Zaktualizuj numery SKU

***

### Karta: CALC\_COLUMNS / Oblicz wartości kolumn

#### Cel

Wykonuje obliczenia na kolumnach tabeli i przechowuje wynik

#### Kiedy stosować

* Oblicz sumę wierszy (ilość × cena jednostkowa)
* Suma kolumn
* Oblicz rabaty
* Oblicz procenty

#### Jak to działa

```
Column A (Quantity): 100
Column B (Unit Price): €50
    ↓
CALCULATE: A × B
    ↓
Column C (Line Total): €5000
```

#### Typy obliczeń

**Typ 1: Proste mnożenie**

```
Formula: Qty × Unit Price = Line Total

Example:
100 units × €50/unit = €5000

Config:
  Column 1: Quantity
  Operator: ×
  Column 2: Unit Price
  Result Column: Line Total
```

**Typ 2: Dodawanie**

```
Formula: Base Price + Shipping + Tax = Total

Example:
€5000 + €100 + €950 = €6050

Config:
  Column 1: Base Price
  Operator: +
  Column 2: Shipping
  Operator: +
  Column 3: Tax
  Result Column: Total
```

**Typ 3: Obliczanie procentowe**

```
Formula: Amount × (1 + Tax%) = Total with Tax

Example:
€5000 × 1.19 = €5950

Config:
  Column: Amount
  Operator: × (1 + Tax%)
  Result Column: Amount_with_Tax
```

**Typ 4: Odejmowanie**

```
Formula: Original Price - Discount = Final Price

Example:
€100 - €10 = €90

Config:
  Column 1: Original Price
  Operator: -
  Column 2: Discount
  Result Column: Final Price
```

#### Przykład ze świata rzeczywistego

**Obliczanie pozycji pojedynczych faktury:**

```
Table: Invoice_Lines

Row 1:
  Quantity: 100
  Unit Price: €25.00
  Calculate: 100 × €25.00 = €2500.00 (Line Total)

Row 2:
  Quantity: 50
  Unit Price: €40.00
  Calculate: 50 × €40.00 = €2000.00 (Line Total)

Row 3:
  Quantity: 200
  Unit Price: €10.00
  Calculate: 200 × €10.00 = €2000.00 (Line Total)

Subtotal: €6500.00 (sum of line totals)
Tax (19%): €1235.00
Shipping: €100.00
TOTAL: €7835.00
```

#### Parametry

```
Table: [Select table]
Column 1: [First column]
Operator: [×, +, -, ÷, %]
Column 2: [Second column] (if needed)
Result Column: [Where to put answer]
```

***

### Karta: CALC\_COLUMNS\_REGEX / Oblicz za pomocą wzoru regularnego

#### Cel

Oblicza wartości kolumn na podstawie dopasowania wzorca

#### Kiedy stosować

* Wyodrębnij wartości z tekstu za pomocą wzorców
* Formatuj dane w oparciu o reguły
* Konwertuj wartości w oparciu o wzorce
* Analizuj tekst strukturalny

#### Jak to działa

**Dopasowanie wzorca regex:**

```
Original Value: "ABC-12345-XYZ"
Pattern: Extract numbers only
Calculation: Convert to "12345"
Result: "12345"
```

#### Przykład: wyodrębnij kod dostawcy

**Scenariusz: Numery artykułów zawierają informacje o dostawcy**

```
Table Column: "Article_Code"
Values: ["SUPP001-2025-A", "SUPP002-2025-B"]

Pattern: Extract supplier code (first 7 characters)
    ↓
Calculate: SUPP001, SUPP002
    ↓
Store in: "Supplier_Code" column

Result:
Article_Code: SUPP001-2025-A  →  Supplier_Code: SUPP001
Article_Code: SUPP002-2025-B  →  Supplier_Code: SUPP002
```

#### Przykład: sformatuj numery telefonów

**Scenariusz: niesformatowane numery telefonów**

```
Original: "491234567890"
Pattern: Format as: +49 123 4567 890
Result: "+49 123 4567 890"
```

#### Przykład: wyodrębnij ceny z tekstu

**Scenariusz: Ceny w formacie tekstowym**

```
Original: "Price is 99.99 EUR"
Pattern: Extract number only
Result: "99.99"
```

#### Parametry

```
Table: [Select table]
Column: [Column to analyze]
Regex Pattern: [Pattern to find]
Replacement: [What to replace with]
Result Column: [Where to store result]
```

#### Typowe wzorce wyrażeń regularnych

```
Numbers only: [0-9]+
Letters only: [a-zA-Z]+
First word: ^\w+
Extract €: €(\d+\.\d{2})
Date format: \d{4}-\d{2}-\d{2}
```

***

## Przykłady obliczeń

### Przykład 1: Obliczenie sumy faktury

```
Step 1: Calculate line totals
  Each row: Qty × Unit Price

Step 2: Sum all line totals
  Sum: €2500 + €2000 + €2000 = €6500

Step 3: Calculate tax
  Tax: €6500 × 0.19 = €1235

Step 4: Add shipping
  Final: €6500 + €1235 + €100 = €7835
```

### Przykład 2: Obliczanie wariancji

```
PO Price: €100
Invoice Price: €103

Variance = |(Invoice - PO)| / PO × 100
Variance = |3| / 100 × 100 = 3%

Store in "Price_Variance%" column
```

### Przykład 3: Wniosek o rabat

```
Original Price: €100
Discount %: 10%
Discount Amount: €100 × 0.10 = €10
Final Price: €100 - €10 = €90
```

***

## Przykład przepływu pracy manipulacji polami

```
Document arrives
    ↓
Check condition: "Amount > €5000?"
    ↓
YES → Set field "Category" = "High Value"
    ↓
Check condition: "Supplier is preferred?"
    ↓
YES → Check "FastTrack" checkbox
    ↓
Copy "Delivery_Address" to "Invoice_Address"
    ↓
In table: Calculate line totals (Qty × Price)
    ↓
In table: Calculate total with tax
    ↓
Document now has all calculated and populated fields
```

***

## Najlepsze praktyki

✅ **Wykonaj:**

* Zachowaj prostotę formuł
* Obliczenia testowe z przykładowymi danymi
* Sprawdź, czy wyniki mają sens
* Udokumentuj, dlaczego zmieniasz pola
* Użyj pola kopiowania, gdy dane są takie same

❌ **Nie:**

* Utwórz odniesienia cykliczne (A=B, B=A)
* Nadpisz ważne dane bez powodu
* Twórz zbyt złożone wzorce wyrażeń regularnych
* Zapomnij o sprawdzeniu wyników obliczeń
* Oblicz na niewłaściwej tabeli/kolumnach

***

## Rozwiązywanie problemów

### „Pole nie jest aktualizowane”

**Przyczyna:** Warunek nie został spełniony lub karta nie została aktywowana

**Rozwiązanie:**

* Sprawdź, czy warunek jest prawdziwy
* Sprawdź, czy karta znajduje się w przepływie pracy
* Przetestuj na przykładowych danych
* Sprawdź literówki w nazwie pola

### „Błędny wynik obliczeń”

**Przyczyna:** Wybrano nieprawidłowe kolumny lub niepoprawną formułę

**Rozwiązanie:**

* Sprawdź kolumny źródłowe
* Sprawdź, czy formuła jest poprawna
* Przetestuj ręcznie
* Przejrzyj miejsca dziesiętne/zaokrąglenia

### „Tabela pokazuje błąd”

**Przyczyna:** Kolumna, do której odnosi się odwołanie, nie istnieje

**Rozwiązanie:**

* Sprawdź pisownię nazwy kolumny
* Sprawdź, czy kolumna zawiera dane
* Upewnij się, że typ danych kolumny odpowiada obliczeniom
* W razie potrzeby dodaj brakujące kolumny

***

## Powiązane karty

* **ACTION\_COPY\_DOCFIELD\_TO\_DOCFIELD** – Kopiuj wartości
* **EDIT\_COLUMN** – Zmień wartości tabeli
* **CALC\_COLUMNS** - Oblicz formuły
* **ACTION\_SET\_FIELD\_TO\_TEXT** – Ustaw wartości tekstowe
* **ACTION\_SET\_BOOLEAN\_FIELD** — Pola wyboru
