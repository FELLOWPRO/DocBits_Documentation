# Karty dopasowania PO — kompletny przewodnik

## Karty dopasowania zamówienia zakupu (PO) — kompletny przewodnik

**Stan:** Obejmuje 15 kart porównania PO ze szczegółowymi obliczeniami

***

Karty porównania PO na tej stronie należą do grupy **And** w Workflow Builder — porównują dane faktury z dopasowanym zamówieniem zakupu, zanim uruchomią się akcje **Then**:

<figure><img src="../../../.gitbook/assets/workflow_designer_cards.png" alt="Płótno Workflow Builder z grupami kart When, And i Then"><figcaption><p>Karty porównania PO dodaje się do grupy <strong>And</strong> przez <strong>Add Card</strong>.</p></figcaption></figure>

***

### 📌 Informacje o wersji

**Najbardziej rozbudowana karta:** CONDITION\_DOC\_TO\_PO\_UNIT\_PRICE (5 wersji, najnowsza v5) **Inne złożone karty:** CONDITION\_OC\_TO\_PO\_ITEMS (v4), CONDITION\_LESS\_THAN\_TOLERANCE\_AS\_VALUE\_OF\_ORDERED\_QUANTITY (v4)

**Kluczowe wzorce:**

* **v2 → v3+:** Dodanie parametrów tolerancji dla elastycznego dopasowania
* **v3 → v4:** Dodanie parametrów trybu porównania
* **v4 → v5:** Rozszerzona tolerancja z wieloma jednostkami (%, EUR, $ itd.)

📖 [Pełna historia wersji](../release.md) | [Wersje i zachowanie kart](card-versions-guide.md)

***

### Zrozumienie dopasowania PO

Gdy otrzymujesz fakturę, powinna ona odpowiadać wcześniej złożonemu zamówieniu zakupu (PO). Karty dopasowania PO automatycznie sprawdzają, czy dane faktury zgadzają się z danymi PO.

**Ogólny obraz:**

```
PO Placed     Invoice Arrives     PO Matching     Decision
(€100)    →   (€103)          →   (Check if       → Approve/Reject
Qty: 100      Qty: 100            within tolerance)
```

<figure><img src="../../../.gitbook/assets/anatomy-po-matching.svg" alt="Izometryczna waga szalkowa: na lewej szalce leży cena jednostkowa z PO równa 100, na prawej cena jednostkowa z faktury równa 103 (100 plus niewielki dodatkowy odważnik). Belka się przechyla, a jej wskazówka znajduje się w zielonym pasie oznaczającym tolerancję 5%." width="768"><figcaption><p>Cena z PO (€100) leży na lewej szalce, a cena z faktury (€103) na prawej. Różnica €3 to 3% ceny z PO, więc wskazówka pozostaje w zielonym pasie tolerancji ±5% i kontrola przechodzi. Poza ±5% (kolor czerwony) faktura wymaga sprawdzenia.</p></figcaption></figure>

***

## 1. Pełne dopasowanie zamówienia zakupu

### Cel

Sprawdza, czy cała faktura odpowiada zamówieniu idealnie lub w granicach tolerancji

### Kiedy stosować

* Przed zatwierdzeniem faktury
* Jako wstępna kontrola jakości
* Aby wcześnie wykryć problemy

### Jak to działa

System porównuje:

* Ilości na fakturze z ilościami w PO
* Ceny na fakturze z cenami w PO
* Pozycje na fakturze z pozycjami w PO
* Sumę faktury z sumą PO

### Wynik

* **TRUE** (pełne dopasowanie): wszystko się zgadza, kontynuuj
* **FALSE** (niedopasowanie): coś się nie zgadza, wymaga sprawdzenia

### Przykład

```
PO:
- Item ABC: Qty 100, Unit Price €50 = €5000
- Item XYZ: Qty 50, Unit Price €20 = €1000
- Total: €6000

Invoice:
- Item ABC: Qty 100, Unit Price €50 = €5000
- Item XYZ: Qty 50, Unit Price €20 = €1000
- Total: €6000

Result: ✅ FULL MATCH
```

***

## 2. Porównanie ceny jednostkowej (dokument a PO)

### Cel

Porównuje cenę jednostkową na fakturze z ceną jednostkową w PO

### Parametry

