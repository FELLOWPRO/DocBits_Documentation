# Field & Table Manipulation Cards - Complete Guide

Te karty trafiają do grupy **Then** w Kreatorze przepływów — akcje uruchamiane po spełnieniu warunków When/And:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Karty dodaje się do grupy <strong>Then</strong> za pomocą <strong>Add Card</strong>.</p></figcaption></figure>

**Obejmuje:** 9 kart do modyfikowania pól i tabel dokumentu

---

# Manipulacja polami dokumentu

## Karta: ACTION_SET_FIELD_TO_TEXT / Set Field to Text Value

### Cel
Automatycznie wypełnia pole dokumentu określonym tekstem

### Kiedy używać
- Wypełnianie pola na podstawie decyzji
- Ustawianie wartości domyślnych
- Wypełnianie standaryzowanych informacji
- Aktualizacja pola na podstawie warunków

### Jak to działa
```
IF Condition is true
    THEN Set Field "Category" to Value "Premium"
```

### Przykładowe scenariusze

**Scenariusz 1: Ustawienie kategorii zatwierdzenia**
```
Condition: Invoice amount > €10,000
    ↓
Action: Set "Approval_Category" field to "High Value"
    ↓
Result: Document now shows "Approval_Category: High Value"
```

**Scenariusz 2: Ustawienie kategorii dostawcy**
```
Condition: Supplier name contains "ABC"
    ↓
Action: Set "Supplier_Type" field to "Preferred Supplier"
    ↓
Result: Document marked as "Preferred Supplier"
```

**Scenariusz 3: Ustawienie uwag dotyczących przetwarzania**
```
Condition: Document has been rejected
    ↓
Action: Set "Processing_Notes" to "Requires supplier revision"
    ↓
Result: Note appears for next processor
```

### Parametry

**Field Name**
Które pole zaktualizować
```
Examples: Category, Type, Status, Comment, Notes
```

**Text Value**
Co umieścić w polu
```
Examples: "Approved", "Pending Review", "High Priority"
```

### Kroki konfiguracji
1. Wybierz pole do wypełnienia
2. Wprowadź wartość tekstową
3. Ustaw warunki (kiedy wypełnić)
4. Zapisz

---

## Karta: ACTION_SET_BOOLEAN_FIELD / Set Checkbox Field

### Cel
Automatycznie zaznacza lub odznacza pole wyboru

### Kiedy używać
- Oznaczanie jako przetworzone
- Ustawianie flag zatwierdzenia
- Włączanie/wyłączanie opcji
- Oznaczanie do eksportu

### Jak to działa
```
IF Condition is true
    THEN Check/Uncheck the "Approved" box
```

### True = zaznaczone, False = niezaznaczone

**Przykłady:**

**Przykład 1: Oznaczenie jako zweryfikowane**
```
Condition: PO matches perfectly
    ↓
Action: Check "Verified" checkbox
    ↓
Result: ✅ Verified (checked)
```

**Przykład 2: Oznaczenie do przeglądu ręcznego**
```
Condition: Price variance > 10%
    ↓
Action: Check "Requires_Manual_Review" checkbox
    ↓
Result: ✅ Requires_Manual_Review (marked)
```

**Przykład 3: Odznaczenie wstępnie wypełnionego pola**
```
Condition: Supplier is blacklisted
    ↓
Action: Uncheck "Approved_for_Payment" checkbox
    ↓
Result: ☐ Approved_for_Payment (unchecked - blocked)
```

### Parametry
```
Checkbox Field: [Choose field]
Set To: ☑ Checked (✅ True)
   or: ☐ Unchecked (❌ False)
```

---

## Karta: ACTION_INVERT_BOOLEAN_FIELD / Toggle Checkbox

### Cel
Przełącza stan pola wyboru (zaznaczone → niezaznaczone i odwrotnie)

### Kiedy używać
- Przełączanie statusu zatwierdzenia
- Przełączanie trybu przetwarzania
- Odwracanie poprzedniego stanu
- Aktualizacja flag boolowskich