* **Unit Price Tolerance**: dopuszczalne odchylenie do tej wartości
* **Tolerance Type**: procentowa (%) lub bezwzględna (€/$)
* **Operator**: równy, większy niż, mniejszy niż itd.

### Jak to działa (tolerancja procentowa)

**Wzór:**

```
Variance % = |(Invoice Price - PO Price)| / PO Price × 100

Check: Is Variance % ≤ Tolerance %?
```

**Przykład krok po kroku:**

```
Step 1: Get prices
  PO Unit Price: €100.00
  Invoice Unit Price: €103.00

Step 2: Calculate difference
  Difference = |€103.00 - €100.00| = €3.00

Step 3: Calculate percentage
  Percentage = (€3.00 / €100.00) × 100 = 3%

Step 4: Check tolerance (5% allowed)
  Is 3% ≤ 5%? YES ✅

Result: PASS - Within tolerance
```

### Przykłady z praktyki

#### Przykład 1: niewielki wzrost (akceptowany)

```
PO Price: €50.00
Invoice Price: €51.50
Tolerance: ±3%

Calculation:
  Variance = |(€51.50 - €50.00)| / €50.00 × 100
  Variance = €1.50 / €50.00 × 100 = 3%

Is 3% ≤ 3%? YES ✅ ACCEPT
```

#### Przykład 2: duży wzrost (odrzucony)

```
PO Price: €50.00
Invoice Price: €55.00
Tolerance: ±3%

Calculation:
  Variance = |(€55.00 - €50.00)| / €50.00 × 100
  Variance = €5.00 / €50.00 × 100 = 10%

Is 10% ≤ 3%? NO ❌ REJECT - NEEDS REVIEW
```

#### Przykład 3: rabat (też sprawdzany)

```
PO Price: €100.00
Invoice Price: €97.00
Tolerance: ±5%

Calculation:
  Variance = |(€97.00 - €100.00)| / €100.00 × 100
  Variance = €3.00 / €100.00 × 100 = 3%

Is 3% ≤ 5%? YES ✅ ACCEPT (Discount is within tolerance)
```

#### Przykład 4: tolerancja bezwzględna

```
PO Price: €10.00
Invoice Price: €10.50
Tolerance: ±€1.00 (absolute, not %)

Calculation:
  Variance = |€10.50 - €10.00| = €0.50

Is €0.50 ≤ €1.00? YES ✅ ACCEPT
```

### Co zrobić z wynikami

**Jeśli PASS ✅:**

* Przejdź do następnej kontroli
* Albo zatwierdź fakturę
* Albo kontynuuj eksport

**Jeśli FAIL ❌:**

* Oznacz do ręcznego sprawdzenia
* Poproś dostawcę o wyjaśnienie
* Skontaktuj się z działem zakupów
* Zatwierdź z notatką, jeśli to akceptowalne

***

## 3. Porównanie ilości

### Cel

Sprawdza, czy zamówiona ilość odpowiada ilości zafakturowanej

### Parametry

* **Tolerance**: dopuszczalna różnica kwotowa lub procentowa
* **Operator**: równa, większa niż, mniejsza niż
* **Quantity Type**: Ordered, Received, Open

### Przykład obliczenia

**Tolerancja procentowa:**

```
Formula:
  Quantity Variance % = |(Invoice Qty - PO Qty)| / PO Qty × 100

Example:
  PO Quantity: 100 units
  Invoice Quantity: 103 units
  Tolerance: ±5%

  Variance = |(103 - 100)| / 100 × 100
  Variance = 3 / 100 × 100 = 3%

  Is 3% ≤ 5%? YES ✅ ACCEPT
```

**Tolerancja bezwzględna:**

```
Formula:
  Quantity Variance = |Invoice Qty - PO Qty|

Example:
  PO Quantity: 100 units
  Invoice Quantity: 102 units
  Tolerance: ±5 units

  Variance = |102 - 100| = 2 units

  Is 2 units ≤ 5 units? YES ✅ ACCEPT
```

### Scenariusze z praktyki

#### Naddostawa (więcej niż zamówiono)

```
Ordered: 100 units
Invoiced: 110 units
Tolerance: ±5%

Variance = |(110-100)|/100 × 100 = 10%

Is 10% ≤ 5%? NO ❌

Decision: Contact supplier - more delivered than ordered
Possible reason: Error by supplier, partial shipment already received
```

#### Niedostawa (mniej niż zamówiono)

```
Ordered: 100 units
Invoiced: 95 units
Tolerance: ±5%

Variance = |(95-100)|/100 × 100 = 5%

Is 5% ≤ 5%? YES ✅

Decision: Accept - within tolerance
Possible reason: Partial shipment, rest to follow
```

***

## 4. Łączna cena różnicy ilości

### Cel

Gdy ilość się różni, oblicza, czy różnica łącznej ceny jest akceptowalna

### Dlaczego to ważne

```
Scenario: You ordered 100 units but received 110
- Quantity is 10% over (bad)
- BUT: You're only charged for 10% extra
- Combined effect might be acceptable
```

### Obliczenie

**Wzór:**

```
Combined Variance = Quantity Variance × Price Variance

If both are within tolerance, combined is usually acceptable
```

**Przykład:**

```
PO:
- Unit Price: €100
- Quantity: 100
- Total: €10,000

Invoice:
- Unit Price: €102 (2% higher)
- Quantity: 105 (5% higher)
- Total: €10,710

Analysis:
- Price variance: 2% ✅
- Quantity variance: 5% ✅
- Combined effect: 1.02 × 1.05 = 1.071 = 7.1% total increase

Is combined variance acceptable? Usually YES ✅
```

***

## 5. Porównanie identyfikatora pozycji / numeru pozycji dostawcy

### Cel

Sprawdza, czy pozycje na fakturze odpowiadają pozycjom w PO

### Jak to działa

**Dokładne dopasowanie (najprostsze):**

```
PO Item ID: ABC-123
Invoice Item ID: ABC-123
Result: ✅ MATCH
```

**Numer pozycji dostawcy (częstszy przypadek):**

```
PO Item: ABC-123 (Our internal code)
Supplier Item: SUPP-456 (Their code for same item)
System matches these as same item
Result: ✅ MATCH
```

### Scenariusz: co, jeśli się nie zgadza?

```
PO Item: ABC-123 (Copper Wire, 2mm)
Invoice Item: ABC-124 (Steel Wire, 2mm)

Result: ❌ NO MATCH

Actions:
1. Is this a substitution? Check with procurement
2. Is this an error? Contact supplier
3. Is the description similar? Verify manually
```

***

## 6. Weryfikacja typu zamówienia

### Cel

Sprawdza, czy typ zamówienia zakupu jest prawidłowy

### Typy zamówień

* **Standard Order**: zwykły zakup
* **Rush Order**: pilny, może mieć dopłatę
* **Frame Agreement**: umowa długoterminowa
* **Blanket Order**: umowa bez określonego końca
* **Consignment**: płacisz dopiero po zużyciu

### Przykład kontroli

```
PO Order Type: Standard Order
Invoice Order Type: Standard Order
Result: ✅ MATCH

If mismatch: Could affect terms, payment, pricing
```

***

## 7. Weryfikacja daty dostawy

### Cel

Sprawdza, czy data dostawy odpowiada obiecanej dacie w PO

### Obliczenie

**Opóźniona dostawa:**

```
Formula:
  Days Late = Invoice Delivery Date - PO Promised Date

Example:
  PO Promised: 2025-10-15
  Actual Delivery: 2025-10-22
  Days Late = 7 days

If tolerance is ±3 days:
  Is 7 ≤ 3? NO ❌ LATE
```

**Wcześniejsza dostawa:**

```
Formula:
  Days Early = PO Promised Date - Invoice Delivery Date

Example:
  PO Promised: 2025-10-15
  Actual Delivery: 2025-10-10
  Days Early = 5 days

Early delivery is usually OK ✅
Unless you need it at specific time
```

### Ustawienia tolerancji

```
±3 days: Allow 3 days late or early
±5 days: Allow up to 5 days variance
0 days: Must match exactly
```

***

## 8. Weryfikacja opłat (podatki, wysyłka itd.)

### Cel

Sprawdza, czy dodatkowe opłaty (podatki, wysyłka, obsługa) odpowiadają PO

### Typowe opłaty

```
- Shipping: €50
- Handling: €10
- Packaging: €5
- Insurance: €15
- Taxes: €300
```

### Obliczenie

**Przykład: kontrola opłaty za wysyłkę**

```
PO Shipping: €50.00
Invoice Shipping: €51.00
Tolerance: ±3%

Variance = |€51.00 - €50.00| / €50.00 × 100 = 2%

Is 2% ≤ 3%? YES ✅ ACCEPT
```