### Jak to działa
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

### Przykład
```
Invoice received with "Priority" checked
    ↓
After processing, invert "Priority" checkbox
    ↓
Checkbox now unchecked (no longer priority)
```

---

## Karta: ACTION_COPY_DOCFIELD_TO_DOCFIELD / Copy Field Value

### Cel
Kopiuje wartość z jednego pola do innego pola

### Kiedy używać
- Kopiowanie informacji o dostawcy do informacji rozliczeniowych
- Duplikowanie danych między polami
- Standaryzacja formatu danych
- Tworzenie kopii zapasowej wartości

### Jak to działa
```
Source Field: "Invoice_Supplier"  Value: "ABC Corp"
    ↓
COPY TO
    ↓
Target Field: "Billing_Partner"  Value: "ABC Corp"

Both fields now have same value
```

### Rzeczywiste przykłady

**Przykład 1: Kopiowanie adresu dostawy**
```
Source: "Delivery_Address" = "123 Main St, Berlin"
    ↓
Copy to: "Billing_Address"
    ↓
Result: Both fields show "123 Main St, Berlin"
```

**Przykład 2: Kopiowanie kodu dostawcy**
```
Source: "Supplier_Code_External" = "SUPP-789"
    ↓
Copy to: "Supplier_Code_Internal"
    ↓
Result: Both codes match, system recognizes supplier
```

**Przykład 3: Kopiowanie kwoty do walidacji**
```
Source: "Invoice_Total" = "€5000"
    ↓
Copy to: "Amount_to_Validate"
    ↓
Result: Validation field has correct amount
```

### Parametry
```
Source Field: [Choose field to copy FROM]
Target Field: [Choose field to copy TO]
```

### Uwagi
- Oryginalne pole pozostaje bez zmian
- Pole docelowe nadpisane wartością źródłową
- Dobre do standaryzacji danych

---

# Manipulacja tabelami

## Karta: EDIT_COLUMN / Edit Table Column

### Cel
Zmienia wartości w kolumnie tabeli na podstawie warunków

### Kiedy używać
- Naprawianie błędów cenowych w pozycjach
- Aktualizacja ilości
- Korygowanie opisów pozycji
- Standaryzacja wartości

### Jak to działa
```
Table Column: "Unit_Price"
Original Values: [100, 105, 103]
    ↓
FIND: Values matching condition
REPLACE: With new value
    ↓
Updated Column: [100, 110, 110] (example)
```

### Przykład: Naprawianie cen

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

### Parametry
```
Table: [Choose table]
Column: [Choose column to edit]
Find: [Value to find]
Replace with: [New value]
Condition: [When to apply]
```

### Typowe zastosowania
- Naprawianie cen jednostkowych
- Standaryzacja opisów
- Korygowanie ilości
- Aktualizacja numerów SKU

---

## Karta: CALC_COLUMNS / Calculate Column Values

### Cel
Wykonuje obliczenia na kolumnach tabeli i zapisuje wynik

### Kiedy używać
- Obliczanie sum pozycji (Qty × Unit Price)
- Sumowanie kolumn
- Obliczanie rabatów
- Obliczanie wartości procentowych

### Jak to działa
```
Column A (Quantity): 100
Column B (Unit Price): €50
    ↓
CALCULATE: A × B
    ↓
Column C (Line Total): €5000
```

### Typy obliczeń

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

**Typ 3: Obliczanie procentów**
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

### Rzeczywisty przykład

**Obliczenie pozycji faktury:**
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

### Parametry
```
Table: [Select table]
Column 1: [First column]
Operator: [×, +, -, ÷, %]
Column 2: [Second column] (if needed)
Result Column: [Where to put answer]
```

---

## Karta: CALC_COLUMNS_REGEX / Calculate with Regex Pattern

### Cel
Oblicza wartości kolumn na podstawie dopasowania wzorca

### Kiedy używać
- Ekstrakcja wartości z tekstu przy użyciu wzorców
- Formatowanie danych na podstawie reguł
- Konwersja wartości na podstawie wzorców
- Parsowanie tekstu strukturalnego