**Przykład: wiele opłat**

```
PO Total Charges:
  - Shipping: €50
  - Taxes: €300
  - Handling: €10
  Total: €360

Invoice Total Charges:
  - Shipping: €50
  - Taxes: €312 (11% tax)
  - Handling: €10
  Total: €372

Difference: €12
Check if within tolerance ✅ or ❌
```

***

## 9. Weryfikacja podatku

### Cel

Sprawdza, czy kwoty podatku są obliczone poprawnie

### Obliczenie

**Wzór:**

```
Tax Amount = Subtotal × Tax Rate

Example:
  Subtotal: €1000
  Tax Rate: 19%
  Expected Tax: €1000 × 0.19 = €190

Invoice Tax: €190
Match? YES ✅
```

**Typowe problemy:**

```
1. Tax rate changed (region-based)
2. Tax applied to wrong amount (before/after discounts)
3. Multiple tax rates (some items 7%, others 19%)
4. Tax exempt items (0% tax)
```

**Przykład: podatek według wielu stawek**

```
Item A: €100 @ 19% tax = €119
Item B: €100 @ 7% tax = €107
Item C: €100 @ 0% tax = €100
Total: €326

Invoice shows €325 (€1 error)

Check: Within tolerance or needs attention?
```

***

## 10. Dopasowanie zakładu / centrum kosztów

### Cel

Zapewnia, że faktura dotyczy właściwego zakładu / centrum kosztów

### Przykład

```
PO is for:
- Facility: Berlin Plant
- Cost Center: CC-2025

Invoice should have:
- Facility: Berlin Plant ✅
- Cost Center: CC-2025 ✅

If different facility: May need different approval
```

***

## 11. Weryfikacja statusu dostawcy

### Cel

Sprawdza, czy dostawca jest nadal zatwierdzony i aktywny

### Typy statusów

```
✅ ACTIVE: Approved, can do business
⚠️ ON HOLD: Temporarily blocked
❌ INACTIVE: No longer doing business
⚠️ CONDITIONAL: Only for specific items
```

### Przykład kontroli

```
Supplier: ABC Corp
Status in Database: ACTIVE
Status when creating PO: ACTIVE
Status when invoice arrives: INACTIVE

Alert: Supplier status changed! Investigate why.
```

***

## Jaką tolerancję wybrać?

### Tolerancje ścisłe (niższe ryzyko, więcej pracy ręcznej)

```
Use for:
- High-value items
- Items where exactness matters
- Regulated industries

Settings:
- Unit Price: ±1%
- Quantity: ±1%
- Delivery Date: ±1 day
- Charges: ±1%
```

### Tolerancje umiarkowane (zrównoważone)

```
Use for:
- Most business transactions
- Standard items
- Normal purchasing

Settings:
- Unit Price: ±3-5%
- Quantity: ±3-5%
- Delivery Date: ±3 days
- Charges: ±5%
```

### Tolerancje luźne (wyższe ryzyko, mniej pracy ręcznej)

```
Use for:
- Low-value items
- Bulk purchases
- Supplier agreements with flexibility

Settings:
- Unit Price: ±10%
- Quantity: ±10%
- Delivery Date: ±7 days
- Charges: ±10%
```

***

## Przykład przepływu dopasowania PO

```
Invoice Arrives
    ↓
Condition: "Is amount > €5000?" → YES
    ↓
Check: Full Match? → NO (10% price difference)
    ↓
Check: Unit Price within 5%? → NO (12% difference)
    ↓
Check: Quantity within 5%? → YES (2% difference)
    ↓
Decision: FAIL - Price variance too high
    ↓
Flag for: Manual review / Buyer approval
    ↓
Wait for: Buyer comment
    ↓
If Approved: Continue to Export
If Rejected: Return to Supplier
```

***

## Rozwiązywanie problemów z dopasowaniem PO

### „Nie znaleziono PO”

```
Cause: Invoice PO number doesn't exist in system
Fix:
1. Verify PO number spelling
2. Check if PO was created
3. Verify PO is in correct organization
4. Ask supplier for PO reference
```

### „Pozycje się nie zgadzają”

```
Cause: Invoice items are different from PO items
Possible Reasons:
1. Substitution approved by procurement
2. Different item numbers for same item
3. Error by supplier
Fix: Contact procurement or supplier
```

### „Cena wyższa niż w PO”

```
Cause: Invoice price > PO price
Possible Reasons:
1. Price increase approved
2. Supplier error
3. Currency difference
4. Additional services included
Fix: Verify with procurement
```

### „Nieprawidłowa data dostawy”

```
Cause: Invoice dated after promised delivery
Possible Reasons:
1. Shipment was delayed
2. Receiving date different from invoice date
3. Partial shipment
Fix: Check shipping documents or contact supplier
```

***

## Tabela podsumowująca

| Karta          | Co sprawdza           | Główne obliczenie       | Typowa tolerancja |
| -------------- | --------------------- | -------------------- | ---------------- |
| Full Match     | Wszystko              | Wszystkie kontrole      | Różna             |
| Unit Price     | Cena za jednostkę     | różnica % lub €         | ±3-5%             |
| Quantity       | Zamówiona ilość       | różnica % lub jednostek | ±3-5%             |
| Combined Price | Suma ze zmianą ilości | Ilość × cena            | ±5-10%            |
| Item ID        | Właściwe pozycje      | dopasowanie tekstu      | Dokładnie         |
| Order Type     | Typ zakupu            | dopasowanie tekstu      | Dokładnie         |
| Delivery Date  | Kiedy dotarło         | różnica dni             | ±3 dni            |
| Charges        | Dodatkowe opłaty      | różnica % lub €         | ±5%               |
| Tax            | Kwota podatku         | obliczenie % podatku    | ±1%               |
| Facility       | Centrum kosztów       | dopasowanie tekstu      | Dokładnie         |
| Supplier       | Zatwierdzony?         | kontrola statusu        | Tylko aktywny     |

***

## Powiązana dokumentacja

* Pełny przepływ pracy znajdziesz w przewodniku „Invoice Validation”.
* Zalecane wartości tolerancji według branż znajdziesz w „Tolerance Settings”.
* Co robić w przypadku niepowodzeń, opisuje „Exception Handling”.
* W sprawie konkretnych zasad tolerancji skontaktuj się z zespołem zakupów.

<!-- workflow-card-example-condition_promised_delivery_date_to_current-20261021 -->

### Obiecana data dostawy a data referencyjna

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-card-extra-ca4dcfa998e7-pl.png" alt="Pola karty w wyświetlanej wersji. Symbole zastępcze nie są skonfigurowane." width="563"><figcaption><p>Pola karty w wyświetlanej wersji. Symbole zastępcze nie są skonfigurowane.</p></figcaption></figure>

`CONDITION_PROMISED_DELIVERY_DATE_TO_CURRENT` · wersja 2

Załóż datę referencyjną `2026-10-21` i obiecaną datę dostawy pozycji `2026-10-23`. Wybierz porównanie „późniejsza niż” i zerową tolerancję dni. Przyszła data spełnia to porównanie; `2026-10-20` nie spełnia. Świadomie skonfiguruj opcje Any/All i dopuszczalne dni tolerancji, a brakującą datę przetestuj osobno.

<!-- workflow-card-example-condition_po_extracted_table_column-20261021 -->

### Kolumna zamówienia zakupu a wyodrębniona kolumna

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-card-extra-e2c12dd67cc0-pl.png" alt="Pola karty w wyświetlanej wersji. Symbole zastępcze nie są skonfigurowane." width="563"><figcaption><p>Pola karty w wyświetlanej wersji. Symbole zastępcze nie są skonfigurowane.</p></figcaption></figure>

`CONDITION_PO_EXTRACTED_TABLE_COLUMN` · wersja 2

Porównaj dopasowaną kolumnę artykułu PO z wyodrębnioną kolumną `article_number`, używając operatora równości i opcji All. Dopasowane wartości `DEMO-A` przechodzą; wyodrębniona wartość `DEMO-B` nie przechodzi. Tabelę przeglądową wybierz tylko wtedy, gdy potrzebna jest udokumentowana zamiana identyfikatora na wartość; przed porównaniem sprawdź to mapowanie.

<!-- workflow-card-example-condition_check_facility_in_po-20261021 -->

### Dozwolone zakłady w zamówieniu zakupu

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-card-extra-813ff783b1f2-pl.png" alt="Pola karty w wyświetlanej wersji. Symbole zastępcze nie są skonfigurowane." width="563"><figcaption><p>Pola karty w wyświetlanej wersji. Symbole zastępcze nie są skonfigurowane.</p></figcaption></figure>