### Jak to działa

**Dopasowywanie wzorca regex:**
```
Original Value: "ABC-12345-XYZ"
Pattern: Extract numbers only
Calculation: Convert to "12345"
Result: "12345"
```

### Przykład: Ekstrakcja kodu dostawcy

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

### Przykład: Formatowanie numerów telefonów

**Scenariusz: Niesformatowane numery telefonów**
```
Original: "491234567890"
Pattern: Format as: +49 123 4567 890
Result: "+49 123 4567 890"
```

### Przykład: Ekstrakcja cen z tekstu

**Scenariusz: Ceny w formacie tekstowym**
```
Original: "Price is 99.99 EUR"
Pattern: Extract number only
Result: "99.99"
```

### Parametry
```
Table: [Select table]
Column: [Column to analyze]
Regex Pattern: [Pattern to find]
Replacement: [What to replace with]
Result Column: [Where to store result]
```

### Typowe wzorce regex
```
Numbers only: [0-9]+
Letters only: [a-zA-Z]+
First word: ^\w+
Extract €: €(\d+\.\d{2})
Date format: \d{4}-\d{2}-\d{2}
```

---

# Przykłady obliczeń

## Przykład 1: Obliczanie sumy faktury
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

## Przykład 2: Obliczanie odchylenia
```
PO Price: €100
Invoice Price: €103

Variance = |(Invoice - PO)| / PO × 100
Variance = |3| / 100 × 100 = 3%

Store in "Price_Variance%" column
```

## Przykład 3: Zastosowanie rabatu
```
Original Price: €100
Discount %: 10%
Discount Amount: €100 × 0.10 = €10
Final Price: €100 - €10 = €90
```

---

# Przykład przepływu pracy manipulacji polami

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

---

# Najlepsze praktyki

✅ **Rób:**
- Utrzymuj formuły proste
- Testuj obliczenia z przykładowymi danymi
- Weryfikuj, czy wyniki mają sens
- Dokumentuj, dlaczego zmieniasz pola
- Używaj kopiowania pola, gdy dane są takie same

❌ **Nie rób:**
- Nie twórz odniesień cyklicznych (A=B, B=A)
- Nie nadpisuj ważnych danych bez powodu
- Nie twórz nadmiernie złożonych wzorców regex
- Nie zapominaj o weryfikacji wyników obliczeń
- Nie obliczaj na niewłaściwej tabeli/kolumnach

---

# Rozwiązywanie problemów

## "Field not updating"
**Przyczyna:** Warunek niespełniony lub karta niewyzwolona

**Rozwiązanie:**
- Sprawdź, czy warunek jest prawdziwy
- Zweryfikuj, czy karta jest w przepływie pracy
- Przetestuj z przykładowymi danymi
- Sprawdź literówki w nazwie pola

## "Calculation result wrong"
**Przyczyna:** Wybrano niewłaściwe kolumny lub formuła jest nieprawidłowa

**Rozwiązanie:**
- Zweryfikuj kolumny źródłowe
- Sprawdź, czy formuła jest poprawna
- Przetestuj ręcznie
- Przejrzyj miejsca dziesiętne/zaokrąglanie

## "Table shows error"
**Przyczyna:** Przywoływana kolumna nie istnieje

**Rozwiązanie:**
- Zweryfikuj pisownię nazwy kolumny
- Sprawdź, czy kolumna ma dane
- Upewnij się, że typ danych kolumny jest zgodny z obliczeniem
- Dodaj brakujące kolumny w razie potrzeby

---

# Powiązane karty

- **ACTION_COPY_DOCFIELD_TO_DOCFIELD** - Kopiowanie wartości
- **EDIT_COLUMN** - Zmiana wartości tabeli
- **CALC_COLUMNS** - Obliczanie formuł
- **ACTION_SET_FIELD_TO_TEXT** - Ustawianie wartości tekstowych
- **ACTION_SET_BOOLEAN_FIELD** - Zaznaczanie pól wyboru