`CONDITION_CHECK_FACILITY_IN_PO` · wersja 2

Wybierz opcję All, porównanie „jest w” i skonfigurowany kod zakładu `DEMO-NORTH`. Dopasowane pozycje PO w tym zakładzie przechodzą; pozycja w `DEMO-SOUTH` nie przechodzi. Używaj kodów zakładów z danych PO, a nie zakładaj, że etykieta wyświetlana jest kodem.

<!-- workflow-card-example-condition_purchase_order_full_match-20261021 -->

### Pełne dopasowanie zamówienia zakupu

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-card-extra-91a5b2a70e88-pl.png" alt="Pola karty w wyświetlanej wersji. Symbole zastępcze nie są skonfigurowane." width="563"><figcaption><p>Pola karty w wyświetlanej wersji. Symbole zastępcze nie są skonfigurowane.</p></figcaption></figure>

`CONDITION_PURCHASE_ORDER_FULL_MATCH` · wersja 2

Użyj całkowicie dopasowanej faktury demonstracyjnej i PO z ilością `2` i ceną jednostkową `100` po obu stronach oraz skonfigurowanymi tolerancjami ilości i ceny. Wybierz warunek pełnego dopasowania: przechodzi. Następnie przetestuj cenę poza skonfigurowaną tolerancją. Brakujące dane porównania lub brak PO nie są udanym pełnym dopasowaniem. Dowód dostawy ma porównanie tylko ilościowe; nie zakładaj, że obowiązują go reguły cen faktury.

<!-- workflow-card-example-condition_po_update_empty_column_check-20261021 -->

### Pusta kolumna bazy danych zamówienia zakupu

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-card-extra-f20345d72edd-pl.png" alt="Pola karty w wyświetlanej wersji. Symbole zastępcze nie są skonfigurowane." width="563"><figcaption><p>Pola karty w wyświetlanej wersji. Symbole zastępcze nie są skonfigurowane.</p></figcaption></figure>

`CONDITION_PO_UPDATE_EMPTY_COLUMN_CHECK` · wersja 2

Wybierz prawidłową tabelę PO i kolumnę oferowaną przez kartę oraz operator „jest pusty”. Dla istniejącego pasującego rekordu PO z pustą wartością warunek przechodzi; wypełniona wartość nie przechodzi. Najpierw sprawdź odwołanie do PO oraz mapowanie tabeli i kolumny. Wartość logiczna `false` jest nadal obecną wartością logiczną; brakujący rekord PO to odrębny błąd danych.

<!-- workflow-card-example-condition_compare_unit_price_percent_per-20261021 -->

### Tolerancja procentowa według podstawy ceny

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-card-extra-14ec95131dfc-pl.png" alt="Pola karty w wyświetlanej wersji. Symbole zastępcze nie są skonfigurowane." width="563"><figcaption><p>Pola karty w wyświetlanej wersji. Symbole zastępcze nie są skonfigurowane.</p></figcaption></figure>

`CONDITION_COMPARE_UNIT_PRICE_PERCENT_PER` · wersja 2

Przykład: cena jednostkowa PO `200`, cena bazowa `100` i skonfigurowana tolerancja `1` dają efektywną stawkę `(200 / 100) * (1 / 100) = 0.02`, czyli `2%`. Pasmo porównania to `196–204`. Równość w granicach tolerancji akceptuje cenę dokumentu `203` i odrzuca `210`. Nie zakładaj, że ta karta odpowiada stałej tolerancji 1%.

<!-- workflow-card-example-condition_compare_po_line_value-20261021 -->

### Wartość pozycji zamówienia zakupu a wartość odniesienia

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-card-extra-43a5d2686fb7-pl.png" alt="Pola karty w wyświetlanej wersji. Symbole zastępcze nie są skonfigurowane." width="563"><figcaption><p>Pola karty w wyświetlanej wersji. Symbole zastępcze nie są skonfigurowane.</p></figcaption></figure>

`CONDITION_COMPARE_PO_LINE_VALUE` · wersja 2

Wybierz dopasowaną kolumnę PO `item_number`, operator równości i wartość `DEMO-A`. Pozycja z wartością `DEMO-A` przechodzi; `DEMO-B` nie przechodzi. Używaj tylko operatorów obsługiwanych dla wybranego typu danych, a brakujące dane dopasowanej pozycji przetestuj osobno.
